<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/insights.md | Scrape: 2026-08-09 | API v26.0 -->

# Ad Account, Insights



The Insights API can return several metrics which are *estimated* or *in-development*. In some cases a metric may be **both ** *estimated and in-development*.

- **Estimated** - Provide directional insights for outcomes that are hard to precisely quantify. They may evolve as we gather more data. See [Ads Help Center, Estimated metrics](https://www.facebook.com/business/help/181058782494426?helpref=faq_content#estimated).

- **In Development** - Still being tested and may change as we improve our methodologies. We encourage you to use it for directional guidance, but please use caution when using it for historical comparisons or strategic planning. See [Ads Help Center, In development metrics](https://www.facebook.com/business/help/181058782494426?helpref=faq_content#indevelopment).

For more information, see [Insights API, Estimated and Deprecated Metrics](https://developers.facebook.com/docs/marketing-api/insights/estimated-in-development)

**Success:** Facebook will no longer be able to aggregate non-inline conversion metric values across iOS 14.5 and non-iOS 14.5 campaigns due to differences in attribution logic. Querying across iOS 14.5 and non-iOS 14.5 campaigns will result in no data getting returned for non-inline conversion metrics such as app installs and purchases. Inline event metrics like impressions, link clicks, and video views, however, can still be aggregated. Please visit our [changelog](https://developers.facebook.com/docs/graph-api/changelog/non-versioned-changes/jan-19-2021) for more information.

**Warning:** The `date_preset = lifetime` parameter is disabled in Graph API v10.0 and replaced with `date_preset = maximum`, which returns a maximum of 37 months of data. For v9.0 and below, `date_preset = maximum` will be enabled on May 25, 2021, and any `lifetime` calls will default to `maximum` and return only 37 months of data.

## Reading

Provides insights on your advertising performance. Allows for deduped metrics across child objects, such as `unique_clicks`, sorting of metrics, and async reporting.

#### Example

### HTTP
```
GET /v25.0/<AD_SET_ID>/insights?fields=impressions&breakdown=publisher_platform HTTP/1.1
Host: graph.facebook.com
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/<AD_SET_ID>/insights?fields=impressions&breakdown=publisher_platform',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

### JavaScript SDK
```
/* make the API call */
FB.api(
    "/<AD_SET_ID>/insights",
    {
        "fields": "impressions",
        "breakdown": "publisher_platform"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

### Android SDK
```
Bundle params = new Bundle();
params.putString("fields", "impressions");
params.putString("breakdown", "publisher_platform");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/<AD_SET_ID>/insights",
    params,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

### iOS SDK
```
NSDictionary *params = @{
  @"fields": @"impressions",
  @"breakdown": @"publisher_platform",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/<AD_SET_ID>/insights"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

### cURL
```
curl -X GET -G \
  -d 'fields="impressions"' \
  -d 'breakdown="publisher_platform"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/insights
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%3CAD_SET_ID%3E%2Finsights%3Ffields%3Dimpressions%26breakdown%3Dpublisher_platform&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `action_attribution_windows`<br><br>*list<enum{1d_view, 7d_view, 28d_view, 1d_click, 7d_click, 28d_click, 1d_ev, dda, default, 7d_view_first_conversion, 28d_view_first_conversion, 7d_view_all_conversions, 28d_view_all_conversions, skan_view, skan_click, skan_click_second_postback, skan_view_second_postback, skan_click_third_postback, skan_view_third_postback}>* | **Default value: **`default`<br>The attribution window for the actions. <br><br>The attribution window determines the window (e.g. 7d) and engagement type (e.g click) that’s used as a filter to report actions. See [About attribution settings and models](https://www.facebook.com/business/help/460276478298895?id=561906377587030) for examples.<br><br>The `default` option means `["7d_click","1d_view"]`.<br> |
| `action_breakdowns`<br><br>*list<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}>* | **Default value: **`Vec`<br>How to break down action results. Supports more than one breakdowns. Default value is ["action_type"].<br><br><br>Note: you must also include `actions` field whenever `action_breakdowns` is specified.<br> |
| `action_report_time`<br><br>*enum{impression, conversion, mixed, lifetime}* | Determines the report time of action stats. For example, if a person<br>saw the ad on Jan 1st but converted on Jan 2nd, when you query the API<br>with `action_report_time=impression`, you see a conversion on Jan<br>1st. When you query the API with `action_report_time=conversion`, you see a conversion on Jan 2nd.<br> |
| `breakdowns`<br><br>*list<enum{ad_extension_domain, ad_extension_url, ad_format_asset, age, app_id, body_asset, breakdown_ad_objective, breakdown_reporting_ad_id, call_to_action_asset, coarse_conversion_value, comscore_market, country, creative_automation_asset_id, creative_relaxation_asset_type, crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id, crm_advertiser_vertical_id, crm_ult_advertiser_id, description_asset, fidelity_type, flexible_format_asset_type, gen_ai_asset_type, gender, hsid, image_asset, impression_device, instagram_ads_follow_type, instagram_ads_instagram_media_product_type, instagram_ads_time_since_creation_bucket, internal_campaign_id, is_auto_advance, is_conversion_id_modeled, is_rendered_as_delayed_skip_ad, landing_destination, link_url_asset, mdsa_landing_destination, media_asset_url, media_creator, media_destination_url, media_format, media_origin_url, media_text_content, media_type, pa_creator_ig_handle, postback_sequence_index, product_brand_breakdown, product_category_breakdown, product_custom_label_0_breakdown, product_custom_label_1_breakdown, product_custom_label_2_breakdown, product_custom_label_3_breakdown, product_custom_label_4_breakdown, product_group_content_id_breakdown, product_id, redownload, region, rta_ugc_topic, skan_campaign_id, skan_conversion_id, skan_version, sot_attribution_model_type, sot_attribution_window, sot_channel, sot_event_type, sot_source, title_asset, user_persona_id, user_persona_name, video_asset, zip, rule_set_id, rule_set_name, dma, frequency_value, overlap_segment, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, mmm, place_page_id, publisher_platform, platform_position, device_platform, standard_event_content_type, conversion_destination, signal_source_bucket, reels_trending_topic, marketing_messages_btn_name, impression_view_time_advertiser_hour_v2}>* | How to break down the result. For more than one breakdown, only certain combinations are available: See [Combining Breakdowns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/breakdowns#combiningbreakdowns) and the [Breakdowns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights/breakdowns) page. The option `impression_device` cannot be used by itself.<br> |
| `date_preset`<br><br>*enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year}* | **Default value: **`last_30d`<br>Represents a relative time range. This field is ignored if `time_range` or `time_ranges` is specified.<br> |
| `default_summary`<br><br>*boolean* | **Default value: **`false`<br>Determine whether to return a summary. If `summary` is set, this param is be ignored; otherwise, a summary section with the same fields as specified by `fields` will be included in the summary section.<br> |
| `export_columns`<br><br>*list<string>* | Select fields on the exporting report file. It is an optional param. Exporting columns are equal to the param fields, if you leave this param blank<br> |
| `export_format`<br><br>*string* | Set the format of exporting report file. If the export_format is set, Report file is asyncrhonizely generated. It expects ["xls", "csv"].<br> |
| `export_name`<br><br>*string* | Set the file name of the exporting report.<br> |
| `fields`<br><br>*list<string>* | Fields to be retrieved. Default behavior is to return impressions and spend.<br> |
| `filtering`<br><br>*list<Filter Object>* | **Default value: **`Vec`<br>Filters on the report data. This parameter is an array of filter objects.<br><br><br>`field` *string*<br>**[required]**<br><br><br>`operator` *enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP}*<br>**[required]**<br><br><br>`value` *string*<br>**[required]**<br> |
| `level`<br><br>*enum {ad, adset, campaign, account}* | Represents the level of result.<br> |
| `limit`<br><br>*integer* | limit<br> |
| `product_id_limit`<br><br>*integer* | Maximum number of product ids to be returned for each ad when breakdown by `product_id`.<br> |
| `sort`<br><br>*list<string>* | **Default value: **`Vec`<br>Field to sort the result, and direction of sorting. You can specify sorting direction by appending "_ascending" or "_descending" to the sort field. For example, "reach_descending". For actions, you can sort by action type in form of "actions:<action_type>". For example, ["actions:link_click_ascending"]. This array supports no more than one element. By default, the sorting direction is ascending.<br> |
| `summary`<br><br>*list<string>* | If this param is used, a summary section will be included, with the fields listed in this param.<br> |
| `summary_action_breakdowns`<br><br>*list<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}>* | **Default value: **`Vec`<br>Similar to `action_breakdowns`, but applies to summary. Default value is ["action_type"].<br> |
| `time_increment`<br><br>*enum{monthly, all_days} or integer* | **Default value: **`all_days`<br>If it is an integer, it is the number of days from 1 to 90. After you pick a reporting period by using `time_range` or `date_preset`, you may choose to have the results for the whole period, or have results for smaller time slices. If "all_days" is used, it means one result set for the whole period. If "monthly" is used, you will get one result set for each calendar month in the given period. Or you can have one result set for each N-day period specified by this param. This param is ignored if `time_ranges` is specified.<br> |
| `time_range`<br><br>*{'since':YYYY-MM-DD,'until':YYYY-MM-DD}* | A single time range object. UNIX timestamp not supported. This param is ignored if `time_ranges` is provided.<br><br><br>`since` *datetime*<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br><br><br>`until` *datetime*<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br> |
| `time_ranges`<br><br>*list<{'since':YYYY-MM-DD,'until':YYYY-MM-DD}>* | Array of time range objects. Time ranges can overlap, for example to return cumulative insights. Each time range will have one result set. You cannot have more granular results with `time_increment` setting in this case.If `time_ranges` is specified, `date_preset`, `time_range` and `time_increment` are ignored.<br><br><br>`since` *datetime*<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br><br><br>`until` *datetime*<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br> |
| `use_account_attribution_setting`<br><br>*boolean* | **Default value: **`false`<br>When this parameter is set to `true`, your ads results will be shown using the attribution settings defined for the ad account.<br> |
| `use_unified_attribution_setting`<br><br>*boolean* | When this parameter is set to `true`, your ads results will be shown using unified attribution settings defined at ad set level and parameter `use_account_attribution_setting` will be ignored.<br> |

#### Fields

Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {},
"summary": {}
}
```

##### data

A list of AdsInsights nodes.

##### paging

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).

##### summary

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like summary=__type__).

| Field | Description |
| --- | --- |
| `account_currency`<br><br>*string* | Currency that is used by your ad account.<br> |
| `account_id`<br><br>*numeric string* | The ID number of your ad account, which groups your advertising activity. Your ad account includes your campaigns, ads and billing.<br><br><br>**[default]**<br> |
| `account_name`<br><br>*string* | The name of your ad account, which groups your advertising activity. Your ad account includes your campaigns, ads and billing.<br> |
| `action_values`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total value of all conversions attributed to your ads.<br> |
| `actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total number of actions Accounts Center accounts took that are attributed to your ads. Actions may include engagement, clicks or conversions.<br> |
| `actions_per_impression`<br><br>*numeric string* | Total number of actions divided by the number of impessions.<br> |
| `actions_results`<br><br>*[AdsActionStats](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of actions as a result of your ad. The results you see here are based on your objective.<br> |
| `activity_recency`<br><br>*string* | activity_recency<br> |
| `ad_click_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | ad_click_actions<br> |
| `ad_format_asset`<br><br>*string* | ad_format_asset<br> |
| `ad_id`<br><br>*numeric string* | The unique ID of the ad you're viewing in reporting.<br><br><br>**[default]**<br> |
| `ad_impression_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | ad_impression_actions<br> |
| `ad_name`<br><br>*string* | The name of the ad you're viewing in reporting.<br> |
| `adjusted_offline_purchase`<br><br>*numeric string* | The number of purchase events that occurred offline and are attributed to your ads, after adjusting attribution settings and based on information received from your offline event set.<br> |
| `adset_end`<br><br>*string* | The date your ad set is scheduled to stop.<br> |
| `adset_id`<br><br>*numeric string* | The unique ID of the ad set you're viewing in reporting. An ad set is a group of ads that share the same budget, schedule, delivery optimization and targeting.<br><br><br>**[default]**<br> |
| `adset_name`<br><br>*string* | The name of the ad set you're viewing in reporting. An ad set is a group of ads that share the same budget, schedule, delivery optimization and targeting.<br> |
| `adset_start`<br><br>*string* | The date your ad set is scheduled to start running.<br> |
| `anchor_event_attribution_setting`<br><br>*string* | anchor_event_attribution_setting<br> |
| `anchor_events_performance_indicator`<br><br>*string* | anchor_events_performance_indicator<br> |
| `app_store_clicks`<br><br>*numeric string* | The number of clicks on links to an app store in your ads.<br> |
| `attention_events_per_impression`<br><br>*numeric string* | attention_events_per_impression<br> |
| `attention_events_unq_per_reach`<br><br>*numeric string* | attention_events_unq_per_reach<br> |
| `attribution_setting`<br><br>*string* | The default attribution window to be used when attribution result is calculated. Each ad set has its own attribution setting value. The attribution setting for campaign or account is calculated based on existing ad sets.<br> |
| `auction_bid`<br><br>*numeric string* | auction_bid<br> |
| `auction_competitiveness`<br><br>*numeric string* | auction_competitiveness<br> |
| `auction_max_competitor_bid`<br><br>*numeric string* | auction_max_competitor_bid<br> |
| `body_asset`<br><br>*AdAssetBody* | body_asset<br> |
| `buying_type`<br><br>*string* | The method by which you pay for and target ads in your campaigns: through dynamic auction bidding, fixed-price bidding, or reach and frequency buying. This field is currently only visible at the campaign level.<br> |
| `call_to_action_clicks`<br><br>*numeric string* | The number of times Accounts Center accounts clicked the call-to-action button on your ad.<br> |
| `campaign_end`<br><br>*string* | The date your campaign is scheduled to stop.<br> |
| `campaign_id`<br><br>*numeric string* | The unique ID number of the ad campaign you're viewing in reporting. Your campaign contains ad sets and ads.<br><br><br>**[default]**<br> |
| `campaign_name`<br><br>*string* | The name of the ad campaign you're viewing in reporting. Your campaign contains ad sets and ads.<br> |
| `campaign_start`<br><br>*string* | The date your campaign is scheduled to start.<br> |
| `cancel_subscription_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cancel_subscription_actions<br> |
| `canvas_avg_view_percent`<br><br>*numeric string* | The average percentage of the Instant Experience that Accounts Center accounts saw. An Instant Experience is a screen that opens after someone interacts with your ad on a mobile device. It may include a series of interactive or multimedia components, including video, images product catalog and more.<br> |
| `canvas_avg_view_time`<br><br>*numeric string* | The average total time, in seconds, that Accounts Center accounts spent viewing an Instant Experience. An Instant Experience is a screen that opens after someone interacts with your ad on a mobile device. It may include a series of interactive or multimedia components, including video, images product catalog and more.<br> |
| `card_views`<br><br>*numeric string* | The number of times Accounts Center accounts viewed a product from your catalog in an ad. If you're using a carousel format, Accounts Center accounts may view multiple products in a single ad. Counts are updated daily, views for today are not included. This metric is currently in beta, and is only available for ads connected to a product catalog. This metric is in development.<br> |
| `catalog_segment_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of actions performed attributed to your ads promoting your catalog segment, broken down by action type.<br> |
| `catalog_segment_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total value of all conversions from your catalog segment attributed to your ads.<br> |
| `catalog_segment_value_in_catalog_currency`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total value of all conversions from your catalog segment attributed to your ads, in the same currency as the catalog.<br> |
| `catalog_segment_value_mobile_purchase_roas`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total return on ad spend (ROAS) from mobile app purchases for your catalog segment.<br> |
| `catalog_segment_value_omni_purchase_roas`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total return on ad spend (ROAS) from all purchases for your catalog segment.<br> |
| `catalog_segment_value_website_purchase_roas`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total return on ad spend (ROAS) from website purchases for your catalog segment.<br> |
| `clicks`<br><br>*numeric string* | The number of clicks on your ads.<br> |
| `coarse_conversion_value`<br><br>*string* | Allows advertisers and ad networks to receive directional post-install quality insights when the volume of campaign conversions isn't high enough to meet the privacy threshold needed to unlock the standard conversion value. Possible values of this breakdown are `low`, `medium` and `high`.<br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed_v4` field.<br> |
| `comparison_node`<br><br>*AdsInsightsComparison* | Parent node that encapsulates fields to be compared (current time range Vs comparison time range)<br> |
| `comscore_market`<br><br>*string* | comscore_market<br> |
| `conditional_time_spent_ms_over_10s_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conditional_time_spent_ms_over_10s_actions<br> |
| `conditional_time_spent_ms_over_15s_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conditional_time_spent_ms_over_15s_actions<br> |
| `conditional_time_spent_ms_over_2s_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conditional_time_spent_ms_over_2s_actions<br> |
| `conditional_time_spent_ms_over_3s_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conditional_time_spent_ms_over_3s_actions<br> |
| `conditional_time_spent_ms_over_6s_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conditional_time_spent_ms_over_6s_actions<br> |
| `configurable_attribution_action`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | configurable attribution action<br> |
| `configurable_attribution_actionvalue`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | configurable attribution actionvalue<br> |
| `configurable_audience_overlap_reach`<br><br>*numeric string* | configurable audience overlap reach<br> |
| `configurable_reachbyfrequency_action`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | configurable reachbyfrequency action<br> |
| `configurable_reachbyfrequency_converters_count`<br><br>*numeric string* | configurable reachbyfrequency converters count<br> |
| `configurable_reachbyfrequency_impressions_cost`<br><br>*numeric string* | configurable reachbyfrequency impressions cost<br> |
| `configurable_reachbyfrequency_impressions_count`<br><br>*numeric string* | configurable reachbyfrequency impressions count<br> |
| `configurable_reachbyfrequency_reach`<br><br>*numeric string* | configurable reachbyfrequency reach<br> |
| `contact_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | contact_actions<br> |
| `contact_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | contact_value<br> |
| `conversion_values`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conversion_values<br> |
| `conversions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | conversions<br> |
| `converted_product_app_custom_event_fb_mobile_purchase`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_app_custom_event_fb_mobile_purchase<br> |
| `converted_product_app_custom_event_fb_mobile_purchase_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_app_custom_event_fb_mobile_purchase_value<br> |
| `converted_product_offline_purchase`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_offline_purchase<br> |
| `converted_product_offline_purchase_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_offline_purchase_value<br> |
| `converted_product_omni_purchase`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_omni_purchase<br> |
| `converted_product_omni_purchase_values`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_omni_purchase_values<br> |
| `converted_product_quantity`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of products purchased which are recorded by your merchant partner's pixel or app SDK for a given product ID and driven by your ads. Has to be used together with converted product ID breakdown.<br> |
| `converted_product_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The value of purchases recorded by your merchant partner's pixel or app SDK for a given product ID and driven by your ads. Has to be used together with converted product ID breakdown.<br> |
| `converted_product_website_pixel_purchase`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_website_pixel_purchase<br> |
| `converted_product_website_pixel_purchase_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | converted_product_website_pixel_purchase_value<br> |
| `cost_per_15_sec_video_view`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_15_sec_video_view<br> |
| `cost_per_2_sec_continuous_video_view`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_2_sec_continuous_video_view<br> |
| `cost_per_action_result`<br><br>*[AdsActionStats](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average you paid for each action associated with your objective.<br> |
| `cost_per_action_type`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average cost of a relevant action.<br> |
| `cost_per_ad_click`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_ad_click<br> |
| `cost_per_completed_video_view`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_completed_video_view<br> |
| `cost_per_contact`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_contact<br> |
| `cost_per_conversion`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_conversion<br> |
| `cost_per_customize_product`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_customize_product<br> |
| `cost_per_dda_countby_convs`<br><br>*numeric string* | cost_per_dda_countby_convs<br> |
| `cost_per_donate`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_donate<br> |
| `cost_per_dwell`<br><br>*numeric string* | The average cost per 1,000 Dwells<br> |
| `cost_per_dwell_3_sec`<br><br>*numeric string* | cost_per_dwell_3_sec<br> |
| `cost_per_dwell_5_sec`<br><br>*numeric string* | cost_per_dwell_5_sec<br> |
| `cost_per_dwell_7_sec`<br><br>*numeric string* | cost_per_dwell_7_sec<br> |
| `cost_per_find_location`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_find_location<br> |
| `cost_per_inline_link_click`<br><br>*numeric string* | The average cost of each inline link click.<br> |
| `cost_per_inline_post_engagement`<br><br>*numeric string* | The average cost of each inline post engagement.<br> |
| `cost_per_objective_result`<br><br>*list<AdsInsightsResult>* | The average cost per objective result from your ads. Objective results are what you're trying to get the most of in your ad campaign, based on the objective you selected.<br> |
| `cost_per_one_thousand_ad_impression`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_one_thousand_ad_impression<br> |
| `cost_per_outbound_click`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average cost for each outbound click.<br> |
| `cost_per_result`<br><br>*list<AdsInsightsResult>* | The average cost per result from your ads.<br> |
| `cost_per_schedule`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_schedule<br> |
| `cost_per_start_trial`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_start_trial<br> |
| `cost_per_submit_application`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_submit_application<br> |
| `cost_per_subscribe`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_subscribe<br> |
| `cost_per_thruplay`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average cost for each ThruPlay. This metric is in development.<br> |
| `cost_per_total_action`<br><br>*numeric string* | The average cost of a relevant action.<br> |
| `cost_per_unique_action_type`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average cost of each unique action. This metric is estimated.<br> |
| `cost_per_unique_click`<br><br>*numeric string* | The average cost for each unique click (all). This metric is estimated.<br> |
| `cost_per_unique_conversion`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | cost_per_unique_conversion<br> |
| `cost_per_unique_inline_link_click`<br><br>*numeric string* | The average cost of each unique inline link click. This metric is estimated.<br> |
| `cost_per_unique_outbound_click`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average cost for each unique outbound click. This metric is estimated.<br> |
| `country`<br><br>*string* | country<br> |
| `cpc`<br><br>*numeric string* | The average cost for each click (all).<br> |
| `cpm`<br><br>*numeric string* | The average cost for 1,000 impressions.<br> |
| `cpp`<br><br>*numeric string* | The average cost to reach 1,000 Accounts Center accounts. This metric is estimated.<br> |
| `created_time`<br><br>*string* | created_time<br> |
| `creative_automation_asset_id`<br><br>*AdAssetMedia* | creative_automation_asset_id<br> |
| `creative_diversity_data`<br><br>*list<CreativeDiversityData>* | creative diversity data<br> |
| `creative_diversity_label`<br><br>*string* | creative diversity label<br> |
| `creative_diversity_score`<br><br>*string* | creative diversity score<br> |
| `creative_fatigue_summary`<br><br>*list<CreativeFatigueSummary>* | creative fatigue summary<br> |
| `creative_fatigued_ads`<br><br>*list<CreativeFatiguedAds>* | creative fatigued ads<br> |
| `creative_relaxation_asset_type`<br><br>*string* | creative_relaxation_asset_type<br> |
| `ctr`<br><br>*numeric string* | The percentage of times Accounts Center accounts saw your ad and performed a click (all).<br> |
| `customize_product_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | customize_product_actions<br> |
| `customize_product_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | customize_product_value<br> |
| `date_start`<br><br>*string* | The start date for your data. This is controlled by the date range you've selected for your reporting view.<br><br><br>**[default]**<br> |
| `date_stop`<br><br>*string* | The end date for your data. This is controlled by the date range you've selected for your reporting view.<br><br><br>**[default]**<br> |
| `dda_countby_convs`<br><br>*numeric string* | dda_countby_convs<br> |
| `dda_results`<br><br>*list<AdsInsightsDdaResult>* | dda_results<br> |
| `deduping_1st_source_ratio`<br><br>*numeric string* | This is the auction removal rate for the ad set with the highest amount of audience overlap with the selected ad set.<br> |
| `deduping_2nd_source_ratio`<br><br>*numeric string* | This is the auction removal rate for the ad set with the second highest amount of audience overlap with the selected ad set.<br> |
| `deduping_3rd_source_ratio`<br><br>*numeric string* | This is the auction removal rate for the ad set with the third highest amount of audience overlap with the selected ad set.<br> |
| `deduping_ratio`<br><br>*numeric string* | The total auction removal rate is the percentage of auctions that an ad set did not compete in due to audience overlap with other ad sets.<br> |
| `deeplink_clicks`<br><br>*numeric string* | The number of clicks on links to specific parts of an app.<br> |
| `description_asset`<br><br>*AdAssetDescription* | description_asset<br> |
| `device_platform`<br><br>*string* | device_platform<br> |
| `dma`<br><br>*string* | dma<br> |
| `donate_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | donate_actions<br> |
| `donate_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | donate_value<br> |
| `dwell_3_sec`<br><br>*numeric string* | dwell_3_sec<br> |
| `dwell_5_sec`<br><br>*numeric string* | dwell_5_sec<br> |
| `dwell_7_sec`<br><br>*numeric string* | dwell_7_sec<br> |
| `dwell_rate`<br><br>*numeric string* | The number of times someone dwells on your display ad divided by the total number of impressions<br> |
| `fidelity_type`<br><br>*string* | To differentiate StoreKit-rendered ads from view-through ads, SKAdNetwork defines a fidelity-type parameter, which you include in the ad signature and receive in the install-validation postback. Use a fidelity-type value of `1` for StoreKit-rendered ads and attributable web ads, and `0` for view-through ads.<br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed_v4` field.<br> |
| `find_location_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | find_location_actions<br> |
| `find_location_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | find_location_value<br> |
| `flexible_format_asset_type`<br><br>*string* | flexible_format_asset_type<br> |
| `frequency`<br><br>*numeric string* | The average number of times each person saw your ad. This metric is estimated.<br> |
| `frequency_value`<br><br>*string* | frequency_value<br> |
| `full_view_impressions`<br><br>*numeric string* | The number of Full Views on your Page's posts as a result of your ad.<br> |
| `full_view_reach`<br><br>*numeric string* | The number of Accounts Center accounts that performed a Full View on your Page's post as a result of your ad.<br> |
| `gen_ai_asset_type`<br><br>*string* | gen_ai_asset_type<br> |
| `hourly_stats_aggregated_by_advertiser_time_zone`<br><br>*string* | hourly_stats_aggregated_by_advertiser_time_zone<br> |
| `hourly_stats_aggregated_by_audience_time_zone`<br><br>*string* | hourly_stats_aggregated_by_audience_time_zone<br> |
| `hsid`<br><br>*string* | The `hsid` key is available for ad impressions that use SKAdNetwork 4 and later. This integer can have up to four digits. You can encode information about your advertisement in each set of digits; you may receive two, three, or all four digits of the sourceIdentifier in the first winning postback, depending on the ad impression's postback data tier.<br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed_v4` field.<br> |
| `image_asset`<br><br>*AdAssetImage* | image_asset<br> |
| `impression_device`<br><br>*string* | impression_device<br> |
| `impressions`<br><br>*numeric string* | The number of times your ads were on screen.<br><br><br>**[default]**<br> |
| `impressions_auto_refresh`<br><br>*string* | impressions_auto_refresh<br> |
| `impressions_gross`<br><br>*string* | impressions_gross<br> |
| `inline_link_click_ctr`<br><br>*numeric string* | The percentage of time Accounts Center accounts saw your ads and performed an inline link click.<br> |
| `inline_link_clicks`<br><br>*numeric string* | The number of clicks on links to select destinations or experiences, on or off Facebook-owned properties. Inline link clicks use a fixed 1-day-click attribution window.<br> |
| `inline_post_engagement`<br><br>*numeric string* | The total number of actions that Accounts Center accounts take involving your ads. Inline post engagements use a fixed 1-day-click attribution window.<br> |
| `instagram_upcoming_event_reminders_set`<br><br>*numeric string* | instagram_upcoming_event_reminders_set<br> |
| `instant_experience_clicks_to_open`<br><br>*numeric string* | instant_experience_clicks_to_open<br> |
| `instant_experience_clicks_to_start`<br><br>*numeric string* | instant_experience_clicks_to_start<br> |
| `instant_experience_outbound_clicks`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | instant_experience_outbound_clicks<br> |
| `interactive_component_tap`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | interactive_component_tap<br> |
| `is_auto_advance`<br><br>*string* | is_auto_advance<br> |
| `landing_page_view_per_link_click`<br><br>*numeric string* | landing_page_view_per_link_click<br> |
| `marketing_messages_delivered`<br><br>*numeric string* | The number of messages your business sent to customers that were delivered. Some messages may not be delivered, such as when a customer's device is out of service. This metric doesn’t include messages delivered to Europe and Japan. In some cases, this metric may be estimated and may differ from what’s shown on your invoice due to small variations in data processing.<br> |
| `marketing_messages_delivery_rate`<br><br>*numeric string* | The number of messages delivered divided by the number of messages sent. Some messages may not be delivered, such as when a customer's device is out of service. This metric doesn't include messages sent to Europe and Japan.<br> |
| `marketing_messages_read_rate_benchmark`<br><br>*string* | We calculate this metric as the 75th percentile of read rates across similar businesses, representing the percentage of messages read out of total messages delivered.<br> |
| `media_asset`<br><br>*AdAssetMedia* | media_asset<br> |
| `mobile_app_purchase_roas`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total return on ad spend (ROAS) from mobile app purchases. This is based on the value that you assigned when you set up the app event. For information on how it's calculated, please refer to https://www.facebook.com/business/help/1848669175353398<br> |
| `multi_event_conversion_attribution_setting`<br><br>*string* | multi_event_conversion_attribution_setting<br> |
| `newsfeed_avg_position`<br><br>*numeric string* | The average position where your ad was inserted into news feeds on mobile and desktop. Position 1 is the one at the top of the feed.<br> |
| `newsfeed_clicks`<br><br>*numeric string* | The total number of clicks your ad received in news feed, on mobile and desktop.<br> |
| `newsfeed_impressions`<br><br>*numeric string* | The total number of times your ad was inserted into news feeds, on mobile and desktop.<br> |
| `objective`<br><br>*string* | The objective reflecting the goal you want to achieve with your advertising. It may be different from the selected objective of the campaign in some cases.<br> |
| `objective_result_rate`<br><br>*list<AdsInsightsResult>* | The number of objective results you received divided by the number of impressions.<br> |
| `objective_results`<br><br>*list<AdsInsightsResult>* | The number of responses you wanted to achieve from your ad campaign, based on your selected objective. For example, if you selected promote your Page as your campaign objective, this metric shows the number of Page likes that happened as a result of your ads.<br> |
| `opportunity_score_l4`<br><br>*numeric string* | opportunity score l4<br> |
| `optimization_goal`<br><br>*string* | The optimization goal you selected for your ad or ad set. Your optimization goal reflects what you want to optimize for the ads.<br> |
| `outbound_clicks`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of clicks on links that take Accounts Center accounts off Facebook-owned properties.<br> |
| `outbound_clicks_ctr`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The percentage of times Accounts Center accounts saw your ad and performed an outbound click.<br> |
| `performance_indicator`<br><br>*string* | performance_indicator<br> |
| `platform_position`<br><br>*string* | platform_position<br> |
| `postback_sequence_index`<br><br>*string* | Sequence of postbacks received from SkAdNetwork API version 4.0. Possible values of this breakdown are `0` (first postback), `1` (second postback) and `2` (third postback).<br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed_v4` field.<br> |
| `private_attribution_conversions`<br><br>*unsigned integer* | private_attribution_conversions<br> |
| `product_brand`<br><br>*string* | product_brand<br> |
| `product_brand_breakdown`<br><br>*string* | product_brand_breakdown<br> |
| `product_category`<br><br>*string* | product_category<br> |
| `product_category_breakdown`<br><br>*string* | product_category_breakdown<br> |
| `product_content_id`<br><br>*string* | product_content_id<br> |
| `product_custom_label_0`<br><br>*string* | product_custom_label_0<br> |
| `product_custom_label_0_breakdown`<br><br>*string* | product_custom_label_0_breakdown<br> |
| `product_custom_label_1`<br><br>*string* | product_custom_label_1<br> |
| `product_custom_label_1_breakdown`<br><br>*string* | product_custom_label_1_breakdown<br> |
| `product_custom_label_2`<br><br>*string* | product_custom_label_2<br> |
| `product_custom_label_2_breakdown`<br><br>*string* | product_custom_label_2_breakdown<br> |
| `product_custom_label_3`<br><br>*string* | product_custom_label_3<br> |
| `product_custom_label_3_breakdown`<br><br>*string* | product_custom_label_3_breakdown<br> |
| `product_custom_label_4`<br><br>*string* | product_custom_label_4<br> |
| `product_custom_label_4_breakdown`<br><br>*string* | product_custom_label_4_breakdown<br> |
| `product_custom_number_0`<br><br>*string* | product_custom_number_0<br> |
| `product_custom_number_1`<br><br>*string* | product_custom_number_1<br> |
| `product_custom_number_2`<br><br>*string* | product_custom_number_2<br> |
| `product_custom_number_3`<br><br>*string* | product_custom_number_3<br> |
| `product_custom_number_4`<br><br>*string* | product_custom_number_4<br> |
| `product_group_content_id`<br><br>*string* | product_group_content_id<br> |
| `product_group_content_id_breakdown`<br><br>*string* | product_group_content_id_breakdown<br> |
| `product_group_retailer_id`<br><br>*string* | product_group_retailer_id<br> |
| `product_id`<br><br>*string* | product_id<br> |
| `product_name`<br><br>*string* | product_name<br> |
| `product_retailer_id`<br><br>*string* | product_retailer_id<br> |
| `product_set_id_breakdown`<br><br>*string* | product_set_id_breakdown<br> |
| `product_vendor_id`<br><br>*string* | product_vendor_id<br> |
| `product_vendor_id_breakdown`<br><br>*string* | product_vendor_id_breakdown<br> |
| `product_views`<br><br>*string* | product_views<br> |
| `promoted_product_set_result`<br><br>*string* | promoted product set result<br> |
| `publisher_platform`<br><br>*string* | publisher_platform<br> |
| `purchase_per_landing_page_view`<br><br>*numeric string* | purchase_per_landing_page_view<br> |
| `purchase_roas`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total return on ad spend (ROAS) from purchases. This is based on information received from one or more of your connected Facebook Business Tools and attributed to your ads. For information on how it's calculated, please refer to https://www.facebook.com/business/help/274294333328345<br> |
| `qualifying_question_qualify_answer_rate`<br><br>*numeric string* | qualifying_question_qualify_answer_rate<br> |
| `reach`<br><br>*numeric string* | The number of Accounts Center accounts that saw your ads at least once. Reach is different from impressions, which may include multiple views of your ads by the same Accounts Center accounts. This metric is estimated.<br> |
| `recurring_subscription_payment_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | recurring_subscription_payment_actions<br> |
| `redownload`<br><br>*string* | Boolean flag that indicates the customer redownloaded and reinstalled the app when the value is true. A `1` indicates customer has reinstalled the app and `0` indicates that customer hasn’t reinstalled the app<br><br>**Note:** This breakdown is only supported by the `total_postbacks_detailed_v4` field.<br> |
| `reels_trending_topic`<br><br>*string* | reels_trending_topic<br> |
| `result_rate`<br><br>*list<AdsInsightsResult>* | The percentage of results you received out of all the views of your ads.<br> |
| `result_values_performance_indicator`<br><br>*string* | result_values_performance_indicator<br> |
| `results`<br><br>*list<AdsInsightsResult>* | The number of times your ad achieved an outcome, based on the objective and settings you selected.<br> |
| `rta_ugc_topic`<br><br>*string* | rta_ugc_topic<br> |
| `rule_asset`<br><br>*AdAssetRule* | rule_asset<br> |
| `rule_set_id`<br><br>*string* | rule_set_id<br> |
| `rule_set_name`<br><br>*string* | rule_set_name<br> |
| `schedule_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | schedule_actions<br> |
| `schedule_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | schedule_value<br> |
| `shops_assisted_purchases`<br><br>*string* | shops_assisted_purchases<br> |
| `skan_version`<br><br>*string* | skan_version<br> |
| `social_spend`<br><br>*numeric string* | The total amount you've spent so far for your ads showed with social information. (ex: Jane Doe likes this).<br> |
| `spend`<br><br>*numeric string* | The estimated total amount of money you've spent on your campaign, ad set or ad during its schedule. This metric is estimated.<br><br><br>**[default]**<br> |
| `start_trial_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | start_trial_actions<br> |
| `start_trial_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | start_trial_value<br> |
| `submit_application_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | submit_application_actions<br> |
| `submit_application_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | submit_application_value<br> |
| `subscribe_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | subscribe_actions<br> |
| `subscribe_value`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | subscribe_value<br> |
| `thumb_stops`<br><br>*numeric string* | The number of times someone dwells on your display ad.<br> |
| `title_asset`<br><br>*AdAssetTitle* | title_asset<br> |
| `today_spend`<br><br>*numeric string* | How much money you've spent on your campaign, ad set or ad since 12 AM today (in your ad account's time zone). If you set a daily budget, you'll see your progress toward it here to determine how much more you can spend before the day ends. This metric is estimated.<br> |
| `total_action_value`<br><br>*numeric string* | total_action_value<br> |
| `total_actions`<br><br>*numeric string* | The total number of actions Accounts Center accounts took that are attributed to your ads. Actions may include engagement, clicks or conversions.<br> |
| `total_card_view`<br><br>*string* | total_card_view<br> |
| `total_unique_actions`<br><br>*numeric string* | The number of Accounts Center accounts that took an action that was attributed to your ads. This metric is estimated.<br> |
| `unique_impressions`<br><br>*numeric string* | The number of Accounts Center accounts that saw your ads at least once.<br> |
| `updated_time`<br><br>*string* | updated_time<br> |
| `user_segment_key`<br><br>*string* | user_segment_key<br> |
| `video_30_sec_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video played for at least 30 seconds, or for nearly its total length if it's shorter than 30 seconds. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video.<br> |
| `video_6_sec_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | video 6 sec watched actions<br> |
| `video_asset`<br><br>*AdAssetVideo* | video_asset<br> |
| `video_avg_time_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The average time a video was played, including any time spent replaying the video for a single impression.<br> |
| `video_complete_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | This shows the number of total views of at least 30 seconds or to the end of your video, whichever occurs first.<br> |
| `video_completed_view_or_15s_passed_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | video_completed_view_or_15s_passed_actions<br> |
| `video_continuous_2_sec_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | video_continuous_2_sec_watched_actions<br> |
| `video_p100_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video was played at 100% of its length, including plays that skipped to this point.<br> |
| `video_p25_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video was played at 25% of its length, including plays that skipped to this point.<br> |
| `video_p50_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video was played at 50% of its length, including plays that skipped to this point.<br> |
| `video_p75_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video was played at 75% of its length, including plays that skipped to this point.<br> |
| `video_p95_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video was played at 95% of its length, including plays that skipped to this point.<br> |
| `video_play_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The number of times your video starts to play. This is counted for each impression of a video, and excludes replays. This metric is in development.<br> |
| `video_play_curve_actions`<br><br>*list<AdsHistogramStats>* | A video-play based curve graph that illustrates the percentage of video plays that reached a given second. Entries 0 to 14 represent seconds 0 thru 14. Entries 15 to 17 represent second ranges [15 to 20), [20 to 25), and [25 to 30). Entries 18 to 20 represent second ranges [30 to 40), [40 to 50), and [50 to 60). Entry 21 represents plays over 60 seconds.<br> |
| `video_play_retention_0_to_15s_actions`<br><br>*list<AdsHistogramStats>* | video_play_retention_0_to_15s_actions<br> |
| `video_play_retention_20_to_60s_actions`<br><br>*list<AdsHistogramStats>* | video_play_retention_20_to_60s_actions<br> |
| `video_play_retention_graph_actions`<br><br>*list<AdsHistogramStats>* | video_play_retention_graph_actions<br> |
| `video_time_watched_actions`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | video_time_watched_actions<br> |
| `website_clicks`<br><br>*numeric string* | The number of clicks on links to your website in your ads.<br> |
| `website_ctr`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The percentage of times Accounts Center accounts saw your ad and performed a link click.<br> |
| `website_purchase_roas`<br><br>*[list<AdsActionStats>](https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats)* | The total return on ad spend (ROAS) from website purchases. This is based on the value of all conversions recorded by the Facebook pixel on your website and attributed to your ads. For information on how it's calculated, please refer to https://www.facebook.com/business/help/1283504535023899<br> |
| `wish_bid`<br><br>*numeric string* | wish_bid<br> |
| `zip`<br><br>*string* | zip<br> |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 613 | Calls to this api have exceeded the rate limit. |
| 2642 | Invalid cursors values |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 2500 | Error parsing graph query |
| 105 | The number of parameters exceeded the maximum for this operation |
| 3001 | Invalid query |

## Creating

### /act_{ad_account_id}/insights
You can make a POST request to *insights* edge from the following paths:

- [/act_{ad_account_id}/insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/insights)

When posting to this edge, an [AdReportRun](https://developers.facebook.com/docs/marketing-api/reference/ad-report-run) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `action_attribution_windows`<br><br>*list<enum{1d_view, 7d_view, 28d_view, 1d_click, 7d_click, 28d_click, 1d_ev, dda, default, 7d_view_first_conversion, 28d_view_first_conversion, 7d_view_all_conversions, 28d_view_all_conversions, skan_view, skan_click, skan_click_second_postback, skan_view_second_postback, skan_click_third_postback, skan_view_third_postback}>* | **Default value: **`default`<br>The attribution window for the actions. The attribution window determines the window (e.g. 7d) and engagement type (e.g click) that’s used as a filter to report actions. See [About attribution settings and models](https://www.facebook.com/business/help/460276478298895?id=561906377587030) for examples. The `default` option means `["7d_view","1d_click"]`.<br> |
| `action_breakdowns`<br><br>*list<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}>* | **Default value: **`Vec`<br>How to break down action results. Supports more than one breakdowns. Default value is ["action_type"]<br><br><br>Note: you must also include `actions` field whenever `action_breakdowns` is specified.<br> |
| `action_report_time`<br><br>*enum{impression, conversion, mixed, lifetime}* | Determines the report time of action stats. For example, if a person            saw the ad on Jan 1st but converted on Jan 2nd, when you query the API            with `action_report_time=impression`, you see a conversion on Jan            1st. When you query the API with `action_report_time=conversion`, you see a conversion on Jan 2nd<br> |
| `breakdowns`<br><br>*list<enum{ad_extension_domain, ad_extension_url, ad_format_asset, age, app_id, body_asset, breakdown_ad_objective, breakdown_reporting_ad_id, call_to_action_asset, coarse_conversion_value, comscore_market, country, creative_automation_asset_id, creative_relaxation_asset_type, crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id, crm_advertiser_vertical_id, crm_ult_advertiser_id, description_asset, fidelity_type, flexible_format_asset_type, gen_ai_asset_type, gender, hsid, image_asset, impression_device, instagram_ads_follow_type, instagram_ads_instagram_media_product_type, instagram_ads_time_since_creation_bucket, internal_campaign_id, is_auto_advance, is_conversion_id_modeled, is_rendered_as_delayed_skip_ad, landing_destination, link_url_asset, mdsa_landing_destination, media_asset_url, media_creator, media_destination_url, media_format, media_origin_url, media_text_content, media_type, pa_creator_ig_handle, postback_sequence_index, product_brand_breakdown, product_category_breakdown, product_custom_label_0_breakdown, product_custom_label_1_breakdown, product_custom_label_2_breakdown, product_custom_label_3_breakdown, product_custom_label_4_breakdown, product_group_content_id_breakdown, product_id, redownload, region, rta_ugc_topic, skan_campaign_id, skan_conversion_id, skan_version, sot_attribution_model_type, sot_attribution_window, sot_channel, sot_event_type, sot_source, title_asset, user_persona_id, user_persona_name, video_asset, zip, rule_set_id, rule_set_name, dma, frequency_value, overlap_segment, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, mmm, place_page_id, publisher_platform, platform_position, device_platform, standard_event_content_type, conversion_destination, signal_source_bucket, reels_trending_topic, marketing_messages_btn_name, impression_view_time_advertiser_hour_v2}>* | How to break down the result. For more than one breakdown, only certain combinations are available: See "Combining Breakdowns" in the Breakdowns page. The option `impression_device` cannot be used by itself<br> |
| `date_preset`<br><br>*enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year}* | **Default value: **`last_30d`<br>Represents a relative time range. This field is ignored if `time_range` or `time_ranges` is specified<br> |
| `default_summary`<br><br>*boolean* | **Default value: **`false`<br>Determine whether to return a summary. If `summary` is set, this param is ignored; otherwise, a summary section with the same fields as specified by `fields` is included in the summary section<br> |
| `export_columns`<br><br>*list<string>* | Select fields on the exporting report file. It is an optional param. Exporting columns are equal to the param fields if you leave this param blank<br> |
| `export_format`<br><br>*string* | Set the format of exporting report file. If the export_format is set, Report file is asyncrhonizely generated. It expects ["xls", "csv"].<br> |
| `export_name`<br><br>*string* | Set the file name of the exporting report.<br> |
| `fields`<br><br>*list<string>* | Fields to be retrieved. Default behavior is to return a list of most used fields<br> |
| `filtering`<br><br>*list<Filter Object>* | **Default value: **`Vec`<br>Filters on the report data. This parameter is an array of filter objects<br><br><br>`field` *string*<br>**[required]**<br><br><br>`operator` *enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP}*<br>**[required]**<br><br><br>`value` *string*<br>**[required]**<br> |
| `graph_cache`<br><br>*boolean* | **Default value: **`true`<br>[internal use only] This param controls whether the the Graph API level cache should be used for insights endpoint<br> |
| `level`<br><br>*enum {ad, adset, campaign, account}* | Represents the level of result<br> |
| `limit`<br><br>*integer* | limit<br> |
| `product_id_limit`<br><br>*integer* | Maximum number of product ids to be returned for each ad when breakdown by `product_id`.<br> |
| `sort`<br><br>*list<string>* | **Default value: **`Vec`<br>Field to sort the result, and direction of sorting. You can specify sorting direction by appending "_ascending" or "_descending" to the sort field. For example, "reach_descending". For actions, you can sort by action type in form of "actions:<action_type>". For example, ["actions:link_click_ascending"]. This array supports no more than one element. By default, the sorting direction is ascending<br> |
| `summary`<br><br>*list<string>* | If this param is used, a summary section is included, with the fields listed in this param<br> |
| `summary_action_breakdowns`<br><br>*list<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}>* | **Default value: **`Vec`<br>Similar to `action_breakdowns`, but applies to summary. Default value is ["action_type"]<br> |
| `time_increment`<br><br>*enum{monthly, all_days} or integer* | **Default value: **`all_days`<br>If it is an integer, it is the number of days from 1 to 90. After you pick a reporting period by using `time_range` or `date_preset`, you may choose to have the results for the whole period, or have results for smaller time slices. If "all_days" is used, it means one result set for the whole period. If "monthly" is used, you get one result set for each calendar month in the given period. Or you can have one result set for each N-day period specified by this param. This param is ignored if `time_ranges` is specified<br> |
| `time_range`<br><br>*{'since':YYYY-MM-DD,'until':YYYY-MM-DD}* | A single time range object. UNIX timestamp not supported. This param is ignored if `time_ranges` is provided<br><br><br>`since` *datetime*<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br><br><br>`until` *datetime*<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br> |
| `time_ranges`<br><br>*list<{'since':YYYY-MM-DD,'until':YYYY-MM-DD}>* | Array of time range objects. Time ranges can overlap, for example to return cumulative insights. Each time range has one result set. You cannot have more granular results with `time_increment` setting in this case.If `time_ranges` is specified, `date_preset`, `time_range` and `time_increment` are ignored<br><br><br>`since` *datetime*<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br><br><br>`until` *datetime*<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br> |
| `use_account_attribution_setting`<br><br>*boolean* | **Default value: **`false`<br>When this parameter is set to true, your ads results are shown using the attribution settings defined for the ad account<br> |
| `use_unified_attribution_setting`<br><br>*boolean* | When this parameter is set to `true`, your ads results will be shown using unified attribution settings defined at ad set level and parameter `use_account_attribution_setting` will be ignored.<br><br>**Note:** Please set this to `true` to get the same behavior as in the Ads Manager.<br> |

#### Return Type

```
Struct  {
report_run_id: numeric string,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 200 | Permissions error |
| 2500 | Error parsing graph query |

## Updating

You can't perform this operation on this endpoint.

## Deleting

You can't perform this operation on this endpoint.
