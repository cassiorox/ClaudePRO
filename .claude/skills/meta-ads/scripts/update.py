#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Atualizar objetos (campaigns, adsets, ads, audience users)
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
    """⚠️ WRITE — Atualiza campanha. Ao ativar (--status ACTIVE), lembre de ativar
    tambem todos os ad sets e ads da campanha."""
    init_api()
    params = {}
    if args.name:
        params['name'] = args.name
    if args.status:
        params['status'] = args.status
    if args.daily_budget:
        params['daily_budget'] = args.daily_budget
    if args.lifetime_budget:
        params['lifetime_budget'] = args.lifetime_budget
    if args.bid_strategy:
        params['bid_strategy'] = args.bid_strategy
    if args.spend_cap:
        params['spend_cap'] = args.spend_cap
    if args.start_time:
        params['start_time'] = args.start_time
    if args.stop_time:
        params['stop_time'] = args.stop_time

    if not params:
        print_error("Nenhum campo para atualizar. Use --name, --status, --daily-budget, etc.")
        sys.exit(1)

    campaign = Campaign(args.id)
    campaign.api_update(params=params)
    safe_delay(1)

    result = campaign.api_get(fields=['id', 'name', 'status', 'daily_budget', 'lifetime_budget',
                                       'bid_strategy', 'start_time', 'stop_time'])
    print(f"Campaign {args.id} atualizada", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_adset(args):
    """⚠️ WRITE — Atualiza ad set (targeting, budget, status, etc).
    Orcamento em centavos: 5000 = R$50,00."""
    init_api()
    params = {}
    if args.name:
        params['name'] = args.name
    if args.status:
        params['status'] = args.status
    if args.daily_budget:
        params['daily_budget'] = args.daily_budget
    if args.lifetime_budget:
        params['lifetime_budget'] = args.lifetime_budget
    if args.targeting:
        params['targeting'] = parse_json_arg(args.targeting, '--targeting')
    if args.bid_amount:
        params['bid_amount'] = args.bid_amount
    if args.bid_strategy:
        params['bid_strategy'] = args.bid_strategy
    if args.optimization_goal:
        params['optimization_goal'] = args.optimization_goal
    if args.start_time:
        params['start_time'] = args.start_time
    if args.end_time:
        params['end_time'] = args.end_time

    if not params:
        print_error("Nenhum campo para atualizar. Use --name, --status, --daily-budget, etc.")
        sys.exit(1)

    adset = AdSet(args.id)
    adset.api_update(params=params)
    safe_delay(1)

    result = adset.api_get(fields=['id', 'name', 'status', 'daily_budget', 'lifetime_budget',
                                    'targeting', 'optimization_goal', 'bid_amount'])
    print(f"AdSet {args.id} atualizado", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_ad(args):
    """⚠️ WRITE — Atualiza ad (status, nome, criativo)."""
    init_api()
    params = {}
    if args.name:
        params['name'] = args.name
    if args.status:
        params['status'] = args.status
    if args.creative:
        params['creative'] = parse_json_arg(args.creative, '--creative')
    if args.tracking_specs:
        params['tracking_specs'] = parse_json_arg(args.tracking_specs, '--tracking-specs')

    if not params:
        print_error("Nenhum campo para atualizar. Use --name, --status, --creative, etc.")
        sys.exit(1)

    ad = Ad(args.id)
    ad.api_update(params=params)
    safe_delay(1)

    result = ad.api_get(fields=['id', 'name', 'status', 'adset_id', 'creative'])
    print(f"Ad {args.id} atualizado", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_audience_users(args):
    init_api()

    schema_list = [s.strip().upper() for s in args.schema.split(',')]
    data_list = parse_json_arg(args.data, '--data')
    if not data_list:
        print_error("--data e obrigatorio (JSON array de arrays)")
        sys.exit(1)

    audience = CustomAudience(args.id)

    if args.action == 'remove':
        result = audience.remove_users(schema=schema_list, users=data_list)
        print(f"Usuarios removidos da audience {args.id}", file=sys.stderr)
    else:
        result = audience.add_users(schema=schema_list, users=data_list)
        print(f"Usuarios adicionados a audience {args.id}", file=sys.stderr)

    safe_delay(1)
    print_json(result)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Meta Ads - Atualizar objetos")
    sub = parser.add_subparsers(dest="command", required=True)

    # --- campaign ---
    p = sub.add_parser("campaign", help="Atualizar campanha")
    p.add_argument("--id", required=True, help="ID da campanha")
    p.add_argument("--name", help="Novo nome")
    p.add_argument("--status", help="Novo status (ACTIVE, PAUSED, DELETED, ARCHIVED)")
    p.add_argument("--daily-budget", help="Orcamento diario em centavos")
    p.add_argument("--lifetime-budget", help="Orcamento vitalicio em centavos")
    p.add_argument("--bid-strategy", help="Estrategia de lance")
    p.add_argument("--spend-cap", help="Limite de gasto em centavos")
    p.add_argument("--start-time", help="Data/hora de inicio (ISO 8601)")
    p.add_argument("--stop-time", help="Data/hora de fim (ISO 8601)")

    # --- adset ---
    p = sub.add_parser("adset", help="Atualizar ad set")
    p.add_argument("--id", required=True, help="ID do ad set")
    p.add_argument("--name", help="Novo nome")
    p.add_argument("--status", help="Novo status (ACTIVE, PAUSED, DELETED, ARCHIVED)")
    p.add_argument("--daily-budget", help="Orcamento diario em centavos")
    p.add_argument("--lifetime-budget", help="Orcamento vitalicio em centavos")
    p.add_argument("--targeting", help="Targeting como JSON string")
    p.add_argument("--bid-amount", help="Valor do lance em centavos")
    p.add_argument("--bid-strategy", help="Estrategia de lance")
    p.add_argument("--optimization-goal", help="Goal de otimizacao")
    p.add_argument("--start-time", help="Data/hora de inicio (ISO 8601)")
    p.add_argument("--end-time", help="Data/hora de fim (ISO 8601)")

    # --- ad ---
    p = sub.add_parser("ad", help="Atualizar anuncio")
    p.add_argument("--id", required=True, help="ID do anuncio")
    p.add_argument("--name", help="Novo nome")
    p.add_argument("--status", help="Novo status (ACTIVE, PAUSED, DELETED, ARCHIVED)")
    p.add_argument("--creative", help='Creative como JSON (ex: \'{"creative_id":"123"}\')')
    p.add_argument("--tracking-specs", help="Tracking specs como JSON string")

    # --- audience-users ---
    p = sub.add_parser("audience-users", help="Adicionar/remover usuarios de custom audience")
    p.add_argument("--id", required=True, help="ID da custom audience")
    p.add_argument("--schema", required=True,
                   help="Schema separado por virgula (EMAIL, PHONE, FN, LN, etc.)")
    p.add_argument("--data", required=True,
                   help="Dados como JSON array de arrays (ex: '[[\"email1\",\"nome1\"],[\"email2\",\"nome2\"]]')")
    p.add_argument("--action", default="add", choices=["add", "remove"],
                   help="Acao (default: add)")

    args = parser.parse_args()

    commands = {
        'campaign': cmd_campaign,
        'adset': cmd_adset,
        'ad': cmd_ad,
        'audience-users': cmd_audience_users,
    }

    fn = commands.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
