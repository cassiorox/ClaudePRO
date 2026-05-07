#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Operacoes Avancadas
Duplicacao de campanhas/adsets/ads, swap de url_tags, batch operations.
Funcionalidades que NAO existem no MCP original.

Uso: python3 advanced.py <subcomando> [args]
"""

import os
import sys
import json
import argparse
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_api, resolve_account, print_json, handle_fb_error,
    print_error, parse_json_arg, add_account_arg, safe_delay,
)


# ---------------------------------------------------------------------------
# Lazy SDK imports
# ---------------------------------------------------------------------------

def _sdk():
    from facebook_business.adobjects.adaccount import AdAccount
    from facebook_business.adobjects.campaign import Campaign
    from facebook_business.adobjects.adset import AdSet
    from facebook_business.adobjects.ad import Ad
    from facebook_business.adobjects.adcreative import AdCreative
    return {
        "AdAccount": AdAccount,
        "Campaign": Campaign,
        "AdSet": AdSet,
        "Ad": Ad,
        "AdCreative": AdCreative,
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _copy_creative_with_url_tags(account_id, source_creative_id, new_url_tags):
    """
    Cria um novo criativo identico ao original mas com url_tags diferentes.
    Retorna o ID do novo criativo.
    """
    S = _sdk()

    # Ler criativo original
    creative = S["AdCreative"](source_creative_id)
    fields = [
        "name", "object_story_spec", "asset_feed_spec", "url_tags",
        "call_to_action_type", "image_hash", "image_url", "video_id",
        "link_url", "title", "body",
    ]
    creative.api_get(fields=fields)
    data = creative.export_all_data()

    # Montar params do novo criativo
    params = {"name": f"{data.get('name', 'creative')} [url_tags_fix]"}

    if "object_story_spec" in data:
        params["object_story_spec"] = data["object_story_spec"]
    if "asset_feed_spec" in data:
        params["asset_feed_spec"] = data["asset_feed_spec"]

    # Campos simples
    for field in ["call_to_action_type", "image_hash", "image_url",
                  "video_id", "link_url", "title", "body"]:
        if field in data and data[field]:
            params[field] = data[field]

    # Aplicar novos url_tags
    params["url_tags"] = new_url_tags

    # Criar novo criativo
    account = S["AdAccount"](account_id)
    new_creative = account.create_ad_creative(params=params)
    return new_creative["id"]


# ---------------------------------------------------------------------------
# Subcomandos
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_swap_url_tags(args):
    """⚠️ WRITE — Troca url_tags de um ad existente.

    Criativos Meta sao imutaveis. Este comando cria um criativo novo identico
    com os url_tags corretos e faz swap atomico no ad.
    """
    init_api()
    S = _sdk()

    ad = S["Ad"](args.ad)
    ad.api_get(fields=["name", "creative", "adset_id"])
    ad_data = ad.export_all_data()

    creative_ref = ad_data.get("creative", {})
    creative_id = creative_ref.get("id") or creative_ref.get("creative_id")
    if not creative_id:
        print_error("Nao foi possivel encontrar o criativo do ad.")
        sys.exit(1)

    # Descobrir account ID a partir do ad
    adset = S["AdSet"](ad_data["adset_id"])
    adset.api_get(fields=["account_id"])
    account_id = f"act_{adset['account_id']}"

    print(f"Criando novo criativo com url_tags: {args.url_tags}", file=sys.stderr)
    new_creative_id = _copy_creative_with_url_tags(account_id, creative_id, args.url_tags)
    safe_delay(1)

    print(f"Atualizando ad {args.ad} para usar criativo {new_creative_id}", file=sys.stderr)
    ad.api_update(params={"creative": {"creative_id": new_creative_id}})
    safe_delay(1)

    # Ler ad atualizado
    ad.api_get(fields=["id", "name", "creative", "status"])
    result = ad.export_all_data()
    result["_new_creative_id"] = new_creative_id
    result["_url_tags_applied"] = args.url_tags
    print_json(result)


@handle_fb_error
def cmd_duplicate_ad(args):
    """⚠️ WRITE — Duplica ad (PAUSED) com opcao de novos url_tags.

    Preserva tracking_specs e conversion_domain do original.
    """
    init_api()
    S = _sdk()

    # Ler ad original
    ad = S["Ad"](args.id)
    ad.api_get(fields=["name", "creative", "adset_id", "status", "tracking_specs", "conversion_domain"])
    data = ad.export_all_data()

    target_adset = args.adset or data.get("adset_id")
    if not target_adset:
        print_error("Informe --adset para o novo ad.")
        sys.exit(1)

    # Descobrir account ID
    adset = S["AdSet"](target_adset)
    adset.api_get(fields=["account_id"])
    account_id = f"act_{adset['account_id']}"
    account = S["AdAccount"](account_id)

    # Resolver criativo
    creative_ref = data.get("creative", {})
    creative_id = creative_ref.get("id") or creative_ref.get("creative_id")

    if args.url_tags and creative_id:
        print(f"Criando novo criativo com url_tags: {args.url_tags}", file=sys.stderr)
        creative_id = _copy_creative_with_url_tags(account_id, creative_id, args.url_tags)
        safe_delay(1)

    # Criar novo ad
    params = {
        "name": args.name or f"{data.get('name', 'ad')} - Copy",
        "adset_id": target_adset,
        "creative": {"creative_id": creative_id},
        "status": "PAUSED",
    }
    if data.get("tracking_specs"):
        params["tracking_specs"] = data["tracking_specs"]
    if data.get("conversion_domain"):
        params["conversion_domain"] = data["conversion_domain"]

    new_ad = account.create_ad(params=params)
    safe_delay(1)

    print(f"Ad duplicado com ID: {new_ad['id']} (PAUSED)", file=sys.stderr)
    print_json({"id": new_ad["id"], "name": params["name"], "status": "PAUSED",
                "creative_id": creative_id, "url_tags": args.url_tags or "(original)"})


@handle_fb_error
def cmd_duplicate_adset(args):
    """⚠️ WRITE — Duplica ad set (PAUSED) para a mesma ou outra campanha.

    Copia: targeting, budgets, bid_strategy, optimization_goal, promoted_object.
    """
    init_api()
    S = _sdk()

    # Ler adset original
    adset = S["AdSet"](args.id)
    fields = [
        "name", "campaign_id", "optimization_goal", "billing_event",
        "targeting", "daily_budget", "lifetime_budget", "bid_amount",
        "bid_strategy", "start_time", "end_time", "promoted_object",
        "destination_type", "account_id", "status",
    ]
    adset.api_get(fields=fields)
    data = adset.export_all_data()

    account_id = f"act_{data['account_id']}"
    account = S["AdAccount"](account_id)
    target_campaign = args.campaign or data.get("campaign_id")

    # Montar params do novo adset
    params = {
        "name": args.name or f"{data.get('name', 'adset')} - Copy",
        "campaign_id": target_campaign,
        "status": "PAUSED",
    }

    # Copiar campos existentes
    copy_fields = [
        "optimization_goal", "billing_event", "targeting",
        "daily_budget", "lifetime_budget", "bid_amount", "bid_strategy",
        "promoted_object", "destination_type",
    ]
    for field in copy_fields:
        if field in data and data[field] is not None:
            params[field] = data[field]

    new_adset = account.create_ad_set(params=params)
    safe_delay(1)

    print(f"Ad set duplicado com ID: {new_adset['id']} (PAUSED)", file=sys.stderr)
    print_json({"id": new_adset["id"], "name": params["name"],
                "campaign_id": target_campaign, "status": "PAUSED"})


@handle_fb_error
def cmd_duplicate_campaign(args):
    """⚠️ WRITE — Duplica campanha inteira (PAUSED).

    --deep: duplica recursivamente todos os ad sets e ads (ACTIVE + PAUSED).
    Sem --deep: duplica so a campanha (sem ad sets/ads).
    """
    init_api()
    S = _sdk()

    # Ler campanha original
    campaign = S["Campaign"](args.id)
    fields = [
        "name", "objective", "special_ad_categories", "daily_budget",
        "lifetime_budget", "bid_strategy", "buying_type", "spend_cap",
        "account_id", "status",
    ]
    campaign.api_get(fields=fields)
    data = campaign.export_all_data()

    account_id = f"act_{data['account_id']}"
    account = S["AdAccount"](account_id)

    # Criar nova campanha
    params = {
        "name": args.name or f"{data.get('name', 'campaign')} - Copy",
        "status": "PAUSED",
    }
    copy_fields = [
        "objective", "special_ad_categories", "daily_budget",
        "lifetime_budget", "bid_strategy", "buying_type", "spend_cap",
    ]
    for field in copy_fields:
        if field in data and data[field] is not None:
            params[field] = data[field]

    new_campaign = account.create_campaign(params=params)
    new_campaign_id = new_campaign["id"]
    safe_delay(1)

    result = {
        "campaign": {"id": new_campaign_id, "name": params["name"], "status": "PAUSED"},
        "adsets": [],
        "ads": [],
    }

    print(f"Campanha duplicada com ID: {new_campaign_id} (PAUSED)", file=sys.stderr)

    # Deep copy: duplicar adsets e ads
    if args.deep:
        print("Duplicando ad sets e ads...", file=sys.stderr)
        adsets = campaign.get_ad_sets(
            fields=["id", "name", "optimization_goal", "billing_event", "targeting",
                    "daily_budget", "lifetime_budget", "bid_amount", "bid_strategy",
                    "promoted_object", "destination_type"],
            params={"effective_status": ["ACTIVE", "PAUSED"]},
        )
        for old_adset in adsets:
            old_data = old_adset.export_all_data()
            adset_params = {
                "name": old_data.get("name", "adset"),
                "campaign_id": new_campaign_id,
                "status": "PAUSED",
            }
            for f in ["optimization_goal", "billing_event", "targeting",
                       "daily_budget", "lifetime_budget", "bid_amount",
                       "bid_strategy", "promoted_object", "destination_type"]:
                if f in old_data and old_data[f] is not None:
                    adset_params[f] = old_data[f]

            new_adset = account.create_ad_set(params=adset_params)
            new_adset_id = new_adset["id"]
            safe_delay(1)

            adset_result = {"id": new_adset_id, "name": adset_params["name"], "ads": []}
            print(f"  Ad set duplicado: {new_adset_id}", file=sys.stderr)

            # Duplicar ads do adset
            ads = S["AdSet"](old_data["id"]).get_ads(
                fields=["id", "name", "creative", "tracking_specs", "conversion_domain"],
                params={"effective_status": ["ACTIVE", "PAUSED"]},
            )
            for old_ad in ads:
                ad_data = old_ad.export_all_data()
                creative_ref = ad_data.get("creative", {})
                creative_id = creative_ref.get("id") or creative_ref.get("creative_id")

                ad_params = {
                    "name": ad_data.get("name", "ad"),
                    "adset_id": new_adset_id,
                    "creative": {"creative_id": creative_id},
                    "status": "PAUSED",
                }
                if ad_data.get("tracking_specs"):
                    ad_params["tracking_specs"] = ad_data["tracking_specs"]

                new_ad = account.create_ad(params=ad_params)
                safe_delay(1)

                adset_result["ads"].append({"id": new_ad["id"], "name": ad_params["name"]})
                print(f"    Ad duplicado: {new_ad['id']}", file=sys.stderr)

            result["adsets"].append(adset_result)

    print_json(result)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads ClaudePRO - Operacoes Avancadas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Subcomando")

    # swap-url-tags
    p = sub.add_parser("swap-url-tags", help="Troca url_tags de um ad existente")
    p.add_argument("--ad", required=True, help="ID do ad")
    p.add_argument("--url-tags", required=True, help="Novos url_tags (ex: utm_source=facebook&utm_medium=cpc)")

    # duplicate-ad
    p = sub.add_parser("duplicate-ad", help="Duplica um ad")
    p.add_argument("--id", required=True, help="ID do ad original")
    p.add_argument("--adset", help="ID do ad set destino (padrao: mesmo do original)")
    p.add_argument("--name", help="Nome do novo ad")
    p.add_argument("--url-tags", help="Novos url_tags para o criativo duplicado")

    # duplicate-adset
    p = sub.add_parser("duplicate-adset", help="Duplica um ad set")
    p.add_argument("--id", required=True, help="ID do ad set original")
    p.add_argument("--campaign", help="ID da campanha destino (padrao: mesma do original)")
    p.add_argument("--name", help="Nome do novo ad set")

    # duplicate-campaign
    p = sub.add_parser("duplicate-campaign", help="Duplica uma campanha")
    p.add_argument("--id", required=True, help="ID da campanha original")
    p.add_argument("--name", help="Nome da nova campanha")
    p.add_argument("--deep", action="store_true", help="Duplicar tambem ad sets e ads")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "swap-url-tags": cmd_swap_url_tags,
        "duplicate-ad": cmd_duplicate_ad,
        "duplicate-adset": cmd_duplicate_adset,
        "duplicate-campaign": cmd_duplicate_campaign,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
