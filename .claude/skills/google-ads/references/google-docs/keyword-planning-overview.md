Keyword Planning (overview)
https://developers.google.com/google-ads/api/docs/keyword-planning/overview
Baixado para Google Ads API v23

# Keyword Planning

Keyword Planning is a process for getting keyword metrics and forecasts as well as searching for new keywords to add to campaigns.

Note: Keyword Planning services are rate limited, allowing fewer requests per minute compared to other services. It is recommended to cache or store results from Keyword Planning as responses do not change frequently, though historical metrics refresh monthly.

## Workflow

Here's a common workflow when using Keyword Planning.

1. Create a manageable list of ideas (.../docs/keyword-planning/generate-keyword-ideas). You can use historical search volume and CPC to reduce the list of keywords to be included in forecasts.
2. Generate forecast metrics (.../docs/keyword-planning/generate-forecast-metrics) for keywords in order to get traffic for keywords in the plan.
3. Create a new campaign with the new keywords.
4. Adjust the keywords and estimation parameters to find a setup which delivers your marketing goals using the keywords and CPC bids which you selected above.
5. Leave the campaign for the duration of the `forecast_period`. Forecasts are based on your campaign running unmodified for the duration of the forecast period. Changing the campaign, including bids and targeting prior to the forecast period, changes performance since daily and seasonal trends are also considered.

Keyword Planning in the API can do the following:

- Generate keyword ideas (.../docs/keyword-planning/generate-keyword-ideas)
- Generate ad group themes (.../docs/keyword-planning/generate-ad-group-themes)
- Generate historical metrics (.../docs/keyword-planning/generate-historical-metrics)
- Generate forecast metrics (.../docs/keyword-planning/generate-forecast-metrics)

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
