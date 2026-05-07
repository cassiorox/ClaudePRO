#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Update operations (4 subcommands)
Subcommands: campaign, ad-group, keyword, ad
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
    safe_delay,
)


# ---------------------------------------------------------------------------
# Status mapping
# ---------------------------------------------------------------------------

def _resolve_status(client, entity_type, status_str):
    """Resolve status string to enum value."""
    status = status_str.upper()
    if entity_type == "campaign":
        enum = client.enums.CampaignStatusEnum
        mapping = {"ENABLED": enum.ENABLED, "PAUSED": enum.PAUSED, "REMOVED": enum.REMOVED}
    elif entity_type == "ad_group":
        enum = client.enums.AdGroupStatusEnum
        mapping = {"ENABLED": enum.ENABLED, "PAUSED": enum.PAUSED, "REMOVED": enum.REMOVED}
    elif entity_type == "ad_group_ad":
        enum = client.enums.AdGroupAdStatusEnum
        mapping = {"ENABLED": enum.ENABLED, "PAUSED": enum.PAUSED, "REMOVED": enum.REMOVED}
    elif entity_type == "ad_group_criterion":
        enum = client.enums.AdGroupCriterionStatusEnum
        mapping = {"ENABLED": enum.ENABLED, "PAUSED": enum.PAUSED, "REMOVED": enum.REMOVED}
    else:
        return None

    return mapping.get(status)


# ---------------------------------------------------------------------------
# 1. campaign
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_campaign(args):
    """Editar status, orcamento, bidding de campanha."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    service = client.get_service("CampaignService")
    ga_service = client.get_service("GoogleAdsService")

    operation = client.get_type("CampaignOperation")
    campaign = operation.update
    campaign.resource_name = ga_service.campaign_path(customer_id, args.campaign_id)

    field_mask_paths = []

    if args.status:
        status_val = _resolve_status(client, "campaign", args.status)
        if status_val is not None:
            campaign.status = status_val
            field_mask_paths.append("status")

    if args.name:
        campaign.name = args.name
        field_mask_paths.append("name")

    if args.budget:
        # Need to update the budget resource separately
        # First, get current campaign to find budget resource
        from lib import run_query
        query = f"""
            SELECT campaign.campaign_budget
            FROM campaign
            WHERE campaign.id = {args.campaign_id}
        """
        rows = run_query(customer_id, query)
        if rows and "campaign" in rows[0]:
            budget_resource = rows[0]["campaign"].get("campaign_budget", "")
            if budget_resource:
                budget_service = client.get_service("CampaignBudgetService")
                budget_op = client.get_type("CampaignBudgetOperation")
                budget = budget_op.update
                budget.resource_name = budget_resource
                budget.amount_micros = int(args.budget) * 10000  # centavos -> micros

                from google.api_core import protobuf_helpers
                client.copy_from(
                    budget_op.update_mask,
                    protobuf_helpers.field_mask(None, budget._pb)
                )
                # Simple field mask for budget
                budget_op.update_mask.paths.clear()
                budget_op.update_mask.paths.append("amount_micros")

                budget_service.mutate_campaign_budgets(
                    customer_id=customer_id, operations=[budget_op]
                )
                print(f"Budget atualizado: {budget_resource}", file=sys.stderr)

    if not field_mask_paths:
        if not args.budget:
            print_error("Nenhum campo para atualizar. Use --status, --name, ou --budget.")
            sys.exit(1)
        # Budget was updated above, just report success
        print_json({"status": "updated", "campaign_id": args.campaign_id, "budget_updated": True})
        return

    # Set field mask
    operation.update_mask.paths.extend(field_mask_paths)

    response = service.mutate_campaigns(
        customer_id=customer_id, operations=[operation]
    )
    result = response.results[0]
    print_json({
        "status": "updated",
        "resource_name": result.resource_name,
        "fields_updated": field_mask_paths,
    })


# ---------------------------------------------------------------------------
# 2. ad-group
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ad_group(args):
    """Editar status, CPC de ad group."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    service = client.get_service("AdGroupService")
    ga_service = client.get_service("GoogleAdsService")

    operation = client.get_type("AdGroupOperation")
    ad_group = operation.update
    ad_group.resource_name = ga_service.ad_group_path(customer_id, args.ad_group_id)

    field_mask_paths = []

    if args.status:
        status_val = _resolve_status(client, "ad_group", args.status)
        if status_val is not None:
            ad_group.status = status_val
            field_mask_paths.append("status")

    if args.name:
        ad_group.name = args.name
        field_mask_paths.append("name")

    if args.cpc_bid:
        ad_group.cpc_bid_micros = int(float(args.cpc_bid) * 1_000_000)
        field_mask_paths.append("cpc_bid_micros")

    if not field_mask_paths:
        print_error("Nenhum campo para atualizar. Use --status, --name, ou --cpc-bid.")
        sys.exit(1)

    operation.update_mask.paths.extend(field_mask_paths)

    response = service.mutate_ad_groups(
        customer_id=customer_id, operations=[operation]
    )
    result = response.results[0]
    print_json({
        "status": "updated",
        "resource_name": result.resource_name,
        "fields_updated": field_mask_paths,
    })


