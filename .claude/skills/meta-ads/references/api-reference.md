# Meta Ads ClaudePRO - Referencia de API

Consulte este arquivo quando precisar de detalhes sobre parametros especificos.

## Objetivos de campanha (--objective)

| Valor | Descricao |
|---|---|
| `OUTCOME_LEADS` | Geracao de leads |
| `OUTCOME_TRAFFIC` | Trafego para site |
| `OUTCOME_SALES` | Conversoes/vendas |
| `OUTCOME_AWARENESS` | Reconhecimento de marca |
| `OUTCOME_ENGAGEMENT` | Engajamento |
| `OUTCOME_APP_PROMOTION` | Instalacao de app |

## Metas de otimizacao (--optimization-goal)

| Valor | Uso |
|---|---|
| `LINK_CLICKS` | Cliques no link |
| `LANDING_PAGE_VIEWS` | Visualizacoes da LP |
| `IMPRESSIONS` | Impressoes |
| `REACH` | Alcance |
| `LEAD_GENERATION` | Leads (formulario) |
| `OFFSITE_CONVERSIONS` | Conversoes no site |
| `VALUE` | Valor de conversao |
| `CONVERSATIONS` | Mensagens |

## Estrategias de lance (--bid-strategy)

| Valor | Descricao |
|---|---|
| `LOWEST_COST_WITHOUT_CAP` | Menor custo (sem limite) |
| `LOWEST_COST_WITH_BID_CAP` | Menor custo com teto |
| `COST_CAP` | Custo-alvo |

## Status possiveis (--status)

- `ACTIVE` -- ativo
- `PAUSED` -- pausado
- `DELETED` -- deletado
- `ARCHIVED` -- arquivado

## Tipos de CTA (--call-to-action-type)

LEARN_MORE, SHOP_NOW, SIGN_UP, DOWNLOAD, GET_OFFER, GET_QUOTE, SUBSCRIBE, WATCH_MORE, APPLY_NOW, BOOK_TRAVEL, CONTACT_US

## Estrutura de targeting (--targeting)

```json
{
  "geo_locations": {
    "countries": ["BR"],
    "regions": [{"key": "3847"}],
    "cities": [{"key": "2345678", "radius": 10, "distance_unit": "kilometer"}]
  },
  "age_min": 18,
  "age_max": 65,
  "genders": [0],
  "interests": [
    {"id": "6003139266461", "name": "Design"}
  ],
  "behaviors": [
    {"id": "6015235495172", "name": "Purchase behavior"}
  ],
  "custom_audiences": [
    {"id": "AUDIENCE_ID"}
  ],
  "excluded_custom_audiences": [
    {"id": "AUDIENCE_ID"}
  ],
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed", "story", "reels"],
  "instagram_positions": ["stream", "story", "reels", "explore"],
  "device_platforms": ["mobile", "desktop"]
}
```

Publico aberto (broad targeting): use apenas `geo_locations` + `age_min`/`age_max`, sem interests/behaviors.

## Estrutura de object_story_spec (--object-story-spec)

### Imagem simples
```json
{
  "page_id": "PAGE_ID",
  "instagram_user_id": "IG_USER_ID",
  "link_data": {
    "link": "https://seusite.com?utm_source=facebook",
    "message": "Texto do post",
    "name": "Titulo do link",
    "description": "Descricao",
    "image_hash": "HASH_DA_IMAGEM",
    "call_to_action": {"type": "LEARN_MORE"}
  }
}
```

### Carrossel
```json
{
  "page_id": "PAGE_ID",
  "link_data": {
    "message": "Texto do post",
    "link": "https://seusite.com",
    "child_attachments": [
      {
        "link": "https://seusite.com/produto1",
        "image_hash": "HASH1",
        "name": "Titulo card 1",
        "description": "Desc card 1",
        "call_to_action": {"type": "LEARN_MORE"}
      },
      {
        "link": "https://seusite.com/produto2",
        "image_hash": "HASH2",
        "name": "Titulo card 2"
      }
    ],
    "multi_share_end_card": false
  }
}
```

### Video
```json
{
  "page_id": "PAGE_ID",
  "video_data": {
    "video_id": "VIDEO_ID",
    "message": "Texto do post",
    "title": "Titulo",
    "link_description": "Descricao",
    "call_to_action": {"type": "LEARN_MORE", "value": {"link": "https://seusite.com"}}
  }
}
```

## Date presets para insights (--date-preset)

today, yesterday, this_month, last_month, this_quarter, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, maximum

## Breakdowns para insights (--breakdowns)

age, gender, country, region, publisher_platform, platform_position, device_platform, impression_device, dma, frequency_value, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, place_page_id, product_id

## Time increments para insights (--time-increment)

1 (diario), 7 (semanal), 14 (quinzenal), 28 (mensal), monthly, all_days

## Campos de insights mais usados (--fields)

impressions, clicks, spend, cpc, cpm, ctr, reach, frequency, actions, cost_per_action_type, conversions, cost_per_conversion, purchase_roas, video_avg_time_watched_actions, video_p25_watched_actions, video_p50_watched_actions, video_p75_watched_actions, video_p100_watched_actions, quality_ranking, engagement_rate_ranking, conversion_rate_ranking

## Orcamento: valores em centavos

| Valor real | Valor no parametro |
|---|---|
| R$ 20/dia | `--daily-budget 2000` |
| R$ 50/dia | `--daily-budget 5000` |
| R$ 100/dia | `--daily-budget 10000` |
| US$ 10/dia | `--daily-budget 1000` |

## Lookalike spec (--spec)

```json
{"country": "BR", "ratio": 0.01}
```

- `ratio`: 0.01 = 1% (mais similar), 0.10 = 10% (mais amplo)
- `country`: codigo ISO do pais

## Schemas de audiencia (--schema)

EMAIL, PHONE, FN (first name), LN (last name), MADID (mobile advertiser ID), GEN (gender), DOB (date of birth), CT (city), ST (state), ZIP, COUNTRY

Dados devem ser hasheados em SHA256 antes de enviar (o SDK faz isso automaticamente).
