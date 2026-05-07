#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Insights & Reporting (7 subcommands)
Subcommands: account, campaign, ad-group, keyword, daily, device, hourly

Parametros comuns:
  --customer-id    Customer ID (sem hifens)
  --date-range     Periodo: LAST_7_DAYS, LAST_30_DAYS, THIS_MONTH, etc
  --since/--until  Periodo especifico (YYYY-MM-DD)
  --campaign-id    Filtrar por campanha
  --limit          Limite de resultados
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import (
    init_client,
    resolve_customer_id,
    run_query,
    print_json,
    print_error,
    handle_google_error_decorator,
    add_customer_arg,
    add_date_args,
    add_limit_arg,
    add_campaign_filter,
    build_date_clause,
)


# ---------------------------------------------------------------------------
# 1. account
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_account(args):
    """KPIs da conta (gasto, impressoes, cliques, conversoes, CTR, CPC, CPA)."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_per_conversion,
            metrics.conversions_from_interactions_rate,
            metrics.search_impression_share
        FROM customer
        WHERE {date_clause}
    """

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 2. campaign
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_campaign(args):
    """Metricas por campanha."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign.status,
            campaign.advertising_channel_type,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_per_conversion,
            metrics.conversions_from_interactions_rate,
            metrics.search_impression_share
        FROM campaign
        WHERE campaign.status != 'REMOVED'
            AND {date_clause}
            AND metrics.cost_micros > 0
        ORDER BY metrics.cost_micros DESC
    """
    if args.limit:
        query += f"\nLIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 3. ad-group
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ad_group(args):
    """Metricas por ad group."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            ad_group.id,
            ad_group.name,
            ad_group.status,
            campaign.name,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_per_conversion
        FROM ad_group
        WHERE ad_group.status != 'REMOVED'
            AND campaign.status != 'REMOVED'
            AND {date_clause}
            AND metrics.cost_micros > 0
    """
    if args.campaign_id:
        query += f"\n            AND campaign.id = {args.campaign_id}"
    query += "\n        ORDER BY metrics.cost_micros DESC"
    if args.limit:
        query += f"\n        LIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 4. keyword
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_keyword(args):
    """Metricas por keyword."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            ad_group_criterion.quality_info.quality_score,
            ad_group.name,
            campaign.name,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_per_conversion
        FROM keyword_view
        WHERE ad_group_criterion.status = 'ENABLED'
            AND campaign.status != 'REMOVED'
            AND {date_clause}
            AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
    """
    if args.campaign_id:
        # Need to re-add since campaign filter goes before ORDER BY
        query = query.replace(
            "ORDER BY metrics.cost_micros DESC",
            f"AND campaign.id = {args.campaign_id}\n        ORDER BY metrics.cost_micros DESC"
        )
    if args.limit:
        query += f"\nLIMIT {args.limit}"
    else:
        query += "\nLIMIT 50"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 5. daily
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_daily(args):
    """Evolucao diaria (segments.date)."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            segments.date,
            campaign.name,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM campaign
        WHERE campaign.status != 'REMOVED'
            AND {date_clause}
            AND metrics.cost_micros > 0
        ORDER BY segments.date
    """
    if args.campaign_id:
        query = query.replace(
            "AND metrics.cost_micros > 0",
            f"AND metrics.cost_micros > 0\n            AND campaign.id = {args.campaign_id}"
        )

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 6. device
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_device(args):
    """Breakdown por dispositivo."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            segments.device,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_per_conversion
        FROM campaign
        WHERE campaign.status != 'REMOVED'
            AND {date_clause}
            AND metrics.cost_micros > 0
    """

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 7. hourly
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_hourly(args):
    """Breakdown por hora do dia."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            segments.hour,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.ctr
        FROM campaign
        WHERE campaign.status != 'REMOVED'
            AND {date_clause}
            AND metrics.impressions > 0
        ORDER BY segments.hour
    """

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Google Ads ClaudePRO - Insights & Reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcomando")

    # 1. account
    p = subparsers.add_parser("account", help="Account-level KPIs")
    add_customer_arg(p)
    add_date_args(p)
    p.set_defaults(func=cmd_account)

    # 2. campaign
    p = subparsers.add_parser("campaign", help="Campaign-level metrics")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p)
    p.set_defaults(func=cmd_campaign)

    # 3. ad-group
    p = subparsers.add_parser("ad-group", help="Ad group-level metrics")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p)
    add_campaign_filter(p)
    p.set_defaults(func=cmd_ad_group)

    # 4. keyword
    p = subparsers.add_parser("keyword", help="Keyword-level metrics")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p, default=50)
    add_campaign_filter(p)
    p.set_defaults(func=cmd_keyword)

    # 5. daily
    p = subparsers.add_parser("daily", help="Daily evolution (segments.date)")
    add_customer_arg(p)
    add_date_args(p)
    add_campaign_filter(p)
    p.set_defaults(func=cmd_daily)

    # 6. device
    p = subparsers.add_parser("device", help="Device breakdown")
    add_customer_arg(p)
    add_date_args(p)
    p.set_defaults(func=cmd_device)

    # 7. hourly
    p = subparsers.add_parser("hourly", help="Hourly breakdown")
    add_customer_arg(p)
    add_date_args(p)
    p.set_defaults(func=cmd_hourly)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
