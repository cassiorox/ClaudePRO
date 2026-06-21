# Referencia de GAQL Queries

Queries GAQL uteis para Google Ads, organizadas por caso de uso.

---

## Versao da API (sempre usar a mais atual)

**Versao em uso no projeto: `v23`** -- e a versao mais nova suportada pelo SDK `google-ads` 30.0.0 instalado (o `GoogleAdsClient` usa a v23 por padrao).

**ATENCAO — o SDK esta atras da API:** a versao mais recente lancada da Google Ads API ja e a **v24 / v24.1** (abr-mai/2026), mas o SDK 30.0.0 so vai ate a **v23**. Para usar de fato a versao mais nova, e preciso **atualizar o SDK** (`pip install -U google-ads` para a 31.x ou superior) e so entao trocar a versao nas chamadas. Enquanto o SDK nao for atualizado, `v23` e a versao correta a usar.

**Regra (sempre usar a versao mais atual disponivel):**
1. Usar sempre a versao MAIS RECENTE suportada pelo SDK instalado. O `GoogleAdsClient` ja seleciona a mais nova por padrao -- nao fixar versao antiga sem motivo.
2. Periodicamente checar se ha SDK novo; se houver, atualizar o SDK e migrar para a versao de API mais nova, atualizando este arquivo.

Para checar a versao instalada do SDK e a API que ele suporta:
```bash
python3 -c "import importlib.metadata as m; print('google-ads', m.version('google-ads'))"
python3 -c "import google.ads.googleads as g, os; p=os.path.dirname(g.__file__); print(sorted([d for d in os.listdir(p) if d.startswith('v') and d[1:].isdigit()]))"
```

A Google lanca ~3 versoes por ano e cada versao tem ~1 ano ate o sunset.

| Versao | Lancamento | Sunset (aprox.) |
|---|---|---|
| `v24` / `v24.1` (mais nova da API) | abr-mai/2026 | ~2027 |
| `v23` (mais nova do SDK 30.0.0) | 28/01/2026 | fev/2027 |
| `v22` | 2025 | out/2026 (tentativo) |
| `v21` | 2025 | ago/2026 (tentativo) |

Deprecacoes relevantes pra gestor de trafego (ver `references/google-docs/release-notes.md` e `sunset-dates.md`): call-only ads deixam de servir em fev/2027; conversoes offline / Customer Match migrando para a Data Manager API.

Documentacao oficial baixada para consulta offline: pasta `references/google-docs/` (ver `references/google-docs/INDEX.md`). Consultar antes de criar/editar campanhas, montar GAQL ou confirmar campos.

Release notes oficiais: https://developers.google.com/google-ads/api/docs/release-notes
Sunset dates: https://developers.google.com/google-ads/api/docs/sunset-dates

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
