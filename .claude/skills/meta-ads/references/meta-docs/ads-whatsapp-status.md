<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/ads-in-whatsapp-status.md | Scrape: 2026-08-09 | API v26.0 -->

# Ads in WhatsApp Status



Businesses use WhatsApp Status to engage with their audiences through photos, videos, and text. Ads in WhatsApp Status help your business get discovered by new customers and make it easy for them to connect with you about your products or services.

## Where ads in WhatsApp Status will appear

These ads only appear in WhatsApp Statuses, which are separate from chats and calls. Statuses in WhatsApp are single vertical images or videos up to 60 minutes with a 9:16 aspect ratio that disappear after 24 hours.

The personal messaging experience on WhatsApp is not changing. WhatsApp collects very limited information from people and personal messages. Calls and statuses remain end-to-end encrypted and are not used to determine what ad WhatsApp users may see.

### Limitations

- WhatsApp Status is available when Instagram Stories is also selected (`instagram_positions: ["story"]`). Standalone Status campaigns are not supported at this time.
- Only single image and single video formats are supported. Carousel, collection, and flexible format ads are not supported.
- Special ad categories (Finance, Employment, Housing, and Social Issues/Elections/Politics) are not eligible for WhatsApp Status.
- Sensitive verticals (Pharma, Healthcare, and GSI) are excluded from WhatsApp Status delivery.
- A/B testing, Dynamic Creative Optimization (DCO), and Reach and Frequency buying are not compatible with WhatsApp Status.
- Advantage+ Creative tools are not available for the WhatsApp Status placement.
- Updating `wamo_whatsapp_identity_spec` on an existing creative is not supported. To change the identity, create a new creative.
- At this time, ads in Status are available globally, except in the EU, UK, Iran, Cuba, Syria, Russia, and North Korea.

## Supported objectives and optimization goals

Ads in WhatsApp Status support the following campaign objectives and their corresponding optimization goals:

| Objective | Optimization goals |
| --- | --- |
| `OUTCOME_AWARENESS` | `REACH`, `IMPRESSIONS`, `THRUPLAY` |
| `OUTCOME_TRAFFIC` | `LINK_CLICKS`, `REACH`, `IMPRESSIONS`, `CONVERSATIONS`, `LANDING_PAGE_VIEWS` |
| `OUTCOME_ENGAGEMENT` | `LINK_CLICKS`, `REACH`, `IMPRESSIONS`, `CONVERSATIONS`, `THRUPLAY`, `LANDING_PAGE_VIEWS` |
| `OUTCOME_LEADS` | `LINK_CLICKS`, `REACH`, `IMPRESSIONS`, `CONVERSATIONS`, `LANDING_PAGE_VIEWS` |
| `OUTCOME_SALES` | `LINK_CLICKS`, `REACH`, `IMPRESSIONS`, `CONVERSATIONS`, `LANDING_PAGE_VIEWS` |

Supported destinations are WhatsApp chat and website. A WhatsApp Business Account (WABA) is not required for the website destination.

## Placement setup

### Permissions

All endpoints require one of the following permissions on your access token:

- `ads_management`
- `business_management` (if access is granted through Business Manager)

### Targeting configuration

To deliver ads on WhatsApp Status, your ad set targeting must include both the `whatsapp` publisher platform with the `status` position and the `instagram` publisher platform with the `story` position:

```json
{
  "targeting": {
    "publisher_platforms": ["instagram", "whatsapp"],
    "instagram_positions": ["story"],
    "whatsapp_positions": ["status"]
  }
}
```

## Reaching people on WhatsApp whose age is unknown

Using this feature is optional and only applies to people using WhatsApp. You can opt out at any time by setting `user_age_unknown: false` in your ad set targeting spec. Excluding people on WhatsApp whose age is unknown may substantially reduce delivery to people on WhatsApp, some of whom you may want to reach.

