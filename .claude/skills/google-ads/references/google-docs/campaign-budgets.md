Campaign budgets (overview)
https://developers.google.com/google-ads/api/docs/campaigns/budgets/overview
Baixado para Google Ads API v24

# Campaign Budgets Overview

There are two types of campaign budgets:
[average daily budgets](https://support.google.com/google-ads/answer/6385083) and
[campaign total budgets](https://support.google.com/google-ads/answer/10486938),
which are used to manage the amount of money spent for your Google Ads campaigns.

This guide describes everything you need to know to work with campaign budgets
in the Google Ads API:

- [Create a budget](https://developers.google.com/google-ads/api/docs/campaigns/budgets/create-budgets)
- [Share a budget](https://developers.google.com/google-ads/api/docs/campaigns/budgets/share-budgets) with one or more campaigns
- [Assign a budget](https://developers.google.com/google-ads/api/docs/campaigns/budgets/assign-budgets) to one or more campaigns
- [Remove budgets](https://developers.google.com/google-ads/api/docs/campaigns/budgets/remove-budgets)
- [Track performance](https://developers.google.com/google-ads/api/docs/campaigns/budgets/track-performance)
- [Restrictions and errors](https://developers.google.com/google-ads/api/docs/campaigns/budgets/restrictions-errors)

## Average daily budget

This is the average amount you're willing to spend per day for this campaign.
You can set an average daily budget with
[`amount_micros`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignBudget#amount_micros) of
[`CampaignBudget`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignBudget).

Google Ads will try to spend your budget evenly throughout the month, using your
average daily budget as a baseline. For example, if your average daily budget
is $100, Google Ads will aim to show $100 worth of ads each day. On some days, you
might spend less than $100, and on others you might spend more, but over the
course of a month, you won't pay more than your daily budget times 30.4 (the
average number of days in a month).

## Campaign total budget

This is the total amount you're willing to spend over the entire duration of
the campaign. You can set a campaign total budget with
[`total_amount_micros`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignBudget#total_amount_micros) of
[`CampaignBudget`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignBudget). Campaign total budgets are
available for Demand Gen, Search, Standard Shopping, Performance Max, and
YouTube campaigns with specific start and end dates. This option is ideal when
you have a set amount you want to spend over a specific period.

Campaign total budgets are available for campaigns using the following [bidding
strategy types](https://developers.google.com/google-ads/api/docs/campaigns/bidding/strategy-types):

- **Demand Gen**: Maximize conversions, Target CPA, Maximize conversion value,
Target ROAS, Maximize clicks, Manual CPC
- **Performance Max**: Target ROAS, Maximize conversion value, Target CPA,
Maximize conversions
- **Search**: Target ROAS, Maximize conversion value, Target CPA, Maximize
conversions, Maximize clicks, Target impression share, Manual CPC
- **Shopping**: Target ROAS, Maximize clicks, Manual CPC
- **Video** (Read-only in the Google Ads API): Target CPM, Target CPV
