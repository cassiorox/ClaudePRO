Date ranges / segmentation (GAQL)
https://developers.google.com/google-ads/api/docs/query/date-ranges
Baixado para Google Ads API v23

# Date Ranges

GAQL lets you specify the date range in three ways: custom date range, predefined date range, predefined time period.

## Custom date range
Specify dates in ISO 8601 extended (YYYY-MM-DD) or basic (YYYYMMDD) format:
```
segments.date BETWEEN '2024-01-01' AND '2024-01-31'
```
```
segments.date >= '20241001' AND segments.date <= '20241031'
```

## Predefined date range

| Date range | Reports generated for... |
| --- | --- |
| TODAY | Today only. |
| YESTERDAY | Yesterday only. |
| LAST_7_DAYS | The last 7 days not including today. |
| LAST_BUSINESS_WEEK | The 5 day business week (Mon-Fri) of the previous business week. |
| THIS_MONTH | All days in the current month. |
| LAST_MONTH | All days in the previous month. |
| LAST_14_DAYS | The last 14 days not including today. |
| LAST_30_DAYS | The last 30 days not including today. |
| THIS_WEEK_SUN_TODAY | The period between the previous Sunday and the current day. |
| THIS_WEEK_MON_TODAY | The period between the previous Monday and the current day. |
| LAST_WEEK_SUN_SAT | The 7-day period starting with the previous Sunday. |
| LAST_WEEK_MON_SUN | The 7-day period starting with the previous Monday. |

Example:
```
segments.date DURING LAST_30_DAYS
```

## Predefined time period
Some date fields refer to a predefined period: segments.week, segments.month, segments.quarter. When filtering on these segments, use the `=` operator with the date that is the first day of the time period. A date that isn't the first day of a period returns a MISALIGNED_DATE_FOR_FILTER error.
```
segments.month = '2024-05-01'
```

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
