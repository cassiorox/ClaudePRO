Conversion management (overview)
https://developers.google.com/google-ads/api/docs/conversions/overview
Baixado para Google Ads API v24

# Conversion management

A [conversion](https://support.google.com/google-ads/answer/6365) in Google Ads is when a
user performs some specified action after clicking an ad or viewing a Display
Network ad. Conversions represent customer interactions vital to your
advertising goals, such as purchasing a product, installing a mobile app, or
signing up for an email list.

[Conversion tracking](https://support.google.com/google-ads/answer/1722022) provides
key insights into users' actions after viewing or clicking an ad. You can keep
track of users who call, buy a product, install a mobile app, and more.

The Google Ads API lets you programmatically manage the end-to-end workflow for
conversion management. The conversion management guide is divided into the
following sections that include creating conversions, importing offline
conversions, adjusting conversion values, monitoring the health of your
conversions, and grouping conversion actions into conversion goals.

[Conversion action categories](https://developers.google.com/google-ads/api/docs/conversions/categories)
Guidance on how to identify which
[conversion action types](https://support.google.com/google-ads/answer/1722054)
align with your business objectives, and how they map to the Google Ads API.

[Getting started](https://developers.google.com/google-ads/api/docs/conversions/getting-started)
How to set your account up for conversion tracking, along with a detailed
[code example](https://developers.google.com/google-ads/api/docs/conversions/create-conversion-actions#code_example)
showing how to create a conversion action in the Google Ads API using the
Google Ads client libraries.

[Manage offline conversions](https://developers.google.com/google-ads/api/docs/conversions/upload-offline)
Implementation details on how to import
[offline conversions](https://support.google.com/google-ads/answer/2998031)
to measure real world transactions such as a qualified lead over the phone
or in-office payment. We recommend starting with (or upgrading to)
**Enhanced Conversions for Leads**, an updated offline conversion import
that utilizes first-party data, such as your customer email or phone number,
to get the most accurate measurement and performance.

[Manage online conversions](https://developers.google.com/google-ads/api/docs/conversions/upload-online)
Website conversion actions are measured using Google Tag, but you can use
the API to improve the accuracy and performance by supplementing your
existing conversion tags with first-party conversion data, like email
address, name, home address, and phone number using
**Enhanced Conversions for Web**.

[Manage call conversions](https://developers.google.com/google-ads/api/docs/conversions/upload-calls)
Implementation details for importing call conversions.

[Manage store sales conversions](https://developers.google.com/google-ads/api/docs/conversions/upload-store-sales-transactions)
Implementation details for importing offline transactions to the Google Ads API.

[Adjust conversions after import](https://developers.google.com/google-ads/api/docs/conversions/upload-adjustments)
Implementation details for how to modify conversions _after_ they've been
imported.

[Manage conversion value rules](https://developers.google.com/google-ads/api/docs/conversions/conversion-value-rules)
Details for setting up conversion value rules, which automatically modify
the value of a conversion if it meets user-defined criteria.

[Custom conversion variables](https://developers.google.com/google-ads/api/docs/conversions/conversion-custom-variables)
Details for setting up custom conversion variables, which you can use to
associate additional information, in the form of tags, to an imported
conversion.

[Conversion goals](https://developers.google.com/google-ads/api/docs/conversions/goals/overview)
Details for setting up conversion goals, which help you organize sets of
conversion actions in order to optimize towards your advertising goals.

[Monitor conversion import health](https://developers.google.com/google-ads/api/docs/conversions/upload-summaries)
How to retrieve [offline data diagnostics](https://support.google.com/google-ads/answer/13812240)
to review the overall health of your conversion import and adjustment
processes.

[Reporting](https://developers.google.com/google-ads/api/docs/conversions/reporting)
How to report on the performance of your conversion actions, plus a
[mapping](https://developers.google.com/google-ads/api/docs/conversions/reporting#map-metrics) of the different Google Ads
UI metrics to the Google Ads API.
