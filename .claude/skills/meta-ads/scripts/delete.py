#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Deletar objetos (campaigns, adsets, ads, creatives, audiences)
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
def cmd_object(args):
    """⚠️ DELETE — Arquiva qualquer objeto (campaign, adset, ad, creative).
    Soft delete: o objeto e arquivado, nao permanentemente removido."""
    init_api()
    from facebook_business.api import FacebookAdsApi

    api = FacebookAdsApi.get_default_api()
    # Use generic POST with status=DELETED which works for campaigns, adsets, ads
    try:
        result = api.call('POST', (args.id,), params={'status': 'DELETED'})
        safe_delay(1)
        print_json({"deleted": True, "id": args.id})
    except Exception:
        # Fallback: try api_delete which works for creatives and other types
        try:
            from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject

            class GenericObject(AbstractCrudObject):
                @classmethod
                def get_endpoint(cls):
                    return ''

            obj = GenericObject(args.id)
            obj.api_delete()
            safe_delay(1)
            print_json({"deleted": True, "id": args.id})
        except Exception as e:
            print_error(f"Falha ao deletar objeto {args.id}: {e}")
            sys.exit(1)


@handle_fb_error
def cmd_audience(args):
    """Deleta uma custom audience."""
    init_api()

    audience = CustomAudience(args.id)
    audience.api_delete()
    safe_delay(1)

    print_json({"deleted": True, "id": args.id})


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Meta Ads - Deletar objetos")
    sub = parser.add_subparsers(dest="command", required=True)

    # --- object ---
    p = sub.add_parser("object", help="Deletar/arquivar qualquer objeto (campaign, adset, ad, creative)")
    p.add_argument("--id", required=True, help="ID do objeto a deletar")

    # --- audience ---
    p = sub.add_parser("audience", help="Deletar custom audience")
    p.add_argument("--id", required=True, help="ID da custom audience")

    args = parser.parse_args()

    commands = {
        'object': cmd_object,
        'audience': cmd_audience,
    }

    fn = commands.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
