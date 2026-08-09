<!-- Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/advideos.md | Scrape: 2026-08-09 | API v26.0 -->

# Ad Videos



## Reading

GET GraphAdAccountAdVideosEdge

#### Example

### HTTP
```
GET /v25.0/{ad-account-id}/advideos HTTP/1.1
Host: graph.facebook.com
```

### PHP SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/advideos',
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
    "/{ad-account-id}/advideos",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

### Android SDK
```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{ad-account-id}/advideos",
    null,
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
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{ad-account-id}/advideos"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fadvideos&version=v25.0)

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters

| Parameter | Description |
| --- | --- |
| `max_aspect_ratio`<br><br>*float* | Maximum video aspect ratio to be used in the video aspect ratio filter.<br> |
| `maxheight`<br><br>*int64* | Maximum video height to be used in the video height filter.<br> |
| `maxlength`<br><br>*int64* | Maximum video duration to be used in the video duration filter.<br> |
| `maxwidth`<br><br>*int64* | Maximum video width to be used in the video width filter.<br> |
| `min_aspect_ratio`<br><br>*float* | Minimum video aspect ratio to be used in the video aspect ratio filter.<br> |
| `minheight`<br><br>*int64* | Minimum video height to be used in the video height filter.<br> |
| `minlength`<br><br>*int64* | Minimum video duration to be used in the video duration filter.<br> |
| `minwidth`<br><br>*int64* | Minimum video width to be used in the video width filter.<br> |
| `title`<br><br>*string* | Video name used in the video names filter.<br> |

#### Fields

Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {},
"summary": {}
}
```

##### data

A list of [Video](https://developers.facebook.com/docs/graph-api/reference/video) nodes.

##### paging

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).

##### summary

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like summary=total_count).

| Field | Description |
| --- | --- |
| `total_count`<br><br>*unsigned int32* | Total number of videos returned by the query.<br> |

#### Error Codes

| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |
| 283 | That action requires the extended permission pages_read_engagement and/or pages_read_user_content and/or pages_manage_ads and/or pages_manage_metadata |

## Creating

### /act_{ad_account_id}/advideos
You can make a POST request to *advideos* edge from the following paths:

- [/act_{ad_account_id}/advideos](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/advideos)

When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video) will be created.

#### Parameters

