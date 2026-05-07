---
name: google-ads
description: Gerencia campanhas Google Ads via SDK oficial (google-ads). Le campanhas, ad groups, keywords, anuncios, search terms, quality scores e insights com GAQL. Cria, edita, pausa e deleta objetos. Faz pesquisa de keywords (Keyword Planner) com volume, CPC e competicao. Use quando o usuario mencionar google ads, campanhas de search, performance max, pmax, keywords, termos de busca, quality score, google adwords, criar campanha google, pausar campanha google, orcamento google ads, RSA, responsive search ad, sitelink, callout, negativas, keyword planner, pesquisa de keywords, volume de busca, CPC estimado. Tambem dispara com /google-ads setup.
---

# Google Ads ClaudePRO

Skill completa para gestao de Google Ads via SDK oficial (`google-ads`). Executa queries GAQL para leitura, e mutate operations para escrita. Equivalente ao meta-ads para o ecossistema Google.

## Setup (primeira vez)

Quando o usuario pedir para configurar, rodar setup, ou for a primeira vez usando a skill, o Claude deve guiar o setup interativo.

**O setup tem um script automatizado** em `scripts/setup.py` que simplifica o processo:

### 1. Verificar dependencias

```bash
pip3 install google-ads google-auth-oauthlib protobuf
```

### 2. Verificar .env

Checar se existe `.claude/skills/google-ads/.env`. Se NAO existir, criar com o template:

```
# Google Ads ClaudePRO — Configuracao
# Os scripts leem este arquivo automaticamente. NAO precisa adicionar ao ~/.zshrc.

# OBRIGATORIO: Developer token (Google Ads API Center)
GOOGLE_ADS_DEVELOPER_TOKEN=""

# OBRIGATORIO: OAuth2 credentials (Google Cloud Console)
GOOGLE_ADS_CLIENT_ID=""
GOOGLE_ADS_CLIENT_SECRET=""
GOOGLE_ADS_REFRESH_TOKEN=""

# OBRIGATORIO: Login customer ID (MCC sem hifens, ex: 1234567890)
GOOGLE_ADS_LOGIN_CUSTOMER_ID=""

# OPCIONAL: Customer ID padrao (evita ter que passar --customer-id toda vez)
GOOGLE_ADS_CUSTOMER_ID=""
```

**Fallback**: Se existir `.claude/skills/google-ads/google-ads.yaml`, o SDK carrega dele automaticamente.

### 3. Preencher credenciais no .env

O usuario precisa obter e preencher no .env (documentacao oficial: https://developers.google.com/google-ads/api/docs/get-started/introduction):

1. **DEVELOPER_TOKEN** — Central de API no Google Ads (Ferramentas > Central de API)
2. **CLIENT_ID e CLIENT_SECRET** — Google Cloud Console (criar projeto > ativar Google Ads API > credenciais OAuth)
3. **LOGIN_CUSTOMER_ID** — ID do MCC (sem hifens)

O **REFRESH_TOKEN** NAO precisa ser preenchido manualmente — o setup.py gera automaticamente (ver passo 4).

### 4. Gerar refresh token (automatico)

Depois que CLIENT_ID, CLIENT_SECRET e DEVELOPER_TOKEN estiverem no .env, rodar:

```bash
python3 .claude/skills/google-ads/scripts/setup.py oauth
```

Isso abre o browser, o usuario autoriza, e o refresh token e salvo automaticamente no .env. Sem copiar/colar nada.

**Ou rodar o fluxo completo de uma vez:**

```bash
python3 .claude/skills/google-ads/scripts/setup.py full
```

Subcomandos do setup.py:

| Subcomando | O que faz |
|---|---|
| `check` | Verifica dependencias e variaveis do .env |
| `oauth` | Gera refresh token via OAuth2 (abre browser) |
| `test` | Testa conexao listando contas acessiveis |
| `full` | Fluxo completo: check + oauth (se necessario) + test |

### 5. Cadastro de contas (contas.yaml) — SETUP CONVERSACIONAL

Depois que o `.env` estiver preenchido e o teste passar, o Claude DEVE proativamente guiar o cadastro de contas:

1. Rodar `read.py accounts` para listar todas as contas acessiveis
2. Perguntar ao usuario: "Qual a tua principal conta Google Ads? Me passa o nome do cliente, e eu preencho o contas.yaml pra ti."
3. Para cada cliente, perguntar:
   - Nome do cliente
   - Customer ID (sem hifens)
4. Preencher o `contas.yaml` automaticamente com as respostas
5. Perguntar: "Quer cadastrar mais algum cliente?"

## Cadastro de clientes (contas.yaml)

**Arquivo:** `.claude/skills/google-ads/contas.yaml`

Antes de executar qualquer operacao, o Claude DEVE ler este arquivo para resolver nomes de clientes para IDs.
Quando o usuario disser "insights do Meu Cliente no Google" ou "campanhas da Meu Cliente", consultar o contas.yaml
para obter o customer_id do cliente.

Se o cliente nao estiver cadastrado, perguntar os dados e oferecer para adicionar ao arquivo.

## Como usar

Todos os scripts estao em `.claude/skills/google-ads/scripts/`. O padrao e:

```
python3 <script>.py <subcomando> [argumentos]
```

O Claude deve interpretar o pedido do usuario e executar o script correto via Bash.

---

## Referencia rapida de operacoes

### Leitura (read.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `accounts` | Lista contas acessiveis via MCC | `read.py accounts` |
| `campaigns` | Campanhas com status, tipo, orcamento | `read.py campaigns --customer-id 1234567890` |
| `ad-groups` | Ad groups de uma campanha | `read.py ad-groups --customer-id 123 --campaign-id 456` |
| `keywords` | Keywords com QS, match type, metricas | `read.py keywords --customer-id 123 --campaign-id 456` |
| `ads` | Anuncios RSA com headlines e descriptions | `read.py ads --customer-id 123 --campaign-id 456` |
| `search-terms` | Termos de busca com metricas | `read.py search-terms --customer-id 123` |
| `extensions` | Assets/extensoes (sitelinks, callouts) | `read.py extensions --customer-id 123` |
| `negative-keywords` | Negativas (campaign e ad group) | `read.py negative-keywords --customer-id 123` |
| `quality-scores` | QS decomposto (creative, landing, ctr) | `read.py quality-scores --customer-id 123` |

### Insights (insights.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `account` | KPIs da conta | `insights.py account --customer-id 123 --date-range LAST_30_DAYS` |
| `campaign` | Metricas por campanha | `insights.py campaign --customer-id 123 --date-range LAST_7_DAYS` |
| `ad-group` | Metricas por ad group | `insights.py ad-group --customer-id 123 --campaign-id 456` |
| `keyword` | Metricas por keyword | `insights.py keyword --customer-id 123 --campaign-id 456` |
| `daily` | Evolucao diaria | `insights.py daily --customer-id 123 --since 2026-03-01 --until 2026-03-31` |
| `device` | Breakdown por dispositivo | `insights.py device --customer-id 123 --date-range LAST_30_DAYS` |
| `hourly` | Breakdown por hora do dia | `insights.py hourly --customer-id 123 --date-range LAST_7_DAYS` |

Parametros comuns de insights:

| Parametro | O que faz | Exemplo |
|---|---|---|
| `--customer-id` | ID da conta (sem hifens) | `1234567890` |
| `--date-range` | Periodo relativo | `LAST_7_DAYS`, `LAST_30_DAYS`, `THIS_MONTH` |
| `--since` / `--until` | Periodo especifico | `2026-03-01` / `2026-03-31` |
| `--campaign-id` | Filtrar por campanha | `123456789` |
| `--limit` | Limite de resultados | `50` |

### Criacao (create.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `campaign` | Cria campanha PAUSED | `create.py campaign --customer-id 123 --name "Search-Leads" --type SEARCH --budget 5000` |
| `ad-group` | Cria ad group | `create.py ad-group --customer-id 123 --campaign-id 456 --name "Broad-Keywords"` |
| `keyword` | Adiciona keywords | `create.py keyword --customer-id 123 --ad-group-id 456 --text "marketing digital" --match-type PHRASE` |
| `rsa` | Cria Responsive Search Ad | `create.py rsa --customer-id 123 --ad-group-id 456 --headlines "h1|h2|h3" --descriptions "d1|d2"` |
| `sitelink` | Cria sitelink | `create.py sitelink --customer-id 123 --campaign-id 456 --text "Fale Conosco" --url "https://..."` |
| `callout` | Cria callout | `create.py callout --customer-id 123 --campaign-id 456 --text "Frete Gratis"` |
| `negative` | Adiciona negativa | `create.py negative --customer-id 123 --campaign-id 456 --text "gratis" --match-type EXACT` |

**IMPORTANTE:** Todas as criacoes sao feitas com status PAUSED. Revisar antes de ativar.

### Edicao (update.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `campaign` | Editar status, orcamento, bidding | `update.py campaign --customer-id 123 --campaign-id 456 --status ENABLED --budget 10000` |
| `ad-group` | Editar status, CPC | `update.py ad-group --customer-id 123 --ad-group-id 456 --status PAUSED` |
| `keyword` | Editar status, bid | `update.py keyword --customer-id 123 --keyword-id 456 --status ENABLED` |
| `ad` | Editar status | `update.py ad --customer-id 123 --ad-id 456 --status PAUSED` |

### Exclusao (delete.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `keyword` | Remove keyword | `delete.py keyword --customer-id 123 --keyword-id 456` |
| `negative` | Remove negativa | `delete.py negative --customer-id 123 --criterion-id 456 --level campaign --parent-id 789` |
| `ad` | Remove anuncio | `delete.py ad --customer-id 123 --ad-group-id 456 --ad-id 789` |

### Keyword Planner (keyword_planner.py)

Descoberta de keywords novas e metricas historicas via `KeywordPlanIdeaService` (sem precisar criar campanha). Defaults pra Brasil: `location-id=2076`, `language-id=1014` (Portugues).

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `ideas` | Gera ideias de keywords a partir de seed terms e/ou URL. Retorna volume mensal, CPC top of page (low/high), competicao (LOW/MEDIUM/HIGH) e index 0-100 | `keyword_planner.py ideas --keywords "marketing digital\|automacao com ia" --limit 50` |
| `historical-metrics` | Volume/CPC historico de uma lista de keywords (sem gerar novas). Retorna tambem volume mes-a-mes dos ultimos 12 meses | `keyword_planner.py historical-metrics --keywords "claude code\|cursor ai\|github copilot"` |

Parametros comuns dos dois subcomandos:

| Parametro | O que faz | Default |
|---|---|---|
| `--customer-id` | ID da conta (sem hifens) | `GOOGLE_ADS_CUSTOMER_ID` |
| `--keywords` | Seeds separadas por `\|`. `ideas` aceita ate 20, `historical-metrics` ate 10000 | — |
| `--url` | URL como seed (so `ideas`). Combinavel com `--keywords` | — |
| `--location-id` | Geo target constant ID. Multiplos separados por virgula | `2076` (Brasil) |
| `--language-id` | Language constant ID | `1014` (Portugues) |
| `--network` | `GOOGLE_SEARCH` ou `GOOGLE_SEARCH_AND_PARTNERS` | `GOOGLE_SEARCH_AND_PARTNERS` |
| `--include-adult` | Inclui keywords adultas | `false` |
| `--limit` | Limita N resultados (so `ideas`, ordenado por volume DESC) | sem limite |

Geo target constants comuns: `2076` Brasil, `1001773` Sao Paulo, `1001852` Rio de Janeiro, `2840` USA. Lista completa: https://developers.google.com/google-ads/api/data/geotargets

Language constants: `1014` Portugues, `1000` Ingles, `1003` Espanhol. Lista: https://developers.google.com/google-ads/api/data/codes-formats#languages

---

## Aprendizados (memória persistente)

**Arquivo:** `aprendizados.md` (na raiz da skill, `.claude/skills/google-ads/aprendizados.md`)

O Claude DEVE:
1. **Ler `aprendizados.md` no início de QUALQUER operação de criação** (campanha, ad group, keyword, RSA)
2. **Quando o usuário corrigir algo**, perguntar: "Quer que eu registre isso nos aprendizados?"
3. **Quando o usuário pedir** ("lembra disso", "registra"), registrar imediatamente
4. **Não duplicar** — verificar se já existe regra similar antes de adicionar

## Registro no historico (apos acoes de escrita)

Depois de qualquer acao que modifica a conta (create, update, delete, pause, activate),
o Claude DEVE perguntar:

> "Quer que eu registre essa acao no historico de otimizacoes?"

Se o usuario confirmar, registrar num arquivo `historico.md` na raiz do workspace com:
- Cliente, o que foi feito (com IDs), motivo, hipotese e metricas antes.

Essa regra garante que o historico de otimizacoes nao se perde.

## Regras de seguranca

O Claude DEVE seguir estas regras ao executar operacoes:

1. **Criar sempre PAUSED** — nunca criar objetos com status ENABLED diretamente
2. **Confirmar antes de deletar** — perguntar ao usuario antes de executar delete
3. **Confirmar antes de ativar** — perguntar antes de mudar status para ENABLED
4. **Ativar TODOS os niveis** — ao ativar uma campanha, SEMPRE ativar tambem todos os ad groups e ads dentro dela. Ordem: campaign -> ad groups -> ads
5. **Respeitar rate limits** — se receber erro de rate limit (RESOURCE_EXHAUSTED), aguardar 60 segundos antes de tentar novamente
6. **Orcamento com cuidado** — ao alterar budget, confirmar o valor com o usuario. Valores sao em micros (5000000 = R$5,00) mas os scripts ja convertem
7. **Nunca hardcodar tokens** — sempre usar env vars ou google-ads.yaml
8. **Nunca assumir origem de dados** — ao mostrar insights no nivel da conta, SEMPRE quebrar por campanha antes de atribuir resultados a uma campanha especifica
9. **cost_micros** — todos os scripts convertem automaticamente cost_micros / 1_000_000 para reais na saida
10. **NUNCA usar MCPs** — esta skill usa SOMENTE os scripts Python locais, NUNCA tools de MCP (adloop, google-ads-mcp, etc)

## Fluxos comuns

### Criar campanha Search completa

1. `create.py campaign` — cria campanha PAUSED
2. `create.py ad-group` — cria ad group PAUSED
3. `create.py keyword` — adiciona keywords (repetir para cada keyword)
4. `create.py rsa` — cria Responsive Search Ad
5. `create.py sitelink` — adiciona sitelinks (opcional)
6. `create.py callout` — adiciona callouts (opcional)
7. Validar: `read.py campaigns`, `read.py ads`, `read.py keywords`
8. Ativar quando pronto (todos os niveis)

### Auditoria de conta

1. `insights.py account` — visao geral
2. `insights.py campaign` — performance por campanha
3. `read.py quality-scores` — QS decomposto
4. `read.py search-terms` — termos de busca (negativar irrelevantes)
5. `insights.py device` — breakdown por dispositivo
6. `read.py negative-keywords` — conferir negativas

### Puxar relatorio de performance

1. `insights.py campaign --date-range LAST_30_DAYS`
2. `insights.py daily --since 2026-03-01 --until 2026-03-31`
3. `insights.py keyword --campaign-id XXX`

### Pesquisa de keywords antes de criar campanha

1. `keyword_planner.py ideas --keywords "tema 1|tema 2"` — descobre keywords relacionadas com volume e CPC estimado
2. `keyword_planner.py ideas --url https://site-do-cliente.com.br --limit 100` — gera ideias a partir da landing page
3. `keyword_planner.py historical-metrics --keywords "lista|de|keywords|escolhidas"` — valida volume/CPC das que vai usar
4. `create.py keyword --ad-group-id XXX --text "keyword escolhida" --match-type PHRASE` — adiciona ao ad group
