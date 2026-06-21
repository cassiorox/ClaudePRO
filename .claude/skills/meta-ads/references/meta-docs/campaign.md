# Campaign (Ad Campaign Group)
Fonte: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/
Baixado para Meta Marketing API v25.0

---

Ads and Commerce

Version

v22.0v23.0v24.0v25.0

# Ad Campaign Group

Updated:May 11, 2026

A campaign is the highest level organizational structure within an ad account and should represent a single objective for an advertiser, for example, to drive page post engagement. Setting objective of the campaign will enforce validation on any ads added to the campaign to ensure they also have the correct objective.

The `date_preset = lifetime` parameter is disabled in Graph API v10.0 and replaced with `date_preset = maximum`, which returns a maximum of 37 months of data. For v9.0 and below, `date_preset = maximum` will be enabled on May 25, 2021, and any `lifetime` calls will default to `maximum` and return only 37 months of data.

### Limits

You can only create 200 ad sets per ad campaign. [Learn more about the ad campaign structure](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group).
If your campaign has more than 70 ad sets and uses [Campaign Budget Optimization](https://developers.facebook.com/docs/marketing-api/bidding/guides/campaign-budget-optimization), you are not able to edit your current bid strategy or turn off CBO. [Learn more in the Business Help Center⁠](https://www.facebook.com/business/help/519856662172206).

### New Required Field for All Campaigns

All businesses using the Marketing API must identify whether or not new and edited campaigns belong to a [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category). Current available categories are: [housing, employment, credit](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category#context), or issues, elections, and politics. Businesses whose ads do not belong to a Special Ad Category must indicate NONE or send an empty array in the `special_ad_categories` field.

Businesses running **housing**, **employment**, or **credit** ads must comply with [targeting and audience restrictions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-restrictions). Targeting for ads about social issues, elections or politics are not affected by the `special_ad_categories` label.

As of **Marketing API 7.0**, the `special_ad_category` parameter on the [`POST /act_<ad_account_id>/campaigns`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns#Creating) endpoint has been deprecated and replaced with a new `special_ad_categories` parameter. The new `special_ad_categories` parameter is required and accepts an array.

If you use the `special_ad_category` parameter, it will still return a string, but you should use `GET /{campaign-id}?fields=special_ad_categories` to get an array back. Refer to [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) for additional information.

## Reading

A campaign is a grouping of ad sets which are organized by the same business objective. Each campaign has an objective that must be valid across the ad sets within that campaign.

After your ads begin delivering, you can query stats for ad campaigns. The statistics returned will be unique stats, deduped across the ad sets. You can also get reports and statistics for all ad sets and ads in an campaign simultaneously.

#### Example

Select language

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

* * *

```
GET v25.0/...?fields={fieldname_of_type_Campaign} HTTP/1.1
Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=...%3Ffields%3D%257Bfieldname_of_type_Campaign%257D&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br>_enum{today, yesterday, this\_month, last\_month, this\_quarter, maximum, data\_maximum, last\_3d, last\_7d, last\_14d, last\_28d, last\_30d, last\_90d, last\_week\_mon\_sun, last\_week\_sun\_sat, last\_quarter, last\_year, this\_week\_mon\_today, this\_week\_sun\_today, this\_year}_ | Date Preset |
| `time_range`<br>_{‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD}_ | Time Range. Note if time range is invalid, it will be ignored.<br>* * *<br>`since` _datetime_<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br>`until` _datetime_<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br>Show child parameters |

#### Fields

| Field | Description |
| --- | --- |
| `id`<br>_numeric string_ | Campaign's ID<br>default |
| `account_id`<br>_numeric string_ | ID of the ad account that owns this campaign |
| `adlabels`<br>_[list<AdLabel>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label)_ | Ad Labels associated with this campaign |
| `bid_strategy`<br>_enum {LOWEST\_COST\_WITHOUT\_CAP, LOWEST\_COST\_WITH\_BID\_CAP, COST\_CAP, LOWEST\_COST\_WITH\_MIN\_ROAS}_ | Bid strategy for this campaign when you enable campaign budget optimization and<br>when you use `AUCTION` as your buying type:<br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy to select<br>if you care most about cost efficiency. However, note that it may be harder to get<br>stable average costs as you spend. Note: this strategy is also known as<br>_automatic bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to a specified amount.<br>Get specified bid cap in the `bid_amount` field for each ad set in this ad campaign.<br>This strategy is known as _manual maximum-cost bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`COST_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual average cost per optimization event to a specified amount.<br>Get specified cost cap in the `bid_amount` field for each ad set in this ad campaign.<br>Learn more in [Ads Help Center, About bid strategies: Cost Cap⁠](https://www.facebook.com/business/help/272336376749096?id=2196356200683573).<br>Notes:<br>If you do not enable campaign budget optimization, you should get `bid_strategy` at the ad set level.<br>`TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0). |
| `boosted_object_id`<br>_numeric string_ | The Boosted Object this campaign has associated, if any |
| `brand_lift_studies`<br>_[list<AdStudy>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-study)_ | Automated Brand Lift V2 studies for this ad set. |
| `budget_rebalance_flag`<br>_bool_ | Whether to automatically rebalance budgets daily for all the adsets under this campaign. [This has been deprecated on Marketing API V7.0](https://developers.facebook.com/docs/graph-api/changelog/version7.0#deprecations). |
| `budget_remaining`<br>_numeric string_ | Remaining budget |
| `buying_type`<br>_string_ | Buying type, possible values are: <br>`AUCTION`: default<br>`RESERVED`: for [reach and frequency ads](https://developers.facebook.com/docs/marketing-api/reachandfrequency)<br>[Reach and Frequency](https://developers.facebook.com/docs/marketing-api/reachandfrequency) is disabled for [housing, employment and credit ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category). |
| `campaign_group_active_time`<br>_numeric string_ | campaign\_group\_active\_time this is only for Internal, This will have the active running length of Campaign Groups |
| `can_create_brand_lift_study`<br>_bool_ | If we can create a new automated brand lift study for the ad set. |
| `can_use_spend_cap`<br>_bool_ | Whether the campaign can set the spend cap |
| `configured_status`<br>_enum {ACTIVE, PAUSED, DELETED, ARCHIVED}_ | If this status is `PAUSED`, all its active ad sets and ads will<br>be paused and have an effective status `CAMPAIGN_PAUSED`. Prefer<br>using 'status' instead of this. |
| `created_time`<br>_datetime_ | Created Time |
| `daily_budget`<br>_numeric string_ | The daily budget of the campaign |
| `effective_status`<br>_enum {ACTIVE, PAUSED, DELETED, ARCHIVED, IN\_PROCESS, WITH\_ISSUES}_ | IN\_PROCESS is available for version 4.0 or higher |
| `has_secondary_skadnetwork_reporting`<br>_bool_ | has\_secondary\_skadnetwork\_reporting |
| `is_adset_budget_sharing_enabled`<br>_bool_ | Whether the child ad sets are managed under ad set budget sharing |
| `is_budget_schedule_enabled`<br>_bool_ | Whether budget scheduling is enabled for the campaign group |
| `is_reels_trending_ads_enabled`<br>_bool_ | is\_reels\_trending\_ads\_enabled |
| `is_skadnetwork_attribution`<br>_bool_ | When set to `true` Indicates that the campaign will include SKAdNetwork, iOS 14+. |
| `issues_info`<br>_[list<AdCampaignIssuesInfo>](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-issues-info)_ | Issues for this campaign that prevented it from deliverying |
| `last_budget_toggling_time`<br>_datetime_ | Last budget toggling time |
| `lifetime_budget`<br>_numeric string_ | The lifetime budget of the campaign |
| `name`<br>_string_ | Campaign's name |
| `objective`<br>_string_ | Campaign's objective<br>See the [Outcome Ad-Driven Experience Objective Validation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax) section below for more information. |
| `pacing_type`<br>_list<string>_ | Defines pacing type of the campaign. The value is an array of options: "standard". |
| `primary_attribution`<br>_enum_ | primary\_attribution |
| `promoted_object`<br>_[AdPromotedObject](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object)_ | The object this campaign is promoting across all its ads |
| `smart_promotion_type`<br>_enum_ | Smart Promotion Type. guided\_creation or smart\_app\_promotion(the choice under APP\_INSTALLS objective). |
| `source_campaign`<br>_[Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group)_ | The source campaign that this campaign is copied from |
| `source_campaign_id`<br>_numeric string_ | The source campaign id that this campaign is copied from |
| `special_ad_categories`<br>_list<enum>_ | special ad categories |
| `special_ad_category`<br>_enum_ | The campaign's Special Ad Category. One of `HOUSING`, `EMPLOYMENT`, `CREDIT`, or `NONE`. |
| `special_ad_category_country`<br>_list<enum>_ | Country field for Special Ad Category. |
| `spend_cap`<br>_numeric string_ | A spend cap for the campaign, such that it will not spend more than this cap. Expressed as integer value of the subunit in your currency. |
| `start_time`<br>_datetime_ | Merging of `start_time`s for the ad sets belonging to this campaign. At the campaign level, `start_time` is a read only field. You can setup `start_time` at the ad set level. |
| `status`<br>_enum {ACTIVE, PAUSED, DELETED, ARCHIVED}_ | If this status is `PAUSED`, all its active ad sets and ads will<br>be paused and have an effective status `CAMPAIGN_PAUSED`. The field<br>returns the same value as 'configured\_status', and is the suggested<br>one to use. |
| `stop_time`<br>_datetime_ | Merging of `stop_time`s for the ad sets belonging to this campaign, if available. At the campaign level, `stop_time` is a read only field. You can setup `stop_time` at the ad set level. |
| `topline_id`<br>_numeric string_ | Topline ID |
| `updated_time`<br>_datetime_ | Updated Time. If you update `spend_cap` or daily budget or lifetime budget, this will not automatically update this field. |

#### Edges

| Edge | Description |
| --- | --- |
| [`ad_studies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/ad_studies)<br>_Edge<AdStudy>_ | The ad studies containing this campaign |
| [`adrules_governed`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/adrules_governed)<br>_Edge<AdRule>_ | Ad rules that govern this campaign - by default, this only returns rules that either directly mention the campaign by id or indirectly through the set entity\_type |
| [`ads`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/ads)<br>_Edge<Adgroup>_ | Ads under this campaign |
| [`adsets`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/adsets)<br>_Edge<AdCampaign>_ | The ad sets under this campaign |
| [`copies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/copies)<br>_Edge<AdCampaignGroup>_ | The copies of this campaign |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 613 | Calls to this api have exceeded the rate limit. |
| 190 | Invalid OAuth 2.0 Access Token |
| 104 | Incorrect signature |
| 2500 | Error parsing graph query |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 200 | Permissions error |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |

## Creating

### /act\_{ad\_account\_id}/async\_batch\_requests

You can make a POST request to _async\_batch\_requests_ edge from the following paths:

[/act\_{ad\_account\_id}/async\_batch\_requests](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/async_batch_requests)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `adbatch`<br>_list<Object>_ | JSON encoded batch reqeust<br>required<br>* * *<br>`name` _string_ <br>required<br>`relative_url` _string_ <br>required<br>`body` _UTF-8 encoded string_ <br>required<br>Show child parameters |
| `name`<br>_UTF-8 encoded string_ | Name of the batch request for tracking purposes.<br>required |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by _id_ in the return type.

```
Struct  {
id: numeric string,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 194 | Missing at least one required parameter |
| 100 | Invalid parameter |
| 2500 | Error parsing graph query |

* * *

### /{campaign\_id}/copies

You can make a POST request to _copies_ edge from the following paths:

[/{campaign\_id}/copies](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/copies)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `deep_copy`<br>_boolean_ | **Default value:**`false`<br>Whether to copy all the child ads. Limits: the total number of children ads to copy should not exceed 3 for a synchronous call and 51 for an asynchronous call. |
| `end_time`<br>_datetime_ | For deep copy, the end time of the sets under the copied campaign, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. When creating a set with a daily budget, specify `end_time=0` to set the set to be ongoing without end date. If not set, the copied sets will inherit the end time from the original set |
| `parameter_overrides`<br>_Campaign spec_ | parameter\_overrides |
| `rename_options`<br>_JSON or object-like arrays_ | Rename options<br>* * *<br>`rename_strategy` _enum {DEEP\_RENAME, ONLY\_TOP\_LEVEL\_RENAME, NO\_RENAME}_<br>**Default value:**`ONLY_TOP_LEVEL_RENAME`<br>`DEEP_RENAME`: will change this object's name and children's names in the copied object. `ONLY_TOP_LEVEL_RENAME`: will change the this object's name but won't change the children's name in the copied object. `NO_RENAME`: will change no name in the copied object<br>`rename_prefix` _string_<br>A prefix to copy names. Defaults to null if not provided.<br>`rename_suffix` _string_<br>A suffix to copy names. Defaults to null if not provided and appends a localized string of `- Copy` based on the ad account locale.<br>Show child parameters |
| `start_time`<br>_datetime_ | For deep copy, the start time of the sets under the copied campaign, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. If not set, the copied sets will inherit the start time from the original set |
| `status_option`<br>_enum {ACTIVE, PAUSED, INHERITED\_FROM\_SOURCE}_ | **Default value:**`PAUSED`<br>`ACTIVE`: the copied campaign will have active status. `PAUSED`: the copied campaign will have paused status. `INHERITED_FROM_SOURCE`: the copied campaign will have the parent status. |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by _copied\_campaign\_id_ in the return type.

```
Struct  {
copied_campaign_id: numeric string,
ad_object_ids:  List  [ Struct  {\
ad_object_type: enum {\
unique_adcreative,\
ad,\
ad_set,\
campaign,\
opportunities,\
privacy_info_center,\
topline,\
ad_account,\
product},\
source_id: numeric string,\
copied_id: numeric string,\
}],
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

* * *

### /act\_{ad\_account\_id}/campaigns

You can make a POST request to _campaigns_ edge from the following paths:

[/act\_{ad\_account\_id}/campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.

#### Example

Select language

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL

* * *

```
POST /v25.0/act_<AD_ACCOUNT_ID>/campaigns HTTP/1.1
Host: graph.facebook.com

name=My+campaign&objective=OUTCOME_TRAFFIC&status=PAUSED&special_ad_categories=%5B%5D&is_adset_budget_sharing_enabled=0
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fcampaigns%3Fname%3DMy%2Bcampaign%26objective%3DOUTCOME_TRAFFIC%26status%3DPAUSED%26special_ad_categories%3D%255B%255D%26is_adset_budget_sharing_enabled%3D0&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `adlabels`<br>_list<Object>_ | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this campaign |
| `bid_strategy`<br>_enum{LOWEST\_COST\_WITHOUT\_CAP, LOWEST\_COST\_WITH\_BID\_CAP, COST\_CAP, LOWEST\_COST\_WITH\_MIN\_ROAS}_ | Choose bid strategy for this campaign to suit your specific business goals.<br>Each strategy has tradeoffs and may be available for certain `optimization_goal`s:<br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as _automatic bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. If you select this, you must provide<br>a bid cap in the `bid_amount` field for each ad set in this ad campaign.<br>Note: during creation this is the default bid strategy if you don't specify.<br>This strategy is also known as _manual maximum-cost bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>**Notes:**<br>If you do not enable campaign budget optimization, you should set `bid_strategy` at ad set level.<br>`TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0). |
| `budget_schedule_specs`<br>_list<JSON or object-like arrays>_ | Initial high demand periods to be created with the campaign.<br>Provide list of `time_start`, `time_end`,`budget_value`, and `budget_value_type`.<br>For example,<br>-F 'budget\_schedule\_specs=\[{<br>"time\_start":1699081200,<br>"time\_end":1699167600,<br>"budget\_value":100,<br>"budget\_value\_type":"ABSOLUTE"<br>}\]'<br>See [High Demand Period](https://developers.facebook.com/docs/graph-api/reference/high-demand-period) for more details on each field.<br>* * *<br>`id` _int64_<br>`time_start` _datetime_<br>`time_end` _datetime_<br>`budget_value` _int64_<br>`budget_value_type` _enum{ABSOLUTE, MULTIPLIER}_<br>`recurrence_type` _enum{ONE\_TIME, WEEKLY}_<br>`weekly_schedule` _list<JSON or object-like arrays>_ <br>* * *<br>`days` _list<int64>_<br>`minute_start` _int64_<br>`minute_end` _int64_<br>`timezone_type` _string_<br>Show child parameters<br>Show child parameters |
| `buying_type`<br>_string_ | **Default value:**`AUCTION`<br>This field will help Facebook make optimizations to delivery, pricing, and limits. All ad sets in this campaign must match the buying type. Possible values are: <br>`AUCTION` (default)<br>`RESERVED` (for [reach and frequency ads](https://developers.facebook.com/docs/marketing-api/reachandfrequency)). |
| `campaign_optimization_type`<br>_enum{NONE, ICO\_ONLY}_ | campaign\_optimization\_type |
| `daily_budget`<br>_int64_ | Daily budget of this campaign. All adsets under this<br>campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both. |
| `execution_options`<br>_list<enum{validate\_only, include\_recommendations}>_ | **Default value:**`Set`<br>An execution setting<br>`validate_only`: when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. <br>`include_recommendations`: this option cannot be used by itself. When this option is used, recommendations for ad object's configuration will be included. A separate section [recommendations](https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation) will be included in the response, but only if recommendations for this specification exist.<br>If the call passes validation or review, response will be `{"success": true}`. If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review. |
| `is_skadnetwork_attribution`<br>_boolean_ | To create an iOS 14 campaign, enable SKAdNetwork attribution for this campaign. |
| `is_using_l3_schedule`<br>_boolean_ | is\_using\_l3\_schedule |
| `iterative_split_test_configs`<br>_list<Object>_ | Array of Iterative Split Test Configs created under this campaign . |
| `lifetime_budget`<br>_int64_ | Lifetime budget of this campaign. All adsets under<br>this campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both. |
| `name`<br>_string_ | Name for this campaign<br>supports emoji |
| `objective`<br>_enum{APP\_INSTALLS, BRAND\_AWARENESS, CONVERSIONS, EVENT\_RESPONSES, LEAD\_GENERATION, LINK\_CLICKS, LOCAL\_AWARENESS, MESSAGES, OFFER\_CLAIMS, OUTCOME\_APP\_PROMOTION, OUTCOME\_AWARENESS, OUTCOME\_ENGAGEMENT, OUTCOME\_LEADS, OUTCOME\_SALES, OUTCOME\_TRAFFIC, PAGE\_LIKES, POST\_ENGAGEMENT, PRODUCT\_CATALOG\_SALES, REACH, STORE\_VISITS, VIDEO\_VIEWS}_ | Campaign's objective. If it is specified the API will validate that any ads created under the campaign match that objective. <br>Currently, with `BRAND_AWARENESS` objective, all creatives should be either only images or only videos, not mixed.<br>See [Outcome Ad-Driven Experience Objective Validation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax) for more information. |
| `promoted_object`<br>_Object_ | The object this campaign is promoting across all its ads. It’s required for Meta iOS 14+ app promotion (SKAdNetwork or Aggregated Event Measurement) campaign creation. Only `product_catalog_id` is used at the ad set level.<br>* * *<br>`application_id` _int_<br>The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement<br>`pixel_id` _numeric string or integer_<br>The ID of a Facebook conversion pixel. Used with offsite conversion campaigns.<br>`custom_event_type` _enum{AD\_IMPRESSION, RATE, TUTORIAL\_COMPLETION, CONTACT, CUSTOMIZE\_PRODUCT, DONATE, FIND\_LOCATION, SCHEDULE, START\_TRIAL, SUBMIT\_APPLICATION, SUBSCRIBE, ADD\_TO\_CART, ADD\_TO\_WISHLIST, INITIATED\_CHECKOUT, ADD\_PAYMENT\_INFO, PURCHASE, LEAD, COMPLETE\_REGISTRATION, CONTENT\_VIEW, SEARCH, SERVICE\_BOOKING\_REQUEST, MESSAGING\_CONVERSATION\_STARTED\_7D, LEVEL\_ACHIEVED, ACHIEVEMENT\_UNLOCKED, SPENT\_CREDITS, LISTING\_INTERACTION, D2\_RETENTION, D7\_RETENTION, OTHER}_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`object_store_url` _URL_<br>The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application\_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br>`object_store_urls` _list<URL>_<br>The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application\_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br>`offer_id` _numeric string or integer_<br>The ID of an Offer from a Facebook Page.<br>`page_id` _Page ID_<br>The ID of a Facebook Page<br>`product_catalog_id` _numeric string or integer_<br>The ID of a Product Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br>`product_item_id` _numeric string or integer_<br>The ID of the product item.<br>`job_listing_id` _numeric string or integer_<br>The ID of the marketplace job listing.<br>`instagram_profile_id` _numeric string or integer_<br>The ID of the instagram profile id.<br>`product_set_id` _numeric string or integer_<br>The ID of a Product Set within an Ad Set level Product<br>Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br>`event_id` _numeric string or integer_<br>The ID of a Facebook Event<br>`offline_conversion_data_set_id` _numeric string or integer_<br>The ID of the offline dataset.<br>`fundraiser_campaign_id` _numeric string or integer_<br>The ID of the fundraiser campaign.<br>`custom_event_str` _string_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`mcme_conversion_id` _numeric string or integer_<br>The ID of a MCME conversion.<br>`conversion_goal_id` _numeric string or integer_<br>The ID of a Conversion Goal.<br>`offsite_conversion_event_id` _numeric string or integer_<br>The ID of a Offsite Conversion Event<br>`boosted_product_set_id` _numeric string or integer_<br>The ID of the Boosted Product Set within an Ad Set level Product<br>Catalog. Should only be present when the advertiser has<br>opted into Product Set Boosting.<br>`lead_ads_form_event_source_type` _enum{inferred, meta\_source, offsite\_crm, offsite\_web, onsite\_crm, onsite\_crm\_single\_event, onsite\_clo\_dep\_aet, onsite\_web, onsite\_p2b\_call, onsite\_messaging, qualified\_lead\_file}_<br>The event source of lead ads form.<br>`lead_ads_custom_event_type` _enum{AD\_IMPRESSION, RATE, TUTORIAL\_COMPLETION, CONTACT, CUSTOMIZE\_PRODUCT, DONATE, FIND\_LOCATION, SCHEDULE, START\_TRIAL, SUBMIT\_APPLICATION, SUBSCRIBE, ADD\_TO\_CART, ADD\_TO\_WISHLIST, INITIATED\_CHECKOUT, ADD\_PAYMENT\_INFO, PURCHASE, LEAD, COMPLETE\_REGISTRATION, CONTENT\_VIEW, SEARCH, SERVICE\_BOOKING\_REQUEST, MESSAGING\_CONVERSATION\_STARTED\_7D, LEVEL\_ACHIEVED, ACHIEVEMENT\_UNLOCKED, SPENT\_CREDITS, LISTING\_INTERACTION, D2\_RETENTION, D7\_RETENTION, OTHER}_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`lead_ads_custom_event_str` _string_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`lead_ads_offsite_conversion_type` _enum{default, clo}_<br>The offsite conversion type for lead ads<br>`value_semantic_type` _enum {VALUE, MARGIN, LIFETIME\_VALUE}_<br>The semantic of the event value to be using for optimization<br>`variation` _enum {OMNI\_CHANNEL\_SHOP\_AUTOMATIC\_DATA\_COLLECTION, PRODUCT\_SET\_AND\_APP, PRODUCT\_SET\_AND\_IN\_STORE, PRODUCT\_SET\_AND\_OMNICHANNEL, PRODUCT\_SET\_AND\_PHONE\_CALL, PRODUCT\_SET\_AND\_WEBSITE, PRODUCT\_SET\_AND\_WEBSITE\_AND\_PHONE\_CALL, PRODUCT\_SET\_WEBSITE\_APP\_AND\_INSTORE}_<br>Variation of the promoted object for a PCA ad<br>`passback_pixel_id` _numeric string or integer_<br>ID of the pixel used for tracking passback events<br>`passback_application_id` _numeric string or integer_<br>ID of the application used for tracking passback events<br>`product_set_optimization` _enum{enabled, disabled}_<br>Enum defining whether or not the ad should be optimized for the promoted product set<br>`full_funnel_objective` _enum{OFFER\_CLAIMS, PAGE\_LIKES, EVENT\_RESPONSES, POST\_ENGAGEMENT, WEBSITE\_CONVERSIONS, LINK\_CLICKS, VIDEO\_VIEWS, LOCAL\_AWARENESS, PRODUCT\_CATALOG\_SALES, LEAD\_GENERATION, BRAND\_AWARENESS, STORE\_VISITS, REACH, APP\_INSTALLS, MESSAGES, OUTCOME\_AWARENESS, OUTCOME\_ENGAGEMENT, OUTCOME\_LEADS, OUTCOME\_SALES, OUTCOME\_TRAFFIC, OUTCOME\_APP\_PROMOTION}_<br>Enum defining the full funnel objective of the campaign<br>`dataset_split_id` _numeric string or integer_<br>ID of the dataset split used to perform additional optimization on the dataset<br>`dataset_split_ids` _array<numeric string>_<br>IDs of the dataset splits used to perform additional optimization on the dataset<br>`lead_ads_selected_pixel_id` _numeric string or integer_<br>The selected pixel id for lead ads conversion leads optimization<br>`custom_attribution_source_ids` _array<numeric string>_<br>IDs of the custom attribution sources used for tracking passback events<br>`multi_event_product` _int64_<br>Identifies which action-to-action product the advertiser is using<br>`product_sales_channel` _enum {ONLINE, IN\_STORE, OMNI}_<br>ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads<br>`anchor_event_config` _JSON object_<br>Configuration for anchor event in multi-event optimization campaigns<br>`multi_event_conversion_info` _JSON object_<br>Configuration for multi-event conversion info in CLO campaigns<br>`live_video_destination` _string_<br>The live video destination type for live video ads<br>`smart_pse_enabled` _boolean_<br>Whether Smart Product Set Expansion is enabled for this campaign.<br>`smart_pse_setting` _enum{ENABLED, DISABLED}_<br>Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues.<br>`lead_ads_follow_up_event` _enum{whatsapp\_conversations}_<br>The selected lead follow-up event for lead ads campaigns.<br>`omnichannel_object` _Object_ <br>* * *<br>`app` _array<JSON object>_<br>`pixel` _array<JSON object>_ <br>required<br>`onsite` _array<JSON object>_<br>Show child parameters<br>`whats_app_business_phone_number_id` _numeric string or integer_<br>`whatsapp_phone_number` _string_<br>Show child parameters |
| `source_campaign_id`<br>_numeric string or integer_ | Used if a campaign has been copied. The ID from the original campaign that was copied. |
| `special_ad_categories`<br>_array<enum {NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES\_ELECTIONS\_POLITICS, ONLINE\_GAMBLING\_AND\_GAMING, FINANCIAL\_PRODUCTS\_SERVICES}>_ | special\_ad\_categories<br>required |
| `special_ad_category_country`<br>_array<enum {AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}>_ | special\_ad\_category\_country |
| `spend_cap`<br>_int64_ | A spend cap for the campaign, such that it will not spend more than this cap. Defined as integer value of subunit in your currency with a minimum value of $100 USD (or approximate local equivalent). Set the value to 922337203685478 to remove the spend cap. Not available for Reach and Frequency or Premium Self Serve campaigns |
| `start_time`<br>_datetime_ | start\_time |
| `status`<br>_enum{ACTIVE, PAUSED, DELETED, ARCHIVED}_ | Only `ACTIVE` and `PAUSED` are valid during<br>creation. Other statuses can be used for update. If it is set to<br>`PAUSED`, its active child objects will be paused and have an effective<br>status `CAMPAIGN_PAUSED`. |
| `stop_time`<br>_datetime_ | stop\_time |
| `topline_id`<br>_numeric string or integer_ | Topline ID |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by _id_ in the return type.

```
Struct  {
id: numeric string,
success: bool,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |
| 200 | Permissions error |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 300 | Edit failure |

* * *

## Updating

### /{campaign\_id}

You can update a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) by making a POST request to [/{campaign\_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group).

#### Parameters

| Parameter | Description |
| --- | --- |
| `adlabels`<br>_list<Object>_ | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this campaign |
| `adset_bid_amounts`<br>_JSON object {numeric string : int64}_ | A map of child adset IDs to their respective bid amounts required in the process of toggling campaign from autobid to manual bid |
| `adset_budgets`<br>_array<JSON object>_ | An array of maps containing all the non-deleted child adset IDs and either daily\_budget or lifetime\_budget, required in the process of toggling between campaign budget and adset budget<br>* * *<br>`adset_id` _numeric string_<br>adset\_id<br>required<br>`daily_budget` _int64_<br>daily\_budget<br>`lifetime_budget` _int64_<br>lifetime\_budget<br>Show child parameters |
| `bid_strategy`<br>_enum{LOWEST\_COST\_WITHOUT\_CAP, LOWEST\_COST\_WITH\_BID\_CAP, COST\_CAP, LOWEST\_COST\_WITH\_MIN\_ROAS}_ | Choose bid strategy for this campaign to suit your specific business goals.<br>Each strategy has tradeoffs and may be available for certain `optimization_goal`s:<br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as _automatic bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. If you select this, you must provide<br>a bid cap in the `bid_amount` field for each ad set in this ad campaign.<br>Note: during creation this is the default bid strategy if you don't specify.<br>This strategy is also known as _manual maximum-cost bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`COST_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual average cost per optimization event to a specified amount.<br>Get specified cost cap in the `bid_amount` field for each ad set in this ad campaign.<br>Learn more in [Ads Help Center, About bid strategies: Cost Cap⁠](https://www.facebook.com/business/help/272336376749096?id=2196356200683573).<br>Notes:<br>If you do not enable campaign budget optimization, you should set `bid_strategy` at ad set level.<br>`TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0). |
| `budget_rebalance_flag`<br>_boolean_ | Whether to automatically rebalance budgets daily for all the adsets under this campaign. |
| `campaign_optimization_type`<br>_enum{NONE, ICO\_ONLY}_ | campaign\_optimization\_type |
| `daily_budget`<br>_int64_ | Daily budget of this campaign. All adsets under this<br>campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both. |
| `execution_options`<br>_list<enum{validate\_only, include\_recommendations}>_ | **Default value:**`Set`<br>An execution setting<br>`validate_only`: when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. <br>`include_recommendations`: this option cannot be used by itself. When this option is used, recommendations for ad object's configuration will be included. A separate section [recommendations](https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation) will be included in the response, but only if recommendations for this specification exist.<br>If the call passes validation or review, response will be `{"success": true}`. If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review. |
| `is_adset_budget_sharing_enabled`<br>_boolean_ | Whether the child ad sets are managed under ad set budget sharing. With ad set budget sharing, advertisers can now share up to 20% of their budget with other ad sets in the same campaign. |
| `is_reels_trending_ads_enabled`<br>_boolean_ | indicator for 'reels trending ads' campaign |
| `is_skadnetwork_attribution`<br>_boolean_ | Flag to indicate that the campaign will be using SKAdNetwork, which also means that it will only be targeting iOS 14.x and above |
| `is_using_l3_schedule`<br>_boolean_ | is\_using\_l3\_schedule |
| `iterative_split_test_configs`<br>_list<Object>_ | Array of Iterative Split Test Configs created under this campaign . |
| `lifetime_budget`<br>_int64_ | Lifetime budget of this campaign. All adsets under<br>this campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both. |
| `name`<br>_string_ | Name for this campaign<br>supports emoji |
| `objective`<br>_enum{APP\_INSTALLS, BRAND\_AWARENESS, CONVERSIONS, EVENT\_RESPONSES, LEAD\_GENERATION, LINK\_CLICKS, LOCAL\_AWARENESS, MESSAGES, OFFER\_CLAIMS, OUTCOME\_APP\_PROMOTION, OUTCOME\_AWARENESS, OUTCOME\_ENGAGEMENT, OUTCOME\_LEADS, OUTCOME\_SALES, OUTCOME\_TRAFFIC, PAGE\_LIKES, POST\_ENGAGEMENT, PRODUCT\_CATALOG\_SALES, REACH, STORE\_VISITS, VIDEO\_VIEWS}_ | Campaign's objective. If it is specified the API will validate that any ads created under the campaign match that objective. <br>Currently, with `BRAND_AWARENESS` objective, all creatives should be either only images or only videos, not mixed.<br>See the [Outcome Ad-Driven Experience Objective Validation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax) section below for more information. |
| `promoted_object`<br>_Object_ | The object this campaign is promoting across all its ads. Only `product_catalog_id` is used at the ad set level.<br>* * *<br>`application_id` _int_<br>The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement<br>`pixel_id` _numeric string or integer_<br>The ID of a Facebook conversion pixel. Used with offsite conversion campaigns.<br>`custom_event_type` _enum{AD\_IMPRESSION, RATE, TUTORIAL\_COMPLETION, CONTACT, CUSTOMIZE\_PRODUCT, DONATE, FIND\_LOCATION, SCHEDULE, START\_TRIAL, SUBMIT\_APPLICATION, SUBSCRIBE, ADD\_TO\_CART, ADD\_TO\_WISHLIST, INITIATED\_CHECKOUT, ADD\_PAYMENT\_INFO, PURCHASE, LEAD, COMPLETE\_REGISTRATION, CONTENT\_VIEW, SEARCH, SERVICE\_BOOKING\_REQUEST, MESSAGING\_CONVERSATION\_STARTED\_7D, LEVEL\_ACHIEVED, ACHIEVEMENT\_UNLOCKED, SPENT\_CREDITS, LISTING\_INTERACTION, D2\_RETENTION, D7\_RETENTION, OTHER}_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`object_store_url` _URL_<br>The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application\_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br>`object_store_urls` _list<URL>_<br>The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application\_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br>`offer_id` _numeric string or integer_<br>The ID of an Offer from a Facebook Page.<br>`page_id` _Page ID_<br>The ID of a Facebook Page<br>`product_catalog_id` _numeric string or integer_<br>The ID of a Product Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br>`product_item_id` _numeric string or integer_<br>The ID of the product item.<br>`job_listing_id` _numeric string or integer_<br>The ID of the marketplace job listing.<br>`instagram_profile_id` _numeric string or integer_<br>The ID of the instagram profile id.<br>`product_set_id` _numeric string or integer_<br>The ID of a Product Set within an Ad Set level Product<br>Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br>`event_id` _numeric string or integer_<br>The ID of a Facebook Event<br>`offline_conversion_data_set_id` _numeric string or integer_<br>The ID of the offline dataset.<br>`fundraiser_campaign_id` _numeric string or integer_<br>The ID of the fundraiser campaign.<br>`custom_event_str` _string_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`mcme_conversion_id` _numeric string or integer_<br>The ID of a MCME conversion.<br>`conversion_goal_id` _numeric string or integer_<br>The ID of a Conversion Goal.<br>`offsite_conversion_event_id` _numeric string or integer_<br>The ID of a Offsite Conversion Event<br>`boosted_product_set_id` _numeric string or integer_<br>The ID of the Boosted Product Set within an Ad Set level Product<br>Catalog. Should only be present when the advertiser has<br>opted into Product Set Boosting.<br>`lead_ads_form_event_source_type` _enum{inferred, meta\_source, offsite\_crm, offsite\_web, onsite\_crm, onsite\_crm\_single\_event, onsite\_clo\_dep\_aet, onsite\_web, onsite\_p2b\_call, onsite\_messaging, qualified\_lead\_file}_<br>The event source of lead ads form.<br>`lead_ads_custom_event_type` _enum{AD\_IMPRESSION, RATE, TUTORIAL\_COMPLETION, CONTACT, CUSTOMIZE\_PRODUCT, DONATE, FIND\_LOCATION, SCHEDULE, START\_TRIAL, SUBMIT\_APPLICATION, SUBSCRIBE, ADD\_TO\_CART, ADD\_TO\_WISHLIST, INITIATED\_CHECKOUT, ADD\_PAYMENT\_INFO, PURCHASE, LEAD, COMPLETE\_REGISTRATION, CONTENT\_VIEW, SEARCH, SERVICE\_BOOKING\_REQUEST, MESSAGING\_CONVERSATION\_STARTED\_7D, LEVEL\_ACHIEVED, ACHIEVEMENT\_UNLOCKED, SPENT\_CREDITS, LISTING\_INTERACTION, D2\_RETENTION, D7\_RETENTION, OTHER}_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`lead_ads_custom_event_str` _string_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`lead_ads_offsite_conversion_type` _enum{default, clo}_<br>The offsite conversion type for lead ads<br>`value_semantic_type` _enum {VALUE, MARGIN, LIFETIME\_VALUE}_<br>The semantic of the event value to be using for optimization<br>`variation` _enum {OMNI\_CHANNEL\_SHOP\_AUTOMATIC\_DATA\_COLLECTION, PRODUCT\_SET\_AND\_APP, PRODUCT\_SET\_AND\_IN\_STORE, PRODUCT\_SET\_AND\_OMNICHANNEL, PRODUCT\_SET\_AND\_PHONE\_CALL, PRODUCT\_SET\_AND\_WEBSITE, PRODUCT\_SET\_AND\_WEBSITE\_AND\_PHONE\_CALL, PRODUCT\_SET\_WEBSITE\_APP\_AND\_INSTORE}_<br>Variation of the promoted object for a PCA ad<br>`passback_pixel_id` _numeric string or integer_<br>ID of the pixel used for tracking passback events<br>`passback_application_id` _numeric string or integer_<br>ID of the application used for tracking passback events<br>`product_set_optimization` _enum{enabled, disabled}_<br>Enum defining whether or not the ad should be optimized for the promoted product set<br>`full_funnel_objective` _enum{OFFER\_CLAIMS, PAGE\_LIKES, EVENT\_RESPONSES, POST\_ENGAGEMENT, WEBSITE\_CONVERSIONS, LINK\_CLICKS, VIDEO\_VIEWS, LOCAL\_AWARENESS, PRODUCT\_CATALOG\_SALES, LEAD\_GENERATION, BRAND\_AWARENESS, STORE\_VISITS, REACH, APP\_INSTALLS, MESSAGES, OUTCOME\_AWARENESS, OUTCOME\_ENGAGEMENT, OUTCOME\_LEADS, OUTCOME\_SALES, OUTCOME\_TRAFFIC, OUTCOME\_APP\_PROMOTION}_<br>Enum defining the full funnel objective of the campaign<br>`dataset_split_id` _numeric string or integer_<br>ID of the dataset split used to perform additional optimization on the dataset<br>`dataset_split_ids` _array<numeric string>_<br>IDs of the dataset splits used to perform additional optimization on the dataset<br>`lead_ads_selected_pixel_id` _numeric string or integer_<br>The selected pixel id for lead ads conversion leads optimization<br>`custom_attribution_source_ids` _array<numeric string>_<br>IDs of the custom attribution sources used for tracking passback events<br>`multi_event_product` _int64_<br>Identifies which action-to-action product the advertiser is using<br>`product_sales_channel` _enum {ONLINE, IN\_STORE, OMNI}_<br>ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads<br>`anchor_event_config` _JSON object_<br>Configuration for anchor event in multi-event optimization campaigns<br>`multi_event_conversion_info` _JSON object_<br>Configuration for multi-event conversion info in CLO campaigns<br>`live_video_destination` _string_<br>The live video destination type for live video ads<br>`smart_pse_enabled` _boolean_<br>Whether Smart Product Set Expansion is enabled for this campaign.<br>`smart_pse_setting` _enum{ENABLED, DISABLED}_<br>Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues.<br>`lead_ads_follow_up_event` _enum{whatsapp\_conversations}_<br>The selected lead follow-up event for lead ads campaigns.<br>`omnichannel_object` _Object_ <br>* * *<br>`app` _array<JSON object>_<br>`pixel` _array<JSON object>_ <br>required<br>`onsite` _array<JSON object>_<br>Show child parameters<br>`whats_app_business_phone_number_id` _numeric string or integer_<br>`whatsapp_phone_number` _string_<br>Show child parameters |
| `smart_promotion_type`<br>_enum{GUIDED\_CREATION, SMART\_APP\_PROMOTION}_ | smart\_promotion\_type |
| `special_ad_category`<br>_enum{NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES\_ELECTIONS\_POLITICS, ONLINE\_GAMBLING\_AND\_GAMING, FINANCIAL\_PRODUCTS\_SERVICES}_ | special\_ad\_category |
| `special_ad_category_country`<br>_array<enum {AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}>_ | special\_ad\_category\_country |
| `spend_cap`<br>_int64_ | A spend cap for the campaign, such that it will not spend more than this cap. Defined as integer value of subunit in your currency with a minimum value of $100 USD (or approximate local equivalent). Set the value to 922337203685478 to remove the spend cap. Not available for Reach and Frequency or Premium Self Serve campaigns |
| `start_time`<br>_datetime_ | start\_time |
| `status`<br>_enum{ACTIVE, PAUSED, DELETED, ARCHIVED}_ | Only `ACTIVE` and `PAUSED` are valid during<br>creation. Other statuses can be used for update. If it is set to<br>`PAUSED`, its active child objects will be paused and have an effective<br>status `CAMPAIGN_PAUSED`. |
| `stop_time`<br>_datetime_ | stop\_time |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node to which you POSTed.

```
Struct  {
success: bool,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 613 | Calls to this api have exceeded the rate limit. |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 801 | Invalid operation |

* * *

## Deleting

### /{campaign\_id}

You can delete a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) by making a DELETE request to [/{campaign\_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group).

#### Parameters

This endpoint doesn't have any parameters.

#### Return Type

```
Struct  {
success: bool,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

* * *

### /act\_{ad\_account\_id}/campaigns

You can dissociate a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) from an [AdAccount](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account) by making a DELETE request to [/act\_{ad\_account\_id}/campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns).

#### Parameters

| Parameter | Description |
| --- | --- |
| `before_date`<br>_datetime_ | Set a before date to delete campaigns before this date |
| `delete_strategy`<br>_enum{DELETE\_ANY, DELETE\_OLDEST, DELETE\_ARCHIVED\_BEFORE}_ | Delete strategy<br>required |
| `object_count`<br>_integer_ | Object count |

#### Return Type

```
Struct  {
objects_left_to_delete_count: unsigned int32,
deleted_object_ids:  List  [numeric string],
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |

* * *

## Objective Validation

These older objectives are deprecated with the release of [Marketing API v17.0](https://developers.facebook.com/docs/graph-api/changelog/version17.0#marketing-api). Please refer to the [Outcome-Driven Ads Experiences mapping table](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax-mapping) below to find the new objectives and their corresponding destination types, optimization goals and promoted objects.

Your campaign objective choice can limit the settings available to you.

### Optimization Goals

Certain campaign objectives support only certain ad set `optimization_goals`. See [Bidding Overview, Validation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/overview#opt-goal-validation).

### Compatible Ad Types

| Objective | Compatible Ad Types |
| --- | --- |
| `APP_INSTALLS` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>[Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `BRAND_AWARENESS` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `CONVERSIONS` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>[App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Ads that click to Messenger](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads#destination)<br>[Offer Ads](https://developers.facebook.com/docs/marketing-api/guides/offer-ads)<br>[Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>[Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `EVENT_RESPONSES` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Event and Local Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/event-ads) |
| `LEAD_GENERATION` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Lead Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `LINK_CLICKS` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>[App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Offer Ads](https://developers.facebook.com/docs/marketing-api/guides/offer-ads)<br>[Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>[Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `MESSAGES` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Messenger Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads#destination) |
| `POST_ENGAGEMENT` | Image Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign)) |
| `PRODUCT_CATALOG_SALES` | Image Ads<br>Carousel Ads<br>[Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>[Collaborative Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/collaborative-ads) |
| `REACH` | Image Ads<br>Video Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `STORE_VISITS` | Image Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Offer Ads](https://developers.facebook.com/docs/marketing-api/guides/offer-ads) |
| `VIDEO_VIEWS` | Video Ads<br>Carousel Ads<br>[Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>[Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>[Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>[Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>[Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>[Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |

### Objectives and Creative Fields

See our [ads guide⁠](https://www.facebook.com/business/ads-guide/) for a list of creatives supported per objective. In the API, the objective determines which [ad creatives](https://developers.facebook.com/docs/reference/ads-api/adcreative) are valid.

| Objective | Creative Fields |
| --- | --- |
| `APP_INSTALLS` | `object_story_id` or `object_story_spec` |
| `CONVERSIONS` | `object_story_id` or `object_story_spec`<br>Notes:<br>If you are creating link ads not connected to a page, use the following creative fields: `title`, `body`, `object_url`, and `image_file` or `image_hash`.<br>Creative cannot include link ads pointing to an app store. |
| `EVENT_RESPONSES` | `object_story_id` or `object_story_spec` |
| `LEAD_GENERATION` | `object_story_id` or `object_story_spec` |
| `LINK_CLICKS` | `object_story_id` or `object_story_spec`<br>Notes:<br>Creative cannot include link ads pointing to an app store.<br>If you select `LINK_CLICKS` as both optimization goal and billing event, you must include `call_to_action`. |
| `MESSAGES` | `object_story_spec` |
| `PAGE_LIKES` | `object_story_id`, `object_story_spec`, `object_id`, and `body` |
| `POST_ENGAGEMENT` | `object_story_id` or `object_story_spec`<br>Note: Creative cannot include link ads pointing to an app store. |
| `VIDEO_VIEWS` | `object_story_id` or `object_story_spec` |

### Objectives and Tracking Specs

Tracking specs are applied by default based on the objective specified, please see the full list of defaults by objective [here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/tracking-specs#default).

There are two important scenarios to take into account:

Tracking pixels are not applied by default, and you must specify it explicitly when your objective is `CONVERSIONS`.
Mobile app ads will no longer track installs or app events by default. **You must explicitly specify to track installs or app events for mobile app ads otherwise your ad will not track.**

To specify to track an install or app event, set the following in your [ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup):

```
tracking_specs=[{'action.type':['mobile_app_install'],'application':[{your_app_id}]},{'action.type':['app_custom_event'],'application':[{your_app_id}]}]
```

### Objective and Promoted Objects

Certain objectives require the `promoted_object` to be set in ad sets. See [Promoted Object](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object) for more information.

| Objective | Required promoted\_object Fields |
| --- | --- |
| `APP_INSTALLS` | `application_id` and `object_store_url`<br>If `optimization_goal` is `OFFSITE_CONVERSIONS`: `application_id`, `object_store_url`, and `custom_event_type` |
| `CONVERSIONS` | `pixel_id` (Conversion pixel ID)<br>`pixel_id` (Facebook pixel ID) and `custom_event_type`<br>`pixel_id` (Facebook pixel ID), `pixel_rule`, and `custom_event_type`<br>`event_id` (Facebook event ID) and `custom_event_type`<br>For mobile app events: `application_id`, `object_store_url`, and `custom_event_type`<br>For offline conversions: `offline_conversion_data_set_id` (Offline dataset ID), and `custom_event_type` |
| `LINK_CLICKS` | For mobile app or Instant Experiences app engagement link clicks: `application_id` and `object_store_url`. |
| `PRODUCT_CATALOG_SALES` | `product_set_id`, or<br>`product_set_id` and `custom_event_type` |
| `PAGE_LIKES` | `page_id` |
| `OFFER_CLAIMS` | `page_id` |

### Objective and Placements

Certain types of ad [placements](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#placement) are valid only for specific objectives or creatives. See [Business Help Center, Available ad placements for marketing objectives⁠](https://www.facebook.com/business/help/279271845888065?id=369787570424415).

The table below shows some placements and their compatible objectives or creatives. You can pick a combination of those compatible placements. Note that:

With `LEAD_GENERATION`, `device_platforms: desktop` cannot be selected together with `publisher_platforms: instagram`.
If your objective is website traffic, `story` for `facebook_positions` does not support `destination_type: messenger`.
If your objective is website traffic, `story` for `messenger_positions` does not support `destination_type: messenger`.
If your objective is website traffic, `ig_search` and `explore_home` for `instagram_positions` do not support `destination_type: whatsapp & messenger`.

| Objective | Creative | Placement |
| --- | --- | --- |
| `APP_INSTALLS`, promoting an Instant Experiences app | Desktop app ads | `device_platforms`: `desktop` |
| `APP_INSTALLS`, promoting a mobile app | Photo or video mobile app ads | `device_platforms`: `mobile`<br>`publisher_platforms`: `facebook`, `feed`, `instagram`, `audience_network`<br>`facebook_positions`: `feed`, `video_feeds`, `instant articles` and `story`<br>`audience_network_positions`: `classic`, `rewarded_video`<br>`messenger_positions`: `story` |
| `BRAND_AWARENESS` | all | `publisher_platforms`: `facebook`, `instagram`, `audience_network`.<br>`facebook_positions`: `feed`, `video_feeds`, `instream_video` and `story`, which is currently under limited availability<br>`instagram_positions`: `stream`<br>`audience_network_positions`: `classic`, `instream_video` |
| `CONVERSIONS` | Photo or video link ads from a page | We support `BRAND_AWARENESS`, `APP_INSTALL`, `POST_ENGAGEMENT`, `VIDEO_VIEWS`, `REACH`, `WEBSITE_CONVERSIONS`, and `TRAFFIC`.<br>Also supported: `right_hand_column` and `story` for `facebook_positions` and `messenger_positions`: `messenger_home` and `story`.<br>`facebook_positions`: `story` only supports the objective `WEBSITE_CONVERSIONS`<br>`messenger_positions`: `story` only supports the objective `WEBSITE_CONVERSIONS`<br>Exception: `instream_video` is not supported for this objective. |
| `CONVERSIONS` | Link ads not connected to a page | `facebook_positions`: `right_hand_column` |
| `CONVERSIONS` (promoting mobile app) | Photo or video mobile app ads | `device_platforms`: `mobile`.<br>`facebook_positions`: `right_hand_column` and `story`. `story` as a `facebook_positions` for this objective does not support `destination_type`: `messenger`.<br>`messenger_positions`: `messenger_home`<br>`story` as a `messenger_positions` for this objective does not support `destination_type: messenger`. |
| `EVENT_RESPONSES` | Event ads | As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `EVENT_RESPONSES` | Page post ads | `publisher_platforms`: `facebook`. <br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `LEAD_GENERATION` | Page post ads | `device_platforms`: `mobile`, `desktop`<br>`publisher_platforms`: `facebook`, `instagram`<br>`facebook_positions`: `feed` and `story`, which is in limited availability<br>instagram\_positions: stream<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `LINK_CLICKS` | Photo or video link ads from a page | All, including `right_hand_column` and `messenger_positions`: `messenger_home` and `story`. |
| `LINK_CLICKS` | Link ads not connected to a page | `facebook_positions`: `right_hand_column` |
| `LINK_CLICKS`, promoting an Instant Experiences app | Desktop app ads | `device_platforms`: `desktop`<br>`facebook_positions`: `right_hand_column` |
| `LINK_CLICKS`, promoting a mobile app | Photo or video mobile app ads | `device_platforms`: `mobile`, `facebook_positions`: `right_hand_column` |
| `PAGE_LIKES` | Video creatives | `publisher_platforms`: `facebook`<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `POST_ENGAGEMENT` | Page post ads with video or photo | `publisher_platforms`: `facebook`, `instagram`<br>`device_platforms`: `mobile`, `desktop`<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `POST_ENGAGEMENT` | Page post ads with text only | `publisher_platforms`: `facebook`, `instagram`<br>`device_platforms`: `mobile`, `desktop`<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `POST_ENGAGEMENT` | New campaign | `publisher_platforms`: `facebook`, `instagram`<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `PRODUCT_CATALOG_SALES` | dynamic ads | All, including `right_hand_column` for `facebook_positions`. |
| `REACH` | Reach ads | All except `right_hand_column` for `facebook_positions` as of 3.0. <br>Includes `messenger_positions`: `story` and `story` for `facebook_positions`. |
| `STORE_VISITS` | store visit ads | `publisher_platforms`: `facebook`<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `VIDEO_VIEWS` | Video ads | `publisher_platforms`: `facebook`, `instagram`, `audience_network`.<br>Includes `story` for `facebook_positions` but not with the `optimation_goal` set to `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS`.<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |

### Objective, Optimization Goal and `attribution_spec`

Use click-through and view-through attribution windows for [ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign#Creating) to track conversions then use for ads delivery optimization. This is different from the attribution window you use for ads reporting. With `attribution_spec`, select a combination of click-through or view-through windows of 1 day or 7 days. The combinations you can use depend on your ad set’s `optimization_goal` and campaign’s `objective`.

**Recommended Default `attribution_spec`**

You may not have provided `attribution_spec` when you created ads sets optimized for Value Optimization. This is an optimization available for conversions, app installs, and product catalog sales objectives. In the past, we defaulted to a 1-day click through attribution window.

| Objective | Optimization Goal | Allowed Combination |
| --- | --- | --- |
| `CONVERSIONS, PRODUCT_CATALOG_SALES` | `OFFSITE_CONVERSIONS` | 1-day click<br>7-day click<br>1-day click and 1-day view<br>7-day click and 1-day view |
| `APP_INSTALLS, LINK_CLICKS` | `OFFSITE_CONVERSIONS` | 1-day click<br>7-day click |
| `APP_INSTALLS` | `APP_INSTALLS` | 1-day click<br>1-day click and 1-day engaged-view<br>1-day click and 1-day view<br>1-day click and 1-day engaged-view and 1-day view |
| `CONVERSIONS` | `INCREMENTAL_OFFSITE_<br>CONVERSIONS` | Null click, Null view |

For all other `optimization_goal` and `objective` combinations, you can only use 1-day click for `attribution_spec`.

### Outcome-Driven Ads Experiences Objective Validation

From v20.0 onwards, Impressions optimization goal is deprecated for the legacy Post Engagement objective and the `ON_POST` destination\_type.

#### Objective values

The following are newer objectives:

`OUTCOME_APP_PROMOTION`
`OUTCOME_AWARENESS`
`OUTCOME_ENGAGEMENT`
`OUTCOME_LEADS`
`OUTCOME_SALES`
`OUTCOME_TRAFFIC`

These newer objectives will eventually replace the original objectives `APP_INSTALLS`, `BRAND_AWARENESS`, `CONVERSIONS`, `EVENT_RESPONSES`, `LEAD_GENERATION`, `LINK_CLICKS`, `LOCAL_AWARENESS`, `MESSAGES`, `OFFER_CLAIMS`, `PAGE_LIKES`, `POST_ENGAGEMENT`, `PRODUCT_CATALOG_SALES`, `REACH`, `STORE_VISITS`, `VIDEO_VIEWS`. We will continue supporting these original objectives throughout 2022.

#### Limitations

Trying to duplicate existing objective campaigns to use the new objective values (`OUTCOME_APP_PROMOTION`, `OUTCOME_AWARENESS`, `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS`, `OUTCOME_SALES`, `OUTCOME_TRAFFIC`) may throw an error.

#### Example

**Outcome-Driven Ads Experiences**

![Image](https://scontent-lax3-2.xx.fbcdn.net/v/t39.2365-6/653703878_1459945372530779_5879871268106845470_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=kYAR7193xYMQ7kNvwGegCoy&_nc_oc=AdoLZ4SSr3qucxyANnE9wAjoQFN_Lf065v6MRg9xHBQLZVo8kIm61ic0kc_RuMI2nRE&_nc_zt=14&_nc_ht=scontent-lax3-2.xx&_nc_gid=R3C-u9zGWLyLJoC-Z8DrLA&_nc_ss=7b289&oh=00_Af_i4U-QAc-jd4Js1-6s4J8cJoaVbQyCQfUKOm4krmB99w&oe=6A51AD67)

```
curl -X POST \
  -F 'name="New ODAX Campaign"' \
  -F 'objective="OUTCOME_ENGAGEMENT"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=ACCESS_TOKEN \
  https://graph.facebook.com/v11.0/
  act_AD_ACCOUNT_ID/campaigns
```

**Legacy**

![Image](https://scontent-lax3-1.xx.fbcdn.net/v/t39.2365-6/653700290_1459945435864106_9212131334945364835_n.png?_nc_cat=102&ccb=1-7&_nc_sid=e280be&_nc_ohc=0J4ik5eAvcQQ7kNvwGQSjIv&_nc_oc=AdpzPDWZl2ecP-kPrVus-P5UFRSQa-NRbFD3FEd2lez9zt5K-rMEyxj5BFsouwlAL_U&_nc_zt=14&_nc_ht=scontent-lax3-1.xx&_nc_gid=R3C-u9zGWLyLJoC-Z8DrLA&_nc_ss=7b289&oh=00_Af8cLCJWrTwvDf2RZPbINYXOwtV8gw8yqE3P2L28v20eKw&oe=6A51C10E)

```
curl -X POST \
  -F 'name="New Campaign"' \
  -F 'objective="APP_INSTALLS"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=ACCESS_TOKEN \
  https://graph.facebook.com/v11.0/
  act_AD_ACCOUNT_ID/campaigns
```

#### Objective Mapping

| Old Objective | New Objective | Destination Type | Optimization Goal | Promoted Object |
| --- | --- | --- | --- | --- |
| `BRAND_AWARENESS` | `OUTCOME_AWARENESS` | — | `AD_RECALL_LIFT` | `page_id` |
| `REACH` | `OUTCOME_AWARENESS` | — | `REACH` | `page_id` |
| `IMPRESSIONS` | `page_id` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | — | `LINK_CLICKS` | `application_id`, `object_store_url` |
| `LANDING_PAGE_VIEWS` | — |
| `REACH` | `application_id`, `object_store_url` |
| `IMPRESSIONS` | — |
| `MESSENGER` | `LINK_CLICKS` | — |
| `REACH` | — |
| `IMPRESSIONS` | — |
| `WHATSAPP` | `LINK_CLICKS` | `page_id` |
| `REACH` | `page_id` |
| `IMPRESSIONS` | `page_id` |
| `PHONE_CALL` | `QUALITY_CALL` | — |
| `LINK_CLICKS` | — |
| `POST_ENGAGEMENT` | `OUTCOME_ENGAGEMENT` | `ON_POST` | `POST_ENGAGEMENT` | — |
| `REACH` | — |
| `IMPRESSIONS` | — |
| `PAGE_LIKES` | `OUTCOME_ENGAGEMENT` | `ON_PAGE` | `PAGE_LIKES` | `page_id` |
| `EVENT_RESPONSES` | `OUTCOME_ENGAGEMENT` | `ON_EVENT` | `EVENT_RESPONSES` | — |
| `POST_ENGAGEMENT` | — |
| `REACH` | — |
| `IMPRESSIONS` | — |
| `APP_INSTALL` | `OUTCOME_APP_PROMOTION` | — | `LINK_CLICKS` | `application_id`, `object_store_url` |
| `OFFSITE_CONVERSIONS` | `application_id`, `object_store_url` |
| `APP_INSTALLS` | `application_id`, `object_store_url` |
| `VIDEO_VIEWS` | `OUTCOME_AWARENESS` | — | `THRUPLAY` | `page_id` |
| `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS` | `page_id` |
| `OUTCOME_ENGAGEMENT` | `ON_VIDEO` | `THRUPLAY` | — |
| `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS` | — |
| `LEAD_GENERATION` | `OUTCOME_LEADS` | `ON_AD` | `LEAD_GENERATION` | `page_id` |
| `QUALITY_LEAD` | `page_id` |
| `LEAD_FROM_MESSENGER` | `LEAD_GENERATION` | `page_id` |
| `LEAD_FROM_IG_DIRECT` | `LEAD_GENERATION` | `page_id` |
| `PHONE_CALL` | `QUALITY_CALL` | `page_id` |
| `MESSAGES` | `OUTCOME_ENGAGEMENT` | `MESSENGER` | `CONVERSATIONS` | `page_id` |
| `LINK_CLICKS` | `page_id` |
| `MESSENGER` | `LEAD_GENERATION` | `page_id` |
| `CONVERSIONS`<br>(See [Available conversion locations and events by objective in Meta Ads Manager⁠](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `OFFSITE_CONVERSIONS` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `LINK_CLICKS` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `REACH` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `LANDING_PAGE_VIEWS` | `pixel_id`, `custom_event_type` |
| `IMPRESSIONS` | `pixel_id`, `custom_event_type` |
| `OUTCOME_LEADS` | — | `OFFSITE_CONVERSIONS` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `LINK_CLICKS` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `REACH` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `LANDING_PAGE_VIEWS` | `pixel_id`, `custom_event_type` |
| `IMPRESSIONS` | `pixel_id`, `custom_event_type` |
| `OUTCOME_SALES` | — | `OFFSITE_CONVERSIONS` | `pixel_id`, `custom_event_type` |
| `application_id`, `object_store_url` |
| `MESSENGER` | `CONVERSATIONS` | `page_id`, `pixel_id`, `custom_event_type` |
| `PHONE_CALL` | `QUALITY_CALL` | `page_id` |
| `PRODUCT_CATALOG_SALES` | `OUTCOME_SALES` | `WEBSITE` | `LINK_CLICKS` | Campaign: `product_catalog_id`<br>Ad set: `product_set_id`, `custom_event_type` |
| `STORE_VISITS` | `OUTCOME_AWARENESS` | — | `REACH` | `place_page_set_id` |

Did you find this page helpful?

![Thumbs up icon](https://static.xx.fbcdn.net/rsrc.php/yR/r/OEXJ0_DJeZv.svg)

![Thumbs down icon](https://static.xx.fbcdn.net/rsrc.php/yb/r/qKPgNVNeatU.svg)

* * *