<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/basic-targeting.md | Scrape: 2026-08-09 | API v26.0 -->

# Basic Targeting



Basic targeting includes:

* [Demographics and Events](#demographics)
* [Location](#location)
* [Interests](#interests)
* [Behaviors](#behaviors)

**Note:** Advertisers running [housing, employment, credit ads, issues, election, or political ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) who are based in the United States or running ads targeted to the United States have different sets of restrictions.

## Demographics and events {#demographics}

Get basic [demographic](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#demo) and location-based targeting data to define targeting from [Targeting Search](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search), then specify options in the `targeting` spec, which contains [ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) attributes defining who should see the ad.

**Note:** You must specify at least one country in targeting, unless you use a [Custom Audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience).

### Targeting by demographic

```html
curl -X POST \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
      "geo_locations": {"countries":["US"]},
      "industries": [{"id":6009003307783,"name":"Accounting and finance"}],
      "life_events": [{"id":6003054185372,"name":"Recently Moved"}],
      "relationship_statuses": [2,4]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

#### Fields

| Name | Description |
| --- | --- |
| `genders`<br><br>array | Genders to target. Defaults to all. `1` targets males, `2` targets females. |
| `age_min`  <br><br>int | Minimum age. Defaults to 18. If used, must be 13 or higher. If the app has custom settings for age restrictions, the app's age restrictions will be used for ads with APP_INSTALL goals. For example, if you set `age_min` to 13 but your app's age minimum is set to 18, 18 will be used in ads targeting. |
| `age_max`<br><br>int | Maximum age. If used, must be 65 or lower. |
| `user_age_unknown`<br><br>boolean | Includes people on WhatsApp whose age is unknown.<br><br>Applies only to the WhatsApp Status placement<br><br>Starting May 2026, if the WhatsApp Status placement is included and this field is not set, it defaults to true.<br><br>Setting it to false allows businesses to exclude [people on WhatsApp whose age is unknown](https://www.facebook.com/business/help/717368264947302?id=176276233019487). Businesses will be able to opt out of including people on WhatsApp whose age is unknown at any time. |

## Location {#location}

Search and retrieve values for location targeting with [Targeting Search](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search). This targeting has two parameters: `geo_locations` to target locations, and optionally, `excluded_geo_locations` to exclude areas.

Use `country_groups` for `geo_locations` to target broader geographic regions such as Europe or North America.

**Warning:** Using `radius` can cause an error, code: 100, subcode 1815946, when targeting multiple locations. We recommend creating an ad for each location or not using `radius` in your call.

### Fields

| Name | Description |
| --- | --- |
| `countries`<br><br>array | Country targeting. Requires array of country codes, see [Targeting Search, Countries](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#countries).  <br>**Example**: `'countries': ['US']` |
| `regions`<br><br>array | State, province, or region. Available values, see [Targeting Search, Regions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#regions). Limit: 200.  <br>**Example**: `'regions': [{'key':'3847'}]` |
| `cities`<br><br>array | Specify `key`, `radius`, and `distance_unit`. For `key`, see [Targeting Search, Cities](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#cities). `radius` is a distance around cities, from 10 to 50 miles or 17 to 80 kilometers. `distance_unit` is mile or kilometer. Limit: 250.  <br>**Example**: `'cities': [{'key':'2430536', 'radius':12, 'distance_unit':'mile'}]` |
| `zips`<br><br>array | Target Zip Code, See [targeting search API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#zipcode). Limit: 50,000 (formerly 2,500). If you provide more than 2,500, the system creates an array known as `location_cluster` which represents a set of zip codes.  <br>**Example**: `'zips':[{'key':'US:94304'},{'key':'US:00501'}]`<br><br>To read a `location_cluster` and see the locations targeted: `GET /location_cluster_ID` |
| `places`<br><br>array | Provide a specific [place](https://developers.facebook.com/docs/graph-api/reference/place). Limit: 200.  <br>**Example:** `"places":[{"key":129672430416115,"name":"SFO", "radius":10, "distance_unit":"mile"}]` |
| `custom_locations`<br><br>array | Available for all objectives. Provide exact location in latitude and longitude or address as the center of an area. Also specify radius for your location from .63 to 50 miles, or 1 to 80 kilometers. `distance_unit` is miles or kilometers; default is mile. Limit: 200. PO Box alone is not supported in `address_string`. You must provide at minimum, a street address.  <br>**Example:** `'custom_locations':[{'address_string': '1601 Willow Road, Menlo Park, CA', 'radius': 5},{'latitude': 36, 'longitude': -121.0, 'radius': 5, 'distance_unit': 'kilometer'},]` |
| `custom_locations.latitude`<br><br>float | Latitude of location |
| `custom_locations.longitude`<br><br>float | Longitude of location |
| `custom_locations.name`<br><br>string | Name for address. You can use with `latitude` and `longitude` values for geo location targeting without providing `address_string` |
| `custom_locations.radius`<br><br>float | Radius around latitude/longitude, in miles unless otherwise in `distance_unit`. From 0.63 to 50 miles, or 1 to 80 kilometers. |
| `custom_locations.distance_unit`<br><br>string | **Optional.**<br><br>`kilometer` or `mile`; default `mile` |
| `custom_locations.address_string`<br><br>string | Address at latitude/longitude, such as 1601 Willow Rd, Menlo Park, CA. Suggested format: street number street name, city, state/province, country. Exclude postal codes. |
| `geo_markets`<br><br>array | Geomarkets using Comscore Markets. Limit: 2500.  <br>**Example:** `'geo_markets':[{'key': 'COMSCORE_MARKET:2001', 'name': 'New York, NY'}, {'key': 'COMSCORE_MARKET:2051', 'name': 'New Orleans, LA'},]` |
| `electoral_district`<br><br>array | Key for electoral districts. Get districts at [Targeting Search, Electoral](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#electoral).  <br>**Example**: `'electoral_districts':[{'key':'US:AK00'},{'key':'US:CA01'},{'key':'US:NY14'}]` |
| `location_types`<br><br>array | The array `['home', 'recent']` is the only option available. If no `location_types` array is provided, it will default to `['home', 'recent']`.<br><br>* `recent`: People whose recent location is in a selected area, as determined from mobile device data. Not available to exclude locations.<br>* `home`: People whose stated location in their Facebook profile "current city" is in an area. Facebook validates this by IP and information from their friends' profile locations. |
| `country_groups`<br><br>array | Global geographical regions and free trade areas. See [Targeting Search, Country Groups](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#country_group).<br><br>Provide array of country group codes:<br><br>* `worldwide`: Worldwide.<br>* `africa`: Africa.<br>* `afta`: ASEAN Free Trade Area.<br>* `android_app_store`: paid apps supporting countries in Android app store.<br>* `android_free_store`: free apps supporting countries in Android app store.<br>* `apec`: Asia-Pacific Economic Cooperation.<br>* `asia`: Asia<br>* `caribbean`: Caribbean.<br>* `central_america`: Central America.<br>* `cisfta`: Commonwealth of Independent States Free Trade Area.<br>* `eea`: European Economic Area.<br>* `emerging_markets`: countries in Emerging Markets<br>* `europe`: Europe.<br>* `gcc`: Gulf Cooperation Council.<br>* `itunes_app_store`: supported countries for iTunes app store.<br>* `mercosur`: MERCOSUR.<br>* `nafta`: North American Free Trade Agreement.<br>* `north_america`: North America.<br>* `oceania`: Oceania.<br>* `south_america`: South America.<br><br>**Example**: `'country_groups': ['asia','mercosur']` |

### Examples

#### Target by countries

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
https://graph.facebook.com/v24.0/act_<AD_ACCOUNT_ID>/adsets
```

#### Location targeting with exclusions {#locations}

```html
curl -X POST \
  -F 'name="My Reach Ad Set"' \
  -F 'optimization_goal="REACH"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'targeting={
       "excluded_geo_locations": {
         "regions": [
           {
             "key": "3847"
           }
         ]
       },
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

#### Target by zip codes

```html
curl -X POST \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
      "geo_locations":{
          "zips":[{"key":"US:94304"},{"key":"US:00501"}]}
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

#### Target by custom locations, geomarkets, and location types

The following code sets up targeting for:

- 5 miles around 1601 Willow Road, Menlo Park, CA
- 5 kilometers around latitude: 36, longitude: -121.0
- COMSCORE_MARKETS 2001 and 2051

```html
curl -X POST \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {
      "custom_locations": [
        {"address_string":"1601 Willow Road, Menlo Park, CA","radius":"5"},
        {
          "latitude": "36",
          "longitude": "-121.0",
          "radius": "5",
          "distance_unit": "kilometer"
        }
      ],
      "geo_markets": [
        {"key":"COMSCORE_MARKET:2001","name":"New York, NY"},
        {"key":"COMSCORE_MARKET:2051","name":"New Orleans, LA"}
      ],
      "location_types": ["recent","home"]
    }
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

#### Search and targeting

To target males age 20-24 within 10 miles of Menlo Park, CA, or living in Texas or in Japan:

##### Step 1

First, get Japan's country code:

```html
curl -G \
  -d 'location_types=["country"]' \
  -d 'type=adgeolocation' \
  -d 'q=japan' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/search
```

##### Step 2
Get Texas's region code:

```html
curl -G \
  -d 'location_types=["region"]' \
  -d 'type=adgeolocation' \
  -d 'q=texas' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/search
```

##### Step 3
Search Menlo Park, CA city code:

```html
curl -G \
  -d 'location_types=["city"]' \
  -d 'type=adgeolocation' \
  -d 'q=menlo' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/search
```

##### Step 4
Provide `genders` and age as `age_min` and `age_max`.

##### Step 5
The targeting spec is ready with country, region, and city codes:

```html
curl \
  -F 'name=My First AdSet' \
  -F 'daily_budget=10000' \
  -F 'bid_amount=300' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'optimization_goal=REACH' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'promoted_object={"page_id":"<PAGE_ID>"}' \
  -F 'targeting={
    "age_max": 24,
    "age_min": 20,
    "device_platforms": ["mobile"],
    "genders": [1],
    "geo_locations": {
      "countries": ["JP"],
      "regions": [{"key":"3886"}],
      "cities": [
        {
          "key": "2420605",
          "radius": 10,
          "distance_unit": "mile"
        }
      ]
    },
    "publisher_platforms": ["facebook","audience_network"]
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

#### Target multiple cities

Set `custom_type` to `multi_city` and define either `country` or `country_group` as described before.

```html
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {
      "custom_locations": [
        {
          "custom_type": "multi_city",
          "min_population": 500000,
          "max_population": 1000000,
          "country": "BR"
        },
        {"custom_type":"multi_city","country_group":"Europe"}
      ],
      "location_types": ["recent","home"]
    }
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

##### Parameters

| Name | Description |
| --- | --- |
| `min_population`<br><br>int | The minimum population threshold on which the cities are chosen for targeting. |
| `max_population`<br><br>int | The maximum population threshold on which the cities are chosen for targeting. |

## Interest targeting {#interests}

Target based on interests from someone's timeline, from Pages liked or from keywords associated with Pages or apps someone uses. See [Targeting Search, Interests](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#interests).

To target people interested in soccer, first query:

```html
curl -G \
  -d 'type=adinterest' \
  -d 'q=soccer' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/search
```

Add this interest by `name` and `id` to a targeting spec, where `path` is the path of this interest in ads tools.

```html
curl -X POST \
  -F 'name="My First AdSet"' \
  -F 'daily_budget=10000' \
  -F 'bid_amount=300' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="REACH"' \
  -F 'campaign_id="<CAMPAIGN_ID>"' \
  -F 'promoted_object={
       "page_id": "<PAGE_ID>"
     }' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
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
       "genders": [
         1
       ],
       "age_max": 24,
       "age_min": 20,
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ],
       "device_platforms": [
         "mobile"
       ],
       "flexible_spec": [
         {
           "interests": [
             {
               "id": "<INTEREST_ID>",
               "name": "<INTEREST_NAME>"
             }
           ]
         }
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

Here's another example:

```html
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "interests": [
      {"id":6003139266461,"name":"Movies"},
      {"id":6003397425735,"name":"Tennis"},
      {"id":6003659420716,"name":"Cooking"}
    ]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

### Fields

| Name | Description |
| --- | --- |
| `interests`<br><br>array | Array  with `id` and optional `name` fields:  <br>`'interests':[{id: 6003139266461,<br>'name': 'Movies'}, {id: 6003139266462}, 6003139266463]` |

## Behavioral targeting {#behaviors}
Target based on digital activities, devices people use, past or intended purchases, and travel. View options at `Browse` such as Frequent Travelers. See [Targeting Search API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search#behaviors).

```html
curl -G \
  -d 'type=adTargetingCategory' \
  -d 'class=behaviors' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/search
```

Add the behavior to `targeting` spec:

```html
curl \
  -F 'name=My First AdSet' \
  -F 'daily_budget=10000' \
  -F 'bid_amount=300' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'optimization_goal=REACH' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'promoted_object={"page_id":"<PAGE_ID>"}' \
  -F 'targeting={
    "age_max": 24,
    "age_min": 20,
    "behaviors": [{"id":6002714895372,"name":"All frequent travelers"}],
    "device_platforms": ["mobile"],
    "genders": [1],
    "geo_locations": {
      "countries": ["JP"],
      "regions": [{"key":"3886"}],
      "cities": [
        {
          "key": "2420605",
          "radius": 10,
          "distance_unit": "mile"
        }
      ]
    },
    "interests": [{"id":6003107902433,"name":"Association football (Soccer)"}],
    "publisher_platforms": ["facebook","audience_network"]
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

Another example:

```html
curl -X POST \
  -F 'name="My AdSet"' \
  -F 'optimization_goal="REACH"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id="<CAMPAIGN_ID>"' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "behaviors": [
         {
           "id": 6007101597783,
           "name": "Business Travelers"
         },
         {
           "id": 6004386044572,
           "name": "Android Owners (All)"
         }
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

## Fields

| Name | Description |
| --- | --- |
| `behaviors`<br><br>array | Array  with `id` and optional `name` fields:  <br>`'behaviors':[{id: 6004386044572,<br>'name': 'Android Owners (All)'}, {id: 6004386044573}, 6004386044574]` |

## Learn more

- [Search Targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search) - Query for Facebook's native ads targeting options.
- [Audience Targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences)
- [Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category)  

Other targeting:

- [Audience Network](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audience-network) - Run ads on Audience Network and extend the reach of your link or app ads
