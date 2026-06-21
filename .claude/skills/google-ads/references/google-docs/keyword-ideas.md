Keyword Ideas (generate-keyword-ideas)
https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
Baixado para Google Ads API v23

# Keyword Ideas

Using KeywordPlanIdeaService, you can search for new keywords relevant to your Google Search campaign, or find historical metrics on keywords.

## Generate ideas

Generate keyword ideas with KeywordPlanIdeaService.GenerateKeywordIdeas. Provide keyword and URL seeds; set targeting parameters (locations, language, network) to narrow your search. Historical statistics such as search volume are returned. Similar to Keyword Planner in the Google Ads UI.

Ways to create seeds:
- KeywordSeed: words or phrases describing what you're advertising (e.g., "plumbers", "drain cleaning").
- UrlSeed: URL of a webpage or website related to your business. Targets only a specific URL; if no hits, search expands to pages from the same domain. Contents of hyperlinks are NOT used to generate ideas.
- KeywordAndUrlSeed: both keyword and URL seeds. Can yield a larger volume of ideas than UrlSeed alone.
- SiteSeed: an entire site. Given a top-level domain (e.g., www.example.com), generates up to 250,000 keyword ideas from publicly available information.

Narrow targeting via GenerateKeywordIdeasRequest fields:
- language — see Language Constants for valid IDs.
- geo_target_constants — see Geo Targets for valid IDs.
- keyword_plan_network — e.g., GOOGLE_SEARCH or GOOGLE_SEARCH_AND_PARTNERS.
- include_adult_keywords.
- keyword_annotation — refine keywords.
- historical_metrics_options — set the date range.

The response supports pagination. Ideas are returned with historical metrics (search volume, competition) you can use to filter the list before forecasting.

The request must have exactly one of url_seed, keyword_seed, or keyword_and_url_seed set.

## Python code example
```python
def main(
    client: GoogleAdsClient,
    customer_id: str,
    location_ids: list[str],
    language_id: str,
    keyword_texts: list[str],
    page_url: str,
):
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")
    keyword_plan_network = (
        client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH_AND_PARTNERS
    )
    location_rns = map_locations_ids_to_resource_names(client, location_ids)
    google_ads_service = client.get_service("GoogleAdsService")
    language_rn = google_ads_service.language_constant_path(language_id)

    if not (keyword_texts or page_url):
        raise ValueError(
            "At least one of keywords or page URL is required, "
            "but neither was specified."
        )

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = language_rn
    request.geo_target_constants = location_rns
    request.include_adult_keywords = False
    request.keyword_plan_network = keyword_plan_network

    if not keyword_texts and page_url:
        request.url_seed.url = page_url
    if keyword_texts and not page_url:
        request.keyword_seed.keywords.extend(keyword_texts)
    if keyword_texts and page_url:
        request.keyword_and_url_seed.url = page_url
        request.keyword_and_url_seed.keywords.extend(keyword_texts)

    keyword_ideas = keyword_plan_idea_service.generate_keyword_ideas(
        request=request
    )

    for idea in keyword_ideas:
        competition_value = idea.keyword_idea_metrics.competition.name
        print(
            f'Keyword idea text "{idea.text}" has '
            f'"{idea.keyword_idea_metrics.avg_monthly_searches}" '
            f'average monthly searches and "{competition_value}" '
            "competition.\n"
        )
```

## curl (REST) example
```
curl -f --request POST \
"https://googleads.googleapis.com/v${API_VERSION}/customers/${CUSTOMER_ID}:generateKeywordIdeas" \
--header "Content-Type: application/json" \
--header "developer-token: ${DEVELOPER_TOKEN}" \
--header "login-customer-id: ${MANAGER_CUSTOMER_ID}" \
--header "Authorization: Bearer ${OAUTH2_ACCESS_TOKEN}" \
--data @- <<EOF
{
  "language": "${LANGUAGE}",
  "geoTargetConstants": ["${GEO_TARGET_CONSTANT}"],
  "includeAdultKeywords": false,
  "keywordPlanNetwork": "GOOGLE_SEARCH",
  "keywordAndUrlSeed": {
    "keywords": ["${KEYWORD}"],
    "url": "${URL}"
  }
}
EOF
```
LANGUAGE is the resource name like "languageConstants/{criterion_id}"; GEO_TARGET_CONSTANT is like "geoTargetConstants/{criterion_id}".

(Java, C#, PHP, Ruby, and Perl samples are also available on the source page; omitted here for brevity.)

## Map to the UI (Keyword Planner)

| Keyword Planner UI | Google Ads API |
| --- | --- |
| Enter Keywords and URLs | GenerateKeywordIdeasRequest.keyword_and_url_seed / keyword_seed / url_seed |
| Locations | GenerateKeywordIdeasRequest.geo_target_constants |
| Adult Keywords | GenerateKeywordIdeasRequest.include_adult_keywords |
| Language | GenerateKeywordIdeasRequest.language |
| Search Networks | GenerateKeywordIdeasRequest.keyword_plan_network |
| Refine Keywords | GenerateKeywordIdeasRequest.keyword_annotation |
| Date Range | GenerateKeywordIdeasRequest.historical_metrics_options |
| Results: Keyword | GenerateKeywordIdeaResult.text |
| Results: Metrics | GenerateKeywordIdeaResult.keyword_idea_metrics |

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving; RPC refs shown for v24).
