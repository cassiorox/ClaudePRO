Date ranges / segmentation (GAQL)
https://developers.google.com/google-ads/api/docs/query/date-ranges
Baixado para Google Ads API v24

# Date Ranges

The Google Ads Query Language lets you specify the date range in these ways:

- Custom date range
- Predefined date range
- Predefined time period

## Custom date range

You can specify dates in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) extended
(`YYYY-MM-DD`) or basic (`YYYYMMDD`) format, for example:

```
segments.date BETWEEN '2024-01-01' AND '2024-01-31'
```

```
segments.date >= '20241001' AND segments.date <= '20241031'
```

## Predefined date range

The list of valid predefined date ranges is as follows:

| Date range | Reports are generated for... |
| --- | --- |
| `TODAY` | Today only. |
| `YESTERDAY` | Yesterday only. |
| `LAST_7_DAYS` | The last 7 days not including today. |
| `LAST_BUSINESS_WEEK` | The 5 day business week, Monday through Friday, of the previous business week. |
| `THIS_MONTH` | All days in the current month. |
| `LAST_MONTH` | All days in the previous month. |
| `LAST_14_DAYS` | The last 14 days not including today. |
| `LAST_30_DAYS` | The last 30 days not including today. |
| `THIS_WEEK_SUN_TODAY` | The period between the previous Sunday and the current day. |
| `THIS_WEEK_MON_TODAY` | The period between the previous Monday and the current day. |
| `LAST_WEEK_SUN_SAT` | The 7-day period starting with the previous Sunday. |
| `LAST_WEEK_MON_SUN` | The 7-day period starting with the previous Monday. |

Example:

```
segments.date DURING LAST_30_DAYS
```

## Predefined time period

Some date fields refer to a predefined period of time, specifically:

- `segments.week`
- `segments.month`
- `segments.quarter`

When filtering on these segments, you can use the `=` operator with the date
that is the first day of the time period. If you specify a date that isn't the
first day of a period, a `MISALIGNED_DATE_FOR_FILTER` error is returned.

For example, to specify the month of May in the year 2024, use the
following condition, specifying the first day of that month:

```
segments.month = '2024-05-01'
```
