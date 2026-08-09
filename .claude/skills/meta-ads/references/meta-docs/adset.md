<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign.md | Scrape: 2026-08-09 | API v26.0 -->

# Ad Set



**Warning:** Beginning September 2, 2025, we will start to roll out more proactive restrictions on custom audiences and custom conversions that may suggest information not permitted under [our terms](https://www.facebook.com/legal/terms/businesstools?_rdr). For example, any custom audience or custom conversions suggesting specific health conditions (e.g., "arthritis", "diabetes") or financial status (e.g., "credit score", "high income") will be flagged and prevented from being used to run ad campaigns.

**What these restrictions mean for your campaigns:**

* You won’t be able to use flagged custom audiences or custom conversions when creating new campaigns.
* If you have an active campaign using flagged custom audiences or custom conversions, you should promptly review and resolve the issues by following the resolution steps to avoid delivery and performance issues.

**For API developers:**

* Starting September 2, 2025, if an ad set contains one or more flagged custom audiences and custom conversions, the [`issues_info` list](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign#Reading) will be populated with one issue per flagged items.
* Creation and editing of ad sets that contain flagged custom audiences and custom conversions will not be blocked, but campaign delivery and performance may be impacted unless the flags are resolved.

More information on this update and how to resolve flagged custom audiences can be found [here](https://www.facebook.com/business/help/1055828013359808), while information for resolving flagged custom conversions is available [here](https://www.facebook.com/business/help/2455915321411996).

An ad set is a group of ads that share the same daily or lifetime budget, schedule, bid type, bid info, and targeting data. Ad sets enable you to group ads according to your criteria, and you can retrieve the ad-related statistics that apply to a set. See [Optimized CPM](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/cost-per-action-ads) and [Promoted Object](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object).

For example, create an ad set with a daily budget:

```html
curl -X POST \
  -F 'name="My Reach Ad Set"' \
  -F 'optimization_goal="REACH"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'targeting={
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "facebook_positions": [
         "feed"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'promoted_object={
       "page_id": "<PAGE_ID>"
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

Create an ad set with a lifetime budget

```html
curl -X POST \
  -F 'name="My First Adset"' \
  -F 'lifetime_budget=20000' \
  -F 'start_time="2025-12-04T20:32:30-0800"' \
  -F 'end_time="2025-12-14T20:32:30-0800"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'bid_amount=100' \
  -F 'billing_event="LINK_CLICKS"' \
  -F 'optimization_goal="LINK_CLICKS"' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

### Limits {#limits}

The following are the limits on ad sets

| Limit | Value |
| --- | --- |
| Maximum number of ad sets per regular ad account | 5000 non-deleted ad sets |
| Maximum number of ad sets per bulk ad account | 10000 non-deleted ad sets |
| Maximum number of ads per ad set | 50 non-archived ads |

### Housing, Employment and Credit Ads

Facebook is committed to protecting people from discrimination, and we are continually improving our ability to detect and deter potential abuse. It’s already against [our policies](https://www.facebook.com/policies/ads/prohibited_content/discriminatory_practices) to discriminate by wrongfully targeting or excluding specific groups of people. As part of a [historic settlement agreement](https://newsroom.fb.com/news/2019/03/protecting-against-discrimination-in-ads/), we are making changes to the way we manage housing, employment and credit ads.

Advertisers must specify a `special_ad_category` for ad campaigns that market housing, employment, and credit. In doing so, the set of targeting options available for ads in these campaigns will be restricted. See [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) for more information.

### Flagged custom conversions, custom audiences and/or lookalike audiences

If an ad set contains one or more custom lookalike audiences flagged with an `operation_status` of `471`, the `issues_info` list will be populated with one issue per flagged audience as warning.

**Example**

```html
{
  "effective_status": "ACTIVE",
  "issues_info": [
    {
      "level": "AD_SET",
      "error_code": 2460003,
      "error_summary": "Custom Audience is blocked",
      "error_message": "Custom Audience is blocked: Some of this ad set’s custom audiences and/or lookalikes are blocked because they suggest the use of information (e.g., health, financial) not allowed under Meta’s terms. Go to Audience Manager for more details, and you can either review each custom audience or lookalike and remove prohibited information, or choose a different one for your ad set or create a new one and make sure it does not include potentially prohibited information. You can also request a review in Audience Manager if you think any don’t use restricted information.",
      "error_type": "SOFT_ERROR",
      "additional_info": "Custom Audience ID: 120231141155310247"
    },
    {
      "level": "AD_SET",
      "error_code": 2460003,
      "error_summary": "Custom Audience is blocked",
      "error_message": "Custom Audience is blocked: Some of this ad set’s custom audiences and/or lookalikes are blocked because they suggest the use of information (e.g., health, financial) not allowed under Meta’s terms. Go to Audience Manager for more details, and you can either review each custom audience or lookalike and remove prohibited information, or choose a different one for your ad set or create a new one and make sure it does not include potentially prohibited information. You can also request a review in Audience Manager if you think any don’t use restricted information.",
      "error_type": "SOFT_ERROR",
      "additional_info": "Custom Audience ID: 120232742978230247"
    },
    {
      "level": "AD_SET",
      "error_code": 2460004,
      "error_summary": "Custom Conversion is blocked",
      "error_message": "Custom Conversion is blocked: This ad set’s custom conversion is blocked because it suggests the use of information (e.g., health, financial) not allowed under Meta’s terms. You can’t edit this custom conversion, but you can choose a different one for this ad set or create a new one that doesn’t use prohibited information. You can also request a review if you think your custom conversion doesn’t use prohibited information.",
      "error_type": "SOFT_ERROR",
      "additional_info": "Custom Conversion ID: 730362226205831"
    }
  ],
  "id": "120228591637010247"
}
```

In addition, attempting to create or modify ad sets containing any flagged custom audience, lookalike audience or custom conversion will fail with an error. The error will contain the list of IDs for the restricted assets.

##### For flagged custom audiences

```json
{
  "error": {
    "error_subcode": 246003,
    "error_data": {
      "Restricted Custom Audience IDs": [
        "<CUSTOM_AUDIENCE_ID1>",
        "<CUSTOM_AUDIENCE_ID2>"
      ]
    }
    "error_user_title": "Your custom audience is currently blocked",
    "error_user_msg": "  This custom audience is blocked because it may contain information (e.g., health, financial) not allowed under Meta’s terms. Visit the audience manager to appeal this decision, edit your audience and remove prohibited information, or choose a different audience."
  },
}
```

##### For flagged custom conversions

```json
{
  "error": {
    "error_subcode": 246004,
    "error_data": {
      "Restricted Custom Conversion ID": "<CUSTOM_CONVERSION_ID>"
    }
    "error_user_title": "Your custom conversion is currently blocked",
    "error_user_msg": "This custom conversion is blocked because it may contain information (e.g., health, financial) not allowed under Meta’s terms. Visit the events manager to appeal this decision, edit your custom conversion and remove prohibited information, or choose a different custom conversion."
  },
}
```

#### To resolve flagged audiences

If your custom or lookalike audiences are flagged, consider these options.

To resolve flagged custom audiences:

* **Review flagged audiences**: Use Audience Manager to review your custom audience along with other information included in an audience, and remove any information that is not allowed under edit the audience to comply with [Meta's terms](https://www.facebook.com/legal/terms/businesstools/).
* **Create new or choose different audiences**: Alternatively, you can create a new custom audience or choose a different existing custom audience and make sure that it does not include information not allowed under our terms and use that to run campaigns.

To resolve flagged lookalike audiences:

* **Resolve issues with the underlying custom audience**: If the underlying custom audience (also known as the seed audience) of your lookalike audience is flagged, you will need to resolve the issue with the underlying custom audience on which the lookalike audience is built. Please refer to the preceding section on how to resolve flagged custom audiences.
* **Create new audiences**: Consider developing new lookalike audiences and make sure that they don't include information that is not allowed under our terms.

##### Request a review

If you believe your custom audience or lookalike audience has been flagged in error and doesn't include non-permitted information, you can request a review via Ads Manager under the campaigns table or, or in Audience Manager by clicking on individual audiences and under the summary tab of the impacted audience.

#### To resolve flagged custom conversions

If any of your custom conversions are flagged for suggesting information that is not allowed under our terms, you may want to consider the following options.

To resolve a flagged custom conversion in a new campaign creation:

* **Create new custom conversion**: Use a new custom conversion and make sure that it does not include information that is not allowed under our terms.
* **Choose a different custom conversion**: Select a different existing custom conversion and make sure it does not include information that is not allowed under our terms.

To resolve a flagged custom conversion in an existing campaign:

* **Duplicate your campaign and select an existing custom conversion**: If you have a running campaign that is flagged due to a flagged custom conversion, consider duplicating the campaign and selecting a different custom conversion that is not flagged before publishing the new duplicated campaign. **Note:** Once the campaign is published, you cannot remove or select a different custom conversion.

##### Request a review

If you believe your custom conversion has been flagged in error and doesn't include non-permitted information, you can request a review via Ads Manager under the campaigns table, or in Events Manager under the custom conversions page.

### Targeting European Union Ads

Beginning Tuesday, May 16, 2023 advertisers who include the European Union (EU), associated territories, or select global/worldwide in their ad targeting on Facebook and Instagram will be asked to include information about who benefits from the ad (the beneficiary) and who is paying for the ad (the payor) for each ad set. Advertisers will be prompted for this information in all ads buying surfaces including Ads Manager and the Marketing API. Beginning Wednesday, August 16, 2023, if beneficiary and payer information is not provided, the ad will not be published.

We are launching this requirement to respond to the EU Digital Services Act (DSA) which goes into full effect for Facebook and Instagram later this year.

Ad sets targeted to the EU and/or associated territories (see [here](https://www.facebook.com/business/help/605021638170961/) for a complete list) are required to provide beneficiary information (who benefits from the ad running), and payer information (who pays for the ad). This applies to new ads, duplicated ads, or significantly edited ads from May 16 forward, and without the required information, the API will respond with a wrong parameter error. For convenience the advertiser can set a saved beneficiary and payor in their ad account, which will be auto-populated during ad set creation, copying, and updating targets to include EU locations and ads under existing ad seta without configured the payor and beneficiary.. For more information about the ad account level parameters, `default_dsa_payor` and `default_dsa_beneficiary`, see to the check the [Ad Account reference document](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account).

To facilitate the creation of ad sets targeting the EU, we're offering a new API which allows developers to get a list of likely beneficiary/payer strings, based on ad account activity. See [Ad Account DSA Recommendations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/dsa_recommendations) for more information.

**Notice:**

* When the default values are set in the ad account, during ad set creation, updating, and ad creation under an existing ad set, if one of them is not provided, the API will automatically fill the default value listed in the ad account. **Do not pass only one of them and expect the API to set the other one to be the same value.** For example, in the ad account settings, `default_dsa_payor` is `payor_default` and `default_dsa_beneficiary` is `beneficiary_default`. During ad set creation, if only `dsa_payor` is passed with the payor, the `dsa_beneficiary` will be automatically filled with value of `beneficiary_default` instead of `dsa_payor`.
* If no saved default values are set or the values are unset, without explicitly passing the payor or beneficiary during ad set creation or when making updates, it will trigger an error and the request will fail.
* The `payer` and the `beneficiary` fields are only for ad sets targeting the EU and/or associated territories.
* For ad sets targeting regions other than the EU and/or associated territories, that information will not be saved even if it is provided.

To facilitate the creation of ad sets targeting the EU, we're offering a new API which allows developers to get a list of likely beneficiary/payer strings, based on ad account activity. See [Ad Account Dsa Recommendations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/dsa_recommendations) for more information.

## Reading

An ad set is a group of ads that share the same daily or lifetime budget, schedule, bid type, bid info, and targeting data. Ad sets enable you to group ads according to your criteria, and you can retrieve the ad-related statistics that apply to a set.

**Warning:** The `date_preset = lifetime` parameter is disabled in Graph API v10.0 and replaced with `date_preset = maximum`, which returns a maximum of 37 months of data. For v9.0 and below, `date_preset = maximum` will be enabled on May 25, 2021, and any `lifetime` calls will default to `maximum` and return only 37 months of data.

### Examples {#read-examples}

```html
curl -X GET \
  -d 'fields="name,status"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

To retrieve date-time related fields in a UNIX timestamp format, use the `date_format` parameter:

```html
curl -X GET \
  -d 'fields="id,name,start_time,end_time"' \
  -d 'date_format="U"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

#### Example

### HTTP
```
GET /v25.0/<AD_SET_ID>/?fields=adset_schedule HTTP/1.1
Host: graph.facebook.com
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/<AD_SET_ID>/?fields=adset_schedule',
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
    "/<AD_SET_ID>/",
    {
        "fields": "adset_schedule"
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
params.putString("fields", "adset_schedule");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/<AD_SET_ID>/",
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
  @"fields": @"adset_schedule",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/<AD_SET_ID>/"
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
  -d 'fields="adset_schedule"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%3CAD_SET_ID%3E%2F%3Ffields%3Dadset_schedule&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br><br>*enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year}* | Date Preset<br> |
| `time_range`<br><br>*{'since':YYYY-MM-DD,'until':YYYY-MM-DD}* | Time Range. Note if time range is invalid, it will be ignored.<br><br><br>`since` *datetime*<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br><br><br>`until` *datetime*<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br> |

#### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>*numeric string* | ID for the Ad Set<br><br><br>**[default]**<br> |
| `account_id`<br><br>*numeric string* | ID for the Ad Account associated with this Ad Set<br> |
| `adlabels`<br><br>*[list<AdLabel>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label)* | Ad Labels associated with this ad set<br> |
| `adset_schedule`<br><br>*list<DayPart>* | Ad set schedule, representing a delivery schedule for a single day<br> |
| `asset_feed_id`<br><br>*numeric string* | The ID of the asset feed that constains a content to create ads<br> |
| `attribution_spec`<br><br>*list<AttributionSpec>* | Conversion attribution spec used for attributing conversions for optimization. Supported window lengths differ by optimization goal and campaign objective. See [Objective, Optimization Goal and `attribution_spec`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#attribution_spec).<br> |
| `bid_adjustments`<br><br>*[AdBidAdjustments](https://developers.facebook.com/docs/marketing-api/reference/ad-bid-adjustments)* | Map of bid adjustment types to values<br> |
| `bid_amount`<br><br>*unsigned int32* | Bid cap or target cost for this ad set. The bid cap used in a *lowest cost bid strategy* is defined as the maximum bid you want to pay for a result based on your `optimization_goal`. The target cost used in a *target cost bid strategy* lets Facebook bid on your behalf to meet your target on average and keep costs stable as you raise budget.<br><br><br>The bid amount's unit is cents for currencies like USD, EUR, and the basic unit for currencies like JPY, KRW. The bid amount for ads with `IMPRESSION` or `REACH` as `billing_event` is per 1,000 occurrences of that event, and the bid amount for ads with other `billing_event`s is for each occurrence.<br> |
| `bid_constraints`<br><br>*[AdCampaignBidConstraint](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-bid-constraint)* | Choose bid constraints for ad set to suit your specific business goals. It usually works together with `bid_strategy` field.<br> |
| `bid_info`<br><br>*map<string, unsigned int32>* | Map of bid objective to bid value.<br> |
| `bid_strategy` This field is only accessible in v3.0 or later.<br><br>*enum {LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS}* | Bid strategy for this ad set when you use `AUCTION` as your buying type:<br><br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as *automatic bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. Get your bid cap with the field `bid_amount`.<br>This strategy is also known as *manual maximum-cost bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>Notes:<br><br><br>• If you enable campaign budget optimization, you should get `bid_strategy` at the parent campaign level.<br>• `TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0).<br> |
| `billing_event`<br><br>*enum {APP_INSTALLS, CLICKS, IMPRESSIONS, LINK_CLICKS, NONE, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, THRUPLAY, PURCHASE, LISTING_INTERACTION}* | The billing event for this ad set:<br>`APP_INSTALLS`: Pay when people install your app.<br>`CLICKS`: Pay when people click anywhere in the ad. <br>`IMPRESSIONS`: Pay when the ads are shown to people.<br>`LINK_CLICKS`: Pay when people click on the link of the ad.<br>`OFFER_CLAIMS`: Pay when people claim the offer.<br>`PAGE_LIKES`: Pay when people like your page.<br>`POST_ENGAGEMENT`: Pay when people engage with your post.<br>`VIDEO_VIEWS`: Pay when people watch your video ads for at least 10 seconds.<br>`THRUPLAY`: Pay for ads that are played to completion, or played for at least 15 seconds.<br> |
| `brand_safety_config`<br><br>*BrandSafetyCampaignConfig* | brand_safety_config<br> |
| `budget_remaining`<br><br>*numeric string* | Remaining budget of this Ad Set<br> |
| `campaign`<br><br>*[Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group)* | The campaign that contains this ad set<br> |
| `campaign_active_time`<br><br>*numeric string* | Campaign running length<br> |
| `campaign_attribution`<br><br>*enum* | campaign_attribution, a new field for app ads campaign, used to indicate a campaign's attribution type, eg: SKAN or AEM<br> |
| `campaign_id`<br><br>*numeric string* | The ID of the campaign that contains this ad set<br> |
| `configured_status`<br><br>*enum {ACTIVE, PAUSED, DELETED, ARCHIVED}* | The status set at the ad set level. It can be different from the<br>effective status due to its parent campaign. Prefer using 'status'<br>instead of this.<br> |
| `contextual_bundling_spec`<br><br>*ContextualBundlingSpec* | specs of contextual bundling Ad Set setup, including signal of opt-in/out the feature<br> |
| `created_time`<br><br>*datetime* | Time when this Ad Set was created<br> |
| `creative_sequence`<br><br>*list<numeric string>* | Order of the adgroup sequence to be shown to users<br> |
| `daily_budget`<br><br>*numeric string* | The daily budget of the set defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api).<br> |
| `daily_min_spend_target`<br><br>*numeric string* | Daily minimum spend target of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. This target is not a guarantee but our best effort.<br> |
| `daily_spend_cap`<br><br>*numeric string* | Daily spend cap of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign.<br> |
| `destination_type`<br><br>*string* | Destination of ads in this Ad Set.<br><br><br>Options include: `WEBSITE`, `APP`, `MESSENGER`, `INSTAGRAM_DIRECT`.<br><br><br>The `ON_AD`, `ON_POST`, `ON_VIDEO`, `ON_PAGE`, and `ON_EVENT` destination types are currently in limited beta testing. Trying to duplicate campaigns with existing destination types using these new destination types may throw an error. See the [Outcome-Driven Ads Experiences](#odax) section below for more information.<br> |
| `dsa_beneficiary`<br><br>*string* | The beneficiary of all ads in this ad set.<br> |
| `dsa_payor`<br><br>*string* | The payor of all ads in this ad set.<br> |
| `effective_status`<br><br>*enum {ACTIVE, PAUSED, DELETED, CAMPAIGN_PAUSED, ARCHIVED, IN_PROCESS, WITH_ISSUES}* | The effective status of the adset. The status could be effective either<br>because of its own status, or the status of its parent campaign. `WITH_ISSUES` is available for version 3.2 or higher. `IN_PROCESS` is available for version 4.0 or higher.<br> |
| `end_time`<br><br>*datetime* | End time, in UTC UNIX timestamp<br> |
| `frequency_control_specs`<br><br>*[list<AdCampaignFrequencyControlSpecs>](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-frequency-control-specs)* | An array of frequency control specs for this ad set. Writes to this field are only available in ad sets where `REACH` and `THRUPLAY` are the performance goal.<br> |
| `instagram_user_id` This field is only accessible in v22.0 or later.<br><br>*numeric string* | Represents your Instagram account id, used for ads, including dynamic creative ads on Instagram.<br> |
| `is_dynamic_creative` This field is only accessible in v3.2 or later.<br><br>*bool* | Whether this ad set is a dynamic creative ad set. dynamic creative ad can be created only under ad set with this field set to be true.<br> |
| `is_incremental_attribution_enabled`<br><br>*bool* | Whether the campaign should use incremental attribution optimization.<br> |
| `issues_info` This field is only accessible in v3.2 or later.<br><br>*[list<AdCampaignIssuesInfo>](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-issues-info)* | Issues for this ad set that prevented it from deliverying<br> |
| `learning_stage_info`<br><br>*[AdCampaignLearningStageInfo](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-learning-stage-info)* | Info about whether the ranking or delivery system is still learning for this ad set. While the ad set is still in learning , we might unstablized delivery performances.<br> |
| `lifetime_budget`<br><br>*numeric string* | The lifetime budget of the set defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api).<br> |
| `lifetime_imps`<br><br>*int32* | Lifetime impressions. Available only for campaigns with `buying_type=FIXED_CPM`<br> |
| `lifetime_min_spend_target`<br><br>*numeric string* | Lifetime minimum spend target of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. This target is not a guarantee but our best effort.<br> |
| `lifetime_spend_cap`<br><br>*numeric string* | Lifetime spend cap of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign.<br> |
| `min_budget_spend_percentage`<br><br>*numeric string* | min_budget_spend_percentage<br> |
| `multi_optimization_goal_weight`<br><br>*string* | multi_optimization_goal_weight<br> |
| `name`<br><br>*string* | Name of the ad set<br> |
| `optimization_goal`<br><br>*enum {NONE, APP_INSTALLS, AD_RECALL_LIFT, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, LEAD_GENERATION, QUALITY_LEAD, LINK_CLICKS, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, QUALITY_CALL, REACH, LANDING_PAGE_VIEWS, VISIT_INSTAGRAM_PROFILE, ENGAGED_PAGE_VIEWS, VALUE, THRUPLAY, DERIVED_EVENTS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, CONVERSATIONS, IN_APP_VALUE, MESSAGING_PURCHASE_CONVERSION, MESSAGING_DEEP_CONVERSATION_AND_FOLLOW, SUBSCRIBERS, REMINDERS_SET, MEANINGFUL_CALL_ATTEMPT, PROFILE_VISIT, PROFILE_AND_PAGE_ENGAGEMENT, ADVERTISER_SILOED_VALUE, AUTOMATIC_OBJECTIVE, MESSAGING_APPOINTMENT_CONVERSION}* | The optimization goal this ad set is using.<br><br>`NONE`: Only available in read mode for campaigns created pre-v2.4.<br><br>`APP_INSTALLS`: Optimize for people more likely to install your app.<br><br>`AD_RECALL_LIFT`: Optimize for people more likely to remember seeing your ads.<br><br>`CLICKS`: Deprecated. Only available in read mode.<br><br>`ENGAGED_USERS`: Optimize for people more likely to take a particular action in your app.<br><br>`EVENT_RESPONSES`: Optimize for people more likely to attend your event.<br><br>`IMPRESSIONS`: Show the ads as many times as possible.<br><br>`LEAD_GENERATION`: Optimize for people more likely to fill out a lead generation form.<br><br>`QUALITY_LEAD`: Optimize for people who are likely to have a deeper conversation with advertisers after lead submission.<br><br>`LINK_CLICKS`: Optimize for people more likely to click in the link of the ad.<br><br>`OFFSITE_CONVERSIONS`: Optimize for people more likely to make a conversion on the site.<br><br>`PAGE_LIKES`: Optimize for people more likely to like your page.<br><br>`POST_ENGAGEMENT`: Optimize for people more likely to engage with your post.<br><br>`QUALITY_CALL`: Optimize for people who are likely to call the advertiser.<br><br>`REACH`: Optimize to reach the most unique users for each day or interval specified in `frequency_control_specs`.<br><br>`LANDING_PAGE_VIEWS`: Optimize for people who are most likely to click on and load your chosen landing page.<br><br>`VISIT_INSTAGRAM_PROFILE`: Optimize for visits to the advertiser's Instagram profile.<br><br>`VALUE`: Optimize for maximum total purchase value within the specified attribution window.<br><br>`THRUPLAY`: Optimize delivery of your ads to people who are more likely to play your ad to completion, or play it for at least 15 seconds.<br><br>`DERIVED_EVENTS`: Optimize for retention, which reaches people who are most likely to return to the app and open it again during a given time frame after installing. You can choose either two days, meaning the app is likely to be reopened between 24 and 48 hours after installation; or seven days, meaning the app is likely to be reopened between 144 and 168 hours after installation.<br><br>`APP_INSTALLS_AND_OFFSITE_CONVERSIONS`: Optimizes for people more likely to install your app and make a conversion on your site. <br><br>`CONVERSATIONS`: Directs ads to people more likely to have a conversation with the business.<br> |
| `optimization_sub_event`<br><br>*string* | Optimization sub event for a specific optimization goal. For example: Sound-On event for Video-View-2s optimization goal.<br> |
| `pacing_type`<br><br>*list<string>* | Defines the pacing type, standard or using ad scheduling<br> |
| `promoted_object`<br><br>*[AdPromotedObject](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object)* | The object this ad set is promoting across all its ads.<br> |
| `recommendations`<br><br>*list<AdRecommendation>* | If there are recommendations for this ad set, this field includes them. Otherwise, will not be included in the response. This field is not included in redownload mode.<br> |
| `recurring_budget_semantics`<br><br>*bool* | If this field is `true`, your daily spend may be more than your daily budget while your weekly spend will not exceed 7 times your daily budget. More details explained in the [Ad Set Budget](https://developers.facebook.com/documentation/ads-commerce/marketing-api) document. If this is `false`, your amount spent daily will not exceed the daily budget. This field is not applicable for lifetime budgets.<br> |
| `regional_regulated_categories`<br><br>*list<enum>* | This param is used to specify `regional_regulated_categories`. Currently it supports `null` and the following values:<br><br><br>• TAIWAN_FINSERV: Use this value to declare a Financial Service ad set if the ad targets Taiwan Audience<br>• AUSTRALIA_FINSERV: Use this value to declare a Financial Service ad set if the ad set targets Australia Audience<br>• INDIA_FINSERV: Use this value to declare a Securities and Investments ad set if the ad set targets India Audience<br>• TAIWAN_UNIVERSAL: Use this value to declare an ad set if it targets Taiwan Audience<br>• SINGAPORE_UNIVERSAL: Use this value to declare an ad set if it targets Singapore Audience<br>• THAILAND_UNIVERSAL: Use this value to declare an ad set if it targets Thailand Audience and you are seeing "Beneficiary/payer is missing" errors (3858634, 3858636).<br>• BRAZIL_REGULATION: Use this value to declare an Ad Set if it targets Thailand Audience and you are seeing "Beneficiary/payer is missing" errors (3858634, 3858636).<br><br><br>If an ad set is a Financial Service Ad and it targets Taiwan, it needs to declare both `TAIWAN_FINSERV` and `TAIWAN_UNIVERSAL`<br><br><br>Example: `null` or `[AUSTRALIA_FINSERV]` or `[TAIWAN_FINSERV, TAIWAN_UNIVERSAL]`<br> |
| `regional_regulation_identities`<br><br>*RegionalRegulationIdentities* | This param is used to specify regional_regulation_identities used to represent the ad set. Currently it supports the following fields:<br><br><br>• taiwan_finserv_beneficiary: used for TAIWAN_FINSERV category<br>• taiwan_finserv_payer: used for TAIWAN_FINSERV category<br>• australia_finserv_beneficiary: used for AUSTRALIA_FINSERV category<br>• australia_finserv_payer: used for AUSTRALIA_FINSERV category<br>• india_finserv_beneficiary: used for INDIA_FINSERV category<br>• india_finserv_payer: used for INDIA_FINSERV category<br>• taiwan_universal_beneficiary: used for TAIWAN_UNIVERSAL category<br>• taiwan_universal_payer: used for TAIWAN_UNIVERSAL category<br>• singapore_universal_beneficiary: used for SINGAPORE_UNIVERSAL category<br>• singapore_universal_payer: used for SINGAPORE_UNIVERSAL category<br>• universal_beneficiary: used for THAILAND_UNIVERSAL category<br>• universal_payer: used for THAILAND_UNIVERSAL category<br>• universal_beneficiary: used for BRAZIL_REGULATION category<br>• universal_payer: used for BRAZIL_REGULATION category<br><br><br>Example:<br><br><br>`regional_regulation_identities: {<br>"taiwan_finserv_beneficiary": <verified_identity_id>,<br>"taiwan_finserv_payer": <verified_identity_id>,<br>"taiwan_universal_beneficiary": <verified_identity_id>,<br>"taiwan_universal_payer": <verified_identity_id>,<br>}`<br><br><br>During creation and update, the passed identities fields need to correspond to declared categories. Both beneficiary and payer identities must be included, and they can use the same identity ID.<br><br><br>To update an existing ad set identities, you need to pass new values for both categories and identities to overwrite the identity id or `null` to remove existing id.<br><br><br>For example:<br><br><br>Upon creation, `regional_regulated_categories` is `[TAIWAN_FINSERV, TAIWAN_UNIVERSAL]` and `regional_regulation_identities` is<br><br><br>`regional_regulation_identities: {<br>"taiwan_finserv_beneficiary": <id_123>,<br>"taiwan_finserv_payer": <id_123>,<br>"taiwan_universal_beneficiary": <id_456>,<br>"taiwan_universal_payer": <id_456>,<br>}`<br><br><br>For update, passing `[TAIWAN_UNIVERSAL]` and<br>`regional_regulation_identities: {<br>"taiwan_finserv_beneficiary": null<br>"taiwan_finserv_payer": null,<br>"taiwan_universal_beneficiary": <id_789>,<br>"taiwan_universal_payer": <id_789>,<br>}`<br><br><br>will remove `TAIWAN_FINSERV` declaration and update the identities ID of `TAIWAN_UNIVERSAL`<br> |
| `review_feedback`<br><br>*string* | Reviews for dynamic creative ad<br> |
| `rf_prediction_id`<br><br>*id* | Reach and frequency prediction ID<br> |
| `source_adset`<br><br>*[AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign)* | The source ad set that this ad set was copied from<br> |
| `source_adset_id`<br><br>*numeric string* | The source ad set id that this ad set was copied from<br> |
| `start_time`<br><br>*datetime* | Start time, in UTC UNIX timestamp<br> |
| `status`<br><br>*enum {ACTIVE, PAUSED, DELETED, ARCHIVED}* | The status set at the ad set level. It can be different from the<br>effective status due to its parent campaign. The field returns the same<br>value as `configured_status`, and is the suggested one to use.<br> |
| `targeting`<br><br>*Targeting* | Targeting<br> |
| `targeting_optimization_types` This field is only accessible in v12.0 or later.<br><br>*list<KeyValue:string,int32>* | Targeting options that are relaxed and used as a signal for optimization<br> |
| `time_based_ad_rotation_id_blocks`<br><br>*list<list<integer>>* | Specify ad creative that displays at custom date ranges in a campaign<br>as an array. A list of Adgroup IDs. The list of ads to display for each<br>time range in a given schedule. For example display first ad in Adgroup<br>for first date range, second ad for second date range, and so on. You<br>can display more than one ad per date range by providing more than<br>one ad ID per array. For example set<br>`time_based_ad_rotation_id_blocks` to [[1], [2, 3], [1, 4]]. On the<br>first date range show ad 1, on the second date range show ad 2 and ad 3<br>and on the last date range show ad 1 and ad 4. Use with<br>`time_based_ad_rotation_intervals` to specify date ranges.<br> |
| `time_based_ad_rotation_intervals`<br><br>*list<unsigned int32>* | Date range when specific ad creative displays during a campaign.<br>Provide date ranges in an array of UNIX timestamps where each<br>timestamp represents the start time for each date range. For example a<br>3-day campaign from May 9 12am to  May 11 11:59PM PST can have three<br>date ranges, the first date range starts from May 9 12:00AM to<br>May 9 11:59PM, second date range starts from May 10 12:00AM to<br>May 10 11:59PM and last starts from  May 11 12:00AM to  May 11 11:59PM.<br>The first timestamp should match the campaign start time. The last<br>timestamp should be at least 1 hour before the campaign end time. You<br>must provide at least two date ranges. All date ranges must cover the<br>whole campaign length, so any date range cannot exceed campaign length.<br>Use with `time_based_ad_rotation_id_blocks` to specify ad creative for<br>each date range.<br> |
| `updated_time`<br><br>*datetime* | Time when the Ad Set was updated<br> |
| `use_new_app_click`<br><br>*bool* | If set, allows Mobile App Engagement ads to optimize for LINK_CLICKS<br> |
| `value_rule_set_id`<br><br>*numeric string* | value_rule_set_id<br> |

#### Edges

| Edge | Description |
| --- | --- |
| [`activities`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/activities)<br><br>*Edge<AdActivity>* | The activities of this ad set<br> |
| [`ad_studies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/ad_studies)<br><br>*Edge<AdStudy>* | The ad studies containing this ad set<br> |
| [`adcreatives`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/adcreatives)<br><br>*Edge<AdCreative>* | The creatives of this ad set<br> |
| [`adrules_governed`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/adrules_governed)<br><br>*Edge<AdRule>* | Ad rules that govern this ad set - by default, this only returns rules that either directly mention the ad set by id or indirectly through the set `entity_type`<br> |
| [`ads`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/ads)<br><br>*Edge<Adgroup>* | The ads under this ad set<br> |
| [`asyncadrequests`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/asyncadrequests)<br><br>*Edge<AdAsyncRequest>* | Async ad requests for this ad set<br> |
| [`copies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/copies)<br><br>*Edge<AdCampaign>* | The copies of this ad set<br> |
| [`delivery_estimate`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/delivery_estimate)<br><br>*Edge<AdCampaignDeliveryEstimate>* | The delivery estimate for this ad set<br> |
| [`message_delivery_estimate`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/message_delivery_estimate)<br><br>*Edge<MessageDeliveryEstimate>* | Delivery estimation of the marketing message campaign<br> |
| [`targetingsentencelines`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/targetingsentencelines)<br><br>*Edge<TargetingSentenceLine>* | The targeting description sentence for this ad set<br> |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |
| 2500 | Error parsing graph query |

## Creating

**Warning:** For v20.0+, the Impressions optimization goal is deprecated for the legacy Post Engagement objective and the `ON_POST` destination_type.

### Examples {#create-examples}

Validate an ad set with a daily budget where the campaign objective is set to `APP_INSTALLS`.

```html
curl -X POST \
  -F 'name="Mobile App Installs Ad Set"' \
  -F 'daily_budget=1000' \
  -F 'bid_amount=2' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="APP_INSTALLS"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'promoted_object={
       "application_id": "<APP_ID>",
       "object_store_url": "<APP_STORE_URL>"
     }' \
  -F 'targeting={
       "device_platforms": [
         "mobile"
       ],
       "facebook_positions": [
         "feed"
       ],
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ],
       "user_os": [
         "IOS"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

### Considerations {#create-considerations}

#### Bid/Budget Validations

**Note:**

- All values in this section are in US Dollars.

- Differenct currencies have different minimum daily budget limits.

- Minimum values are defined in terms of the daily budget but apply to lifetime budgets as well.

- Minimum budget takes the total spent budget into account.

When creating an ad set, there will be a minimum budget for different billing events (Clicks, Impressions, Actions).  If the minimum daily budget is $5, a campaign lasting 5 days will need at least $25 for budget.

**Warning:** Budget amounts shown are for illustrative purposes only and can change based on situation.

If `bid_strategy` is set to `LOWEST_COST_WITHOUT_CAP` in the ad set:

| Billing Event | Minimum Daily Budget |
| --- | --- |
| Impressions | $0.50 |
| Clicks/Likes/Video Views | $2.50 |
| Low-frequency Actions  <br>(Includes mobile app installs, offer claims, or canvas app installs) | $40  <br>**Important:** This minimum daily budget is the same for all countries. |

If `bid_strategy` is set to `LOWEST_COST_WITH_BID_CAP` in the ad set:

| Billing Event | Minimum Daily Budget |
| --- | --- |
| Impressions | At least the `bid_amount`. For example, if the bid amount is $10, then $10 will be the minimum budget required. |
| Clicks/Actions | 5x the `bid_amount` for a Click or Action. For example, if the bid amount is $5 per click/action, then $25 will be the minimum budget required. |

**Note:** Budgets in non-USD currencies will be converted and validated upon time of ad set creation.

**Note:** For ads belonging to ad accounts from countries in the list below, the minimum values are 2x the ones in the tables. For example, if the billing event is an Impression, the minimum daily budget is $0.50, but in the the following countries the minimum would be $1.00:

Australia, Austria, Belgium, Canada, Denmark, Finland, France, Germany, Greece, Hong Kong, Israel, Italy, Japan, Netherlands, New Zealand, Norway, Singapore, South Korea, Spain, Sweden, Switzerland, Taiwan, United Kingdom, United States of America.

The only exception to this rule are Low-Frequency Actions when `bid_strategy` is `LOWEST_COST_WITHOUT_CAP`.

#### Locale targeted page post

If you promote a Page post which has been targeted by locale the ad set targeting must include the same, or a subset of, locale targeting as the Page post.

E.g. if the Page post is targeted at locales 6 (US English) and 24 (UK English), then the ad set must be targeted at one or more of the same locales.

#### Mobile App Ads

Mobile app ad sets should

- be used in conjunction with [targeting spec](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#mobile) fields `user_device` and `user_os`

- have a `MOBILE_APP_*` objective on the [campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group)

#### Desktop App Ads

Desktop app ad sets must

- include a [targeting spec](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting) of either

- `'page_types':['desktopfeed']` or

- `'page_types':['rightcolumn']` or

- `'page_types':['desktop']` along with the other targeting options you have selected.

- include a `CANVAS_APP_*` objective

#### Lookalike Expansion

Beginning with v13.0, for newly created ad sets that optimize for value, conversions, or app events, lookalike expansion will be turned on by default and cannot be disabled. When getting an ad set that optimizes for value, conversions, or app events, we will return a new lookalike property in the `targeting_optimization_types` map that indicates lookalike expansion is enabled and complements the existing `detailed_targeting` property for the detailed targeting expansion.

#### Targeting DSA Regulated Locations (EU)

For ad sets targeting the EU and/or associated territories, the `dsa_payor` and `dsa_beneficiary` fields are required. The information provided in these 2 fields  will be shown to end users to indicate who is paying for the ad and who is the beneficiary of the ad.

**Request**

Include the following fields in an API call to the `/{adset_id}` endpoint.

```
{
  "dsa_payor": "<PAYOR_NAME>",
  "dsa_beneficiary": "<BENEFICIARY_NAME>"
  ...
}
```

**Fields**

| Name | Description |
| --- | --- |
| `dsa_payor`<br><br>string (max 512 char) | The payor of all ads in this ad set. |
| `dsa_beneficiary`<br><br>string (max 512 char) | The beneficiary of all ads in this ad set. |

If these fields are not provided, the API may returns the following errors:

**Payor missing error**

```
{
  "error": {
    "message": "Invalid parameter",
    "type": "FacebookApiException",
    "code": 100,
    "error_data": "{\"blame_field_specs\":[[\"dsa_payor\"]]}",
    "error_subcode": 3858079,
    "is_transient": false,
    "error_user_title": "No payor provided in DSA regulated region",
    "error_user_msg": "The DSA requires ads to provide payor information in regulated regions. Updating/creating ad needs to provide payor of the ad.",
    "fbtrace_id": "fbtrace_id"
  },
  "__fb_trace_id__": "fbtrace_id",
  "__www_request_id__": "request_id"
}
```

**Beneficiary missing error**

```
{
  "error": {
    "message": "Invalid parameter",
    "type": "FacebookApiException",
    "code": 100,
    "error_data": "{\"blame_field_specs\":[[\"dsa_beneficiary\"]]}",
    "error_subcode": 3858081,
    "is_transient": false,
    "error_user_title": "No payor/beneficiary provided in DSA regulated location",
    "error_user_msg": "The DSA requires ads to provide beneficiary information in regulated regions. Updating/creating ad needs to provide beneficiary of the ad.",
    "fbtrace_id": "fbtrace_id"
  },
  "__fb_trace_id__": "fbtrace_id",
  "__www_request_id__": "request_id"
}
```

### /{ad_set_id}/copies
You can make a POST request to *copies* edge from the following paths:

- [/{ad_set_id}/copies](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/copies)

When posting to this edge, an [AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `campaign_id`<br><br>*numeric string or integer* | Single ID of a campaign to make parent of the copy. The copy inherits all campaign settings, such as budget from the parent.Ignore if you want to keep the copy under the original campaign parent.<br> |
| `deep_copy`<br><br>*boolean* | **Default value: **`false`<br>Whether to copy all the child ads. Limits: the total number of children ads to copy should not exceed 3 for a synchronous call and 51 for an asynchronous call.<br> |
| `end_time`<br><br>*datetime* | The end time of the set, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. When creating a set with a daily budget, specify `end_time=0` to set the set to be ongoing without end date. If not set, the copied adset will inherit the end time from the original set<br> |
| `rename_options`<br><br>*JSON or object-like arrays* | Rename options<br><br><br>`rename_strategy` *enum {DEEP_RENAME, ONLY_TOP_LEVEL_RENAME, NO_RENAME}*<br><br>**Default value: **`ONLY_TOP_LEVEL_RENAME`<br>`DEEP_RENAME`: will change this object's name and children's names in the copied object. `ONLY_TOP_LEVEL_RENAME`: will change the this object's name but won't change the children's name in the copied object. `NO_RENAME`: will change no name in the copied object<br><br><br>`rename_prefix` *string*<br>A prefix to copy names. Defaults to null if not provided.<br><br><br>`rename_suffix` *string*<br>A suffix to copy names. Defaults to null if not provided and appends a localized string of `- Copy` based on the ad account locale.<br> |
| `start_time`<br><br>*datetime* | The start time of the set, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. If not set, the copied adset will inherit the start time from the original set<br> |
| `status_option`<br><br>*enum {ACTIVE, PAUSED, INHERITED_FROM_SOURCE}* | **Default value: **`PAUSED`<br>`ACTIVE`: the copied adset will have active status. `PAUSED`: the copied adset will have paused status. `INHERITED_FROM_SOURCE`: the copied adset will have the status from the original set.<br> |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *copied_adset_id* in the return type.

```
Struct  {
copied_adset_id: numeric string,
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
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 2695 | The ad set creation reached its campaign group(ios14) limit. |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |

### /act_{ad_account_id}/adsets
You can make a POST request to *adsets* edge from the following paths:

- [/act_{ad_account_id}/adsets](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adsets)

When posting to this edge, an [AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) will be created.

#### Example

### HTTP
```
POST /v25.0/act_<AD_ACCOUNT_ID>/adsets HTTP/1.1
Host: graph.facebook.com

name=My+First+Adset&lifetime_budget=20000&start_time=2026-05-12T10%3A45%3A09-0700&end_time=2026-05-22T10%3A45%3A09-0700&campaign_id=%3CAD_CAMPAIGN_ID%3E&bid_amount=100&billing_event=LINK_CLICKS&optimization_goal=LINK_CLICKS&targeting=%7B%22facebook_positions%22%3A%5B%22feed%22%5D%2C%22geo_locations%22%3A%7B%22countries%22%3A%5B%22US%22%5D%7D%2C%22publisher_platforms%22%3A%5B%22facebook%22%2C%22audience_network%22%5D%7D&status=PAUSED
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/act_<AD_ACCOUNT_ID>/adsets',
    array (
      'name' => 'My First Adset',
      'lifetime_budget' => '20000',
      'start_time' => '2026-05-12T10:45:09-0700',
      'end_time' => '2026-05-22T10:45:09-0700',
      'campaign_id' => '<AD_CAMPAIGN_ID>',
      'bid_amount' => '100',
      'billing_event' => 'LINK_CLICKS',
      'optimization_goal' => 'LINK_CLICKS',
      'targeting' => '{"facebook_positions":["feed"],"geo_locations":{"countries":["US"]},"publisher_platforms":["facebook","audience_network"]}',
      'status' => 'PAUSED',
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
    "/act_<AD_ACCOUNT_ID>/adsets",
    "POST",
    {
        "name": "My First Adset",
        "lifetime_budget": "20000",
        "start_time": "2026-05-12T10:45:09-0700",
        "end_time": "2026-05-22T10:45:09-0700",
        "campaign_id": "<AD_CAMPAIGN_ID>",
        "bid_amount": "100",
        "billing_event": "LINK_CLICKS",
        "optimization_goal": "LINK_CLICKS",
        "targeting": "{\"facebook_positions\":[\"feed\"],\"geo_locations\":{\"countries\":[\"US\"]},\"publisher_platforms\":[\"facebook\",\"audience_network\"]}",
        "status": "PAUSED"
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
params.putString("name", "My First Adset");
params.putString("lifetime_budget", "20000");
params.putString("start_time", "2026-05-12T10:45:09-0700");
params.putString("end_time", "2026-05-22T10:45:09-0700");
params.putString("campaign_id", "<AD_CAMPAIGN_ID>");
params.putString("bid_amount", "100");
params.putString("billing_event", "LINK_CLICKS");
params.putString("optimization_goal", "LINK_CLICKS");
params.putString("targeting", "{\"facebook_positions\":[\"feed\"],\"geo_locations\":{\"countries\":[\"US\"]},\"publisher_platforms\":[\"facebook\",\"audience_network\"]}");
params.putString("status", "PAUSED");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/adsets",
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
  @"name": @"My First Adset",
  @"lifetime_budget": @"20000",
  @"start_time": @"2026-05-12T10:45:09-0700",
  @"end_time": @"2026-05-22T10:45:09-0700",
  @"campaign_id": @"<AD_CAMPAIGN_ID>",
  @"bid_amount": @"100",
  @"billing_event": @"LINK_CLICKS",
  @"optimization_goal": @"LINK_CLICKS",
  @"targeting": @"{\"facebook_positions\":[\"feed\"],\"geo_locations\":{\"countries\":[\"US\"]},\"publisher_platforms\":[\"facebook\",\"audience_network\"]}",
  @"status": @"PAUSED",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/adsets"
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
  -F 'name="My First Adset"' \
  -F 'lifetime_budget=20000' \
  -F 'start_time="2026-05-12T10:45:09-0700"' \
  -F 'end_time="2026-05-22T10:45:09-0700"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'bid_amount=100' \
  -F 'billing_event="LINK_CLICKS"' \
  -F 'optimization_goal="LINK_CLICKS"' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fadsets%3Fname%3DMy%2BFirst%2BAdset%26lifetime_budget%3D20000%26start_time%3D2026-05-12T10%253A45%253A09-0700%26end_time%3D2026-05-22T10%253A45%253A09-0700%26campaign_id%3D%253CAD_CAMPAIGN_ID%253E%26bid_amount%3D100%26billing_event%3DLINK_CLICKS%26optimization_goal%3DLINK_CLICKS%26targeting%3D%257B%2522facebook_positions%2522%253A%255B%2522feed%2522%255D%252C%2522geo_locations%2522%253A%257B%2522countries%2522%253A%255B%2522US%2522%255D%257D%252C%2522publisher_platforms%2522%253A%255B%2522facebook%2522%252C%2522audience_network%2522%255D%257D%26status%3DPAUSED&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `adlabels`<br><br>*list<Object>* | Specifies list of labels to be associated with this object. This field is optional<br> |
| `adset_schedule`<br><br>*list<Object>* | Ad set schedule, representing a delivery schedule for a single day<br><br><br>`start_minute` *int64*<br>A 0 based minute of the day representing when the schedule starts<br><br>**[required]**<br><br><br>`end_minute` *int64*<br>A 0 based minute of the day representing when the schedule ends<br><br>**[required]**<br><br><br>`days` *list<int64>*<br>Array of ints representing which days the schedule is active. Valid values are 0-6 with 0 representing Sunday, 1 representing Monday, ... and 6 representing Saturday.<br><br>**[required]**<br><br><br>`timezone_type` *enum {USER, ADVERTISER}*<br><br>**Default value: **`USER` |
| `attribution_spec`<br><br>*list<JSON object>* | Conversion attribution spec used for attributing conversions for optimization. Supported window lengths differ by optimization goal and campaign objective.<br><br><br>`event_type` *enum {CLICK_THROUGH, VIEW_THROUGH, ENGAGED_VIDEO_VIEW}*<br>**[required]**<br><br><br>`window_days` *int64*<br>**[required]**<br><br><br>`weight` *float*<br><br>**Default value: **`100` |
| `automatic_manual_state`<br><br>*enum{UNSET, AUTOMATIC, MANUAL}* | automatic_manual_state<br> |
| `bid_amount`<br><br>*integer* | Bid cap or target cost for this ad set. The bid cap used in a *lowest cost bid strategy* is defined as the maximum bid you want to pay for a result based on your `optimization_goal`. The target cost used in a *target cost bid strategy* lets Facebook bid to meet your target on average and keep costs stable as you spend. If an ad level `bid_amount` is specified, updating this value will overwrite the previous ad level bid. Unless you are using [Reach and Frequency](https://developers.facebook.com/docs/marketing-api/reachandfrequency), `bid_amount` is required if `bid_strategy` is set to `LOWEST_COST_WITH_BID_CAP` or `COST_CAP`.<br><br>The bid amount's unit is cents for currencies like USD, EUR, and the basic unit for currencies like JPY, KRW. The bid amount for ads with `IMPRESSION` or `REACH` as `billing_event` is per 1,000 occurrences, and has to be at least 2 US cents or more. For ads with other `billing_event`s, the bid amount is for each occurrence, and has a minimum value 1 US cents. The minimum bid amounts of other currencies are of similar value to the US Dollar values provided.<br> |
| `bid_strategy` This field is only accessible in v3.0 or later.<br><br>*enum{LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS}* | Choose bid strategy for this ad set to suit your specific business goals.<br>Each strategy has tradeoffs and may be available for certain `optimization_goal`s:<br><br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as *automatic bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. If you select this, you must provide<br>a bid cap with the `bid_amount` field.<br>Note: during creation this bid strategy is set if you provide `bid_amount` only.<br>This strategy is also known as *manual maximum-cost bidding*.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost](https://www.facebook.com/business/help/721453268045071).<br><br><br>Notes:<br><br><br>• If you enable campaign budget optimization, you should set `bid_strategy` at the parent campaign level.<br><br>• `TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0).<br><br> |
| `billing_event`<br><br>*enum{APP_INSTALLS, CLICKS, IMPRESSIONS, LINK_CLICKS, NONE, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, THRUPLAY, PURCHASE, LISTING_INTERACTION}* | The billing event that this ad set is using:<br>APP_INSTALLS: Pay when people install your app.<br>CLICKS: Deprecated.<br>IMPRESSIONS: Pay when the ads are shown to people.<br>LINK_CLICKS: Pay when people click on the link of the ad.<br>OFFER_CLAIMS: Pay when people claim the offer.<br>PAGE_LIKES: Pay when people like your page.<br>POST_ENGAGEMENT: Pay when people engage with your post.<br>VIDEO_VIEWS: Pay when people watch your video ads for at least 10 seconds.<br>THRUPLAY: Pay for ads that are played to completion, or played for at least 15 seconds.<br> |
| `budget_schedule_specs`<br><br>*list<JSON or object-like arrays>* | Initial high demand periods to be created with the ad set.<br><br>Provide list of `time_start`, `time_end`,`budget_value`, and `budget_value_type`.<br>For example,<br>-F 'budget_schedule_specs=[{<br><br>"time_start":1699081200,<br><br>"time_end":1699167600,<br><br>"budget_value":100,<br><br>"budget_value_type":"ABSOLUTE"<br><br>}]'<br><br>See [High Demand Period](https://developers.facebook.com/docs/graph-api/reference/high-demand-period) for more details on each field.<br><br><br>`id` *int64*<br><br>`time_start` *datetime*<br><br>`time_end` *datetime*<br><br>`budget_value` *int64*<br><br>`budget_value_type` *enum{ABSOLUTE, MULTIPLIER}*<br><br>`recurrence_type` *enum{ONE_TIME, WEEKLY}*<br><br>`weekly_schedule` *list<JSON or object-like arrays>*<br><br>`days` *list<int64>*<br><br>`minute_start` *int64*<br><br>`minute_end` *int64*<br><br>`timezone_type` *string* |
| `budget_source`<br><br>*enum{NONE, RMN}* | budget_source<br> |
| `budget_split_set_id`<br><br>*numeric string or integer* | budget_split_set_id<br> |
| `campaign_attribution`<br><br>*enum{}* | campaign_attribution<br> |
| `campaign_id`<br><br>*numeric string or integer* | The ad campaign you wish to add this ad set to.<br> |
| `campaign_spec`<br><br>*Campaign spec* | Provide `name`, `objective` and `buying_type` for a campaign you want to create. Otherwise you need to provide `campaign_id` for an existing ad campaign. For example:<br>-F 'campaign_spec={<br>  "name": "Inline created campaign",<br>  "objective": "CONVERSIONS",<br>  "buying_type": "AUCTION"<br>}'<br><br>Please refer to the [Outcome-Driven Ads Experiences mapping table](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax-mapping) to find new objectives and their corresponding destination types, optimization goals and promoted objects.<br> |
| `contextual_bundling_spec`<br><br>*Object* | settings of Contextual Bundle to support ads serving in Facebook contextual surfaces<br><br><br>`status` *enum{OPT_OUT, OPT_IN}* |
| `cost_bidding_mode`<br><br>*enum{VOLUME_FOCUSED, BALANCED, COST_FOCUSED}* | cost_bidding_mode<br> |
| `creative_sequence`<br><br>*list<numeric string or integer>* | Order of the adgroup sequence to be shown to users<br> |
| `daily_budget`<br><br>*int64* | The daily budget defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api), allowed only for ad sets with a duration (difference between `end_time` and `start_time`) longer than 24 hours. <br>Either `daily_budget` or `lifetime_budget` must be greater than 0.<br> |
| `daily_imps`<br><br>*int64* | Daily impressions. Available only for campaigns with `buying_type=FIXED_CPM`<br> |
| `daily_min_spend_target`<br><br>*int64* | Daily minimum spend target of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. This target is not a guarantee but our best effort.<br> |
| `daily_spend_cap`<br><br>*int64* | Daily spend cap of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. Set the value to 922337203685478 to remove the spend cap.<br> |
| `destination_type`<br><br>*enum{WEBSITE, APP, MESSENGER, APPLINKS_AUTOMATIC, WHATSAPP, INSTAGRAM_DIRECT, FACEBOOK, MESSAGING_MESSENGER_WHATSAPP, MESSAGING_INSTAGRAM_DIRECT_MESSENGER, MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP, MESSAGING_INSTAGRAM_DIRECT_WHATSAPP, SHOP_AUTOMATIC, ON_AD, ON_POST, ON_EVENT, ON_VIDEO, ON_PAGE, INSTAGRAM_PROFILE, FACEBOOK_PAGE, INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE, INSTAGRAM_LIVE, FACEBOOK_LIVE, IMAGINE}* | Destination of ads in this Ad Set. Options include: Website, App, Messenger, `INSTAGRAM_DIRECT`, `INSTAGRAM_PROFILE`.<br> |
| `dsa_beneficiary`<br><br>*string* | dsa_beneficiary<br> |
| `dsa_payor`<br><br>*string* | dsa_payor<br> |
| `end_time`<br><br>*datetime* | End time, required when `lifetime_budget` is specified. e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. When creating a set with a daily budget, specify `end_time=0` to set the set to be ongoing and have no end date. UTC UNIX timestamp<br> |
| `execution_options`<br><br>*list<enum{validate_only, include_recommendations}>* | **Default value: **`Set`<br>An execution setting<br> `validate_only`: when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. <br>`include_recommendations`: this option cannot be used by itself. When this option is used, recommendations  for ad object's configuration will be included. A separate section [recommendations](https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation) will be included in the response, but only if recommendations for this specification exist.<br>If the call passes validation or review, response will be `{"success": true}`. If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review.<br> |
| `existing_customer_budget_percentage`<br><br>*int64* | existing_customer_budget_percentage<br> |
| `frequency_control_specs`<br><br>*list<Object>* | An array of frequency control specs for this ad set. Writes to this field are only available in ad sets where `REACH` and `THRUPLAY` are the performance goal.<br><br><br>`event` *enum{IMPRESSIONS, VIDEO_VIEWS, VIDEO_VIEWS_2S, VIDEO_VIEWS_15S}*<br>Event name, only `IMPRESSIONS` currently.<br><br>**[required]**<br><br><br>`interval_days` *integer*<br>Interval period in days, between 1 and 90<br>(inclusive)<br><br>**[required]**<br><br><br>`max_frequency` *integer*<br>The maximum frequency, between 1 and 90<br>(inclusive)<br><br>**[required]**<br><br><br>`type` *enum{NONE, CAP, TARGET}* |
| `is_dc_follow_optimized`<br><br>*boolean* | is_dc_follow_optimized<br> |
| `is_dynamic_creative` This field is only accessible in v3.2 or later.<br><br>*boolean* | Indicates the ad set must only be used for dynamic creatives. Dynamic creative ads can be created in this ad set. Defaults to `false`<br> |
| `is_sac_cfca_terms_certified`<br><br>*boolean* | is_sac_cfca_terms_certified<br> |
| `lifetime_budget`<br><br>*int64* | Lifetime budget, defined in  your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api). If specified, you must also specify an `end_time`.<br>Either `daily_budget` or `lifetime_budget` must be greater than 0.<br> |
| `lifetime_imps`<br><br>*int64* | Lifetime impressions. Available only for campaigns with `buying_type=FIXED_CPM`<br> |
| `lifetime_min_spend_target`<br><br>*int64* | Lifetime minimum spend target of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. This target is not a guarantee but our best effort.<br> |
| `lifetime_spend_cap`<br><br>*int64* | Lifetime spend cap of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. Set the value to 922337203685478 to remove the spend cap.<br> |
| `max_budget_spend_percentage`<br><br>*int64* | max_budget_spend_percentage<br> |
| `min_budget_spend_percentage`<br><br>*int64* | min_budget_spend_percentage<br> |
| `multi_event_conversion_attribution_window_seconds`<br><br>*int64* | multi_event_conversion_attribution_window_seconds<br> |
| `multi_optimization_goal_weight`<br><br>*enum{UNDEFINED, BALANCED, PREFER_INSTALL, PREFER_EVENT}* | multi_optimization_goal_weight<br> |
| `name`<br><br>*string* | Ad set name, max length of 400 characters.<br><br>**[required]**<br><br>**[supports emoji]**<br> |
| `optimization_goal`<br><br>*enum{NONE, APP_INSTALLS, AD_RECALL_LIFT, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, LEAD_GENERATION, QUALITY_LEAD, LINK_CLICKS, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, QUALITY_CALL, REACH, LANDING_PAGE_VIEWS, VISIT_INSTAGRAM_PROFILE, ENGAGED_PAGE_VIEWS, VALUE, THRUPLAY, DERIVED_EVENTS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, CONVERSATIONS, IN_APP_VALUE, MESSAGING_PURCHASE_CONVERSION, MESSAGING_DEEP_CONVERSATION_AND_FOLLOW, SUBSCRIBERS, REMINDERS_SET, MEANINGFUL_CALL_ATTEMPT, PROFILE_VISIT, PROFILE_AND_PAGE_ENGAGEMENT, ADVERTISER_SILOED_VALUE, AUTOMATIC_OBJECTIVE, MESSAGING_APPOINTMENT_CONVERSION}* | What the ad set is optimizing for. <br>`APP_INSTALLS`: Will optimize for people more likely to install your app.<br>`ENGAGED_USERS`: Will optimize for people more likely to take a particular action in your app.<br>`EVENT_RESPONSES`: Will optimize for people more likely to attend your event.<br>`IMPRESSIONS`: Will show the ads as many times as possible.<br>`LEAD_GENERATION`: Will optimize for people more likely to fill out a lead generation form.<br>`LINK_CLICKS`: Will optimize for people more likely to click in the link of the ad.<br>`OFFER_CLAIMS`: Will optimize for people more likely to claim the offer.<br>`OFFSITE_CONVERSIONS`: Will optimize for people more likely to make a conversion in the site<br>`PAGE_ENGAGEMENT`: Will optimize for people more likely to engage with your page.<br>`PAGE_LIKES`: Will optimize for people more likely to like your page.<br>`POST_ENGAGEMENT`: Will optimize for people more likely to engage with your post.<br>`REACH`: Optimize to reach the most unique users of each day or interval specified in `frequency_control_specs`.<br>`SOCIAL_IMPRESSIONS`: Increase the number of impressions with social context. For example, with the names of one or more of the user's friends attached to the ad who have already liked the page or installed the app.<br>`VALUE`: Will optimize for maximum total purchase value within the specified attribution window.<br>`THRUPLAY`: Will optimize delivery of your ads to people are more likely to play your ad to completion, or play it for at least 15 seconds.<br>`AD_RECALL_LIFT`: Optimize for people more likely to remember seeing your ads.<br>`VISIT_INSTAGRAM_PROFILE`: Optimize for visits to the advertiser's instagram profile.<br> |
| `optimization_sub_event`<br><br>*enum{NONE, VIDEO_SOUND_ON, TRIP_CONSIDERATION, TRAVEL_INTENT, TRAVEL_INTENT_NO_DESTINATION_INTENT, TRAVEL_INTENT_BUCKET_01, TRAVEL_INTENT_BUCKET_02, TRAVEL_INTENT_BUCKET_03, TRAVEL_INTENT_BUCKET_04, TRAVEL_INTENT_BUCKET_05, POST_INTERACTION}* | Optimization sub event for a specific optimization goal (ex: Sound-On event for Video-View-2s optimization goal)<br> |
| `pacing_type`<br><br>*list<string>* | Defines the pacing type, standard by default or using [ad scheduling](https://developers.facebook.com/docs/marketing-api/adset/pacing)<br> |
| `promoted_object`<br><br>*Object* | The object this ad set is promoting across all its ads.<br>Required with certain campaign objectives.<br><br>**CONVERSIONS**<br>• `pixel_id` (Conversion pixel ID)<br>• `pixel_id` (Facebook pixel ID) and `custom_event_type`<br>• `pixel_id` (Facebook pixel ID) and `pixel_rule` and `custom_event_type`<br>• `event_id` (Facebook event ID) and `custom_event_type`<br>• `application_id`, `object_store_url`, and `custom_event_type` for<br>mobile app events<br>• `offline_conversion_data_set_id` (Offline dataset ID) and<br>`custom_event_type` for offline conversions<br><br>**PAGE_LIKES**<br>• `page_id`<br><br>**OFFER_CLAIMS**<br>• `page_id`<br><br>**LINK_CLICKS**<br>• `application_id` and `object_store_url` for mobile app or Canvas app engagement link clicks<br><br>**APP_INSTALLS**<br>• `application_id` and `object_store_url`<br><br>**if the `optimization_goal` is `OFFSITE_CONVERSIONS`**<br>• `application_id`, `object_store_url`, and `custom_event_type` (Standard Events)<br>• `application_id`, `object_store_url`, `custom_event_type = OTHER` and `custom_event_str` (Custom Events)<br><br>**PRODUCT_CATALOG_SALES**<br>• `product_set_id`<br>• `product_set_id` and `custom_event_type`<br><br>When `optimization_goal` is `LEAD_GENERATION`, `page_id` needs to be passed as promoted_object.<br><br>Please refer to the [Outcome-Driven Ads Experiences mapping table](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax-mapping) to find new objectives and their corresponding destination types, optimization goals and promoted objects.<br><br>`application_id` *int*<br>The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement<br><br><br>`pixel_id` *numeric string or integer*<br>The ID of a Facebook conversion pixel.  Used with offsite conversion campaigns.<br><br><br>`custom_event_type` *enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER}*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`object_store_url` *URL*<br>The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br><br><br>`object_store_urls` *list<URL>*<br>The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br><br><br>`offer_id` *numeric string or integer*<br>The ID of an Offer from a Facebook Page.<br><br><br>`page_id` *Page ID*<br>The ID of a Facebook Page<br><br><br>`product_catalog_id` *numeric string or integer*<br>The ID of a Product Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br><br><br>`product_item_id` *numeric string or integer*<br>The ID of the product item.<br><br><br>`job_listing_id` *numeric string or integer*<br>The ID of the marketplace job listing.<br><br><br>`instagram_profile_id` *numeric string or integer*<br>The ID of the instagram profile id.<br><br><br>`product_set_id` *numeric string or integer*<br>The ID of a Product Set within an Ad Set level Product<br>Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br><br><br>`event_id` *numeric string or integer*<br>The ID of a Facebook Event<br><br><br>`offline_conversion_data_set_id` *numeric string or integer*<br>The ID of the offline dataset.<br><br><br>`fundraiser_campaign_id` *numeric string or integer*<br>The ID of the fundraiser campaign.<br><br><br>`custom_event_str` *string*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`mcme_conversion_id` *numeric string or integer*<br>The ID of a MCME conversion.<br><br><br>`conversion_goal_id` *numeric string or integer*<br>The ID of a Conversion Goal.<br><br><br>`offsite_conversion_event_id` *numeric string or integer*<br>The ID of a Offsite Conversion Event<br><br><br>`boosted_product_set_id` *numeric string or integer*<br>The ID of the Boosted Product Set within an Ad Set level Product<br>Catalog. Should only be present when the advertiser has<br>opted into Product Set Boosting.<br><br><br>`lead_ads_form_event_source_type` *enum{inferred, meta_source, offsite_crm, offsite_web, onsite_crm, onsite_crm_single_event, onsite_clo_dep_aet, onsite_web, onsite_p2b_call, onsite_messaging, qualified_lead_file}*<br>The event source of lead ads form.<br><br><br>`lead_ads_custom_event_type` *enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER}*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`lead_ads_custom_event_str` *string*<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br><br><br>`lead_ads_offsite_conversion_type` *enum{default, clo}*<br>The offsite conversion type for lead ads<br><br><br>`value_semantic_type` *enum {VALUE, MARGIN, LIFETIME_VALUE}*<br>The semantic of the event value to be using for optimization<br><br><br>`variation` *enum {OMNI_CHANNEL_SHOP_AUTOMATIC_DATA_COLLECTION, PRODUCT_SET_AND_APP, PRODUCT_SET_AND_IN_STORE, PRODUCT_SET_AND_OMNICHANNEL, PRODUCT_SET_AND_PHONE_CALL, PRODUCT_SET_AND_WEBSITE, PRODUCT_SET_AND_WEBSITE_AND_PHONE_CALL, PRODUCT_SET_WEBSITE_APP_AND_INSTORE}*<br>Variation of the promoted object for a PCA ad<br><br><br>`passback_pixel_id` *numeric string or integer*<br>ID of the pixel used for tracking passback events<br><br><br>`passback_application_id` *numeric string or integer*<br>ID of the application used for tracking passback events<br><br><br>`product_set_optimization` *enum{enabled, disabled}*<br>Enum defining whether or not the ad should be optimized for the promoted product set<br><br><br>`full_funnel_objective` *enum{OFFER_CLAIMS, PAGE_LIKES, EVENT_RESPONSES, POST_ENGAGEMENT, WEBSITE_CONVERSIONS, LINK_CLICKS, VIDEO_VIEWS, LOCAL_AWARENESS, PRODUCT_CATALOG_SALES, LEAD_GENERATION, BRAND_AWARENESS, STORE_VISITS, REACH, APP_INSTALLS, MESSAGES, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION}*<br>Enum defining the full funnel objective of the campaign<br><br><br>`dataset_split_id` *numeric string or integer*<br>ID of the dataset split used to perform additional optimization on the dataset<br><br><br>`dataset_split_ids` *array<numeric string>*<br>IDs of the dataset splits used to perform additional optimization on the dataset<br><br><br>`lead_ads_selected_pixel_id` *numeric string or integer*<br>The selected pixel id for lead ads conversion leads optimization<br><br><br>`custom_attribution_source_ids` *array<numeric string>*<br>IDs of the custom attribution sources used for tracking passback events<br><br><br>`multi_event_product` *int64*<br>Identifies which action-to-action product the advertiser is using<br><br><br>`product_sales_channel` *enum {ONLINE, IN_STORE, OMNI}*<br>ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads<br><br><br>`anchor_event_config` *JSON object*<br>Configuration for anchor event in multi-event optimization campaigns<br><br><br>`multi_event_conversion_info` *JSON object*<br>Configuration for multi-event conversion info in CLO campaigns<br><br><br>`live_video_destination` *string*<br>The live video destination type for live video ads<br><br><br>`smart_pse_enabled` *boolean*<br>Whether Smart Product Set Expansion is enabled for this campaign.<br><br><br>`smart_pse_setting` *enum{ENABLED, DISABLED}*<br>Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues.<br><br><br>`lead_ads_follow_up_event` *enum{whatsapp_conversations}*<br>The selected lead follow-up event for lead ads campaigns.<br><br><br>`omnichannel_object` *Object*<br><br>`app` *array<JSON object>*<br><br>`pixel` *array<JSON object>*<br>**[required]**<br><br><br>`onsite` *array<JSON object>*<br><br>`whats_app_business_phone_number_id` *numeric string or integer*<br><br>`whatsapp_phone_number` *string* |
| `relative_value`<br><br>*float* | relative_value<br> |
| `rf_prediction_id`<br><br>*numeric string or integer* | Reach and frequency prediction ID<br> |
| `source_adset_id`<br><br>*numeric string or integer* | The source adset id that this ad is copied from (if applicable).<br> |
| `start_time`<br><br>*datetime* | The start time of the set, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp<br> |
| `status`<br><br>*enum{ACTIVE, PAUSED, DELETED, ARCHIVED}* | Only `ACTIVE` and `PAUSED` are valid for creation. The other statuses<br>can be used for update. If it is set to `PAUSED`, all its active ads<br>will be paused and have an effective status `ADSET_PAUSED`.<br> |
| `targeting`<br><br>*Targeting object* | An ad set's targeting structure.  "countries" is required. See [targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting).<br> |
| `time_based_ad_rotation_id_blocks`<br><br>*list<list<int64>>* | Specify ad creative that displays at custom date ranges in a campaign<br>as an array. A list of Adgroup IDs. The list of ads to display for each<br>time range in a given schedule. For example display first ad in Adgroup<br>for first date range, second ad for second date range, and so on. You<br>can display more than one ad per date range by providing more than<br>one ad ID per array. For example set<br>`time_based_ad_rotation_id_blocks` to [[1], [2, 3], [1, 4]]. On the<br>first date range show ad 1, on the second date range show ad 2 and ad 3<br>and on the last date range show ad 1 and ad 4. Use with<br>`time_based_ad_rotation_intervals` to specify date ranges.<br> |
| `time_based_ad_rotation_intervals`<br><br>*list<int64>* | Date range when specific ad creative displays during a campaign.<br>Provide date ranges in an array of UNIX timestamps where each<br>timestamp represents the start time for each date range. For example a<br>3-day campaign from May 9 12am to  May 11 11:59PM PST can have three<br>date ranges, the first date range starts from May 9 12:00AM to<br>May 9 11:59PM, second date range starts from May 10 12:00AM to<br>May 10 11:59PM and last starts from  May 11 12:00AM to  May 11 11:59PM.<br>The first timestamp should match the campaign start time. The last<br>timestamp should be at least 1 hour before the campaign end time. You<br>must provide at least two date ranges. All date ranges must cover the<br>whole campaign length, so any date range cannot exceed campaign length.<br>Use with `time_based_ad_rotation_id_blocks` to specify ad creative for<br>each date range.<br> |
| `time_start`<br><br>*datetime* | Time start<br> |
| `time_stop`<br><br>*datetime* | Time stop<br> |
| `tune_for_category`<br><br>*enum{NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING, FINANCIAL_PRODUCTS_SERVICES}* | tune_for_category<br> |
| `value_rule_set_id`<br><br>*numeric string or integer* | Value Rule Set ID<br> |
| `value_rules_applied`<br><br>*boolean* | value_rules_applied<br> |

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
| 200 | Permissions error |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 2695 | The ad set creation reached its campaign group(ios14) limit. |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 2641 | Your ad includes or excludes locations that are currently restricted |
| 190 | Invalid OAuth 2.0 Access Token |
| 900 | No such application exists. |

## Updating

### Examples {#update-examples}

```html
curl -X POST \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="LINK_CLICKS"' \
  -F 'bid_amount=200' \
  -F 'targeting={
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "facebook_positions": [
         "feed"
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

To update the `end_time` of an ad set, using ISO-8601 date-time format

### PHP Business SDK
```
use FacebookAds\Object\AdSet;

$adset = new AdSet('<AD_SET_ID>');
$adset->end_time = '2013-10-02T00:00:00-0700';
$adset->update();
```

### Python Business SDK
```
from facebookads.objects import AdSet

adset = AdSet('<AD_SET_ID>')
adset[AdSet.Field.end_time] = '2013-10-02T00:00:00-0700'
adset.remote_update()
```

### cURL
```
curl \
-F "end_time=2013-10-02T00:00:00-0700" \
-F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/<AD_SET_ID>"
```

To update the status of an ad set to paused

### PHP Business SDK
```
use FacebookAds\Object\AdSet;

$adset = new AdSet('<AD_SET_ID>');
$adset->campaign_status = AdSet::STATUS_PAUSED;
$adset->update();
```

### Python Business SDK
```
from facebookads.objects import AdSet

adset = AdSet('<AD_SET_ID>')
adset[AdSet.Field.status] = AdSet.Status.paused
adset.remote_update()
```

### cURL
```
curl \
-F "campaign_status=PAUSED" \
-F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/<AD_SET_ID>"
```

### Remarks

An archived ad set can only update two fields: `name` and `campaign_status`. The `campaign_status` field can only be changed to `DELETED`.

A deleted ad set can only change its `name`.

There are two considerations to take into account when adjusting an ad set's budget value or budget type:

- When updating a set's lifetime or daily budget to a lower value, the new value must be at least 10% greater than the current amount spent already. For example: if an ad set has a $1000 lifetime budget and has spend $300 so far, the lowest new lifetime budget would be $330.

- Since `v2.4`, ad sets have a minimum required budget. Any update must take that into consideration. Check the details at the [Create Considerations](#create-considerations) section from this page.

**Note:** When using the Reservation buying type, some fields may not be available to be updated through the API.

You can't perform this operation on this endpoint.

## Deleting

### Examples {#delete-examples}

```html
curl -X DELETE \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

### /{ad_set_id}
You can delete an [AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) by making a DELETE request to [/{ad_set_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign).

#### Example

### HTTP
```
DELETE /v25.0/<AD_SET_ID>/ HTTP/1.1
Host: graph.facebook.com
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/<AD_SET_ID>/',
    array (),
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
    "/<AD_SET_ID>/",
    "DELETE",
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
    "/<AD_SET_ID>/",
    null,
    HttpMethod.DELETE,
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
                               initWithGraphPath:@"/<AD_SET_ID>/"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

### cURL
```
curl -X DELETE -G \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=DELETE&path=%3CAD_SET_ID%3E%2F&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

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
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |

## Outcome-Driven Ads Experiences {#odax}

### Example

**Outcome-Driven Ads Experiences (Engagement Outcome + `ON_PAGE` destination_type)**

```
curl -i -X POST \
  -d "name=New ODAX Adset" \
  -d "autobid=true" \
  -d "optimization_goal=PAGE_LIKES" \
  -d "destination_type=ON_PAGE" \
  -d "billing_event=IMPRESSIONS" \
  -d "daily_budget=500" \
  -d "targeting={\"geo_locations\": {\"countries\": [\"US\"]}}" \
  -d "promoted_object={\"page_id\": PAGE_ID}" \
  -d "campaign_id=CAMPAIGN_ID" \
  -d "status=PAUSED" \
  -d "access_token=ACCESS_TOKEN" \
  https://graph.facebook.com/v11.0/
  act_AD_ACCOUNT_ID/adsets
```

**Legacy**

```
curl -i -X POST \
  -d "name=New ODAX Adset" \
  -d "autobid=true" \
  -d "optimization_goal=PAGE_LIKES" \
  -d "billing_event=IMPRESSIONS" \
  -d "daily_budget=500" \
  -d "targeting={\"geo_locations\": {\"countries\": [\"US\"]}}" \
  -d "promoted_object={\"page_id\": PAGE_ID}" \
  -d "campaign_id=CAMPAIGN_ID" \
  -d "status=PAUSED" \
  -d "access_token=ACCESS_TOKEN" \
  https://graph.facebook.com/v11.0/
  act_AD_ACCOUNT_ID/adsets
```

### Restrictions
There will be new restrictions on Outcome-Driven Ads Experiences (ODAX) campaigns as outlined in the table below. Refer to the [Outcome-Driven Ads Experiences mapping table](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax-mapping) to find the new objectives and their corresponding destination types, optimization goals and promoted objects.

| ODAX Objectives | Conversion Location (L2) | Conversion Events (L2) | Optimization Goals (L2) | Legacy Objectives |
| --- | --- | --- | --- | --- |
| **Awareness**  <br>*Reach the largest number of people who are likely to remember your ad.* | N/A | N/A | Ad Recall Lift, Reach, Impressions<br><br>API enum {`AD_RECALL_LIFT`, `REACH`, `IMPRESSIONS`} | Reach, Brand Awareness |
| **Traffic**  <br>*Send people to a destination like your website, app or Shop.* | Facebook Shops (closed beta) | N/A | Link Clicks<br><br>API enum {`LINK_CLICKS`} | Traffic |
|  | Website | N/A | Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br><br>API enum {`LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Traffic |
|  | App | N/A | Link Clicks, Daily Unique Reach<br><br>API enum {`LINK_CLICKS`, `REACH`} | Traffic |
|  | Messenger | N/A | Link Clicks, Impressions, Daily Unique Reach<br><br>API enum {`LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Traffic |
|  | WhatsApp | N/A | Link Clicks, Impressions, Daily Unique Reach<br><br>API enum {`LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Traffic |
| **Engagement**  <br>*Find people likely to interact with your business online, and take actions like starting a conversation or commenting on posts.* | On Video | N/A | ThruPlay, 2 second continuous view<br><br>API enum {`THRUPLAY`, `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS`} | Video Views |
|  | On Post | N/A | Post Engagement, Impressions, Daily Unique Reach<br><br>API enum {`POST_ENGAGEMENT`, `IMPRESSIONS`, `REACH`} | Post Engagement |
|  | On Event | N/A | Event Response, Impressions, Post Engagement, Daily Unique Reach<br><br>API enum {`EVENT_RESPONSES`, `IMPRESSIONS`, `POST_ENGAGEMENT`, `REACH`} | Event Responses |
|  | Messenger | N/A | Conversations, Link Clicks<br><br>API enum {`CONVERSATIONS`, `LINK_CLICKS`} | Messages |
|  | WhatsApp | N/A | Conversations, Link Clicks<br><br>API enum {`CONVERSATIONS`, `LINK_CLICKS`} | Messages |
|  | Instagram | N/A | Conversations, Link Clicks<br><br>API enum {`CONVERSATIONS`, `LINK_CLICKS`} | Messages |
|  | Website | AddToWishlist, Contact, CustomizeProduct, Donate, FindLocation,, Schedule, Search, StartTrial, SubmitApplication, Subscribe, ViewContent | Conversions, Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br><br>API enum {`OFFSITE_CONVERSIONS`, `ONSITE_CONVERSIONS`,  `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | App | Achieve Level, Activate App, Add to Wishlist, Complete Tutorial, Contact, Customize Product, Donate, Find Location, In-App Ad Click, In-App Ad Impression, Rate, Schedule, Search, Spent Credits, Start Trial, Submit Application, Subscribe, Unlock Achievement, View Content | App Events, Link Clicks, Daily Unique Reach<br><br>API enum {`APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `REACH`} | Conversions |
|  | On Page | N/A | Page Likes<br><br>API enum {`PAGE_LIKES`} | Engagement |
| **Leads**  <br>*Find people interested in your business who are likely to share their contact information.* | Website | Lead, CompleteRegistration, Contact, FindLocation, Schedule, StartTrial, SubmitApplication, Subscribe | Conversions, Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br><br>API enum {`OFFSITE_CONVERSIONS`, `ONSITE_CONVERSIONS`,  `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | Instant Forms | N/A | Leads<br><br>API enum {`LEAD_GENERATION`, `QUALITY_LEAD`} | Lead Generation |
|  | Messenger | N/A | Leads<br><br>API enum {`LEAD_GENERATION`, `QUALITY_LEAD`} | Messages |
|  | Calls | N/A | Calls<br><br>API enum {`QUALITY_CALL`} | Lead Generation |
|  | App | Complete Registration, Complete Tutorial, Contact, Find Location, Schedule, Start Trial, Submit Application, Subscribe | App Events, Link Clicks, Daily Unique Reach<br><br>API enum {`APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `REACH`} | Conversions |
| **App Promotion**  <br>*Find people likely to install your app.* | N/A | All app events, including all custom events | Non-AAA: Link Clicks, App Installs, App Events, Value<br><br>API enum {`LINK_CLICKS`, `APP_INSTALLS`, `APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `VALUE`}<br><br>AAA: App Installs, App Installs w/ App Events, App Events, Value<br><br>API enum {`APP_INSTALLS`, `APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `VALUE`} | App Installs |
| **Sales**  <br>*Find people likely to make purchases or take other important actions online or in store.* | Website & Facebook Shops (closed beta) | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | (source of truth: same as today's Conversions objective + web and shop)<br><br>API enum {`OFFSITE_CONVERSIONS`, `VALUE`, `LINK_CLICKS`, `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | Website | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversions, Value, Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br><br>API enum {`OFFSITE_CONVERSIONS`, `VALUE`, `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | App | Purchase, Initiate Checkout, Add Payment Info, Add to Cart, Complete Registration, Donate, In-App Ad Click, In-App Ad Impression, Spent Credits, Start Trial, Subscribe, View Content | App Events, Link Clicks, Daily Unique Reach<br><br>API enum {`OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `REACH`} | Conversions |
|  | Website & App | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversions<br><br>API enum {`OFFSITE_CONVERSIONS`} | Conversions |
|  | Messenger | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversations, Conversions, Link Clicks, Impressions, Reach<br><br>API enum {`CONVERSATIONS`, `OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | WhatsApp | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversions, Link Clicks, Impressions, Reach<br><br>API enum {`OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
