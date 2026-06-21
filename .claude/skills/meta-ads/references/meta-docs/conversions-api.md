# Conversions API (CAPI)
Fonte: https://developers.facebook.com/docs/marketing-api/conversions-api/
Baixado para Meta Marketing API v25.0

---

# Conversions API

Updated: Feb 25, 2026

The Conversions API creates a connection between an advertiser's marketing data (website events, app events, business messaging events, offline conversions) from a server, website platform, mobile app, or CRM to Meta systems that optimize ad targeting, decrease cost per result, and measure outcomes.

Rather than maintaining separate connection points for each data source, advertisers can use the Conversions API to send multiple event types and simplify their tech stack. For direct integrations, this means a connection between the advertiser's server and Meta's Conversions API endpoint.

Server events are linked to a dataset ID and are processed like events sent via the Meta Pixel, Facebook SDK (iOS/Android), MMP SDK, offline event set, or .csv upload. Server events may be used in measurement, reporting, or optimization. Offline events may be used for attributed offline event measurement, offline custom audience creation, or measurement.

For optimal performance, follow the Conversions API best practices.

## Recommended Steps

- **Get Started** — Choose an integration method, see prerequisites, understand where to begin. (/conversions-api/get-started)
- **Implement the API and start sending requests** — Make POST requests; learn about dropped events, batch requests, event transaction time. (/conversions-api/using-the-api)
- **Verify your setup** — Confirm events are received, deduplicated, and matched correctly. (/conversions-api/verifying-setup)

## Documentation

- **API Parameters** — Required and optional parameters to improve ads attribution and delivery optimization. (/conversions-api/parameters)
- **Payload Helper** — How your payload should be structured when sent to Facebook. (/conversions-api/payload-helper)
- **Troubleshooting** — How to handle error codes returned by the Conversions API. (/conversions-api/support)

## Resources

- Meta Pixel Standard Events and Custom Events
- Business Help Center: About Conversions API, Test Your Server Events
- Direct Integration Playbook for Developers (PDF)
- Data Processing Options — Limited Data Use feature for Conversions API. (/marketing-api/overview/data-processing-options)