| Parameter | Description |
| --- | --- |
| `audio_story_wave_animation_handle`<br><br>*string* | Everstore handle of wave animation used to burn audio story video<br> |
| `composer_session_id`<br><br>*string* | SELF_EXPLANATORY<br> |
| `description`<br><br>*UTF-8 string* | SELF_EXPLANATORY<br><br>**[supports emoji]**<br> |
| `edit_description_spec`<br><br>*JSON object* | This represents the schema that the client should send to WWW for the edit description spec during video upload.<br><br><br>`screen_readers` *array<JSON object>* |
| `end_offset` This field is only accessible in v2.3 or later.<br><br>*int64* | end_offset<br> |
| `file_size` This field is only accessible in v2.3 or later.<br><br>*int64* | The size of the video file in bytes. Using during<br>[chunked upload](https://developers.facebook.com/docs/marketing-api/advideo#chunked).<br> |
| `file_url`<br><br>*string* | SELF_EXPLANATORY<br> |
| `fisheye_video_cropped`<br><br>*boolean* | Whether the single fisheye video is cropped or not<br> |
| `front_z_rotation`<br><br>*float* | The front z rotation in degrees on the single fisheye video<br> |
| `name`<br><br>*string* | The name of the video in the library.<br> |
| `og_action_type_id`<br><br>*numeric string or integer* | SELF_EXPLANATORY<br> |
| `og_icon_id`<br><br>*numeric string or integer* | SELF_EXPLANATORY<br> |
| `og_object_id`<br><br>*OG object ID or URL string* | SELF_EXPLANATORY<br> |
| `og_phrase`<br><br>*string* | SELF_EXPLANATORY<br> |
| `og_suggestion_mechanism`<br><br>*string* | SELF_EXPLANATORY<br> |
| `original_fov`<br><br>*int64* | Original field of view of the source camera<br> |
| `original_projection_type` This field is only accessible in v2.3 or later.<br><br>*enum {equirectangular, cubemap, half_equirectangular}* | Original Projection type of the video being uploaded<br> |
| `prompt_id` This field is only accessible in v2.3 or later.<br><br>*string* | SELF_EXPLANATORY<br> |
| `prompt_tracking_string` This field is only accessible in v2.3 or later.<br><br>*string* | SELF_EXPLANATORY<br> |
| `referenced_sticker_id`<br><br>*numeric string or integer* | SELF_EXPLANATORY<br> |
| `selected_audio_spec`<br><br>*JSON object* | selected_audio_spec is params for uploading videos with selected audio when performing audio swap<br><br><br>`audio_asset_id` *string* |
| `source`<br><br>*string* | The video, encoded as form data. See the<br>[Video Format](https://developers.facebook.com/docs/graph-api/reference/video-format) doc for more<br>details on video formats.<br> |
| `source_instagram_media_id`<br><br>*numeric string* | The V2 ID of the Instagram video to upload. Cannot be used with `upload_phase`.<br> |
| `start_offset` This field is only accessible in v2.3 or later.<br><br>*int64* | The start position in byte of the chunk that<br>is being sent, inclusive. Used during<br>[chunked upload](https://developers.facebook.com/docs/marketing-api/advideo#chunked).<br> |
| `time_since_original_post`<br><br>*int64* | SELF_EXPLANATORY<br> |
| `title`<br><br>*UTF-8 string* | The name of the video being uploaded. Must be less than 255 characters. Special characters may count as more than 1 character.<br><br>**[supports emoji]**<br> |
| `transcode_setting_properties` This field is only accessible in v2.3 or later.<br><br>*string* | Properties used in computing transcode settings for the video<br> |
| `unpublished_content_type`<br><br>*enum {SCHEDULED, SCHEDULED_RECURRING, DRAFT, PUBLISH_PENDING, ADS_POST, INLINE_CREATED, PUBLISHED, REVIEWABLE_BRANDED_CONTENT}* | SELF_EXPLANATORY<br> |
| `upload_phase` This field is only accessible in v2.3 or later.<br><br>*enum {start, transfer, finish, cancel}* | The phase during chunked upload. Using during<br>[chunked upload](https://developers.facebook.com/docs/marketing-api/advideo#chunked).<br> |
| `upload_session_id` This field is only accessible in v2.3 or later.<br><br>*numeric string or integer* | The session ID of this chunked upload. Using<br>during [chunked upload](https://developers.facebook.com/docs/marketing-api/advideo#chunked).<br> |
| `video_file_chunk` This field is only accessible in v2.3 or later.<br><br>*string* | The chunk of the video, between `start_offset`<br>and `end_offset`. Using during<br>[chunked upload](https://developers.facebook.com/docs/marketing-api/advideo#chunked).<br> |

#### Return Type

```
Struct  {
id: numeric string,
upload_session_id: numeric string,
video_id: numeric string,
start_offset: numeric string,
end_offset: numeric string,
success: bool,
skip_upload: bool,
upload_domain: string,
region_hint: string,
xpv_asset_id: numeric string,
is_xpv_single_prod: bool,
transcode_bit_rate_bps: numeric string,
transcode_dimension: numeric string,
should_expand_to_transcode_dimension: bool,
action_id: string,
gop_size_seconds: numeric string,
target_video_codec: string,
target_hdr: string,
maximum_frame_rate: numeric string,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 222 | Video not visible |
| 389 | Unable to fetch video file from URL. |
| 190 | Invalid OAuth 2.0 Access Token |
| 352 | The video file you selected is in a format that we don't support. |
| 6001 | There was a problem uploading your video. Please try again. |
| 382 | The video file you tried to upload is too small. Please try again with a larger file. |
| 351 | There was a problem with your video file. Please try again with another file, |
| 6000 | There was a problem uploading your video file. Please try again with another file. |

## Updating

You can't perform this operation on this endpoint.

## Deleting

### /act_{ad_account_id}/advideos
You can dissociate a [Video](https://developers.facebook.com/docs/graph-api/reference/video) from an [AdAccount](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account) by making a DELETE request to [/act_{ad_account_id}/advideos](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/advideos).

#### Parameters

| Parameter | Description |
| --- | --- |
| `video_id`<br><br>*video ID* | Ad account library video ID<br><br>**[required]**<br> |

#### Return Type

```
Struct  {
success: bool,
}
```

#### Error Codes

| Error Code | Description |
| --- | --- |
| 613 | Calls to this api have exceeded the rate limit. |
| 100 | Invalid parameter |
