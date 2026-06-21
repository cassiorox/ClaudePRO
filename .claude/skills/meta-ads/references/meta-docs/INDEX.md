# Documentacao oficial Meta Marketing API — v25.0

Copia offline da documentacao oficial da Meta (developers.facebook.com), baixada para a versao **v25.0** da Graph/Marketing API. Consulte estes arquivos antes de subir ou editar campanhas quando precisar confirmar parametros, campos, edges ou comportamento da API.

> Sempre usar a versao MAIS ATUAL suportada pelo SDK instalado (hoje `v25.0`). Quando o SDK subir de versao, re-baixar estas paginas para a nova versao. Regra completa em `../api-reference.md`.

## Nucleo (referencia de objetos)

| Arquivo | Conteudo |
|---|---|
| [campaign.md](campaign.md) | Objeto Campaign — fields, edges, error codes (objetivos, special_ad_categories, bid_strategy no nivel de campanha) |
| [ad-set.md](ad-set.md) | Objeto Ad Set — orcamento, schedule, optimization_goal, billing_event, promoted_object, targeting |
| [ad.md](ad.md) | Objeto Ad — criativo, status, tracking_specs, conversion_domain |
| [ad-creative.md](ad-creative.md) | Objeto AdCreative — estrutura geral do criativo |
| [ad-creative-link-data.md](ad-creative-link-data.md) | link_data (imagem/carrossel): link, message, name, image_hash, child_attachments, call_to_action |
| [object-story-spec.md](object-story-spec.md) | object_story_spec — montagem do post do anuncio (page_id, link_data, video_data) |
| [targeting-specs.md](targeting-specs.md) | Estrutura de targeting — geo_locations, idade, genero, interesses, comportamentos, posicionamentos |
| [bidding.md](bidding.md) | Estrategias de lance (bid_strategy) e como/quando usar teto/custo-alvo |
| [insights.md](insights.md) | Insights API — visao geral e jobs assincronos |
| [insights-parameters.md](insights-parameters.md) | Parametros de insights: fields, date_preset, breakdowns, time_increment |
| [campaign-structure.md](campaign-structure.md) | Hierarquia Campaign > Ad Set > Ad |
| [changelog-v25.md](changelog-v25.md) | Changelog oficial da v25.0 (mudancas e deprecacoes) |

## Guias

| Arquivo | Conteudo |
|---|---|
| [get-started.md](get-started.md) | Primeiros passos com a Marketing API |
| [advantage-plus-sales.md](advantage-plus-sales.md) | Advantage+ Sales/App/Leads (substituto do ASC, descontinuado na v25) |
| [outcome-driven-ads.md](outcome-driven-ads.md) | ODAX — objetivos OUTCOME_* (obrigatorio desde a v21) |
| [conversions-api.md](conversions-api.md) | Conversions API (CAPI) — envio de eventos server-side |
| [custom-audiences.md](custom-audiences.md) | Publicos personalizados — criacao, schemas de hashing, regras |
| [lookalike-audiences.md](lookalike-audiences.md) | Publicos semelhantes (lookalike) — ratio, country, lookalike_spec |
| [lead-ads.md](lead-ads.md) | Lead Ads / formularios de geracao de leads |
| [carousel-ads.md](carousel-ads.md) | Anuncios em carrossel (e video) |

## Notas da v25.0 (importante)

- **Advantage+ Shopping (ASC)** e **Advantage+ App campaigns** estao **descontinuadas**: nao podem ser criadas, duplicadas nem editadas. Migrar para Advantage+ Sales/App/Leads padrao (ver `advantage-plus-sales.md`).
- **ODAX obrigatorio** desde a v21: usar objetivos `OUTCOME_*`.
- **Insights (jobs assincronos)** agora retornam campos de erro por padrao (`error_code`, `error_message`, `error_subcode`, `error_user_title`, `error_user_msg`); `error_code` mudou de `uint` para `int`. Parametro `metadata=1` depreciado.

## Fallbacks de URL no download (5 paginas)

Algumas URLs originais davam 404 na v25; foram substituidas pela referencia oficial equivalente (anotado no cabecalho de cada arquivo):
1. `targeting-specs` → `/audiences/reference/basic-targeting/`
2. `insights-parameters` → consolidado da Insights API + ad-account/insights (nao ha pagina standalone na v25)
3. `advantage-plus-sales` → `/advantage-campaigns/` (ASC descontinuada)
4. `carousel-ads` → `/guides/videoads/` (Video and Carousel Ads)
5. `outcome-driven-ads` → blog oficial do ODAX

---
Baixado em 2026-06-21. Para atualizar: re-rodar o scrape destas paginas quando o SDK `facebook-business` mudar de versao maior.
