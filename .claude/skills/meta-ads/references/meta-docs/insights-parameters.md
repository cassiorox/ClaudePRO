# Insights parameters
Fonte: https://developers.facebook.com/docs/marketing-api/insights/
(Nota: a URL original /insights/parameters/ retorna 404 na v25. O conteudo de parametros/campos foi consolidado na pagina principal da Ads Insights API e na referencia /reference/ad-account/insights. Este arquivo resume os principais parametros.)
Baixado para Meta Marketing API v25.0

---

# Ads Insights API — Parameters, Fields, and Breakdowns

Requests to any insights edge (`/{ad-account-id}/insights`, `/{campaign-id}/insights`, `/{ad-set-id}/insights`, `/{ad-id}/insights`) are customized with three components: parameters, fields (metrics), and breakdowns.

## Key parameters

| Parameter | Description |
| --- | --- |
| `level` | Aggregation level of returned rows: `account`, `campaign`, `adset`, `ad`. |
| `date_preset` | Predefined date range. Values: `today`, `yesterday`, `this_month`, `last_month`, `this_quarter`, `maximum`, `data_maximum`, `last_3d`, `last_7d`, `last_14d`, `last_28d`, `last_30d`, `last_90d`, `last_week_mon_sun`, `last_week_sun_sat`, `last_quarter`, `last_year`, `this_week_mon_today`, `this_week_sun_today`, `this_year`. |
| `time_range` | `{'since':'YYYY-MM-DD','until':'YYYY-MM-DD'}`. Overrides `date_preset`. Start date cannot be beyond 37 months. |
| `time_ranges` | Array of multiple time ranges for comparison. |
| `time_increment` | Number of days per row (e.g. `1` = daily breakdown), or `monthly`, or `all_days`. |
| `breakdowns` | How to segment results. E.g. `age`, `gender`, `country`, `region`, `publisher_platform`, `platform_position`, `impression_device`, `device_platform`, `placement`, `hourly_stats_aggregated_by_advertiser_time_zone`, etc. Some breakdowns cannot be combined. |
| `action_breakdowns` | Segments action metrics. E.g. `action_type`, `action_carousel_card_id`, `action_carousel_card_name`, `action_video_type`, `action_destination`, `action_device`, `action_reaction`, `action_target_id`. |
| `action_attribution_windows` | Attribution windows for action stats. E.g. `1d_view`, `7d_view`, `28d_view`, `1d_click`, `7d_click`, `28d_click`, `default`. |
| `filtering` | Array of filter objects: `{"field":...,"operator":"IN/EQUAL/...","value":[...]}`. |
| `sort` | Field and direction to sort results, e.g. `impressions_descending`. |
| `fields` | Comma-separated list of metrics to return. |
| `limit` | Max number of rows per page (use pagination). |
| `use_account_attribution_setting` | Boolean. Use the ad account's attribution setting. |
| `use_unified_attribution_setting` | Boolean. Use the unified (ad set level) attribution setting. |

## Common fields (metrics)

`account_id`, `account_name`, `campaign_id`, `campaign_name`, `adset_id`, `adset_name`, `ad_id`, `ad_name`, `impressions`, `reach`, `frequency`, `spend`, `clicks`, `cpc`, `cpm`, `cpp`, `ctr`, `inline_link_clicks`, `inline_link_click_ctr`, `cost_per_inline_link_click`, `unique_clicks`, `unique_ctr`, `actions`, `action_values`, `conversions`, `conversion_values`, `cost_per_action_type`, `cost_per_conversion`, `purchase_roas`, `website_ctr`, `video_play_actions`, `video_avg_time_watched_actions`, `video_p25/p50/p75/p100_watched_actions`, `date_start`, `date_stop`, `objective`, `optimization_goal`, `quality_ranking`, `engagement_rate_ranking`, `conversion_rate_ranking`.

## Example

```
curl -G \
  -d "level=ad" \
  -d "date_preset=last_7d" \
  -d "fields=ad_name,spend,impressions,clicks,ctr,cpc,actions,cost_per_action_type" \
  -d "breakdowns=publisher_platform,platform_position" \
  -d "action_attribution_windows=['7d_click','1d_view']" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<CAMPAIGN_ID>/insights"
```

## Asynchronous reports

For large reports, request an async job via `POST /{object-id}/insights`, poll `GET /{ad-report-run-id}`, then fetch results from the insights edge with the report run ID. In v25.0+, failed async jobs return `error_code`, `error_message`, `error_subcode`, `error_user_title`, `error_user_msg`.

## Canonical references

- Ads Insights API overview: /docs/marketing-api/insights/
- Breakdowns: /docs/marketing-api/insights/breakdowns
- Ad Account Insights reference (full field list): /docs/marketing-api/reference/ad-account/insights
- Best Practices (incl. async): /docs/marketing-api/insights/best-practices
