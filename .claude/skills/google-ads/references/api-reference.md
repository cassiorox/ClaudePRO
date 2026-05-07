# Referencia de GAQL Queries

Queries GAQL uteis para Google Ads, organizadas por caso de uso.

---

## Account KPIs

```sql
SELECT
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_per_conversion,
  metrics.conversions_from_interactions_rate,
  metrics.search_impression_share
FROM customer
WHERE segments.date BETWEEN '{since}' AND '{until}'
```

## Campanhas

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_per_conversion
FROM campaign
WHERE campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

## Ad Groups

```sql
SELECT
  ad_group.id,
  ad_group.name,
  ad_group.status,
  ad_group.type,
  ad_group.cpc_bid_micros,
  campaign.id,
  campaign.name,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions
FROM ad_group
WHERE ad_group.status != 'REMOVED'
  AND campaign.id = {campaign_id}
ORDER BY metrics.cost_micros DESC
```

## Keywords com Quality Score

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  ad_group.name,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.ctr,
  metrics.average_cpc
FROM keyword_view
WHERE ad_group_criterion.status = 'ENABLED'
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Search Terms

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.ctr,
  metrics.average_cpc
FROM search_term_view
WHERE segments.date BETWEEN '{since}' AND '{until}'
  AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

## Anuncios RSA

```sql
SELECT
  ad_group_ad.ad.id,
  ad_group_ad.ad.name,
  ad_group_ad.status,
  ad_group_ad.ad.type,
  ad_group_ad.ad.responsive_search_ad.headlines,
  ad_group_ad.ad.responsive_search_ad.descriptions,
  ad_group_ad.ad.final_urls,
  ad_group.name,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM ad_group_ad
WHERE ad_group_ad.status != 'REMOVED'
  AND ad_group_ad.ad.type = 'RESPONSIVE_SEARCH_AD'
ORDER BY metrics.cost_micros DESC
```

## Evolucao Diaria

```sql
SELECT
  segments.date,
  campaign.name,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions
FROM campaign
WHERE segments.date BETWEEN '{since}' AND '{until}'
  AND campaign.status != 'REMOVED'
  AND metrics.cost_micros > 0
ORDER BY segments.date
```

## Breakdown por Dispositivo

```sql
SELECT
  segments.device,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.ctr,
  metrics.average_cpc
FROM campaign
WHERE segments.date BETWEEN '{since}' AND '{until}'
  AND campaign.status != 'REMOVED'
  AND metrics.cost_micros > 0
```

## Breakdown por Hora

```sql
SELECT
  segments.hour,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.ctr
FROM campaign
WHERE segments.date BETWEEN '{since}' AND '{until}'
  AND campaign.status != 'REMOVED'
  AND metrics.impressions > 0
ORDER BY segments.hour
```

## Negativas (Campaign Level)

```sql
SELECT
  campaign_criterion.keyword.text,
  campaign_criterion.keyword.match_type,
  campaign_criterion.negative,
  campaign.name
FROM campaign_criterion
WHERE campaign_criterion.negative = TRUE
  AND campaign_criterion.type = 'KEYWORD'
```

## Negativas (Ad Group Level)

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.negative,
  ad_group.name,
  campaign.name
FROM ad_group_criterion
WHERE ad_group_criterion.negative = TRUE
  AND ad_group_criterion.type = 'KEYWORD'
```

## Assets (Sitelinks, Callouts)

```sql
SELECT
  asset.id,
  asset.name,
  asset.type,
  asset.sitelink_asset.description1,
  asset.sitelink_asset.description2,
  asset.sitelink_asset.link_text,
  asset.callout_asset.callout_text
FROM asset
WHERE asset.type IN ('SITELINK', 'CALLOUT', 'STRUCTURED_SNIPPET')
```

---

## Periodos pre-definidos (date_range)

| Valor | Descricao |
|-------|-----------|
| `TODAY` | Hoje |
| `YESTERDAY` | Ontem |
| `LAST_7_DAYS` | Ultimos 7 dias |
| `LAST_14_DAYS` | Ultimos 14 dias |
| `LAST_30_DAYS` | Ultimos 30 dias |
| `THIS_MONTH` | Este mes |
| `LAST_MONTH` | Mes passado |
| `THIS_QUARTER` | Este trimestre |
| `LAST_QUARTER` | Trimestre passado |

## Tipos de campanha (advertising_channel_type)

| Tipo | Descricao |
|------|-----------|
| `SEARCH` | Rede de pesquisa |
| `DISPLAY` | Rede de display |
| `SHOPPING` | Shopping |
| `VIDEO` | YouTube |
| `PERFORMANCE_MAX` | Performance Max |
| `SMART` | Smart campaigns |

## Match Types

| Tipo | GAQL | Descricao |
|------|------|-----------|
| Exact | `EXACT` | [keyword] |
| Phrase | `PHRASE` | "keyword" |
| Broad | `BROAD` | keyword |
