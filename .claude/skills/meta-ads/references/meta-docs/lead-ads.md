# Lead Ads
Fonte: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/
Baixado para Meta Marketing API v25.0

---

# Lead Ads

Updated: May 21, 2026

Capture leads in Facebook ads — lead ads provide people with a quick and privacy-safe way to sign up to receive information from your business.

## How it works

Lead ads make forms simple for people and more valuable for businesses. Prospective customers sign up for what you're offering and you get accurate contact information to follow up. The form is mobile-friendly and uses information people already shared with Facebook.

## Before you begin

You need:

- **Facebook Page** — all leads generated via a lead ad belong to the Facebook Page.
- **Instagram Account (optional)** — needed to run a lead ad on Instagram; leads still belong to the Facebook Page.
- **Facebook app** — any third-party app (website, mobile app, script) enabling the Marketing API. Has an app ID found in App Dashboard.
- **Test App (optional)** — for development, testing, staging, QA.
- **App Review** — to retrieve lead data, your app must undergo App Review with `leads_retrieval` and `pages_manage_ads` permissions, then complete Business Verification.
- **Access Token** — Use Page access tokens (rate-limited based on active Page users) rather than User access tokens.

## Limitations

You can't retrieve leads if your app is in Development mode (except leads submitted by someone with a role in that same app). Apps in Live mode have access to all leads.

## Create a new lead ad

1. Create a form to use for the lead ad. (/guides/lead-ads/create)
2. Create the ad in Ads Manager or with the Marketing API and associate the form ID. (/guides/lead-ads/create)

## Integrating CRMs

You can set up leads to be instantly updated into your CRM:
- CRM Partners supporting lead ads.
- Custom integration using Webhooks and the Graph API. (/guides/lead-ads/retrieving#webhooks)
- The Graph API as the primary way to retrieve new lead ads in real time.

## Conversions API integration

Share your CRM data about leads back to Meta to unlock quality lead optimization. See Conversion Leads CRM Integration guide. (/conversions-api/conversion-leads-integration)

## Retrieve leads

To read lead data, you need Page Admin access or flexible permissions.

Ways to retrieve leads:
- **Bulk read with the Graph API** — Retrieve leads as JSON objects. Suitable for fetching new leads a few times a day. (/guides/lead-ads/retrieving#bulk-read)
- **Webhooks** — Real-time CRM integration; an update is sent to your endpoint each time a new lead is submitted, then you fetch via the Marketing API. (/guides/lead-ads/quickstart/webhooks-integration)
- **Leads Center** — Manage and download leads in Meta Business Suite.

## Learn more

Graph API Overview, Graph API Rate Limits, Lead Forms for Ads, Retrieving Leads, Retrieving Leads: Webhooks, Testing and Troubleshooting.
