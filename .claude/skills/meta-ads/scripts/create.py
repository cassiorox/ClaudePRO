#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Criar objetos (campaigns, adsets, ads, creatives, audiences)
Todas as criações defaultam para status=PAUSED.
"""
import os, sys, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (init_api, resolve_account, print_json, handle_fb_error,
                 print_error, parse_fields, parse_json_arg, add_account_arg,
                 add_fields_arg, safe_delay)

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.customaudience import CustomAudience


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_campaign(args):
    """⚠️ WRITE — Cria campanha (status PAUSED por padrao).

    Objetivos: OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_ENGAGEMENT,
    OUTCOME_AWARENESS, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION
    Orcamento em centavos: 5000 = R$50,00
    """
    init_api()
    account_id = resolve_account(args.account)

    params = {
        'name': args.name,
        'objective': args.objective,
        'status': args.status or 'PAUSED',
        'special_ad_categories': [args.special_ad_categories] if args.special_ad_categories != 'NONE' else [],
        'buying_type': args.buying_type or 'AUCTION',
    }
    if args.daily_budget:
        params['daily_budget'] = args.daily_budget
    if args.lifetime_budget:
        params['lifetime_budget'] = args.lifetime_budget
    if args.bid_strategy:
        params['bid_strategy'] = args.bid_strategy
    if args.start_time:
        params['start_time'] = args.start_time
    if args.stop_time:
        params['stop_time'] = args.stop_time
    if args.spend_cap:
        params['spend_cap'] = args.spend_cap

    account = AdAccount(account_id)
    result = account.create_campaign(params=params)
    safe_delay(1)

    print(f"Criado campaign com ID: {result['id']} (status: {params['status']})", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_adset(args):
    """⚠️ WRITE — Cria ad set (status PAUSED por padrao).

    Requer: campaign_id, optimization_goal, targeting (JSON), billing_event.
    Orcamento em centavos: daily_budget 5000 = R$50,00/dia
    """
    init_api()
    account_id = resolve_account(args.account)

    targeting = parse_json_arg(args.targeting, '--targeting')
    if not targeting:
        print_error("--targeting e obrigatorio (JSON string)")
        sys.exit(1)

    params = {
        'name': args.name,
        'campaign_id': args.campaign,
        'optimization_goal': args.optimization_goal,
        'billing_event': args.billing_event or 'IMPRESSIONS',
        'targeting': targeting,
        'status': args.status or 'PAUSED',
    }
    if args.daily_budget:
        params['daily_budget'] = args.daily_budget
    if args.lifetime_budget:
        params['lifetime_budget'] = args.lifetime_budget
    if args.bid_amount:
        params['bid_amount'] = args.bid_amount
    if args.bid_strategy:
        params['bid_strategy'] = args.bid_strategy
    if args.start_time:
        params['start_time'] = args.start_time
    if args.end_time:
        params['end_time'] = args.end_time
    if args.promoted_object:
        params['promoted_object'] = parse_json_arg(args.promoted_object, '--promoted-object')
    if args.destination_type:
        params['destination_type'] = args.destination_type

    account = AdAccount(account_id)
    result = account.create_ad_set(params=params)
    safe_delay(1)

    print(f"Criado adset com ID: {result['id']} (status: {params['status']})", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_ad(args):
    """⚠️ WRITE — Cria ad (status PAUSED por padrao).

    Requer: adset_id, creative (JSON: {"creative_id":"123"}).
    """
    init_api()
    account_id = resolve_account(args.account)

    creative = parse_json_arg(args.creative, '--creative')
    if not creative:
        print_error("--creative e obrigatorio (JSON string, ex: '{\"creative_id\":\"123\"}')")
        sys.exit(1)

    params = {
        'name': args.name,
        'adset_id': args.adset,
        'creative': creative,
        'status': args.status or 'PAUSED',
    }
    if args.tracking_specs:
        params['tracking_specs'] = parse_json_arg(args.tracking_specs, '--tracking-specs')
    if args.conversion_domain:
        params['conversion_domain'] = args.conversion_domain
    if args.degrees_of_freedom_spec:
        params['degrees_of_freedom_spec'] = parse_json_arg(args.degrees_of_freedom_spec, '--degrees-of-freedom-spec')

    account = AdAccount(account_id)
    result = account.create_ad(params=params)
    safe_delay(1)

    print(f"Criado ad com ID: {result['id']} (status: {params['status']})", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_creative(args):
    """⚠️ WRITE — Cria criativo. Criativos sao IMUTAVEIS apos criacao.

    Para trocar url_tags de um criativo existente, use advanced.py swap-url-tags.
    """
    init_api()
    account_id = resolve_account(args.account)

    params = {'name': args.name}

    if args.instagram_user_id:
        params['instagram_user_id'] = args.instagram_user_id
    if args.object_story_spec:
        params['object_story_spec'] = parse_json_arg(args.object_story_spec, '--object-story-spec')
    if args.asset_feed_spec:
        params['asset_feed_spec'] = parse_json_arg(args.asset_feed_spec, '--asset-feed-spec')
    if args.url_tags:
        params['url_tags'] = args.url_tags
    if args.call_to_action_type:
        params['call_to_action_type'] = args.call_to_action_type
    if args.image_hash:
        params['image_hash'] = args.image_hash
    if args.image_url:
        params['image_url'] = args.image_url
    if args.video_id:
        params['video_id'] = args.video_id
    if args.link_url:
        params['link_url'] = args.link_url
    if args.title:
        params['title'] = args.title
    if args.body:
        params['body'] = args.body

    account = AdAccount(account_id)
    result = account.create_ad_creative(params=params)
    safe_delay(1)

    print(f"Criado creative com ID: {result['id']}", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_image(args):
    init_api()
    import requests
    import tempfile

    account_id = resolve_account(args.account)

    # Download image to temp file
    print("Baixando imagem...", file=sys.stderr)
    response = requests.get(args.url, stream=True)
    response.raise_for_status()

    # Determine extension from URL or content-type
    ext = '.jpg'
    content_type = response.headers.get('content-type', '')
    if 'png' in content_type or args.url.lower().endswith('.png'):
        ext = '.png'
    elif 'webp' in content_type or args.url.lower().endswith('.webp'):
        ext = '.webp'

    tmp = tempfile.NamedTemporaryFile(suffix=ext, delete=False)
    try:
        for chunk in response.iter_content(chunk_size=8192):
            tmp.write(chunk)
        tmp.close()

        params = {}
        if args.name:
            params['name'] = args.name

        account = AdAccount(account_id)
        result = account.create_ad_image(params=params, files={'filename': tmp.name})
        safe_delay(1)

        print(f"Imagem enviada com sucesso", file=sys.stderr)
        print_json(result)
    finally:
        os.unlink(tmp.name)


@handle_fb_error
def cmd_video(args):
    init_api()
    account_id = resolve_account(args.account)

    params = {'file_url': args.url}
    if args.name:
        params['name'] = args.name
    if args.title:
        params['title'] = args.title
    if args.description:
        params['description'] = args.description

    account = AdAccount(account_id)
    result = account.create_ad_video(params=params)
    safe_delay(1)

    print(f"Video enviado com ID: {result['id']}", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_custom_audience(args):
    init_api()
    account_id = resolve_account(args.account)

    params = {
        'name': args.name,
        'subtype': args.subtype or 'CUSTOM',
    }
    if args.description:
        params['description'] = args.description
    if args.customer_file_source:
        params['customer_file_source'] = args.customer_file_source

    account = AdAccount(account_id)
    result = account.create_custom_audience(params=params)
    safe_delay(1)

    print(f"Criado custom audience com ID: {result['id']}", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_lookalike(args):
    init_api()
    account_id = resolve_account(args.account)

    spec = parse_json_arg(args.spec, '--spec')
    if not spec:
        print_error("--spec e obrigatorio (JSON string, ex: '{\"country\":\"BR\",\"ratio\":0.01}')")
        sys.exit(1)

    params = {
        'name': args.name,
        'subtype': 'LOOKALIKE',
        'origin_audience_id': args.source,
        'lookalike_spec': spec,
    }

    account = AdAccount(account_id)
    result = account.create_custom_audience(params=params)
    safe_delay(1)

    print(f"Criado lookalike audience com ID: {result['id']}", file=sys.stderr)
    print_json(result)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Meta Ads - Criar objetos")
    sub = parser.add_subparsers(dest="command", required=True)

    # --- campaign ---
    p = sub.add_parser("campaign", help="Criar campanha")
    add_account_arg(p)
    p.add_argument("--name", required=True, help="Nome da campanha")
    p.add_argument("--objective", required=True,
                   help="Objetivo (OUTCOME_LEADS, OUTCOME_TRAFFIC, OUTCOME_SALES, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT)")
    p.add_argument("--status", default="PAUSED", help="Status (default: PAUSED)")
    p.add_argument("--special-ad-categories", default="NONE",
                   help="Categoria especial (NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS)")
    p.add_argument("--daily-budget", help="Orcamento diario em centavos (ex: 5000 = R$50)")
    p.add_argument("--lifetime-budget", help="Orcamento vitalicio em centavos")
    p.add_argument("--bid-strategy",
                   help="Estrategia de lance (LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP)")
    p.add_argument("--buying-type", default="AUCTION", help="Tipo de compra (default: AUCTION)")
    p.add_argument("--start-time", help="Data/hora de inicio (ISO 8601)")
    p.add_argument("--stop-time", help="Data/hora de fim (ISO 8601)")
    p.add_argument("--spend-cap", help="Limite de gasto em centavos")

    # --- adset ---
    p = sub.add_parser("adset", help="Criar ad set")
    add_account_arg(p)
    p.add_argument("--name", required=True, help="Nome do ad set")
    p.add_argument("--campaign", required=True, help="ID da campanha")
    p.add_argument("--optimization-goal", required=True,
                   help="Goal (LINK_CLICKS, IMPRESSIONS, REACH, LEAD_GENERATION, OFFSITE_CONVERSIONS, LANDING_PAGE_VIEWS)")
    p.add_argument("--billing-event", default="IMPRESSIONS", help="Evento de cobranca (default: IMPRESSIONS)")
    p.add_argument("--targeting", required=True, help="Targeting como JSON string")
    p.add_argument("--status", default="PAUSED", help="Status (default: PAUSED)")
    p.add_argument("--daily-budget", help="Orcamento diario em centavos")
    p.add_argument("--lifetime-budget", help="Orcamento vitalicio em centavos")
    p.add_argument("--bid-amount", help="Valor do lance em centavos")
    p.add_argument("--bid-strategy", help="Estrategia de lance")
    p.add_argument("--start-time", help="Data/hora de inicio (ISO 8601)")
    p.add_argument("--end-time", help="Data/hora de fim (ISO 8601)")
    p.add_argument("--promoted-object", help="Objeto promovido como JSON string")
    p.add_argument("--destination-type", help="Tipo de destino")

    # --- ad ---
    p = sub.add_parser("ad", help="Criar anuncio")
    add_account_arg(p)
    p.add_argument("--name", required=True, help="Nome do anuncio")
    p.add_argument("--adset", required=True, help="ID do ad set")
    p.add_argument("--creative", required=True, help='Creative como JSON (ex: \'{"creative_id":"123"}\')')
    p.add_argument("--status", default="PAUSED", help="Status (default: PAUSED)")
    p.add_argument("--tracking-specs", help="Tracking specs como JSON string")
    p.add_argument("--conversion-domain", help="Dominio de conversao")
    p.add_argument("--degrees-of-freedom-spec", help="Controle de format options como JSON string")

    # --- creative ---
    p = sub.add_parser("creative", help="Criar creative")
    add_account_arg(p)
    p.add_argument("--name", required=True, help="Nome do creative")
    p.add_argument("--instagram-user-id", help="ID da conta Instagram (obrigatorio para ads no Instagram)")
    p.add_argument("--object-story-spec", help="Object story spec como JSON string")
    p.add_argument("--asset-feed-spec", help="Asset feed spec como JSON string")
    p.add_argument("--url-tags", help="URL tags para tracking")
    p.add_argument("--call-to-action-type",
                   help="CTA (LEARN_MORE, SHOP_NOW, SIGN_UP, DOWNLOAD, GET_OFFER, SUBSCRIBE)")
    p.add_argument("--image-hash", help="Hash da imagem")
    p.add_argument("--image-url", help="URL da imagem")
    p.add_argument("--video-id", help="ID do video")
    p.add_argument("--link-url", help="URL do link")
    p.add_argument("--title", help="Titulo do creative")
    p.add_argument("--body", help="Texto do corpo")

    # --- image ---
    p = sub.add_parser("image", help="Upload de imagem")
    add_account_arg(p)
    p.add_argument("--url", required=True, help="URL da imagem para upload")
    p.add_argument("--name", help="Nome da imagem")

    # --- video ---
    p = sub.add_parser("video", help="Upload de video")
    add_account_arg(p)
    p.add_argument("--url", required=True, help="URL do video para upload")
    p.add_argument("--name", help="Nome do video")
    p.add_argument("--title", help="Titulo do video")
    p.add_argument("--description", help="Descricao do video")

    # --- custom-audience ---
    p = sub.add_parser("custom-audience", help="Criar custom audience")
    add_account_arg(p)
    p.add_argument("--name", required=True, help="Nome da audiencia")
    p.add_argument("--subtype", default="CUSTOM", help="Subtipo (default: CUSTOM)")
    p.add_argument("--description", help="Descricao da audiencia")
    p.add_argument("--customer-file-source",
                   help="Fonte (USER_PROVIDED_ONLY, PARTNER_PROVIDED_ONLY, BOTH_USER_AND_PARTNER_PROVIDED)")

    # --- lookalike ---
    p = sub.add_parser("lookalike", help="Criar lookalike audience")
    add_account_arg(p)
    p.add_argument("--name", required=True, help="Nome da audiencia")
    p.add_argument("--source", required=True, help="ID da audiencia de origem")
    p.add_argument("--spec", required=True, help='Spec como JSON (ex: \'{"country":"BR","ratio":0.01}\')')

    args = parser.parse_args()

    commands = {
        'campaign': cmd_campaign,
        'adset': cmd_adset,
        'ad': cmd_ad,
        'creative': cmd_creative,
        'image': cmd_image,
        'video': cmd_video,
        'custom-audience': cmd_custom_audience,
        'lookalike': cmd_lookalike,
    }

    fn = commands.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
