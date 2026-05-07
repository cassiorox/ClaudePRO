#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Targeting Search & Validation
Subcommands: interests, interest-suggestions, behaviors, demographics,
             geolocations, validate, reach, delivery, describe
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_api,
    resolve_account,
    print_json,
    handle_fb_error,
    print_error,
    parse_json_arg,
    add_account_arg,
)

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.targetingsearch import TargetingSearch

# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


@handle_fb_error
def cmd_interests(args):
    """Search interests by keyword."""
    init_api()
    params = {
        "q": args.q,
        "type": "adinterest",
        "limit": args.limit,
    }
    if args.locale:
        params["locale"] = args.locale

    results = TargetingSearch.search(params=params)
    print_json(list(results))


@handle_fb_error
def cmd_interest_suggestions(args):
    """Get related interest suggestions from seed interest IDs."""
    init_api()
    ids = [i.strip() for i in args.ids.split(",")]
    params = {
        "type": "adinterestsuggestion",
        "interest_list": ids,
        "limit": args.limit,
    }
    if args.locale:
        params["locale"] = args.locale

    results = TargetingSearch.search(params=params)
    print_json(list(results))


@handle_fb_error
def cmd_behaviors(args):
    """List available targeting behaviors."""
    init_api()
    params = {
        "type": "adTargetingCategory",
        "class": "behaviors",
    }
    if args.locale:
        params["locale"] = args.locale

    results = TargetingSearch.search(params=params)
    print_json(list(results))


@handle_fb_error
def cmd_demographics(args):
    """List available targeting demographics."""
    init_api()
    params = {
        "type": "adTargetingCategory",
        "class": "demographics",
    }
    if args.locale:
        params["locale"] = args.locale

    results = TargetingSearch.search(params=params)
    print_json(list(results))


@handle_fb_error
def cmd_geolocations(args):
    """Search geolocations by keyword."""
    init_api()
    params = {
        "q": args.q,
        "type": "adgeolocation",
        "limit": args.limit,
    }
    if args.types:
        params["location_types"] = [t.strip() for t in args.types.split(",")]
    if args.country:
        params["country_code"] = args.country
    if args.locale:
        params["locale"] = args.locale

    results = TargetingSearch.search(params=params)
    print_json(list(results))


@handle_fb_error
def cmd_validate(args):
    """Validate a targeting spec against an ad account."""
    init_api()
    account_id = resolve_account(args.account)
    spec = parse_json_arg(args.spec, "spec")

    account = AdAccount(account_id)

    # Try SDK method first, fall back to direct API call
    try:
        result = account.get_targeting_validation(
            params={"targeting_spec": spec}
        )
        print_json(list(result))
    except AttributeError:
        # SDK doesn't expose this method directly — use raw API call
        from facebook_business.api import FacebookAdsApi
        api = FacebookAdsApi.get_default_api()
        response = api.call(
            "GET",
            f"/{account_id}/targetingvalidation",
            params={"targeting_spec": json.dumps(spec)},
        )
        print_json(response.json())


@handle_fb_error
def cmd_reach(args):
    """Get reach estimate for a targeting spec."""
    init_api()
    account_id = resolve_account(args.account)
    spec = parse_json_arg(args.spec, "spec")

    account = AdAccount(account_id)
    params = {"targeting_spec": spec}
    if args.optimization_goal:
        params["optimization_goal"] = args.optimization_goal

    result = account.get_reach_estimate(params=params)
    print_json(list(result))


@handle_fb_error
def cmd_delivery(args):
    """Get delivery estimate for a targeting spec."""
    init_api()
    account_id = resolve_account(args.account)
    spec = parse_json_arg(args.spec, "spec")

    account = AdAccount(account_id)
    params = {"targeting_spec": spec}
    if args.optimization_goal:
        params["optimization_goal"] = args.optimization_goal
    if args.daily_budget:
        params["daily_budget"] = args.daily_budget
    if args.lifetime_budget:
        params["lifetime_budget"] = args.lifetime_budget

    result = account.get_delivery_estimate(params=params)
    print_json(list(result))


