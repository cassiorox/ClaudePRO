GAQL query structure
https://developers.google.com/google-ads/api/docs/query/structure
Baixado para Google Ads API v23

# Query structure

A GAQL query is made up of clauses: SELECT, FROM, WHERE, ORDER BY, LIMIT, PARAMETERS. SELECT and FROM are required; the others are optional.

## SELECT
Specifies a comma-separated list of resource fields, segment fields, and metrics. Required.
```
SELECT
  campaign.id,
  campaign.name
FROM campaign
```
Multiple field types in a single request:
```
SELECT
  campaign.id,
  campaign.name,
  bidding_strategy.id,
  bidding_strategy.name,
  segments.device,
  segments.date,
  metrics.impressions,
  metrics.clicks
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```
Errors occur when: querying non-selectable fields; selecting attributes of repeated fields; selecting fields not available for the FROM resource; selecting incompatible segments/metrics.

## FROM
Specifies the main resource returned. Only a single resource can be specified. Required for GoogleAdsService Search/SearchStream, but must NOT be specified when using GoogleAdsFieldService. Attributed resources are implicitly joined; add their attributes to SELECT to return their values.
```
SELECT
  campaign.id,
  ad_group.id
FROM ad_group
```
The resource_name field of the main resource is always returned even if not explicitly selected.

## WHERE
Specifies filtering conditions. One or more conditions separated by AND, each following `field_name Operator value`. Optional.
```
SELECT
  campaign.id,
  campaign.name,
  metrics.impressions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```
Multiple conditions:
```
SELECT
  campaign.id,
  campaign.name,
  segments.device,
  metrics.clicks
FROM campaign
WHERE metrics.impressions > 0
  AND segments.device = MOBILE
  AND segments.date DURING LAST_30_DAYS
```
Segments in WHERE must be in SELECT, with the following core date segments as exceptions: segments.date, segments.week, segments.month, segments.quarter, segments.year. If any of these is selected, at least one must be used in WHERE.

## ORDER BY
Each ordering is a field_name followed by ASC or DESC (defaults to ASC). Optional.
```
SELECT
  campaign.name,
  metrics.clicks
FROM campaign
ORDER BY metrics.clicks DESC
```
Multiple fields:
```
SELECT
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks
FROM ad_group
ORDER BY
  campaign.name,
  metrics.impressions DESC,
  metrics.clicks DESC
```

## LIMIT
```
SELECT
  campaign.name,
  ad_group.name,
  segments.device,
  metrics.impressions
FROM ad_group
ORDER BY metrics.impressions DESC
LIMIT 50
```

## PARAMETERS
Specifies meta parameters.

### include_drafts
Set to true to allow draft entities to be returned. Defaults to false.
```
SELECT campaign.name
FROM campaign
PARAMETERS include_drafts=true
```

### omit_unselected_resource_names
Set to true to prevent resource names from being returned unless explicitly requested in SELECT. Defaults to false.
```
SELECT
  campaign.name,
  customer.id
FROM campaign
PARAMETERS omit_unselected_resource_names = true
```

## Additional language rules
- The main resource field is NOT required in SELECT:
  ```
  SELECT campaign.id
  FROM ad_group
  WHERE ad_group.status = PAUSED
  ```
- Metrics can be exclusively selected:
  ```
  SELECT
      metrics.impressions,
      metrics.clicks,
      metrics.cost_micros
  FROM campaign
  ```
- Segmentation fields can be selected alone:
  ```
  SELECT segments.device FROM campaign
  ```
- resource_name can be used to filter or order:
  ```
  SELECT
      campaign.id,
      campaign.name
  FROM campaign
  WHERE campaign.resource_name = 'customers/1234567/campaigns/987654'
  ```

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
