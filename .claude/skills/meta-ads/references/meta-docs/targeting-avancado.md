<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting.md | Scrape: 2026-08-09 | API v26.0 -->

# Advanced targeting



Advanced targeting includes:

* [Mobile](#mobile) and [Placement](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting)
* [Advanced Demographic Targeting](#demographic)
    * [Education and workplace](#education-and-workplace)
* [Custom Audiences](#custom_audiences)
* [Locales](#locales)
* [Reach People Interested in Selected Cities and Regions](#reach-people-interested-in-selected-cities-and-regions)
* [Broad Category Targeting](#broadcategories)
* [Targeting Expansion](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion)
* [Flexible Targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/flexible-targeting)

You can use any combination of these advanced targeting options in your own [custom audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience) and lookalikes. By default, Facebook `ORs` combinations together. Learn more about [core or basic targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/basic-targeting).

**Warning:** If you use `flexible_spec`, you must also provide one of the following under `targeting`:

* `geo_locations` (geographical targeting field from country, region, city, zip)
* `custom_audiences`
* `product_audience_specs`
* `dynamic_audience_ids`

### Limitations

* Advertisers running housing, employment, and credit ads, who are based in the United States or running ads targeted to the United States have different sets of restrictions. See [**Special Ad Category**](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category).
* See our [Targeting Restrictions guide](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-restrictions) for more limitations.

## Mobile

Mobile targeting is useful for [Mobile App Install ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads).

```
curl -X POST \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "user_device": ["Galaxy S6","One m9"],
    "user_os": ["android"]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

You can combine categories, such as iPod OR iPad OR iPhone.

**These categories are not mutually exclusive**. If you select iOS you target all devices running iOS, including iPhone and iPod, without specifying `user_device`.

**For Brand Awareness Objective ads**, you can't target based on mobile device type, such as feature phones or Samsung, or based on iOS version number. You can only choose Android or iOS, or all mobile phones.

### Available fields

| Field | Description |
| --- | --- |
| `user_os`<br><br>type: array | **Required.**<br><br>One or more values from OS option table below. Possible values are at [Targeting Search API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search) with `type=adTargetingCategory` and `class=user_os`. You cannot target the minimum version of one platform with the other platform. However you can target both platforms without specifying minimal versions of either.  <br><br>**Valid:**  <br>- `['iOS', 'Android']`  <br>- `['iOS']`  <br>- `['Android_ver_4.2_and_above']`  <br>- `['iOS_ver_8.0_to_9.0']`<br><br>**Invalid:**  <br>- `['Android', 'iOS_ver_8.0_and_above']`  <br>- `['iOS', 'Android_ver_4.0_and_above']` |
| `user_device`<br><br>type: array | **Optional.**<br><br>Devices must match the value in `user_os`. Get possible values at [Targeting Search API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search) with `type=adTargetingCategory` and `class=user_device`. |
| `excluded_user_device`<br><br>type: array | **Optional.**<br><br>Devices to exclude. Devices must match the value in `user_os`. Get possible values at [Targeting Search API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search) with `type=adTargetingCategory` and `class=user_device`. |
| `wireless_carrier`<br><br>type: array | **Optional.**<br><br>Allowed value is `Wifi`. Target mobile users currently on Wi-Fi networks. |

### Operating system options

| Field | Description |
| --- | --- |
| `iOS`<br><br>type: string | iOS devices, including iPhone, iPad, and iPod |
| `iOS_ver_x.x_and_above`<br><br>type: string | iOS devices running OS version x.x and above.<br><br>**Options:** 2.0, 3.0, 4.0, 4.3, 5.0, 6.0, 7.0, 8.0, 9.0.<br>**Example:** `iOS_ver_4.0_and_above`<br><br>For Meta App Ads:<br><br>* SKAdNetwork and Meta's Aggregated Event Measurement ad sets only support version range from `iOS_ver_14.0_and_above`.<br>* Non-SKAdNetwork or Meta's Aggregated Event Measurement ad set only support iOS version range from `iOS_ver_2.0_to_14.4`. |
| `iOS_ver_x.x_to y.y`<br><br>type: string | iOS devices running OS versions x.x to y.y.<br><br>**Options:** 2.0, 3.0, 4.0, 4.3, 5.0, 6.0, 7.0, 8.0, 9.0.<br><br>**Example:** `iOS_ver_8.0_to_9.0`, where x.x must be less than y.y |
| `Android`<br><br>type: string | Android devices |
| `Android_ver_x.x_and_above`<br><br>type: string | Android devices running version x.x and above.<br><br>**Options:** 2.0, 2.1, 2.2, 2.3, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2., 4.3, 4.4, 5.0, 5.1, 6.0, 7.0, 7.1, and 8.0.<br><br>**Example:** `Android_ver_4.0_and_above` |
| `Android_ver_x.x_to y.y`<br><br>type: string | Android devices running versions x.x to y.y.<br><br>**Options:** 2.0, 2.1, 2.2, 2.3, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2., 4.3, 4.4, 5.0, 5.1, 6.0, 7.0, 7.1, and 8.0.<br><br>**Example:** `Android_ver_4.2_to_8.0`, where x.x must be less than y.y |

## Advanced demographic targeting {#demographic}

Target based on relationships, education, finances, and life events.

### Examples

First query `life_events`:

```
curl -G \
  -d 'type=adTargetingCategory' \
  -d 'class=life_events' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/search
```

Add these to `targeting_spec`:

```
curl -X POST \
  -F 'name="My First AdSet"' \
  -F 'daily_budget=10000' \
  -F 'bid_amount=300' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="REACH"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'promoted_object={
       "page_id": "<PAGE_ID>"
     }' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "age_max": 24,
       "age_min": 20,
       "behaviors": [
         {
           "id": 6002714895372,
           "name": "All travelers"
         }
       ],
       "device_platforms": [
         "mobile"
       ],
       "genders": [
         1
       ],
       "geo_locations": {
         "countries": [
           "US"
         ],
         "regions": [
           {
             "key": "4081"
           }
         ],
         "cities": [
           {
             "key": 777934,
             "radius": 10,
             "distance_unit": "mile"
           }
         ]
       },
       "interests": [
         {
           "id": "<INTEREST_ID>",
           "name": "<INTEREST_NAME>"
         }
       ],
       "life_events": [
         {
           "id": 6002714398172,
           "name": "Newlywed (1 year)"
         }
       ],
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

This example targets:

* Location: Japan or United States: Menlo Park (+10 mi) California or United States: Texas
* Age: 20 - 24
* Gender: male
* Interests: Association football (Soccer)
* Behaviors: All frequent travelers
* Life Event: Newlywed (1 year)
* Home Ownership: Renters

Here's another example targeting by location, demographic, relationship status and interests:

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "age_max": 43,
    "age_min": 18,
    "genders": [1],
    "geo_locations": {
      "regions": [{"key":"3847"}],
      "cities": [
        {
          "key": "2430536",
          "radius": 12,
          "distance_unit": "mile"
        }
      ]
    },
    "interests": [{"id":6003139266461,"name":"Movies"}],
    "relationship_statuses": [
      2,
      3,
      4
    ]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

### Possible options

| Name | Description |
| --- | --- |
| `relationship_statuses`<br><br>type: array | Array of integers representing relationship status.<br><br>`1`: single<br><br>`2`: in_relationship<br><br>`3`: married<br><br>`4`: engaged<br><br>`6`: not specified<br><br>**Default:** `ALL`, if you specify Null or do not provide a value.<br><br>**Restrictions:** Do not use `0`. |
| `life_events`<br><br>type: array | Array of objects with 'id' and optional 'name' fields: `[{'id': 123, 'name': 'foo'}, {'id': 456}, 789]` |
| `industries`<br><br>type: array | Array of objects with 'id' and optional 'name' fields |
| `income`<br><br>type: array | Array of objects with 'id' and optional 'name' fields |
| `family_statuses`<br><br>type: array | Array of objects with 'id' and (optional) 'name' fields |

### Education and work {#education-and-workplace}
Use [Targeting Search API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#demo) for all options.

| Name | Description |
| --- | --- |
| `education_schools`<br><br>type: array | Schools, colleges, and institutions.<br><br>**Limit:** 200 education schools.<br><br>**Example:** `[{id: 105930651606, 'name': 'Harvard University'}, {id: 105930651607}, 105930651608]` |
| `education_statuses`<br><br>type: array | Array of integers to target based on education level.<br><br>`1`: HIGH_SCHOOL<br><br>`2`: UNDERGRAD<br><br>`3`: ALUM<br><br>`4`: HIGH_SCHOOL_GRAD<br><br>`5`: SOME_COLLEGE<br><br>`6`: ASSOCIATE_DEGREE<br><br>`7`: IN_GRAD_SCHOOL<br><br>`8`: SOME_GRAD_SCHOOL<br><br>`9`: MASTER_DEGREE<br><br>`10`: PROFESSIONAL_DEGREE<br><br>`11`: DOCTORATE_DEGREE<br><br>`12`: UNSPECIFIED<br><br>`13`: SOME_HIGH_SCHOOL |
| `college_years`<br><br>type: array | Array of integers. College graduation<br><br>**Limit:** Earliest year allowed is 1980 |
| `education_majors`<br><br>type: array | Majors.<br><br>**Example:** `[{'id': 123, 'name': 'Computer Science'}, {'id': 456}, 789]`<br><br>**Limit:** 200 |
| `work_employers`<br><br>type: array | Company, organization, or workplace<br><br>**Example:** `[{'id':'50431654','name':'Microsoft'}, {'id':50431655}, 50431656]`<br><br>**Limit:**  200 |
| `work_positions`<br><br>type: array | Self-declared work. <br><br>**Example:** `[{'id':105763692790962, 'name':'Contractor'}, {'id':105763692790963}, 105763692790964]`<br><br>**Limit:** 200 |

## Custom audiences {#custom_audiences}

Create a [custom audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience) and add users. You can use the audience in targeting, either for inclusion or exclusion. Include up to 500 custom audiences in `custom_audiences` and 500 custom audiences in `excluded_custom_audiences`.

**Note:** `excluded_custom_audiences` in `targeting_specs` is different than `excluded_custom_audiences` in `APP_COMBINATION` Custom Audience.

| Field | Description |
| --- | --- |
| `custom_audiences`<br><br>type: array | Array of audience IDs or audience objects. `'id'` field only: `[123, 456]`, or `[{'id': 123}, {'id': 456}]` |
| `excluded_custom_audiences`<br><br>type: array | Array of audience IDs or audience objects. `'id'` field only: `[123, 456]`, or `[{'id': 123}, {'id': 456}]` |

```
targeting:{
     "geo_locations":{
       "countries":["US"],
     },
     "age_min":25,
     "age_max":40,
     "custom_audiences":[{"id":6004192254512}]}
     "excluded_custom_audiences":
       [{"id":6004192252847}],
 }
```

## Locales

Provide granular targeting on locale:

| Field | Description |
| --- | --- |
| `locales`<br><br>type: array | Locales, see [Targeting Search, Locales](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#locale). Indices in a sub-array 'locales'. Target Accounts Center accounts with language other than common language for a location. Provide an ID for the language, such as 5 for German. Limit: 50. See mapping of virtual 'locales' to language sets at [Targeting Search, Locale](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#locale) with `type=adlocale`. |

## Reach people interested in selected cities and regions

This feature expands upon our existing location targeting feature, by enabling advertisers to reach people who have shown intent to travel to, make purchases in, or general interest in the cities and regions you've selected, within the same country.  

* To opt in, set the `geo` parameter under `individual_setting` in `targeting_automation` to `1`.
* To opt out, set the `geo` parameter under `individual_setting` in  `targeting_automation` to `0`.

```json
"targeting": {
  "age_range": [25, 35],
  "geo_locations": {
    "countries": ["GB"],
    "cities": [{"key":"2430536", "radius":12, "distance_unit":"mile"}]
  },
  "targeting_automation": {
    "individual_setting": {
      "geo": 1
    }
  }
}
```

#### Limitations

This feature works when you have selected cities or regions in your location targeting (i.e., `geo_locations` field).

#### Example request

```bash
curl -X POST \
  -F 'name="advantage audience test"' \
  -F 'is_autobid="true"' \
  -F 'daily_budget="100"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'campaign_id="<CAMPAIGN_ID>"' \
  -F 'targeting={
    "age_range": [25,35],
    "geo_locations":
      {
        "cities": [{"key":"2430536","radius":12,"distance_unit":"mile"}]
      },
    "targeting_automation": {"individual_setting": {"geo": 1 } }}' \
  -F 'access_token="<ACCESS_TOKEN>"' \
https://facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

For more information about the feature, see [How to reach people interested in your selected cities and regions](https://www.facebook.com/business/help/726389026372510).

## Enable age and gender suggestions

**Warning:** Currently, this feature is available to select advertisers but will gradually roll out to all advertisers in the coming months.

To use age or gender as suggestions, simply configure the `individual_setting` parameter in the `targeting_automation` field. The API also returns this setting when you retrieve the ad set, if it exists for the ad set.

#### Limitations

* This feature is only available for the `OUTCOME_SALES` and `APP_INSTALLS` objectives.
* When using age and gender suggestions, Meta shows ads beyond these settings when doing so is likely to improve ad performance.

### Age as a suggestion

Set the `age` parameter under `individual_setting` in `targeting_automation` to `1`. Then, include the `age_range` field in your audience specification.

#### Example request

```json
{
  "geo_locations": {
    "countries": [
      "US"
    ]
  },
  "age_min": 18,
  "age_range": [25, 35],
  "targeting_automation": {
    "individual_setting": {
      "age": 1
    }
  }
}
```

### Gender as a suggestion

Set the `gender` parameter under `individual_setting` in `targeting_automation` to `1`.

#### Example request

```html
{
  "geo_locations": {
    "countries": [
      "US"
    ]
  },
  "age_min": 21,
  "genders":[1],
  "targeting_automation": {
    "individual_setting": {
      "gender": 1
    }
  }
}
```

### Create an ad set with suggestions

#### Example request

```html
 curl -X POST \
  -F 'name="advantage audience test"' \
  -F 'is_autobid="true"' \
  -F 'daily_budget="100"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'campaign_id="<CAMPAIGN_ID>"' \
  -F 'promoted_object={"pixel_id": "<PIXEL_ID>","custom_event_type": "PURCHASE"}' \
  -F 'targeting={
    "age_min": 18,
    "age_range": [25,35],
    "genders":[1],
    "geo_locations": {
      "countries": ["US"]
    },
    "targeting_automation": {"individual_setting": {"age": 1, "gender": 1 } }}' \
  -F 'access_token="<ACCESS_TOKEN>"' \
https://facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

#### Example response

```html
{
  "id": "<AD_SET_ID>",
}
```

### Retrieve an ad set with suggestions

#### Example request

```html
curl -X GET \
  -d 'fields="targeting"' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_SET_ID>/
```

#### Example response

```html
{
  "targeting": {
    "age_max": 65,
    "age_min": 19,
    "age_range": [
      25,
      35
    ],
    "genders": [
      1
    ],
    "geo_locations": {
      "countries": [
        "US"
      ],
      "location_types": [
        "home",
        "recent"
      ]
    },
    "targeting_relaxation_types": {
      "lookalike": 0,
      "custom_audience": 0
    },
    "targeting_automation": {
      "advantage_audience": 0,
      "individual_setting": {
        "age": 1,
        "gender": 1
      }
    }
  },
  "id": "<AD_SET_ID>",
}
```

## Custom broad category targeting {#broadcategories}

Use Broad Categories for custom targeting created or permissioned specifically for your account. To include the cooking category and small business owner category:

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "user_adclusters": [
      {"id":6002714885172,"name":"Cooking"},
      {"id":6002714898572,"name":"Small Business Owners"}
    ]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

To target based on BCT plus location and demographics:

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "relationship_statuses": [2],
    "user_adclusters": [{"id":6002714886772,"name":"Food & Dining"}]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

You have options:

| Name | Description |
| --- | --- |
| `user_adclusters`<br><br>type: array | Array of ID-name pairs for __BCT clusters__. See below for information on retrieving BCT's. Limit: 50 ID-name pairs. |

To query this targeting for Ad account, make an `HTTP GET`:

```
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/broadtargetingcategories
```

The response is an array of JSON key-value pairs:

| Name | Description |
| --- | --- |
| `id`<br><br>type: long | Use the broad category ID in the ad targeting spec |
| `name`<br><br>type: string | Name of broad category |
| `parent_category`<br><br>type: string | Parent category of broad category |
| `size_lower_bound`<br><br>type: int | Lower bound audience size of broad category |
| `size_upper_bound`<br><br>type: int | Upper bound audience size of broad category |
| `type`<br><br>type: int | 6=BCT |
| `type_name`<br><br>type: string | BCT |

## Resources

- [Targeting Search](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search)
- [Reach Estimate](https://developers.facebook.com/docs/marketing-api/reference/reach-estimate)
- [Targeting Descriptions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-description)
- [Custom Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience)
