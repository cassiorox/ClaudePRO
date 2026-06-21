# Documentacao oficial Google Ads API — v24

Copia offline da documentacao oficial do Google (developers.google.com/google-ads/api), baixada com a skill apontando para **v24** (versao em uso, teto do SDK `google-ads` 31.0.0 instalado). Consulte estes arquivos antes de criar/editar campanhas, montar GAQL ou confirmar campos/comportamento da API.

> **Versao:** o projeto usa `v24`, a versao mais nova suportada pelo SDK 31.0.0 (atualizado de 30.0.0 em 21/06/2026, que travava em v23). Regra completa e tabela de sunset em `../api-reference.md`. As paginas oficiais servem sempre a versao mais recente em servico.

## Conceitos e estrutura

| Arquivo | Conteudo |
|---|---|
| [start-introduction.md](start-introduction.md) | Introducao / get started com a API |
| [concepts-overview.md](concepts-overview.md) | Visao geral dos conceitos da API |
| [best-practices-overview.md](best-practices-overview.md) | Boas praticas, rate limits, performance |
| [sunset-dates.md](sunset-dates.md) | Cronograma de deprecacao e sunset das versoes |
| [release-notes.md](release-notes.md) | Release notes completas (historico de versoes) |

## Campanhas e estrutura de conta

| Arquivo | Conteudo |
|---|---|
| [campaigns-create.md](campaigns-create.md) | Criar campanhas (guia completo e detalhado, ~53 KB) |
| [campaign-budgets.md](campaign-budgets.md) | Orcamentos de campanha |
| [ad-groups-create.md](ad-groups-create.md) | Criar grupos de anuncios |
| [responsive-search-ads.md](responsive-search-ads.md) | Anuncios responsivos de pesquisa (RSA) |
| [bidding-strategy-types.md](bidding-strategy-types.md) | Tipos de estrategia de lance |
| [assets-overview.md](assets-overview.md) | Assets/extensoes (sitelinks, callouts, snippets) |
| [conversions-overview.md](conversions-overview.md) | Acompanhamento de conversoes |
| [performance-max-overview.md](performance-max-overview.md) | Campanhas Performance Max |

## Keyword planning

| Arquivo | Conteudo |
|---|---|
| [keyword-planning-overview.md](keyword-planning-overview.md) | Visao geral do planejamento de keywords |
| [keyword-ideas.md](keyword-ideas.md) | Gerar ideias de keywords (volume, CPC, concorrencia) |

## GAQL (Google Ads Query Language)

| Arquivo | Conteudo |
|---|---|
| [gaql-overview.md](gaql-overview.md) | Visao geral da GAQL |
| [gaql-grammar.md](gaql-grammar.md) | Gramatica formal da GAQL |
| [gaql-structure.md](gaql-structure.md) | Estrutura das queries (SELECT/FROM/WHERE/ORDER/LIMIT) |
| [gaql-cookbook.md](gaql-cookbook.md) | Exemplos prontos de queries |
| [date-ranges.md](date-ranges.md) | Periodos pre-definidos e segmentacao por data |

## Fallbacks de URL no download (5 paginas)

Algumas URLs originais davam 404; foram substituidas pela canonica oficial (anotado no cabecalho de cada arquivo):
1. campaign-budgets → `/campaigns/budgets/overview`
2. ad-groups → `/campaigns/create-ad-groups`
3. RSA → `/responsive-search-ads/overview`
4. bidding → `/campaigns/bidding/strategy-types`
5. date-ranges → `/query/date-ranges`

## Notas de versao (sunset-dates)

- **v24** (22/04/2026) — major estavel **em uso**, teto do SDK 31.0.0. Minor mais recente: **v24.1** (13/05/2026). Sunset ~2027.
- v23 (28/01/2026) — sunset previsto **fev/2027**.
- v22 sunset ~out/2026 (tentativo); v21 sunset ~ago/2026 (tentativo).
- Deprecacoes relevantes: call-only ads param de servir em fev/2027; conversoes offline / Customer Match migrando para a Data Manager API.

---
Baixado em 2026-06-21 (v24, apos upgrade do SDK 30.0.0 → 31.0.0). Para atualizar: atualizar o SDK `google-ads` e re-rodar o scrape destas paginas quando mudar de versao maior.
