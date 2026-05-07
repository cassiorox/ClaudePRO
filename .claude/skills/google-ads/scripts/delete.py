#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Delete operations (3 subcommands)
Subcommands: keyword, negative, ad

REGRA: O Claude DEVE confirmar com o usuario antes de executar qualquer delete.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import (
    init_client,
    resolve_customer_id,
    print_json,
    print_error,
    handle_google_error_decorator,
    add_customer_arg,
)


# ---------------------------------------------------------------------------
# 1. keyword
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_keyword(args):
    """Remove keyword de um ad group."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    service = client.get_service("AdGroupCriterionService")
    resource_name = client.get_service("GoogleAdsService").ad_group_criterion_path(
        customer_id, args.ad_group_id, args.keyword_id
    )

    operation = client.get_type("AdGroupCriterionOperation")
    operation.remove = resource_name

    response = service.mutate_ad_group_criteria(
        customer_id=customer_id, operations=[operation]
    )
    result = response.results[0]
    print_json({
        "status": "removed",
        "resource_name": result.resource_name,
    })


# ---------------------------------------------------------------------------
# 2. negative
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_negative(args):
    """Remove negative keyword (campaign ou ad group level)."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)
    ga_service = client.get_service("GoogleAdsService")

    level = args.level.lower()

    if level == "ad_group" or level == "ad-group":
        service = client.get_service("AdGroupCriterionService")
        resource_name = ga_service.ad_group_criterion_path(
            customer_id, args.parent_id, args.criterion_id
        )
        operation = client.get_type("AdGroupCriterionOperation")
        operation.remove = resource_name

        response = service.mutate_ad_group_criteria(
            customer_id=customer_id, operations=[operation]
        )
    else:
        # campaign level
        service = client.get_service("CampaignCriterionService")
        resource_name = ga_service.campaign_criterion_path(
            customer_id, args.parent_id, args.criterion_id
        )
        operation = client.get_type("CampaignCriterionOperation")
        operation.remove = resource_name

        response = service.mutate_campaign_criteria(
            customer_id=customer_id, operations=[operation]
        )

    result = response.results[0]
    print_json({
        "status": "removed",
        "resource_name": result.resource_name,
        "level": level,
    })


# ---------------------------------------------------------------------------
# 3. ad
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ad(args):
    """Remove anuncio de um ad group."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    service = client.get_service("AdGroupAdService")
    resource_name = client.get_service("GoogleAdsService").ad_group_ad_path(
        customer_id, args.ad_group_id, args.ad_id
    )

    operation = client.get_type("AdGroupAdOperation")
    operation.remove = resource_name

    response = service.mutate_ad_group_ads(
        customer_id=customer_id, operations=[operation]
    )
    result = response.results[0]
    print_json({
        "status": "removed",
        "resource_name": result.resource_name,
    })


# ---------------------------------------------------------------------------
# CLI parser
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Google Ads ClaudePRO - Delete operations (CONFIRM BEFORE RUNNING)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # 1. keyword
    p = sub.add_parser("keyword", help="Remove keyword from ad group")
    add_customer_arg(p)
    p.add_argument("--ad-group-id", required=True, help="Ad group ID")
    p.add_argument("--keyword-id", required=True, help="Keyword criterion ID")
    p.set_defaults(func=cmd_keyword)

    # 2. negative
    p = sub.add_parser("negative", help="Remove negative keyword")
    add_customer_arg(p)
    p.add_argument("--criterion-id", required=True, help="Criterion ID")
    p.add_argument("--level", required=True, help="campaign or ad-group")
    p.add_argument("--parent-id", required=True, help="Campaign ID or Ad group ID")
    p.set_defaults(func=cmd_negative)

    # 3. ad
    p = sub.add_parser("ad", help="Remove ad from ad group")
    add_customer_arg(p)
    p.add_argument("--ad-group-id", required=True, help="Ad group ID")
    p.add_argument("--ad-id", required=True, help="Ad ID")
    p.set_defaults(func=cmd_ad)

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
