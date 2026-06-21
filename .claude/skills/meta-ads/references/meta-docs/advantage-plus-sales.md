# Advantage+ Sales Campaigns (Advantage+ Campaign Experience)
Fonte: https://developers.facebook.com/docs/marketing-api/advantage-campaigns/
(Nota: a URL original /advantage-plus-shopping-campaigns/ retorna 404 na v25 pois ASC foi descontinuada; este e o doc oficial substituto.)
Baixado para Meta Marketing API v25.0

---

Ads and Commerce

# Advantage+ Campaign Experience for Sales, App, and Leads

Updated:Jun 17, 2026

Beginning with v25.0, you will no longer be able to use the [Advantage+ shopping campaign (ASC) API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-shopping-campaigns) with the `smart_promotion_type=AUTOMATED_SHOPPING_ADS` field to create ASC campaigns, or the [Advantage+ app campaign API](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) with the `smart_promotion_type=SMART_APP_PROMOTION` field to create AAC campaigns. Instead, you will need to create campaigns with [Advantage+ audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-expansion/advantage-audience), [Advantage+ campaign budget](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/advantage-campaign-budget), and Advantage+ placements to create campaigns with an `advantage_state` that reflects the type of Advantage+ campaign. For more details, see the [Advantage+ campaign experience blog post](https://developers.facebook.com/blog/post/2025/06/03/advantage-plus-campaign-experience-for-sales-and-app).

The `existing_customer_budget_percentage` field is not available for new Advantage+ campaigns. Existing ASC campaigns with this field will remain functional until v26.0, when they will be paused, and can only be migrated via Ads Manager where you will be prompted to “Duplicate Campaign”. For new campaigns, refer to the [Replicate `existing_customer_budget_percentage` Behavior](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns#replicate-existing-customer-budget-percentage-behavior) section below.

This guide shows you how to create Advantage+ sales and app campaigns with `advantage_state` set to `advantage_plus_sales` or `advantage_plus_app`. These campaigns will be displayed in Ads Manager as Advantage+ sales (or app) campaign “ON” with the associated performance benefits. Advantage+ sales and app campaigns are the updated, streamlined versions of [Advantage+ shopping campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-shopping-campaigns) and [Advantage+ app campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns).

In this new setup, all sales and app promotion campaigns can benefit from the AI optimizations that drive performance for Advantage+ shopping and app campaigns today. The complete range of ad tools will remain available to meet businesses’ needs.

You will need to ensure the campaign includes [Advantage+ audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-expansion/advantage-audience), [Advantage+ campaign budget](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/advantage-campaign-budget), and Advantage+ placement for the campaign to have the Advantage+ state enabled, as reflected in the `advantage_state` field set to a value other than `DISABLED`.

**Note:** No action is required to opt in to Advantage+ placement, as it is the default setting in the API.

## Create an Advantage+ campaign

### Step 1: Choose an objective for the ad campaign

`OUTCOME_SALES`: Use this to achieve the same performance results of an Advantage+ shopping campaign when opted into the following automation settings.
`APP_INSTALLS`: Use this to achieve the same performance results of an Advantage+ app campaign when opted into the following automation settings.
`OUTCOME_LEADS`: Use this to achieve an Advantage+ leads campaign. Advantage+ leads campaigns are designed to maximize the performance of your leads campaigns with less set up time and greater efficiency. Using AI, Advantage+ leads campaigns can help you generate qualified leads by delivering your ads to more relevant audiences on more effective ad placements.

### Step 2: Set the required Advantage+ criteria

You can [create an ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad-campaign) that uses the same automation levers as an Advantage+ shopping campaign or Advantage+ app campaign using the following settings:

#### Advantage+ placement state automation criteria

No [placement targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting) or exclusions should be set, so all available placements will be eligible.
All ad sets in the ad campaign must fit this criteria or the ad campaign will reflect `advantage_state: DISABLED` due to placement restrictions (that is, `advantage_placement_state: DISABLED`).
Placement exclusions may be set on the ad account level and the campaign will still be eligible for an `advantage_state` value that is not `DISABLED`.

#### Advantage+ budget state criteria

The budget is configured at the ad campaign level using a supported bid strategy

#### Advantage+ audience state criteria

Any of the following criteria may be used. **Note:** The following behavior must be applied to **at least one** ad set in the ad campaign.

_(Recommended)_ Opt into [Advantage+ audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-expansion/advantage-audience) with `"targeting_automation": {"advantage_audience": 1}`.
No targeting parameters set besides [`geo_locations`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/basic-targeting#location), which are allowed.
_(Advanced setup)_Individual targeting options are allowed, but with relaxation. For more details on how to enable relaxation for individual targeting options, refer to the following documentation:

[Advantage Lookalike](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-expansion/advantage-lookalike)
[Advantage Custom Audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-expansion/advantage-custom-audience)
[Advantage Detailed Targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-expansion/advantage-detailed-targeting)
[Advanced Targeting: Enable Age and Gender as Suggestions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#enable-age-and-gender-suggestions)

### Step 3: Verify the `advantage_state_info` opt-in

Once opted into these three automation levers, the ad campaign will reflect the following `advantage_state` at the ad campaign level in `advantage_state_info` depending on the objective.

```
GET /v25.0/<CAMPAIGN_ID>?fields=name,objective,advantage_state_info
```

#### `objective: OUTCOME_SALES`

```
advantage_state_info: {
 advantage_state: ADVANTAGE_PLUS_SALES
 advantage_budget_state: ENABLED
 advantage_audience_state: ENABLED
 advantage_placement_state: ENABLED
}
```

#### `objective: APP_PROMOTION`

```
advantage_state_info: {
 advantage_state: ADVANTAGE_PLUS_APP
 advantage_budget_state: ENABLED
 advantage_audience_state: ENABLED
 advantage_placement_state: ENABLED
}
```

#### `objective: OUTCOME_LEADS`

```
advantage_state_info: {
 advantage_state: ADVANTAGE_PLUS_LEADS
 advantage_budget_state: ENABLED
 advantage_audience_state: ENABLED
 advantage_placement_state: ENABLED
}
```

#### `DISABLED` state

If any of the levers `advantage_budget_state`, `advantage_audience_state`, or `advantage_placement_state` are `DISABLED`, the `advantage_state` within `advantage_state_info` will be `DISABLED`.

```
advantage_state_info: {
 advantage_state: DISABLED
 advantage_budget_state: DISABLED
 advantage_audience_state: ENABLED
 advantage_placement_state: ENABLED
}
```

A campaign must have `advantage_budget_state`, `advantage_audience_state`, and `advantage_placement_state` set to `ENABLED` in order to have the `advantage_state` set to `ADVANTAGE_PLUS_SALES`, `ADVANTAGE_PLUS_APP`, or `ADVANTAGE_PLUS_LEADS`.

If any of the automation levers return `DISABLED`, the `advantage_state` will reflect `DISABLED`.

The `advantage_state` field and its sub-fields `advantage_budget_state`, `advantage_audience_state`, and `advantage_placement_state` are read-only state information flags that can be queried, but are set by configuring the Advantage+ automation levers.

**Note:** Campaigns created with an `advantage_state` of `ADVANTAGE_PLUS_SALES`, `ADVANTAGE_PLUS_APP`, or `ADVANTAGE_PLUS_LEADS` will reflect a `smart_promotion_type` of `GUIDED_CREATION`.

## Replicate Advantage+ shopping campaign performance with Advantage+ campaigns

Set your ad campaign objective to `OUTCOME_SALES`.
Refrain from setting placement targeting or placement exclusions.
Configure a budget at the ad campaign level with a `bid_strategy` with `LOWEST_COST_WITHOUT_CAP` (recommended), `COST_CAP`, `LOWEST_COST_WITH_BID_CAP`, or `LOWEST_COST_WITH_MIN_ROAS`.
Refrain from setting any targeting parameters besides `geo_locations`, or opt into Advantage+ audience.

## Replicate `existing_customer_budget_percentage` behavior

To replicate `existing_customer_budget_percentage` behavior for your ad campaign, create two ad sets per ad campaign that separate existing customers from new customers.

Set up a custom audience that defines your existing customers and have its custom audience ID.

Set your budget at the ad campaign level using Advantage campaign budget.

Create an ad set by making a `POST` request to `/act_<AD_ACCOUNT_ID/adsets`.

Set a maximum spending limit for the ad set:

`"daily_min_spend_target": "X",
"daily_spend_cap": "X"`
Set the `custom_audience` settings to include the custom audience that you consider your existing customers. Make sure this is not a suggestion or relaxed by ensuring that `targeting_relaxation_types` is set to `0` for custom audiences.

```
{
"targeting":{
"geo_locations":{
"countries":["US"]
},
"custom_audiences":[{\
"id":<CUSTOM_AUDIENCE_ID>\
}],
"targeting_relaxation_types":{
"custom_audience":0
}
}
}
```
Use the [same creative settings](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad-creative) in both ad sets. Then, you can [create your ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad) with the `/act_<AD_ACCOUNT_ID>/ads` endpoint.

Creating ads with an Advantage+ state follows the same process as in manual sales campaigns. Refer to this documentation to create ads with an enabled Advantage+ state:

[Manual Ads (non-Catalog Ads)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup)
[Advantage+ Catalog Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads)
[Shops Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/shops-ads)
[Localized Catalogs (or Advantage+ Catalog Ads for Multiple Languages or Countries)](https://developers.facebook.com/documentation/ads-commerce/catalog/guides/localized-catalog)
Duplicate your ad set, but edit it so that it includes a [custom audience exclusion](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#custom_audiences) to exclude people who are your existing customers. You can:

Include a second ad set in your `POST` call in step 3 with the exclusion of your custom audience that represents your existing customers.

Repeat steps 1-4 to create a second ad set but ensure that your custom audience of existing customers is set to `exclude`.

Use the [`/adcopies` endpoint](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign/copies) to duplicate your first ad set, then make a `POST` call to edit the ad set to exclude the custom audience ID of existing customers.

```
{
"targeting":{
"geo_locations":{
"countries":["US"]
},
"age_min":25,
"age_max":40,
"excluded_custom_audiences":[{\
"id":<CUSTOM_AUDIENCE_ID>\
}],
}
}
```

You have created a new ad campaign with a spending limit on existing customers. It will run after review.

## Migrate Advantage+ shopping campaigns and Advantage+ app campaigns into Advantage+ campaigns

### Limitations

Advantage+ app campaigns can only be migrated, not copied, into the Advantage+ format.
Advantage+ shopping campaigns using `existing_customer_budget_percentage` cannot be migrated to the Advantage+ structure using the Marketing API. Open the campaign in Ads Manager to migrate to the Advantage+ structure.

### Copy and migrate

You can copy your Advantage+ shopping campaign into a new campaign in the Advantage+ structure with the `migrate_to_advantage_plus` parameter.

#### Example request

```
curl -X POST <AD_CAMPAIGN_ID>/copies?migrate_to_advantage_plus=true
```

#### Example response

```
{
  "copied_campaign_id": "6877326900432",
  "ad_object_ids": [\
    {\
      "ad_object_type": "campaign",\
      "source_id": "6877313029432",\
      "copied_id": "6877326900432"\
    }\
  ]
}
```

When the new campaign (`copied_id`) is queried, it will reflect a `smart_promotion_type` of `GUIDED_CREATION` and will have `advantage_state_info` details.

### Campaigns using `existing_customer_budget_percentage`

Campaigns using `existing_customer_budget_percentage` can only be migrated to the Advantage+ structure by duplicating the campaign in the Ads Manager. You may open the campaign in Ads Manager for instructions on how to duplicate into the Advantage+ structure. For recreating as a new campaign, see the [Replicate Existing Customer Budget Percentage](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns#replicate-existing-customer-budget-percentage-behavior) section.

### Migrate only

If you would like to keep the same campaign IDs, you can use the `migrate_to_advantage_plus` field to migrate your Advantage+ shopping campaigns/Advantage+ app campaigns into the Advantage+ format.

#### Example request

```
curl -X POST <AD_CAMPAIGN_ID>?migrate_to_advantage_plus=true
```

#### Example response

```
{
success: <BOOLEAN>
}
```

The campaign will then reflect a `smart_promotion_type` of `GUIDED_CREATION` and will have `advantage_state_info` details.

## FAQ

**Why are we updating Advantage+ shopping campaigns to Advantage+ sales campaigns?**

Advantage+ sales campaigns use the same automation features as Advantage+ shopping campaigns, and they are both built on the principles of liquidity, including the combination of Advantage+ budget, Advantage+ audience, and Advantage+ placements. The Advantage+ campaign experience for Sales also reflects expanded supported use cases not available with the Advantage+ shopping campaign endpoint. Advertisers can now benefit from similar performance with additional features available for manual campaigns, like additional conversion locations, and may now create more than one adset per campaign.

**What are the implications of this update to the Advantage+ campaign experience on my campaign performance?**

If you keep the same settings in the new Advantage+ campaign experience as you used in your previous Advantage+ shopping campaigns, Advantage+ app campaigns or manual campaigns, then nothing will change. Your campaign will perform similarly to the previous set up.

**What happens to my campaign learnings when I use the migrate\_to\_advantage\_plus field to copy or migrate my campaign?**

Migrating or migrating and copying an ASC/AAC campaign into Advantage+ format, including using the `migrate_to_advantage_plus` field, will force the campaign into the learning stage. This means that newly copied campaigns will be in the learning stage, as well as campaigns that are migrated only without a copy action. This applies to all campaigns and there is not a workaround for the learnings.

**Why are my advertisers seeing the new experience in some ad accounts and the original experience in others?**

We typically roll out products at the ad account level, so there is a chance you could see two different experiences across different ad sets during the rollout period. Once the new experience has fully rolled out, all ad accounts will have the same experience. Aim to maintain your existing strategy, regardless of the experience you have within Ads Manager.

**What happens to my existing Advantage+ shopping campaigns that I created via API when v25.0 rolls out?**

ASC/AAC campaigns that can be migrated into Advantage+ structure may use the `migrate_to_advantage_plus` field to migrate or copy and migrate their campaigns.
With the introduction of v24.0, you will not be able to create ASC campaigns with `smart_promotion_type=AUTOMATED_SHOPPING_ADS`, but may revert to v23.0 to do so. The introduction of v25.0 will give an error for all attempts to create ASC campaigns with `smart_promotion_type=AUTOMATED_SHOPPING_ADS` on any version of the API.
If not migrated prior, existing Advantage+ shopping campaigns cannot be edited and will maintain all previous settings with the introduction of v25.0. Un-migrated eligible campaigns may still take migration actions for “Copy and Migrate” or “Migrate Only”, but will be blocked from all other edit activity with v25.0.
The v25.0 edit exceptions are for ASC campaigns that use `existing_customer_budget_percentage` and cannot be migrated, or ASC campaigns that have more than 50 ads within the adset and cannot be migrated - these campaigns will be editable after v25.0, but may not be duplicated. We advise you to begin creating Advantage+ sales campaigns with `"advantage_state": "ADVANTAGE_PLUS_SALES"` as soon as possible to avoid any disruption with v25.0.
All legacy ASC/AAC campaigns will be blocked from edits with the release of v26.0 and will no longer be able to use the `migrate_to_advantage_plus` field to migrate. This includes campaigns that have more than 50 ads within their adsets, or campaigns that are using `existing_customer_budget_percentage`.

**What happens if I try to create an ASC/AAC campaign on v25.0?**

ASC/AAC will not be able to be created on any API version with the release of v25.0.

**How can I migrate my Advantage app campaigns into Advantage+?**

AAC campaigns cannot be copied and migrated, but may be migrated using the `migrate_to_advantage_plus` field. See the [migration instructions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns#migrate-to-advantage-campaigns) above.

**Will I be able to edit my old Advantage+ shopping campaigns that I created via API without issue in the new Ads Manager UI after the new Advantage+ campaign UI experience is fully rolled out?**

Yes. Once the ad account has been upgraded into the new Advantage+ experience on Ads Manager, campaigns that were created as Advantage+ shopping campaigns will show as “Advantage+ On” in the Ads Manager whether they were created via API or UI.

**Will my ASC campaigns created through the API with automated\_shopping\_ads reflect as “advantage\_state”: “ADVANTAGE\_PLUS\_SALES” after this change?**

If you edit the ASC campaign within the Ads Manager UI in any way and accept turning on Advantage+ campaign budget when prompted, it will be converted to an `ADVANTAGE_PLUS_SALES` campaign that shows as “Advantage+ On” through the Ads Manager UI, and `"advantage_state": "ADVANTAGE_PLUS_SALES"` when queried on its API settings. The campaign will also change from `smart_promotion_type=AUTOMATED_SHOPPING_ADS` to `smart_promotion_type=GUIDED_CREATION`. However, you must edit something about the ASC campaign in the Ads Manager in order to prompt this change and accept the Advantage+ campaign budget.

If the ASC campaign was created and edited exclusively through the API, it will continue to reflect as `smart_promotion_type=AUTOMATED_SHOPPING_ADS` in the API settings until something is edited about this campaign in the Ads Manager. It will show as “Advantage+ On: through the Ads Manager UI after the ad account has been upgraded into the new Advantage+ experience.

**If I create an ASC campaign before my ad account is enrolled in the new Advantage+ campaign Ads Manager experience, will that campaign reflect as “Advantage+ On” when it becomes enrolled? Will it show as “advantage\_state”: “ADVANTAGE\_PLUS\_SALES” in the API?**

ASC campaigns created through the old ASC experience in Ads Manager will show with “Advantage+ On” settings once the ad account has been upgraded into the new Advantage+ campaign Ads Manager experience.

However, ASC campaigns created on the Ads Manager with the old ASC UI before the ad account has been upgraded into the new Advantage+ campaign UI experience will need to be edited in the Ads Manager and accept turning on Advantage+ campaign budget when prompted in order to reflect Advantage+ Sales being on in the new interface and `"advantage_state": "ADVANTAGE_PLUS_SALES"`. This will also then display the budget at the campaign level in reporting and update to `smart_promotion_type=GUIDED_CREATION`. Otherwise, the campaign will continue to reflect `smart_promotion_type=AUTOMATED_SHOPPING_ADS` on the API settings.

**What’s the impact when I edit an API-created ASC campaign in the new Advantage+ campaign UI experience and leave its settings as “Advantage+ On”?**

The campaign converts from Advantage+ shopping campaign (i.e., `smart_promotion_type=AUTOMATED_SHOPPING_ADS`) to an Advantage+ sales campaign (i.e., `"advantage_state": "ADVANTAGE_PLUS_SALES"`) with `smart_promotion_type=GUIDED_CREATION`.

**What happens to my ASC campaigns with smart\_promotion\_type=AUTOMATED\_SHOPPING\_ADS that were using existing\_customer\_budget\_percentage if it’s not supported with Advantage+ sales campaigns?**

ASC campaigns that use `existing_customer_budget_percentage` cannot be migrated to the Advantage+ structure with `"advantage_state": "ADVANTAGE_PLUS_SALES"` using the API, but can be migrated into Advantage+ structure if you open the campaign in Ads Manager.

ASC campaigns using `existing_customer_budget_percentage` will still be editable with the release v25.0 but unable to be duplicated. These campaigns will be paused with the release of v26.0, so we recommend migrating the campaigns to Advantage+ structure within Ads Manager as soon as possible.

**Can I use the advantage\_state field to make a POST request to create an ADVANTAGE\_PLUS\_SALES campaign?**

No. Developers will need to follow the criteria above to make a campaign with Advantage+ audience, Advantage+ placement, and Advantage+ budget criteria.

**Can I make a POST request to smart\_promotion\_type to set it back to GUIDED\_CREATION instead of AUTOMATED\_SHOPPING\_ADS?**

No. Please edit the campaign in Ads Manager once the ad account is enrolled in the new UI to convert the campaign, or use the `migrate_to_advantage_plus` field to migrate the campaign via API.

**Note:** Not all campaigns will be eligible to migrate from ASC to Advantage+ sales. ASC campaigns using `existing_customer_budget_percentage` cannot be migrated via the API, but can be migrated in Ads Manager. ASC campaigns where the count of ads within the ASC adset is greater than 50 cannot be migrated into Advantage+ sales campaigns at all. These campaigns will remain in the ASC structure but will continue to be editable after v25.0. However, all legacy ASC campaigns with `smart_promotion_type` will be uneditable with the release of v26.0.

**What specific qualifications will make my campaign ENABLED for advantage\_audience\_state?**

If `"targeting_automation": {"advantage_audience": 1}` for at least one ad set in the campaign, OR
If `"targeting_automation": {"advantage_audience": 0}` or is not set, and at least one ad set in the campaign has:

Ad set is using default age or age <= 25 or using age as a suggestion
Ad set is using default gender or using gender as a suggestion
Ad set is not using custom audience inclusion or using Advantage custom audience

**How do I disable an Advantage+ sales campaign so that advantage\_state will reflect DISABLED?**

If you set up your budget, audience, or placement details outside of the criteria listed above, the campaign will reflect `advantage_state:DISABLED`.

**Can I migrate my ad campaign if it is part of a Special Ad Category?**

Access to Advantage+ Audience, Advantage Custom Audience, and Advantage Detailed Targeting for Special Ad Category campaigns related to Housing, Employment, and Financial Products and Services is currently being rolled out to advertisers. If your campaign is eligible at the point of migration, it will be recreated in the Advantage+ structure. If not, it will be migrated into a similar structure using broad targeting. For more details, please see this [Help Center article⁠](https://www.facebook.com/business/help/298000447747885).

Did you find this page helpful?

![Thumbs up icon](https://static.xx.fbcdn.net/rsrc.php/yR/r/OEXJ0_DJeZv.svg)

![Thumbs down icon](https://static.xx.fbcdn.net/rsrc.php/yb/r/qKPgNVNeatU.svg)

* * *