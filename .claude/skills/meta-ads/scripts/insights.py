#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Insights & Reporting
Subcommands: account, campaign, adset, ad, async

Parametros de insights disponiveis:
  --date-preset       Periodo relativo (today, yesterday, last_7d, last_30d, etc)
  --time-range        JSON com datas: '{"since":"2026-01-01","until":"2026-01-31"}'
  --time-ranges       JSON com multiplos periodos para comparacao
  --time-increment    Granularidade: 1-90 (dias), monthly, all_days
  --breakdowns        Segmentar por: age, gender, country, region, publisher_platform,
                      platform_position, device_platform, impression_device
  --action-breakdowns Segmentar acoes: action_type, action_device, action_destination
  --action-report-time Quando acoes contam: impression, conversion, mixed
  --action-attribution-windows  Janela de atribuicao: 1d_view, 7d_click, 28d_click, dda
  --filtering         JSON de filtros: '[{"field":"spend","operator":"GREATER_THAN","value":50}]'
  --sort              Ordenar: spend_descending, impressions_ascending, etc
  --level             Nivel de agregacao: account, campaign, adset, ad
  --default-summary   Incluir linha de resumo/totais
  --locale            Idioma dos resultados: pt_BR, en_US, etc
  --since / --until   Paginacao temporal (alternativa a time-range)
  --offset            Paginacao por offset numerico
