Keyword Planning (overview)
https://developers.google.com/google-ads/api/docs/keyword-planning/overview
Baixado para Google Ads API v24

# Keyword Planning

Keyword Planning is a process for [getting keyword metrics and
forecasts](https://support.google.com/google-ads/answer/3022575) as well as
[searching for new keywords](https://support.google.com/google-ads/answer/6325025) to
add to campaigns.

## Workflow

Here's a common workflow when using Keyword Planning.

1. Create a manageable list of
[ideas](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas). You can use
historical search volume and CPC to reduce the list of keywords to be
included in forecasts.
2. Generate [forecast
metrics](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-forecast-metrics) for keywords in
order to get traffic for keywords in the plan.
3. Create a new campaign with the new keywords.
4. Adjust the keywords and estimation parameters to find a setup which delivers
your marketing goals using the keywords and CPC bids which you selected
above.
5. Leave the campaign for the duration of the
[`forecast_period`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordForecastMetricsRequest#forecast_period).
Forecasts are based on your campaign running unmodified for the duration of
the forecast period. Changing the campaign, including bids and targeting
prior to the forecast period, changes performance since daily and seasonal
trends are also considered.

Keyword Planning in the API can do the following:

- [Generate keyword ideas](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas)
- [Generate ad group
themes](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-ad-group-themes)
- [Generate historical
metrics](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics)
- [Generate forecast
metrics](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-forecast-metrics)
