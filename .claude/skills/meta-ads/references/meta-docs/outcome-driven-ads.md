# Outcome-Driven Ad Experiences (ODAX)
Fonte: https://developers.facebook.com/blog/post/2021/12/21/simplifying-campaign-objectives-outcome-driven-ad-experiences/
(Nota: a URL original /marketing-api/outcome-driven-ads/ retorna 404; este e o documento oficial de referencia do ODAX. ODAX e obrigatorio desde a v21.0.)
Baixado para Meta Marketing API v25.0

---

# Simplifying campaign objectives with Outcome-Driven Ad Experiences

December 21, 2021 (atualizado)

## What is Outcome-Driven Ad Experiences (ODAX)?

Meta redesigned the objective selection experience for new campaigns. Advertisers select their desired business outcomes (Awareness, Traffic, Engagement, Leads, App Promotion, Sales) and the interface guides them to the most optimal campaign setup. ODAX provides logical choices aligned with marketing concepts, helps discover on-site solutions, and reduces campaign-setup complexity.

## The change: 11 objectives consolidated into 6

1. Awareness
2. Traffic
3. Engagement
4. Leads
5. App Promotion
6. Sales

Note: Store Traffic objective is not initially supported by ODAX but remains as a legacy objective.

## Impacts to the API

### Ad Account

Read field `has_advertiser_opted_in_odax`:
- `true` → ODAX experience (6 objectives)
- `false` → Legacy experience (11 objectives)

Write field `odax_opt_in` (testing only):
- `true` → ODAX experience; `false` → Legacy. Enables an ad account to create ODAX campaigns via the API (does not change the Ads Manager experience).

### Campaign — `objective` field (read & write) new ODAX values

- `OUTCOME_AWARENESS`
- `OUTCOME_ENGAGEMENT`
- `OUTCOME_LEADS`
- `OUTCOME_SALES`
- `OUTCOME_TRAFFIC`
- `OUTCOME_APP_PROMOTION`

### Ad Set — `destination_type` field

Read new ODAX values: `ON_AD`, `ON_POST`, `ON_VIDEO`, `ON_EVENT`, `ON_PAGE`.

Write (with associated outcome):
- `ON_AD` (LEADS)
- `ON_POST` (ENGAGEMENT)
- `ON_VIDEO` (ENGAGEMENT)
- `ON_EVENT` (ENGAGEMENT)
- `ON_PAGE` (ENGAGEMENT)

`destination_type` corresponds to conversion location and engagement type in Ads Manager. New restrictions apply on ODAX campaigns (see Ad Set reference #restrictions).

### Ad

Restrictions that were based on legacy objectives are now decided by destination type, promoted object, and optimization goal. Example: Asset customizations for DCO are compatible with `OUTCOME_ENGAGEMENT` + `on_video` destination type but not with `OUTCOME_ENGAGEMENT` + `on_post`.

## Reference

See the Outcome-Driven Ads Experiences mapping table in the Ad Campaign Group (Campaign) reference for new objectives, destination types, and optimization goals. ODAX became mandatory for new ad sets/ads starting with Marketing API v21.0.
