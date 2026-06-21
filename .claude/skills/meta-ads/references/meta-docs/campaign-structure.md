# Campaign Structure (Marketing API Overview)
Fonte: https://developers.facebook.com/docs/marketing-api/campaign-structure/
Baixado para Meta Marketing API v25.0

---

# Overview

Updated: Jun 16, 2026

Use the Marketing API to automate advertising across Meta technologies. The API provides functions for ad creation, management, and performance analysis. You can programmatically generate ad campaigns, ad sets, and individual ads, allowing rapid deployment and iteration based on real-time performance data.

In addition to ad creation, you can:

- Update, pause, or delete ads
- Ensure that campaigns remain aligned with business objectives
- Access detailed insights and analytics to track ad performance and make data-driven decisions

## How it works

The Marketing API hierarchy: ad campaigns contain ad sets, which contain ads, which reference ad creatives.

### Ad campaigns

A campaign is the highest level organizational structure within an ad account and should represent a single objective (for example, to drive Page post engagement). Setting the objective of the campaign enforces validation on any ads added to that campaign to ensure they also have the correct objective.

### Ad sets

Ad sets are groups of ads used to configure the budget and period the ads should run for. All ads within an ad set should have the same targeting, budget, billing, optimization goal, and duration. Create an ad set for each target audience with your bid; ads in the set target the same audience with the same bid. One ad set per audience helps control spend per audience, schedule delivery, and provides per-audience metrics.

### Ad creatives

Ad creatives contain just the visual elements of the ad and you can't change them once they're created. Each ad account has a creative library to store creatives for reuse in ads.

### Ads

An ad object contains all of the information necessary to display an ad on Facebook, Instagram, Messenger, and WhatsApp, including the ad creative. Create multiple ads in each ad set to optimize ad delivery based on different images, links, video, text, or placements.

### Ad components

| Component | Ad Campaign | Ad Set | Ad |
| --- | --- | --- | --- |
| Objective | ✓ | | |
| Schedule | | ✓ | |
| Budget | | ✓ | |
| Bidding | | ✓ | |
| Audience | | ✓ | |
| Ad Creative | | | ✓ |
