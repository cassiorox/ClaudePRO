<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/conversions-api.md | Scrape: 2026-08-09 | API v26.0 -->

# Conversions API



The Conversions API is designed to create a connection between an advertiser's marketing data (such as website events, app events, business messaging events and offline conversions) from an advertiser's server, website platform, mobile app, or CRM to Meta systems that optimize ad targeting, decrease cost per result and measure outcomes.

Rather than maintaining separate connection points for each data source, advertisers can use the Conversions API to send multiple event types and reduce the number of separate integrations they maintain. In the case of direct integrations, this entails establishing a connection between an advertiser's server and Meta's Conversions API endpoint.

Server events are linked to a dataset ID and are processed like events sent using the Meta Pixel, Facebook SDK for iOS or Android, mobile measurement partner SDK, offline event set, or .csv upload. This means that server events may be used in measurement, reporting, or optimization in a similar way as other connection channels. Offline events may be used for attributed offline events measurement, offline custom audience creation or measurement.

For optimal ad performance and measurement, follow the [Conversions API best practices](https://developers.facebook.com/documentation/ads-commerce/conversions-api/best-practices).

### Recommended steps

1. [**Get Started**](https://developers.facebook.com/documentation/ads-commerce/conversions-api/get-started): Choose the integration method that works best for you, see prerequisites for using the API, and understand where to begin.
2. [**Implement the API and start sending requests**](https://developers.facebook.com/documentation/ads-commerce/conversions-api/using-the-api): Start making `POST` requests and learn more about dropped events, batch requests, and event transaction time.
3. [**Verify your setup**](https://developers.facebook.com/documentation/ads-commerce/conversions-api/verifying-setup): Confirm that Meta has received your events and that events are deduplicated and matched correctly.

## Documentation

### [API Parameters](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters)
Required and optional parameters you can use to improve ads attribution and delivery optimization.

### [Payload Helper](https://developers.facebook.com/documentation/ads-commerce/conversions-api/payload-helper)
See how your payload should be structured when it is sent to Meta from your server.

### [Troubleshooting](https://developers.facebook.com/documentation/ads-commerce/conversions-api/support)
Learn how to handle error codes returned by the Conversions API.

## Resources

### Meta Pixel Events

Learn more about the Meta Pixel's [Standard Events](https://developers.facebook.com/docs/facebook-pixel/implementation/conversion-tracking#standard-events) and [Custom Events](https://developers.facebook.com/docs/facebook-pixel/implementation/conversion-tracking#custom-events).

### Business Help Center

From our Help Center, see [About Conversions API](https://www.facebook.com/business/help/2041148702652965) and [Test Your Server Events](https://www.facebook.com/business/help/1624255387706033).

### Playbook

View the [Direct Integration Playbook for Developers (PDF)](https://www.facebook.com/gms_hub/share/conversions-api-direct-integration-playbook_english.pdf).

### [Data Processing Options](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/data-processing-options)

Learn more about the Limited Data Use feature and how to implement it for Conversions API.
