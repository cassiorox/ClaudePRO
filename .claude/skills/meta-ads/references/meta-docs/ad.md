# Ad (adgroup)
Fonte: https://developers.facebook.com/docs/marketing-api/reference/adgroup/
Baixado para Meta Marketing API v25.0

---

# Ad

Updated: May 6, 2026

Contains information to display an ad and associate it with an ad set. Each ad is associated with an ad set and all ads in a set have the same daily or lifetime budget, schedule, and targeting. Creating multiple ads in an ad set helps optimize their delivery based on variations in images, links, video, text or placements.

Note that results returned by `synchronous_ad_review` does not represent the final decision made during full review of your ad.

### Ads with Political Content

To increase transparency of ads on Facebook, we require advertisers running ads with political content to complete authorization. You must indicate that your ad has political content and provide the name of the funding source for the ad. Your ad account must be authorized by a Page admin to run political ads for this Page (Issue, Electoral or Political Ads tab under Page Settings). Ad account users must go through a verification process.

### Ads with Page Mentions

With Facebook's ads tools such as Ads Manager you can create an ad with a Page Mention. This displays a link in your ad which opens an advertiser's Facebook page. We do not provide this functionality in Marketing API. If you try to create an ad with the API with a Page Mention it will succeed, however we will deliver the ad without the mention.

### Targeting DSA Regulated Locations (European Union)

To create or copy an ad which is in an ad set targeted in the EU's Digital Services Act (DSA) regulated locations, set the payor/beneficiary information first. If `default_dsa_payor` and `default_dsa_beneficiary` are set in an ad account, during the copying process they will be filled with saved default values.

### Targeting Youth in EU, EEA, and Switzerland

Meta will stop showing ads to youth in the EU, EEA, and Switzerland. When creating new ad sets or updating existing ones that target youth in these regions, they will be prevented.

### Examples

Creating an ad:

```
curl -X POST \
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
       "creative_id": "<CREATIVE_ID>"
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

To create a political ad, provide `authorization_category` with the value `POLITICAL`:

```
curl -X POST \
  -F 'name="My AdGroup"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
       "creative_id": "<CREATIVE_ID>"
     }' \
  -F 'status="PAUSED"' \
  -F 'authorization_category="POLITICAL"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

## Reading

An ad object contains the data necessary to visually display an ad and associate it with a corresponding ad set.

### By ad ID

```
curl -X GET \
  -d 'fields="id,name"' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

### By ad campaign

```
curl -X GET \
  -d 'fields="name"' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>/ads
```

#### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset` _enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year}_ | Date Preset |
| `review_feedback_breakdown` _boolean_ | Default value: `false` |
| `time_range` _{'since':YYYY-MM-DD,'until':YYYY-MM-DD}_ | Time Range. If time range is invalid, it will be ignored. |

#### Fields

| Field | Description |
| --- | --- |
| `id` _numeric string_ | id (default) |
| `account_id` _numeric string_ | account_id |
| `ad_active_time` _numeric string_ | ad_active_time |
| `ad_review_feedback` _AdgroupReviewFeedback_ | ad_review_feedback |
| `ad_schedule_end_time` _datetime_ | ad_schedule_end_time |
| `ad_schedule_start_time` _datetime_ | ad_schedule_start_time |
| `adlabels` _list<AdLabel>_ | adlabels |
| `adset` _AdSet_ | adset |
| `adset_id` _numeric string_ | adset_id |
| `bid_amount` _int32_ | bid_amount |
| `bid_info` _map<string, unsigned int32>_ | bid_info |
| `bid_type` _enum {CPC, CPM, MULTI_PREMIUM, ABSOLUTE_OCPM, CPA}_ | bid_type |
| `campaign` _Campaign_ | campaign |
| `campaign_id` _numeric string_ | campaign_id |
| `configured_status` _enum {ACTIVE, PAUSED, DELETED, ARCHIVED}_ | configured_status |
| `conversion_domain` _string_ | conversion_domain |
| `conversion_specs` _list<ConversionActionQuery>_ | conversion_specs |
| `created_time` _datetime_ | created_time |
| `creative` _AdCreative_ | creative |
| `creative_asset_groups_spec` _AdCreativeAssetGroupsSpec_ | creative_asset_groups_spec |
| `demolink_hash` _string_ | demolink_hash |
| `display_sequence` _int32_ | display_sequence |
| `effective_status` _enum {ACTIVE, PAUSED, DELETED, PENDING_REVIEW, DISAPPROVED, PREAPPROVED, PENDING_BILLING_INFO, CAMPAIGN_PAUSED, ARCHIVED, ADSET_PAUSED, IN_PROCESS, WITH_ISSUES}_ | effective_status |
| `engagement_audience` _bool_ | engagement_audience |
| `failed_delivery_checks` _list<DeliveryCheck>_ | failed_delivery_checks |
| `is_autobid` _bool_ | is_autobid |
| `issues_info` _list<AdgroupIssuesInfo>_ | issues_info |
| `last_updated_by_app_id` _id_ | last_updated_by_app_id |
| `name` _string_ | name |
| `preview_shareable_link` _string_ | preview_shareable_link |
| `priority` _unsigned int32_ | priority |
| `recommendations` _list<AdRecommendation>_ | recommendations |
| `source_ad` _Ad_ | source_ad |
| `source_ad_id` _numeric string_ | source_ad_id |
| `special_ad_categories` _list<enum>_ | special_ad_categories |
| `status` _enum {ACTIVE, PAUSED, DELETED, ARCHIVED}_ | status |
| `targeting` _Targeting_ | targeting |
| `tracking_and_conversion_with_defaults` _TrackingAndConversionWithDefaults_ | tracking_and_conversion_with_defaults |
| `tracking_specs` _list<ConversionActionQuery>_ | tracking_specs |
| `updated_time` _datetime_ | updated_time |

