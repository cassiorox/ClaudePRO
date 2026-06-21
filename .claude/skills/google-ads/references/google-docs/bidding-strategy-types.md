Bidding strategy types (bidding)
https://developers.google.com/google-ads/api/docs/campaigns/bidding/strategy-types
Baixado para Google Ads API v24

# Bidding strategy types

video_library [Video library: Smart Bidding](https://developers.google.com/google-ads/api/videos/catalog#smart-bidding)

A [bidding strategy](https://support.google.com/google-ads/answer/2472725) can be used as a standard strategy for a single campaign or as a [portfolio strategy](https://support.google.com/google-ads/answer/6263072) across multiple campaigns.

In the Google Ads API, all bidding strategies are managed using one or both of the following:

- The [`campaign_bidding_strategy`](https://developers.google.com/google-ads/api/reference/rpc/v24/Campaign#campaign_bidding_strategy) union field of the [`Campaign`](https://developers.google.com/google-ads/api/reference/rpc/v24/Campaign) object for standard strategies at the campaign level.
- The [`BiddingStrategy`](https://developers.google.com/google-ads/api/reference/rpc/v24/BiddingStrategy) object for portfolio strategies at the account level.

Any bidding strategy is defined by a single bidding scheme that matches its type and contains the relevant bids.

In the following table, the **Valid Contexts** column indicates whether a given [`BiddingStrategyType`](https://developers.google.com/google-ads/api/reference/rpc/v24/BiddingStrategyTypeEnum.BiddingStrategyType) and its matching bidding scheme can be used in the context of **standard** or **portfolio** strategies.

| [BiddingStrategyType](https://developers.google.com/google-ads/api/reference/rpc/v24/BiddingStrategyTypeEnum.BiddingStrategyType) | Bidding scheme | Valid Contexts | Description |
| --- | --- | --- | --- |
| ~~`COMMISSION`~~ | ~~[`Commission`](https://developers.google.com/google-ads/api/reference/rpc/v24/Commission)~~ | **Standard** | Works only with Hotel campaigns.<br><br>No longer available. Use `TARGET_ROAS` or `ENHANCED_CPC` instead. |
| `FIXED_CPM` | [`FixedCpm`](https://developers.google.com/google-ads/api/reference/rpc/v24/FixedCpm) | **Standard** | A manual bidding strategy for a fixed cost-per-thousand impressions. |
| `MANUAL_CPA` | [`ManualCpa`](https://developers.google.com/google-ads/api/reference/rpc/v24/ManualCpa) | **Standard** | Lets advertiser set the bid per advertiser-specified action. This type of strategy is only available for Local Services campaigns. |
| `MANUAL_CPC` | [`ManualCpc`](https://developers.google.com/google-ads/api/reference/rpc/v24/ManualCpc) | **Standard** | Focus on clicks: Use maximum CPC bids. |
| `MANUAL_CPM` | [`ManualCpm`](https://developers.google.com/google-ads/api/reference/rpc/v24/ManualCpm) | **Standard** | CPM (Cost-per-thousand impressions).<br><br>Works only with Display Network Only campaigns. Using this bidding scheme with Search campaigns results in [`OperationAccessDeniedError.OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE`](https://developers.google.com/google-ads/api/reference/rpc/v24/OperationAccessDeniedErrorEnum.OperationAccessDeniedError#operation_not_permitted_for_campaign_type). |
| `MANUAL_CPV` | [`ManualCpv`](https://developers.google.com/google-ads/api/reference/rpc/v24/ManualCpv) | **Standard** | Manual cost per view (CPV). |
| `MAXIMIZE_CONVERSIONS` | [`MaximizeConversions`](https://developers.google.com/google-ads/api/reference/rpc/v24/MaximizeConversions) | **Portfolio**<br>**Standard** | Maximize conversions using an optional target CPA. As a portfolio strategy, it can be used with Search, Shopping, Express, and Performance Max campaigns. As a standard strategy, it can be used with Search, Display, Video, and App campaigns. |
| `MAXIMIZE_CONVERSION_VALUE` | [`MaximizeConversionValue`](https://developers.google.com/google-ads/api/reference/rpc/v24/MaximizeConversionValue) | **Standard** | Maximize conversion value using an optional target ROAS. |
| ~~`PAGE_ONE_PROMOTED`~~ | `PageOnePromoted` | **Portfolio** | Target search page location.<br><br>No longer available. Use `TARGET_IMPRESSION_SHARE` instead. |
| `PERCENT_CPC` | [`PercentCpc`](https://developers.google.com/google-ads/api/reference/rpc/v24/PercentCpc) | **Standard** | Percent cost per click (CPC). |
| `TARGET_CPA` | [`TargetCpa`](https://developers.google.com/google-ads/api/reference/rpc/v24/TargetCpa) | **Portfolio** | Target cost per acquisition (CPA): Must meet [eligibility requirements](https://support.google.com/google-ads/answer/6268632).<br><br>For standard target CPA behavior, use `MaximizeConversions` with a target CPA. |
| `TARGET_CPM` | [`TargetCpm`](https://developers.google.com/google-ads/api/reference/rpc/v24/TargetCpm) | **Standard** | Target cost-per-thousand impressions (CPM). |
| `TARGET_CPV` | [`TargetCpv`](https://developers.google.com/google-ads/api/reference/rpc/v24/TargetCpv) | **Standard** | Target cost-per-view (CPV). |
| `TARGET_IMPRESSION_SHARE` | [`TargetImpressionShare`](https://developers.google.com/google-ads/api/reference/rpc/v24/TargetImpressionShare) | **Portfolio**<br>**Standard** | Target impression share. |
| ~~`TARGET_OUTRANK_SHARE`~~ | `TargetOutrankShare` | **Portfolio** | Target outranking share.<br><br>No longer available. Use `TARGET_IMPRESSION_SHARE` instead. |
| `TARGET_ROAS` | [`TargetRoas`](https://developers.google.com/google-ads/api/reference/rpc/v24/TargetRoas) | **Portfolio** | Target return on ad spend: Must meet [eligibility requirements](https://support.google.com/google-ads/answer/6268637).<br><br>For standard target ROAS behavior, use `MaximizeConversionValue` with a target ROAS. |
| `TARGET_SPEND` | [`TargetSpend`](https://developers.google.com/google-ads/api/reference/rpc/v24/TargetSpend) | **Portfolio**<br>**Standard** | [Maximize clicks](https://support.google.com/google-ads/answer/6268626). Set an average daily budget and the Google Ads system sets your maximum cost per click (CPC) bids on your behalf, with the goal of getting you the most clicks possible within that budget. |

Errors result if you try to use a bidding scheme in the wrong context. For example:

- Using a portfolio-only bidding scheme in the context of a standard strategy generates a [`BiddingError.INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE`](https://developers.google.com/google-ads/api/reference/rpc/v24/BiddingErrorEnum.BiddingError#invalid_anonymous_bidding_strategy_type) error.
- Using a standard-only bidding scheme in the context of a portfolio strategy generates a [`BiddingStrategyError.BIDDING_STRATEGY_NOT_SUPPORTED`](https://developers.google.com/google-ads/api/reference/rpc/v24/BiddingStrategyErrorEnum.BiddingStrategyError#bidding_strategy_not_supported) error.

## Bidding strategy recommendations

The Google Ads API provides several [recommendation](https://support.google.com/google-ads/answer/3448398) types which can help you optimize your campaign bidding strategies. For example, the [`MAXIMIZE_CONVERSIONS_OPT_IN`](https://developers.google.com/google-ads/api/reference/rpc/v24/Recommendation#maximize_conversions_opt_in_recommendation) type recommends using the maximize conversions bidding strategy for your campaigns. In cases where the campaign would be budget-constrained at the current budget with the new bidding strategy, the recommendation also provides a suggested new [budget amount](https://developers.google.com/google-ads/api/reference/rpc/v24/Recommendation.MaximizeConversionsOptInRecommendation#recommended_budget_amount_micros).

One benefit of using recommendations for bidding optimization is that the [`Recommendation`](https://developers.google.com/google-ads/api/reference/rpc/v24/Recommendation) provides predicted metrics that you can use to estimate how performance might change as a result of applying the recommendation. These predicted metrics can be compared to the baseline metrics using values directly from the [`impact`](https://developers.google.com/google-ads/api/reference/rpc/v24/Recommendation#impact) field of the recommendation.

For additional recommendation types and guidance on working with recommendations in the Google Ads API, visit the [Optimization score and recommendations](https://developers.google.com/google-ads/api/docs/recommendations) guide.
