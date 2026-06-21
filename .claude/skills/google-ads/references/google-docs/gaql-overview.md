GAQL overview (Google Ads Query Language)
https://developers.google.com/google-ads/api/docs/query/overview
Baixado para Google Ads API v23

# Google Ads Query Language

## Key terminology

- **Resource**: An entity in Google Ads, such as `campaign` or `ad_group`.
- **Segment**: A dimension used to group data, such as `segments.date` or `segments.device`. When segments are included in SELECT with metrics, metrics are split by segment.
- **Metric**: A measurement of performance, such as `metrics.impressions` or `metrics.clicks`.
- **Attributed Resource**: A resource implicitly joined to the main resource in the FROM clause, allowing you to select its attributes along with main resource attributes.

## Query for resource or metadata information

GAQL can query the API for:
- Resources and their related attributes, segments, and metrics using `GoogleAdsService` Search or SearchStream. Result is a list of `GoogleAdsRow` instances, each representing a resource. If segments are requested, the response includes an additional row for each segment-resource tuple.
- Metadata about available fields and resources using `GoogleAdsFieldService`. Result is a list of `GoogleAdsField` instances.

### Query for resource attributes
```
SELECT
  campaign.id,
  campaign.name,
  campaign.status
FROM campaign
ORDER BY campaign.id
```
Each resulting GoogleAdsRow represents a campaign object populated with the selected fields, including the campaign's resource_name.

### Query for metrics
```
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.impressions
FROM campaign
WHERE campaign.status = 'PAUSED'
  AND metrics.impressions > 1000
ORDER BY campaign.id
```

### Query for segments
```
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.impressions,
  segments.date,
FROM campaign
WHERE campaign.status = 'PAUSED'
  AND metrics.impressions > 1000
  AND segments.date during LAST_30_DAYS
ORDER BY campaign.id
```
Segmenting splits the selected metrics, grouping by each segment in the SELECT clause.

### Query for attributes of a related resource
```
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  bidding_strategy.name
FROM campaign
ORDER BY campaign.id
```
You join against attributed resources implicitly by selecting an attribute in your query.

## Best practices
- Select only the fields you need to avoid long response times and timeouts.
- Use LIMIT during development and testing to avoid processing large result sets.
- Apply filters in the WHERE clause to minimize data transfer and response size.
- Use GoogleAdsFieldService to check field compatibility and data types before constructing complex queries.
- Be mindful that some fields, especially those involving large amounts of data or complex calculations, can increase query cost.

## Mutate based on query results
You can take returned results as objects, modify them, and send them back to the mutate method in that resource's service. Example workflow:
1. Execute a query for all campaigns that are currently PAUSED and have impressions greater than 1000.
2. Get the Campaign object from the campaign field of each GoogleAdsRow.
3. Change the status of each campaign from PAUSED to ENABLED.
4. Call CampaignService.MutateCampaigns with the modified campaigns.

## Field metadata
Queries sent to GoogleAdsFieldService retrieve field metadata. Typical query:
```
SELECT
  name,
  category,
  selectable,
  filterable,
  sortable,
  selectable_with,
  data_type,
  is_repeated
WHERE name = "<INSERT_RESOURCE_OR_FIELD>"
```
Replace <INSERT_RESOURCE_OR_FIELD> with a resource (such as customer or campaign) or field (such as campaign.id, metrics.impressions, or ad_group.id).

## Code examples
The client libraries have examples of using GAQL in GoogleAdsService. The basic operations folder has examples such as GetCampaigns, GetKeywords, and SearchForGoogleAdsFields.

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
