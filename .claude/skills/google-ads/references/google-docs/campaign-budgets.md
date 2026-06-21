Campaign budgets (overview)
https://developers.google.com/google-ads/api/docs/campaigns/budgets/overview
Baixado para Google Ads API v23

# Campaign Budgets Overview

(Fallback URL: original .../campaigns/budgets returned 404; canonical is .../campaigns/budgets/overview.)

There are two types of campaign budgets: average daily budgets and campaign total budgets, used to manage spend for your Google Ads campaigns.

Working with budgets in the API:
- Create a budget (.../campaigns/budgets/create-budgets)
- Share a budget with one or more campaigns (.../campaigns/budgets/share-budgets)
- Assign a budget to one or more campaigns (.../campaigns/budgets/assign-budgets)
- Remove budgets (.../campaigns/budgets/remove-budgets)
- Track performance (.../campaigns/budgets/track-performance)
- Restrictions and errors (.../campaigns/budgets/restrictions-errors)

## Average daily budget
The average amount you're willing to spend per day for this campaign. Set with `amount_micros` of CampaignBudget. Google Ads spends evenly throughout the month using this as a baseline; over a month you won't pay more than daily budget x 30.4 (avg days/month).

## Campaign total budget
The total amount you're willing to spend over the entire campaign duration. Set with `total_amount_micros` of CampaignBudget. Available for Demand Gen, Search, Standard Shopping, Performance Max, and YouTube campaigns with specific start and end dates.

Campaign total budgets are available for these bidding strategy types:
- Demand Gen: Maximize conversions, Target CPA, Maximize conversion value, Target ROAS, Maximize clicks, Manual CPC
- Performance Max: Target ROAS, Maximize conversion value, Target CPA, Maximize conversions
- Search: Target ROAS, Maximize conversion value, Target CPA, Maximize conversions, Maximize clicks, Target impression share, Manual CPC
- Shopping: Target ROAS, Maximize clicks, Manual CPC
- Video (read-only in the API): Target CPM, Target CPV

Note: amount_micros is in micros (1,000,000 micros = 1 unit of currency).

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
