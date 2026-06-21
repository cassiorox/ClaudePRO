Deprecation and sunset (versioning / sunset schedule)
https://developers.google.com/google-ads/api/docs/sunset-dates
Baixado para Google Ads API v24

# Deprecation and sunset

## Page Summary

- When a new API version is released, a deprecated version is given a sunset date after which it will no longer be available.
- Google aims to keep at most four major versions available at any time, with major versions lasting around 12 months and minor versions around 10 months.
- You will need to perform at most two upgrades per year, and you can upgrade directly to a non-sequential later version.
- There is at least a 20-week overlap between the release of client libraries for the latest version and the sunset date of the version being retired.
- You can view the Google Ads API versions used by your project in the Google Cloud Console under APIs & Services.
- Deprecated versions are still usable but not the latest, while sunset versions are no longer functional and require an immediate upgrade.
- The timetable provides specific release, deprecation, and tentative sunset dates for available API versions, encouraging upgrades to the latest version.
- Specific client library versions support different Google Ads API versions as detailed in the provided tables for various programming languages.
- Feature deprecations, such as changes to conversion environment usage and handling of gclid/gbraid values, are also announced with effective dates and details on the developer blog.

With the release of a new [version](https://developers.google.com/google-ads/api/docs/concepts/versioning), a deprecated
version is given a sunset date, after which that version will no longer be
available. Here are some other guidelines to keep in mind:

- We strive to keep at most four major versions available at any one time.
- _Major_ versions have a lifespan of around **12 months**— _minor_
versions: 10 months.
- You'll have to perform at most **two upgrades per year**, and you don't have
to upgrade in strict sequential order—for instance, you can upgrade
from version (N) directly to version (N+2).
- The overlap between the date when all client libraries are released for the
latest version and the version to be sunset is at least 20 weeks.

Our [client libraries](https://developers.google.com/google-ads/api/docs/client-libs) support any available versions of a
service, so you can gradually upgrade by specifying different versions of used
services.

## Timetable

The following table lists the specific deprecation and sunset dates for each
available version, and projected release dates for future versions. We
encourage you to upgrade to the latest version as soon as feasible after its
release. The tentative date means that the sunset could happen any time in that
month, and the dates could change.
[Subscribe to the blog](https://ads-developers.googleblog.com/2024/09/subscribe-to-blog.html)
for API version sunset announcement reminders.

| API version | Release date | Sunset date | Upgrade guide |
| --- | --- | --- | --- |
| Released versions |
| [v21](https://developers.google.com/google-ads/api/docs/release-notes#v21_2025-08-06) | August 6, 2025 | August 2026 (tentative) | [Upgrade from v20 to v21](https://developers.google.com/google-ads/api/docs/upgrade#v20-v21) |
| [v22](https://developers.google.com/google-ads/api/docs/release-notes#v22_2025-10-15) | October 15, 2025 | October 2026 (tentative) | [Upgrade from v21 to v22](https://developers.google.com/google-ads/api/docs/upgrade#v21-v22) |
| [v23](https://developers.google.com/google-ads/api/docs/release-notes#v23_2026-01-28) | January 28, 2026 | February 2027 | [Upgrade from v22 to v23](https://developers.google.com/google-ads/api/docs/upgrade#v22-v23) |
| [v23.1](https://developers.google.com/google-ads/api/docs/release-notes#v23-1-2026-02-25) | February 25, 2026 | February 2027 | [Upgrade from v23 to v23.1](https://developers.google.com/google-ads/api/docs/upgrade#v23-v23_1) |
| [v23.2](https://developers.google.com/google-ads/api/docs/release-notes#v23-2-2026-03-25) | March 25, 2026 | February 2027 | [Upgrade from v23.1 to v23.2](https://developers.google.com/google-ads/api/docs/upgrade#v23_1-v23_2) |
| [v24](https://developers.google.com/google-ads/api/docs/release-notes#v24-2026-04-22) | April 22, 2026 | May 2027 | [Upgrade from v23.2 to v24](https://developers.google.com/google-ads/api/docs/upgrade#v23_2-v24) |
| [v24.1](https://developers.google.com/google-ads/api/docs/release-notes#v24-1-2026-05-13) | May 13, 2026 | May 2027 | [Upgrade from v24 to v24.1](https://developers.google.com/google-ads/api/docs/upgrade#v24-v24_1) |
| Upcoming versions |
| v24.2 | June 2026 | May 2027 |  |
| v25 | July 2026 | August 2027 |  |
| v25.1 | August 2026 | August 2027 |  |
| v25.2 | September 2026 | August 2027 |  |
| v26 | October 2026 | November 2027 |  |
| v26.1\* | November 2026 | November 2027 |  |

\* v26.1 is designated as an optional release due to overlap with
the holiday season.

## View the versions your project is using

You can view a list of methods and services your project has recently called
using the [Google Cloud Console](https://console.cloud.google.com/):

1. Open the **APIs & Services** in the Google Cloud Console.
2. Click **Google Ads API** in the table.
3. On the **METRICS** subtab, you should see your recent requests plotted on
each graph. You can see which methods you've sent requests to in the
**Methods** table. The method name
includes a Google Ads API version, a service, and a method name, such as
`google.ads.googleads.v24.services.GoogleAdsService.Mutate`.
4. (Optional) Choose the timeframe you want to view for your requests.

## Differences between deprecation and sunset

| Term | Deprecation | Sunset |
| --- | --- | --- |
| **Definition** | The deprecated version is a version that is _not the latest one_. Once a new version is released, all previous versions will be marked **deprecated.** | The sunset version can _no longer be used_. Requests sent to this version will fail on or after the sunset date. |
| **Implication** | You can still use the deprecated versions until they're _sunset_, but the references of the deprecated versions are de-highlighted to show that they're not the latest version anymore. We encourage you to upgrade to the latest version as soon as possible to benefit from new features. | You need to upgrade from the sunset versions _immediately_ in order to use the Google Ads API. We _highly recommend_ that you upgrade to the _latest version_, using the [upgrade guide](https://developers.google.com/google-ads/api/docs/upgrade). |
| **Timing** | On average, we release a new version every 3 to 4 months, so the given version will be deprecated after approximately 3 to 4 months. | We aim to sunset a version 1 year after its release. |
| **API** | API endpoints for the deprecated versions _still function as usual_. You can access our API endpoints using our client libraries and REST. However, new features are not added to deprecated versions. | API endpoints for the sunset versions _stop working_ after the sunset dates. The Google Ads API will throw an error if you try to access the API endpoints of the sunset versions. |
| **[Client libraries](https://developers.google.com/google-ads/api/docs/client-libs)** | For purposes of providing compact client libraries, we _will stop including_ deprecated API versions in a new client library version after the deprecation date. This helps you save space when incorporating our client libraries in your projects. | Client libraries _no longer support_ the sunset API versions in any new client library versions after the sunset dates. |
| **[Support](https://developers.google.com/google-ads/api/support)** | We provide regular support for the deprecated versions. | The sunset versions are _no longer supported_ after the sunset date. |

## Supported client library versions

The table shows which client libraries work with which API versions.

### Java

|     |     |
| --- | --- |
| ##### Google Ads API | ##### Client library for Java |
| `v24` | Min:`43.0.0` Max: - |
| `v23` | Min:`42.0.0` Max: - |
| `v22` | Min:`41.0.0` Max: - |
| `v21` | Min:`39.0.0` Max: - |

### C\#

|     |     |
| --- | --- |
| ##### Google Ads API | ##### Client library for .NET |
| `v24` | Min:`25.3.0` Max: - |
| `v23` | Min:`25.1.0` Max: - |
| `v22` | Min:`24.1.0` Max: - |
| `v21` | Min:`24.0.0` Max: - |

### PHP

|     |     |
| --- | --- |
| ##### Google Ads API | ##### Client library for PHP |
| `v24` | Min:`33.3.0` Max: - |
| `v23` | Min:`32.2.0` Max: - |
| `v22` | Min:`31.0.0` Max: - |
| `v21` | Min:`28.0.0` Max: - |

### Python

|     |     |
| --- | --- |
| ##### Google Ads API | ##### Client library for Python |
| `v24` | Min:`30.1.0` Max: - |
| `v23` | Min:`29.2.0` Max: - |
| `v22` | Min:`28.1.0` Max: - |
| `v21` | Min:`28.0.0` Max: - |

### Ruby

|     |     |
| --- | --- |
| ##### Google Ads API | ##### Client library for Ruby |
| `v24` | Min:`40.0.0` Max: - |
| `v23` | Min:`38.0.0` Max: - |
| `v22` | Min:`36.0.0` Max: - |
| `v21` | Min:`35.0.0` Max: - |

### Perl

|     |     |
| --- | --- |
| ##### Google Ads API | ##### Client library for Perl |
| `v24` | Min:`32.0.0` Max: - |
| `v23` | Min:`31.0.0` Max: - |
| `v22` | Min:`29.0.0` Max: - |
| `v21` | Min:`28.0.0` Max: - |

## Feature deprecations

Regularly monitor the [Google Ads developer blog](https://ads-developers.googleblog.com/)
to be the first to hear about upcoming feature deprecations.

The following table lists the specific feature deprecations that are
planned for the Google Ads API. More details for each deprecation can be found in the
linked blog posts.

| Feature | Description | Effective date | Additional notes |
| --- | --- | --- | --- |
| Data retention policy change | The retention period for granular reporting data (daily, hourly, weekly) is being reduced to 37 months. High-level data (monthly, quarterly, yearly) remains available for 11 years. | June 1, 2026 | See [our blog post](https://ads-developers.googleblog.com/2026/05/new-data-retention-policy-for-google.html) for more details. |
| Changes to offline conversions support | As of June 15, 2026, developer tokens with no recent offline conversion requests must use the Data Manager API for their offline conversion workflows. If your developer token sent an [`UploadClickConversions`](https://developers.google.com/google-ads/api/reference/rpc/v24/ConversionUploadService/UploadClickConversions) request between December 17, 2025 and June 15, 2026, you can continue to use your developer token with the Google Ads API for offline conversion workflows. However, we recommend that you [upgrade your offline conversion workflows to the Data Manager API](https://developers.google.com/data-manager/api/devguides/events/google-ads/offline/upgrade) for an improved developer experience and access to additional features. Otherwise, as of June 15, 2026, any [`UploadClickConversions`](https://developers.google.com/google-ads/api/reference/rpc/v24/ConversionUploadService/UploadClickConversions) request will fail with the error `CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE`. [Use the Data Manager API](https://developers.google.com/data-manager/api/devguides/events/google-ads/offline) for your offline conversion workflows instead of the Google Ads API. | June 15, 2026 | See [our blog post](https://ads-developers.googleblog.com/2026/05/changes-to-offline-click-conversion.html) for more details. |
| Changes to Customer Match support | As of April 1, 2026, developer tokens with no recent Customer Match requests must use the Data Manager API for their Customer Match workflows. If your developer token sent an [`OfflineUserDataJobService`](https://developers.google.com/google-ads/api/reference/rpc/v24/OfflineUserDataJobService) or [`UserDataService`](https://developers.google.com/google-ads/api/reference/rpc/v24/UserDataService) request for Customer Match audiences between October 1, 2025 and March 31, 2026, you can continue to use your developer token with the Google Ads API for Customer Match workflows. However, we recommend that you [upgrade your Customer Match workflows to the Data Manager API](https://developers.google.com/data-manager/api/devguides/audiences/google-ads/customer-match/upgrade) for an improved developer experience and access to additional features. Otherwise, as of April 1, 2026, any [`OfflineUserDataJobService`](https://developers.google.com/google-ads/api/reference/rpc/v24/OfflineUserDataJobService) or [`UserDataService`](https://developers.google.com/google-ads/api/reference/rpc/v24/UserDataService) request for Customer Match audiences will fail with the error `CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE`. [Use the Data Manager API](https://developers.google.com/data-manager/api/devguides/audiences/google-ads/customer-match) for your Customer Match workflows instead of the Google Ads API. | April 1, 2026 | See [our blog post](https://ads-developers.googleblog.com/2026/03/changes-to-customer-match-support-in.html) for more details. |
| Changes to IP address and session attribute support | The Google Ads API no longer accepts new adopters of session attributes or IP address data as part of conversion imports. Existing users should migrate to the Data Manager API. | February 2, 2026 | See [our blog post](https://ads-developers.googleblog.com/2026/01/changes-to-ip-address-and-session.html) for more details. |
| Call-only ads deprecation | New call-only ads cannot be created. Existing call-only ads will stop serving in February 2027 and API support will be removed. Advertisers should use Responsive Search Ads with call assets instead. | January 2026 | See [our blog post](https://ads-developers.googleblog.com/2025/10/upgrade-your-call-only-ads-to.html) for more details. |
