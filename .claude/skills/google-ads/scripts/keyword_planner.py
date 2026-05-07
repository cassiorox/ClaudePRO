#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Keyword Planner (2 subcommands)
Subcommands: ideas, historical-metrics

Cobre KeywordPlanIdeaService do SDK oficial (descoberta de keywords + metricas
historicas sem precisar criar campanha).

Defaults sao para o mercado brasileiro:
  - location_id: 2076 (Brazil)
  - language_id: 1014 (Portuguese)
  - network: GOOGLE_SEARCH_AND_PARTNERS

Parametros comuns:
  --customer-id    Customer ID (sem hifens)
  --keywords       Seed keywords (separadas por |). Ate 20 por request
  --url            Page URL para usar como seed (opcional, combinavel com --keywords)
  --location-id    Geo target constant ID (default 2076 = Brazil)
  --language-id    Language constant ID (default 1014 = Portuguese)
  --network        GOOGLE_SEARCH ou GOOGLE_SEARCH_AND_PARTNERS
  --include-adult  Inclui keywords adultas (default: false)
  --limit          Limita N resultados na saida (ordenado por avg_monthly_searches DESC)
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import (
    init_client,
    resolve_customer_id,
    micros_to_currency,
    print_json,
    print_error,
    handle_google_error_decorator,
    add_customer_arg,
    add_limit_arg,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _split_keywords(raw):
    """Quebra string 'kw1|kw2|kw3' em lista, removendo vazios e duplicadas."""
    if not raw:
        return []
    seen = set()
    out = []
    for kw in raw.split("|"):
        kw = kw.strip()
        if kw and kw.lower() not in seen:
            seen.add(kw.lower())
            out.append(kw)
    return out


def _resolve_network_enum(client, network_str):
    """Converte string em KeywordPlanNetworkEnum. Default: SEARCH_AND_PARTNERS."""
    enum = client.enums.KeywordPlanNetworkEnum
    network = (network_str or "GOOGLE_SEARCH_AND_PARTNERS").upper()
    if network in ("SEARCH", "GOOGLE_SEARCH"):
        return enum.GOOGLE_SEARCH
    return enum.GOOGLE_SEARCH_AND_PARTNERS


def _round_currency(micros):
    """Converte micros para reais com 2 casas decimais."""
    return round(micros_to_currency(micros or 0), 2)


def _idea_to_dict(idea):
    """Converte um GenerateKeywordIdeaResult para dict legivel."""
    metrics = idea.keyword_idea_metrics
    return {
        "keyword": idea.text,
        "avg_monthly_searches": metrics.avg_monthly_searches or 0,
        "competition": metrics.competition.name if metrics.competition else "UNSPECIFIED",
        "competition_index": metrics.competition_index or 0,
        "low_top_of_page_bid": _round_currency(metrics.low_top_of_page_bid_micros),
        "high_top_of_page_bid": _round_currency(metrics.high_top_of_page_bid_micros),
    }


def _historical_to_dict(result):
    """Converte um GenerateKeywordHistoricalMetricsResult para dict."""
    metrics = result.keyword_metrics
    monthly = []
    for m in metrics.monthly_search_volumes:
        monthly.append({
            "year": int(m.year) if m.year else None,
            "month": m.month.name if m.month else None,
            "searches": m.monthly_searches or 0,
        })
    return {
        "keyword": result.text,
        "avg_monthly_searches": metrics.avg_monthly_searches or 0,
        "competition": metrics.competition.name if metrics.competition else "UNSPECIFIED",
        "competition_index": metrics.competition_index or 0,
        "low_top_of_page_bid": _round_currency(metrics.low_top_of_page_bid_micros),
        "high_top_of_page_bid": _round_currency(metrics.high_top_of_page_bid_micros),
        "monthly_search_volumes": monthly,
        "close_variants": list(result.close_variants),
    }


def _build_targeting(client, args):
    """Constroi resource names de language e geo target."""
    google_ads_service = client.get_service("GoogleAdsService")
    geo_service = client.get_service("GeoTargetConstantService")

    language_id = args.language_id or "1014"
    location_ids = [loc.strip() for loc in (args.location_id or "2076").split(",") if loc.strip()]

    language_rn = google_ads_service.language_constant_path(language_id)
    location_rns = [geo_service.geo_target_constant_path(lid) for lid in location_ids]

    return language_rn, location_rns


# ---------------------------------------------------------------------------
# 1. ideas — KeywordPlanIdeaService.generate_keyword_ideas
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ideas(args):
    """Gera ideias de keywords a partir de seeds (keywords e/ou URL)."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    keywords = _split_keywords(args.keywords)
    page_url = args.url

    if not keywords and not page_url:
        print_error("Informe ao menos --keywords ou --url como seed.")
        sys.exit(1)

    if len(keywords) > 20:
        print_error(f"Maximo 20 seed keywords por request (recebido: {len(keywords)}).")
        sys.exit(1)

    service = client.get_service("KeywordPlanIdeaService")
    language_rn, location_rns = _build_targeting(client, args)

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = language_rn
    request.geo_target_constants.extend(location_rns)
    request.include_adult_keywords = bool(args.include_adult)
    request.keyword_plan_network = _resolve_network_enum(client, args.network)

    if keywords and page_url:
        request.keyword_and_url_seed.url = page_url
        request.keyword_and_url_seed.keywords.extend(keywords)
    elif keywords:
        request.keyword_seed.keywords.extend(keywords)
    elif page_url:
        request.url_seed.url = page_url

    response = service.generate_keyword_ideas(request=request)

    ideas = [_idea_to_dict(idea) for idea in response]
    ideas.sort(key=lambda x: x["avg_monthly_searches"], reverse=True)

    if args.limit:
        ideas = ideas[: args.limit]

    print_json({
        "seed_keywords": keywords,
        "seed_url": page_url,
        "language_id": args.language_id or "1014",
        "location_ids": [loc.strip() for loc in (args.location_id or "2076").split(",")],
        "network": (args.network or "GOOGLE_SEARCH_AND_PARTNERS").upper(),
        "total_ideas": len(ideas),
        "ideas": ideas,
    })


# ---------------------------------------------------------------------------
# 2. historical-metrics — KeywordPlanIdeaService.generate_keyword_historical_metrics
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_historical_metrics(args):
    """Pega volume/CPC historico de uma lista de keywords (sem gerar novas)."""
    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)

    keywords = _split_keywords(args.keywords)
    if not keywords:
        print_error("Informe --keywords (separadas por |).")
        sys.exit(1)
    if len(keywords) > 10000:
        print_error(f"Maximo 10000 keywords por request (recebido: {len(keywords)}).")
        sys.exit(1)

    service = client.get_service("KeywordPlanIdeaService")
    language_rn, location_rns = _build_targeting(client, args)

    request = client.get_type("GenerateKeywordHistoricalMetricsRequest")
    request.customer_id = customer_id
    request.keywords.extend(keywords)
    request.language = language_rn
    request.geo_target_constants.extend(location_rns)
    request.include_adult_keywords = bool(args.include_adult)
    request.keyword_plan_network = _resolve_network_enum(client, args.network)

    response = service.generate_keyword_historical_metrics(request=request)

    results = [_historical_to_dict(r) for r in response.results]
    results.sort(key=lambda x: x["avg_monthly_searches"], reverse=True)

    print_json({
        "input_keywords": keywords,
        "language_id": args.language_id or "1014",
        "location_ids": [loc.strip() for loc in (args.location_id or "2076").split(",")],
        "network": (args.network or "GOOGLE_SEARCH_AND_PARTNERS").upper(),
        "total_results": len(results),
        "results": results,
    })


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def add_targeting_args(parser):
    parser.add_argument(
        "--location-id",
        default="2076",
        help="Geo target constant ID (default: 2076 = Brasil). Multiplos separados por virgula.",
    )
    parser.add_argument(
        "--language-id",
        default="1014",
        help="Language constant ID (default: 1014 = Portugues).",
    )
    parser.add_argument(
        "--network",
        default="GOOGLE_SEARCH_AND_PARTNERS",
        choices=["GOOGLE_SEARCH", "GOOGLE_SEARCH_AND_PARTNERS"],
        help="Rede de origem das metricas (default: GOOGLE_SEARCH_AND_PARTNERS).",
    )
    parser.add_argument(
        "--include-adult",
        action="store_true",
        help="Inclui keywords adultas (default: false).",
    )


def main():
    parser = argparse.ArgumentParser(
        description="Google Ads ClaudePRO - Keyword Planner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcomando")

    # 1. ideas
    p = subparsers.add_parser("ideas", help="Gera ideias de keywords a partir de seeds")
    add_customer_arg(p)
    p.add_argument("--keywords", help="Seed keywords separadas por | (max 20)")
    p.add_argument("--url", help="Page URL como seed (combinavel com --keywords)")
    add_targeting_args(p)
    add_limit_arg(p)
    p.set_defaults(func=cmd_ideas)

    # 2. historical-metrics
    p = subparsers.add_parser(
        "historical-metrics",
        help="Volume/CPC historicos de uma lista de keywords (sem gerar novas)",
    )
    add_customer_arg(p)
    p.add_argument(
        "--keywords",
        required=True,
        help="Keywords separadas por | (max 10000)",
    )
    add_targeting_args(p)
    p.set_defaults(func=cmd_historical_metrics)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
