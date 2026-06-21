GAQL Query Cookbook (exemplos)
https://developers.google.com/google-ads/api/docs/query/cookbook
Baixado para Google Ads API v23

# Query Cookbook

GAQL queries that return the same data as screens in the Google Ads UI, plus how to look up geo constants. All dated queries default to the last seven days unless stated otherwise.

## Replicate Google Ads UI screens

### Campaigns
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

### Ad groups
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

### By resource name
Look up Mountain View, CA, by its resource name geoTargetConstants/1014044.
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

Note: The REST searchStream endpoint is POST https://googleads.googleapis.com/v{API_VERSION}/customers/{CUSTOMER_ID}/googleAds:searchStream with headers developer-token, login-customer-id, Authorization: Bearer {token}.

Page last updated 2026-06-03 UTC. Content reflects Google Ads API v23 (latest serving).
