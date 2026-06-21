# Targeting specs (Basic Targeting)
Fonte: https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting/
Baixado para Meta Marketing API v25.0
(Nota: a URL original /audiences/reference/targeting-specs/ retorna 404 na v25; este e o doc oficial equivalente do `targeting` spec.)

---

# Basic Targeting

Updated: May 21, 2026

Basic targeting includes Demographics and Events, Location, Interests, and Behaviors. Get targeting data from Targeting Search, then specify options in the `targeting` spec (an ad set attribute defining who should see the ad).

Note: You must specify at least one country in targeting, unless you use a Custom Audience.

## Demographics and events

### Targeting by demographic (example)

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
| `genders` array | Genders to target. Defaults to all. `1` = males, `2` = females. |
| `age_min` int | Minimum age. Defaults to 18. If used, must be 13 or higher. App age restrictions override for APP_INSTALL goals. |
| `age_max` int | Maximum age. If used, must be 65 or lower. |
| `user_age_unknown` boolean | Includes people on WhatsApp whose age is unknown. Applies only to WhatsApp Status placement. From May 2026 defaults to true if placement included and not set. |

## Location

Two parameters: `geo_locations` to target, optionally `excluded_geo_locations` to exclude. Use `country_groups` to target broader regions. Using `radius` with multiple locations can cause error 100 subcode 1815946 — create one ad per location or omit radius.

### Fields

| Name | Description |
| --- | --- |
| `countries` array | Array of country codes. Example: `'countries': ['US']` |
| `regions` array | State/province/region. Limit 200. Example: `'regions': [{'key':'3847'}]` |
| `cities` array | Specify `key`, `radius` (10-50 mi / 17-80 km), `distance_unit`. Limit 250. Example: `[{'key':'2430536','radius':12,'distance_unit':'mile'}]` |
| `zips` array | Target Zip Code. Limit 50,000 (>2,500 creates a `location_cluster`). Example: `[{'key':'US:94304'}]` |
| `places` array | Specific place. Limit 200. Example: `[{"key":129672430416115,"name":"SFO","radius":10,"distance_unit":"mile"}]` |
| `custom_locations` array | Lat/long or address as center. Radius .63-50 mi / 1-80 km. Limit 200. PO Box alone not supported. |
| `custom_locations.latitude/longitude` float | Coordinates of location |
| `custom_locations.name` string | Name for address (use with lat/long without address_string) |
| `custom_locations.radius` float | Radius around lat/long. .63-50 mi or 1-80 km. |
| `custom_locations.distance_unit` string | `kilometer` or `mile` (default `mile`) |
| `custom_locations.address_string` string | Address at lat/long. Format: street, city, state/province, country. Exclude postal codes. |
| `geo_markets` array | Comscore Markets. Limit 2500. Example: `[{'key':'COMSCORE_MARKET:2001','name':'New York, NY'}]` |
| `electoral_district` array | Electoral districts. Example: `[{'key':'US:NY14'}]` |
| `location_types` array | `['home','recent']` is the only option; defaults to that. `recent` = recent location from mobile data (not for exclusions); `home` = stated current city. |
| `country_groups` array | Regions/free trade areas: worldwide, africa, afta, android_app_store, android_free_store, apec, asia, caribbean, central_america, cisfta, eea, emerging_markets, europe, gcc, itunes_app_store, mercosur, nafta, north_america, oceania, south_america. |

### Multi-city targeting

Set `custom_type` to `multi_city` with `country` or `country_group`, plus `min_population` and `max_population`.

## Interest targeting

Query interests via `type=adinterest`. Add to `targeting` via `interests` or inside `flexible_spec`.

```
curl \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "interests": [
      {"id":6003139266461,"name":"Movies"},
      {"id":6003397425735,"name":"Tennis"},
      {"id":6003659420716,"name":"Cooking"}
    ]
  }' \
  ...
```

### Fields

| Name | Description |
| --- | --- |
| `interests` array | Array with `id` and optional `name`. Example: `[{id:6003139266461,'name':'Movies'},{id:6003139266462}]` |

## Behavioral targeting

Query via `type=adTargetingCategory&class=behaviors`. Add to `targeting` via `behaviors`.

```
"behaviors": [
  {"id":6007101597783,"name":"Business Travelers"},
  {"id":6004386044572,"name":"Android Owners (All)"}
]
```

### Fields

| Name | Description |
| --- | --- |
| `behaviors` array | Array with `id` and optional `name`. Example: `[{id:6004386044572,'name':'Android Owners (All)'}]` |

## Other common targeting keys (seen in examples)

`facebook_positions` (e.g. `["feed"]`), `publisher_platforms` (e.g. `["facebook","audience_network"]`), `device_platforms` (e.g. `["mobile"]`), `flexible_spec` (AND/OR interest grouping).

## Learn more

- Targeting Search — query Facebook's native ads targeting options
- Detailed Targeting — multi-type search in a single request
- Special Ad Category