# ---------------------------------------------------------------------------
# 3. keyword
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_keyword(args):
    """Editar status, bid de keyword."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    service = client.get_service("AdGroupCriterionService")

    operation = client.get_type("AdGroupCriterionOperation")
    criterion = operation.update
    criterion.resource_name = client.get_service("GoogleAdsService").ad_group_criterion_path(
        customer_id, args.ad_group_id, args.keyword_id
    )

    field_mask_paths = []

    if args.status:
        status_val = _resolve_status(client, "ad_group_criterion", args.status)
        if status_val is not None:
            criterion.status = status_val
            field_mask_paths.append("status")

    if args.bid:
        criterion.cpc_bid_micros = int(float(args.bid) * 1_000_000)
        field_mask_paths.append("cpc_bid_micros")

    if not field_mask_paths:
        print_error("Nenhum campo para atualizar. Use --status ou --bid.")
        sys.exit(1)

    operation.update_mask.paths.extend(field_mask_paths)

    response = service.mutate_ad_group_criteria(
        customer_id=customer_id, operations=[operation]
    )
    result = response.results[0]
    print_json({
        "status": "updated",
        "resource_name": result.resource_name,
        "fields_updated": field_mask_paths,
    })


# ---------------------------------------------------------------------------
# 4. ad
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ad(args):
    """Editar status de anuncio."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    service = client.get_service("AdGroupAdService")

    operation = client.get_type("AdGroupAdOperation")
    ad_group_ad = operation.update
    ad_group_ad.resource_name = client.get_service("GoogleAdsService").ad_group_ad_path(
        customer_id, args.ad_group_id, args.ad_id
    )

    field_mask_paths = []

    if args.status:
        status_val = _resolve_status(client, "ad_group_ad", args.status)
        if status_val is not None:
            ad_group_ad.status = status_val
            field_mask_paths.append("status")

    if not field_mask_paths:
        print_error("Nenhum campo para atualizar. Use --status.")
        sys.exit(1)

    operation.update_mask.paths.extend(field_mask_paths)

    response = service.mutate_ad_group_ads(
        customer_id=customer_id, operations=[operation]
    )
    result = response.results[0]
    print_json({
        "status": "updated",
        "resource_name": result.resource_name,
        "fields_updated": field_mask_paths,
    })


# ---------------------------------------------------------------------------
# CLI parser
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Google Ads ClaudePRO - Update operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # 1. campaign
    p = sub.add_parser("campaign", help="Update campaign (status, budget, name)")
    add_customer_arg(p)
    p.add_argument("--campaign-id", required=True, help="Campaign ID")
    p.add_argument("--status", help="ENABLED, PAUSED, REMOVED")
    p.add_argument("--name", help="New campaign name")
    p.add_argument("--budget", help="New daily budget in centavos (5000 = R$50)")
    p.set_defaults(func=cmd_campaign)

    # 2. ad-group
    p = sub.add_parser("ad-group", help="Update ad group (status, CPC, name)")
    add_customer_arg(p)
    p.add_argument("--ad-group-id", required=True, help="Ad group ID")
    p.add_argument("--status", help="ENABLED, PAUSED, REMOVED")
    p.add_argument("--name", help="New ad group name")
    p.add_argument("--cpc-bid", help="Max CPC bid in reais (ex: 2.50)")
    p.set_defaults(func=cmd_ad_group)

    # 3. keyword
    p = sub.add_parser("keyword", help="Update keyword (status, bid)")
    add_customer_arg(p)
    p.add_argument("--ad-group-id", required=True, help="Ad group ID")
    p.add_argument("--keyword-id", required=True, help="Keyword criterion ID")
    p.add_argument("--status", help="ENABLED, PAUSED, REMOVED")
    p.add_argument("--bid", help="CPC bid in reais (ex: 1.50)")
    p.set_defaults(func=cmd_keyword)

    # 4. ad
    p = sub.add_parser("ad", help="Update ad status")
    add_customer_arg(p)
    p.add_argument("--ad-group-id", required=True, help="Ad group ID")
    p.add_argument("--ad-id", required=True, help="Ad ID")
    p.add_argument("--status", help="ENABLED, PAUSED, REMOVED")
    p.set_defaults(func=cmd_ad)

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
