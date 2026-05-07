#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Read operations (9 subcommands)
CLI for reading Google Ads data via google-ads SDK with GAQL queries.
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
# 1. accounts
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_accounts(args):
    """Lista contas acessiveis via MCC."""
    client = init_client()
    service = client.get_service("CustomerService")
    response = service.list_accessible_customers()
    accounts = []
    for resource_name in response.resource_names:
        customer_id = resource_name.split("/")[-1]
        # Try to get account details
        try:
            query = """
                SELECT
                    customer.id,
                    customer.descriptive_name,
                    customer.currency_code,
                    customer.time_zone,
                    customer.manager
                FROM customer
                LIMIT 1
            """
            rows = run_query(customer_id, query)
            if rows:
                accounts.append(rows[0].get("customer", {"id": customer_id}))
            else:
                accounts.append({"id": customer_id})
        except Exception:
            accounts.append({"id": customer_id})
    print_json(accounts)


# ---------------------------------------------------------------------------
# 2. campaigns
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_campaigns(args):
    """Lista campanhas com status, tipo e orcamento."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign.status,
            campaign.advertising_channel_type,
            campaign_budget.amount_micros,
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
        ORDER BY metrics.cost_micros DESC
    """
    if args.limit:
        query += f"\nLIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 3. ad-groups
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ad_groups(args):
    """Lista ad groups de uma campanha."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            ad_group.id,
            ad_group.name,
            ad_group.status,
            ad_group.type,
            ad_group.cpc_bid_micros,
            campaign.id,
            campaign.name,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions
        FROM ad_group
        WHERE ad_group.status != 'REMOVED'
            AND {date_clause}
    """
    if args.campaign_id:
        query += f"\n            AND campaign.id = {args.campaign_id}"
    query += "\n        ORDER BY metrics.cost_micros DESC"
    if args.limit:
        query += f"\n        LIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 4. keywords
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_keywords(args):
    """Lista keywords com Quality Score, match type e metricas."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            ad_group_criterion.status,
            ad_group_criterion.quality_info.quality_score,
            ad_group.name,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM keyword_view
        WHERE ad_group_criterion.status != 'REMOVED'
            AND {date_clause}
    """
    if args.campaign_id:
        query += f"\n            AND campaign.id = {args.campaign_id}"
    query += "\n        ORDER BY metrics.cost_micros DESC"
    if args.limit:
        query += f"\n        LIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 5. ads
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ads(args):
    """Lista anuncios RSA com headlines e descriptions."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            ad_group_ad.ad.id,
            ad_group_ad.ad.name,
            ad_group_ad.status,
            ad_group_ad.ad.type,
            ad_group_ad.ad.responsive_search_ad.headlines,
            ad_group_ad.ad.responsive_search_ad.descriptions,
            ad_group_ad.ad.final_urls,
            ad_group.name,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions
        FROM ad_group_ad
        WHERE ad_group_ad.status != 'REMOVED'
            AND {date_clause}
    """
    if args.campaign_id:
        query += f"\n            AND campaign.id = {args.campaign_id}"
    query += "\n        ORDER BY metrics.cost_micros DESC"
    if args.limit:
        query += f"\n        LIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 6. search-terms
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_search_terms(args):
    """Lista termos de busca com metricas."""
    customer_id = resolve_customer_id(args.customer_id)
    date_clause = build_date_clause(args)

    query = f"""
        SELECT
            search_term_view.search_term,
            search_term_view.status,
            campaign.name,
            ad_group.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM search_term_view
        WHERE {date_clause}
            AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
    """
    if args.limit:
        query += f"\nLIMIT {args.limit}"
    else:
        query += "\nLIMIT 100"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 7. extensions
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_extensions(args):
    """Lista assets/extensoes (sitelinks, callouts, etc)."""
    customer_id = resolve_customer_id(args.customer_id)

    query = """
        SELECT
            asset.id,
            asset.name,
            asset.type,
            asset.sitelink_asset.description1,
            asset.sitelink_asset.description2,
            asset.sitelink_asset.link_text,
            asset.callout_asset.callout_text,
            asset.structured_snippet_asset.header,
            asset.structured_snippet_asset.values
        FROM asset
        WHERE asset.type IN ('SITELINK', 'CALLOUT', 'STRUCTURED_SNIPPET')
    """
    if args.limit:
        query += f"\nLIMIT {args.limit}"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# 8. negative-keywords
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_negative_keywords(args):
    """Lista negative keywords (campaign e ad group level)."""
    customer_id = resolve_customer_id(args.customer_id)
    all_results = []

    # Campaign level negatives
    query_campaign = """
        SELECT
            campaign_criterion.keyword.text,
            campaign_criterion.keyword.match_type,
            campaign_criterion.criterion_id,
            campaign.id,
            campaign.name
        FROM campaign_criterion
        WHERE campaign_criterion.negative = TRUE
            AND campaign_criterion.type = 'KEYWORD'
    """
    rows = run_query(customer_id, query_campaign)
    for row in rows:
        row["_level"] = "campaign"
    all_results.extend(rows)

    # Ad group level negatives
    query_adgroup = """
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            ad_group_criterion.criterion_id,
            ad_group.id,
            ad_group.name,
            campaign.id,
            campaign.name
        FROM ad_group_criterion
        WHERE ad_group_criterion.negative = TRUE
            AND ad_group_criterion.type = 'KEYWORD'
    """
    rows = run_query(customer_id, query_adgroup)
    for row in rows:
        row["_level"] = "ad_group"
    all_results.extend(rows)

    print_json(all_results)


