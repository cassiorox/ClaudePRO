<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads.md | Scrape: 2026-08-09 | API v26.0 -->

# Lead Ads



Capture leads in Facebook ads — lead ads provide people with a quick and privacy-safe way to sign up to receive information from your business.

## How it works
Lead ads make forms simple for people and more valuable for businesses. Set up a lead ad where prospective customers can sign up for what you're offering and you'll get accurate contact information to follow up.

The form is mobile-friendly and uses information people already shared with Facebook. It's easier and faster for people to reach businesses — and advertisers get accurate, actionable information. Learn more about [Lead Ads](https://www.facebook.com/business/ads/lead-ads).

## Before you begin

To get started with lead ads, you need the following:

* Facebook Page  
Gives your business a presence on Facebook and helps you connect with customers. See [Facebook for Business](https://www.facebook.com/business/products/pages) or [Create a new Page](https://developers.facebook.com/docs/pages/getting-started). All leads generated via a lead ad belong to the Facebook Page.

* Instagram Account (*optional*)  
You need an Instagram Account if you want to run a lead ad on Instagram. The leads generated via the ad still belong to the Facebook Page.

* Facebook app  
Can be any third-party app, such as a website, mobile app, or script. The app enables the [Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api) to integrate with Facebook. Each app has an app ID you use whenever you use one of our [SDKs](https://developers.facebook.com/docs#apis-and-sdks) or [Open Graph tags for sharing](https://developers.facebook.com/docs/sharing/webmasters). Find your app ID in your [App Dashboard](https://developers.facebook.com/apps). Learn more about [how to create an app and app ID](https://developers.facebook.com/docs/development/create-an-app).

* Test App (*optional*)  
Quickly create Facebook app IDs for use during development, testing, staging, or QA phases. Test apps have their own app ID and independent settings and are helpful in pre-production. See [Test Apps](https://developers.facebook.com/docs/development/build-and-test/test-apps).

* App Review  
To retrieve lead data, your app must undergo [App Review](https://developers.facebook.com/docs/apps/review). You must include the `leads_retrieval` and `pages_manage_ads` permissions in your submission. Check our [Submitting for Review guide](https://developers.facebook.com/docs/app-review/submission-guide) for details. After approval, you will be asked to complete [Business Verification](https://developers.facebook.com/docs/development/release/business-verification).

* Access Token  
All apps that access Facebook need an access token, or you can get a token when you create your new app. You can obtain access tokens via a number of methods. See the [access tokens documentation](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens) for more information on the different types and how to get them.  
Access tokens can be [short or long-lived](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens#termtokens). You should not depend on these lifetimes remaining the same as they may change without warning or expire early.
**Warning:** User access tokens are rate-limited based on active users on the app, which is usually **one** for lead ad integrations. Use Page access tokens. They're rate-limited based on active users on the Page.

## Limitations {#limitations}

You can't retrieve leads if your app is in [Development mode](https://developers.facebook.com/docs/development/build-and-test/app-modes#development-mode). For testing purposes, Development mode app users can access leads submitted by someone with a role in that same app. See [App Roles](https://developers.facebook.com/docs/development/build-and-test/app-roles) for more information.

**Note:** Apps in [Live mode](https://developers.facebook.com/docs/development/build-and-test/app-modes#live-mode) continue to have access to all leads.

## Create a new lead ad

1. [Create a form](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/create) to use for the lead ad.
2. Create the ad in the [Ads Manager](https://www.facebook.com/ads/manage/powereditor/) or with the Marketing API and associate the form ID. See [Lead Ads, Creating](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/create).

## Integrating CRMs

With Facebook lead ads, you can set up the leads you receive from Facebook to be instantly updated into your CRM system. Your options include:

* [CRM Partners](https://www.facebook.com/business/help/908902042493104) supporting lead ads.
* Custom integration using [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks) and the [Graph API](https://developers.facebook.com/docs/graph-api). See the [Lead Ads Webhooks documentation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/retrieving#webhooks) for more information.
* The [Graph API](https://developers.facebook.com/docs/graph-api) is the primary way to get data in and out of Facebook and is a low-level HTTP-based API that you can use to retrieve new lead ads in real time.

## Conversions API integration

To see a better performance in your lead ads, you can choose to share your CRM data about your leads back to Meta to unlock quality lead optimization. This allows Meta to better optimize for quality leads by using data on which generated leads turned out to be quality leads from your CRM directly.

See more information about connecting your CRM to the Conversions API in the [Conversion Leads CRM Integration guide](https://developers.facebook.com/documentation/ads-commerce/conversions-api/conversion-leads-integration).

## Retrieve leads

**Warning:** To read lead data, you need Page Admin access or flexible permissions. With the latter option, you can retrieve leads without Page Admin access.

### Ways to retrieve leads

* Bulk read with the Graph API — Retrieve the leads as JSON objects, making it easy to integrate and map data. This is suitable if you want to fetch new leads a few times a day. For more frequent updates, use Webhooks. See [Retrieving Leads: Bulk Reading](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/retrieving#bulk-read) for more information.
* Webhooks — Good for CRM integration with Facebook to receive leads in real time. Retrieve every new lead in real time. Every time a new lead is submitted, an update is sent to your endpoint to notify you that a new lead is available. You can then fetch the information of the lead by accessing the Marketing API. See [How to use our Webhooks](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/quickstart/webhooks-integration) for more information.
* Leads Center — See [Manage and download your leads in Meta Business Suite](https://www.facebook.com/business/help/929596264178167) for more information.

## Learn more

* [Graph API Overview](https://developers.facebook.com/docs/graph-api/overview)
* [Graph API Rate Limits](https://developers.facebook.com/docs/graph-api/advanced/rate-limiting)
* [Lead Forms for Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/create)
* [Retrieving Leads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/retrieving)
* [Retrieving Leads: Webhooks](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/retrieving#webhooks)
* [Testing and Troubleshooting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/testing-troubleshooting)
* Business Help Center: [About lead ads](https://www.facebook.com/business/help/1481110642181372?id=735435806665862)
* Business Help Center: [Verify your business](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
