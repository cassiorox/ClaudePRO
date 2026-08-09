<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/breakdowns.md | Scrape: 2026-08-09 | API v26.0 -->

# Insights API Breakdowns



You can group the Insights API results into different sets using breakdowns.

The Insights API can return several metrics that are estimated, in development, or both. Insights breakdown values are estimated. For more information, see [Insights API, Estimated, and Deprecated Metrics](https://developers.facebook.com/docs/graph-api/reference/adgroup/insights).

## Limitations

### Unavailable fields

Do not request the following fields when specifying a breakdown:

* `app_store_clicks`
* `newsfeed_avg_position`
* `newsfeed_clicks`
* `relevance_score`
* `newsfeed_impressions`

### Restrictions for off-Meta action metrics

The following breakdowns will no longer be available for off-Meta action metrics.

#### Type 1

* `region`
* `dma`
* `hourly_stats_aggregated_by_audience_time_zone`
* `hourly_stats_aggregated_by_advertiser_time_zone`

#### Type 2

* `action_device`
* `action_destination`
* `action_target_id`
* `product_id`
* `action_carousel_card_id/action_carousel_card_name`
* `action_canvas_component_name`

**Rules related to queries containing above breakdowns:**

* **Type 1** — The Insights API will not return unsupported off-Meta metrics (for example, an actions metric with Type 1 breakdowns).
* **Type 2** — Off-Meta web metrics will continue to be returned from the API, however will not contain the breakdown value.
The mobile metrics will not be returned anymore when queried with these breakdowns.

**Note:** The breakdowns listed above will still be supported for on-Meta metrics such as impressions and link clicks. The changes will also not impact historical data prior to April 27, 2021; breakdowns for historical data will continue to be available.

### Action metrics

Metrics will not be available under the following scenarios:

* When there is an attempted aggregation across multiple attribution settings
* When requested with impacted breakdowns (this restriction only applies for off-Meta and action types).

**Note:** Metrics will be available if querying with `action_attribution_windows=1d_click,7d_click,1d_view,incrementality` (not including the default window).

## Generic breakdowns {#genericbreakdowns}

The following breakdowns are available.

| Breakdown | Description |
| --- | --- |
| `action_device` | The device on which the conversion event you're tracking occurred. For example, \"Desktop\" if someone converted on a desktop computer. |
| `action_canvas_component_name` | Name of a component within a Canvas ad. |
| `action_carousel_card_id` | The ID of the specific carousel card that people engaged with when they saw your ad. |
| `action_carousel_card_name` | The specific carousel card that people engaged with when they saw your ad. The cards are identified by their headlines. |
| `action_destination` | The destination where people go after clicking on your ad. The destination can be your Facebook Page, an external URL for your conversion pixel, or an app configured with the software development kit (SDK). |
| `action_reaction` | The number of reactions on your ads or boosted posts. The reactions button on an ad allows people to share different reactions on its content: Like, Love, Haha, Wow, Sad, or Angry. |
| `action_target_id` | The ID of destination where people go after clicking on your ad. This could be your Facebook Page, an external URL for your conversion pixel or an app configured with the software development kit (SDK). |
| `action_type` | The kind of actions taken on your ad, Page, app, or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses, and more. |
| `action_video_sound` | The sound status (on/off) when someone plays your video ad. |
| `action_video_type` | Video metrics breakdown. |
| `ad_format_asset` | The ID of the ad format asset involved in impression, click, or action. |
| `age` | The age range of the people you've reached. |
| `app_id` | The ID of the application associated with the ad account or campaign requested. The application information, including its ID, is viewable in the [App Dashboard](https://developers.facebook.com/apps/).<br><br>**Note:** This breakdown is only supported by the `total_postbacks` field. |
| `body_asset` | The ID of the body asset involved in impression, click, or action. |
| `call_to_action_asset` | The ID of the call to action asset involved in impression, click, or action. |
| `country` | The country where the people you've reached are located. The country value is based on information, such as a person's hometown, their current city, and the geographical location where they tend to be when they visit Meta. |
| `description_asset` | The ID of the description asset involved in impression, click, or action. |
| `device_platform` | The type of device, mobile or desktop, used by people when they viewed or clicked on an ad, as shown in ads reporting. |
| `dma` | The Designated Market Area (DMA) regions are the 210 geographic areas in the United States in which local television viewing is measured by The Nielsen Company.<br>**Note:** May need to be enabled via Ads Manager reporting breakdown menu |
| `frequency_value` | The number of times an ad in your Reservation campaign was served to each Accounts Center account.<br><br>**Note:** **Availability notice (effective August 6, 2026):** This breakdown may be unavailable for some ad accounts. If a synchronous request returns no results, the account administrator can opt in to this breakdown via Ads Manager, or you can retrieve the data through an asynchronous report job. See the [changelog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/out-of-cycle-changes/occ-2026#may-8--2026) for details. |
| `gender` | Gender of people you've reached. People who don't list their gender are shown as 'not specified'. |
| `hourly_stats_aggregated_by_advertiser_time_zone` | Hourly breakdown aggregated by the time ads were delivered in the advertiser's time zone. For example, if your ads are scheduled to run from 9 AM to 11 AM, but they reach audiences in multiple time zones, they may deliver from 9 AM to 1 PM in the advertiser's time zone. Stats will be aggregated into four groups 9 AM - 10 AM, 10 AM - 11 AM, 11 AM - 12 PM, and 12 PM - 1 PM. |
| `hourly_stats_aggregated_by_audience_time_zone` | Hourly breakdown aggregated by the time ads were delivered in the audiences' time zone. For example, if your ads are scheduled to run from 9:00 am to 11:00 am, but they reach audiences in multiple time zones, they may deliver from 9:00 am to 1:00 pm in the advertiser's time zone. Stats are aggregated into 2 groups: 9:00 am to 10:00 am and 10:00 am to 11:00 am.<br><br>**Note:** **Availability notice (effective August 6, 2026):** This breakdown may be unavailable for some ad accounts. If a synchronous request returns no results, the account administrator can opt in to this breakdown via Ads Manager, or you can retrieve the data through an asynchronous report job. See the [changelog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/out-of-cycle-changes/occ-2026#may-8--2026) for details. |
| `image_asset` | The ID of the image asset involved in impression, click, or action. |
| `impression_device` | The device where your last ad was served to someone on Meta. For example \"iPhone\" if someone viewed your ad on an iPhone.<br><br>**Note:** **Availability notice (effective August 6, 2026):** This breakdown may be unavailable for some ad accounts. If a synchronous request returns no results, the account administrator can opt in to this breakdown via Ads Manager, or you can retrieve the data through an asynchronous report job. This applies to `impression_device` on its own and to any breakdown combination that includes `impression_device`. See the [changelog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/out-of-cycle-changes/occ-2026#may-8--2026) for details. |
| `is_conversion_id_modeled` | A boolean flag that indicates whether the `conversion_bits` are modeled. A `0` indicates `conversion_bits` aren't modeled, and a `1` indicates that `conversion_bits` are modeled.  <br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed` field. |
| `link_url_asset` | The ID of the URL asset involved in impression, click, or action. |
| `place_page_id` | The ID of the place page involved in impression or click.<br><br>**Note:** Account-level insights and `page_place_id` are not compatible with each other, so they cannot be queried together. |
| `platform_position` | Where your ad was shown within a platform, for example on Facebook desktop Feed, or Instagram Mobile Feed. |
| `product_id` | The ID of the product involved in impression, click, or action. |
| `publisher_platform` | Which platform your ad was shown, for example on Facebook, Instagram, or Audience Network. |
| `region` | The regions where the people you've reached are located. The region value is based on information such as a person's hometown, their current city and the geographical location where they tend to be when they visit Facebook. |
| `skan_campaign_id` | The raw campaign ID received as a part of Skan postback from iOS 15+.<br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed` field. |
| `skan_conversion_id` | The assigned Conversion ID (also referred to as Priority ID) of the event or event bundle configured in the application's SKAdNetwork configuration schema. The app events configuration can be viewed and adjusted in Meta Events Manager. You can learn more about [configuring your app events for Apple's SKAdNetwork](http://www.facebook.com/business/help/670955636925518).<br><br>**Note:** This breakdown is only supported by the `total_postbacks` field. |
| `title_asset` | The ID of the title asset involved in impression, click, or action. |
| `user_segment_key` | User segment (ex: new, existing) of Advantage+ Shopping Campaigns (ASC). Existing user is specified by the custom audience in ASC settings. |
| `video_asset` | The ID of the video asset involved in impression, click, or action. |

**Notes**

- Filtering `app_id` and `skan_conversion_id` using the `filtering` field is currently not supported.
- The `dma` breakdown is not available for the `estimated_ad_recall_rate` metric or `video_thruplay_watched_actions` metric.
- The `dma` breakdown employs a sampling methodology to compute unique metrics like reach. In instances where there are a large number of DMA regions with comparatively low volumes, those DMA regions might not be represented in the sample or could be scaled up to a power of 2. Therefore, query the corresponding impressions as well for enhanced accuracy.
- `frequency_value` is used with `reach` only. For example, how frequently a unique user saw an ad.
- By design, `image_asset` and `video_asset` breakdowns are not available at the ad account level for assets used in [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/asset-feed).
- [Ad actions](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats) `video_p25_watched_actions`, `video_p50_watched_actions`, `video_p75_watched_actions`, `video_p95_watched_actions`, and `video_p100_watched_actions` do not support `region` breakdown.
- All Dynamic Creative asset breakdowns only support a limited set of metrics:
| Dynamic Creative Breakdowns | Supported metrics for Dynamic Creative Breakdowns |
| --- | --- |
| - `ad_format_asset`<br>- `body_asset`<br>- `call_to_action_asset`<br>- `description_asset`<br>- `image_asset`<br>- `link_url_asset`<br>- `title_asset`<br>- `video_asset` | - `impressions`<br>- `clicks`<br>- `spend`<br>- `reach`<br>- `actions`<br>- `action_values` |

The following call groups the results by `age` and `gender`.

### cURL
```
curl -G \
  -d "breakdowns=age,gender" \
  -d "fields=impressions" \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/<API_VERSION>/<AD_CAMPAIGN_ID>/insights"
```

```
{
  "data": [
    {
      "impressions": "4",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "age": "13-17",
      "gender": "female"
    },
    {
      "impressions": "17459",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "age": "18-24",
      "gender": "female"
    },
    {
      "impressions": "11086",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "age": "25-34",
      "gender": "female"
    },
    {
      "impressions": "4314",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "age": "25-34",
      "gender": "male"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MgZDZD"
    }
  }
}
```

Show Response

## Hourly breakdowns {#hourlybreakdowns}

Hourly stats are now an available breakdown using the following breakdowns:

* `hourly_stats_aggregated_by_advertiser_time_zone`
* `hourly_stats_aggregated_by_audience_time_zone`

See [Combining Breakdowns](#combiningbreakdowns) for limits on number of breakdowns you may request with the hourly breakdown. Hourly breakdowns do not support unique fields, which are any fields prepended with `unique_*`, `reach` or `frequency`. `reach` and `frequency` fields will return 0 when hourly breakdowns are in use.

### cURL
```
curl -G \
-d "fields=impressions" \
-d "breakdowns=hourly_stats_aggregated_by_audience_time_zone" \
-d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/<AD_CAMPAIGN_ID>/insights"
```

```
{
  "data": [
    {
      "impressions": "1148",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "hourly_stats_aggregated_by_audience_time_zone": "00:00:00 - 00:59:59"
    },
    {
      "impressions": "172",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "hourly_stats_aggregated_by_audience_time_zone": "01:00:00 - 01:59:59"
    },
    {
      "impressions": "2921",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "hourly_stats_aggregated_by_audience_time_zone": "10:00:00 - 10:59:59"
    },
    {
      "impressions": "3685",
      "date_start": "2016-03-05",
      "date_stop": "2016-04-01",
      "hourly_stats_aggregated_by_audience_time_zone": "11:00:00 - 11:59:59"
    },
    ...
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjMZD"
    }
  }
}
```

Show Response

## Action breakdown {#actionsbreakdown}

Group results in the `actions` field. You can use the following breakdowns for `action_breakdowns`:

The following are the possible breakdowns that can be supplied into the `action_breakdowns` field.

If `action_breakdowns` parameter is not specified, `action_type` is implicitly added as the `action_breakdowns`.

## Total count in `actions`

The total count (sum) of all values returned in group results (`actions`).

**Note:** This result may not equal `total_actions` since fields returned in `actions` are hierarchical and include detailed actions not counted.

```
total_actions - 33
    page_engagement - 10
        post_engagement - 10
            link_click - 2
            comment - 3
            post_reaction - 3
            like - 2
    mobile_app_install - 12
    app_custom_event - 11
        app_custom_event.fb_mobile_activate_app - 6
        app_custom_event.other - 5
```

In this example, `post_engagement` is a sum of `link_click`, `comment`, `like`, and `post_reaction`, where `post_reaction` is the count of all reactions, including likes. The `total_actions` field represents a sum of top-level actions for an object, such as `page_engagement`, `mobile_app_install`, and `app_custom_event`.

## Combining breakdowns {#combiningbreakdowns}

Due to storage constraints, only some permutations of breakdowns are available. **Permutations marked with an asterisk (\*) can be joined with `action_type`, `action_target_id` and `action_destination` which is the name for `action_target_id`.**

| Permutation |
| --- |
| `action_converted_product_id` - Under limited availability for Collaborative Ads. |
| `action_type` \* |
| `action_type, action_converted_product_id`  - Under limited availability for Collaborative Ads. |
| `action_target_id` \* |
| `action_device *` |
| `action_device, impression_device` \* |
| `action_device, publisher_platform` \* |
| `action_device, publisher_platform, impression_device` \* |
| `action_device, publisher_platform, platform_position` \* |
| `action_device, publisher_platform, platform_position, impression_device` \* |
| `action_reaction` |
| `action_type, action_reaction` |
| `age` \* |
| `gender` \* |
| `age, gender` \* |
| `app_id, skan_conversion_id ` |
| `country` \* |
| `region` \* |
| `publisher_platform` \* |
| `publisher_platform, impression_device` \* |
| `publisher_platform, platform_position` \* |
| `publisher_platform, platform_position, impression_device` \* |
| `product_id` \* |
| `hourly_stats_aggregated_by_advertiser_time_zone` \* |
| `hourly_stats_aggregated_by_audience_time_zone` \* |
| `action_carousel_card_id / action_carousel_card_name` |
| `action_carousel_card_id / action_carousel_card_name` |
| `action_carousel_card_id / action_carousel_card_name, impression_device` |
| `action_carousel_card_id / action_carousel_card_name, country` |
| `action_carousel_card_id / action_carousel_card_name, age` |
| `action_carousel_card_id / action_carousel_card_name, gender` |
| `action_carousel_card_id / action_carousel_card_name, age, gender` |

### Limitations {#combining-limitations}

- `video_*` fields cannot be requested with any hourly stats breakdowns.
- `video_avg_time_watched_actions` field cannot be requested with the region breakdown.
- `action_type` is implicitly added as the `action_breakdowns` when `action_breakdowns` parameter is not specified.
