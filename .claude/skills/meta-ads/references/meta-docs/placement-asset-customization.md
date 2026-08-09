<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization.md | Scrape: 2026-08-09 | API v26.0 -->

# Placement Asset Customization



Use Placement Asset Customization to customize the creative assets displayed in different ad [placements](https://developers.facebook.com/docs/marketing-api/buying-api/ad-units#placements). Maintain control over each creative asset, while using several different placements.

Placement Asset Customization is one of three APIs that use asset customization rules. Learn more about [Asset Customization Rules](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/asset-customization-rules).

## Get started

- Step 1: [Create an ad campaign and ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/asset-customization-rules#campaign)
- Step 2: [Provide creative and customize assets](#asset-feed)
- Step 3: [Create your ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/asset-customization-rules#ad)
- Optional Step 4: Get [insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/insights) and analyze results
- Optional Step 5: [Read Ad Creative](#read-ad-creative)

**Warning:** Placement Asset Customization with existing posts is no longer supported via the API. You can only use this option in Ads Manager.

## Step 2: Provide creative {#asset-feed}

Use `asset_feed_spec` to provide your creative. You can specify multiple creative assets for each asset type, including images, videos, carousels, headlines, and body text. Only provide one link description, since the link description cannot be customized per placement.

To apply customization:

1. Set [`asset_customization_rules`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/asset-customization-rules) inside your `asset_feed_spec`.
2. For each rule, add `customization_spec` and asset labels.

**Note:** For Placement Asset Customization, every `asset_feed_spec` needs to have more than one customization rule attached to it.

See [Asset Customization Rules](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/asset-customization-rules).
### Supported properties

| Property name | Description |
| --- | --- |
| `customization_spec`<br><br>type: [Supported Fields](#supported-fields) | **Required.**<br><br>Placements where you want to display the assets. |
| `image_label`<br><br>format: `{"name": "{LABEL_NAME}"}` | **Required for `SINGLE_IMAGE` format.**<br><br>Label of the image you want to display. This label attaches to the image assets in `asset_feed_spec`. |
| `video_label`<br><br>format: `{"name": "{LABEL_NAME}"}` | **Required for `SINGLE_VIDEO` format.**<br><br>Label of the video you want to display. This label attaches to the video assets in `asset_feed_spec`. |
| `carousel_label`<br><br>format: `{"name": "{LABEL_NAME}"}` | **Required for `CAROUSELS` format.**<br><br>Label of the carousel you want to display. This label attaches to the carousel assets in `asset_feed_spec`.<br><br>**Note:** if providing carousels via Placement Asset Customization, all child attachments must be defined within the Asset Feed Spec and referenced via `adlabels` (ad labels). Child attachments may not be defined inline. See [Asset Feed Spec Options](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/options) for more details on the `carousels` format. |

### Supported fields in `customization_spec` {#supported-fields}

| Property name | Description |
| --- | --- |
| `publisher_platforms` | **Required**.<br><br>Possible placements for your ad. Options are: `facebook`, `instagram`, `messenger`, `audience_network`, and `threads`. |
| `facebook_positions` | **Optional, but required if Facebook is selected in `publisher_platforms`.**<br><br>Facebook specific placement. Options are: `feed`, `right_hand_column`, `marketplace`, `video_feeds`, `search`, `story`, and `notification`. |
| `instagram_positions` | **Optional, but required if Instagram is selected in `publisher_platforms`.**<br><br>Instagram specific placements. Options are: `stream`, `story`, `explore`, `explore_home`, `profile_feed` and `ig_search`.<br><br>**Note:** The `explore_home` placement only supports the `SINGLE_IMAGE` format. |
| `messenger_positions` | **Optional, but required if Messenger is selected in `publisher_platforms`.**<br><br>Messenger specific placements. Options are: `sponsored_messages` and `story`. |
| `audience_network_positions` | **Optional, but required if Audience Networks is selected in `publisher_platforms`.**<br><br>Audience Network specific placement. Options are: `classic`, `instream_video`, and `rewarded_video`. |
| `threads_positions` | **Optional, but required if Threads is selected in `publisher_platforms`.**<br><br>Threads specific placement: `threads_stream`<br><br>**Note:** `publisher_platform: instagram` and `instagram_positions: stream` are required to select `threads_positions: threads_stream`. |

Learn more about our [available placement options](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting).

**Example** — Feed Setup

```curl
curl -X POST \
  -F 'object_story_spec={
      "page_id": "<PAGE_ID>",
      "instagram_user_id": "<IG_USER_ID>",
    }' \
  -F 'asset_feed_spec={
      "videos": [{
        "adlabels": [{"name": "labelfb"}],
        "video_id": "<VIDEO_ID>"
      },
      {
        "adlabels": [{"name": "labelig"}],
        "video_id": "<VIDEO_ID>"
      }],
      "bodies": [{"text": "Begin Your Adventure"}],
      "link_urls": [{
        "website_url": "<WEBSITE_URL>",
        "display_url": "<DISPLAY_URL>"
      }],
      "titles": [{"text": "Level Up"}],
      "ad_formats": ["SINGLE_VIDEO"],
      "call_to_action_types": ["WATCH_MORE"],
      "descriptions": [{"text": "Description"}],
      "asset_customization_rules": [{
        "customization_spec": {
          "publisher_platforms": ["facebook"],
          "facebook_positions": ["feed","instream_video"]
        },
        "video_label": {
          "name": "labelfb"
        }
      },
      {
        "customization_spec": {
          "publisher_platforms": ["instagram"],
          "instagram_positions": ["stream"]
        },
        "video_label": {
          "name": "labelig"
        }
      }]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

**Example** — Instagram Explore home asset customization

```curl
curl -X POST \
  -F 'object_story_spec={
      "page_id": "<PAGE_ID>",
      "instagram_user_id": "<INSTAGRAM_ID>",
    }' \
  -F 'asset_feed_spec={
    "ad_formats": ["SINGLE_IMAGE"],
    "asset_customization_rules": [{
      "image_label": {
        "name": "<IMAGE_LABEL>"
      },
      "customization_spec": {
        "publisher_platforms": ["instagram"],
        "instagram_positions": ["explore_home"]
      }
    }],
    "bodies": [{
      "text": "",
      "adlabels": [{
        "name": "adlabel1"
      },
      {
        "name": "adlabel2"
      }]
    }],
    "call_to_action_types": ["LEARN_MORE"],
    "images": [{
      "hash": "<IMAGE_HASH>",
      "adlabels": [{"name": "adlabel1"}]
    },
    {
      "hash": "<IMAGE_HASH>",
      "image_crops": {
        "100x100": [
          [
            604,
            0
          ],
          [
            1659,
            1055
          ]
        ]
      },
      "adlabels": [{"name": "adlabel2"}]
    }],
    "link_urls": [{
      "website_url": "<WEBSITE_URL>",
      "display_url": "<DISPLAY_URL>",
      "deeplink_url": "<DEEPLINK_URL>",
      "adlabels": [
        {
          "name": "adlabel1"
        },
        {
          "name": "adlabel2"
        }
      ]
    }],
    "optimization_type": "PLACEMENT",
    "titles": [{
      "text": "<TEXT>",
      "adlabels": [
        {
          "name": "adlabel1"
        },
        {
          "name": "adlabel2"
        }
      ]
      }]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

**Example** - Instagram search results Asset Customization

```curl
curl -X POST \
  -F 'object_story_spec={
      "page_id": "<PAGE_ID>",
      "instagram_user_id": "<INSTAGRAM_ID>",
    }' \
  -F 'asset_feed_spec={
    "ad_formats": ["SINGLE_IMAGE"],
    "asset_customization_rules": [{
      "image_label": {
        "name": "placement_asset_f1048d832ecd558_1661539731099"
      },
      "customization_spec": {
        "publisher_platforms": ["instagram"],
        "instagram_positions": ["ig_search"]
      }
    }],
    "bodies": [{
      "text": "<TEXT>",
      "adlabels": [
        {
          "name": "adlabel1"
        },
        {
          "name": "adlabel2"
        }
      ]
    }],
    "call_to_action_types": ["LEARN_MORE"],
    "images": [{
      "hash": "9ffd7307eae1f9c6e5250fc8760d285f",
      "adlabels": [{"name": "adlabel1"}]
    },
    {
      "hash": "9ffd7307eae1f9c6e5250fc8760d285f",
      "image_crops": {
        "100x100": [
          [
            604,
            0
          ],
          [
            1659,
            1055
          ]
        ]
      },
      "adlabels": [{"name": "adlabel2"}]
    }],
    "link_urls": [{
      "website_url": "<WEBSITE_URL>",
      "display_url": "<DISPLAY_URL>",
      "deeplink_url": "<DEEPLINK_URL>",
      "adlabels": [
        {
          "name": "adlabel1"
        },
        {
          "name": "adlabel2"
        }
      ]
    }],
    "optimization_type": "PLACEMENT",
    "titles": [{
      "text": "",
      "adlabels": [
        {
          "name": "adlabel1"
        },
        {
          "name": "adlabel2"
        }
      ]
    }]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```

**Example** — Threads Feed Setup

```curl
curl -X POST \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "instagram_user_id": "<IG_USER_ID>",
    "threads_user_id" : "<THREADS_USER_ID>",
  }' \
  -F 'asset_feed_spec={
    "videos": [{
      "adlabels": [{"name": "labelfb"}],
      "video_id": "<VIDEO_ID>"
    },
    {
      "adlabels": [{"name": "labelig"}],
      "video_id": "<VIDEO_ID>"
    },
    {
      "adlabels": [{"name": "labelthreads"}],
      "video_id": "<VIDEO_ID>"
    }],
    "bodies": [{"text": "Begin Your Adventure"}],
    "link_urls": [{
      "website_url": "<WEBSITE_URL>",
      "display_url": "<DISPLAY_URL>"
    }],
    "titles": [{"text": "Level Up"}],
    "ad_formats": ["SINGLE_VIDEO"],
    "call_to_action_types": ["WATCH_MORE"],
    "descriptions": [{"text": "Description"}],
    "asset_customization_rules": [{
      "customization_spec": {
        "publisher_platforms": ["instagram"],
        "instagram_positions": ["stream"]
      },
      "video_label": {
        "name": "labelig"
      }
    },
    {
      "customization_spec": {
        "publisher_platforms": ["threads"],
        "threads_positions": ["threads_stream"]
      },
      "video_label": {
        "name": "labelthreads"
      }
    },
    {
      "customization_spec": {},
      "video_label": {
        "name": "labelfb"
      }
    }],
    "optimization_type": "PLACEMENT"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v23.0/act_<AD_ACCOUNT_ID>/adcreatives
```

See [all available options for Asset Feed Spec](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec/options).

## Optional step 5: Read ad creative {#read-ad-creative}

For Placement Asset Customization ads, retrieve Instagram-related creative fields via `act_<AD_ACCOUNT_ID>/ads`. For example:

```text
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads?fields=creative{effective_instagram_media_id,instagram_permalink_url}
```
