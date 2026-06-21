# Insights (Ads Insights API overview)
Fonte: https://developers.facebook.com/docs/marketing-api/insights/
Baixado para Meta Marketing API v25.0

---

# Ads Insights API

Updated: Apr 27, 2026

The Ads Insights API provides performance data and statistics for Meta ads. With its flexible reporting options, you can customize your requests and obtain nearly any metric available in Meta Ads Manager.

## Before you begin

To access the Ads Insights API, you will need:

- An app.
- The `ads_read` permission.

You should also set up your ads to track the actions you're interested in, using tools like the Conversions API or Meta Pixel.

## Calling the Ads Insights API

The Ads Insights API is available as an edge off of all ad objects.

| Resource | Provides |
| --- | --- |
| `/{ad-account-id}/insights` | Insights from an ad account |
| `/{campaign-id}/insights` | Insights from an ad campaign |
| `/{ad-set-id}/insights` | Insights from an ad set |
| `/{ad-id}/insights` | Insights from an ad |

By default, `GET` requests return basic metrics for the ad object, typically from the past 30 days.

### Example request

```
curl -G \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<CAMPAIGN_ID>/insights"
```

### Example response

```
{
  "data": [
    {
      "account_id": "<AD_ACCOUNT_ID>",
      "campaign_id": "<CAMPAIGN_ID>",
      "date_start": "2025-03-14",
      "date_stop": "2025-04-12",
      "impressions": "361324",
      "spend": "5339.5"
    }
  ],
  "paging": { "cursors": { "before": "MAZDZD", "after": "MAZDZD" } }
}
```

## Customizing Your Requests

You obtain more specific data via three main components: parameters (time ranges, attribution windows, etc.), fields (metrics), and breakdowns. For example, number of clicks by gender in the last 7 days:

- Parameters: `date_preset=last_7d`
- Fields: `clicks`
- Breakdowns: `gender`

### Example request

```
curl -G \
  -d "date_preset=last_7d" \
  -d "fields=clicks" \
  -d "breakdowns=gender" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<CAMPAIGN_ID>/insights"
```

## Learn More

- Parameters and Fields
- Metrics
- Breakdowns: /docs/marketing-api/insights/breakdowns
- Asynchronous Requests: /docs/marketing-api/insights/best-practices#asynchronous
- Limits and Best Practices: /docs/marketing-api/insights/best-practices
- Conversions reporting, Product-Level Reporting, Marketing Mix Modeling

Auto-generated reference docs per ad object insights edge: Ad Account Insights, Ad Campaign Insights, Ad Set Insights, Ad Insights.
