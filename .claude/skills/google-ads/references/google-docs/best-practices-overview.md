Best practices (optimization, errors, rate limits)
https://developers.google.com/google-ads/api/docs/best-practices/overview
Baixado para Google Ads API v24

# Best Practices

ondemand_video [Video: Check out the best practices talk from the 2019 workshop](https://www.youtube.com/watch?v=J9zVoWT7twk&list=None&start=None)

This guide covers some best practices you can implement to optimize
the efficiency and performance of your apps.

## Ongoing maintenance

To ensure that your app runs uninterrupted:

- Keep your developer contact email in the API center up to date.
This is the alias we use to contact you. If we're unable to contact you
regarding compliance with the API Terms and Conditions, your API access
may be revoked without your prior knowledge. Avoid using a personal email
address tied to an individual or unmonitored account. To view the API
center, you must be logged in to your manager account.

- To be informed of issues such as product changes, maintenance downtime,
deprecation dates, and so on, subscribe to our

  - [API blog](https://ads-developers.googleblog.com/search/label/google_ads_api)
  - [Product blog](https://blog.google/products/ads-commerce/)
- Keep your app compliant with the Google Ads API
[Terms and Conditions](https://developers.google.com/google-ads/api/docs/api-policy/terms) (T&C).
If required, the token review and compliance team will reach out to you
using your contact email. If you have questions or concerns about
the T&C, you can reach out to the review team by responding to
the email they sent you when reviewing your developer token application.


## Optimization

You can optimize your app by running batch operations and, if appropriate,
sending sparse objects.

### Batch operations

Making a request to the API entails a number of fixed costs, such as
round-trip network latency, serialization and deserialization processing, and
calls to back-end systems. To lessen the impact of these fixed costs and
increase overall performance, most mutate methods in the API are designed to
accept an array of operations. By batching multiple operations into each
request, you can reduce the number of requests you make and the associated
fixed costs. If you can, avoid making requests with only one operation.

For example, suppose you're adding 50,000 keywords to a campaign across multiple
ad groups. Instead of making 50,000 requests with 1 keyword each,
make 100 requests with 500 keywords each, or even 10 requests with
5,000 keywords each. There are limits on the number of operations
allowed in a request, so you may need to adjust your batch size to achieve
optimal performance.

### Send sparse objects

When objects are sent to the API, fields must be deserialized, validated,
and stored in the database. Passing in full objects when you only want to update
a few fields can result in extra processing time and decreased performance.
To mitigate this, the Google Ads API supports sparse updates, allowing you
to populate only the fields in an object that you need to change or that are
required. Sparse updates process faster and are less likely to produce errors.
Fields that aren't in the update_mask (also known as `FieldMask`) are left
unchanged.

For example, an app that updates keyword-level bids can benefit from using
sparse updates, as only the ad group ID, criterion ID, and bids fields would
need to be populated.

## Error handling and management

During development, you're likely to encounter errors. This section describes
considerations and strategies for building error management into your app.
In addition to this section, visit the [Troubleshooting
guide](https://developers.google.com/google-ads/api/docs/best-practices/troubleshooting) for more information on managing
errors.

### Distinguish request sources

Some apps are primarily interactive, issuing API calls directly in response
to user-initiated actions in a UI. Others work primarily offline, issuing
API calls as part of a periodic back-end process. Many apps combine the two.
When thinking about error management, it can be useful to distinguish these
different types of requests.

For user-initiated requests, your primary concern should be providing a good
experience for your users. Use the specific error that occurred to provide the
user with as much context as you can in the UI. Offer easy steps they can take
to resolve the error (check out the suggestions below).

For requests initiated on the back end, implement handlers for the different
types of errors your app may encounter. Always include a default handler to
address rare or previously unencountered errors. A good approach for a default
handler is to add the failed operation and error to a queue for a human operator
to review and determine an appropriate resolution.

### Distinguish error types

Knowing the differences between error types in Google Ads API is crucial when
building robust error handling. Some of the most common error types are:

1. [Authentication errors](https://developers.google.com/google-ads/api/docs/best-practices/error-types#authentication_errors)
2. [Retryable errors](https://developers.google.com/google-ads/api/docs/best-practices/error-types#retryable_errors)
3. [Validation errors](https://developers.google.com/google-ads/api/docs/best-practices/error-types#validation_errors)
4. [Sync-related errors](https://developers.google.com/google-ads/api/docs/best-practices/error-types#sync-related_errors)

Refer to [Error Types](https://developers.google.com/google-ads/api/docs/best-practices/error-types) and
[Common Errors](https://developers.google.com/google-ads/api/docs/common-errors) for more details.

### Sync back ends

If your app's users have manual access to Google Ads accounts, they may make
changes that your app is not aware of, causing your app's local database to go
out of sync. As noted in our [Error Types](https://developers.google.com/google-ads/api/docs/best-practices/error-types) guide,
you can address sync-related errors reactively when they occur, but you can also
try to prevent them proactively. One proactive strategy is to run a nightly
sync job on all your accounts, retrieving the Google Ads objects in your
accounts and comparing against your local database.

### Log errors

All errors should be logged to facilitate debugging and monitoring. At a
minimum, log the request ID, the operations that caused the error, and the
error itself. Other information to log includes customer ID, API service,
round-trip request latency, number of retries, and the raw request and response.

### Monitor trends

Be sure to monitor trends in API errors so that you can detect and address
problems with your app. Consider building your own solution or employing one
of many available commercial tools that can use your logs to produce interactive
dashboards and send automated alerts.

## Development

Use test accounts during development.

### Use test accounts

[Test accounts](https://developers.google.com/google-ads/api/docs/best-practices/test-accounts) are Google Ads
accounts that don't actually serve ads. You can use a test account to
experiment with the Google Ads API and test that your app's connectivity, campaign
management logic, or other processing are working as expected. Your developer
token does not need to be approved to be used on a test account, so you can
start developing with the Google Ads API immediately after requesting a developer
token, even before your app is reviewed.

[Next: API limits and quotas](https://developers.google.com/google-ads/api/docs/best-practices/quotas)
