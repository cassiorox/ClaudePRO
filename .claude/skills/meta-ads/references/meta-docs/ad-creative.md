# Ad Creative
Fonte: https://developers.facebook.com/docs/marketing-api/reference/ad-creative/
Baixado para Meta Marketing API v25.0

---

# Ad Creative

Updated: Mar 24, 2026

Format which provides layout and contains content for the ad. The Ads Guide contains information on size requirements for each ad unit.

### Ads About Social Issues, Elections, and Politics

Advertisers running ads about social issues, elections, and politics need to specify `special_ad_categories` while creating an ad campaign. In addition, businesses still have to set `authorization_category` to flag at the ad creative level.

### Examples

Get information about an ad creative:

```
curl -G \
  -d 'fields=name,object_story_id' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>
```

Create a link ad:

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "link_data": {
      "image_hash": "<IMAGE_HASH>",
      "link": "<URL>",
      "message": "try it out"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

You can replace `picture` with `image_hash` to specify an image from your ad account's image library. You can also specify image cropping with `image_crops` in `link_data`.

To create a political ad creative, use `authorization_category` with value `POLITICAL`. To use media that is digitally created or altered for political ads, use `POLITICAL_WITH_DIGITALLY_CREATED_MEDIA`.

## Limits

Only returns 50,000 ad creatives, pagination past this is unavailable.

### Fields-Level Limits

| Limit | Value |
| --- | --- |
| Maximum ad title length | 25 characters, recommended |
| Minimum ad title length | 1 character |
| Maximum ad body length | 90 characters, recommended |
| Minimum ad body length | 1 character |
| Maximum length of a URL | 1000 characters |
| Maximum length of an individual word in title or body | 30 characters, recommended |

### Title and Body Limits

Cannot start with punctuation `\ / ! . ? - * ( ) , ; :`. Cannot have consecutive punctuation except three full-stops `...`. Words no longer than 30 characters. Only three 1-character words allowed. Disallowed: IPA symbols (except ə, ɚ, ɛ, ɜ, ɝ, ɞ, ɟ), standalone diacritical marks, superscript/subscript (except ™ and ℠), and `^~_={}[]|<>`.

### Exceptions

- Link Ads cannot use special characters.
- Page Posts Ads allow special characters such as ★.

## Reading

An ad creative object is an instance of a specific creative being used to define the `creative` field of one or more ads.

### Read Thumbnail

```
curl -G \
  -d 'thumbnail_width=150' \
  -d 'thumbnail_height=120' \
  -d 'fields=thumbnail_url' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>
```

#### Parameters

| Parameter | Description |
| --- | --- |
| `thumbnail_height` _int64_ | Default value: `64`. Rendered height of thumbnails in pixels |
| `thumbnail_width` _int64_ | Default value: `64`. Rendered width of thumbnails in pixels |

#### Fields

| Field | Description |
| --- | --- |
| `id` _numeric string_ | Unique ID for an ad creative. |
| `account_id` _numeric string_ | Ad account ID this ad creative belongs to. |
| `actor_id` _numeric string_ | The actor ID (Page ID) of this creative |
| `ad_disclaimer_spec` _AdCreativeAdDisclaimer_ | Ad disclaimer data on creative. |
| `adlabels` _list<AdLabel>_ | Ad Labels associated with this creative. |
| `applink_treatment` _enum_ | Used for Dynamic Ads. Action if a person clicks a link but the app is not installed. |
| `asset_feed_spec` _AdAssetFeedSpec_ | Used for Dynamic Creative to deliver different variations. Formatted as a JSON string. |
| `authorization_category` _enum_ | Whether ad was configured to be labeled as a political ad. Cannot be used for Dynamic Ads. |
| `body` _string_ | The body of the ad. Not supported for video post creatives |
| `branded_content` _AdCreativeBrandedContentAds_ | branded_content |
| `branded_content_sponsor_page_id` _numeric string_ | ID for page representing business which runs Branded Content ads. |
| `bundle_folder_id` _numeric string_ | The Dynamic Ad's bundle folder ID |
| `call_to_action` _AdCreativeLinkDataCallToAction_ | Call to action for an ad created from existing Instagram post |
| `call_to_action_type` _enum_ | Type of CTA button. Values include: OPEN_LINK, LIKE_PAGE, SHOP_NOW, PLAY_GAME, INSTALL_APP, USE_APP, CALL, CALL_ME, VIDEO_CALL, INSTALL_MOBILE_APP, USE_MOBILE_APP, MOBILE_DOWNLOAD, BOOK_TRAVEL, LISTEN_MUSIC, WATCH_VIDEO, LEARN_MORE, SIGN_UP, DOWNLOAD, WATCH_MORE, NO_BUTTON, VISIT_PAGES_FEED, CALL_NOW, APPLY_NOW, CONTACT, BUY_NOW, GET_OFFER, GET_OFFER_VIEW, BUY_TICKETS, UPDATE_APP, GET_DIRECTIONS, BUY, SEND_UPDATES, MESSAGE_PAGE, DONATE, SUBSCRIBE, SAY_THANKS, SELL_NOW, SHARE, DONATE_NOW, GET_QUOTE, CONTACT_US, ORDER_NOW, START_ORDER, ADD_TO_CART, VIEW_CART, VIEW_IN_CART, VIDEO_ANNOTATION, RECORD_NOW, INQUIRE_NOW, CONFIRM, REFER_FRIENDS, REQUEST_TIME, GET_SHOWTIMES, LISTEN_NOW, TRY_DEMO, FOLLOW_USER, RAISE_MONEY, SEE_SHOP, GET_DETAILS, FIND_OUT_MORE, VISIT_WEBSITE, BROWSE_SHOP, EVENT_RSVP, WHATSAPP_MESSAGE, FOLLOW_NEWS_STORYLINE, SEE_MORE, BOOK_NOW, FIND_A_GROUP, FIND_YOUR_GROUPS, PAY_TO_ACCESS, PURCHASE_GIFT_CARDS, FOLLOW_PAGE, SEND_A_GIFT, SWIPE_UP_SHOP, SWIPE_UP_PRODUCT, SEND_GIFT_MONEY, PLAY_GAME_ON_FACEBOOK, GET_STARTED, OPEN_INSTANT_APP, AUDIO_CALL, GET_PROMOTIONS, JOIN_CHANNEL, MAKE_AN_APPOINTMENT, ASK_ABOUT_SERVICES, BOOK_A_CONSULTATION, GET_A_QUOTE, BUY_VIA_MESSAGE, ASK_FOR_MORE_INFO, CHAT_WITH_US, VIEW_PRODUCT, VIEW_CHANNEL, GET_IN_TOUCH, ASK_A_QUESTION, START_A_CHAT, CHAT_NOW, ASK_US, WATCH_LIVE_VIDEO, JOIN_LIVE_VIDEO, SHOP_WITH_AI, TRY_ON_WITH_AI. |
| `categorization_criteria` _enum_ | The Dynamic Category Ad's categorization field, e.g. brand |
| `category_media_source` _enum_ | The Dynamic Ad's rendering mode for category ads |
| `degrees_of_freedom_spec` _AdCreativeDegreesOfFreedomSpec_ | Types of transformations enabled for the given creative |
| `destination_set_id` _numeric string_ | ID of the Product Set for a Destination Catalog |
| `dynamic_ad_voice` _string_ | Used for Store Traffic Objective inside Dynamic Ads. DYNAMIC or STORY_OWNER. |
| `effective_authorization_category` _enum_ | Whether ad is a political ad. May differ from authorization_category if systems identified it as political. |
| `effective_instagram_media_id` _numeric string_ | The ID of an Instagram post to use in an ad |
| `effective_object_story_id` _Post ID_ | ID of a page post to use in an ad, organic or unpublished |
| `enable_direct_install` _bool_ | Whether Direct Install should be enabled on supported devices |
| `enable_launch_instant_app` _bool_ | Whether Instant App should be enabled on supported devices |
| `image_crops` _AdsImageCrops_ | JSON object defining crop dimensions for the image. |
| `image_hash` _string_ | Image hash for ad creative. If provided, do not add image_url. |
| `image_url` _string_ | URL for the image for this creative. If provided, do not include image_hash. |
| `instagram_permalink_url` _string_ | URL for a post on Instagram you want to run as an ad. |
| `instagram_user_id` _numeric string_ | Instagram actor ID |
| `interactive_components_spec` _AdCreativeInteractiveComponentsSpec_ | Spec for interactive components on the ad |
| `link_destination_display_url` _string_ | Overwrites the display URL for link ads when object_url is a click tag |
| `link_og_id` _numeric string_ | The Open Graph ID for the link in this creative |
| `link_url` _string_ | Identify a specific landing tab on your Facebook page by the Page tab's URL. |
| `media_sourcing_spec` _AdCreativeMediaSourcingSpec_ | media_sourcing_spec |
| `name` _string_ | Name of this ad creative. Limit of 100 characters. |
| `object_id` _numeric string_ | ID for Facebook object being promoted. |
| `object_store_url` _string_ | iTunes or Google Play of the destination of an app ad |
| `object_story_id` _Post ID_ | ID of a Facebook Page post to use in an ad. Null if created via object_story_spec; use effective_object_story_id instead. |
| `object_story_spec` _AdCreativeObjectStorySpec_ | Create a new unpublished page post and turn it into an ad. Specify link_data, photo_data, video_data, text_data or template_data. |
| `object_type` _enum {APPLICATION, DOMAIN, EVENT, OFFER, PAGE, PHOTO, SHARE, STATUS, STORE_ITEM, VIDEO, INVALID, PRIVACY_CHECK_FAIL, POST_DELETED}_ | The type of Facebook object you want to advertise. |
| `object_url` _string_ | URL that opens if someone clicks your link on a link ad. Not connected to a Facebook page. |
| `page_welcome_message` _string_ | Page welcome message for CTM ads |
| `place_page_set_id` _numeric string_ | ID of the page set for this creative (Local Awareness). |
| `platform_customizations` _AdCreativePlatformCustomization_ | Specify exact media to use on different placements. |
| `playable_asset_id` _numeric string_ | The ID of the playable asset in this creative |
| `portrait_customizations` _AdCreativePortraitCustomizations_ | Rendering customizations for portrait mode ads (IG Stories, FB Stories, IGTV). |
| `product_set_id` _numeric string_ | Used for Dynamic Ad. ID for a product set. |
| `recommender_settings` _AdCreativeRecommenderSettings_ | Settings to display Dynamic ads based on product recommendations. |
| `source_instagram_media_id` _numeric string_ | The ID of an Instagram post for creating ads |
| `status` _enum {ACTIVE, IN_PROCESS, WITH_ISSUES, DELETED}_ | The status of the creative. |
| `template_url` _string_ | Used for Dynamic Ads with third-party click tracking. |
| `template_url_spec` _AdCreativeTemplateURLSpec_ | Used for Dynamic Ads with third-party click tracking. |
| `thumbnail_id` _numeric string_ | thumbnail_id |
| `thumbnail_url` _string_ | URL for a thumbnail image for this ad creative. |
| `title` _string_ | Title for link ad, which does not belong to a page. |
| `url_tags` _string_ | Query string parameters which replace or append to urls clicked from page post ads. |
| `use_page_actor_override` _bool_ | Used for App Ads. If true, display the Facebook page associated with the app ads. |
| `video_id` _numeric string_ | Facebook object ID for video in this ad creative. |

#### Edges

| Edge | Description |
| --- | --- |
| `previews` _Edge<AdPreview>_ | The HTML Snippets for previewing this creative |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 2635 | You are calling a deprecated version of the Ads API. |
| 80004 | Too many calls to this ad-account. |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |
| 2500 | Error parsing graph query |
| 270 | Not allowed for apps with development access level. |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

## Creating

Define creative as part of an ad set or standalone. We store ad creative in your ad account's creative library. If you try to add a creative that isn't unique, we return the existing creative ID.

Create a Link Ad with a call to action:

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "link_data": {
      "call_to_action": {"type":"SIGN_UP","value":{"link":"<URL>"}},
      "link": "<URL>",
      "message": "try it out"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Create a carousel ad:

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "link_data": {
      "child_attachments": [
        {
          "description": "$8.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https://www.link.com/product1",
          "name": "Product 1",
          "video_id": "<VIDEO_ID>"
        },
        {
          "description": "$9.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https://www.link.com/product2",
          "name": "Product 2",
          "video_id": "<VIDEO_ID>"
        },
        {
          "description": "$10.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https://www.link.com/product3",
          "name": "Product 3"
        }
      ],
      "link": "<URL>"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

### Inline Page Post Creation

Specify page post content with `object_story_spec` which creates an unpublished page post. Get the new ID by retrieving `object_story_id` from the ad creative.

### Create an ad from an existing page post

```
curl \
  -F 'name=Sample Promoted Post' \
  -F 'object_story_id=<POST_ID>' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

### Adding url_tags to an ad

```
curl \
  -F 'object_story_id=<POST_ID>' \
  -F 'url_tags=key1=val1&key2=val2' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

## Updating

```
curl \
  -F 'name=New creative name' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>
```

POST Parameters: `account_id`, `adlabels`, `name` (up to 100 chars), `status` enum {ACTIVE, IN_PROCESS, WITH_ISSUES, DELETED}. Return: `{ success: bool }`.

## Deleting

```
curl -X DELETE \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>/
```

Return: `{ success: bool }`.
