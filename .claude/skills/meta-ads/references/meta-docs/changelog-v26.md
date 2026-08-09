<!-- Fonte: https://developers.facebook.com/docs/graph-api/changelog/version26.0 | Scrape: 2026-08-09 -->

# Changelog v26.0 — Graph API e Marketing API

**Lancamento:** 29 de julho de 2026 | **Disponivel ate:** TBD (~2 anos)

## Marketing API

### Delivery Estimate — campos removidos
_Aplica a v26.0+. Aplica a TODAS as versoes em 27/10/2026._

Os campos `daily_outcomes_curve`, `budget_guardrail` e `estimate_dau` foram removidos das respostas de Delivery Estimate. Sem substituto.

Endpoints afetados:
- `GET /{ad-account-id}/delivery_estimate`
- `GET /{adset-id}/delivery_estimate`

### Ads in WhatsApp Status — suporte expandido
_Aplica a v26.0+._

- Criativos podem incluir `wamo_whatsapp_identity_spec` para entregar em WhatsApp Status.
- `user_age_unknown` default `true` quando WhatsApp Status esta selecionado.
- Otimizacao offsite-conversion suportada para Sales, Leads e Engagement. Landing Page Views tambem.
- Carrossel suporta ate 10 cards.

### Advantage+ Audience — flag explicito obrigatorio (HEC-F)
_Aplica a v26.0+ no lancamento. Vira obrigatorio pra todas as versoes quando a v25.0 for descontinuada (data TBD)._

Ao criar conjunto de anuncios de **Habitacao, Emprego ou Credito/Financeiro (HEC-F)** com targeting relaxavel em setup nao-broad, e obrigatorio setar explicitamente `targeting_automation.advantage_audience` como `1` ou `0`. Omitir retorna erro `ADS_TARGETING__REQUIRE_EXPLICIT_ADVANTAGE_AUDIENCE_FLAG`. Setups broad/default nao sao afetados.

**Atencao nesta skill:** os scripts em `scripts/` **nao** passam `targeting_automation` por conta propria. Ao criar conjunto de nicho HEC-F (habitacao, emprego, credito/financeiro) com targeting restrito, incluir o flag manualmente no `--targeting`:

```json
{"geo_locations": {"countries": ["BR"]}, "targeting_automation": {"advantage_audience": 0}}
```

Use `0` para travar o targeting no que foi definido, ou `1` para deixar a Meta expandir o publico.

Endpoint afetado: `POST /{ad-account-id}/adsets`

### Instagram Explore Feed — placement removido
_Aplica a v26.0+._

O placement Instagram Explore Feed **nao existe mais**. A entrega migra pros outros placements elegiveis; requisicoes que especificam Explore explicitamente **retornam erro**. Remover `explore` (e `explore_home`) de `instagram_positions` nas configuracoes manuais de placement.

Endpoints afetados:
- `POST /act_{ad-account-id}/adsets`
- `POST /{ad-set-id}`

### Web+App campaign — destino web_only depreciado
_Aplica a v26.0+. Todas as versoes em 27/10/2026._

Criativo com `applink_treatment=web_only` nao pode mais ser anexado a ad de campanha com conversion location Website and App.

### Messenger Stories — placement depreciado
_Aplica a v26.0+. Todas as versoes (inclusive chamadas sem versao) em 27/10/2026._

O valor `story` em `messenger_positions` e removido silenciosamente em chamadas v26.0+. Quem usa placement manual deve remover `story`; Advantage+ Placements nao precisa de acao.

### Poll ads — criacao depreciada
_Aplica a v26.0+. Todas as versoes em 27/10/2026._

Componentes de enquete nao sao mais suportados na criacao/edicao de ads e criativos. `poll_spec` e o tipo `poll` em `interactive_components_spec` ficam indisponiveis.

### Shop Ads — default WEBSITE_AND_SHOP
_A partir da v26.0._

Criativos elegiveis defaultam automaticamente para `destination_spec.destination_type = WEBSITE_AND_SHOP` quando o anunciante tem shop. Opt-out: setar explicitamente `destination_type = WEBSITE_AND_SHOP_OPT_OUT`.

Endpoints afetados:
- `POST /{ad-account-id}/adcreatives`
- `POST /{ad-account-id}/ads`

## Graph API (fora do Marketing)

### Commerce Order Management API — depreciada por completo
_v26.0+: bloqueada desde 29/07/2026. Todas as versoes em 27/10/2026._

Checkout dentro do Facebook/Instagram (Shops) foi encerrado; os 47 endpoints de commerce orders foram depreciados sem substituto.

### Protocolo legado
_v26.0+ desde 29/07/2026. Todas as versoes em 27/10/2026._

- `pretty` ignorado (JSON compacto sempre)
- `debug` ignorado
- `date_format` retorna erro
- `GET /?ids=...` na raiz retorna erro (usar requests por objeto ou batch)
- `If-None-Match`/ETag/304 removidos

### Page (New Pages Experience)
Campos `current_location`, `genre`, `network`, `parking`, `start_info` depreciados; `auto_publish_page_info_updates` removido de settings.

### Rights Manager
Campos de owner migrados pro tipo `RightsHolderOwner` (`reference_owner` → `reference_owner_rh_owner`, etc.).

## Business SDK v26

- `facebook-business` 26.0.0 publicado no PyPI (pinado na API v26.0).
- Integracao com o Conversions API Parameter Builder (open source) — auto-gera/melhora `fbc`, `fbp`, `event_source_url`, `referrer_url`, `client_ip_address` e normaliza/hasheia PII.

## Descontinuacao de versoes

- **09/06/2026:** Marketing API v23.0 encerrada (v24.0 e a mais antiga suportada).
- **06/10/2026:** Marketing API v24.0 encerra.
- **24/09/2026:** Graph API v20.0 removida.
- **21/01/2027:** Graph API v21.0 removida.
- **27/10/2026:** a maioria das remocoes da v26.0 se estende a todas as versoes restantes, inclusive chamadas sem versao.
