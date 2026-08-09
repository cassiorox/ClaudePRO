<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group.md | Scrape: 2026-08-09 | API v26.0 -->

# Ad Campaign Group



A campaign is the highest level organizational structure within an ad account and should represent a single objective for an advertiser, for example, to drive page post engagement. Setting objective of the campaign will enforce validation on any ads added to the campaign to ensure they also have the correct objective.

**Warning:** The `date_preset = lifetime` parameter is disabled in Graph API v10.0 and replaced with `date_preset = maximum`, which returns a maximum of 37 months of data. For v9.0 and below, `date_preset = maximum` will be enabled on May 25, 2021, and any `lifetime` calls will default to `maximum` and return only 37 months of data.

### Limits

- You can only create 200 ad sets per ad campaign. [Learn more about the ad campaign structure](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group).
- If your campaign has more than 70 ad sets and uses [Campaign Budget Optimization](https://developers.facebook.com/docs/marketing-api/bidding/guides/campaign-budget-optimization), you are not able to edit your current bid strategy or turn off CBO. [Learn more in the Business Help Center](https://www.facebook.com/business/help/519856662172206).

### New Required Field for All Campaigns

All businesses using the Marketing API must identify whether or not new and edited campaigns belong to a [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category). Current available categories are: [housing, employment, credit](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category#context), or issues, elections, and politics. Businesses whose ads do not belong to a Special Ad Category must indicate NONE or send an empty array in the `special_ad_categories` field.

Businesses running **housing**, **employment**, or **credit** ads must comply with [targeting and audience restrictions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-restrictions). Targeting for ads about social issues, elections or politics are not affected by the `special_ad_categories` label.

**Warning:** As of **Marketing API 7.0**, the `special_ad_category` parameter on the [`POST /act_<ad_account_id>/campaigns`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns#Creating) endpoint has been deprecated and replaced with a new `special_ad_categories` parameter. The new `special_ad_categories` parameter is required and accepts an array.

If you use the `special_ad_category` parameter, it will still return a string, but you should use `GET /{campaign-id}?fields=special_ad_categories` to get an array back. Refer  to [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) for additional information.

## Reading

A campaign is a grouping of ad sets which are organized by the same business objective. Each campaign has an objective that must be valid across the ad sets within that campaign.

After your ads begin delivering, you can query stats for ad campaigns. The statistics returned will be unique stats, deduped across the ad sets. You can also get reports and statistics for all ad sets and ads in an campaign simultaneously.

#### Example

### HTTP
```
GET v25.0/...?fields={fieldname_of_type_Campaign} HTTP/1.1
Host: graph.facebook.com
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '...?fields={fieldname_of_type_Campaign}',
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
    "...?fields={fieldname_of_type_Campaign}",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

### Android SDK
```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "...?fields={fieldname_of_type_Campaign}",
    null,
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
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"...?fields={fieldname_of_type_Campaign}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=...%3Ffields%3D%257Bfieldname_of_type_Campaign%257D&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br><br>*enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year}* | Date Preset<br> |
| `time_range`<br><br>*{'since':YYYY-MM-DD,'until':YYYY-MM-DD}* | Time Range. Note if time range is invalid, it will be ignored.<br><br><br>`since` *datetime*<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br><br><br>`until` *datetime*<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br> |

#### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>*numeric string* | Campaign's ID<br><br><br>**[default]**<br> |
| `account_id`<br><br>*numeric string* | ID of the ad account that owns this campaign<br> |
| `adlabels`<br><br>*[list<AdLabel>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label)* | Ad Labels associated with this campaign<br> |
| `bid_strategy` This field is only accessible in v3.0 or later.<br><br>*enum {LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS}* | Bid strategy for this campaign when you enable campaign budget optimization and<br>when you use `AUCTION` as your buying type:<br><br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy to select<br>if you care most about cost efficiency. However, note that it may be harder to get<br>stable average costs as you spend. Note: this strategy is also known as<br>*automatic bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to a specified amount.<br>Get specified bid cap in the `bid_amount` field for each ad set in this ad campaign.<br>This strategy is known as *manual maximum-cost bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`COST_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual average cost per optimization event to a specified amount.<br>Get specified cost cap in the `bid_amount` field for each ad set in this ad campaign.<br>Learn more in [Ads Help Center, About bid strategies: Cost Cap](https://www.facebook.com/business/help/272336376749096?id=2196356200683573).<br>Notes:<br><br><br>• If you do not enable campaign budget optimization, you should get `bid_strategy` at the ad set level.<br>• `TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0).<br> |
| `boosted_object_id`<br><br>*numeric string* | The Boosted Object this campaign has associated, if any<br> |
| `brand_lift_studies`<br><br>*[list<AdStudy>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-study)* | Automated Brand Lift V2 studies for this ad set.<br> |
| `budget_rebalance_flag`<br><br>*bool* | Whether to automatically rebalance budgets daily for all the adsets under this campaign. [This has been deprecated on Marketing API V7.0](https://developers.facebook.com/docs/graph-api/changelog/version7.0#deprecations).<br> |
| `budget_remaining`<br><br>*numeric string* | Remaining budget<br> |
| `buying_type`<br><br>*string* | Buying type, possible values are: <br>`AUCTION`: default<br>`RESERVED`: for [reach and frequency ads](https://developers.facebook.com/docs/marketing-api/reachandfrequency)<br>[Reach and Frequency](https://developers.facebook.com/docs/marketing-api/reachandfrequency) is disabled for [housing, employment and credit ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category).<br> |
| `campaign_group_active_time`<br><br>*numeric string* | campaign_group_active_time this is only for Internal, This will have the active running length of Campaign Groups<br> |
| `can_create_brand_lift_study`<br><br>*bool* | If we can create a new automated brand lift study for the ad set.<br> |
| `can_use_spend_cap`<br><br>*bool* | Whether the campaign can set the spend cap<br> |
| `configured_status`<br><br>*enum {ACTIVE, PAUSED, DELETED, ARCHIVED}* | If this status is `PAUSED`, all its active ad sets and ads will<br>be paused and have an effective status `CAMPAIGN_PAUSED`. Prefer<br>using 'status' instead of this.<br> |
| `created_time`<br><br>*datetime* | Created Time<br> |
| `daily_budget`<br><br>*numeric string* | The daily budget of the campaign<br> |
| `effective_status`<br><br>*enum {ACTIVE, PAUSED, DELETED, ARCHIVED, IN_PROCESS, WITH_ISSUES}* | IN_PROCESS is available for version 4.0 or higher<br> |
| `has_secondary_skadnetwork_reporting`<br><br>*bool* | has_secondary_skadnetwork_reporting<br> |
| `is_adset_budget_sharing_enabled`<br><br>*bool* | Whether the child ad sets are managed under ad set budget sharing<br> |
| `is_budget_schedule_enabled`<br><br>*bool* | Whether budget scheduling is enabled for the campaign group<br> |
| `is_reels_trending_ads_enabled`<br><br>*bool* | is_reels_trending_ads_enabled<br> |
| `is_skadnetwork_attribution`<br><br>*bool* | When set to `true` Indicates that the campaign will include SKAdNetwork, iOS 14+.<br> |
| `issues_info` This field is only accessible in v3.2 or later.<br><br>*[list<AdCampaignIssuesInfo>](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-issues-info)* | Issues for this campaign that prevented it from deliverying<br> |
| `last_budget_toggling_time`<br><br>*datetime* | Last budget toggling time<br> |
| `lifetime_budget`<br><br>*numeric string* | The lifetime budget of the campaign<br> |
| `name`<br><br>*string* | Campaign's name<br> |
| `objective`<br><br>*string* | Campaign's objective<br><br><br>See the [Outcome Ad-Driven Experience Objective Validation](#odax) section below for more information.<br> |
| `pacing_type`<br><br>*list<string>* | Defines pacing type of the campaign. The value is an array of options:  "standard".<br> |
| `primary_attribution`<br><br>*enum* | primary_attribution<br> |
| `promoted_object`<br><br>*[AdPromotedObject](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object)* | The object this campaign is promoting across all its ads<br> |
| `smart_promotion_type`<br><br>*enum* | Smart Promotion Type. guided_creation or smart_app_promotion(the choice under APP_INSTALLS objective).<br> |
| `source_campaign`<br><br>*[Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group)* | The source campaign that this campaign is copied from<br> |
| `source_campaign_id`<br><br>*numeric string* | The source campaign id that this campaign is copied from<br> |
| `special_ad_categories` This field is only accessible in v7.0 or later.<br><br>*list<enum>* | special ad categories<br> |
| `special_ad_category`<br><br>*enum* | The campaign's Special Ad Category. One of `HOUSING`, `EMPLOYMENT`, `CREDIT`, or `NONE`.<br> |
| `special_ad_category_country` This field is only accessible in v7.0 or later.<br><br>*list<enum>* | Country field for  Special Ad Category.<br> |
| `spend_cap`<br><br>*numeric string* | A spend cap for the campaign, such that it will not spend more than this cap. Expressed as integer value of the subunit in your currency.<br> |
| `start_time`<br><br>*datetime* | Merging of `start_time`s for the ad sets belonging to this campaign. At the campaign level, `start_time` is a read only field. You can setup `start_time` at the ad set level.<br> |
| `status`<br><br>*enum {ACTIVE, PAUSED, DELETED, ARCHIVED}* | If this status is `PAUSED`, all its active ad sets and ads will<br>be paused and have an effective status `CAMPAIGN_PAUSED`. The field<br>returns the same value as 'configured_status', and is the suggested<br>one to use.<br> |
| `stop_time`<br><br>*datetime* | Merging of `stop_time`s for the ad sets belonging to this campaign, if available. At the campaign level, `stop_time` is a read only field. You can setup `stop_time` at the ad set level.<br> |
| `topline_id`<br><br>*numeric string* | Topline ID<br> |
| `updated_time`<br><br>*datetime* | Updated Time. If you update `spend_cap` or daily budget or lifetime budget, this will not automatically update this field.<br> |

#### Edges

| Edge | Description |
| --- | --- |
| [`ad_studies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/ad_studies)<br><br>*Edge<AdStudy>* | The ad studies containing this campaign<br> |
| [`adrules_governed`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/adrules_governed)<br><br>*Edge<AdRule>* | Ad rules that govern this campaign - by default, this only returns rules that either directly mention the campaign by id or indirectly through the set entity_type<br> |
| [`ads`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/ads)<br><br>*Edge<Adgroup>* | Ads under this campaign<br> |
| [`adsets`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/adsets)<br><br>*Edge<AdCampaign>* | The ad sets under this campaign<br> |
| [`copies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/copies)<br><br>*Edge<AdCampaignGroup>* | The copies of this campaign<br> |

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

### /act_{ad_account_id}/async_batch_requests
You can make a POST request to *async_batch_requests* edge from the following paths:

- [/act_{ad_account_id}/async_batch_requests](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/async_batch_requests)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `adbatch`<br><br>*list<Object>* | JSON encoded batch reqeust<br><br>**[required]**<br><br><br>`name` *string*<br>**[required]**<br><br><br>`relative_url` *string*<br>**[required]**<br><br><br>`body` *UTF-8 encoded string*<br>**[required]**<br> |
| `name`<br><br>*UTF-8 encoded string* | Name of the batch request for tracking purposes.<br><br>**[required]**<br> |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *id* in the return type.

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

### /{campaign_id}/copies
You can make a POST request to *copies* edge from the following paths:

- [/{campaign_id}/copies](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/copies)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `deep_copy`<br><br>*boolean* | **Default value: **`false`<br>Whether to copy all the child ads. Limits: the total number of children ads to copy should not exceed 3 for a synchronous call and 51 for an asynchronous call.<br> |
| `end_time`<br><br>*datetime* | For deep copy, the end time of the sets under the copied campaign, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. When creating a set with a daily budget, specify `end_time=0` to set the set to be ongoing without end date. If not set, the copied sets will inherit the end time from the original set<br> |
| `parameter_overrides`<br><br>*Campaign spec* | parameter_overrides<br> |
| `rename_options`<br><br>*JSON or object-like arrays* | Rename options<br><br><br>`rename_strategy` *enum {DEEP_RENAME, ONLY_TOP_LEVEL_RENAME, NO_RENAME}*<br><br>**Default value: **`ONLY_TOP_LEVEL_RENAME`<br>`DEEP_RENAME`: will change this object's name and children's names in the copied object. `ONLY_TOP_LEVEL_RENAME`: will change the this object's name but won't change the children's name in the copied object. `NO_RENAME`: will change no name in the copied object<br><br><br>`rename_prefix` *string*<br>A prefix to copy names. Defaults to null if not provided.<br><br><br>`rename_suffix` *string*<br>A suffix to copy names. Defaults to null if not provided and appends a localized string of `- Copy` based on the ad account locale.<br> |
| `start_time`<br><br>*datetime* | For deep copy, the start time of the sets under the copied campaign, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. If not set, the copied sets will inherit the start time from the original set<br> |
| `status_option`<br><br>*enum {ACTIVE, PAUSED, INHERITED_FROM_SOURCE}* | **Default value: **`PAUSED`<br>`ACTIVE`: the copied campaign will have active status. `PAUSED`: the copied campaign will have paused status. `INHERITED_FROM_SOURCE`: the copied campaign will have the parent status.<br> |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *copied_campaign_id* in the return type.

```
Struct  {
copied_campaign_id: numeric string,
ad_object_ids:  List  [ Struct  {
ad_object_type: enum {
unique_adcreative,
ad,
ad_set,
campaign,
opportunities,
privacy_info_center,
topline,
ad_account,
product},
source_id: numeric string,
copied_id: numeric string,
}],
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

### /act_{ad_account_id}/campaigns
You can make a POST request to *campaigns* edge from the following paths:

- [/act_{ad_account_id}/campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.

#### Example

### HTTP
```
POST /v25.0/act_<AD_ACCOUNT_ID>/campaigns HTTP/1.1
Host: graph.facebook.com

name=My+campaign&objective=OUTCOME_TRAFFIC&status=PAUSED&special_ad_categories=%5B%5D&is_adset_budget_sharing_enabled=0
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/act_<AD_ACCOUNT_ID>/campaigns',
    array (
      'name' => 'My campaign',
      'objective' => 'OUTCOME_TRAFFIC',
      'status' => 'PAUSED',
      'special_ad_categories' => '[]',
      'is_adset_budget_sharing_enabled' => '0',
    ),
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
    "/act_<AD_ACCOUNT_ID>/campaigns",
    "POST",
    {
        "name": "My campaign",
        "objective": "OUTCOME_TRAFFIC",
        "status": "PAUSED",
        "special_ad_categories": "[]",
        "is_adset_budget_sharing_enabled": "0"
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
params.putString("name", "My campaign");
params.putString("objective", "OUTCOME_TRAFFIC");
params.putString("status", "PAUSED");
params.putString("special_ad_categories", "[]");
params.putString("is_adset_budget_sharing_enabled", "0");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/campaigns",
    params,
    HttpMethod.POST,
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
  @"name": @"My campaign",
  @"objective": @"OUTCOME_TRAFFIC",
  @"status": @"PAUSED",
  @"special_ad_categories": @"[]",
  @"is_adset_budget_sharing_enabled": @"0",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/campaigns"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

### cURL
```
curl -X POST \
  -F 'name="My campaign"' \
  -F 'objective="OUTCOME_TRAFFIC"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'is_adset_budget_sharing_enabled=0' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fcampaigns%3Fname%3DMy%2Bcampaign%26objective%3DOUTCOME_TRAFFIC%26status%3DPAUSED%26special_ad_categories%3D%255B%255D%26is_adset_budget_sharing_enabled%3D0&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `adlabels`<br><br>*list<Object>* | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this campaign<br> |
| `bid_strategy` This field is only accessible in v3.0 or later.<br><br>*enum{LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS}* | Choose bid strategy for this campaign to suit your specific business goals.<br>Each strategy has tradeoffs and may be available for certain `optimization_goal`s:<br><br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as *automatic bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. If you select this, you must provide<br>a bid cap in the `bid_amount` field for each ad set in this ad campaign.<br>Note: during creation this is the default bid strategy if you don't specify.<br>This strategy is also known as *manual maximum-cost bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br><br>**Notes:**<br><br><br>• If you do not enable campaign budget optimization, you should set `bid_strategy` at ad set level.<br>• `TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0).<br> |
| `budget_schedule_specs`<br><br>*list<JSON or object-like arrays>* | Initial high demand periods to be created with the campaign.<br><br>Provide list of `time_start`, `time_end`,`budget_value`, and `budget_value_type`.<br>For example,<br>-F 'budget_schedule_specs=[{<br><br>"time_start":1699081200,<br><br>"time_end":1699167600,<br><br>"budget_value":100,<br><br>"budget_value_type":"ABSOLUTE"<br><br>}]'<br><br>See [High Demand Period](https://developers.facebook.com/docs/graph-api/reference/high-demand-period) for more details on each field.<br><br><br>`id` *int64*<br><br>`time_start` *datetime*<br><br>`time_end` *datetime*<br><br>`budget_value` *int64*<br><br>`budget_value_type` *enum{ABSOLUTE, MULTIPLIER}*<br><br>`recurrence_type` *enum{ONE_TIME, WEEKLY}*<br><br>`weekly_schedule` *list<JSON or object-like arrays>*<br><br>`days` *list<int64>*<br><br>`minute_start` *int64*<br><br>`minute_end` *int64*<br><br>`timezone_type` *string* |
| `buying_type`<br><br>*string* | **Default value: **`AUCTION`<br>This field will help Facebook make optimizations to delivery, pricing, and limits. All ad sets in this campaign must match the buying type. Possible values are: <br>`AUCTION` (default)<br>`RESERVED` (for [reach and frequency ads](https://developers.facebook.com/docs/marketing-api/reachandfrequency)).<br> |
| `campaign_optimization_type`<br><br>*enum{NONE, ICO_ONLY}* | campaign_optimization_type<br> |
| `daily_budget`<br><br>*int64* | Daily budget of this campaign. All adsets under this<br>campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both.<br> |
| `execution_options`<br><br>*list<enum{validate_only, include_recommendations}>* | **Default value: **`Set`<br>An execution setting<br> `validate_only`: when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. <br>`include_recommendations`: this option cannot be used by itself. When this option is used, recommendations  for ad object's configuration will be included. A separate section [recommendations](https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation) will be included in the response, but only if recommendations for this specification exist.<br>If the call passes validation or review, response will be `{"success": true}`. If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review.<br> |
| `is_skadnetwork_attribution`<br><br>*boolean* | To create an iOS 14 campaign, enable SKAdNetwork attribution for this campaign.<br> |
| `is_using_l3_schedule`<br><br>*boolean* | is_using_l3_schedule<br> |
| `iterative_split_test_configs`<br><br>*list<Object>* | Array of Iterative Split Test Configs created under this campaign .<br> |
| `lifetime_budget`<br><br>*int64* | Lifetime budget of this campaign. All adsets under<br>this campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both.<br> |
| `name`<br><br>*string* | Name for this campaign<br><br>**[supports emoji]**<br> |
| `objective`<br><br>*enum{APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, OUTCOME_APP_PROMOTION, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS}* | Campaign's objective. If it is specified the API will validate that any ads created under the campaign match that objective. <br>Currently, with `BRAND_AWARENESS` objective, all creatives should be either only images or only videos, not mixed.<br><br>See [Outcome Ad-Driven Experience Objective Validation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax) for more information.<br> |
| `promoted_object`<br><br>*Object* | The object this campaign is promoting across all its ads. It’s required for Meta iOS 14+ app promotion (SKAdNetwork or Aggregated Event Measurement) campaign creation. Only `product_catalog_id` is used at the ad set level.<br><br><br>`application_id` *int*<br>The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement<br><br><br>`pixel_id` *numeric string or integer*<br>The ID of a Facebook conversion pixel.  Used with offsite conversion campaigns.<br><br><br>`custom_event_type` *enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER}*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`object_store_url` *URL*<br>The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br><br><br>`object_store_urls` *list<URL>*<br>The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br><br><br>`offer_id` *numeric string or integer*<br>The ID of an Offer from a Facebook Page.<br><br><br>`page_id` *Page ID*<br>The ID of a Facebook Page<br><br><br>`product_catalog_id` *numeric string or integer*<br>The ID of a Product Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br><br><br>`product_item_id` *numeric string or integer*<br>The ID of the product item.<br><br><br>`job_listing_id` *numeric string or integer*<br>The ID of the marketplace job listing.<br><br><br>`instagram_profile_id` *numeric string or integer*<br>The ID of the instagram profile id.<br><br><br>`product_set_id` *numeric string or integer*<br>The ID of a Product Set within an Ad Set level Product<br>Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br><br><br>`event_id` *numeric string or integer*<br>The ID of a Facebook Event<br><br><br>`offline_conversion_data_set_id` *numeric string or integer*<br>The ID of the offline dataset.<br><br><br>`fundraiser_campaign_id` *numeric string or integer*<br>The ID of the fundraiser campaign.<br><br><br>`custom_event_str` *string*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`mcme_conversion_id` *numeric string or integer*<br>The ID of a MCME conversion.<br><br><br>`conversion_goal_id` *numeric string or integer*<br>The ID of a Conversion Goal.<br><br><br>`offsite_conversion_event_id` *numeric string or integer*<br>The ID of a Offsite Conversion Event<br><br><br>`boosted_product_set_id` *numeric string or integer*<br>The ID of the Boosted Product Set within an Ad Set level Product<br>Catalog. Should only be present when the advertiser has<br>opted into Product Set Boosting.<br><br><br>`lead_ads_form_event_source_type` *enum{inferred, meta_source, offsite_crm, offsite_web, onsite_crm, onsite_crm_single_event, onsite_clo_dep_aet, onsite_web, onsite_p2b_call, onsite_messaging, qualified_lead_file}*<br>The event source of lead ads form.<br><br><br>`lead_ads_custom_event_type` *enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER}*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`lead_ads_custom_event_str` *string*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`lead_ads_offsite_conversion_type` *enum{default, clo}*<br>The offsite conversion type for lead ads<br><br><br>`value_semantic_type` *enum {VALUE, MARGIN, LIFETIME_VALUE}*<br>The semantic of the event value to be using for optimization<br><br><br>`variation` *enum {OMNI_CHANNEL_SHOP_AUTOMATIC_DATA_COLLECTION, PRODUCT_SET_AND_APP, PRODUCT_SET_AND_IN_STORE, PRODUCT_SET_AND_OMNICHANNEL, PRODUCT_SET_AND_PHONE_CALL, PRODUCT_SET_AND_WEBSITE, PRODUCT_SET_AND_WEBSITE_AND_PHONE_CALL, PRODUCT_SET_WEBSITE_APP_AND_INSTORE}*<br>Variation of the promoted object for a PCA ad<br><br><br>`passback_pixel_id` *numeric string or integer*<br>ID of the pixel used for tracking passback events<br><br><br>`passback_application_id` *numeric string or integer*<br>ID of the application used for tracking passback events<br><br><br>`product_set_optimization` *enum{enabled, disabled}*<br>Enum defining whether or not the ad should be optimized for the promoted product set<br><br><br>`full_funnel_objective` *enum{OFFER_CLAIMS, PAGE_LIKES, EVENT_RESPONSES, POST_ENGAGEMENT, WEBSITE_CONVERSIONS, LINK_CLICKS, VIDEO_VIEWS, LOCAL_AWARENESS, PRODUCT_CATALOG_SALES, LEAD_GENERATION, BRAND_AWARENESS, STORE_VISITS, REACH, APP_INSTALLS, MESSAGES, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION}*<br>Enum defining the full funnel objective of the campaign<br><br><br>`dataset_split_id` *numeric string or integer*<br>ID of the dataset split used to perform additional optimization on the dataset<br><br><br>`dataset_split_ids` *array<numeric string>*<br>IDs of the dataset splits used to perform additional optimization on the dataset<br><br><br>`lead_ads_selected_pixel_id` *numeric string or integer*<br>The selected pixel id for lead ads conversion leads optimization<br><br><br>`custom_attribution_source_ids` *array<numeric string>*<br>IDs of the custom attribution sources used for tracking passback events<br><br><br>`multi_event_product` *int64*<br>Identifies which action-to-action product the advertiser is using<br><br><br>`product_sales_channel` *enum {ONLINE, IN_STORE, OMNI}*<br>ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads<br><br><br>`anchor_event_config` *JSON object*<br>Configuration for anchor event in multi-event optimization campaigns<br><br><br>`multi_event_conversion_info` *JSON object*<br>Configuration for multi-event conversion info in CLO campaigns<br><br><br>`live_video_destination` *string*<br>The live video destination type for live video ads<br><br><br>`smart_pse_enabled` *boolean*<br>Whether Smart Product Set Expansion is enabled for this campaign.<br><br><br>`smart_pse_setting` *enum{ENABLED, DISABLED}*<br>Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues.<br><br><br>`lead_ads_follow_up_event` *enum{whatsapp_conversations}*<br>The selected lead follow-up event for lead ads campaigns.<br><br><br>`omnichannel_object` *Object*<br><br>`app` *array<JSON object>*<br><br>`pixel` *array<JSON object>*<br>**[required]**<br><br><br>`onsite` *array<JSON object>*<br><br>`whats_app_business_phone_number_id` *numeric string or integer*<br><br>`whatsapp_phone_number` *string* |
| `source_campaign_id`<br><br>*numeric string or integer* | Used if a campaign has been copied. The ID from the original campaign that was copied.<br> |
| `special_ad_categories` This field is only accessible in v7.0 or later.<br><br>*array<enum {NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING, FINANCIAL_PRODUCTS_SERVICES}>* | special_ad_categories<br><br>**[required]**<br> |
| `special_ad_category_country` This field is only accessible in v7.0 or later.<br><br>*array<enum {AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}>* | special_ad_category_country<br> |
| `spend_cap`<br><br>*int64* | A spend cap for the campaign, such that it will not spend more than this cap. Defined as integer value of subunit in your currency with a minimum value of $100 USD (or approximate local equivalent). Set the value to 922337203685478 to remove the spend cap. Not available for Reach and Frequency or Premium Self Serve campaigns<br> |
| `start_time`<br><br>*datetime* | start_time<br> |
| `status`<br><br>*enum{ACTIVE, PAUSED, DELETED, ARCHIVED}* | Only `ACTIVE` and `PAUSED` are valid during<br>creation. Other statuses can be used for update. If it is set to<br>`PAUSED`, its active child objects will be paused and have an effective<br>status `CAMPAIGN_PAUSED`.<br> |
| `stop_time`<br><br>*datetime* | stop_time<br> |
| `topline_id`<br><br>*numeric string or integer* | Topline ID<br> |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *id* in the return type.

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

## Updating

### /{campaign_id}
You can update a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) by making a POST request to [/{campaign_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group).

#### Parameters

| Parameter | Description |
| --- | --- |
| `adlabels`<br><br>*list<Object>* | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this campaign<br> |
| `adset_bid_amounts`<br><br>*JSON object {numeric string : int64}* | A map of child adset IDs to their respective bid amounts required in the process of toggling campaign from autobid to manual bid<br> |
| `adset_budgets`<br><br>*array<JSON object>* | An array of maps containing all the non-deleted child adset IDs and either daily_budget or lifetime_budget, required in the process of toggling between campaign budget and adset budget<br><br><br>`adset_id` *numeric string*<br>adset_id<br><br>**[required]**<br><br><br>`daily_budget` *int64*<br>daily_budget<br><br><br>`lifetime_budget` *int64*<br>lifetime_budget<br> |
| `bid_strategy` This field is only accessible in v3.0 or later.<br><br>*enum{LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS}* | Choose bid strategy for this campaign to suit your specific business goals.<br>Each strategy has tradeoffs and may be available for certain `optimization_goal`s:<br><br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as *automatic bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. If you select this, you must provide<br>a bid cap in the `bid_amount` field for each ad set in this ad campaign.<br>Note: during creation this is the default bid strategy if you don't specify.<br>This strategy is also known as *manual maximum-cost bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`COST_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual average cost per optimization event to a specified amount.<br>Get specified cost cap in the `bid_amount` field for each ad set in this ad campaign.<br>Learn more in [Ads Help Center, About bid strategies: Cost Cap](https://www.facebook.com/business/help/272336376749096?id=2196356200683573).<br><br><br>Notes:<br><br><br>• If you do not enable campaign budget optimization, you should set `bid_strategy` at ad set level.<br>• `TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0).<br> |
| `budget_rebalance_flag`<br><br>*boolean* | Whether to automatically rebalance budgets daily for all the adsets under this campaign.<br> |
| `campaign_optimization_type`<br><br>*enum{NONE, ICO_ONLY}* | campaign_optimization_type<br> |
| `daily_budget`<br><br>*int64* | Daily budget of this campaign. All adsets under this<br>campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both.<br> |
| `execution_options`<br><br>*list<enum{validate_only, include_recommendations}>* | **Default value: **`Set`<br>An execution setting<br> `validate_only`: when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. <br>`include_recommendations`: this option cannot be used by itself. When this option is used, recommendations  for ad object's configuration will be included. A separate section [recommendations](https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation) will be included in the response, but only if recommendations for this specification exist.<br>If the call passes validation or review, response will be `{"success": true}`. If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review.<br> |
| `is_adset_budget_sharing_enabled`<br><br>*boolean* | Whether the child ad sets are managed under ad set budget sharing. With ad set budget sharing, advertisers can now share up to 20% of their budget with other ad sets in the same campaign.<br> |
| `is_reels_trending_ads_enabled`<br><br>*boolean* | indicator for 'reels trending ads' campaign<br> |
| `is_skadnetwork_attribution`<br><br>*boolean* | Flag to indicate that the campaign will be using SKAdNetwork, which also means that it will only be targeting iOS 14.x and above<br> |
| `is_using_l3_schedule`<br><br>*boolean* | is_using_l3_schedule<br> |
| `iterative_split_test_configs`<br><br>*list<Object>* | Array of Iterative Split Test Configs created under this campaign .<br> |
| `lifetime_budget`<br><br>*int64* | Lifetime budget of this campaign. All adsets under<br>this campaign will share this budget. You can either set budget at the<br>campaign level or at the adset level, not both.<br> |
| `name`<br><br>*string* | Name for this campaign<br><br>**[supports emoji]**<br> |
| `objective`<br><br>*enum{APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, OUTCOME_APP_PROMOTION, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS}* | Campaign's objective. If it is specified the API will validate that any ads created under the campaign match that objective. <br>Currently, with `BRAND_AWARENESS` objective, all creatives should be either only images or only videos, not mixed.<br><br><br>See the [Outcome Ad-Driven Experience Objective Validation](#odax) section below for more information.<br> |
| `promoted_object`<br><br>*Object* | The object this campaign is promoting across all its ads. Only `product_catalog_id` is used at the ad set level.<br><br><br>`application_id` *int*<br>The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement<br><br><br>`pixel_id` *numeric string or integer*<br>The ID of a Facebook conversion pixel.  Used with offsite conversion campaigns.<br><br><br>`custom_event_type` *enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER}*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`object_store_url` *URL*<br>The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br><br><br>`object_store_urls` *list<URL>*<br>The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br><br><br>`offer_id` *numeric string or integer*<br>The ID of an Offer from a Facebook Page.<br><br><br>`page_id` *Page ID*<br>The ID of a Facebook Page<br><br><br>`product_catalog_id` *numeric string or integer*<br>The ID of a Product Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br><br><br>`product_item_id` *numeric string or integer*<br>The ID of the product item.<br><br><br>`job_listing_id` *numeric string or integer*<br>The ID of the marketplace job listing.<br><br><br>`instagram_profile_id` *numeric string or integer*<br>The ID of the instagram profile id.<br><br><br>`product_set_id` *numeric string or integer*<br>The ID of a Product Set within an Ad Set level Product<br>Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br><br><br>`event_id` *numeric string or integer*<br>The ID of a Facebook Event<br><br><br>`offline_conversion_data_set_id` *numeric string or integer*<br>The ID of the offline dataset.<br><br><br>`fundraiser_campaign_id` *numeric string or integer*<br>The ID of the fundraiser campaign.<br><br><br>`custom_event_str` *string*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`mcme_conversion_id` *numeric string or integer*<br>The ID of a MCME conversion.<br><br><br>`conversion_goal_id` *numeric string or integer*<br>The ID of a Conversion Goal.<br><br><br>`offsite_conversion_event_id` *numeric string or integer*<br>The ID of a Offsite Conversion Event<br><br><br>`boosted_product_set_id` *numeric string or integer*<br>The ID of the Boosted Product Set within an Ad Set level Product<br>Catalog. Should only be present when the advertiser has<br>opted into Product Set Boosting.<br><br><br>`lead_ads_form_event_source_type` *enum{inferred, meta_source, offsite_crm, offsite_web, onsite_crm, onsite_crm_single_event, onsite_clo_dep_aet, onsite_web, onsite_p2b_call, onsite_messaging, qualified_lead_file}*<br>The event source of lead ads form.<br><br><br>`lead_ads_custom_event_type` *enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER}*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`lead_ads_custom_event_str` *string*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`lead_ads_offsite_conversion_type` *enum{default, clo}*<br>The offsite conversion type for lead ads<br><br><br>`value_semantic_type` *enum {VALUE, MARGIN, LIFETIME_VALUE}*<br>The semantic of the event value to be using for optimization<br><br><br>`variation` *enum {OMNI_CHANNEL_SHOP_AUTOMATIC_DATA_COLLECTION, PRODUCT_SET_AND_APP, PRODUCT_SET_AND_IN_STORE, PRODUCT_SET_AND_OMNICHANNEL, PRODUCT_SET_AND_PHONE_CALL, PRODUCT_SET_AND_WEBSITE, PRODUCT_SET_AND_WEBSITE_AND_PHONE_CALL, PRODUCT_SET_WEBSITE_APP_AND_INSTORE}*<br>Variation of the promoted object for a PCA ad<br><br><br>`passback_pixel_id` *numeric string or integer*<br>ID of the pixel used for tracking passback events<br><br><br>`passback_application_id` *numeric string or integer*<br>ID of the application used for tracking passback events<br><br><br>`product_set_optimization` *enum{enabled, disabled}*<br>Enum defining whether or not the ad should be optimized for the promoted product set<br><br><br>`full_funnel_objective` *enum{OFFER_CLAIMS, PAGE_LIKES, EVENT_RESPONSES, POST_ENGAGEMENT, WEBSITE_CONVERSIONS, LINK_CLICKS, VIDEO_VIEWS, LOCAL_AWARENESS, PRODUCT_CATALOG_SALES, LEAD_GENERATION, BRAND_AWARENESS, STORE_VISITS, REACH, APP_INSTALLS, MESSAGES, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION}*<br>Enum defining the full funnel objective of the campaign<br><br><br>`dataset_split_id` *numeric string or integer*<br>ID of the dataset split used to perform additional optimization on the dataset<br><br><br>`dataset_split_ids` *array<numeric string>*<br>IDs of the dataset splits used to perform additional optimization on the dataset<br><br><br>`lead_ads_selected_pixel_id` *numeric string or integer*<br>The selected pixel id for lead ads conversion leads optimization<br><br><br>`custom_attribution_source_ids` *array<numeric string>*<br>IDs of the custom attribution sources used for tracking passback events<br><br><br>`multi_event_product` *int64*<br>Identifies which action-to-action product the advertiser is using<br><br><br>`product_sales_channel` *enum {ONLINE, IN_STORE, OMNI}*<br>ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads<br><br><br>`anchor_event_config` *JSON object*<br>Configuration for anchor event in multi-event optimization campaigns<br><br><br>`multi_event_conversion_info` *JSON object*<br>Configuration for multi-event conversion info in CLO campaigns<br><br><br>`live_video_destination` *string*<br>The live video destination type for live video ads<br><br><br>`smart_pse_enabled` *boolean*<br>Whether Smart Product Set Expansion is enabled for this campaign.<br><br><br>`smart_pse_setting` *enum{ENABLED, DISABLED}*<br>Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues.<br><br><br>`lead_ads_follow_up_event` *enum{whatsapp_conversations}*<br>The selected lead follow-up event for lead ads campaigns.<br><br><br>`omnichannel_object` *Object*<br><br>`app` *array<JSON object>*<br><br>`pixel` *array<JSON object>*<br>**[required]**<br><br><br>`onsite` *array<JSON object>*<br><br>`whats_app_business_phone_number_id` *numeric string or integer*<br><br>`whatsapp_phone_number` *string* |
| `smart_promotion_type`<br><br>*enum{GUIDED_CREATION, SMART_APP_PROMOTION}* | smart_promotion_type<br> |
| `special_ad_category`<br><br>*enum{NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING, FINANCIAL_PRODUCTS_SERVICES}* | special_ad_category<br> |
| `special_ad_category_country` This field is only accessible in v7.0 or later.<br><br>*array<enum {AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}>* | special_ad_category_country<br> |
| `spend_cap`<br><br>*int64* | A spend cap for the campaign, such that it will not spend more than this cap. Defined as integer value of subunit in your currency with a minimum value of $100 USD (or approximate local equivalent). Set the value to 922337203685478 to remove the spend cap. Not available for Reach and Frequency or Premium Self Serve campaigns<br> |
| `start_time`<br><br>*datetime* | start_time<br> |
| `status`<br><br>*enum{ACTIVE, PAUSED, DELETED, ARCHIVED}* | Only `ACTIVE` and `PAUSED` are valid during<br>creation. Other statuses can be used for update. If it is set to<br>`PAUSED`, its active child objects will be paused and have an effective<br>status `CAMPAIGN_PAUSED`.<br> |
| `stop_time`<br><br>*datetime* | stop_time<br> |

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

## Deleting

### /{campaign_id}
You can delete a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) by making a DELETE request to [/{campaign_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group).

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

### /act_{ad_account_id}/campaigns
You can dissociate a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) from an [AdAccount](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account) by making a DELETE request to [/act_{ad_account_id}/campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns).

#### Parameters

| Parameter | Description |
| --- | --- |
| `before_date`<br><br>*datetime* | Set a before date to delete campaigns before this date<br> |
| `delete_strategy`<br><br>*enum{DELETE_ANY, DELETE_OLDEST, DELETE_ARCHIVED_BEFORE}* | Delete strategy<br><br>**[required]**<br> |
| `object_count`<br><br>*integer* | Object count<br> |

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

## Objective Validation

**Warning:** These older objectives are deprecated with the release of [Marketing API v17.0](https://developers.facebook.com/docs/graph-api/changelog/version17.0#marketing-api). Please refer to the [Outcome-Driven Ads Experiences mapping table](#odax-mapping) below to find the new objectives and their corresponding destination types, optimization goals and promoted objects.

Your campaign objective choice can limit the settings available to you.

### Optimization Goals

Certain campaign objectives support only certain ad set `optimization_goals`. See [Bidding Overview, Validation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/overview#opt-goal-validation).

### Compatible Ad Types

| Objective | Compatible Ad Types |
| --- | --- |
| `APP_INSTALLS` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>- [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `BRAND_AWARENESS` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `CONVERSIONS` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>- [App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Ads that click to Messenger](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads#destination)<br>- [Offer Ads](https://developers.facebook.com/docs/marketing-api/guides/offer-ads)<br>- [Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>- [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `EVENT_RESPONSES` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Event and Local Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/event-ads) |
| `LEAD_GENERATION` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Lead Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `LINK_CLICKS` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>- [App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Offer Ads](https://developers.facebook.com/docs/marketing-api/guides/offer-ads)<br>- [Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>- [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `MESSAGES` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Messenger Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads#destination) |
| `POST_ENGAGEMENT` | - Image Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign)) |
| `PRODUCT_CATALOG_SALES` | - Image Ads<br>- Carousel Ads<br>- [Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ads)<br>- [Collaborative Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/collaborative-ads) |
| `REACH` | - Image Ads<br>- Video Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |
| `STORE_VISITS` | - Image Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Collection Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Offer Ads](https://developers.facebook.com/docs/marketing-api/guides/offer-ads) |
| `VIDEO_VIEWS` | - Video Ads<br>- Carousel Ads<br>- [Instant Experience Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instant-experiences)<br>- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads) (see [placement limitations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#campaign))<br>- [Segment Asset Customization Ads](https://developers.facebook.com/docs/marketing-api/dynamic-creative/segment-asset-customization)<br>- [Placement Asset Customization Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization)<br>- [Multi-Language Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/multi-language-ads)<br>- [Dynamic Creative](https://developers.facebook.com/docs/marketing-api/dynamic-creative/overview) |

### Objectives and Creative Fields {#objective_creative}

See our [ads guide](https://www.facebook.com/business/ads-guide/) for a list of creatives supported per objective. In the API, the objective determines which [ad creatives](https://developers.facebook.com/docs/reference/ads-api/adcreative) are valid.

| Objective | Creative Fields |
| --- | --- |
| `APP_INSTALLS` | `object_story_id` or `object_story_spec` |
| `CONVERSIONS` | `object_story_id` or `object_story_spec`<br><br>Notes:<br><br>- If you are creating link ads not connected to a page, use the following creative fields: `title`, `body`, `object_url`, and `image_file` or `image_hash`.<br>- Creative cannot include link ads pointing to an app store. |
| `EVENT_RESPONSES` | `object_story_id` or `object_story_spec` |
| `LEAD_GENERATION` | `object_story_id` or `object_story_spec` |
| `LINK_CLICKS` | `object_story_id` or `object_story_spec`<br><br>Notes:<br><br>- Creative cannot include link ads pointing to an app store.<br>- If you select `LINK_CLICKS` as both optimization goal and billing event, you must include `call_to_action`. |
| `MESSAGES` | `object_story_spec` |
| `PAGE_LIKES` | `object_story_id`, `object_story_spec`, `object_id`, and `body` |
| `POST_ENGAGEMENT` | `object_story_id` or `object_story_spec`<br><br>Note: Creative cannot include link ads pointing to an app store. |
| `VIDEO_VIEWS` | `object_story_id` or `object_story_spec` |

### Objectives and Tracking Specs {#objective_tracking}

Tracking specs are applied by default based on the objective specified, please see the full list of defaults by objective [here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/tracking-specs#default).

There are two important scenarios to take into account:

* Tracking pixels are not applied by default, and you must specify it explicitly when your objective is `CONVERSIONS`.
* Mobile app ads will no longer track installs or app events by default. **You must explicitly specify to track installs or app events for mobile app ads otherwise your ad will not track.**

To specify to track an install or app event, set the following in your [ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup):

```
tracking_specs=[{'action.type':['mobile_app_install'],'application':[{your_app_id}]},{'action.type':['app_custom_event'],'application':[{your_app_id}]}]
```

### Objective and Promoted Objects {#promoted-object}

Certain objectives require the `promoted_object` to be set in ad sets. See [Promoted Object](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object) for more information.

| Objective | Required promoted_object Fields |
| --- | --- |
| `APP_INSTALLS` | - `application_id` and `object_store_url`<br>- If `optimization_goal` is `OFFSITE_CONVERSIONS`: `application_id`, `object_store_url`, and `custom_event_type` |
| `CONVERSIONS` | - `pixel_id` (Conversion pixel ID)<br>- `pixel_id` (Facebook pixel ID) and `custom_event_type`<br>- `pixel_id` (Facebook pixel ID), `pixel_rule`, and `custom_event_type`<br>- `event_id` (Facebook event ID) and `custom_event_type`<br>- For mobile app events: `application_id`, `object_store_url`, and `custom_event_type`<br>- For offline conversions: `offline_conversion_data_set_id` (Offline dataset ID), and `custom_event_type` |
| `LINK_CLICKS` | For mobile app or Instant Experiences app engagement link clicks: `application_id` and `object_store_url`. |
| `PRODUCT_CATALOG_SALES` | - `product_set_id`, or<br>- `product_set_id` and `custom_event_type` |
| `PAGE_LIKES` | `page_id` |
| `OFFER_CLAIMS` | `page_id` |

### Objective and Placements {#placement}

Certain types of ad [placements](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#placement) are valid only for specific objectives or creatives. See [Business Help Center, Available ad placements for marketing objectives](https://www.facebook.com/business/help/279271845888065?id=369787570424415).

The table below shows some placements and their compatible objectives or creatives. You can pick a combination of those compatible placements. Note that:

* With `LEAD_GENERATION`, `device_platforms: desktop` cannot be selected together with `publisher_platforms: instagram`.
* If your objective is website traffic, `story` for `facebook_positions` does not support `destination_type: messenger`.
* If your objective is website traffic, `story` for `messenger_positions` does not support `destination_type: messenger`.
* If your objective is website traffic, `ig_search` and `explore_home` for `instagram_positions` do not support `destination_type: whatsapp & messenger`.

| Objective | Creative | Placement |
| --- | --- | --- |
| `APP_INSTALLS`, promoting an Instant Experiences app | Desktop app ads | `device_platforms`: `desktop` |
| `APP_INSTALLS`, promoting a mobile app | Photo or video mobile app ads | `device_platforms`: `mobile`<br><br>`publisher_platforms`: `facebook`, `feed`, `instagram`, `audience_network`<br> `facebook_positions`: `feed`, `video_feeds`, `instant articles` and `story`<br><br>`audience_network_positions`: `classic`, `rewarded_video`<br><br>`messenger_positions`: `story` |
| `BRAND_AWARENESS` | all | `publisher_platforms`: `facebook`, `instagram`, `audience_network`.<br><br>`facebook_positions`: `feed`, `video_feeds`, `instream_video` and `story`, which is currently under limited availability<br><br>`instagram_positions`: `stream`<br><br>`audience_network_positions`: `classic`, `instream_video` |
| `CONVERSIONS` | Photo or video link ads from a page | We support `BRAND_AWARENESS`, `APP_INSTALL`, `POST_ENGAGEMENT`, `VIDEO_VIEWS`, `REACH`, `WEBSITE_CONVERSIONS`, and `TRAFFIC`.<br>Also supported: `right_hand_column` and `story` for `facebook_positions` and `messenger_positions`: `messenger_home` and `story`.<br><br>`facebook_positions`: `story` only supports the objective `WEBSITE_CONVERSIONS`<br><br>`messenger_positions`: `story` only supports the objective `WEBSITE_CONVERSIONS`<br><br>Exception: `instream_video` is not supported for this objective. |
| `CONVERSIONS` | Link ads not connected to a page | `facebook_positions`: `right_hand_column` |
| `CONVERSIONS` (promoting mobile app) | Photo or video mobile app ads | `device_platforms`: `mobile`.<br><br>`facebook_positions`: `right_hand_column` and `story`. `story` as a `facebook_positions` for this objective does not support `destination_type`: `messenger`.<br><br>`messenger_positions`: `messenger_home`<br><br>`story` as a `messenger_positions` for this objective does not support `destination_type: messenger`. |
| `EVENT_RESPONSES` | Event ads | As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `EVENT_RESPONSES` | Page post ads | `publisher_platforms`: `facebook`. <br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `LEAD_GENERATION` | Page post ads | `device_platforms`: `mobile`, `desktop`<br><br>`publisher_platforms`: `facebook`, `instagram`<br><br>`facebook_positions`: `feed` and `story`, which is in limited availability<br><br>instagram_positions: stream<br><br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `LINK_CLICKS` | Photo or video link ads from a page | All, including `right_hand_column` and `messenger_positions`: `messenger_home` and `story`. |
| `LINK_CLICKS` | Link ads not connected to a page | `facebook_positions`: `right_hand_column` |
| `LINK_CLICKS`, promoting an Instant Experiences app | Desktop app ads | `device_platforms`: `desktop`<br><br>`facebook_positions`: `right_hand_column` |
| `LINK_CLICKS`, promoting a mobile app | Photo or video mobile app ads | `device_platforms`: `mobile`, `facebook_positions`: `right_hand_column` |
| `PAGE_LIKES` | Video creatives | `publisher_platforms`: `facebook`<br><br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `POST_ENGAGEMENT` | Page post ads with video or photo | `publisher_platforms`: `facebook`, `instagram`<br><br>`device_platforms`: `mobile`, `desktop`<br><br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `POST_ENGAGEMENT` | Page post ads with text only | `publisher_platforms`: `facebook`, `instagram`<br><br>`device_platforms`: `mobile`, `desktop`<br><br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `POST_ENGAGEMENT` | New campaign | `publisher_platforms`: `facebook`, `instagram`<br><br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `PRODUCT_CATALOG_SALES` | dynamic ads | All, including `right_hand_column` for `facebook_positions`. |
| `REACH` | Reach ads | All except `right_hand_column` for `facebook_positions` as of 3.0. <br>Includes `messenger_positions`: `story` and `story` for `facebook_positions`. |
| `STORE_VISITS` | store visit ads | `publisher_platforms`: `facebook`<br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |
| `VIDEO_VIEWS` | Video ads | `publisher_platforms`: `facebook`, `instagram`, `audience_network`.<br><br>Includes `story` for `facebook_positions` but not with the `optimation_goal` set to `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS`.<br><br>As of 3.0, you cannot use `right_hand_column` for `facebook_positions` |

### Objective, Optimization Goal and `attribution_spec` {#attribution_spec}
Use click-through and view-through attribution windows for [ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign#Creating) to track conversions then use for ads delivery optimization. This is different from the attribution window you use for ads reporting. With `attribution_spec`, select a combination of click-through or view-through windows of 1 day or 7 days. The combinations you can use depend on your ad set's `optimization_goal` and campaign's `objective`.

**Recommended Default `attribution_spec`**

You may not have provided `attribution_spec` when you created ads sets optimized for Value Optimization. This is an optimization available for conversions, app installs, and product catalog sales objectives. In the past, we defaulted to a 1-day click through attribution window.

| Objective | Optimization Goal | Allowed Combination |
| --- | --- | --- |
| `CONVERSIONS, PRODUCT_CATALOG_SALES` | `OFFSITE_CONVERSIONS` | 1-day click<br>7-day click<br>1-day click and 1-day view<br>7-day click and 1-day view |
| `APP_INSTALLS, LINK_CLICKS` | `OFFSITE_CONVERSIONS` | 1-day click<br><br>7-day click |
| `APP_INSTALLS` | `APP_INSTALLS` | 1-day click<br>1-day click and 1-day engaged-view<br>1-day click and 1-day view<br>1-day click and 1-day engaged-view and 1-day view |
| `CONVERSIONS` | `INCREMENTAL_OFFSITE_<br>CONVERSIONS` | Null click, Null view |

For all other `optimization_goal` and `objective` combinations, you can only use 1-day click for `attribution_spec`.

### Outcome-Driven Ads Experiences Objective Validation {#odax}

**Warning:** From v20.0 onwards, Impressions optimization goal is deprecated for the legacy Post Engagement objective and the `ON_POST` destination_type.

#### Objective values

The following are newer objectives:

* `OUTCOME_APP_PROMOTION`
* `OUTCOME_AWARENESS`
* `OUTCOME_ENGAGEMENT`
* `OUTCOME_LEADS`
* `OUTCOME_SALES`
* `OUTCOME_TRAFFIC`

These newer objectives will eventually replace the original objectives `APP_INSTALLS`, `BRAND_AWARENESS`, `CONVERSIONS`, `EVENT_RESPONSES`, `LEAD_GENERATION`, `LINK_CLICKS`, `LOCAL_AWARENESS`, `MESSAGES`, `OFFER_CLAIMS`, `PAGE_LIKES`, `POST_ENGAGEMENT`, `PRODUCT_CATALOG_SALES`, `REACH`, `STORE_VISITS`, `VIDEO_VIEWS`. We will continue supporting these original objectives throughout 2022.

#### Limitations

* Trying to duplicate existing objective campaigns to use the new objective values (`OUTCOME_APP_PROMOTION`, `OUTCOME_AWARENESS`, `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS`, `OUTCOME_SALES`, `OUTCOME_TRAFFIC`) may throw an error.

#### Example

**Outcome-Driven Ads Experiences**

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

#### Objective Mapping {#odax-mapping}

| Old Objective | New Objective | Destination Type | Optimization Goal | Promoted Object |
| --- | --- | --- | --- | --- |
| `BRAND_AWARENESS` | `OUTCOME_AWARENESS` | — | `AD_RECALL_LIFT` | `page_id` |
| `REACH` | `OUTCOME_AWARENESS` | — | `REACH` | `page_id` |
| `REACH` | `OUTCOME_AWARENESS` | — | `IMPRESSIONS` | `page_id` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | — | `LINK_CLICKS` | `application_id`, `object_store_url` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | — | `LANDING_PAGE_VIEWS` | — |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | — | `REACH` | `application_id`, `object_store_url` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | — | `IMPRESSIONS` | — |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `MESSENGER` | `LINK_CLICKS` | — |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `MESSENGER` | `REACH` | — |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `MESSENGER` | `IMPRESSIONS` | — |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `WHATSAPP` | `LINK_CLICKS` | `page_id` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `WHATSAPP` | `REACH` | `page_id` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `WHATSAPP` | `IMPRESSIONS` | `page_id` |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `PHONE_CALL` | `QUALITY_CALL` | — |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | `PHONE_CALL` | `LINK_CLICKS` | — |
| `POST_ENGAGEMENT` | `OUTCOME_ENGAGEMENT` | `ON_POST` | `POST_ENGAGEMENT` | — |
| `POST_ENGAGEMENT` | `OUTCOME_ENGAGEMENT` | `ON_POST` | `REACH` | — |
| `POST_ENGAGEMENT` | `OUTCOME_ENGAGEMENT` | `ON_POST` | `IMPRESSIONS` | — |
| `PAGE_LIKES` | `OUTCOME_ENGAGEMENT` | `ON_PAGE` | `PAGE_LIKES` | `page_id` |
| `EVENT_RESPONSES` | `OUTCOME_ENGAGEMENT` | `ON_EVENT` | `EVENT_RESPONSES` | — |
| `EVENT_RESPONSES` | `OUTCOME_ENGAGEMENT` | `ON_EVENT` | `POST_ENGAGEMENT` | — |
| `EVENT_RESPONSES` | `OUTCOME_ENGAGEMENT` | `ON_EVENT` | `REACH` | — |
| `EVENT_RESPONSES` | `OUTCOME_ENGAGEMENT` | `ON_EVENT` | `IMPRESSIONS` | — |
| `APP_INSTALL` | `OUTCOME_APP_PROMOTION` | — | `LINK_CLICKS` | `application_id`, `object_store_url` |
| `APP_INSTALL` | `OUTCOME_APP_PROMOTION` | — | `OFFSITE_CONVERSIONS` | `application_id`, `object_store_url` |
| `APP_INSTALL` | `OUTCOME_APP_PROMOTION` | — | `APP_INSTALLS` | `application_id`, `object_store_url` |
| `VIDEO_VIEWS` | `OUTCOME_AWARENESS` | — | `THRUPLAY` | `page_id` |
| `VIDEO_VIEWS` | `OUTCOME_AWARENESS` | — | `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS` | `page_id` |
| `VIDEO_VIEWS` | `OUTCOME_ENGAGEMENT` | `ON_VIDEO` | `THRUPLAY` | — |
| `VIDEO_VIEWS` | `OUTCOME_ENGAGEMENT` | `ON_VIDEO` | `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS` | — |
| `LEAD_GENERATION` | `OUTCOME_LEADS` | `ON_AD` | `LEAD_GENERATION` | `page_id` |
| `LEAD_GENERATION` | `OUTCOME_LEADS` | `ON_AD` | `QUALITY_LEAD` | `page_id` |
| `LEAD_GENERATION` | `OUTCOME_LEADS` | `LEAD_FROM_MESSENGER` | `LEAD_GENERATION` | `page_id` |
| `LEAD_GENERATION` | `OUTCOME_LEADS` | `LEAD_FROM_IG_DIRECT` | `LEAD_GENERATION` | `page_id` |
| `LEAD_GENERATION` | `OUTCOME_LEADS` | `PHONE_CALL` | `QUALITY_CALL` | `page_id` |
| `MESSAGES` | `OUTCOME_ENGAGEMENT` | `MESSENGER` | `CONVERSATIONS` | `page_id` |
| `MESSAGES` | `OUTCOME_ENGAGEMENT` | `MESSENGER` | `LINK_CLICKS` | `page_id` |
| `MESSAGES` | `OUTCOME_ENGAGEMENT` | `MESSENGER` | `LEAD_GENERATION` | `page_id` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `OFFSITE_CONVERSIONS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `OFFSITE_CONVERSIONS` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `LINK_CLICKS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `LINK_CLICKS` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `REACH` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `REACH` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `LANDING_PAGE_VIEWS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_ENGAGEMENT` | — | `IMPRESSIONS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `OFFSITE_CONVERSIONS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `OFFSITE_CONVERSIONS` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `LINK_CLICKS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `LINK_CLICKS` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `REACH` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `REACH` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `LANDING_PAGE_VIEWS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_LEADS` | — | `IMPRESSIONS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_SALES` | — | `OFFSITE_CONVERSIONS` | `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_SALES` | — | `OFFSITE_CONVERSIONS` | `application_id`, `object_store_url` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_SALES` | `MESSENGER` | `CONVERSATIONS` | `page_id`, `pixel_id`, `custom_event_type` |
| `CONVERSIONS`<br><br>(See [Available conversion locations and events by objective in Meta Ads Manager](https://www.facebook.com/business/help/2035196646663270) for more information on available conversion events by objective.) | `OUTCOME_SALES` | `PHONE_CALL` | `QUALITY_CALL` | `page_id` |
| `PRODUCT_CATALOG_SALES` | `OUTCOME_SALES` | `WEBSITE` | `LINK_CLICKS` | Campaign: `product_catalog_id`<br><br>Ad set: `product_set_id`, `custom_event_type` |
| `STORE_VISITS` | `OUTCOME_AWARENESS` | — | `REACH` | `place_page_set_id` |
