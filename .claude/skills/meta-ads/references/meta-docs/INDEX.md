# Documentacao oficial Meta Marketing API — v26.0

Copia offline da documentacao oficial (developers.facebook.com) referente a **API v26.0**, lancada em 29/07/2026. Consultar antes de subir ou editar campanhas quando precisar confirmar parametros, campos, edges ou comportamento da API.

Cada arquivo traz a URL de origem e a data do scrape na primeira linha.

**Como atualizar:** as paginas oficiais servem markdown puro em
`https://developers.facebook.com/documentation/ads-commerce/<path>.md`.
Baixar com `curl -sL` e sobrescrever — com User-Agent de browser a Meta devolve HTML em vez de markdown, entao nao trocar o UA.

## Referencia de objetos

| Arquivo | Conteudo |
|---|---|
| [changelog-v26.md](changelog-v26.md) | Changelog completo da v26.0 (breaking changes, deprecacoes, datas) — **ler antes de qualquer migracao** |
| [campaign.md](campaign.md) | Campaign (`/act_X/campaigns`) — objetivos, special_ad_categories, CBO |
| [adset.md](adset.md) | Ad Set (`/act_X/adsets`) — orcamento, otimizacao, targeting, promoted_object |
| [ad.md](ad.md) | Ad (`/act_X/ads`) — criacao, copies, limites |
| [ad-creative.md](ad-creative.md) | Ad Creative — object_story_spec, asset_feed_spec, contextual_multi_ads |
| [ad-image.md](ad-image.md) | Upload de imagens (`/act_X/adimages`) — hashes |
| [ad-videos.md](ad-videos.md) | Upload de videos (`/act_X/advideos`) |
| [campaign-structure.md](campaign-structure.md) | Visao geral da Marketing API e hierarquia Campaign > Ad Set > Ad |

## Publicos e targeting

| Arquivo | Conteudo |
|---|---|
| [targeting-basico.md](targeting-basico.md) | Targeting basico — geo, idade, genero |
| [targeting-avancado.md](targeting-avancado.md) | Targeting avancado — interesses, comportamentos, flexible_spec |
| [targeting-search.md](targeting-search.md) | Busca de interesses/comportamentos/geo (`/search`) |
| [custom-audience.md](custom-audience.md) | Publicos personalizados — engajamento, site, lista |
| [lookalike-audiences.md](lookalike-audiences.md) | Publicos semelhantes — ratio, country, lookalike_spec |
| [placement-asset-customization.md](placement-asset-customization.md) | asset_customization_rules (feed vs story por midia) |

## Insights

| Arquivo | Conteudo |
|---|---|
| [insights-api.md](insights-api.md) | Guia introdutorio de Insights |
| [insights-reference.md](insights-reference.md) | Referencia completa — parametros, fields, action types |
| [insights-breakdowns.md](insights-breakdowns.md) | Breakdowns disponiveis |

## Guias e formatos

| Arquivo | Conteudo |
|---|---|
| [get-started.md](get-started.md) | Primeiros passos com a Marketing API |
| [bidding.md](bidding.md) | Estrategias de lance e como/quando usar teto/custo-alvo |
| [advantage-plus-sales.md](advantage-plus-sales.md) | Advantage+ Sales/App/Leads (substituto do ASC, descontinuado na v25) |
| [carousel-ads.md](carousel-ads.md) | Anuncios em carrossel e video |
| [lead-ads.md](lead-ads.md) | Lead Ads / formularios de geracao de leads |
| [conversions-api.md](conversions-api.md) | Conversions API (CAPI) — eventos server-side |
| [ads-whatsapp-status.md](ads-whatsapp-status.md) | Ads em WhatsApp Status (novidade da v26.0) |

## Conteudo que continua em v25.0

Estas paginas deixaram de existir como referencia standalone na estrutura de docs da v26.0. O conteudo segue valido (as estruturas nao mudaram), mas para campos novos consultar o arquivo v26.0 indicado.

| Arquivo | Situacao |
|---|---|
| [object-story-spec.md](object-story-spec.md) | Consolidado pela Meta dentro de `ad-creative.md` |
| [ad-creative-link-data.md](ad-creative-link-data.md) | Consolidado pela Meta dentro de `ad-creative.md` |
| [outcome-driven-ads.md](outcome-driven-ads.md) | Post de blog de 2021, sem versao de API. ODAX segue obrigatorio na v26.0 |

## Avisos da v26.0 para o fluxo desta skill

- `instagram_positions`: **`explore` e `explore_home` nao existem mais** — especificar retorna erro. Remover de qualquer targeting.
- `messenger_positions`: valor `story` removido (silenciosamente).
- Conjuntos **HEC-F** (habitacao, emprego, credito) com targeting restrito **exigem** `targeting_automation.advantage_audience` explicito (`0` ou `1`). Os scripts desta skill nao passam esse flag sozinhos — incluir no `--targeting`.
- **Shop Ads**: criativos elegiveis passam a defaultar para `destination_type = WEBSITE_AND_SHOP` quando a conta tem shop. Opt-out via `destination_spec.destination_type = WEBSITE_AND_SHOP_OPT_OUT`.
- **Delivery Estimate**: campos `daily_outcomes_curve`, `budget_guardrail` e `estimate_dau` foram removidos da resposta. `targeting.py delivery` continua funcionando — esses campos apenas nao vem mais.
- **Poll ads**: `poll_spec` e o tipo `poll` em `interactive_components_spec` ficaram indisponiveis.
- **27/10/2026**: a maioria dessas remocoes passa a valer para TODAS as versoes, inclusive chamadas sem versao explicita.

---
Scrape em 2026-08-09. Os links "Try it in Graph API Explorer" dentro dos arquivos ainda apontam para `version=v25.0` — isso vem das proprias paginas da Meta e foi mantido verbatim.
