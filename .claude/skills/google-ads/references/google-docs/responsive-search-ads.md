Responsive search ads (RSA)
https://developers.google.com/google-ads/api/docs/responsive-search-ads/overview
Baixado para Google Ads API v24

# Responsive Search Ads

Use responsive search ads to promote products on the [Google Network](https://support.google.com/google-ads/answer/1752334). The main features of [responsive search ads](https://support.google.com/google-ads/answer/7684791) are that they let you:

- Set three or more headlines and two or more descriptions that will automatically rotate into the ad to determine which work best.
- Pin any headlines and descriptions you want so that they always appear in the ad.
- Collect performance statistics on different combinations of headlines and descriptions so you can determine their effectiveness. The system automatically favors headline and description combinations which work well together.
- Display customized URLs by specifying `path1` and `path2`, which are then appended to the end of your landing page domain to determine the displayed URL.

## Format

Responsive search ads are displayed with three headlines and two descriptions at serve time, plus a customizable URL based on the landing page domain and how you've set up the `path1` and `path2` fields on your ad.

Here's an example of what an ad like this might look like, based on the example shown later in the guide:

![](https://developers.google.com/static/google-ads/api/images/responsive-search-ads.png)

Headlines and descriptions are represented as arrays of a resource called an [`AdTextAsset`](https://developers.google.com/google-ads/api/reference/rpc/v24/AdTextAsset).

Responsive search ads also support the new concept of pinning. If you want finer control than simply allowing the system to mix and match headlines and descriptions, you can pin headlines and descriptions to specific positions. For example, if you want a specific headline to always show first, you can set that `AssetLink` to have a `pinnedField` of `HEADLINE_1`. Then, whenever that ad is served, that specific text will be in the first headline position and the other fields will be drawn from the pool of remaining assets. If more than one asset is pinned to a specific position, then that position will rotate text between all assets that are pinned to that position.

## Additional resources

To learn more about responsive search ads, check out the following Help Center articles.

- [About responsive search ads](https://support.google.com/google-ads/answer/7684791)
- [Create effective Search ads](https://support.google.com/google-ads/answer/6167122)
