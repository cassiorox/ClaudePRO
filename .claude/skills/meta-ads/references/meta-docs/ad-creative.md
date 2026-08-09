<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative.md | Scrape: 2026-08-09 | API v26.0 -->

# Ad Creative



Format which provides layout and contains content for the ad. To see available ad creatives, visit [Ads Guide](https://www.facebook.com/business/ads-guide). The guide also contains information on size requirements for each ad unit. See also [Facebook for Business](https://www.facebook.com/business/overview) and [Inline page post creation blog post](https://developers.facebook.com/ads/blog/post/2014/08/28/creative-page-post-api).

### Ads About Social Issues, Elections, and Politics

Advertisers running ads about social issues, elections, and politics need to specify [`special_ad_categories`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) while creating an ad campaign. In addition, businesses still have to set `authorization_category` to flag at the ad creative level. [Learn more about the requirements.](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category#issues-elections-politics)

### Examples

For example, get information about an ad creative, such as the ID of the newly created unpublished page post:

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

You can replace `picture` with `image_hash` to specify an image from your ad account's image library. You can also specify image cropping with `image_crops` in `link_data`. See [Image Crop, Reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/image-crops).

To create a political ad creative, use the field `authorization_category` with value `POLITICAL`. For example:

```
curl \
  -F 'authorization_category=POLITICAL' \
  -F 'object_story_spec={
    ...
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Beginning January 9, 2024, to create an issue, electoral, or political ad creative that uses media that is digitally created or altered, use the `authorization_category` field with the `POLITICAL_WITH_DIGITALLY_CREATED_MEDIA` value. For example:

```
curl \
  -F 'authorization_category=POLITICAL_WITH_DIGITALLY_CREATED_MEDIA' \
  -F 'object_story_spec={
    ...
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

For guidelines on Facebook ads see [Ad Guidelines](https://www.facebook.com/ad_guidelines.php).

## Related Resources {#resources}

- [App Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads)

- [Video & Carousel Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads)

- [Advantage+ Catalog Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads)

- [Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads)

- [Ads that Click to WhatsApp](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp)

- [Lead Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads)

## Limits {#limits}

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

- Should be between minimum and maximum title and body lengths.

- Cannot start with punctuation `\ / ! . ? - * ( ) , ; :`

- Cannot have consecutive punctuation except of three full-stops `...`

- Words no longer than 30 characters

- Only three 1-character words allowed

The following characters are not allowed:

- IPA Symbols. Except: ə, ɚ, ɛ, ɜ, ɝ, ɞ, ɟ

- Diacritical Marks. Precomposed version of a character + diacritical mark are allowed. Standalone diacritical marks are not allowed.

- Superscript and subscript characters except ™ and ℠

- These characters `^~_={}[]|<>`

### Exceptions

- **Link Ads** cannot use special characters

- **Page Posts Ads** allow special characters such as `★`

### Placement {#placement}

See [Placement](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative#placements) for restrictions on placement of your ad based on creative.

## Reading

An ad creative object is an instance of a specific creative which is being used to define the `creative` field of one or more [ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup)

### Read Thumbnail {#read_examples}

Request the thumbnail URL and dimensions:

```
curl -G \
  -d 'thumbnail_width=150' \
  -d 'thumbnail_height=120' \
  -d 'fields=thumbnail_url' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>
```

#### Example

### HTTP
```
GET /v25.0/<CREATIVE_ID>/?fields=asset_feed_spec HTTP/1.1
Host: graph.facebook.com
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/<CREATIVE_ID>/?fields=asset_feed_spec',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

### JavaScript SDK
```
/* make the API call */
FB.api(
    "/<CREATIVE_ID>/",
    {
        "fields": "asset_feed_spec"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

### Android SDK
```
Bundle params = new Bundle();
params.putString("fields", "asset_feed_spec");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/<CREATIVE_ID>/",
    params,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

### iOS SDK
```
NSDictionary *params = @{
  @"fields": @"asset_feed_spec",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/<CREATIVE_ID>/"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

### cURL
```
curl -X GET -G \
  -d 'fields="asset_feed_spec"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>/
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%3CCREATIVE_ID%3E%2F%3Ffields%3Dasset_feed_spec&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `thumbnail_height`<br><br>*int64* | **Default value: **`64`<br>Rendered height of thumbnails provided in thumbnail_url, in pixels<br> |
| `thumbnail_width`<br><br>*int64* | **Default value: **`64`<br>Rendered width of thumbnails accessible in thumbnail_url, in pixels<br> |

#### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>*numeric string* | Unique ID for an ad creative, numeric string.<br> |
| `account_id`<br><br>*numeric string* | Ad account ID for the account this ad creative belongs to.<br> |
| `actor_id`<br><br>*numeric string* | The actor ID (Page ID) of this creative<br> |
| `ad_disclaimer_spec`<br><br>*[AdCreativeAdDisclaimer](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-ad-disclaimer)* | Ad disclaimer data on creative for additional information on ads.<br> |
| `adlabels`<br><br>*[list<AdLabel>](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label)* | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this creative. Used to group it with related ad objects.<br> |
| `applink_treatment`<br><br>*enum* | Used for [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management). Specify what action should occur if a person clicks a link in the ad, but the business' app is not installed on their device. For example, open a webpage displaying the product, or open the app in an app store on the person's mobile device.<br> |
| `asset_feed_spec`<br><br>*[AdAssetFeedSpec](https://developers.facebook.com/docs/marketing-api/reference/ad-asset-feed-spec)* | Used for [Dynamic Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec) to automatically experiment and deliver different variations of an ad's creative. Specifies an asset feed with multiple images, text and other assets used to generate variations of an ad. Formatted as a JSON string.<br> |
| `authorization_category`<br><br>*enum* | Specifies whether ad was configured to be labeled as a political ad or not.<br>See [Facebook Advertising Policies](https://www.facebook.com/policies/ads). This field cannot be used for [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ad).<br> |
| `body`<br><br>*string* | The body of the ad. Not supported for video post creatives<br> |
| `branded_content`<br><br>*[AdCreativeBrandedContentAds](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-branded-content-ads)* | branded_content<br> |
| `branded_content_sponsor_page_id`<br><br>*numeric string* | ID for page representing business which runs Branded Content ads. See [Creating Branded Content Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/branded-content).<br> |
| `bundle_folder_id`<br><br>*numeric string* | The [Dynamic Ad's](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads) bundle folder ID<br> |
| `call_to_action`<br><br>*[AdCreativeLinkDataCallToAction](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-call-to-action)* | Call to action for an ad created from existing Instagram post<br> |
| `call_to_action_type`<br><br>*enum {OPEN_LINK, LIKE_PAGE, SHOP_NOW, PLAY_GAME, INSTALL_APP, USE_APP, CALL, CALL_ME, VIDEO_CALL, INSTALL_MOBILE_APP, USE_MOBILE_APP, MOBILE_DOWNLOAD, BOOK_TRAVEL, LISTEN_MUSIC, WATCH_VIDEO, LEARN_MORE, SIGN_UP, DOWNLOAD, WATCH_MORE, NO_BUTTON, VISIT_PAGES_FEED, CALL_NOW, APPLY_NOW, CONTACT, BUY_NOW, GET_OFFER, GET_OFFER_VIEW, BUY_TICKETS, UPDATE_APP, GET_DIRECTIONS, BUY, SEND_UPDATES, MESSAGE_PAGE, DONATE, SUBSCRIBE, SAY_THANKS, SELL_NOW, SHARE, DONATE_NOW, GET_QUOTE, CONTACT_US, ORDER_NOW, START_ORDER, ADD_TO_CART, VIEW_CART, VIEW_IN_CART, VIDEO_ANNOTATION, RECORD_NOW, INQUIRE_NOW, CONFIRM, REFER_FRIENDS, REQUEST_TIME, GET_SHOWTIMES, LISTEN_NOW, TRY_DEMO, WOODHENGE_SUPPORT, SOTTO_SUBSCRIBE, FOLLOW_USER, RAISE_MONEY, SEE_SHOP, GET_DETAILS, FIND_OUT_MORE, VISIT_WEBSITE, BROWSE_SHOP, EVENT_RSVP, WHATSAPP_MESSAGE, FOLLOW_NEWS_STORYLINE, SEE_MORE, BOOK_NOW, FIND_A_GROUP, FIND_YOUR_GROUPS, PAY_TO_ACCESS, PURCHASE_GIFT_CARDS, FOLLOW_PAGE, SEND_A_GIFT, SWIPE_UP_SHOP, SWIPE_UP_PRODUCT, SEND_GIFT_MONEY, PLAY_GAME_ON_FACEBOOK, GET_STARTED, OPEN_INSTANT_APP, AUDIO_CALL, GET_PROMOTIONS, JOIN_CHANNEL, MAKE_AN_APPOINTMENT, ASK_ABOUT_SERVICES, BOOK_A_CONSULTATION, GET_A_QUOTE, BUY_VIA_MESSAGE, ASK_FOR_MORE_INFO, CHAT_WITH_US, VIEW_PRODUCT, VIEW_CHANNEL, GET_IN_TOUCH, ASK_A_QUESTION, START_A_CHAT, CHAT_NOW, ASK_US, WATCH_LIVE_VIDEO, JOIN_LIVE_VIDEO, SHOP_WITH_AI, TRY_ON_WITH_AI}* | Type of call to action button in your ad. This determines the button text and header text for your ad. See [Ads Guide](https://www.facebook.com/business/ads-guide/) for [campaign objectives](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) and permitted call to action types.<br> |
| `categorization_criteria`<br><br>*enum* | The [Dynamic Category Ad's](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads) categorization field, e.g. brand<br> |
| `category_media_source`<br><br>*enum* | The [Dynamic Ad's](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads) rendering mode for category ads<br> |
| `collaborative_ads_lsb_image_bank_id`<br><br>*numeric string* | Used for CPAS local delivery image bank<br> |
| `contextual_multi_ads`<br><br>*AdCreativeContextualMultiAds* | contextual_multi_ads<br> |
| `creative_sourcing_spec`<br><br>*[AdCreativeSourcingSpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-sourcing-spec)* | creative_sourcing_spec<br> |
| `degrees_of_freedom_spec`<br><br>*[AdCreativeDegreesOfFreedomSpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-degrees-of-freedom-spec)* | Specifies the types of transformations that are enabled for the given creative<br> |
| `destination_set_id`<br><br>*numeric string* | The ID of the Product Set for a Destination Catalog that will be used to link with Travel Catalogs<br> |
| `dynamic_ad_voice`<br><br>*string* | Used for [Store Traffic Objective inside Dynamic Ads](https://developers.facebook.com/docs/marketing-api/guides/dynamic-ad/store-visits). Allows you to control the voice of your ad. If set to `DYNAMIC`, page name and profile picture in your ad post come from the nearest page location. If set to `STORY_OWNER`, page name and profile picture in your ad post come from the main page location.<br> |
| `effective_authorization_category`<br><br>*enum* | Specifies whether ad is a political ad or not.<br>See [Facebook Advertising Policies](https://www.facebook.com/policies/ads). This field cannot be used for [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-ad).<br><br><br>This value can be different than the authorization_category value in case our systems have identified the ad as political even though it was not configured to be labeled as such.<br> |
| `effective_instagram_media_id`<br><br>*numeric string* | The ID of an Instagram post to use in an ad<br> |
| `effective_object_story_id`<br><br>*token with structure: Post ID* | The ID of a page post to use in an ad, regardless of whether it's an organic or unpublished page post<br> |
| `enable_direct_install`<br><br>*bool* | Whether Direct Install should be enabled on supported devices<br> |
| `enable_launch_instant_app`<br><br>*bool* | Whether Instant App should be enabled on supported devices<br> |
| `existing_post_title`<br><br>*string* | existing_post_title<br> |
| `facebook_branded_content`<br><br>*AdCreativeFacebookBrandedContent* | Stores fields for Facebook Branded Content<br> |
| `format_transformation_spec`<br><br>*list<AdCreativeFormatTransformationSpec>* | format_transformation_spec<br> |
| `generative_asset_spec`<br><br>*AdCreativeGenerativeAssetSpec* | generative_asset_spec<br> |
| `image_crops`<br><br>*[AdsImageCrops](https://developers.facebook.com/docs/marketing-api/reference/ads-image-crops)* | A JSON object defining crop dimensions for the image specified. See [image crop reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/image-crops) for more details<br> |
| `image_hash`<br><br>*string* | Image hash for ad creative. If provided, do not add `image_url`. See [image library](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image) for more details.<br> |
| `image_url`<br><br>*string* | A URL for the image for this creative. We save the image at this URL to the ad account's image library. If provided, do not include `image_hash`.<br> |
| `instagram_permalink_url`<br><br>*string* | URL for a post on Instagram you want to run as an ad. Also known as Instagram media.<br> |
| `instagram_user_id`<br><br>*numeric string* | Instagram actor ID<br> |
| `interactive_components_spec`<br><br>*[AdCreativeInteractiveComponentsSpec](https://developers.facebook.com/docs/graph-api/reference/ad-creative-interactive-components-spec)* | Specification for all the interactive components that would show up on the ad<br> |
| `link_destination_display_url`<br><br>*string* | Overwrites the display URL for link ads when `object_url` is set to a click tag<br> |
| `link_og_id`<br><br>*numeric string* | The Open Graph (OG) ID for the link in this creative if the landing page has OG tags<br> |
| `link_url`<br><br>*string* | Identify a specific landing tab on your Facebook page by the Page tab's URL. See [connection objects](https://developers.facebook.com/docs/reference/ads-api/connectionobjects) for retrieving Page tab URLs. You can add [app_data](https://developers.facebook.com/documentation/facebook-login/guides/advanced/manual-flow) parameters to the URL to pass data to a Page's tab.<br> |
| `marketing_message_structured_spec`<br><br>*AdCreativeMarketingMessageStructuredSpec* | marketing_message_structured_spec<br> |
| `media_sourcing_spec`<br><br>*[AdCreativeMediaSourcingSpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-media-sourcing-spec)* | media_sourcing_spec<br> |
| `messenger_sponsored_message`<br><br>*string* | Used for Messenger sponsored message. JSON string with message for this ad creative. See [Messenger Platform, Send API Reference](docs/messenger-platform/reference/send-api).<br> |
| `name`<br><br>*string* | Name of this ad creative as seen in the ad account's library. This field has a limit of 100 characters.<br> |
| `object_id`<br><br>*numeric string* | ID for Facebook object being promoted with ads or relevant to the ad or ad type. For example a page ID if you are running ads to generate Page Likes. See [promoted_object](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object).<br> |
| `object_store_url`<br><br>*string* | iTunes or Google Play of the destination of an app ad<br> |
| `object_story_id`<br><br>*token with structure: Post ID* | ID of a Facebook Page post to use in an ad. You can get this ID by [querying the posts of the page](https://developers.facebook.com/docs/graph-api/reference/page/feed). If this post includes an image, it should not exceed 8 MB. Facebook will upload the image from the post to your ad account's [image library](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image). If you create an unpublished page post via `object_story_spec` at the same time as creating the ad, this ID will be null. However, the `effective_object_story_id` will be the ID of the page post regardless of whether it's an organic or unpublished page post.<br> |
| `object_story_spec`<br><br>*[AdCreativeObjectStorySpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec)* | Use if you want to create a new unpublished page post and turn the post into an ad. The Page ID and the content to create a new unpublished page post. Specify `link_data`, `photo_data`, `video_data`, `text_data` or `template_data` with the content.<br> |
| `object_type`<br><br>*enum {APPLICATION, DOMAIN, EVENT, OFFER, PAGE, PHOTO, SHARE, STATUS, STORE_ITEM, VIDEO, INVALID, PRIVACY_CHECK_FAIL, POST_DELETED}* | The type of Facebook object you want to advertise. Allowed values are:<br>`PAGE`<br>`DOMAIN`<br>`EVENT`<br>`STORE_ITEM`: refers to an iTunes or Google Play store destination<br>`SHARE`: from a page<br>`PHOTO`<br>`STATUS`: of a page<br>`VIDEO`<br>`APPLICATION`: app on Facebook<br>`INVALID`: when an invalid object_id was specified such as a deleted object or if you do not have permission to see the object. In very few cases, this field may be empty if Facebook is unable to identify the type of advertised object<br>`PRIVACY_CHECK_FAIL`: you are missing the permission to load this object type<br>`POST_DELETED`: this object_type has been deleted<br> |
| `object_url`<br><br>*string* | URL that opens if someone clicks your link on a link ad. This URL is not connected to a Facebook page.<br> |
| `page_welcome_message`<br><br>*string* | Page welcome message for CTM ads<br> |
| `photo_album_source_object_story_id`<br><br>*string* | photo_album_source_object_story_id<br> |
| `place_page_set_id`<br><br>*numeric string* | The ID of the page set for this creative. See the[Local Awareness guide](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/event-ads)<br> |
| `platform_customizations`<br><br>*[AdCreativePlatformCustomization](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-platform-customization)* | Use this field to specify the exact media to use on different Facebook [placements](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#placement). You can currently use this setting for images and videos. Facebook replaces the media originally defined in ad creative with this media when the ad displays in a specific placements. For example, if you define a media here for `instagram`, Facebook uses that media instead of the media defined in the ad creative when the ad appears on Instagram.<br> |
| `playable_asset_id`<br><br>*numeric string* | The ID of the playable asset in this creative<br> |
| `portrait_customizations`<br><br>*AdCreativePortraitCustomizations* | This field describes the rendering customizations selected for portrait mode ads like IG Stories, FB Stories, IGTV, etc<br> |
| `product_data`<br><br>*list<AdCreativeProductData>* | product_data<br> |
| `product_set_id`<br><br>*numeric string* | Used for [Dynamic Ad](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads). An ID for a product set, which groups related products or other items being advertised.<br> |
| `product_suggestion_settings`<br><br>*AdCreativeProductSuggestionSettings* | product_suggestion_settings<br> |
| `recommender_settings`<br><br>*AdCreativeRecommenderSettings* | Used for [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads). Settings to display Dynamic ads based on product recommendations.<br> |
| `referral_id`<br><br>*numeric string* | The ID of Referral Ad Configuration in this creative<br> |
| `source_facebook_post_id`<br><br>*numeric string* | source_facebook_post_id<br> |
| `source_instagram_media_id`<br><br>*numeric string* | The ID of an Instagram post for creating ads<br> |
| `status`<br><br>*enum {ACTIVE, IN_PROCESS, WITH_ISSUES, DELETED}* | The status of the creative. `WITH_ISSUES` and `IN_PROCESS` are available for 4.0 or higher<br> |
| `template_url`<br><br>*string* | Used for [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads) when you want to use third-party click tracking. See [Dynamic Ads, Click Tracking and Templates](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management#adtemplate).<br> |
| `template_url_spec`<br><br>*[AdCreativeTemplateURLSpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-template-url-spec)* | Used for [Dynamic Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads) when you want to use third-party click tracking. See [Dynamic Ads, Click Tracking and Templates](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management#adtemplate).<br> |
| `threads_media_id`<br><br>*numeric string* | threads_media_id<br> |
| `threads_user_id`<br><br>*numeric string* | threads_user_id<br> |
| `thumbnail_id`<br><br>*numeric string* | thumbnail_id<br> |
| `thumbnail_url`<br><br>*string* | URL for a thumbnail image for this ad creative. You can provide dimensions for this with `thumbnail_width` and `thumbnail_height`. [See example](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative#thumbnail-example).<br> |
| `title`<br><br>*string* | Title for link ad, which does not belong to a page.<br> |
| `url_tags`<br><br>*string* | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only<br> |
| `use_page_actor_override`<br><br>*bool* | Used for [App Ads](https://developers.facebook.com/docs/app-ads). If `true`, we display the Facebook page associated with the app ads.<br> |
| `video_id`<br><br>*numeric string* | Facebook object ID for video in this ad creative.<br> |
| `wamo_whatsapp_identity_spec`<br><br>*AdCreativeWAMOWhatsAppIdentitySpec* | wamo_whatsapp_identity_spec<br> |

#### Edges

| Edge | Description |
| --- | --- |
| [`previews`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative/previews)<br><br>*Edge<AdPreview>* | The HTML Snippets for previewing this creative<br> |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |
| 2500 | Error parsing graph query |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

## Creating

Define creative as part of an ad set or standalone. In either case, we store your ad creative in your ad account's creative library to use in ads. If you try to add an creative that isn't unique, we do not generate it and return the creative ID of the existing ad creative. For example, create a Link Ad with a call to action:

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

You use `link_caption` to pass the call to action object. By doing this, you can customize the call to action caption. To customize the call to action description, pass `link_description` in the call to action object.

Create a [carousel ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads)

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "link_data": {
      "child_attachments": [
        {
          "description": "$8.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https:\/\/www.link.com\/product1",
          "name": "Product 1",
          "video_id": "<VIDEO_ID>"
        },
        {
          "description": "$9.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https:\/\/www.link.com\/product2",
          "name": "Product 2",
          "video_id": "<VIDEO_ID>"
        },
        {
          "description": "$10.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https:\/\/www.link.com\/product3",
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

### Partnership Ads Posts

As a partnership ads sponsor, you can create ads with posts where your brand is tagged. Create a campaign, ad set, as ads as your normally do. The only difference is in the ad creative.

Set the `sponsor_page_id` field for `facebook_branded_content` and/or the `sponsor_id` field for `instagram_branded_content` in the ad creative.  For example:

```
curl \
 -F 'access_token=<TOKEN>' \
 -F 'facebook_branded_content':{'sponsor_page_id=<PAGE_ID>'}\
 // OR
 -F 'instagram_branded_content':{'sponsor_id=<Instagram_user_ID>'}\
 -F 'object_story_id=<OBJECT_STORY_ID>' \
https://graph.facebook.com/<VERSION>/<ACCOUNT_ID>/adcreatives
```

Where `object_story_id` is the post id in the format of: `postOwnerID_postID`.

### Inline Page Post Creation {#inline_post}

Most ad creatives rely on page posts for creative content. While you may create page posts separately then reference them by ID, it is easier to create them in the same call you use to provide ad creative. Specify the page post content with `object_story_spec` which creates an unpublished page post. See [Inline Page Post, Blog](https://developers.facebook.com/ads/blog/post/2014/08/28/creative-page-post-api).

You can get the new ID by retrieving `object_story_id` from the ad creative. To get post ids created with `object_story_spec` through [`/promotable_posts`](https://developers.facebook.com/docs/graph-api/reference/page/feed), pass `include_inline=true` in your `HTTP GET`. If `include_inline` value is `false`, we don't return any ids.

### Get Related Objects {#obtaining_objects}

Many ad creatives require `object_id` for a relevant Facebook object, app ID, or page tab's URL. See [Connection Objects](https://developers.facebook.com/docs/reference/ads-api/connectionobjects) for more information.

### Examples {#create_example}

Create a Video Page Like ad:

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "video_data": {
      "call_to_action": {"type":"LIKE_PAGE","value":{"page":"<PAGE_ID>"}},
      "image_url": "<THUMBNAIL_URL>",
      "video_id": "<VIDEO_ID>"
    }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Create an ad from an existing page post

```
curl \
  -F 'name=Sample Promoted Post' \
  -F 'object_story_id=<POST_ID>' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Create a Photo Ad with [Branded Content](https://www.facebook.com/business/news/branded-content-update) from another page. This is available for photo, video, and link ads.

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "photo_data": {
      "branded_content_sponsor_page_id": "<SPONSOR_PAGE_ID>",
      "image_hash": "<IMAGE_HASH>"
    }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Adding `url_tags` to an ad

```
curl \
  -F 'object_story_id=<POST_ID>' \
  -F 'url_tags=key1=val1&key2=val2' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

You can't perform this operation on this endpoint.

## Updating

### Examples {#update_example}

```
curl \
  -F 'name=New creative name 1517287550' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>
```

### /{ad_creative_id}
You can update an [AdCreative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) by making a POST request to [/{ad_creative_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative).

#### Parameters

| Parameter | Description |
| --- | --- |
| `account_id`<br><br>*numeric string* | Ad account ID for the account this ad creative belongs to.<br> |
| `adlabels`<br><br>*list<Object>* | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this creative. Used to group it with related ad objects.<br> |
| `name`<br><br>*string* | The name of the creative in the creative library. This field takes a string of up to 100 characters.<br> |
| `status`<br><br>*enum {ACTIVE, IN_PROCESS, WITH_ISSUES, DELETED}* | The status of this ad creative. See [Storing and Retrieving Ad Objects](https://developers.facebook.com/documentation/ads-commerce/marketing-api/best-practices/manage-your-ad-object-status).<br> |

#### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node to which you POSTed.

```
Struct  {
success: bool,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

## Deleting

### Examples {#delete_examples}

```
curl -X DELETE \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>/
```

### /{ad_creative_id}
You can delete an [AdCreative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) by making a DELETE request to [/{ad_creative_id}](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative).

#### Parameters

| Parameter | Description |
| --- | --- |
| `account_id`<br><br>*numeric string* | Ad account ID for the account this ad creative belongs to.<br> |
| `adlabels`<br><br>*list<Object>* | [Ad Labels](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-label) associated with this creative. Used to group it with related ad objects.<br> |
| `name`<br><br>*string* | Name of this ad creative as seen in the ad account's library.<br> |
| `status`<br><br>*enum {ACTIVE, IN_PROCESS, WITH_ISSUES, DELETED}* | The status of this ad creative. See [Storing and Retrieving Ad Objects](https://developers.facebook.com/documentation/ads-commerce/marketing-api/best-practices/manage-your-ad-object-status).<br> |

#### Return Type

```
Struct  {
success: bool,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |
