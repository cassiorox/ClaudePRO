# Ad Set (Ad Campaign)
Fonte: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/
Baixado para Meta Marketing API v25.0

---

Ads and Commerce

Version

v22.0v23.0v24.0v25.0

# Ad Set

Updated:Apr 21, 2026

Beginning September 2, 2025, we will start to roll out more proactive restrictions on custom audiences and custom conversions that may suggest information not permitted under [our terms⁠](https://www.facebook.com/legal/terms/businesstools?_rdr). For example, any custom audience or custom conversions suggesting specific health conditions (e.g., “arthritis”, “diabetes”) or financial status (e.g., “credit score”, “high income”) will be flagged and prevented from being used to run ad campaigns.

**What these restrictions mean for your campaigns:**

You won’t be able to use flagged custom audiences or custom conversions when creating new campaigns.
If you have an active campaign using flagged custom audiences or custom conversions, you should promptly review and resolve the issues by following the resolution steps to avoid delivery and performance issues.

**For API developers:**

Starting September 2, 2025, if an ad set contains one or more flagged custom audiences and custom conversions, the [`issues_info` list](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign#Reading) will be populated with one issue per flagged items.
Creation and editing of ad sets that contain flagged custom audiences and custom conversions will not be blocked, but campaign delivery and performance may be impacted unless the flags are resolved.

More information on this update and how to resolve flagged custom audiences can be found [here⁠](https://www.facebook.com/business/help/1055828013359808), while information for resolving flagged custom conversions is available [here⁠](https://www.facebook.com/business/help/2455915321411996).

An ad set is a group of ads that share the same daily or lifetime budget, schedule, bid type, bid info, and targeting data. Ad sets enable you to group ads according to your criteria, and you can retrieve the ad-related statistics that apply to a set. See [Optimized CPM](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/cost-per-action-ads) and [Promoted Object](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object).

For example, create an ad set with a daily budget:

```
curl -X POST \
  -F 'name="My Reach Ad Set"' \
  -F 'optimization_goal="REACH"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'targeting={
       "geo_locations": {
         "countries": [\
           "US"\
         ]
       },
       "facebook_positions": [\
         "feed"\
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

```
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
       "facebook_positions": [\
         "feed"\
       ],
       "geo_locations": {
         "countries": [\
           "US"\
         ]
       },
       "publisher_platforms": [\
         "facebook",\
         "audience_network"\
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

### Limits

The following are the limits on ad sets

| Limit | Value |
| --- | --- |
| Maximum number of ad sets per regular ad account | 5000 non-deleted ad sets |
| Maximum number of ad sets per bulk ad account | 10000 non-deleted ad sets |
| Maximum number of ads per ad set | 50 non-archived ads |

### Housing, Employment and Credit Ads

Facebook is committed to protecting people from discrimination, and we are continually improving our ability to detect and deter potential abuse. It’s already against [our policies⁠](https://www.facebook.com/policies/ads/prohibited_content/discriminatory_practices) to discriminate by wrongfully targeting or excluding specific groups of people. As part of a [historic settlement agreement⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fnewsroom.fb.com%2Fnews%2F2019%2F03%2Fprotecting-against-discrimination-in-ads%2F&h=AUAA0tuNv1uz3JWgEuBnb1wfUhpfntzHVdL_PYWBmUiGLoDGIsXejj1qAKtBPw-ynO_U3EdozvvYiswT1p1xN-DXJiNavKKbLGs2WGzzcIaUU8v3g4mS-DJRe00yvz6Jujtbr30_TXnk5Q), we are making changes to the way we manage housing, employment and credit ads.

Advertisers must specify a `special_ad_category` for ad campaigns that market housing, employment, and credit. In doing so, the set of targeting options available for ads in these campaigns will be restricted. See [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) for more information.

### Flagged custom conversions, custom audiences and/or lookalike audiences

If an ad set contains one or more custom lookalike audiences flagged with an `operation_status` of `471`, the `issues_info` list will be populated with one issue per flagged audience as warning.

**Example**

```
{
  "effective_status": "ACTIVE",
  "issues_info": [\
    {\
      "level": "AD_SET",\
      "error_code": 2460003,\
      "error_summary": "Custom Audience is blocked",\
      "error_message": "Custom Audience is blocked: Some of this ad set’s custom audiences and/or lookalikes are blocked because they suggest the use of information (e.g., health, financial) not allowed under Meta’s terms. Go to Audience Manager for more details, and you can either review each custom audience or lookalike and remove prohibited information, or choose a different one for your ad set or create a new one and make sure it does not include potentially prohibited information. You can also request a review in Audience Manager if you think any don’t use restricted information.",\
      "error_type": "SOFT_ERROR",\
      "additional_info": "Custom Audience ID: 120231141155310247"\
    },\
    {\
      "level": "AD_SET",\
      "error_code": 2460003,\
      "error_summary": "Custom Audience is blocked",\
      "error_message": "Custom Audience is blocked: Some of this ad set’s custom audiences and/or lookalikes are blocked because they suggest the use of information (e.g., health, financial) not allowed under Meta’s terms. Go to Audience Manager for more details, and you can either review each custom audience or lookalike and remove prohibited information, or choose a different one for your ad set or create a new one and make sure it does not include potentially prohibited information. You can also request a review in Audience Manager if you think any don’t use restricted information.",\
      "error_type": "SOFT_ERROR",\
      "additional_info": "Custom Audience ID: 120232742978230247"\
    },\
    {\
      "level": "AD_SET",\
      "error_code": 2460004,\
      "error_summary": "Custom Conversion is blocked",\
      "error_message": "Custom Conversion is blocked: This ad set’s custom conversion is blocked because it suggests the use of information (e.g., health, financial) not allowed under Meta’s terms. You can’t edit this custom conversion, but you can choose a different one for this ad set or create a new one that doesn’t use prohibited information. You can also request a review if you think your custom conversion doesn’t use prohibited information.",\
      "error_type": "SOFT_ERROR",\
      "additional_info": "Custom Conversion ID: 730362226205831"\
    }\
  ],
  "id": "120228591637010247"
}
```

In addition, attempting to create or modify ad sets containing any flagged custom audience, lookalike audience or custom conversion will fail with an error. The error will contain the list of IDs for the restricted assets.

##### For flagged custom audiences

```
{
  "error": {
    "error_subcode": 246003,
    "error_data": {
      "Restricted Custom Audience IDs": [\
        "<CUSTOM_AUDIENCE_ID1>",\
        "<CUSTOM_AUDIENCE_ID2>"\
      ]
    }
    "error_user_title": "Your custom audience is currently blocked",
    "error_user_msg": "  This custom audience is blocked because it may contain information (e.g., health, financial) not allowed under Meta’s terms. Visit the audience manager to appeal this decision, edit your audience and remove prohibited information, or choose a different audience."
  },
}
```

##### For flagged custom conversions

```
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

**Review flagged audiences**: Use Audience Manager to review your custom audience along with other information included in an audience, and remove any information that is not allowed under edit the audience to comply with [Meta’s terms⁠](https://www.facebook.com/legal/terms/businesstools/).
**Create new or choose different audiences**: Alternatively, you can create a new custom audience or choose a different existing custom audience and make sure that it does not include information not allowed under our terms and use that to run campaigns.

To resolve flagged lookalike audiences:

**Resolve issues with the underlying custom audience**: If the underlying custom audience (also known as the seed audience) of your lookalike audience is flagged, you will need to resolve the issue with the underlying custom audience on which the lookalike audience is built. Please refer to the preceding section on how to resolve flagged custom audiences.
**Create new audiences**: Consider developing new lookalike audiences and make sure that they don’t include information that is not allowed under our terms.

##### Request a review

If you believe your custom audience or lookalike audience has been flagged in error and doesn’t include non-permitted information, you can request a review via Ads Manager under the campaigns table or, or in Audience Manager by clicking on individual audiences and under the summary tab of the impacted audience.

#### To resolve flagged custom conversions

If any of your custom conversions are flagged for suggesting information that is not allowed under our terms, you may want to consider the following options.

To resolve a flagged custom conversion in a new campaign creation:

**Create new custom conversion**: Use a new custom conversion and make sure that it does not include information that is not allowed under our terms.
**Choose a different custom conversion**: Select a different existing custom conversion and make sure it does not include information that is not allowed under our terms.

To resolve a flagged custom conversion in an existing campaign:

**Duplicate your campaign and select an existing custom conversion**: If you have a running campaign that is flagged due to a flagged custom conversion, consider duplicating the campaign and selecting a different custom conversion that is not flagged before publishing the new duplicated campaign. **Note:** Once the campaign is published, you cannot remove or select a different custom conversion.

##### Request a review

If you believe your custom conversion has been flagged in error and doesn’t include non-permitted information, you can request a review via Ads Manager under the campaigns table, or in Events Manager under the custom conversions page.

### Targeting European Union Ads

Beginning Tuesday, May 16, 2023 advertisers who include the European Union (EU), associated territories, or select global/worldwide in their ad targeting on Facebook and Instagram will be asked to include information about who benefits from the ad (the beneficiary) and who is paying for the ad (the payor) for each ad set. Advertisers will be prompted for this information in all ads buying surfaces including Ads Manager and the Marketing API. Beginning Wednesday, August 16, 2023, if beneficiary and payer information is not provided, the ad will not be published.

We are launching this requirement to respond to the EU Digital Services Act (DSA) which goes into full effect for Facebook and Instagram later this year.

Ad sets targeted to the EU and/or associated territories (see [here⁠](https://www.facebook.com/business/help/605021638170961/) for a complete list) are required to provide beneficiary information (who benefits from the ad running), and payer information (who pays for the ad). This applies to new ads, duplicated ads, or significantly edited ads from May 16 forward, and without the required information, the API will respond with a wrong parameter error. For convenience the advertiser can set a saved beneficiary and payor in their ad account, which will be auto-populated during ad set creation, copying, and updating targets to include EU locations and ads under existing ad seta without configured the payor and beneficiary.. For more information about the ad account level parameters, `default_dsa_payor` and `default_dsa_beneficiary`, see to the check the [Ad Account reference document](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account).

To facilitate the creation of ad sets targeting the EU, we’re offering a new API which allows developers to get a list of likely beneficiary/payer strings, based on ad account activity. See [Ad Account DSA Recommendations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/dsa_recommendations) for more information.

**Notice:**

When the default values are set in the ad account, during ad set creation, updating, and ad creation under an existing ad set, if one of them is not provided, the API will automatically fill the default value listed in the ad account. **Do not pass only one of them and expect the API to set the other one to be the same value.** For example, in the ad account settings, `default_dsa_payor` is `payor_default` and `default_dsa_beneficiary` is `beneficiary_default`. During ad set creation, if only `dsa_payor` is passed with the payor, the `dsa_beneficiary` will be automatically filled with value of `beneficiary_default` instead of `dsa_payor`.
If no saved default values are set or the values are unset, without explicitly passing the payor or beneficiary during ad set creation or when making updates, it will trigger an error and the request will fail.
The `payer` and the `beneficiary` fields are only for ad sets targeting the EU and/or associated territories.
For ad sets targeting regions other than the EU and/or associated territories, that information will not be saved even if it is provided.

To facilitate the creation of ad sets targeting the EU, we’re offering a new API which allows developers to get a list of likely beneficiary/payer strings, based on ad account activity. See [Ad Account Dsa Recommendations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/dsa_recommendations) for more information.

## Reading

An ad set is a group of ads that share the same daily or lifetime budget, schedule, bid type, bid info, and targeting data. Ad sets enable you to group ads according to your criteria, and you can retrieve the ad-related statistics that apply to a set.

The `date_preset = lifetime` parameter is disabled in Graph API v10.0 and replaced with `date_preset = maximum`, which returns a maximum of 37 months of data. For v9.0 and below, `date_preset = maximum` will be enabled on May 25, 2021, and any `lifetime` calls will default to `maximum` and return only 37 months of data.

### Examples

```
curl -X GET \
  -d 'fields="name,status"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

To retrieve date-time related fields in a UNIX timestamp format, use the `date_format` parameter:

```
curl -X GET \
  -d 'fields="id,name,start_time,end_time"' \
  -d 'date_format="U"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

#### Example

Select language

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL

* * *

```
GET /v25.0/<AD_SET_ID>/?fields=adset_schedule HTTP/1.1
Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%3CAD_SET_ID%3E%2F%3Ffields%3Dadset_schedule&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br>_enum{today, yesterday, this\_month, last\_month, this\_quarter, maximum, data\_maximum, last\_3d, last\_7d, last\_14d, last\_28d, last\_30d, last\_90d, last\_week\_mon\_sun, last\_week\_sun\_sat, last\_quarter, last\_year, this\_week\_mon\_today, this\_week\_sun\_today, this\_year}_ | Date Preset |
| `time_range`<br>_{‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD}_ | Time Range. Note if time range is invalid, it will be ignored.<br>* * *<br>`since` _datetime_<br>A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day.<br>`until` _datetime_<br>A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day.<br>Show child parameters |

#### Fields

| Field | Description |
| --- | --- |
| `id`<br>_numeric string_ | ID for the Ad Set<br>default |
| `account_id`<br>_numeric string_ | ID for the Ad Account associated with this Ad Set |
| `adlabels`<br>_[list<AdLabel>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label)_ | Ad Labels associated with this ad set |
| `adset_schedule`<br>_list<DayPart>_ | Ad set schedule, representing a delivery schedule for a single day |
| `asset_feed_id`<br>_numeric string_ | The ID of the asset feed that constains a content to create ads |
| `attribution_spec`<br>_list<AttributionSpec>_ | Conversion attribution spec used for attributing conversions for optimization. Supported window lengths differ by optimization goal and campaign objective. See [Objective, Optimization Goal and `attribution_spec`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#attribution_spec). |
| `bid_adjustments`<br>_[AdBidAdjustments](https://developers.facebook.com/docs/marketing-api/reference/ad-bid-adjustments)_ | Map of bid adjustment types to values |
| `bid_amount`<br>_unsigned int32_ | Bid cap or target cost for this ad set. The bid cap used in a _lowest cost bid strategy_ is defined as the maximum bid you want to pay for a result based on your `optimization_goal`. The target cost used in a _target cost bid strategy_ lets Facebook bid on your behalf to meet your target on average and keep costs stable as you raise budget.<br>The bid amount's unit is cents for currencies like USD, EUR, and the basic unit for currencies like JPY, KRW. The bid amount for ads with `IMPRESSION` or `REACH` as `billing_event` is per 1,000 occurrences of that event, and the bid amount for ads with other `billing_event`s is for each occurrence. |
| `bid_constraints`<br>_[AdCampaignBidConstraint](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-bid-constraint)_ | Choose bid constraints for ad set to suit your specific business goals. It usually works together with `bid_strategy` field. |
| `bid_info`<br>_map<string, unsigned int32>_ | Map of bid objective to bid value. |
| `bid_strategy`<br>_enum {LOWEST\_COST\_WITHOUT\_CAP, LOWEST\_COST\_WITH\_BID\_CAP, COST\_CAP, LOWEST\_COST\_WITH\_MIN\_ROAS}_ | Bid strategy for this ad set when you use `AUCTION` as your buying type:<br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as _automatic bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. Get your bid cap with the field `bid_amount`.<br>This strategy is also known as _manual maximum-cost bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>Notes:<br>If you enable campaign budget optimization, you should get `bid_strategy` at the parent campaign level.<br>`TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0). |
| `billing_event`<br>_enum {APP\_INSTALLS, CLICKS, IMPRESSIONS, LINK\_CLICKS, NONE, OFFER\_CLAIMS, PAGE\_LIKES, POST\_ENGAGEMENT, THRUPLAY, PURCHASE, LISTING\_INTERACTION}_ | The billing event for this ad set:<br>`APP_INSTALLS`: Pay when people install your app.<br>`CLICKS`: Pay when people click anywhere in the ad. <br>`IMPRESSIONS`: Pay when the ads are shown to people.<br>`LINK_CLICKS`: Pay when people click on the link of the ad.<br>`OFFER_CLAIMS`: Pay when people claim the offer.<br>`PAGE_LIKES`: Pay when people like your page.<br>`POST_ENGAGEMENT`: Pay when people engage with your post.<br>`VIDEO_VIEWS`: Pay when people watch your video ads for at least 10 seconds.<br>`THRUPLAY`: Pay for ads that are played to completion, or played for at least 15 seconds. |
| `brand_safety_config`<br>_BrandSafetyCampaignConfig_ | brand\_safety\_config |
| `budget_remaining`<br>_numeric string_ | Remaining budget of this Ad Set |
| `campaign`<br>_[Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group)_ | The campaign that contains this ad set |
| `campaign_active_time`<br>_numeric string_ | Campaign running length |
| `campaign_attribution`<br>_enum_ | campaign\_attribution, a new field for app ads campaign, used to indicate a campaign's attribution type, eg: SKAN or AEM |
| `campaign_id`<br>_numeric string_ | The ID of the campaign that contains this ad set |
| `configured_status`<br>_enum {ACTIVE, PAUSED, DELETED, ARCHIVED}_ | The status set at the ad set level. It can be different from the<br>effective status due to its parent campaign. Prefer using 'status'<br>instead of this. |
| `contextual_bundling_spec`<br>_ContextualBundlingSpec_ | specs of contextual bundling Ad Set setup, including signal of opt-in/out the feature |
| `created_time`<br>_datetime_ | Time when this Ad Set was created |
| `creative_sequence`<br>_list<numeric string>_ | Order of the adgroup sequence to be shown to users |
| `daily_budget`<br>_numeric string_ | The daily budget of the set defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api). |
| `daily_min_spend_target`<br>_numeric string_ | Daily minimum spend target of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. This target is not a guarantee but our best effort. |
| `daily_spend_cap`<br>_numeric string_ | Daily spend cap of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. |
| `destination_type`<br>_string_ | Destination of ads in this Ad Set.<br>Options include: `WEBSITE`, `APP`, `MESSENGER`, `INSTAGRAM_DIRECT`.<br>The `ON_AD`, `ON_POST`, `ON_VIDEO`, `ON_PAGE`, and `ON_EVENT` destination types are currently in limited beta testing. Trying to duplicate campaigns with existing destination types using these new destination types may throw an error. See the [Outcome-Driven Ads Experiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign#odax) section below for more information. |
| `dsa_beneficiary`<br>_string_ | The beneficiary of all ads in this ad set. |
| `dsa_payor`<br>_string_ | The payor of all ads in this ad set. |
| `effective_status`<br>_enum {ACTIVE, PAUSED, DELETED, CAMPAIGN\_PAUSED, ARCHIVED, IN\_PROCESS, WITH\_ISSUES}_ | The effective status of the adset. The status could be effective either<br>because of its own status, or the status of its parent campaign. `WITH_ISSUES` is available for version 3.2 or higher. `IN_PROCESS` is available for version 4.0 or higher. |
| `end_time`<br>_datetime_ | End time, in UTC UNIX timestamp |
| `frequency_control_specs`<br>_[list<AdCampaignFrequencyControlSpecs>](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-frequency-control-specs)_ | An array of frequency control specs for this ad set. Writes to this field are only available in ad sets where `REACH` and `THRUPLAY` are the performance goal. |
| `instagram_user_id`<br>_numeric string_ | Represents your Instagram account id, used for ads, including dynamic creative ads on Instagram. |
| `is_dynamic_creative`<br>_bool_ | Whether this ad set is a dynamic creative ad set. dynamic creative ad can be created only under ad set with this field set to be true. |
| `is_incremental_attribution_enabled`<br>_bool_ | Whether the campaign should use incremental attribution optimization. |
| `issues_info`<br>_[list<AdCampaignIssuesInfo>](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-issues-info)_ | Issues for this ad set that prevented it from deliverying |
| `learning_stage_info`<br>_[AdCampaignLearningStageInfo](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-learning-stage-info)_ | Info about whether the ranking or delivery system is still learning for this ad set. While the ad set is still in learning , we might unstablized delivery performances. |
| `lifetime_budget`<br>_numeric string_ | The lifetime budget of the set defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api). |
| `lifetime_imps`<br>_int32_ | Lifetime impressions. Available only for campaigns with `buying_type=FIXED_CPM` |
| `lifetime_min_spend_target`<br>_numeric string_ | Lifetime minimum spend target of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. This target is not a guarantee but our best effort. |
| `lifetime_spend_cap`<br>_numeric string_ | Lifetime spend cap of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. |
| `min_budget_spend_percentage`<br>_numeric string_ | min\_budget\_spend\_percentage |
| `multi_optimization_goal_weight`<br>_string_ | multi\_optimization\_goal\_weight |
| `name`<br>_string_ | Name of the ad set |
| `optimization_goal`<br>_enum {NONE, APP\_INSTALLS, AD\_RECALL\_LIFT, ENGAGED\_USERS, EVENT\_RESPONSES, IMPRESSIONS, LEAD\_GENERATION, QUALITY\_LEAD, LINK\_CLICKS, OFFSITE\_CONVERSIONS, PAGE\_LIKES, POST\_ENGAGEMENT, QUALITY\_CALL, REACH, LANDING\_PAGE\_VIEWS, VISIT\_INSTAGRAM\_PROFILE, ENGAGED\_PAGE\_VIEWS, VALUE, THRUPLAY, DERIVED\_EVENTS, APP\_INSTALLS\_AND\_OFFSITE\_CONVERSIONS, CONVERSATIONS, IN\_APP\_VALUE, MESSAGING\_PURCHASE\_CONVERSION, MESSAGING\_DEEP\_CONVERSATION\_AND\_FOLLOW, SUBSCRIBERS, REMINDERS\_SET, MEANINGFUL\_CALL\_ATTEMPT, PROFILE\_VISIT, PROFILE\_AND\_PAGE\_ENGAGEMENT, ADVERTISER\_SILOED\_VALUE, AUTOMATIC\_OBJECTIVE, MESSAGING\_APPOINTMENT\_CONVERSION}_ | The optimization goal this ad set is using.<br>`NONE`: Only available in read mode for campaigns created pre-v2.4.<br>`APP_INSTALLS`: Optimize for people more likely to install your app.<br>`AD_RECALL_LIFT`: Optimize for people more likely to remember seeing your ads.<br>`CLICKS`: Deprecated. Only available in read mode.<br>`ENGAGED_USERS`: Optimize for people more likely to take a particular action in your app.<br>`EVENT_RESPONSES`: Optimize for people more likely to attend your event.<br>`IMPRESSIONS`: Show the ads as many times as possible.<br>`LEAD_GENERATION`: Optimize for people more likely to fill out a lead generation form.<br>`QUALITY_LEAD`: Optimize for people who are likely to have a deeper conversation with advertisers after lead submission.<br>`LINK_CLICKS`: Optimize for people more likely to click in the link of the ad.<br>`OFFSITE_CONVERSIONS`: Optimize for people more likely to make a conversion on the site.<br>`PAGE_LIKES`: Optimize for people more likely to like your page.<br>`POST_ENGAGEMENT`: Optimize for people more likely to engage with your post.<br>`QUALITY_CALL`: Optimize for people who are likely to call the advertiser.<br>`REACH`: Optimize to reach the most unique users for each day or interval specified in `frequency_control_specs`.<br>`LANDING_PAGE_VIEWS`: Optimize for people who are most likely to click on and load your chosen landing page.<br>`VISIT_INSTAGRAM_PROFILE`: Optimize for visits to the advertiser's Instagram profile.<br>`VALUE`: Optimize for maximum total purchase value within the specified attribution window.<br>`THRUPLAY`: Optimize delivery of your ads to people who are more likely to play your ad to completion, or play it for at least 15 seconds.<br>`DERIVED_EVENTS`: Optimize for retention, which reaches people who are most likely to return to the app and open it again during a given time frame after installing. You can choose either two days, meaning the app is likely to be reopened between 24 and 48 hours after installation; or seven days, meaning the app is likely to be reopened between 144 and 168 hours after installation.<br>`APP_INSTALLS_AND_OFFSITE_CONVERSIONS`: Optimizes for people more likely to install your app and make a conversion on your site. <br>`CONVERSATIONS`: Directs ads to people more likely to have a conversation with the business. |
| `optimization_sub_event`<br>_string_ | Optimization sub event for a specific optimization goal. For example: Sound-On event for Video-View-2s optimization goal. |
| `pacing_type`<br>_list<string>_ | Defines the pacing type, standard or using ad scheduling |
| `promoted_object`<br>_[AdPromotedObject](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object)_ | The object this ad set is promoting across all its ads. |
| `recommendations`<br>_list<AdRecommendation>_ | If there are recommendations for this ad set, this field includes them. Otherwise, will not be included in the response. This field is not included in redownload mode. |
| `recurring_budget_semantics`<br>_bool_ | If this field is `true`, your daily spend may be more than your daily budget while your weekly spend will not exceed 7 times your daily budget. More details explained in the [Ad Set Budget](https://developers.facebook.com/documentation/ads-commerce/marketing-api) document. If this is `false`, your amount spent daily will not exceed the daily budget. This field is not applicable for lifetime budgets. |
| `regional_regulated_categories`<br>_list<enum>_ | This param is used to specify `regional_regulated_categories`. Currently it supports `null` and the following values:<br>TAIWAN\_FINSERV: Use this value to declare a Financial Service ad set if the ad targets Taiwan Audience<br>AUSTRALIA\_FINSERV: Use this value to declare a Financial Service ad set if the ad set targets Australia Audience<br>INDIA\_FINSERV: Use this value to declare a Securities and Investments ad set if the ad set targets India Audience<br>TAIWAN\_UNIVERSAL: Use this value to declare an ad set if it targets Taiwan Audience<br>SINGAPORE\_UNIVERSAL: Use this value to declare an ad set if it targets Singapore Audience<br>THAILAND\_UNIVERSAL: Use this value to declare an ad set if it targets Thailand Audience and you are seeing "Beneficiary/payer is missing" errors (3858634, 3858636).<br>BRAZIL\_REGULATION: Use this value to declare an Ad Set if it targets Thailand Audience and you are seeing "Beneficiary/payer is missing" errors (3858634, 3858636).<br>If an ad set is a Financial Service Ad and it targets Taiwan, it needs to declare both `TAIWAN_FINSERV` and `TAIWAN_UNIVERSAL`<br>Example: `null` or `[AUSTRALIA_FINSERV]` or `[TAIWAN_FINSERV, TAIWAN_UNIVERSAL]` |
| `regional_regulation_identities`<br>_RegionalRegulationIdentities_ | This param is used to specify regional\_regulation\_identities used to represent the ad set. Currently it supports the following fields:<br>taiwan\_finserv\_beneficiary: used for TAIWAN\_FINSERV category<br>taiwan\_finserv\_payer: used for TAIWAN\_FINSERV category<br>australia\_finserv\_beneficiary: used for AUSTRALIA\_FINSERV category<br>australia\_finserv\_payer: used for AUSTRALIA\_FINSERV category<br>india\_finserv\_beneficiary: used for INDIA\_FINSERV category<br>india\_finserv\_payer: used for INDIA\_FINSERV category<br>taiwan\_universal\_beneficiary: used for TAIWAN\_UNIVERSAL category<br>taiwan\_universal\_payer: used for TAIWAN\_UNIVERSAL category<br>singapore\_universal\_beneficiary: used for SINGAPORE\_UNIVERSAL category<br>singapore\_universal\_payer: used for SINGAPORE\_UNIVERSAL category<br>universal\_beneficiary: used for THAILAND\_UNIVERSAL category<br>universal\_payer: used for THAILAND\_UNIVERSAL category<br>universal\_beneficiary: used for BRAZIL\_REGULATION category<br>universal\_payer: used for BRAZIL\_REGULATION category<br>Example:<br>`regional_regulation_identities: {<br>"taiwan_finserv_beneficiary": <verified_identity_id>,<br>"taiwan_finserv_payer": <verified_identity_id>,<br>"taiwan_universal_beneficiary": <verified_identity_id>,<br>"taiwan_universal_payer": <verified_identity_id>,<br>}`<br>During creation and update, the passed identities fields need to correspond to declared categories. Both beneficiary and payer identities must be included, and they can use the same identity ID.<br>To update an existing ad set identities, you need to pass new values for both categories and identities to overwrite the identity id or `null` to remove existing id.<br>For example:<br>Upon creation, `regional_regulated_categories` is `[TAIWAN_FINSERV, TAIWAN_UNIVERSAL]` and `regional_regulation_identities` is<br>`regional_regulation_identities: {<br>"taiwan_finserv_beneficiary": <id_123>,<br>"taiwan_finserv_payer": <id_123>,<br>"taiwan_universal_beneficiary": <id_456>,<br>"taiwan_universal_payer": <id_456>,<br>}`<br>For update, passing `[TAIWAN_UNIVERSAL]` and<br>`regional_regulation_identities: {<br>"taiwan_finserv_beneficiary": null<br>"taiwan_finserv_payer": null,<br>"taiwan_universal_beneficiary": <id_789>,<br>"taiwan_universal_payer": <id_789>,<br>}`<br>will remove `TAIWAN_FINSERV` declaration and update the identities ID of `TAIWAN_UNIVERSAL` |
| `review_feedback`<br>_string_ | Reviews for dynamic creative ad |
| `rf_prediction_id`<br>_id_ | Reach and frequency prediction ID |
| `source_adset`<br>_[AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign)_ | The source ad set that this ad set was copied from |
| `source_adset_id`<br>_numeric string_ | The source ad set id that this ad set was copied from |
| `start_time`<br>_datetime_ | Start time, in UTC UNIX timestamp |
| `status`<br>_enum {ACTIVE, PAUSED, DELETED, ARCHIVED}_ | The status set at the ad set level. It can be different from the<br>effective status due to its parent campaign. The field returns the same<br>value as `configured_status`, and is the suggested one to use. |
| `targeting`<br>_Targeting_ | Targeting |
| `targeting_optimization_types`<br>_list<KeyValue:string,int32>_ | Targeting options that are relaxed and used as a signal for optimization |
| `time_based_ad_rotation_id_blocks`<br>_list<list<integer>>_ | Specify ad creative that displays at custom date ranges in a campaign<br>as an array. A list of Adgroup IDs. The list of ads to display for each<br>time range in a given schedule. For example display first ad in Adgroup<br>for first date range, second ad for second date range, and so on. You<br>can display more than one ad per date range by providing more than<br>one ad ID per array. For example set<br>`time_based_ad_rotation_id_blocks` to \[\[1\], \[2, 3\], \[1, 4\]\]. On the<br>first date range show ad 1, on the second date range show ad 2 and ad 3<br>and on the last date range show ad 1 and ad 4. Use with<br>`time_based_ad_rotation_intervals` to specify date ranges. |
| `time_based_ad_rotation_intervals`<br>_list<unsigned int32>_ | Date range when specific ad creative displays during a campaign.<br>Provide date ranges in an array of UNIX timestamps where each<br>timestamp represents the start time for each date range. For example a<br>3-day campaign from May 9 12am to May 11 11:59PM PST can have three<br>date ranges, the first date range starts from May 9 12:00AM to<br>May 9 11:59PM, second date range starts from May 10 12:00AM to<br>May 10 11:59PM and last starts from May 11 12:00AM to May 11 11:59PM.<br>The first timestamp should match the campaign start time. The last<br>timestamp should be at least 1 hour before the campaign end time. You<br>must provide at least two date ranges. All date ranges must cover the<br>whole campaign length, so any date range cannot exceed campaign length.<br>Use with `time_based_ad_rotation_id_blocks` to specify ad creative for<br>each date range. |
| `updated_time`<br>_datetime_ | Time when the Ad Set was updated |
| `use_new_app_click`<br>_bool_ | If set, allows Mobile App Engagement ads to optimize for LINK\_CLICKS |
| `value_rule_set_id`<br>_numeric string_ | value\_rule\_set\_id |

#### Edges

| Edge | Description |
| --- | --- |
| [`activities`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/activities)<br>_Edge<AdActivity>_ | The activities of this ad set |
| [`ad_studies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/ad_studies)<br>_Edge<AdStudy>_ | The ad studies containing this ad set |
| [`adcreatives`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/adcreatives)<br>_Edge<AdCreative>_ | The creatives of this ad set |
| [`adrules_governed`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/adrules_governed)<br>_Edge<AdRule>_ | Ad rules that govern this ad set - by default, this only returns rules that either directly mention the ad set by id or indirectly through the set `entity_type` |
| [`ads`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/ads)<br>_Edge<Adgroup>_ | The ads under this ad set |
| [`asyncadrequests`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/asyncadrequests)<br>_Edge<AdAsyncRequest>_ | Async ad requests for this ad set |
| [`copies`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/copies)<br>_Edge<AdCampaign>_ | The copies of this ad set |
| [`delivery_estimate`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/delivery_estimate)<br>_Edge<AdCampaignDeliveryEstimate>_ | The delivery estimate for this ad set |
| [`message_delivery_estimate`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/message_delivery_estimate)<br>_Edge<MessageDeliveryEstimate>_ | Delivery estimation of the marketing message campaign |
| [`targetingsentencelines`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/targetingsentencelines)<br>_Edge<TargetingSentenceLine>_ | The targeting description sentence for this ad set |

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

For v20.0+, the Impressions optimization goal is deprecated for the legacy Post Engagement objective and the `ON_POST` destination\_type.

### Examples

Validate an ad set with a daily budget where the campaign objective is set to `APP_INSTALLS`.

```
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
       "device_platforms": [\
         "mobile"\
       ],
       "facebook_positions": [\
         "feed"\
       ],
       "geo_locations": {
         "countries": [\
           "US"\
         ]
       },
       "publisher_platforms": [\
         "facebook",\
         "audience_network"\
       ],
       "user_os": [\
         "IOS"\
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

### Considerations

#### Bid/Budget Validations

**Note:**

All values in this section are in US Dollars.

Differenct currencies have different minimum daily budget limits.

Minimum values are defined in terms of the daily budget but apply to lifetime budgets as well.

Minimum budget takes the total spent budget into account.

When creating an ad set, there will be a minimum budget for different billing events (Clicks, Impressions, Actions). If the minimum daily budget is $5, a campaign lasting 5 days will need at least $25 for budget.

Budget amounts shown are for illustrative purposes only and can change based on situation.

If `bid_strategy` is set to `LOWEST_COST_WITHOUT_CAP` in the ad set:

| Billing Event | Minimum Daily Budget |
| --- | --- |
| Impressions | $0.50 |
| Clicks/Likes/Video Views | $2.50 |
| Low-frequency Actions<br>(Includes mobile app installs, offer claims, or canvas app installs) | $40<br>**Important:** This minimum daily budget is the same for all countries. |

If `bid_strategy` is set to `LOWEST_COST_WITH_BID_CAP` in the ad set:

| Billing Event | Minimum Daily Budget |
| --- | --- |
| Impressions | At least the `bid_amount`. For example, if the bid amount is $10, then $10 will be the minimum budget required. |
| Clicks/Actions | 5x the `bid_amount` for a Click or Action. For example, if the bid amount is $5 per click/action, then $25 will be the minimum budget required. |

Budgets in non-USD currencies will be converted and validated upon time of ad set creation.

For ads belonging to ad accounts from countries in the list below, the minimum values are 2x the ones in the tables. For example, if the billing event is an Impression, the minimum daily budget is $0.50, but in the the following countries the minimum would be $1.00:

Australia, Austria, Belgium, Canada, Denmark, Finland, France, Germany, Greece, Hong Kong, Israel, Italy, Japan, Netherlands, New Zealand, Norway, Singapore, South Korea, Spain, Sweden, Switzerland, Taiwan, United Kingdom, United States of America.

The only exception to this rule are Low-Frequency Actions when `bid_strategy` is `LOWEST_COST_WITHOUT_CAP`.

#### Locale targeted page post

If you promote a Page post which has been targeted by locale the ad set targeting must include the same, or a subset of, locale targeting as the Page post.

E.g. if the Page post is targeted at locales 6 (US English) and 24 (UK English), then the ad set must be targeted at one or more of the same locales.

#### Mobile App Ads

Mobile app ad sets should

be used in conjunction with [targeting spec](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#mobile) fields `user_device` and `user_os`
have a `MOBILE_APP_*` objective on the [campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group)

#### Desktop App Ads

Desktop app ad sets must

include a [targeting spec](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting) of either

`'page_types':['desktopfeed']` or

`'page_types':['rightcolumn']` or

`'page_types':['desktop']` along with the other targeting options you have selected.
include a `CANVAS_APP_*` objective

#### Lookalike Expansion

Beginning with v13.0, for newly created ad sets that optimize for value, conversions, or app events, lookalike expansion will be turned on by default and cannot be disabled. When getting an ad set that optimizes for value, conversions, or app events, we will return a new lookalike property in the `targeting_optimization_types` map that indicates lookalike expansion is enabled and complements the existing `detailed_targeting` property for the detailed targeting expansion.

#### Targeting DSA Regulated Locations (EU)

For ad sets targeting the EU and/or associated territories, the `dsa_payor` and `dsa_beneficiary` fields are required. The information provided in these 2 fields will be shown to end users to indicate who is paying for the ad and who is the beneficiary of the ad.

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
| `dsa_payor`<br>string (max 512 char) | The payor of all ads in this ad set. |
| `dsa_beneficiary`<br>string (max 512 char) | The beneficiary of all ads in this ad set. |

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

### /{ad\_set\_id}/copies

You can make a POST request to _copies_ edge from the following paths:

[/{ad\_set\_id}/copies](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/copies)

When posting to this edge, an [AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `campaign_id`<br>_numeric string or integer_ | Single ID of a campaign to make parent of the copy. The copy inherits all campaign settings, such as budget from the parent.Ignore if you want to keep the copy under the original campaign parent. |
| `deep_copy`<br>_boolean_ | **Default value:**`false`<br>Whether to copy all the child ads. Limits: the total number of children ads to copy should not exceed 3 for a synchronous call and 51 for an asynchronous call. |
| `end_time`<br>_datetime_ | The end time of the set, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. When creating a set with a daily budget, specify `end_time=0` to set the set to be ongoing without end date. If not set, the copied adset will inherit the end time from the original set |
| `rename_options`<br>_JSON or object-like arrays_ | Rename options<br>* * *<br>`rename_strategy` _enum {DEEP\_RENAME, ONLY\_TOP\_LEVEL\_RENAME, NO\_RENAME}_<br>**Default value:**`ONLY_TOP_LEVEL_RENAME`<br>`DEEP_RENAME`: will change this object's name and children's names in the copied object. `ONLY_TOP_LEVEL_RENAME`: will change the this object's name but won't change the children's name in the copied object. `NO_RENAME`: will change no name in the copied object<br>`rename_prefix` _string_<br>A prefix to copy names. Defaults to null if not provided.<br>`rename_suffix` _string_<br>A suffix to copy names. Defaults to null if not provided and appends a localized string of `- Copy` based on the ad account locale.<br>Show child parameters |
| `start_time`<br>_datetime_ | The start time of the set, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp. If not set, the copied adset will inherit the start time from the original set |
| `status_option`<br>_enum {ACTIVE, PAUSED, INHERITED\_FROM\_SOURCE}_ | **Default value:**`PAUSED`<br>`ACTIVE`: the copied adset will have active status. `PAUSED`: the copied adset will have paused status. `INHERITED_FROM_SOURCE`: the copied adset will have the status from the original set. |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by _copied\_adset\_id_ in the return type.

```
Struct  {
copied_adset_id: numeric string,
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
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 2695 | The ad set creation reached its campaign group(ios14) limit. |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |

* * *

### /act\_{ad\_account\_id}/adsets

You can make a POST request to _adsets_ edge from the following paths:

[/act\_{ad\_account\_id}/adsets](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adsets)

When posting to this edge, an [AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) will be created.

#### Example

Select language

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL

* * *

```
POST /v25.0/act_<AD_ACCOUNT_ID>/adsets HTTP/1.1
Host: graph.facebook.com

name=My+First+Adset&lifetime_budget=20000&start_time=2026-05-12T10%3A45%3A09-0700&end_time=2026-05-22T10%3A45%3A09-0700&campaign_id=%3CAD_CAMPAIGN_ID%3E&bid_amount=100&billing_event=LINK_CLICKS&optimization_goal=LINK_CLICKS&targeting=%7B%22facebook_positions%22%3A%5B%22feed%22%5D%2C%22geo_locations%22%3A%7B%22countries%22%3A%5B%22US%22%5D%7D%2C%22publisher_platforms%22%3A%5B%22facebook%22%2C%22audience_network%22%5D%7D&status=PAUSED
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fadsets%3Fname%3DMy%2BFirst%2BAdset%26lifetime_budget%3D20000%26start_time%3D2026-05-12T10%253A45%253A09-0700%26end_time%3D2026-05-22T10%253A45%253A09-0700%26campaign_id%3D%253CAD_CAMPAIGN_ID%253E%26bid_amount%3D100%26billing_event%3DLINK_CLICKS%26optimization_goal%3DLINK_CLICKS%26targeting%3D%257B%2522facebook_positions%2522%253A%255B%2522feed%2522%255D%252C%2522geo_locations%2522%253A%257B%2522countries%2522%253A%255B%2522US%2522%255D%257D%252C%2522publisher_platforms%2522%253A%255B%2522facebook%2522%252C%2522audience_network%2522%255D%257D%26status%3DPAUSED&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `adlabels`<br>_list<Object>_ | Specifies list of labels to be associated with this object. This field is optional |
| `adset_schedule`<br>_list<Object>_ | Ad set schedule, representing a delivery schedule for a single day<br>* * *<br>`start_minute` _int64_<br>A 0 based minute of the day representing when the schedule starts<br>required<br>`end_minute` _int64_<br>A 0 based minute of the day representing when the schedule ends<br>required<br>`days` _list<int64>_<br>Array of ints representing which days the schedule is active. Valid values are 0-6 with 0 representing Sunday, 1 representing Monday, ... and 6 representing Saturday.<br>required<br>`timezone_type` _enum {USER, ADVERTISER}_<br>**Default value:**`USER`<br>Show child parameters |
| `attribution_spec`<br>_list<JSON object>_ | Conversion attribution spec used for attributing conversions for optimization. Supported window lengths differ by optimization goal and campaign objective.<br>* * *<br>`event_type` _enum {CLICK\_THROUGH, VIEW\_THROUGH, ENGAGED\_VIDEO\_VIEW}_ <br>required<br>`window_days` _int64_ <br>required<br>`weight` _float_<br>**Default value:**`100`<br>Show child parameters |
| `automatic_manual_state`<br>_enum{UNSET, AUTOMATIC, MANUAL}_ | automatic\_manual\_state |
| `bid_amount`<br>_integer_ | Bid cap or target cost for this ad set. The bid cap used in a _lowest cost bid strategy_ is defined as the maximum bid you want to pay for a result based on your `optimization_goal`. The target cost used in a _target cost bid strategy_ lets Facebook bid to meet your target on average and keep costs stable as you spend. If an ad level `bid_amount` is specified, updating this value will overwrite the previous ad level bid. Unless you are using [Reach and Frequency](https://developers.facebook.com/docs/marketing-api/reachandfrequency), `bid_amount` is required if `bid_strategy` is set to `LOWEST_COST_WITH_BID_CAP` or `COST_CAP`.<br>The bid amount's unit is cents for currencies like USD, EUR, and the basic unit for currencies like JPY, KRW. The bid amount for ads with `IMPRESSION` or `REACH` as `billing_event` is per 1,000 occurrences, and has to be at least 2 US cents or more. For ads with other `billing_event`s, the bid amount is for each occurrence, and has a minimum value 1 US cents. The minimum bid amounts of other currencies are of similar value to the US Dollar values provided. |
| `bid_strategy`<br>_enum{LOWEST\_COST\_WITHOUT\_CAP, LOWEST\_COST\_WITH\_BID\_CAP, COST\_CAP, LOWEST\_COST\_WITH\_MIN\_ROAS}_ | Choose bid strategy for this ad set to suit your specific business goals.<br>Each strategy has tradeoffs and may be available for certain `optimization_goal`s:<br>`LOWEST_COST_WITHOUT_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` without limiting your bid amount. This is the best strategy<br>if you care most about cost efficiency. However with this strategy it may be harder to get<br>stable average costs as you spend. This strategy is also known as _automatic bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>`LOWEST_COST_WITH_BID_CAP`: Designed to get the most results for your budget based on<br>your ad set `optimization_goal` while limiting actual bid to your specified<br>amount. With a bid cap you have more control over your<br>cost per actual optimization event. However if you set a limit which is too low you may<br>get less ads delivery. If you select this, you must provide<br>a bid cap with the `bid_amount` field.<br>Note: during creation this bid strategy is set if you provide `bid_amount` only.<br>This strategy is also known as _manual maximum-cost bidding_.<br>Learn more in [Ads Help Center, About bid strategies: Lowest cost⁠](https://www.facebook.com/business/help/721453268045071).<br>Notes:<br>If you enable campaign budget optimization, you should set `bid_strategy` at the parent campaign level.<br>`TARGET_COST` bidding strategy has been deprecated with [Marketing API v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0). |
| `billing_event`<br>_enum{APP\_INSTALLS, CLICKS, IMPRESSIONS, LINK\_CLICKS, NONE, OFFER\_CLAIMS, PAGE\_LIKES, POST\_ENGAGEMENT, THRUPLAY, PURCHASE, LISTING\_INTERACTION}_ | The billing event that this ad set is using:<br>APP\_INSTALLS: Pay when people install your app.<br>CLICKS: Deprecated.<br>IMPRESSIONS: Pay when the ads are shown to people.<br>LINK\_CLICKS: Pay when people click on the link of the ad.<br>OFFER\_CLAIMS: Pay when people claim the offer.<br>PAGE\_LIKES: Pay when people like your page.<br>POST\_ENGAGEMENT: Pay when people engage with your post.<br>VIDEO\_VIEWS: Pay when people watch your video ads for at least 10 seconds.<br>THRUPLAY: Pay for ads that are played to completion, or played for at least 15 seconds. |
| `budget_schedule_specs`<br>_list<JSON or object-like arrays>_ | Initial high demand periods to be created with the ad set.<br>Provide list of `time_start`, `time_end`,`budget_value`, and `budget_value_type`.<br>For example,<br>-F 'budget\_schedule\_specs=\[{<br>"time\_start":1699081200,<br>"time\_end":1699167600,<br>"budget\_value":100,<br>"budget\_value\_type":"ABSOLUTE"<br>}\]'<br>See [High Demand Period](https://developers.facebook.com/docs/graph-api/reference/high-demand-period) for more details on each field.<br>* * *<br>`id` _int64_<br>`time_start` _datetime_<br>`time_end` _datetime_<br>`budget_value` _int64_<br>`budget_value_type` _enum{ABSOLUTE, MULTIPLIER}_<br>`recurrence_type` _enum{ONE\_TIME, WEEKLY}_<br>`weekly_schedule` _list<JSON or object-like arrays>_ <br>* * *<br>`days` _list<int64>_<br>`minute_start` _int64_<br>`minute_end` _int64_<br>`timezone_type` _string_<br>Show child parameters<br>Show child parameters |
| `budget_source`<br>_enum{NONE, RMN}_ | budget\_source |
| `budget_split_set_id`<br>_numeric string or integer_ | budget\_split\_set\_id |
| `campaign_attribution`<br>_enum{}_ | campaign\_attribution |
| `campaign_id`<br>_numeric string or integer_ | The ad campaign you wish to add this ad set to. |
| `campaign_spec`<br>_Campaign spec_ | Provide `name`, `objective` and `buying_type` for a campaign you want to create. Otherwise you need to provide `campaign_id` for an existing ad campaign. For example:<br>-F 'campaign\_spec={<br>"name": "Inline created campaign",<br>"objective": "CONVERSIONS",<br>"buying\_type": "AUCTION"<br>}'<br>Please refer to the [Outcome-Driven Ads Experiences mapping table](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax-mapping) to find new objectives and their corresponding destination types, optimization goals and promoted objects. |
| `contextual_bundling_spec`<br>_Object_ | settings of Contextual Bundle to support ads serving in Facebook contextual surfaces<br>* * *<br>`status` _enum{OPT\_OUT, OPT\_IN}_<br>Show child parameters |
| `cost_bidding_mode`<br>_enum{VOLUME\_FOCUSED, BALANCED, COST\_FOCUSED}_ | cost\_bidding\_mode |
| `creative_sequence`<br>_list<numeric string or integer>_ | Order of the adgroup sequence to be shown to users |
| `daily_budget`<br>_int64_ | The daily budget defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api), allowed only for ad sets with a duration (difference between `end_time` and `start_time`) longer than 24 hours. <br>Either `daily_budget` or `lifetime_budget` must be greater than 0. |
| `daily_imps`<br>_int64_ | Daily impressions. Available only for campaigns with `buying_type=FIXED_CPM` |
| `daily_min_spend_target`<br>_int64_ | Daily minimum spend target of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. This target is not a guarantee but our best effort. |
| `daily_spend_cap`<br>_int64_ | Daily spend cap of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. Set the value to 922337203685478 to remove the spend cap. |
| `destination_type`<br>_enum{WEBSITE, APP, MESSENGER, APPLINKS\_AUTOMATIC, WHATSAPP, INSTAGRAM\_DIRECT, FACEBOOK, MESSAGING\_MESSENGER\_WHATSAPP, MESSAGING\_INSTAGRAM\_DIRECT\_MESSENGER, MESSAGING\_INSTAGRAM\_DIRECT\_MESSENGER\_WHATSAPP, MESSAGING\_INSTAGRAM\_DIRECT\_WHATSAPP, SHOP\_AUTOMATIC, ON\_AD, ON\_POST, ON\_EVENT, ON\_VIDEO, ON\_PAGE, INSTAGRAM\_PROFILE, FACEBOOK\_PAGE, INSTAGRAM\_PROFILE\_AND\_FACEBOOK\_PAGE, INSTAGRAM\_LIVE, FACEBOOK\_LIVE, IMAGINE}_ | Destination of ads in this Ad Set. Options include: Website, App, Messenger, `INSTAGRAM_DIRECT`, `INSTAGRAM_PROFILE`. |
| `dsa_beneficiary`<br>_string_ | dsa\_beneficiary |
| `dsa_payor`<br>_string_ | dsa\_payor |
| `end_time`<br>_datetime_ | End time, required when `lifetime_budget` is specified. e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. When creating a set with a daily budget, specify `end_time=0` to set the set to be ongoing and have no end date. UTC UNIX timestamp |
| `execution_options`<br>_list<enum{validate\_only, include\_recommendations}>_ | **Default value:**`Set`<br>An execution setting<br>`validate_only`: when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. <br>`include_recommendations`: this option cannot be used by itself. When this option is used, recommendations for ad object's configuration will be included. A separate section [recommendations](https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation) will be included in the response, but only if recommendations for this specification exist.<br>If the call passes validation or review, response will be `{"success": true}`. If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review. |
| `existing_customer_budget_percentage`<br>_int64_ | existing\_customer\_budget\_percentage |
| `frequency_control_specs`<br>_list<Object>_ | An array of frequency control specs for this ad set. Writes to this field are only available in ad sets where `REACH` and `THRUPLAY` are the performance goal.<br>* * *<br>`event` _enum{IMPRESSIONS, VIDEO\_VIEWS, VIDEO\_VIEWS\_2S, VIDEO\_VIEWS\_15S}_<br>Event name, only `IMPRESSIONS` currently.<br>required<br>`interval_days` _integer_<br>Interval period in days, between 1 and 90<br>(inclusive)<br>required<br>`max_frequency` _integer_<br>The maximum frequency, between 1 and 90<br>(inclusive)<br>required<br>`type` _enum{NONE, CAP, TARGET}_<br>Show child parameters |
| `is_dc_follow_optimized`<br>_boolean_ | is\_dc\_follow\_optimized |
| `is_dynamic_creative`<br>_boolean_ | Indicates the ad set must only be used for dynamic creatives. Dynamic creative ads can be created in this ad set. Defaults to `false` |
| `is_sac_cfca_terms_certified`<br>_boolean_ | is\_sac\_cfca\_terms\_certified |
| `lifetime_budget`<br>_int64_ | Lifetime budget, defined in your [account currency](https://developers.facebook.com/documentation/ads-commerce/marketing-api). If specified, you must also specify an `end_time`.<br>Either `daily_budget` or `lifetime_budget` must be greater than 0. |
| `lifetime_imps`<br>_int64_ | Lifetime impressions. Available only for campaigns with `buying_type=FIXED_CPM` |
| `lifetime_min_spend_target`<br>_int64_ | Lifetime minimum spend target of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. This target is not a guarantee but our best effort. |
| `lifetime_spend_cap`<br>_int64_ | Lifetime spend cap of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. Set the value to 922337203685478 to remove the spend cap. |
| `max_budget_spend_percentage`<br>_int64_ | max\_budget\_spend\_percentage |
| `min_budget_spend_percentage`<br>_int64_ | min\_budget\_spend\_percentage |
| `multi_event_conversion_attribution_window_seconds`<br>_int64_ | multi\_event\_conversion\_attribution\_window\_seconds |
| `multi_optimization_goal_weight`<br>_enum{UNDEFINED, BALANCED, PREFER\_INSTALL, PREFER\_EVENT}_ | multi\_optimization\_goal\_weight |
| `name`<br>_string_ | Ad set name, max length of 400 characters.<br>required<br>supports emoji |
| `optimization_goal`<br>_enum{NONE, APP\_INSTALLS, AD\_RECALL\_LIFT, ENGAGED\_USERS, EVENT\_RESPONSES, IMPRESSIONS, LEAD\_GENERATION, QUALITY\_LEAD, LINK\_CLICKS, OFFSITE\_CONVERSIONS, PAGE\_LIKES, POST\_ENGAGEMENT, QUALITY\_CALL, REACH, LANDING\_PAGE\_VIEWS, VISIT\_INSTAGRAM\_PROFILE, ENGAGED\_PAGE\_VIEWS, VALUE, THRUPLAY, DERIVED\_EVENTS, APP\_INSTALLS\_AND\_OFFSITE\_CONVERSIONS, CONVERSATIONS, IN\_APP\_VALUE, MESSAGING\_PURCHASE\_CONVERSION, MESSAGING\_DEEP\_CONVERSATION\_AND\_FOLLOW, SUBSCRIBERS, REMINDERS\_SET, MEANINGFUL\_CALL\_ATTEMPT, PROFILE\_VISIT, PROFILE\_AND\_PAGE\_ENGAGEMENT, ADVERTISER\_SILOED\_VALUE, AUTOMATIC\_OBJECTIVE, MESSAGING\_APPOINTMENT\_CONVERSION}_ | What the ad set is optimizing for. <br>`APP_INSTALLS`: Will optimize for people more likely to install your app.<br>`ENGAGED_USERS`: Will optimize for people more likely to take a particular action in your app.<br>`EVENT_RESPONSES`: Will optimize for people more likely to attend your event.<br>`IMPRESSIONS`: Will show the ads as many times as possible.<br>`LEAD_GENERATION`: Will optimize for people more likely to fill out a lead generation form.<br>`LINK_CLICKS`: Will optimize for people more likely to click in the link of the ad.<br>`OFFER_CLAIMS`: Will optimize for people more likely to claim the offer.<br>`OFFSITE_CONVERSIONS`: Will optimize for people more likely to make a conversion in the site<br>`PAGE_ENGAGEMENT`: Will optimize for people more likely to engage with your page.<br>`PAGE_LIKES`: Will optimize for people more likely to like your page.<br>`POST_ENGAGEMENT`: Will optimize for people more likely to engage with your post.<br>`REACH`: Optimize to reach the most unique users of each day or interval specified in `frequency_control_specs`.<br>`SOCIAL_IMPRESSIONS`: Increase the number of impressions with social context. For example, with the names of one or more of the user's friends attached to the ad who have already liked the page or installed the app.<br>`VALUE`: Will optimize for maximum total purchase value within the specified attribution window.<br>`THRUPLAY`: Will optimize delivery of your ads to people are more likely to play your ad to completion, or play it for at least 15 seconds.<br>`AD_RECALL_LIFT`: Optimize for people more likely to remember seeing your ads.<br>`VISIT_INSTAGRAM_PROFILE`: Optimize for visits to the advertiser's instagram profile. |
| `optimization_sub_event`<br>_enum{NONE, VIDEO\_SOUND\_ON, TRIP\_CONSIDERATION, TRAVEL\_INTENT, TRAVEL\_INTENT\_NO\_DESTINATION\_INTENT, TRAVEL\_INTENT\_BUCKET\_01, TRAVEL\_INTENT\_BUCKET\_02, TRAVEL\_INTENT\_BUCKET\_03, TRAVEL\_INTENT\_BUCKET\_04, TRAVEL\_INTENT\_BUCKET\_05, POST\_INTERACTION}_ | Optimization sub event for a specific optimization goal (ex: Sound-On event for Video-View-2s optimization goal) |
| `pacing_type`<br>_list<string>_ | Defines the pacing type, standard by default or using [ad scheduling](https://developers.facebook.com/docs/marketing-api/adset/pacing) |
| `promoted_object`<br>_Object_ | The object this ad set is promoting across all its ads.<br>Required with certain campaign objectives.<br>**CONVERSIONS** <br>`pixel_id` (Conversion pixel ID)<br>`pixel_id` (Facebook pixel ID) and `custom_event_type`<br>`pixel_id` (Facebook pixel ID) and `pixel_rule` and `custom_event_type`<br>`event_id` (Facebook event ID) and `custom_event_type`<br>`application_id`, `object_store_url`, and `custom_event_type` for<br>mobile app events<br>`offline_conversion_data_set_id` (Offline dataset ID) and<br>`custom_event_type` for offline conversions<br>**PAGE\_LIKES** <br>`page_id`<br>**OFFER\_CLAIMS** <br>`page_id`<br>**LINK\_CLICKS** <br>`application_id` and `object_store_url` for mobile app or Canvas app engagement link clicks<br>**APP\_INSTALLS** <br>`application_id` and `object_store_url`<br>**if the `optimization_goal` is `OFFSITE_CONVERSIONS`** <br>`application_id`, `object_store_url`, and `custom_event_type` (Standard Events)<br>`application_id`, `object_store_url`, `custom_event_type = OTHER` and `custom_event_str` (Custom Events)<br>**PRODUCT\_CATALOG\_SALES** <br>`product_set_id`<br>`product_set_id` and `custom_event_type`<br>When `optimization_goal` is `LEAD_GENERATION`, `page_id` needs to be passed as promoted\_object.<br>Please refer to the [Outcome-Driven Ads Experiences mapping table](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#odax-mapping) to find new objectives and their corresponding destination types, optimization goals and promoted objects.<br>* * *<br>`application_id` _int_<br>The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement<br>`pixel_id` _numeric string or integer_<br>The ID of a Facebook conversion pixel. Used with offsite conversion campaigns.<br>`custom_event_type` _enum{AD\_IMPRESSION, RATE, TUTORIAL\_COMPLETION, CONTACT, CUSTOMIZE\_PRODUCT, DONATE, FIND\_LOCATION, SCHEDULE, START\_TRIAL, SUBMIT\_APPLICATION, SUBSCRIBE, ADD\_TO\_CART, ADD\_TO\_WISHLIST, INITIATED\_CHECKOUT, ADD\_PAYMENT\_INFO, PURCHASE, LEAD, COMPLETE\_REGISTRATION, CONTENT\_VIEW, SEARCH, SERVICE\_BOOKING\_REQUEST, MESSAGING\_CONVERSATION\_STARTED\_7D, LEVEL\_ACHIEVED, ACHIEVEMENT\_UNLOCKED, SPENT\_CREDITS, LISTING\_INTERACTION, D2\_RETENTION, D7\_RETENTION, OTHER}_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`object_store_url` _URL_<br>The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application\_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br>`object_store_urls` _list<URL>_<br>The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application\_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign.<br>`offer_id` _numeric string or integer_<br>The ID of an Offer from a Facebook Page.<br>`page_id` _Page ID_<br>The ID of a Facebook Page<br>`product_catalog_id` _numeric string or integer_<br>The ID of a Product Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br>`product_item_id` _numeric string or integer_<br>The ID of the product item.<br>`job_listing_id` _numeric string or integer_<br>The ID of the marketplace job listing.<br>`instagram_profile_id` _numeric string or integer_<br>The ID of the instagram profile id.<br>`product_set_id` _numeric string or integer_<br>The ID of a Product Set within an Ad Set level Product<br>Catalog. Used with<br>[Dynamic Product Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads).<br>`event_id` _numeric string or integer_<br>The ID of a Facebook Event<br>`offline_conversion_data_set_id` _numeric string or integer_<br>The ID of the offline dataset.<br>`fundraiser_campaign_id` _numeric string or integer_<br>The ID of the fundraiser campaign.<br>`custom_event_str` _string_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`mcme_conversion_id` _numeric string or integer_<br>The ID of a MCME conversion.<br>`conversion_goal_id` _numeric string or integer_<br>The ID of a Conversion Goal.<br>`offsite_conversion_event_id` _numeric string or integer_<br>The ID of a Offsite Conversion Event<br>`boosted_product_set_id` _numeric string or integer_<br>The ID of the Boosted Product Set within an Ad Set level Product<br>Catalog. Should only be present when the advertiser has<br>opted into Product Set Boosting.<br>`lead_ads_form_event_source_type` _enum{inferred, meta\_source, offsite\_crm, offsite\_web, onsite\_crm, onsite\_crm\_single\_event, onsite\_clo\_dep\_aet, onsite\_web, onsite\_p2b\_call, onsite\_messaging, qualified\_lead\_file}_<br>The event source of lead ads form.<br>`lead_ads_custom_event_type` _enum{AD\_IMPRESSION, RATE, TUTORIAL\_COMPLETION, CONTACT, CUSTOMIZE\_PRODUCT, DONATE, FIND\_LOCATION, SCHEDULE, START\_TRIAL, SUBMIT\_APPLICATION, SUBSCRIBE, ADD\_TO\_CART, ADD\_TO\_WISHLIST, INITIATED\_CHECKOUT, ADD\_PAYMENT\_INFO, PURCHASE, LEAD, COMPLETE\_REGISTRATION, CONTENT\_VIEW, SEARCH, SERVICE\_BOOKING\_REQUEST, MESSAGING\_CONVERSATION\_STARTED\_7D, LEVEL\_ACHIEVED, ACHIEVEMENT\_UNLOCKED, SPENT\_CREDITS, LISTING\_INTERACTION, D2\_RETENTION, D7\_RETENTION, OTHER}_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`lead_ads_custom_event_str` _string_<br>The event from an App Event of a mobile app,<br>not in the standard event list.<br>`lead_ads_offsite_conversion_type` _enum{default, clo}_<br>The offsite conversion type for lead ads<br>`value_semantic_type` _enum {VALUE, MARGIN, LIFETIME\_VALUE}_<br>The semantic of the event value to be using for optimization<br>`variation` _enum {OMNI\_CHANNEL\_SHOP\_AUTOMATIC\_DATA\_COLLECTION, PRODUCT\_SET\_AND\_APP, PRODUCT\_SET\_AND\_IN\_STORE, PRODUCT\_SET\_AND\_OMNICHANNEL, PRODUCT\_SET\_AND\_PHONE\_CALL, PRODUCT\_SET\_AND\_WEBSITE, PRODUCT\_SET\_AND\_WEBSITE\_AND\_PHONE\_CALL, PRODUCT\_SET\_WEBSITE\_APP\_AND\_INSTORE}_<br>Variation of the promoted object for a PCA ad<br>`passback_pixel_id` _numeric string or integer_<br>ID of the pixel used for tracking passback events<br>`passback_application_id` _numeric string or integer_<br>ID of the application used for tracking passback events<br>`product_set_optimization` _enum{enabled, disabled}_<br>Enum defining whether or not the ad should be optimized for the promoted product set<br>`full_funnel_objective` _enum{OFFER\_CLAIMS, PAGE\_LIKES, EVENT\_RESPONSES, POST\_ENGAGEMENT, WEBSITE\_CONVERSIONS, LINK\_CLICKS, VIDEO\_VIEWS, LOCAL\_AWARENESS, PRODUCT\_CATALOG\_SALES, LEAD\_GENERATION, BRAND\_AWARENESS, STORE\_VISITS, REACH, APP\_INSTALLS, MESSAGES, OUTCOME\_AWARENESS, OUTCOME\_ENGAGEMENT, OUTCOME\_LEADS, OUTCOME\_SALES, OUTCOME\_TRAFFIC, OUTCOME\_APP\_PROMOTION}_<br>Enum defining the full funnel objective of the campaign<br>`dataset_split_id` _numeric string or integer_<br>ID of the dataset split used to perform additional optimization on the dataset<br>`dataset_split_ids` _array<numeric string>_<br>IDs of the dataset splits used to perform additional optimization on the dataset<br>`lead_ads_selected_pixel_id` _numeric string or integer_<br>The selected pixel id for lead ads conversion leads optimization<br>`custom_attribution_source_ids` _array<numeric string>_<br>IDs of the custom attribution sources used for tracking passback events<br>`multi_event_product` _int64_<br>Identifies which action-to-action product the advertiser is using<br>`product_sales_channel` _enum {ONLINE, IN\_STORE, OMNI}_<br>ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads<br>`anchor_event_config` _JSON object_<br>Configuration for anchor event in multi-event optimization campaigns<br>`multi_event_conversion_info` _JSON object_<br>Configuration for multi-event conversion info in CLO campaigns<br>`live_video_destination` _string_<br>The live video destination type for live video ads<br>`smart_pse_enabled` _boolean_<br>Whether Smart Product Set Expansion is enabled for this campaign.<br>`smart_pse_setting` _enum{ENABLED, DISABLED}_<br>Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues.<br>`lead_ads_follow_up_event` _enum{whatsapp\_conversations}_<br>The selected lead follow-up event for lead ads campaigns.<br>`omnichannel_object` _Object_ <br>* * *<br>`app` _array<JSON object>_<br>`pixel` _array<JSON object>_ <br>required<br>`onsite` _array<JSON object>_<br>Show child parameters<br>`whats_app_business_phone_number_id` _numeric string or integer_<br>`whatsapp_phone_number` _string_<br>Show child parameters |
| `relative_value`<br>_float_ | relative\_value |
| `rf_prediction_id`<br>_numeric string or integer_ | Reach and frequency prediction ID |
| `source_adset_id`<br>_numeric string or integer_ | The source adset id that this ad is copied from (if applicable). |
| `start_time`<br>_datetime_ | The start time of the set, e.g. `2015-03-12 23:59:59-07:00` or `2015-03-12 23:59:59 PDT`. UTC UNIX timestamp |
| `status`<br>_enum{ACTIVE, PAUSED, DELETED, ARCHIVED}_ | Only `ACTIVE` and `PAUSED` are valid for creation. The other statuses<br>can be used for update. If it is set to `PAUSED`, all its active ads<br>will be paused and have an effective status `ADSET_PAUSED`. |
| `targeting`<br>_Targeting object_ | An ad set's targeting structure. "countries" is required. See [targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting). |
| `time_based_ad_rotation_id_blocks`<br>_list<list<int64>>_ | Specify ad creative that displays at custom date ranges in a campaign<br>as an array. A list of Adgroup IDs. The list of ads to display for each<br>time range in a given schedule. For example display first ad in Adgroup<br>for first date range, second ad for second date range, and so on. You<br>can display more than one ad per date range by providing more than<br>one ad ID per array. For example set<br>`time_based_ad_rotation_id_blocks` to \[\[1\], \[2, 3\], \[1, 4\]\]. On the<br>first date range show ad 1, on the second date range show ad 2 and ad 3<br>and on the last date range show ad 1 and ad 4. Use with<br>`time_based_ad_rotation_intervals` to specify date ranges. |
| `time_based_ad_rotation_intervals`<br>_list<int64>_ | Date range when specific ad creative displays during a campaign.<br>Provide date ranges in an array of UNIX timestamps where each<br>timestamp represents the start time for each date range. For example a<br>3-day campaign from May 9 12am to May 11 11:59PM PST can have three<br>date ranges, the first date range starts from May 9 12:00AM to<br>May 9 11:59PM, second date range starts from May 10 12:00AM to<br>May 10 11:59PM and last starts from May 11 12:00AM to May 11 11:59PM.<br>The first timestamp should match the campaign start time. The last<br>timestamp should be at least 1 hour before the campaign end time. You<br>must provide at least two date ranges. All date ranges must cover the<br>whole campaign length, so any date range cannot exceed campaign length.<br>Use with `time_based_ad_rotation_id_blocks` to specify ad creative for<br>each date range. |
| `time_start`<br>_datetime_ | Time start |
| `time_stop`<br>_datetime_ | Time stop |
| `tune_for_category`<br>_enum{NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES\_ELECTIONS\_POLITICS, ONLINE\_GAMBLING\_AND\_GAMING, FINANCIAL\_PRODUCTS\_SERVICES}_ | tune\_for\_category |
| `value_rule_set_id`<br>_numeric string or integer_ | Value Rule Set ID |
| `value_rules_applied`<br>_boolean_ | value\_rules\_applied |

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
| 200 | Permissions error |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 2695 | The ad set creation reached its campaign group(ios14) limit. |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 2641 | Your ad includes or excludes locations that are currently restricted |
| 190 | Invalid OAuth 2.0 Access Token |
| 900 | No such application exists. |

* * *

## Updating

### Examples

```
curl -X POST \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="LINK_CLICKS"' \
  -F 'bid_amount=200' \
  -F 'targeting={
       "geo_locations": {
         "countries": [\
           "US"\
         ]
       },
       "facebook_positions": [\
         "feed"\
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

To update the `end_time` of an ad set, using ISO-8601 date-time format

Select language

PHP Business SDKPython Business SDKcURL

* * *

```
use FacebookAds\Object\AdSet;

$adset = new AdSet('<AD_SET_ID>');
$adset->end_time = '2013-10-02T00:00:00-0700';
$adset->update();
```

To update the status of an ad set to paused

Select language

PHP Business SDKPython Business SDKcURL

* * *

```
use FacebookAds\Object\AdSet;

$adset = new AdSet('<AD_SET_ID>');
$adset->campaign_status = AdSet::STATUS_PAUSED;
$adset->update();
```

### Remarks

An archived ad set can only update two fields: `name` and `campaign_status`. The `campaign_status` field can only be changed to `DELETED`.

A deleted ad set can only change its `name`.

There are two considerations to take into account when adjusting an ad set's budget value or budget type:

When updating a set's lifetime or daily budget to a lower value, the new value must be at least 10% greater than the current amount spent already. For example: if an ad set has a $1000 lifetime budget and has spend $300 so far, the lowest new lifetime budget would be $330.

Since `v2.4`, ad sets have a minimum required budget. Any update must take that into consideration. Check the details at the [Create Considerations](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign#create-considerations) section from this page.

**Note:** When using the Reservation buying type, some fields may not be available to be updated through the API.

You can't perform this operation on this endpoint.

## Deleting

### Examples

```
curl -X DELETE \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

### /{ad\_set\_id}

You can delete an [AdSet](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) by making a DELETE request to [/{ad\_set\_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign).

#### Example

Select language

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL

* * *

```
DELETE /v25.0/<AD_SET_ID>/ HTTP/1.1
Host: graph.facebook.com
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

* * *

## Outcome-Driven Ads Experiences

### Example

**Outcome-Driven Ads Experiences (Engagement Outcome + `ON_PAGE` destination\_type)**

![Image](https://scontent-lax3-1.xx.fbcdn.net/v/t39.2365-6/652175380_1459945409197442_7497882046605313292_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=3Q1jfk1ApLEQ7kNvwEwxU2w&_nc_oc=AdpiW-96r_lkZRqGcUWVsd78nFvJ5a0N9lre0DJNlWgNuOYqiAhgyXrDJJMeCCHE97I&_nc_zt=14&_nc_ht=scontent-lax3-1.xx&_nc_gid=kZbPJ5Cmr2bDcdb9daeTxg&_nc_ss=7b289&oh=00_Af8zGcF479yUk-SiuWipsTuzU7zcEPsKdcCGhrWoRdOKHw&oe=6A51A88E)

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

![Image](https://scontent-lax3-2.xx.fbcdn.net/v/t39.2365-6/653701894_1459945279197455_6817375532106702758_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=Nn7SgzIcEIwQ7kNvwGy0FN8&_nc_oc=Adp9H9hxvw2qsZ5zo1xNYt_xRR_jmmCxNPvrybWxtMEeBCz9YRxHEmSwDe_eWzWMXgo&_nc_zt=14&_nc_ht=scontent-lax3-2.xx&_nc_gid=kZbPJ5Cmr2bDcdb9daeTxg&_nc_ss=7b289&oh=00_Af9viALKz3wL1tkhaCX92f4Wy_MtDOIZQmTyPyCSJjnxwg&oe=6A51C253)

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
| **Awareness**<br>_Reach the largest number of people who are likely to remember your ad._ | N/A | N/A | Ad Recall Lift, Reach, Impressions<br>API enum {`AD_RECALL_LIFT`, `REACH`, `IMPRESSIONS`} | Reach, Brand Awareness |
| **Traffic**<br>_Send people to a destination like your website, app or Shop._ | Facebook Shops (closed beta) | N/A | Link Clicks<br>API enum {`LINK_CLICKS`} | Traffic |
|  | Website | N/A | Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br>API enum {`LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Traffic |
|  | App | N/A | Link Clicks, Daily Unique Reach<br>API enum {`LINK_CLICKS`, `REACH`} | Traffic |
|  | Messenger | N/A | Link Clicks, Impressions, Daily Unique Reach<br>API enum {`LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Traffic |
|  | WhatsApp | N/A | Link Clicks, Impressions, Daily Unique Reach<br>API enum {`LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Traffic |
| **Engagement**<br>_Find people likely to interact with your business online, and take actions like starting a conversation or commenting on posts._ | On Video | N/A | ThruPlay, 2 second continuous view<br>API enum {`THRUPLAY`, `TWO_SECOND_CONTINUOUS_VIDEO_VIEWS`} | Video Views |
|  | On Post | N/A | Post Engagement, Impressions, Daily Unique Reach<br>API enum {`POST_ENGAGEMENT`, `IMPRESSIONS`, `REACH`} | Post Engagement |
|  | On Event | N/A | Event Response, Impressions, Post Engagement, Daily Unique Reach<br>API enum {`EVENT_RESPONSES`, `IMPRESSIONS`, `POST_ENGAGEMENT`, `REACH`} | Event Responses |
|  | Messenger | N/A | Conversations, Link Clicks<br>API enum {`CONVERSATIONS`, `LINK_CLICKS`} | Messages |
|  | WhatsApp | N/A | Conversations, Link Clicks<br>API enum {`CONVERSATIONS`, `LINK_CLICKS`} | Messages |
|  | Instagram | N/A | Conversations, Link Clicks<br>API enum {`CONVERSATIONS`, `LINK_CLICKS`} | Messages |
|  | Website | AddToWishlist, Contact, CustomizeProduct, Donate, FindLocation,, Schedule, Search, StartTrial, SubmitApplication, Subscribe, ViewContent | Conversions, Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br>API enum {`OFFSITE_CONVERSIONS`, `ONSITE_CONVERSIONS`, `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | App | Achieve Level, Activate App, Add to Wishlist, Complete Tutorial, Contact, Customize Product, Donate, Find Location, In-App Ad Click, In-App Ad Impression, Rate, Schedule, Search, Spent Credits, Start Trial, Submit Application, Subscribe, Unlock Achievement, View Content | App Events, Link Clicks, Daily Unique Reach<br>API enum {`APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `REACH`} | Conversions |
|  | On Page | N/A | Page Likes<br>API enum {`PAGE_LIKES`} | Engagement |
| **Leads**<br>_Find people interested in your business who are likely to share their contact information._ | Website | Lead, CompleteRegistration, Contact, FindLocation, Schedule, StartTrial, SubmitApplication, Subscribe | Conversions, Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br>API enum {`OFFSITE_CONVERSIONS`, `ONSITE_CONVERSIONS`, `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | Instant Forms | N/A | Leads<br>API enum {`LEAD_GENERATION`, `QUALITY_LEAD`} | Lead Generation |
|  | Messenger | N/A | Leads<br>API enum {`LEAD_GENERATION`, `QUALITY_LEAD`} | Messages |
|  | Calls | N/A | Calls<br>API enum {`QUALITY_CALL`} | Lead Generation |
|  | App | Complete Registration, Complete Tutorial, Contact, Find Location, Schedule, Start Trial, Submit Application, Subscribe | App Events, Link Clicks, Daily Unique Reach<br>API enum {`APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `REACH`} | Conversions |
| **App Promotion**<br>_Find people likely to install your app._ | N/A | All app events, including all custom events | Non-AAA: Link Clicks, App Installs, App Events, Value<br>API enum {`LINK_CLICKS`, `APP_INSTALLS`, `APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `VALUE`}<br>AAA: App Installs, App Installs w/ App Events, App Events, Value<br>API enum {`APP_INSTALLS`, `APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `VALUE`} | App Installs |
| **Sales**<br>_Find people likely to make purchases or take other important actions online or in store._ | Website & Facebook Shops (closed beta) | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | (source of truth: same as today’s Conversions objective + web and shop)<br>API enum {`OFFSITE_CONVERSIONS`, `VALUE`, `LINK_CLICKS`, `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | Website | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversions, Value, Landing Page Views, Link Clicks, Impressions, Daily Unique Reach<br>API enum {`OFFSITE_CONVERSIONS`, `VALUE`, `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | App | Purchase, Initiate Checkout, Add Payment Info, Add to Cart, Complete Registration, Donate, In-App Ad Click, In-App Ad Impression, Spent Credits, Start Trial, Subscribe, View Content | App Events, Link Clicks, Daily Unique Reach<br>API enum {`OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `REACH`} | Conversions |
|  | Website & App | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversions<br>API enum {`OFFSITE_CONVERSIONS`} | Conversions |
|  | Messenger | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversations, Conversions, Link Clicks, Impressions, Reach<br>API enum {`CONVERSATIONS`, `OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |
|  | WhatsApp | Purchase, InitiateCheckout, AddPaymentInfo, AddToCart, CompleteRegistration, Donate, StartTrial, Subscribe, ViewContent | Conversions, Link Clicks, Impressions, Reach<br>API enum {`OFFSITE_CONVERSIONS`, `LINK_CLICKS`, `IMPRESSIONS`, `REACH`} | Conversions |

Did you find this page helpful?

![Thumbs up icon](https://static.xx.fbcdn.net/rsrc.php/yR/r/OEXJ0_DJeZv.svg)

![Thumbs down icon](https://static.xx.fbcdn.net/rsrc.php/yb/r/qKPgNVNeatU.svg)

* * *