# ---------------------------------------------------------------------------
# 9. quality-scores
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_quality_scores(args):
    """Lista Quality Score decomposto (creative, landing page, expected CTR)."""
    customer_id = resolve_customer_id(args.customer_id)

    query = """
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            ad_group_criterion.quality_info.quality_score,
            ad_group_criterion.quality_info.creative_quality_score,
            ad_group_criterion.quality_info.post_click_quality_score,
            ad_group_criterion.quality_info.search_predicted_ctr,
            ad_group.name,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros
        FROM keyword_view
        WHERE ad_group_criterion.status = 'ENABLED'
            AND campaign.status != 'REMOVED'
            AND ad_group.status != 'REMOVED'
        ORDER BY metrics.cost_micros DESC
    """
    if args.limit:
        query += f"\nLIMIT {args.limit}"
    else:
        query += "\nLIMIT 50"

    results = run_query(customer_id, query)
    print_json(results)


# ---------------------------------------------------------------------------
# CLI parser
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Google Ads ClaudePRO - Read operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # 1. accounts
    p = sub.add_parser("accounts", help="List accessible customer accounts")
    p.set_defaults(func=cmd_accounts)

    # 2. campaigns
    p = sub.add_parser("campaigns", help="List campaigns with status, type, budget")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p)
    p.set_defaults(func=cmd_campaigns)

    # 3. ad-groups
    p = sub.add_parser("ad-groups", help="List ad groups of a campaign")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p)
    add_campaign_filter(p)
    p.set_defaults(func=cmd_ad_groups)

    # 4. keywords
    p = sub.add_parser("keywords", help="List keywords with QS, match type, metrics")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p)
    add_campaign_filter(p)
    p.set_defaults(func=cmd_keywords)

    # 5. ads
    p = sub.add_parser("ads", help="List ads with RSA details")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p)
    add_campaign_filter(p)
    p.set_defaults(func=cmd_ads)

    # 6. search-terms
    p = sub.add_parser("search-terms", help="List search terms with metrics")
    add_customer_arg(p)
    add_date_args(p)
    add_limit_arg(p, default=100)
    p.set_defaults(func=cmd_search_terms)

    # 7. extensions
    p = sub.add_parser("extensions", help="List assets (sitelinks, callouts, snippets)")
    add_customer_arg(p)
    add_limit_arg(p)
    p.set_defaults(func=cmd_extensions)

    # 8. negative-keywords
    p = sub.add_parser("negative-keywords", help="List negative keywords (campaign + ad group)")
    add_customer_arg(p)
    p.set_defaults(func=cmd_negative_keywords)

    # 9. quality-scores
    p = sub.add_parser("quality-scores", help="Quality Score decomposed (creative, landing, ctr)")
    add_customer_arg(p)
    add_limit_arg(p, default=50)
    p.set_defaults(func=cmd_quality_scores)

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