"""

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_api,
    resolve_account,
    print_json,
    handle_fb_error,
    print_error,
    parse_fields,
    parse_json_arg,
    add_account_arg,
    add_fields_arg,
)

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

# ---------------------------------------------------------------------------
# Default fields
# ---------------------------------------------------------------------------

DEFAULT_INSIGHTS_FIELDS = [
    "impressions",
    "clicks",
    "spend",
    "cpc",
    "cpm",
    "ctr",
    "actions",
    "cost_per_action_type",
    "reach",
    "frequency",
]

DATE_PRESET_CHOICES = [
    "today",
    "yesterday",
    "this_month",
    "last_month",
    "this_quarter",
    "last_3d",
    "last_7d",
    "last_14d",
    "last_28d",
    "last_30d",
    "last_90d",
    "maximum",
]

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _add_insights_args(parser):
    """Add all common insight arguments to a subparser."""
    add_fields_arg(parser)

    # --- Time ---
    parser.add_argument(
        "--date-preset",
        default="last_30d",
        choices=DATE_PRESET_CHOICES,
        help="Date preset (default: last_30d)",
    )
    parser.add_argument(
        "--time-range",
        help='JSON: \'{"since":"2026-01-01","until":"2026-01-31"}\'',
    )
    parser.add_argument(
        "--time-ranges",
        help='JSON com multiplos periodos para comparacao: \'[{"since":"2026-01-01","until":"2026-01-31"},{"since":"2026-02-01","until":"2026-02-28"}]\'',
    )
    parser.add_argument(
        "--time-increment",
        default="all_days",
        help="Granularidade: 1-90 (dias), monthly, all_days (default: all_days)",
    )
    parser.add_argument(
        "--since",
        help="Data inicio para paginacao temporal (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--until",
        help="Data fim para paginacao temporal (YYYY-MM-DD)",
    )

    # --- Segmentation ---
    parser.add_argument(
        "--breakdowns",
        help="Segmentar por: age,gender,country,region,publisher_platform,platform_position,device_platform,impression_device",
    )
    parser.add_argument(
        "--level",
        choices=["account", "campaign", "adset", "ad"],
        help="Nivel de agregacao",
    )
    parser.add_argument(
        "--action-breakdowns",
        help="Segmentar acoes: action_type,action_device,action_destination,action_conversion_device",
    )

    # --- Attribution ---
    parser.add_argument(
        "--action-report-time",
        choices=["impression", "conversion", "mixed"],
        help="Quando acoes contam: impression, conversion, mixed",
    )
    parser.add_argument(
        "--action-attribution-windows",
        help="Janelas de atribuicao (CSV): 1d_view,7d_click,28d_click,dda,default",
    )
    parser.add_argument(
        "--use-account-attribution",
        action="store_true",
        help="Usar configuracao de atribuicao da conta",
    )
    parser.add_argument(
        "--use-unified-attribution",
        action="store_true",
        default=True,
        help="Usar atribuicao unificada (default: true)",
    )

    # --- Filtering & Sorting ---
    parser.add_argument(
        "--filtering",
        help='JSON: \'[{"field":"spend","operator":"GREATER_THAN","value":50}]\'',
    )
    parser.add_argument(
        "--sort",
        help="Ordenar: spend_descending, impressions_ascending, etc",
    )

    # --- Output ---
    parser.add_argument(
        "--default-summary",
        action="store_true",
        help="Incluir linha de resumo/totais nos resultados",
    )
    parser.add_argument(
        "--locale",
        help="Idioma dos resultados: pt_BR, en_US, es_ES, etc",
    )

    # --- Pagination ---
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Limite de resultados por pagina (default: 25)",
    )
    parser.add_argument(
        "--offset",
        type=int,
        help="Pular N resultados (paginacao por offset)",
    )
    parser.add_argument("--after", help="Cursor de paginacao (proxima pagina)")
    parser.add_argument("--before", help="Cursor de paginacao (pagina anterior)")


def _build_insights_params(args):
    """Build the params dict from parsed arguments.

    Logica de tempo:
      - time_range ou time_ranges tem prioridade sobre date_preset
      - since/until sao usados para paginacao temporal (se nao tiver time_range)
    """
    params = {}

    # --- Time ---
    time_range = getattr(args, "time_range", None)
    time_ranges = getattr(args, "time_ranges", None)
    since = getattr(args, "since", None)
    until_ = getattr(args, "until", None)

    if time_ranges:
        params["time_ranges"] = parse_json_arg(time_ranges, "time-ranges")
    elif time_range:
        params["time_range"] = parse_json_arg(time_range, "time-range")
    elif since or until_:
        if since:
            params["since"] = since
        if until_:
            params["until"] = until_
    elif args.date_preset:
        params["date_preset"] = args.date_preset

    if args.time_increment:
        params["time_increment"] = args.time_increment

    # --- Segmentation ---
    if args.breakdowns:
        params["breakdowns"] = args.breakdowns.split(",")
    if args.level:
        params["level"] = args.level
    if args.action_breakdowns:
        params["action_breakdowns"] = args.action_breakdowns.split(",")

    # --- Attribution ---
    action_report_time = getattr(args, "action_report_time", None)
    if action_report_time:
        params["action_report_time"] = action_report_time

    action_attr_windows = getattr(args, "action_attribution_windows", None)
    if action_attr_windows:
        params["action_attribution_windows"] = action_attr_windows.split(",")

    if getattr(args, "use_account_attribution", False):
        params["use_account_attribution_setting"] = True
    if getattr(args, "use_unified_attribution", False):
        params["use_unified_attribution_setting"] = True

    # --- Filtering & Sorting ---
    if args.filtering:
        params["filtering"] = parse_json_arg(args.filtering, "filtering")
    if args.sort:
        params["sort"] = [args.sort]

    # --- Output ---
    if getattr(args, "default_summary", False):
        params["default_summary"] = True
    locale = getattr(args, "locale", None)
    if locale:
        params["locale"] = locale

    # --- Pagination ---
    if args.limit:
        params["limit"] = args.limit
    offset = getattr(args, "offset", None)
    if offset is not None:
        params["offset"] = offset
    if getattr(args, "after", None):
        params["after"] = args.after
    if getattr(args, "before", None):
        params["before"] = args.before

    return params


def _resolve_fields(args):
    """Resolve fields from args or return defaults."""
    if args.fields:
        return parse_fields(args.fields)
    return list(DEFAULT_INSIGHTS_FIELDS)


# ---------------------------------------------------------------------------
# Post-processing
# ---------------------------------------------------------------------------

# Prefixos de acoes redundantes que a Meta retorna em duplicata
_REDUNDANT_PREFIXES = (
    "omni_",
    "onsite_web_app_",
    "onsite_web_",
    "onsite_app_",
    "web_app_in_store_",
    "offsite_conversion.fb_pixel_",
)


def _strip_redundant_actions(results):
    """Remove acoes redundantes dos insights (~60% menor).

    A Meta retorna a mesma acao com prefixos diferentes (omni_purchase,
    onsite_web_app_purchase, offsite_conversion.fb_pixel_purchase, etc).
    Mantemos apenas a acao canonica (ex: purchase, link_click).
    """
    action_fields = ("actions", "cost_per_action_type", "action_values")
    for row in results:
        if not hasattr(row, 'get'):
            continue
        for field in action_fields:
            actions = row.get(field)
            if not actions or not isinstance(actions, list):
                continue
            row[field] = [
                a for a in actions
                if not any(a.get("action_type", "").startswith(p) for p in _REDUNDANT_PREFIXES)
            ]
    return results


# Campos que estao em centavos na API
_BUDGET_FIELDS = (
    "daily_budget", "lifetime_budget", "budget_remaining",
    "spend_cap", "amount_spent", "balance",
)


def _format_monetary(results):
    """Converte campos de orcamento de centavos para reais (/ 100).

    Campos de insights como spend, cpc, cpm ja vem formatados pela API.
    Mas daily_budget, lifetime_budget, etc vem em centavos.
    """
    for row in results:
        if not hasattr(row, 'get'):
            continue
        for field in _BUDGET_FIELDS:
            val = row.get(field)
            if val is not None:
                try:
                    row[field] = f"{int(val) / 100:.2f}"
                except (ValueError, TypeError):
                    pass
    return results


def _postprocess(results):
    """Aplica compact mode e formatacao monetaria."""
    results = _strip_redundant_actions(results)
    results = _format_monetary(results)
    return results


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


@handle_fb_error
def cmd_account(args):
    """Account-level insights."""
    init_api()
    account_id = resolve_account(getattr(args, "id", None) or getattr(args, "account", None))
    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    account = AdAccount(account_id)
    cursor = account.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(_postprocess(results))


@handle_fb_error
def cmd_campaign(args):
    """Campaign-level insights."""
    init_api()
    if not args.id:
        print_error("--id e obrigatorio para insights de campanha.")
        sys.exit(1)

    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    campaign = Campaign(args.id)
    cursor = campaign.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(_postprocess(results))


@handle_fb_error
def cmd_adset(args):
    """Ad set-level insights."""
    init_api()
    if not args.id:
        print_error("--id e obrigatorio para insights de ad set.")
        sys.exit(1)

    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    adset = AdSet(args.id)
    cursor = adset.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(_postprocess(results))


@handle_fb_error
def cmd_ad(args):
    """Ad-level insights."""
    init_api()
    if not args.id:
        print_error("--id e obrigatorio para insights de ad.")
        sys.exit(1)

    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    ad = Ad(args.id)
    cursor = ad.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(_postprocess(results))


@handle_fb_error
def cmd_async(args):
    """Async report for heavy queries."""
    init_api()
    account_id = resolve_account(getattr(args, "id", None) or getattr(args, "account", None))
    fields = _resolve_fields(args)
    params = _build_insights_params(args)
    poll_interval = args.poll_interval

    account = AdAccount(account_id)
    report = account.get_insights_async(fields=fields, params=params)

    print(f"Async report criado: {report['id']}", file=sys.stderr)
    print(f"Aguardando conclusao (poll a cada {poll_interval}s)...", file=sys.stderr)

    while True:
        report = report.api_get()
        status = report.get("async_status", "Unknown")
        pct = report.get("async_percent_completion", 0)

        print(f"  Status: {status} ({pct}%)", file=sys.stderr)

        if status == "Job Completed":
            break
        if status in ("Job Failed", "Job Skipped"):
            print_error(f"Report falhou com status: {status}")
            sys.exit(1)

        time.sleep(poll_interval)

    print("Buscando resultados...", file=sys.stderr)
    cursor = report.get_result()
    results = [item for item in cursor]
    print_json(_postprocess(results))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Insights & Reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcomando")

    # account
    p_account = subparsers.add_parser("account", help="Account-level insights")
    p_account.add_argument("--id", help="Account ID (default: META_AD_ACCOUNT_ID)")
    add_account_arg(p_account)
    _add_insights_args(p_account)
    p_account.set_defaults(func=cmd_account)

    # campaign
    p_campaign = subparsers.add_parser("campaign", help="Campaign insights")
    p_campaign.add_argument("--id", required=True, help="Campaign ID")
    _add_insights_args(p_campaign)
    p_campaign.set_defaults(func=cmd_campaign)

    # adset
    p_adset = subparsers.add_parser("adset", help="Ad set insights")
    p_adset.add_argument("--id", required=True, help="Ad set ID")
    _add_insights_args(p_adset)
    p_adset.set_defaults(func=cmd_adset)

    # ad
    p_ad = subparsers.add_parser("ad", help="Ad insights")
    p_ad.add_argument("--id", required=True, help="Ad ID")
    _add_insights_args(p_ad)
    p_ad.set_defaults(func=cmd_ad)

    # async
    p_async = subparsers.add_parser("async", help="Async report (heavy queries)")
    p_async.add_argument("--id", help="Account ID (default: META_AD_ACCOUNT_ID)")
    add_account_arg(p_async)
    _add_insights_args(p_async)
    p_async.add_argument(
        "--poll-interval",
        type=int,
        default=5,
        help="Poll interval in seconds (default: 5)",
    )
    p_async.set_defaults(func=cmd_async)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
