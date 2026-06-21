GAQL Query Cookbook (exemplos)
https://developers.google.com/google-ads/api/docs/query/cookbook
Baixado para Google Ads API v24

# Query Cookbook

This guide provides a set of Google Ads Query Language queries that demonstrate
how to return the same data as screens in the Google Ads UI, as well as how to
look up geo constants. You can use these queries as is, or as starting points
for constructing your own customized queries.

For a summary table of common UI terms and predefined reports mapped to API
resources, see [Reports in the Google Ads UI](https://developers.google.com/google-ads/api/docs/reporting/uireports).

## Replicate Google Ads UI screens

This section showcases API queries that return the same data as the default
screens of the Google Ads UI. If you're building an app that
shows metrics and data similarly to Google Ads, these queries can help you pull
analogous data from the API.

### Campaigns

The default Campaigns overview screen in the UI.

```
SELECT campaign.name,
  campaign_budget.amount_micros,
  campaign.status,
  campaign.optimization_score,
  campaign.advertising_channel_type,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  campaign.bidding_strategy_type
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status != 'REMOVED'
```

curl (REST):

```
curl -f --request POST "https://googleads.googleapis.com/v${API_VERSION}/customers/${CUSTOMER_ID}/googleAds:searchStream" \
--header "Content-Type: application/json" \
--header "developer-token: ${DEVELOPER_TOKEN}" \
--header "login-customer-id: ${MANAGER_CUSTOMER_ID}" \
--header "Authorization: Bearer ${OAUTH2_ACCESS_TOKEN}" \
--data '{
"query": "
  SELECT campaign.name,
    campaign_budget.amount_micros,
    campaign.status,
    campaign.optimization_score,
    campaign.advertising_channel_type,
    metrics.clicks,
    metrics.impressions,
    metrics.ctr,
    metrics.average_cpc,
    metrics.cost_micros,
    campaign.bidding_strategy_type
  FROM campaign
  WHERE segments.date DURING LAST_7_DAYS
    AND campaign.status != 'REMOVED'
"
}'
```

### Ad groups

The default Ad groups overview screen in the UI.

```
SELECT ad_group.name,
  campaign.name,
  ad_group.status,
  ad_group.type,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros
FROM ad_group
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group.status != 'REMOVED'
```

### Ads

The default Ads overview screen in the UI.

This particular query specifically fetches the individual components of an
ad, which are seen rendered together in the UI screen's **Ad** column.

```
SELECT ad_group_ad.ad.expanded_text_ad.headline_part1,
  ad_group_ad.ad.expanded_text_ad.headline_part2,
  ad_group_ad.ad.expanded_text_ad.headline_part3,
  ad_group_ad.ad.final_urls,
  ad_group_ad.ad.expanded_text_ad.description,
  ad_group_ad.ad.expanded_text_ad.description2,
  campaign.name,
  ad_group.name,
  ad_group_ad.policy_summary.approval_status,
  ad_group_ad.ad.type,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros
FROM ad_group_ad
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group_ad.status != 'REMOVED'
```

### Search keywords

The default Search keywords overview screen in the UI.

```
SELECT ad_group_criterion.keyword.text,
  campaign.name,
  ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.approval_status,
  ad_group_criterion.final_urls,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros
FROM keyword_view
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group_criterion.status != 'REMOVED'
```

### Search terms

The default Search terms overview screen in the UI.

```
SELECT search_term_view.search_term,
  segments.keyword.info.match_type,
  search_term_view.status,
  campaign.name,
  ad_group.name,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  campaign.advertising_channel_type
FROM search_term_view
WHERE segments.date DURING LAST_7_DAYS
```

### Audiences

The default Audiences overview screen in the UI.

```
SELECT ad_group_criterion.resource_name,
  ad_group_criterion.type,
  campaign.name,
  ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.bid_modifier,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  campaign.advertising_channel_type
FROM ad_group_audience_view
WHERE segments.date DURING LAST_7_DAYS
```

### Age (Demographics)

The default Age demographics overview screen in the UI.

```
SELECT ad_group_criterion.age_range.type,
  campaign.name,
  ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.bid_modifier,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  campaign.advertising_channel_type
FROM age_range_view
WHERE segments.date DURING LAST_7_DAYS
```

### Gender (Demographics)

The default Gender demographics overview screen in the UI.

```
SELECT ad_group_criterion.gender.type,
  campaign.name,
  ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.bid_modifier,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  campaign.advertising_channel_type
FROM gender_view
WHERE segments.date DURING LAST_7_DAYS
```

### Locations

The default Locations overview screen in the UI.

```
SELECT campaign_criterion.location.geo_target_constant,
  campaign.name,
  campaign_criterion.bid_modifier,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros
FROM location_view
WHERE segments.date DURING LAST_7_DAYS
  AND campaign_criterion.status != 'REMOVED'
```

## Look up geo constants

The [Codes and formats](https://developers.google.com/google-ads/api/data/codes-formats) page provides
reference tables for most constants used in the API. However, you can also
dynamically look up some constants using the Google Ads Query Language.

This sample shows how to look up a location by its resource name or by its
display name.

### By resource name

Look up Mountain View, CA, by its resource name `geoTargetConstants/1014044`.

```
SELECT geo_target_constant.canonical_name,
  geo_target_constant.country_code,
  geo_target_constant.id,
  geo_target_constant.name,
  geo_target_constant.status,
  geo_target_constant.target_type
FROM geo_target_constant
WHERE geo_target_constant.resource_name = 'geoTargetConstants/1014044'
```

### By display name

Look up "Mountain View" as a city name in the United States.

```
SELECT geo_target_constant.canonical_name,
  geo_target_constant.country_code,
  geo_target_constant.id,
  geo_target_constant.name,
  geo_target_constant.status,
  geo_target_constant.target_type
FROM geo_target_constant
WHERE geo_target_constant.country_code = 'US'
  AND geo_target_constant.target_type = 'City'
  AND geo_target_constant.name = 'Mountain View'
  AND geo_target_constant.status = 'ENABLED'
```
