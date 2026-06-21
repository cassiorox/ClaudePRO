# Ad Creative Link Data
Fonte: https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data/
Baixado para Meta Marketing API v25.0

---

# Ad Creative Link Data

## Reading

The specification for a link ad or carousel ad.

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `ad_context` string | String that represents the ad context provided by advertiser |
| `additional_image_index` int32 | The index (zero based) of the image from the additional images array to use as the ad image for a dynamic product ad |
| `app_link_spec` AdCreativeLinkDataAppLinkSpec | Native deeplinks attached to the post |
| `attachment_style` enum | The style of the attachment |
| `boosted_product_set_id` numeric string | Combined with product_set_id to promote a specific Product Set while including other products. Use the All Products Product Set ID in product_set_id and the specific Product Set ID here. |
| `branded_content_sponsor_page_id` numeric string | The branded content sponsor page id |
| `call_to_action` AdCreativeLinkDataCallToAction | Optional CTA button. If not specified, on Instagram a default CTA is used: `{"type":"LEARN_MORE","value":{"link":<LINK VALUE OF LINK_DATA>}}`. LIKE_PAGE is not supported. |
| `caption` string | Link caption. Overwrites the caption under the title. Must be an actual URL. Not used in Instagram ads. |
| `child_attachments` list<AdCreativeLinkDataChildAttachment> | A 2-5 element array of link objects required for carousel ads. If `multi_share_optimized` is true, up to 10 objects; Facebook optimizes order and shows top 5. Recommend at least 3 attachments. For Instagram Carousel: at least 3 for MOBILE_APP_INSTALLS, 2 for others. |
| `collection_thumbnails` list<AdCreativeCollectionThumbnailInfo> | List of Canvas media component IDs and square cropping info for Collection style feed rendering |
| `customization_rules_spec` list<AdCustomizationRuleSpec> | Customization rules for a dynamic ad |
| `description` string | Link description. Overwrites the description in the link. Not used for Instagram ads. |
| `event_id` numeric string | The id of a Facebook event. Used only for Website Clicks campaign with Buy Tickets CTA and link pointing to event ticketing website. |
| `force_single_link` bool | Whether to force the post to render in a single link format |
| `format_option` enum {carousel_ar_effects, carousel_images_multi_items, carousel_images_single_item, carousel_slideshows, collection_video, single_image} | How to render your ad. Default is carousel_images_multi_items. |
| `image_crops` AdsImageCrops | How the image should be cropped. Use crop spec with 100x100 key for Facebook Feed and Instagram. |
| `image_hash` string | Hash of an image in your ad account's image library. Provide this or `picture` but not both. |
| `image_layer_specs` list<AdCreativeLinkDataImageLayerSpec> | How to render image overlays on a dynamic item in Dynamic Ads |
| `image_overlay_spec` AdCreativeLinkDataImageOverlaySpec | How to render image overlays on a dynamic item in Dynamic Ads |
| `link` string | Link url. Required to be the same as the CTA link url. Required for a carousel ad. |
| `message` string | The main body of the post. Required for a carousel ad. |
| `multi_share_end_card` bool | If false, removes the end card displaying the page icon. Default true. Used by carousel ads. |
| `multi_share_optimized` bool | If true, automatically select and order images and links. Default true. Used by carousel ads. |
| `name` string | Name of the link. Overwrites the title of the link when previewing the ad. Ignored when CTA type is LIKE_PAGE. |
| `offer_id` numeric string | The id of a Facebook native offer |
| `page_welcome_message` string | Customized greeting presented when the user is redirected from a click-to-Messenger or click-to-WhatsApp ad. For click-to-WhatsApp, a JSON object passed as a string. |
| `picture` string | URL of a picture to use in the post. Specify this or `image_hash` but not both. Saved into the ad account image library. |
| `post_click_configuration` AdCreativePostClickConfiguration | Customized contents for the ad post-click experience |
| `preferred_image_tags` list<string> | Select which image to display by its tag, in order of priority |
| `preferred_video_tags` list<string> | Selects which video to use by tag. Only applied if opted into Dynamic Media. |
| `retailer_item_ids` list<string> | List of product IDs provided by the advertiser for Collections |
| `show_multiple_images` bool | Use with force_single_link=true to show a single dynamic item in carousel format using multiple images from the catalog. |
| `sponsorship_info` AdCreativeLinkDataSponsorshipInfoSpec | Details of the sponsor for the event ad |
| `static_fallback_spec` AdCreativeStaticFallbackSpec | Give a fallback creative for dynamic ads |
| `use_flexible_image_aspect_ratio` bool | Default true. Only applies if you do not provide a cropping spec. If true, renders the entire image when aspect ratio is between 1.91:1 and 1:1, otherwise auto-crops. Use only for single image ads, not carousel ads. Not supported for Donation, Offer, Dynamic Ads, ads with image overlays, or ads using stock images. |

## Creating / Updating / Deleting

You can't perform these operations on this endpoint (read-only spec object).
