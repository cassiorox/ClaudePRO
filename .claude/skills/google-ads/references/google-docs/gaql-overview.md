GAQL overview (Google Ads Query Language)
https://developers.google.com/google-ads/api/docs/query/overview
Baixado para Google Ads API v24

# Google Ads Query Language

## Key terminology

**Resource** — An entity in Google Ads, such as `campaign` or `ad_group`.

**Segment** — A dimension used to group data, such as `segments.date` or `segments.device`. When segments are included in `SELECT` clause with metrics, metrics are split by segment.

**Metric** — A measurement of performance, such as `metrics.impressions` or `metrics.clicks`.

**Attributed Resource** — A resource that is implicitly joined to the main resource in `FROM` clause, allowing you to select its attributes along with main resource attributes.

## Query for resource or metadata information

The Google Ads Query Language can query the Google Ads API for the following types of information:

- Resources and their related attributes, segments, and metrics using [`GoogleAdsService`](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService) _Search_ or _SearchStream_:
The result from a GoogleAdsService query is a list of
[`GoogleAdsRow`](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsRow) instances, with each `GoogleAdsRow`
representing a resource.

  If any attributes or metrics are requested, then the
row also includes those fields. If any segments are requested, then the
response also shows an additional row for each segment-resource tuple.

- Metadata about available fields and resources in [`GoogleAdsFieldService`](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsFieldService):
This service provides a catalog of queryable fields with specifics about their
compatibility and type.

  The result from a `GoogleAdsFieldService` query is
a list of [`GoogleAdsField`](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsField) instances, with each
`GoogleAdsField` containing details about the requested field.

For more details on query structure see [Query Structure](https://developers.google.com/google-ads/api/docs/query/structure) and [Google Ads Query Language Grammar](https://developers.google.com/google-ads/api/docs/query/grammar).

### Query for resource attributes

Here is an example of a basic query for attributes of the campaign resource that
illustrates how to return the campaign ID, name, and status:

```
SELECT
  campaign.id,
  campaign.name,
  campaign.status
FROM campaign
ORDER BY campaign.id
```

This query orders by campaign ID. Each resulting `GoogleAdsRow` represents
a `campaign` object populated with the selected fields, including the
campaign's `resource_name`.

To find out what other fields are available for campaign queries, consult the
[`Campaign` reference documentation](https://developers.google.com/google-ads/api/reference/rpc/v24/Campaign).

### Query for metrics

Alongside selected attributes for a given resource, you can also query for
related metrics:

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

This query filters for only the campaigns that have a status of `PAUSED` and
have had greater than 1000 impressions, while ordering by campaign ID. Each
resulting `GoogleAdsRow` would have a `metrics` field populated with the
selected metrics.

For a list of queryable metrics, consult the [`Metrics` documentation](https://developers.google.com/google-ads/api/reference/rpc/v24/Metrics).

### Query for segments

Alongside selected attributes for a given resource, you can also query for
related segments:

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

Similar to querying for metrics, this query filters for only the campaigns that
have a status of `PAUSED` and have had greater than 1000 impressions. However,
this query segments the data by date. This leads to each resulting
`GoogleAdsRow` representing a tuple of a campaign and the date `Segment`.
Segmenting splits the selected metrics, grouping by each segment in the SELECT
clause.

For a list of queryable segments, consult the
[`Segments` documentation](https://developers.google.com/google-ads/api/reference/rpc/v24/Segments).

### Query for attributes of a related resource

In a query for a given resource, you may be able to join against other related
resources if available. These related resources are known as "attributed
resources". You can join against attributed resources implicitly by selecting an
attribute in your query.

```
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  bidding_strategy.name
FROM campaign
ORDER BY campaign.id
```

This query not only selects campaign attributes, but also pulls in related
attributes from each campaign selected. Each resulting `GoogleAdsRow` represents
a `campaign` object populated with the selected campaign attributes, as well as
the selected bidding strategy attribute `bidding_strategy.name`.

To find out what attributed resources are available for campaign queries,
consult the [`Campaign` reference documentation](https://developers.google.com/google-ads/api/reference/rpc/v24/Campaign).

## Best practices

- Select only the fields you need to avoid long response times and timeouts.
- Use `LIMIT` during development and testing to avoid processing large result
sets.
- Apply filters in the `WHERE` clause to minimize data transfer and response
size.
- Use [`GoogleAdsFieldService`](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsFieldService) to check
field compatibility and data types before constructing complex queries.
- Be mindful that some fields, especially those involving large amounts of data
or complex calculations, can increase query cost.

## Mutate based on query results

When querying for a given resource, you can immediately take those returned
results as objects, modify them, and send them back to the mutate method in that
resource's service. Here is a sample workflow:

1. Execute a query for all campaigns that are currently `PAUSED` and have
impressions greater than 1000.
2. Get the `Campaign` object from the `campaign` field of each `GoogleAdsRow` in
the response.
3. Change the status of each campaign from `PAUSED` to `ENABLED`.
4. Call [`CampaignService.MutateCampaigns`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignService)
with the modified campaigns to update them.

## Field metadata

Queries sent to `GoogleAdsFieldService` are meant for retrieving field metadata.
This information can be used to understand how the fields can be used together
in a query. Since data is available from the API and it provides the necessary
metadata needed to validate or build a query, this allows for developers to do
so programmatically. Here's a
typical query for metadata:

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

You can replace `<INSERT_RESOURCE_OR_FIELD>` in this query with either a
resource (such as `customer` or `campaign`) or field (such as `campaign.id`,
`metrics.impressions`, or `ad_group.id`).

For a list of queryable fields, consult the
[`GoogleAdsField` documentation](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsField).

## Code examples

The [client libraries](https://developers.google.com/google-ads/api/docs/client-libs) have examples of using the
Google Ads Query Language in `GoogleAdsService`. The **basic operations** folder has
examples such as `GetCampaigns`, `GetKeywords`, and `SearchForGoogleAdsFields`.