#### Edges

| Edge | Description |
| --- | --- |
| `adcreatives` _Edge<AdCreative>_ | adcreatives |
| `adrules_governed` _Edge<AdRule>_ | adrules_governed |
| `copies` _Edge<Adgroup>_ | copies |
| `insights` _Edge<AdsInsights>_ | insights |
| `leads` _Edge<UserLeadGenInfo>_ | leads |
| `previews` _Edge<AdPreview>_ | previews |
| `targetingsentencelines` _Edge<TargetingSentenceLine>_ | targetingsentencelines |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80004 | Too many calls to this ad-account. Wait and try again. |
| 613 | Calls to this api have exceeded the rate limit. |
| 190 | Invalid OAuth 2.0 Access Token |
| 104 | Incorrect signature |
| 2635 | You are calling a deprecated version of the Ads API. |
| 2500 | Error parsing graph query |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 200 | Permissions error |
| 270 | This Ads API request is not allowed for apps with development access level. |

## Creating

Before you create an ad, you need an existing ad set and ad creative. You can create ads synchronously and asynchronously. New ads are in pending state and do not run until Facebook approves or rejects them.

### Synchronous Creation

```
curl -X POST \
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
       "creative_id": "<CREATIVE_ID>"
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

### Asynchronous Creation

Create multiple ads at a time asynchronously via `HTTP POST` to: `https://graph.facebook.com/{API_VERSION}/act_{AD_ACCOUNT_ID}/asyncadrequestsets`

Fields: `name` (required), `ad_specs` (required, array of ad specs), `notification_uri` (optional), `notification_mode` (optional: OFF / ON_COMPLETE).

### Limits

| Limit | Value |
| --- | --- |
| Ads in regular ad account | 5000 non-deleted ads |
| Ads in bulk ad account | 50000 non-deleted ads |
| Ads in an ad set | 50 non-deleted ads |
| Archived ads in an ad account | 100,000 archived ads |

### /act_{ad_account_id}/ads — POST Parameters

| Parameter | Description |
| --- | --- |
| `ad_schedule_end_time` _datetime_ | End time of an individual ad. Only for sales and app promotion campaigns. |
| `ad_schedule_start_time` _datetime_ | Start time of an individual ad. Only for sales and app promotion campaigns. |
| `adlabels` _list<Object>_ | Ad labels associated with this ad |
| `adset_id` _int64_ | The ID of the ad set, required on creation. |
| `adset_spec` _Ad set spec_ | When provided, adset_id field is not required. |
| `audience_id` _string_ | The ID of the audience. |
| `bid_amount` _integer_ | Deprecated. Set bid_amount for the ad set. |
| `conversion_domain` _string_ | Domain where conversions happen. Required for campaigns that share data with a pixel. First and second level domains only, e.g. `facebook.com`. |
| `creative` _AdCreative_ | Required for create. ID or creative spec: `{"creative_id": <CREATIVE_ID>}`. |
| `creative_asset_groups_spec` _string_ | creative_asset_groups_spec |
| `display_sequence` _int64_ | Sequence of the ad within the same campaign |
| `engagement_audience` _boolean_ | Create a new audience based on users who engage with this ad |
| `execution_options` _list<enum{validate_only, synchronous_ad_review, include_recommendations}>_ | Execution setting. `validate_only` runs validation without mutation. `synchronous_ad_review` must be specified with `validate_only`. |
| `name` _string_ | Name of the ad. Required. |
| `priority` _int64_ | Priority |
| `source_ad_id` _numeric string_ | ID of the source Ad, if applicable. |
| `status` _enum{ACTIVE, PAUSED, DELETED, ARCHIVED}_ | Only ACTIVE and PAUSED are valid during creation. New ads go through review (PENDING_REVIEW) before reverting to ACTIVE/PAUSED. Use PAUSED during testing. |
| `tracking_specs` _Object_ | Log actions taken by people on your ad. |

#### Return Type

```
Struct {
  id: numeric string,
  success: bool,
}
```

### /{ad_id}/copies — POST Parameters

| Parameter | Description |
| --- | --- |
| `adset_id` _numeric string or integer_ | Single ID of an adset to make the parent of the copy. |
| `creative_parameters` _AdCreative_ | Creative inputs used to construct the creative in the new ad. |
| `rename_options` _JSON_ | `rename_strategy` enum {DEEP_RENAME, ONLY_TOP_LEVEL_RENAME (default), NO_RENAME}; `rename_prefix`; `rename_suffix`. |
| `status_option` _enum {ACTIVE, PAUSED (default), INHERITED_FROM_SOURCE}_ | Status of the copied ad. |

Return: `{ copied_ad_id: numeric string }`

## Updating

```
curl -X POST \
  -F 'name="My New Ad"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

### Limitations

- Only fields used during ad creation can be updated.
- `adset_id` and `social_prefs` cannot be updated.
- Ads with `status = ARCHIVED` have only two mutable fields: `name` and `status` (can only change status to DELETED).
- Ads with `status = DELETED` only can have `name` changed.
- Ads in an ad set with `creative_sequence` set cannot be changed to PAUSED, ARCHIVED, or DELETED.

## Deleting

```
curl -X DELETE \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

You cannot delete ads in ad set with `creative_sequence` settings. Return: `{ success: bool }`.
