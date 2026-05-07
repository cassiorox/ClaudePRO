#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Datasets / Pixels (read + diagnostics)
Operações sobre AdsPixel: listar, detalhes, criar, stats, share/unshare,
e diagnósticos de saúde do pixel/CAPI.
"""
import os
import sys
import argparse
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import (
    init_api, resolve_account, print_json, handle_fb_error,
    print_error, parse_fields, add_account_arg, add_fields_arg,
    safe_delay,
)

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adspixel import AdsPixel


# ---------------------------------------------------------------------------
# Field defaults
# ---------------------------------------------------------------------------

# Default fields seguros (lê com ads_management/ads_read padrão).
# `owner_ad_account` e `creator` exigem permissão extra de owner e disparam
# erro #200. Quem precisar pode pedir via --fields.
_PIXEL_FIELDS = [
    "id", "name", "code", "creation_time", "last_fired_time",
    "is_created_by_business", "is_unavailable", "can_proxy",
    "owner_business", "automatic_matching_fields",
    "enable_automatic_matching", "data_use_setting",
    "first_party_cookie_status",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_fields(args):
    if args.fields:
        return parse_fields(args.fields)
    return _PIXEL_FIELDS


def _parse_time(value):
    """Aceita Unix timestamp ou 'YYYY-MM-DD'."""
    if value is None:
        return None
    if isinstance(value, int) or value.isdigit():
        return int(value)
    try:
        dt = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return int(dt.timestamp())
    except ValueError:
        print_error(f"Formato de data invalido: {value} (use YYYY-MM-DD ou unix timestamp)")
        sys.exit(1)


def _hours_since(ts):
    """Retorna horas desde um timestamp. Aceita Unix int ou ISO string."""
    if not ts:
        return None
    try:
        if isinstance(ts, (int, float)):
            unix = int(ts)
        elif isinstance(ts, str) and ts.isdigit():
            unix = int(ts)
        elif isinstance(ts, str):
            # ISO 8601 com timezone, ex: "2026-04-30T20:59:51-0300"
            dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            unix = int(dt.timestamp())
        else:
            return None
    except (ValueError, TypeError):
        return None
    return round((time.time() - unix) / 3600, 1)


def _aggregate_events(cursor):
    """Recebe o cursor de pixel.get_stats(aggregation=event) e retorna
    {event_name: total_count} somando todos os buckets horários.
    """
    summary = {}
    for s in cursor:
        bucket = s.export_all_data() if hasattr(s, "export_all_data") else s
        inner = bucket.get("data") or []
        # Caso 1: bucket tem lista de {value, count}
        if isinstance(inner, list) and inner and isinstance(inner[0], dict):
            for item in inner:
                event = item.get("value") or item.get("event") or "unknown"
                count = int(item.get("count") or 0)
                summary[event] = summary.get(event, 0) + count
        else:
            # Caso 2: formato plano (fallback)
            event = bucket.get("aggregation") or bucket.get("event") or "unknown"
            count = int(bucket.get("count") or bucket.get("value") or 0)
            summary[event] = summary.get(event, 0) + count
    return summary


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_list(args):
    """Lista pixels/datasets de uma ad account."""
    init_api()
    account_id = resolve_account(args.account)
    fields = _resolve_fields(args)

    account = AdAccount(account_id)
    cursor = account.get_ads_pixels(fields=fields)
    results = [p.export_all_data() for p in cursor]
    print_json(results)


@handle_fb_error
def cmd_get(args):
    """Detalhes de um pixel/dataset (--id)."""
    init_api()
    fields = _resolve_fields(args)

    pixel = AdsPixel(args.id)
    pixel.api_get(fields=fields)
    print_json(pixel)


@handle_fb_error
def cmd_create(args):
    """⚠️ WRITE — Cria pixel novo na ad account.

    Atenção: cada ad account pode ter no máximo 1 pixel próprio.
    Se já existir, a API retorna erro.
    """
    init_api()
    account_id = resolve_account(args.account)

    params = {"name": args.name}
    account = AdAccount(account_id)
    result = account.create_ads_pixel(params=params)
    safe_delay(1)

    print(f"Pixel criado: {result.get('id')}", file=sys.stderr)
    print_json(result)


@handle_fb_error
def cmd_stats(args):
    """Stats de eventos do pixel agregadas por dimensão.

    aggregation suportadas: event, host, url, device_os, device_type,
    pixel_fire, browser_total_counts_unique_users, event_total_counts
    """
    init_api()

    params = {"aggregation": args.aggregation}
    start = _parse_time(args.start)
    end = _parse_time(args.end)
    if start:
        params["start_time"] = start
    if end:
        params["end_time"] = end
    if args.event:
        params["event"] = args.event

    pixel = AdsPixel(args.id)
    cursor = pixel.get_stats(params=params)
    results = [s.export_all_data() if hasattr(s, "export_all_data") else s for s in cursor]
    print_json(results)


@handle_fb_error
def cmd_events(args):
    """Lista eventos únicos recebidos pelo pixel no período (atalho de stats)."""
    init_api()

    params = {"aggregation": "event"}
    start = _parse_time(args.start)
    end = _parse_time(args.end)
    if start:
        params["start_time"] = start
    if end:
        params["end_time"] = end

    pixel = AdsPixel(args.id)
    cursor = pixel.get_stats(params=params)
    summary = _aggregate_events(cursor)
    output = sorted(
        ({"event": k, "count": v} for k, v in summary.items()),
        key=lambda x: x["count"],
        reverse=True,
    )
    print_json(output)


@handle_fb_error
def cmd_share(args):
    """⚠️ WRITE — Compartilha pixel com outra ad account."""
    init_api()
    target = args.account if args.account.startswith("act_") else f"act_{args.account}"
    target_id = target.replace("act_", "")

    pixel = AdsPixel(args.id)
    result = pixel.create_shared_account(params={"account_id": target_id})
    safe_delay(1)
    print_json(result)


@handle_fb_error
def cmd_unshare(args):
    """⚠️ WRITE — Remove compartilhamento de pixel com ad account."""
    init_api()
    target = args.account if args.account.startswith("act_") else f"act_{args.account}"
    target_id = target.replace("act_", "")

    pixel = AdsPixel(args.id)
    result = pixel.delete_shared_accounts(params={"account_id": target_id})
    safe_delay(1)
    print_json(result)


@handle_fb_error
def cmd_shared_accounts(args):
    """Lista ad accounts que tem acesso compartilhado a este pixel."""
    init_api()
    pixel = AdsPixel(args.id)
    cursor = pixel.get_shared_accounts(fields=["id", "name", "account_status"])
    results = [a.export_all_data() for a in cursor]
    print_json(results)


@handle_fb_error
def cmd_diagnostics(args):
    """Resumo de saúde do pixel: status, último fire, eventos recentes,
    automatic matching, CAPI status, sinais de problema.

    Combina vários endpoints num único output amigável.
    """
    init_api()

    pixel = AdsPixel(args.id)
    pixel.api_get(fields=_PIXEL_FIELDS)
    info = pixel.export_all_data()

    last_fired = info.get("last_fired_time")
    last_fired_hours = _hours_since(last_fired) if last_fired else None

    # Stats dos últimos 7 dias agregados por evento
    end = int(time.time())
    start = end - (7 * 24 * 3600)
    try:
        cursor = pixel.get_stats(params={
            "aggregation": "event",
            "start_time": start,
            "end_time": end,
        })
        events_summary = _aggregate_events(cursor)
    except Exception as e:
        events_summary = {"_error": str(e)}

    # Avaliação de saúde
    issues = []
    if info.get("is_unavailable"):
        issues.append("pixel marcado como is_unavailable=true")
    if not last_fired:
        issues.append("pixel nunca disparou um evento (last_fired_time vazio)")
    elif last_fired_hours is not None and last_fired_hours > 24:
        issues.append(f"último evento há {last_fired_hours}h (mais de 1 dia atrás)")
    if not events_summary or "_error" in events_summary:
        issues.append("nenhum evento agregado retornado nos últimos 7 dias")
    if not info.get("enable_automatic_matching"):
        issues.append("automatic matching desabilitado (pode reduzir match rate)")

    health = "HEALTHY" if not issues else ("DEGRADED" if len(issues) <= 2 else "UNHEALTHY")

    diagnostics = {
        "pixel_id": info.get("id"),
        "name": info.get("name"),
        "health": health,
        "last_fired_time": last_fired,
        "last_fired_hours_ago": last_fired_hours,
        "is_unavailable": info.get("is_unavailable"),
        "can_proxy": info.get("can_proxy"),
        "automatic_matching_enabled": info.get("enable_automatic_matching"),
        "automatic_matching_fields": info.get("automatic_matching_fields"),
        "first_party_cookie_status": info.get("first_party_cookie_status"),
        "data_use_setting": info.get("data_use_setting"),
        "owner_ad_account": info.get("owner_ad_account"),
        "events_last_7d": dict(sorted(events_summary.items(), key=lambda x: -(x[1] if isinstance(x[1], int) else 0))),
        "issues": issues,
    }
    print_json(diagnostics)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads - Datasets / Pixels (signal diagnostics)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # list
    p = sub.add_parser("list", help="Lista pixels da ad account")
    add_account_arg(p)
    add_fields_arg(p)
    p.set_defaults(func=cmd_list)

    # get
    p = sub.add_parser("get", help="Detalhes de um pixel")
    p.add_argument("--id", required=True)
    add_fields_arg(p)
    p.set_defaults(func=cmd_get)

    # create
    p = sub.add_parser("create", help="⚠️ Cria pixel novo (1 por conta)")
    p.add_argument("--name", required=True)
    add_account_arg(p)
    p.set_defaults(func=cmd_create)

    # stats
    p = sub.add_parser("stats", help="Stats de eventos agregadas")
    p.add_argument("--id", required=True)
    p.add_argument(
        "--aggregation", default="event",
        help="event | host | url | device_os | device_type | pixel_fire | "
             "browser_total_counts_unique_users | event_total_counts",
    )
    p.add_argument("--start", help="Data início (YYYY-MM-DD ou unix ts)")
    p.add_argument("--end", help="Data fim (YYYY-MM-DD ou unix ts)")
    p.add_argument("--event", help="Filtrar por evento específico (ex: Purchase)")
    p.set_defaults(func=cmd_stats)

    # events
    p = sub.add_parser("events", help="Resumo de eventos únicos recebidos")
    p.add_argument("--id", required=True)
    p.add_argument("--start", help="Data início (YYYY-MM-DD ou unix ts)")
    p.add_argument("--end", help="Data fim (YYYY-MM-DD ou unix ts)")
    p.set_defaults(func=cmd_events)

    # share
    p = sub.add_parser("share", help="⚠️ Compartilha pixel com ad account")
    p.add_argument("--id", required=True, help="Pixel ID")
    p.add_argument("--account", required=True, help="Ad account destino (act_XXX)")
    p.set_defaults(func=cmd_share)

    # unshare
    p = sub.add_parser("unshare", help="⚠️ Remove compartilhamento de pixel")
    p.add_argument("--id", required=True, help="Pixel ID")
    p.add_argument("--account", required=True, help="Ad account a remover (act_XXX)")
    p.set_defaults(func=cmd_unshare)

    # shared-accounts
    p = sub.add_parser("shared-accounts", help="Lista contas com acesso ao pixel")
    p.add_argument("--id", required=True)
    p.set_defaults(func=cmd_shared_accounts)

    # diagnostics
    p = sub.add_parser("diagnostics", help="Resumo de saúde do pixel (health check)")
    p.add_argument("--id", required=True)
    p.set_defaults(func=cmd_diagnostics)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
