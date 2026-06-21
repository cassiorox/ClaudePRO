Responsive search ads (RSA)
https://developers.google.com/google-ads/api/docs/responsive-search-ads/overview
Baixado para Google Ads API v23

# Responsive Search Ads

(Fallback URL: original .../ads/responsive-search-ad returned 404; canonical is .../responsive-search-ads/overview.)

Use responsive search ads (RSA) to promote products on the Google Network. Main features:
- Set three or more headlines and two or more descriptions that automatically rotate into the ad to determine which work best.
- Pin any headlines and descriptions so that they always appear in the ad.
- Collect performance statistics on different combinations; the system automatically favors combinations that work well together.
- Display customized URLs by specifying path1 and path2, appended to your landing page domain to form the displayed URL.

## Format
RSAs are displayed with three headlines and two descriptions at serve time, plus a customizable URL based on the landing page domain and your path1/path2 fields.

Headlines and descriptions are represented as arrays of an AdTextAsset resource.

## Pinning
RSAs support pinning. For finer control than letting the system mix and match, pin headlines/descriptions to specific positions. For example, to always show a specific headline first, set that AssetLink to have a pinnedField of HEADLINE_1. When the ad is served, that text appears in the first headline position and the other fields are drawn from the pool of remaining assets. If more than one asset is pinned to a position, that position rotates text between all assets pinned to it.

Next: Create responsive search ads (.../responsive-search-ads/create-responsive-search-ads) — ad creation is done with AdGroupAdService.

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
