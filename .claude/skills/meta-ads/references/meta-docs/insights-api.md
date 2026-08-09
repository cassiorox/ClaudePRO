<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights.md | Scrape: 2026-08-09 | API v26.0 -->

# Ads Insights API



The Ads Insights API provides performance data and statistics for Meta ads. With its flexible reporting options, you can customize your requests and obtain nearly any metric available in Meta Ads Manager.

## Before you begin

To access the Ads Insights API, you will need:

* An [app](https://developers.facebook.com/apps). (See [Meta App Development](https://developers.facebook.com/docs/development) for more information.)
* The ads_read permission. (See [Permissions](https://developers.facebook.com/docs/permissions) and [Authorization](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization) for more information.)

You should also set up your ads to track the actions you're interested in. For that, you can use tools like the Conversions API or Meta Pixel.

## Calling the Ads Insights API

The Ads Insights API is available as an edge off of all ad objects. (See more information about Meta's ad hierarchy [here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview#how-it-works).)

| Resource | Provides |
| --- | --- |
| [`/{ad-account-id}/insights`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/insights) | Insights from an ad account |
| [`/{campaign-id}/insights`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/insights) | Insights from an ad campaign |
| [`/{ad-set-id}/insights`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/insights) | Insights from an ad set |
| [`/{ad-id}/insights`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup/insights) | Insights from an ad |

By default, `GET` requests will return basic metrics for the ad object, typically from the past 30 days.

### Example request

```html
curl -G \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<CAMPAIGN_ID>/insights"
```

### Example response:

```json
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
  "paging": {
    "cursors": {
    "before": "MAZDZD",
    "after": "MAZDZD"
    }
  }
}
```

## Customizing Your Requests

You can obtain much more specific data by leveraging three main components in your request: parameters (to specify things like time ranges, attribution windows, etc.), fields (i.e., metrics), and breakdowns. For example, to know the number of clicks (all) by gender that happened in the last 7 days of your campaign, you might include:

* Parameters: `date_preset=last_7d`
* Fields: `clicks`
* Breakdowns: `gender`

### Example request

```html
curl -G \
  -d "date_preset=last_7d" \
  -d "fields=clicks" \
  -d "breakdowns=gender" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<CAMPAIGN_ID>/insights"
```

### Example response

```json
{
  "data": [
    {
      "clicks": "7346",
      "date_start": "2025-04-06",
      "date_stop": "2025-04-12",
      "gender": "female"
    },
    {
      "clicks": "3788",
      "date_start": "2025-04-06",
      "date_stop": "2025-04-12",
      "gender": "male"
    },
    {
      "clicks": "79",
      "date_start": "2025-04-06",
      "date_stop": "2025-04-12",
      "gender": "unknown"
    },
  ],
  "paging": {
    "cursors": {
    "before": "MAZDZD",
    "after": "MAZDZD"
    }
  }
}
```

## Learn More

The Ads Insights API can be powerful, so be sure to read on and learn how to master its features:

* Parameters and Fields
* Metrics
* [Breakdowns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/breakdowns)
* [Asynchronous Requests](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/best-practices#asynchronous)
* [Limits and Best Practices](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/best-practices)
* Specific guides for [conversions reporting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/tracking-specs), Product-Level Reporting, and [Marketing Mix Modeling](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/marketing-mix-modeling)

You can additionally find auto-generated reference documentation for each ad object's insights edge:

* [Ad Account Insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/insights)
* [Ad Campaign Insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/insights)
* [Ad Set Insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/insights)
* [Ad Insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup/insights)

If you plan to include data from the Ads Insights API in your solution, please also review the [Meta Platform Terms](https://developers.facebook.com/terms) and [Developer Policies for Marketing API](https://developers.facebook.com/devpolicy/#marketingapi).
