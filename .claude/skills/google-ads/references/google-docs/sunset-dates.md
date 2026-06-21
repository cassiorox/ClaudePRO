Deprecation and sunset (versioning / sunset schedule)
https://developers.google.com/google-ads/api/docs/sunset-dates
Baixado para Google Ads API v23

# Deprecation and sunset

When a new version is released, a deprecated version is given a sunset date, after which it is no longer available. Guidelines:
- At most four major versions available at any one time.
- Major versions last around 12 months; minor versions around 10 months.
- At most two upgrades per year; you can upgrade non-sequentially (e.g., N directly to N+2).
- At least a 20-week overlap between all client libraries being released for the latest version and the sunset of the version being retired.

## Timetable (release / sunset dates)

Released versions:

| API version | Release date | Sunset date |
| --- | --- | --- |
| v21 | August 6, 2025 | August 2026 (tentative) |
| v22 | October 15, 2025 | October 2026 (tentative) |
| v23 | January 28, 2026 | February 2027 |
| v23.1 | February 25, 2026 | February 2027 |
| v23.2 | March 25, 2026 | February 2027 |
| v24 | April 22, 2026 | May 2027 |
| v24.1 | May 13, 2026 | May 2027 |

Upcoming versions:

| API version | Release date | Sunset date |
| --- | --- | --- |
| v24.2 | June 2026 | May 2027 |
| v25 | July 2026 | August 2027 |
| v25.1 | August 2026 | August 2027 |
| v25.2 | September 2026 | August 2027 |
| v26 | October 2026 | November 2027 |
| v26.1* | November 2026 | November 2027 |

* v26.1 is an optional release due to overlap with the holiday season.

NOTE on versions: As of this scrape (page updated 2026-06-10), the latest released version is v24.1 and the latest stable major is v24 (released April 22, 2026). v23 was released January 28, 2026 with sunset date February 2027. The earlier versions v21 (sunset August 2026 tentative) and v22 (sunset October 2026 tentative) are the next to be retired. Reference RPC docs link to /v24/ as current.

## Differences between deprecation and sunset
- Deprecation: a version that is not the latest. Once a new version is released, all previous versions are marked deprecated. Deprecated versions still function as usual via client libraries and REST, but no new features are added. New release cadence is roughly every 3-4 months.
- Sunset: the version can no longer be used. Requests sent to a sunset version fail on or after the sunset date. Aim is to sunset a version ~1 year after its release. Client libraries no longer support sunset versions after the sunset date.

## Supported client library versions (minimum)

Java: v24 -> 43.0.0; v23 -> 42.0.0; v22 -> 41.0.0; v21 -> 39.0.0
.NET (C#): v24 -> 25.3.0; v23 -> 25.1.0; v22 -> 24.1.0; v21 -> 24.0.0
PHP: v24 -> 33.3.0; v23 -> 32.2.0; v22 -> 31.0.0; v21 -> 28.0.0
Python: v24 -> 30.1.0; v23 -> 29.2.0; v22 -> 28.1.0; v21 -> 28.0.0
Ruby: v24 -> 40.0.0; v23 -> 38.0.0; v22 -> 36.0.0; v21 -> 35.0.0
Perl: v24 -> 32.0.0; v23 -> 31.0.0; v22 -> 29.0.0; v21 -> 28.0.0

## Feature deprecations (selected)

| Feature | Description | Effective date |
| --- | --- | --- |
| Data retention policy change | Granular reporting data (daily, hourly, weekly) retention reduced to 37 months. High-level data (monthly, quarterly, yearly) stays 11 years. | June 1, 2026 |
| Changes to offline conversions support | Developer tokens with no recent offline conversion requests must use the Data Manager API. UploadClickConversions requests fail with CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE if not allowlisted. | June 15, 2026 |
| Changes to Customer Match support | Developer tokens with no recent Customer Match requests must use the Data Manager API. OfflineUserDataJobService / UserDataService requests for Customer Match fail with CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE if not allowlisted. | April 1, 2026 |
| IP address and session attribute support | API no longer accepts new adopters of session attributes or IP address data in conversion imports; migrate to Data Manager API. | February 2, 2026 |
| Call-only ads deprecation | New call-only ads cannot be created. Existing call-only ads stop serving February 2027 and API support removed. Use Responsive Search Ads with call assets instead. | January 2026 |

Page last updated 2026-06-10 UTC.
