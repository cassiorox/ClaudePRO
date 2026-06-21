# Changelog v25.0
Fonte: https://developers.facebook.com/docs/graph-api/changelog/version25.0
Baixado para Meta Marketing API v25.0

---

# Version 25.0

## Graph API

Released February 18, 2026 | Available until TBD.

### Insights (deprecations coming with v26.0)

When v26.0 is released, several page reach, page post reach, video impressions, and story impressions metrics will be deprecated and will return an error if requested in any API version.

#### Page Insights API — removing:
`page_impressions_unique` (use `page_total_media_view_unique` + `page_media_view`), `page_impressions_paid_unique`, `page_impressions_viral_unique`, `page_impressions_nonviral_unique`, `page_posts_impressions`, `page_posts_impressions_unique`, `page_posts_impressions_paid`, `page_posts_impressions_paid_unique`, `page_posts_impressions_organic_unique`, `page_posts_served_impressions_organic_unique`, `page_posts_impressions_viral`, `page_posts_impressions_viral_unique`, `page_posts_impressions_nonviral`, `page_posts_impressions_nonviral_unique`, `page_video_views_unique`.

#### Post Insights API — removing:
`post_impressions_unique` (use `post_total_media_view_unique` + `post_media_view`), `post_impressions_paid_unique`, `post_impressions_fan_unique`, `post_impressions_organic_unique`, `post_impressions_viral_unique`, `post_impressions_nonviral_unique`, `post_video_views_organic_unique`, `post_video_views_paid_unique`, `post_video_views_unique`.

#### Video Insights API — removing:
`post_impressions_unique`, `total_video_impressions`, `total_video_impressions_unique`, `total_video_impressions_paid_unique`, `total_video_impressions_paid`, `total_video_impressions_organic_unique`, `total_video_impressions_organic`, `total_video_impressions_viral_unique`, `total_video_impressions_viral`, `total_video_impressions_fan_unique`, `total_video_impressions_fan`, `total_video_impressions_fan_paid_unique`, `total_video_impressions_fan_paid`, `total_video_views_organic_unique`, `total_video_views_paid_unique`, `total_video_views_unique`.

#### Stories Insights API — removing:
`PAGE_STORY_IMPRESSIONS_BY_STORY_ID` (use `STORY_MEDIA_VIEW`), `PAGE_STORY_IMPRESSIONS_BY_STORY_ID_UNIQUE` (use `STORY_TOTAL_MEDIA_VIEW_UNIQUE`).

### Node metadata
Applies to v25.0+ (all versions May 19, 2026). The `metadata=1` query parameter is deprecated and will no longer return field metadata. Use the Graph API Explorer or API references instead.

### Webhooks mTLS
Starting March 31, 2026, Meta will sign a new Webhooks mTLS certificate using a Meta-owned CA (same common name `client.webhooks.fbclientcerts.com`). If your servers verify the certificate, you must trust the new Meta CA (download `meta-outbound-api-ca-2025-12.pem`) before the deadline to avoid TLS handshake failures.

## Marketing API

February 18, 2026 | Available until TBD.

### Advantage+ Campaigns

#### Advantage+ Shopping Campaigns and Advantage+ App Campaigns deprecation
Applies to v25.0+ (all versions May 19, 2026). Creation, duplication, and updates to Advantage+ shopping campaigns and Advantage+ app campaigns is no longer allowed. Migrate to Advantage+ campaigns.

Affected endpoints:
- `POST /{ad-account-id}/campaigns`
- `POST /{campaign-id}/copies`

### Insights

#### Asynchronous Jobs
Applies to v25.0+. New default fields returned when an asynchronous ad report fails: `error_code`, `error_message`, `error_subcode`, `error_user_title`, `error_user_msg`. The `error_code` field type changes from `uint` to `int`.

Affected endpoints:
- `GET /{ad-report-run-id}`
