# Object Story Spec (ad-creative-object-story-spec)
Fonte: https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec/
Baixado para Meta Marketing API v25.0

---

# Ad Creative Object Story Spec

## Reading

The specifications of a creative containing the page id and other content to create a new unpublished page post specified using one of `link_data`, `photo_data`, `video_data`, `text_data` or `template_data`.

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `instagram_user_id` numeric string | The Instagram user account that the ad will be posted to |
| `link_data` AdCreativeLinkData | The spec for a link page post or carousel ad |
| `page_id` numeric string | ID of a Facebook page. An unpublished page post will be created on this page. User must have Admin or Editor role for this page. |
| `photo_data` AdCreativePhotoData | The spec for a photo page post. |
| `product_data` list<AdCreativeProductData> | The spec for products to enable catalog related experience. |
| `template_data` AdCreativeLinkData | The spec for a template link page post as used in Dynamic Product Ads. |
| `text_data` AdCreativeTextData | The spec for a text page post. |
| `video_data` AdCreativeVideoData | The spec for a video page post. |

## Creating / Updating / Deleting

You can't perform these operations on this endpoint (read-only spec object).