WhatsApp's [Terms of Service](https://www.whatsapp.com/legal/terms-of-service) require people to be at least 13 years old to register for and use WhatsApp (or older in some countries or territories), but it does not have age information for all people. The `user_age_unknown` targeting field controls whether these people are included in your ad set's audience. If you include people on WhatsApp whose age is unknown, we may not have age information for all of the people who may see your ads. Ads delivered to people on WhatsApp whose age is unknown must be suitable for people of all ages. As always, you are required to follow our [Advertising Standards](https://transparency.meta.com/policies/ad-standards).

If the WhatsApp Status placement is included and this field is not set, it defaults to `true`, meaning people on WhatsApp whose age is unknown **are included** in your audience.

| Value | Behavior |
| --- | --- |
| `true` (or omitted) | People on WhatsApp whose age is unknown **are included** in the ad set audience. This is the default. |
| `false` | People on WhatsApp whose age is unknown **are excluded** from the ad set audience. |

See [People on WhatsApp whose age is unknown](https://www.facebook.com/business/help/717368264947302?id=176276233019487) for more information.

#### Example: include people on WhatsApp whose age is unknown

```json
{
  "targeting": {
    "geo_locations": {"countries": ["US"]},
    "publisher_platforms": ["instagram", "whatsapp"],
    "instagram_positions": ["story"],
    "whatsapp_positions": ["status"],
    "user_age_unknown": true
  }
}
```

## WhatsApp identity

Ad creatives for WhatsApp Status use the `wamo_whatsapp_identity_spec` field to associate a WhatsApp business profile with the ad. This identity controls the profile name and image that appear on the Status ad.

### Identity types

The `wamo_whatsapp_identity_id` field accepts an ID from one of three entity types:

| Identity type | Description |
| --- | --- |
| Page ID | Facebook Page identity (`PAGE_BACKED`). |
| Page WhatsApp Number ID | A Phone Link or Business Link identity. |
| WhatsApp Business Account to Number ID | A Business Connected identity. |

When you create a creative for a campaign with the WhatsApp Status placement, you should provide a `wamo_whatsapp_identity_spec`. If an identity is not specified, the Facebook Page identity is shown by default.

## Create an ad creative for WhatsApp Status

Use the `POST /act_<AD_ACCOUNT_ID>/adcreatives` endpoint to create an ad creative. WhatsApp Status creatives support single image and single video formats with `link_data` in the `object_story_spec`.

### Parameters

| Name | Description | Example |
| --- | --- | --- |
| `wamo_whatsapp_identity_spec` | Optional. Contains `wamo_whatsapp_identity_id` to associate a WhatsApp identity with the ad, and `whatsapp_phone_number` to specify the WhatsApp phone number. If not provided, some ads may not deliver to WhatsApp Status. | `{"wamo_whatsapp_identity_id": "987654321098765", "whatsapp_phone_number": "+1234567890"}` |

### Examples

#### Create an ad creative with identity

```bash
curl 'https://graph.facebook.com/v25.0/act_123456789/adcreatives' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer EAAJB...' \
-d '{
  "object_story_spec": {
    "page_id": "109876543210",
    "link_data": {
      "link": "https://www.example.com/summer-sale",
      "call_to_action": {
        "type": "WHATSAPP_MESSAGE",
        "value": {
          "app_destination": "whatsapp"
        }
      }
    }
  },
  "wamo_whatsapp_identity_spec": {
    "wamo_whatsapp_identity_id": "987654321098765",
    "whatsapp_phone_number": "+1234567890"
  }
}'
```

## Read ad creatives with WhatsApp identity

To retrieve the `wamo_whatsapp_identity_spec` field from existing ad creatives, include it in the `fields` parameter of any GET creative endpoint:

```bash
curl 'https://graph.facebook.com/v25.0/<AD_CREATIVE_ID>?fields=wamo_whatsapp_identity_spec{wamo_whatsapp_identity_id,whatsapp_phone_number}' \
-H 'Authorization: Bearer EAAJB...'
```

The following GET endpoints support the `wamo_whatsapp_identity_spec` field:

| Endpoint | Description |
| --- | --- |
| `GET /<AD_CREATIVE_ID>` | Read a single ad creative. |
| `GET /<AD_ACCOUNT_ID>/adcreatives` | List all ad creatives for an ad account. |
| `GET /<CAMPAIGN_ID>/adcreatives` | List ad creatives for a campaign. |
| `GET /<AD_ID>/adcreatives` | List ad creatives for an ad. |

## Preview ads on WhatsApp Status

To generate a preview of an ad rendered on WhatsApp Status, use `ad_format=WHATSAPP_STATUS_MEDIA` with any preview endpoint. Previews render with the correct WhatsApp identity.

| Endpoint | Description |
| --- | --- |
| `GET /<AD_CREATIVE_ID>/previews` | Preview an ad creative. |
| `GET /<AD_ID>/previews` | Preview an ad. |
| `GET /<AD_ACCOUNT_ID>/generatepreviews` | Generate a preview from a creative spec. |

#### Example request

```bash
curl 'https://graph.facebook.com/v25.0/120210123456780123/previews?ad_format=WHATSAPP_STATUS_MEDIA' \
-H 'Authorization: Bearer EAAJB...'
```

## Next steps

- [Placement targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting)
- [People on WhatsApp whose age is unknown](https://www.facebook.com/business/help/717368264947302?id=176276233019487)
- [Ads that Click to WhatsApp](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp)
