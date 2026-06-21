# Carousel ads (Video and Carousel Ads)
Fonte: https://developers.facebook.com/docs/marketing-api/guides/videoads/
(Nota: a URL original /creative/carousel-ads/ retorna 404 na v25; este e o doc oficial de carousel ads.)
Baixado para Meta Marketing API v25.0

---

# Video and Carousel Ads

Updated: May 21, 2026

You can create, measure, and optimize video and carousel ads on Facebook through the API. The `video_id` must be associated with the ad account.

## Carousel Ads

Get more creative real-estate in Feed and drive people to your website or mobile app. Create a carousel ad two ways:

1. Create an ad and unpublished page post in one call (ad creative API).
2. Create an unpublished Page post then create an ad creative using the post (not available for video carousel).

Carousel ads are not supported for Facebook Stories.

### Create inline

Specify page post content in `object_story_spec`, which creates an unpublished page post from `adcreatives`:

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "link_data": {
      "child_attachments": [
        {"description":"$8.99","image_hash":"<IMAGE_HASH>","link":"https://www.link.com/product1","name":"Product 1","video_id":"<VIDEO_ID>"},
        {"description":"$9.99","image_hash":"<IMAGE_HASH>","link":"https://www.link.com/product2","name":"Product 2","video_id":"<VIDEO_ID>"},
        {"description":"$10.99","image_hash":"<IMAGE_HASH>","link":"https://www.link.com/product3","name":"Product 3"}
      ],
      "link": "<URL>"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Response: `{"id":"<CREATIVE_ID>"}`

### Create post, then ad

Create an unpublished Page post (use a Page access token), with `child_attachments` as an array of link objects. Then provide an ad creative with `object_story_id` = `<PAGE_ID>_<POST_ID>`.

### Create Video Carousel Ad

Video carousel ads can include `caption` in the child attachment to customize the display URL on the end screen. Each child can have a `call_to_action` and `video_id`.

### Create mobile app ad — limitations

- Carousel mobile app ads support only one app.
- Minimum of 3 images (vs 2 on non-app carousel ads).
- Must have a call to action.
- The end card (page profile photo) won't display.
- Specify the same app store link in each `child_attachment`.

## Field Specification

| Name | Description |
| --- | --- |
| `child_attachments` object | A 2-10 element array of link objects required for carousel ads. Use at least 3 for optimal performance. |
| `child_attachments.link` string | Link URL or app store URL. Required. |
| `child_attachments.picture` URL | Preview image. 1:1 aspect ratio, min 458x458 px. Either `picture` or `image_hash` required. |
| `child_attachments.image_hash` string | Hash of preview image from image library. Either `picture` or `image_hash` required. |
| `child_attachments.name` string | Title of link preview. Truncated ~35 chars. Set a unique name (reported in interfaces). |
| `child_attachments.description` string | Price, discount, or website domain. Truncated ~30 chars. |
| `child_attachments.call_to_action` object | Optional CTA. |
| `child_attachments.video_id` string | ID of the ad video. If specified, must also set `image_hash` or `picture`. |
| `message` string | Main body of post. |
| `link` string | URL of a link to "See more". Required. |
| `caption` string | URL to display in the "See more" link. Not applicable for carousel mobile app ads. |
| `multi_share_optimized` boolean | If true, automatically select and order images and links. Default true. |
| `multi_share_end_card` boolean | If false, removes the end card. Default true. |

## Per-product ad statistics

Group actions for Carousel ads by product with `action_breakdowns=['action_carousel_card_id','action_carousel_card_name']`. Each `child_attachment` has a different card ID. Available per-card: `website_ctr` (with `fields=['website_ctr']`); action types like `link_click`, `mobile_app_install`, `app_custom_event.*`, `offsite_conversion.*` (with `fields=['actions']`). Also supports `cost_per_action_type`.

## Placements

If you select only `right_hand_column`, you can only use single-video or carousel format (plain video format not supported with RHS-only).

## See also

Instagram Carousel Ads, Unpublished Page Posts, Ad Creatives, Upload Videos to Facebook Guide.
