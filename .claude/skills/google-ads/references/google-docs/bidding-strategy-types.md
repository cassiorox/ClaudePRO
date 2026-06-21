Bidding strategy types (bidding)
https://developers.google.com/google-ads/api/docs/campaigns/bidding/strategy-types
Baixado para Google Ads API v23

# Bidding strategy types

(Fallback URL: original .../campaigns/bidding/bidding-overview returned 404. This page, strategy-types, gives the practical overview of bidding strategy types. A bidding-overview page also exists at .../campaigns/bidding/overview.)

A bidding strategy can be used as a standard strategy for a single campaign or as a portfolio strategy across multiple campaigns.

In the Google Ads API, bidding strategies are managed using one or both of:
- The `campaign_bidding_strategy` union field of the Campaign object — for standard strategies at the campaign level.
- The `BiddingStrategy` object — for portfolio strategies at the account level.

Any bidding strategy is defined by a single bidding scheme that matches its type and contains the relevant bids. The "Valid Contexts" column indicates whether a given BiddingStrategyType can be used as standard or portfolio.

| BiddingStrategyType | Bidding scheme | Valid Contexts | Description |
| --- | --- | --- | --- |
| COMMISSION (deprecated) | Commission | Standard | Hotel campaigns only. No longer available; use TARGET_ROAS or ENHANCED_CPC. |
| FIXED_CPM | FixedCpm | Standard | Manual fixed cost-per-thousand impressions. |
| MANUAL_CPA | ManualCpa | Standard | Bid per advertiser-specified action. Local Services campaigns only. |
| MANUAL_CPC | ManualCpc | Standard | Focus on clicks: use maximum CPC bids. |
| MANUAL_CPM | ManualCpm | Standard | CPM. Display Network Only campaigns. |
| MANUAL_CPV | ManualCpv | Standard | Manual cost per view. |
| MAXIMIZE_CONVERSIONS | MaximizeConversions | Portfolio, Standard | Maximize conversions with optional target CPA. |
| MAXIMIZE_CONVERSION_VALUE | MaximizeConversionValue | Standard | Maximize conversion value with optional target ROAS. |
| PAGE_ONE_PROMOTED (deprecated) | PageOnePromoted | Portfolio | No longer available; use TARGET_IMPRESSION_SHARE. |
| PERCENT_CPC | PercentCpc | Standard | Percent cost per click. |
| TARGET_CPA | TargetCpa | Portfolio | Target CPA (eligibility required). For standard tCPA, use MaximizeConversions with a target CPA. |
| TARGET_CPM | TargetCpm | Standard | Target CPM. |
| TARGET_CPV | TargetCpv | Standard | Target cost-per-view. |
| TARGET_IMPRESSION_SHARE | TargetImpressionShare | Portfolio, Standard | Target impression share. |
| TARGET_OUTRANK_SHARE (deprecated) | TargetOutrankShare | Portfolio | No longer available; use TARGET_IMPRESSION_SHARE. |
| TARGET_ROAS | TargetRoas | Portfolio | Target ROAS (eligibility required). For standard tROAS, use MaximizeConversionValue with a target ROAS. |
| TARGET_SPEND | TargetSpend | Portfolio, Standard | Maximize clicks. Set an average daily budget; Google Ads sets max CPC bids to get the most clicks within budget. |

Errors result from using a bidding scheme in the wrong context:
- Portfolio-only scheme in a standard strategy: BiddingError.INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE.
- Standard-only scheme in a portfolio strategy: BiddingStrategyError.BIDDING_STRATEGY_NOT_SUPPORTED.

## Bidding strategy recommendations
The API provides recommendation types to optimize bidding (e.g., MAXIMIZE_CONVERSIONS_OPT_IN recommends the maximize conversions strategy, with a suggested new budget if budget-constrained). Recommendations include predicted metrics comparable to baseline via the `impact` field. See the Optimization score and recommendations guide (.../docs/recommendations).

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving; RPC refs shown for v24).