@handle_fb_error
def cmd_describe(args):
    """Get human-readable targeting description."""
    init_api()
    account_id = resolve_account(args.account)
    spec = parse_json_arg(args.spec, "spec")

    account = AdAccount(account_id)

    # Try SDK method first, fall back to direct API call
    try:
        result = account.get_targeting_sentence_lines(
            params={"targeting_spec": spec}
        )
        print_json(list(result))
    except AttributeError:
        from facebook_business.api import FacebookAdsApi
        api = FacebookAdsApi.get_default_api()
        response = api.call(
            "GET",
            f"/{account_id}/targetingsentencelines",
            params={"targeting_spec": json.dumps(spec)},
        )
        print_json(response.json())


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Targeting Search & Validation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcomando")

    # interests
    p_interests = subparsers.add_parser("interests", help="Search interests by keyword")
    p_interests.add_argument("--q", required=True, help="Search keyword")
    p_interests.add_argument("--limit", type=int, default=25, help="Result limit")
    p_interests.add_argument("--locale", help="Locale (e.g. pt_BR, en_US)")
    p_interests.set_defaults(func=cmd_interests)

    # interest-suggestions
    p_suggestions = subparsers.add_parser(
        "interest-suggestions", help="Get related interest suggestions"
    )
    p_suggestions.add_argument(
        "--ids", required=True, help="Comma-separated interest IDs"
    )
    p_suggestions.add_argument("--limit", type=int, default=25, help="Result limit")
    p_suggestions.add_argument("--locale", help="Locale")
    p_suggestions.set_defaults(func=cmd_interest_suggestions)

    # behaviors
    p_behaviors = subparsers.add_parser("behaviors", help="List available behaviors")
    p_behaviors.add_argument("--locale", help="Locale")
    p_behaviors.set_defaults(func=cmd_behaviors)

    # demographics
    p_demographics = subparsers.add_parser(
        "demographics", help="List available demographics"
    )
    p_demographics.add_argument("--locale", help="Locale")
    p_demographics.set_defaults(func=cmd_demographics)

    # geolocations
    p_geo = subparsers.add_parser("geolocations", help="Search geolocations")
    p_geo.add_argument("--q", required=True, help="Search keyword")
    p_geo.add_argument(
        "--types",
        help="Comma-separated location types: country,region,city,zip,geo_market,electoral_district",
    )
    p_geo.add_argument("--country", help="Country code filter (e.g. BR, US)")
    p_geo.add_argument("--limit", type=int, default=25, help="Result limit")
    p_geo.add_argument("--locale", help="Locale")
    p_geo.set_defaults(func=cmd_geolocations)

    # validate
    p_validate = subparsers.add_parser("validate", help="Validate targeting spec")
    p_validate.add_argument(
        "--account", required=True, help="Ad account ID (e.g. act_123)"
    )
    p_validate.add_argument(
        "--spec", required=True, help="Targeting spec as JSON string"
    )
    p_validate.set_defaults(func=cmd_validate)

    # reach
    p_reach = subparsers.add_parser("reach", help="Get reach estimate")
    p_reach.add_argument(
        "--account", required=True, help="Ad account ID (e.g. act_123)"
    )
    p_reach.add_argument(
        "--spec", required=True, help="Targeting spec as JSON string"
    )
    p_reach.add_argument("--optimization-goal", help="Optimization goal")
    p_reach.set_defaults(func=cmd_reach)

    # delivery
    p_delivery = subparsers.add_parser("delivery", help="Get delivery estimate")
    p_delivery.add_argument(
        "--account", required=True, help="Ad account ID (e.g. act_123)"
    )
    p_delivery.add_argument(
        "--spec", required=True, help="Targeting spec as JSON string"
    )
    p_delivery.add_argument("--optimization-goal", help="Optimization goal")
    p_delivery.add_argument("--daily-budget", type=int, help="Daily budget in cents")
    p_delivery.add_argument(
        "--lifetime-budget", type=int, help="Lifetime budget in cents"
    )
    p_delivery.set_defaults(func=cmd_delivery)

    # describe
    p_describe = subparsers.add_parser(
        "describe", help="Get human-readable targeting description"
    )
    p_describe.add_argument(
        "--account", required=True, help="Ad account ID (e.g. act_123)"
    )
    p_describe.add_argument(
        "--spec", required=True, help="Targeting spec as JSON string"
    )
    p_describe.set_defaults(func=cmd_describe)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
