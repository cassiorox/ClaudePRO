<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads.md | Scrape: 2026-08-09 | API v26.0 -->

# Video and Carousel Ads



You can create, measure, and optimize video and carousel ads on Facebook through the API. See [Facebook for Business, Carousel Ads](https://www.facebook.com/business/a/online-sales/carousel-link-ads). For supported video formats for ads, see [Advertiser Help Center, Videos](https://www.facebook.com/business/help/1640701476174343).

### Limitations

* The `video_id` must be associated with the ad account.

## Video ads {#video_create}

To create a video ad in a `VIDEO_VIEWS` objective and optimize the bid for reach, follow these steps:

* Step 1: [Provide ad creatives](#create-ad-creative)
* Step 2: [Create ad campaign](#create-ad-campaign)
* Step 3: [Create an ad set](#create-ad-set)
* Step 4: [Create an ad](#create-ad)

### Step 1: Provide [ad creatives](https://developers.facebook.com/docs/reference/ads-api/adcreative) {#create-ad-creative}

Create a video ad using an existing video ID and a video uploaded to Facebook.

You need:

* `pages_read_engagement` and `ads_management` permissions
* [a video uploaded](https://developers.facebook.com/docs/graph-api/video-uploads) to either the `act_{ad-account-id}/advideos` endpoint

```bash
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
  "page_id": "<PAGE_ID>",
  "video_data": {"image_url":"<THUMBNAIL_URL>","video_id":"<VIDEO_ID>"}
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

### Step 2: Create [ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) {#create-ad-campaign}

Set objective to `VIDEO_VIEWS`:

```bash
curl -X POST \
  -F 'name="Video Views campaign"' \
  -F 'objective="OUTCOME_ENGAGEMENT"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```

See [Reference: Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group), [AdObjectives in PHP](https://github.com/facebook/facebook-php-ads-sdk/blob/master/src/FacebookAds/Object/Values/AdObjectives.php) and [AdObjectives in Python](https://github.com/facebook/facebook-python-ads-sdk/blob/199daddec0174ac45d4ee985490b987739cb13af/facebookads/mixins.py#L128).

### Step 3: Create an [ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) {#create-ad-set}

If your goal is lowest cost-per-view possible, pair the video view campaign objective with an ad set's `optimization_goal=THRUPLAY`. You can set `bidding_event` to `IMPRESSIONS` or `THRUPLAY`, to pay per impression or per video view. See [CPV bidding](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/cost-per-action-ads).

```bash
curl \
  -F 'name=A CPV Ad Set' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=500' \
  -F 'start_time=2024-05-06T04:45:29+0000' \
  -F 'end_time=2024-06-06T04:45:29+0000' \
  -F 'billing_event=THRUPLAY' \
  -F 'optimization_goal=THRUPLAY' \
  -F 'bid_amount=100' \
  -F 'targeting={
  "device_platforms": ["mobile"],
  "geo_locations": {"countries":["US"]},
  "publisher_platforms": ["facebook"]
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

Cost-per-view rates are lower for ad sets with `optimization_goal=THRUPLAY` compared to CPVs from Reach and Frequency buying optimized for video views. The end date must be in the future. See [Reference: Ad Set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign).

### Step 4: Create an [ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup) {#create-ad}

Use the existing ad set and ad creative:

```bash
curl -X POST \
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
  "creative_id": "<CREATIVE_ID>"
  }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

When a campaign objective is `VIDEO_VIEWS`, by default the ad gets the right [tracking specs](https://developers.facebook.com/documentation/ads-commerce/marketing-api/tracking-specs) which define actions tracked for an ad. For example, video views:

```
{'action.type':'video_view','post':'POST_ID','post.wall':'PAGE_ID'}
```

See [Ads Manager: My Campaigns](https://www.facebook.com/ads/manager/account/campaigns/) and [Reference: Ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup).

#### Example brand awareness {#example_bao}
To create a video ad for brand awareness, see [brand awareness blog](https://developers.facebook.com/ads/blog/post/2015/12/09/brand-awareness/).

#### Example reach and frequency {#example_rf}

To extend the reach of a video to more people, use the video view campaign objective with [Reach and Frequency](https://developers.facebook.com/docs/reference/ads-api/reachandfrequency). You need to create a prediction, reserve it, and assign it to your ad set.

Follow the [video view creation](#video_create), but apply Reach and Frequency to your ad set. Specify these additional parameters:

```
-F "rf_prediction_id=<RESERVATION_ID>" \
```

## Video for direct response {#dr}

To encourage people to move from awareness to action, see [Video Creative in the Carousel Format](https://developers.facebook.com/ads/blog/post/2015/10/21/video-creative-in-carousel/).

* **Reach people who watched a video**. From awareness to affinity and consideration. See [remarketing](#remarketing).
* **Engage with brand and products**. Add a call-to-action to visit a specific page on your website. See [call to action](#call_to_action).

### Remarketing {#remarketing}

Video ads remarketing provides support for advertisers to target certain custom audiences from organic or paid videos on both Facebook and Instagram. Use this feature to target people who have already viewed a video with additional ads, such as ads that promote related products. See [Research: Creative Combinations that Work](https://www.facebook.com/business/news/creative-ad-sequencing).

You need advertiser permission for the Page containing a video to create an audience for that video.

For the audience, set `subtype=ENGAGEMENT`. Then write rules for the audience you want to create. Each rule has an `object_id`, such as video ID, and `event_name`. The `event_name` is one of:

* `video_watched`: the number of times your video was watched for an aggregate of at least 3 seconds, or for nearly its total length, whichever happened first.
* `video_completed`: the number of times your video was watched at 95% of its length, including watches that skipped to this point.
* `video_view_10s`: the number of times your video was watched for an aggregate of at least 10 seconds, or for nearly its total length, whichever happened first.
* `video_view_15s`: the number of times your video was watched for an aggregate of at least 15 seconds, or for nearly its total length, whichever happened first.
* `video_view_25_percent`: the number of times your video was watched at 25% of its length, including watches that skipped to this point.
* `video_view_50_percent`: the number of times your video was watched at 50% of its length, including watches that skipped to this point.
* `video_view_75_percent`: the number of times your video was watched at 75% of its length, including watches that skipped to this point.

You can combine videos to create an audience based on various videos and actions. For example, an audience could contain 3 second views from video A, and completes from video B and C.

This creates an audience from the past 14 days of 3s+ video viewers of video 1 and completed video viewers of video 2. The audience also autofills for viewers prior to audience creation with `prefill=true`.

```bash
curl \
  -F 'name=Video Ads Engagement Audience' \
  -F 'subtype=ENGAGEMENT' \
  -F 'description=Users who watched my video' \
  -F 'prefill=1' \
  -F 'rule=[
  {"object_id":"%video_id_1","event_name":"video_watched"},
  {"object_id":"%video_id_2","event_name":"video_completed"}
  ]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```

Backfill is supported for video views after October 16, 2015.

### Call to action {#call_to_action}

Video with Call to Action (CTA) prompts people to learn more and visit a specific page on a website. Improve performance when your primary objective is driving video views or brand awareness and your secondary objective is driving offsite clicks. You should use a video link ad for the latter. How CTAs render:

* For Mobile and Desktop, shown as part of the post. When the video is paused, it displays next to the Resume option.
* For Mobile, when someone clicks a video to watch in full screen, a floating CTA appears as a video overlay.
* External video link posts do not display CTAs.

You can use video with CTAs only with the following campaign objectives:

* `PAGE_LIKES`
* [`LEAD_GENERATION`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/create#video)
* [`LOCAL_AWARENESS`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/event-ads)
* `LINK_CLICKS`
* `CONVERSIONS`
* [`APP_INSTALLS`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads#create_video)
* `VIDEO_VIEWS`
* `BRAND_AWARENESS`
* [Mobile app engagement](https://developers.facebook.com/docs/app-ads/formats/ad-for-mobile-app)

See [Video expansion to Additional Objectives](https://developers.facebook.com/ads/blog/post/2015/04/09/expansion-video-objectives/). This creates a video ad with `GET_DIRECTIONS` call to action:

```bash
curl \
  -F 'object_story_spec={
  "page_id": "<PAGE_ID>",
  "video_data": {
  "call_to_action": {
  "type": "GET_DIRECTIONS",
  "value": {
  "link": "fbgeo:\/\/37.48327, -122.15033, \"1601 Willow Rd Menlo Park CA\""
  }
  },
  "image_url": "<THUMBNAIL_URL>",
  "link_description": "Come check out our new store in Menlo Park!",
  "video_id": "<VIDEO_ID>"
  }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
   https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

## Video metrics {#metrics}

### Video post insights, organic {#pageinsights}

Learn more about how your videos perform on Facebook and make more informed decisions about video content. Metrics are available only when someone starts watching videos. This includes video views, unique video views, the average duration of the video view, and audience retention. See where people drop off in your videos and parts people may find most interesting.

### Video ad insights, paid {#adstats}

Use the [Ad Insights API](https://developers.facebook.com/docs/marketing-api/insights-api). The [response](https://developers.facebook.com/docs/marketing-api/reference/ads-insights) contains various video metrics.

### Video type {#type}

Retrieve video ad stats grouped by video type such as auto-play, click-to-play. Include `action_video_type` in `action_breakdowns`. Expected values for `action_video_type` are `total`, `click_to_play`, and `auto_play`.

**The `action_video_type` option is in limited testing.** To identify clients with the breakdown, check `CAN_USE_VIDEO_METRICS_BREAKDOWN` for the [ad account](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account).

```bash
curl -G \
  -d 'action_breakdowns=action_video_type' \
  -d 'date_preset=last_30_days' \
  -d 'fields=actions,video_avg_pct_watched_actions,video_complete_watched_actions' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```

The response includes objects with `action_type` as `video_view` and contain a key `action_video_type`:

```
{
  "data": [
    {
      "actions": [
        ...
        {
          "action_type": "video_play",
          "value": 9898
        },
        {
          "action_type": "video_view",
          "action_video_type": "total",
          "value": 921129
        },
        {
          "action_type": "video_view",
          "action_video_type": "auto_play",
          "value": 915971
        },
        {
          "action_type": "video_view",
          "action_video_type": "click_to_play",
          "value": 5158
        }
      ],
      "video_avg_pct_watched_actions": [
        {
          "action_type": "video_view",
          "action_video_type": "total",
          "value": 60.59
        },
        {
          "action_type": "video_view",
          "action_video_type": "auto_play",
          "value": 60.47
        },
        {
          "action_type": "video_view",
          "action_video_type": "click_to_play",
          "value": 80.63
        }
      ],
      "video_complete_watched_actions": [
        {
          "action_type": "video_view",
          "action_video_type": "total",
          "value": 156372
        },
        {
          "action_type": "video_view",
          "action_video_type": "auto_play",
          "value": 154015
        },
        {
          "action_type": "video_view",
          "action_video_type": "click_to_play",
          "value": 2357
        }
      ],
      "date_start": "2014-12-26",
      "date_stop": "2015-03-25"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MA==",
      "after": "MA=="
    }
  }
}
```

See [Ad Insights API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights).

## Carousel ads {#carousel}
A carousel ad displays multiple creatives in Feed and links to your website or mobile app. Create a carousel ad two ways:

- Create an ad and unpublished page post in one call: [ad creative API](https://developers.facebook.com/docs/reference/ads-api/adcreative).
- Create an [unpublished Page post](https://developers.facebook.com/docs/reference/ads-api/unpublished-page-posts) then create an [ad creative](https://developers.facebook.com/docs/reference/ads-api/adcreative) using the post (not available for video carousel).

**Carousel ads are not supported for Facebook Stories.**

### Create inline {#inline}

Create a carousel ad page post while creating an ad creative. Specify the page post content in `object_story_spec`, which creates an unpublished page post from `adcreatives`. See [ad creatives](https://developers.facebook.com/docs/reference/ads-api/adcreative#object_story_spec). For example:

```bash
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

The response is a creative ID:

```
{"id":"<CREATIVE_ID>"}
```

### Create post, then ad {#pageFirst}

Create an unpublished Page post. `child_attachments` is an [array of link objects](#spec). On each link object, `picture`, `name` and `description` are optional. You can post these as by the Page only with a Page access token.

```bash
curl -X GET \
  -d 'message="Browse our latest products"' \
  -d 'published=0' \
  -d 'child_attachments=[
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 1",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       },
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 2",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       },
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 3",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       },
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 4",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       }
     ]' \
  -d 'caption="WWW.EXAMPLE.COM"' \
  -d 'link="http://www.example.com/products"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PAGE_ID>/posts
```

Then, provide ad creative with the unpublished Page post. Use the `id` for the `object_story_id` in your ad creative.

```bash
curl -X POST \
  -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

### Create Video Carousel Ad {#create_video}

Video carousel ads can have 'caption' in the child attachment to customize the display URL on the end screen:

```
"child_attachments": [
 {
   "link": "https://www.facebookmarketingdevelopers.com/",
   "name": "Facebook Marketing Developers",
   "description": "Facebook Marketing Developers",
   "call_to_action": {
     "type": "APPLY_NOW",
     "value": {
      "link_title": "Facebook Marketing Developers"
     }
   },
   "video_id": "123",
   "caption": "mycustomlinkcaption.com"
  },
]
```

To get child attachments details, use ID and call [Graph API, Video, Reference](https://developers.facebook.com/docs/graph-api/reference/video).

### Create mobile app ad {#create_mobile}

Limitations:

* Carousel mobile app ads support only one app
* Minimum of 3 images compared to 2 on non-app ad carousel ads
* Carousel mobile app ads must have a call to action
* The end card which typically displays the Page's profile photo will not display for carousel mobile app ads.
Note that you should specify the same app store link in each `child_attachment`. You do not have to specify the link again in the `call_to_action:{'value':{'link':... }}}`

For example, to create a carousel ad for mobile app installs:

```bash
curl -X POST \
  -F 'name="Carousel app ad"' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "link_data": {
         "message": "My message",
         "link": "http://www.example.com/appstoreurl",
         "caption": "WWW.ITUNES.COM",
         "name": "The link name",
         "description": "The link description",
         "child_attachments": [
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           },
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           },
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           },
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           }
         ],
         "multi_share_optimized": true
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

You can only publish your post as the Facebook Page associated with the mobile app. And you must use a Page access token.

```bash
curl \
  -F 'message=My description' \
  -F 'link=<APP_STORE_URL>' \
  -F 'caption=WWW.ITUNES.COM' \
  -F 'child_attachments=[
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    },
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    },
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    },
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    }
  ]' \
  -F 'multi_share_optimized=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PAGE_ID>/feed
```

Use the `id` from the response to create the AdCreative:

```bash
curl -X POST \
  -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

## Field specification {#spec}
This is a Carousel Ad on iOS, showing how fields described are used.

| Name | Description |
| --- | --- |
| `child_attachments`<br><br>type: object | A 2-10 element array of link objects required for carousel ads. **You should use at least 3 objects for optimal performance; 2 objects is for enabling lightweight integrations and using 2 objects can result in sub-optimal campaign results.** |
| `child_attachments.link`<br><br>type: string | Link URL or app store URL attached to the post. Required. |
| `child_attachments.picture`<br><br>type: URL | Preview image associated with the link. 1:1 aspect ratio and a minimum of 458 x 458 px for best display. Either `picture` or `image_hash` must be specified. |
| `child_attachments.image_hash`<br><br>type: string | Hash of preview image associated with the link from your [image library](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image); use 1:1 aspect ratio and a minimum of 458 x 458 px for best display. Either `picture` or `image_hash` must be specified. |
| `child_attachments.name`<br><br>type: string | Title of link preview. If not specified, the title of the linked page is used. Typically truncated after 35 characters. You should set a unique `name`, since Facebook **interfaces** show actions reported by `name`. |
| `child_attachments.description`<br><br>type: string | Either a price, discount, or website domain. If not specified, content from the linked page is extracted and used. Typically truncated after 30 characters. |
| `child_attachments.call_to_action`<br><br>type: object | Optional call to action. See [Call To Action](https://developers.facebook.com/docs/marketing-api/unpublished-page-posts#cta-spec). You do not have to specify the link again in `call_to_action:{'value':{'link':... }}}`. |
| `child_attachments.video_id`<br><br>type: string | ID of the [ad video](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/advideos). Can be used in any child element. If specified, must also set `image_hash` or `picture`. |
| `message`<br><br>type: string | Main body of post, also called the status message. |
| `link`<br><br>type: string | URL of a link to "See more". Required. |
| `caption`<br><br>type: string | URL to display in the "See more" link. Not applicable for carousel mobile app ads. |
| `multi_share_optimized`<br><br>type: boolean | If set to `true`, automatically select and order images and links. Otherwise use original order of child elements. Defaults to `true`. |
| `multi_share_end_card`<br><br>type: boolean | If set to `false`, removes the end card which displays the page icon. Default is `true`. |

## Per-product ad statistics {#stats}

Group actions for Carousel ads by each product with `actions_breakdown=['action_carousel_card_id', 'action_carousel_card_name']`.  Each `child_attachment` has a different card ID. `action_carousel_card_id` and `action_carousel_card_name` are only for Carousel ads.

Get the following stats per card:

* `website_ctr`: available when specifying `fields=['website_ctr']`
* `app_install`, `app_use`, `apps.uses`, `credit_spent`,  `mobile_app_install`, `tab_view`, `link_click`, `mobile_app_install`, `app_custom_event.*`, `offsite_conversion.*`: available when specifying `fields=['actions']`. Other actions are not available with a card breakdown.

```bash
curl -G \
  -d 'action_breakdowns=["action_type","action_carousel_card_id"]' \
  -d 'level=ad' \
  -d 'date_preset=last_30_days' \
  -d 'time_increment=all_days' \
  -d 'breakdowns=placement' \
  --data-urlencode 'filtering=[
    {
      "field": "action_type",
      "operator": "IN",
      "value": ["link_click"]
    }
  ]' \
  -d 'fields=impressions,inline_link_clicks,actions,website_ctr' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```

Response:

```
{
...
   "website_ctr": [
      {
         "action_carousel_card_id": "1",
         "action_type": "link_click",
         "value": 51.401869158878
      },
      {
         "action_carousel_card_id": "2",
         "action_type": "link_click",
         "value": 50.980392156863
      }
   ],
   "placement": "mobile_feed",
   "date_start": "2015-05-25",
   "date_stop": "2015-05-28"
}
```

You can also request `cost_per_action_type` for a breakdown of costs by action type:

```bash
curl -G \
  -d 'action_breakdowns=["action_type","action_carousel_card_name"]' \
  -d 'level=ad' \
  -d 'breakdowns=placement' \
  -d 'fields=impressions,campaign_name,cost_per_action_type' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```

Sample response:

```
{
   "data": [
      {
         "impressions": "1862555",
         "campaign_name": "My Campaign",
         "cost_per_action_type": [
            {
               "action_carousel_card_name": "My Carousel Card 1",
               "action_type": "app_custom_event.fb_mobile_activate_app",
               "value": 0.093347346315861
            },
            {
               "action_carousel_card_name": "My Carousel Card 2",
               "action_type": "app_custom_event.fb_mobile_activate_app",
               "value": 0.38324089579301
            },
            ...
         ],
      }
   ]
}
```

**Note:** * Carousel breakdown metrics for `action_report_time=impression` are inaccurate before June 20, 2015.
* Carousel breakdown metrics for `action_report_time=conversion` are inaccurate before July 20, 2015.

## Placements {#place}

If you only select `right_hand_column` as your placement, you can only use a single-video or carousel format in your ad group. The video format is not supported with only a `right_hand_column` placement selected. See [Advanced Targeting and Placement](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting).

For example, create an ad set with `right_hand_column` as your only placement:

```bash
curl \
  -F 'name=RHS only Ad Set' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=500' \
  -F 'start_time=2017-11-21T15:41:36+0000' \
  -F 'end_time=2017-11-28T15:41:36+0000' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'bid_amount=100' \
  -F 'targeting={
    "device_platforms": ["mobile"],
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["facebook"] ,
    "facebook_positions": ["right_hand_column"] ,
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

Provide an ad creative with video:

```bash
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "video_data": {"image_url":"<THUMBNAIL_URL>","video_id":"<VIDEO_ID>"}
  }' \
  -F 'access_token=ACCESS_TOKEN' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

Or provide a canvas ad format for ad creative:

```bash
curl \
  -F 'image_hash=<IMAGE_HASH>' \
  -F 'object_story_spec={
    "link_data": {
      "call_to_action": {"type":"LEARN_MORE"},
      "image_hash": "<IMAGE_HASH>",
      "link": "CANVAS_LINK",
      "name": "Creative message"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

If you try to create an ad with the ad set and ad creative:

```bash
curl \
  -F 'name=My Ad' \
  -F 'adset_id=<AD_SET_ID>' \
  -F 'creative={"creative_id":"<CREATIVE_ID>"}' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

In case you get an error code, you should provide a supported creative or change your targeting.

## See also

- [Upload Videos to Facebook Guide](https://developers.facebook.com/docs/graph-api/video-uploads)
- [Carousel for Mobile App Ads](https://developers.facebook.com/ads/blog/post/2015/05/11/carousel-app-ads)
- [Page Feed Graph API Reference](https://developers.facebook.com/docs/graph-api/reference/page/feed)
- [Unpublished Page Posts](https://developers.facebook.com/docs/reference/ads-api/unpublished-page-posts)
- [Ad Creatives](https://developers.facebook.com/docs/reference/ads-api/adcreative)
- [Instagram Carousel Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads#carousel)
