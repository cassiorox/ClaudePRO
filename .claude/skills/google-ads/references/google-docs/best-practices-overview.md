Best practices (optimization, errors, rate limits)
https://developers.google.com/google-ads/api/docs/best-practices/overview
Baixado para Google Ads API v23

# Best Practices

## Ongoing maintenance
- Keep your developer contact email in the API center up to date. This is the alias Google uses to contact you; if they can't reach you about compliance with the API T&C, your API access may be revoked. Avoid personal/unmonitored addresses.
- Subscribe to the API blog and Product blog to be informed of product changes, maintenance downtime, deprecation dates, etc.
- Keep your app compliant with the Google Ads API Terms and Conditions.

## Optimization

### Batch operations
Each API request has fixed costs (round-trip latency, serialization, back-end calls). Most mutate methods accept an array of operations. Batch multiple operations per request to reduce request count and fixed costs. Avoid single-operation requests. Example: to add 50,000 keywords, make 100 requests of 500 keywords each (or 10 of 5,000) instead of 50,000 single requests. There are limits on operations per request, so adjust batch size for optimal performance.

### Send sparse objects
The API supports sparse updates: populate only the fields you need to change or that are required. Fields not in the update_mask (FieldMask) are left unchanged. Sparse updates process faster and produce fewer errors. Example: a keyword-bid updater only needs ad group ID, criterion ID, and bid fields.

## Error handling and management

### Distinguish request sources
For user-initiated requests, prioritize a good UX: surface the specific error with context and offer resolution steps. For back-end requests, implement handlers per error type, plus a default handler (e.g., queue failed operation + error for human review).

### Distinguish error types
Common types: Authentication errors, Retryable errors, Validation errors, Sync-related errors. See Error Types and Common Errors guides.

### Sync back ends
Manual changes by users can desync your local DB. Address sync errors reactively, and proactively run a nightly sync job comparing Google Ads objects against your local database.

### Log errors
At minimum log: request ID, the operations that caused the error, and the error itself. Also useful: customer ID, API service, round-trip latency, number of retries, raw request/response.

### Monitor trends
Monitor trends in API errors to detect and address problems. Build your own or use commercial tools for dashboards and automated alerts.

## Development

### Use test accounts
Test accounts are Google Ads accounts that don't serve ads. Use them to experiment and test connectivity/campaign logic. Your developer token does NOT need to be approved to use a test account, so you can start developing immediately after requesting a token.

Next: API limits and quotas (.../docs/best-practices/quotas)

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
