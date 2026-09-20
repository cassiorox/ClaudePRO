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
pip3 install "google-ads>=32.0.0" google-auth-oauthlib protobuf
```

A versao minima importa: ate a 31.4.0 a biblioteca recusava rodar sem developer token, que desde
09/09/2026 nao e mais emitido pra quem esta comecando. Quem ja tem a lib instalada atualiza com
`pip3 install --upgrade "google-ads>=32.0.0"`.

### 2. Verificar .env

Checar se existe `.claude/skills/google-ads/.env`. Se NAO existir, criar a partir do modelo que ja vem na pasta:

```bash
cp .claude/skills/google-ads/.env.example .claude/skills/google-ads/.env
```

O modelo tem os campos comentados. Sao dois obrigatorios (`CLIENT_ID` e `CLIENT_SECRET`) mais o
`REFRESH_TOKEN`, que o proprio setup gera.

**Fallback**: Se existir `.claude/skills/google-ads/google-ads.yaml`, o SDK carrega dele automaticamente.

### 3. Conseguir as credenciais no Google Cloud

> **Mudou em setembro de 2026.** O Google aposentou os developer tokens em 09/09/2026. Quem manda no
> nivel de acesso agora e o **projeto do Google Cloud** que gerou as credenciais OAuth, nao mais o token.
> Tambem **nao e mais necessario ter conta MCC**. Tutorial que ainda manda pegar developer token na
> Central de API esta desatualizado. Fonte:
> https://developers.google.com/google-ads/api/docs/api-policy/developer-token

Sao nove passos, nesta ordem. O Claude deve guiar o usuario um a um e conferir antes de seguir:

1. **Criar o projeto** no [Google Cloud Console](https://console.cloud.google.com/).
2. **Entrar no projeto criado.** O seletor de projeto no topo da tela **nao muda sozinho** depois de
   criar. Se seguir direto, o usuario ativa a API, pede acesso e cria credenciais tudo no projeto
   anterior, sem nenhum aviso. Pedir pra ele confirmar o nome no seletor antes de continuar.
3. **Ativar a Google Ads API** nesse projeto.
4. **Configurar a tela de consentimento** (tipo Externo, nome do app, e-mail de contato).
5. **Publicar o app.** Em *Google Auth Platform > Publico-alvo*, botao **Publicar app**. Enquanto o
   status for "Testes", o refresh token **expira em 7 dias** e a integracao morre sozinha na semana
   seguinte. Publicar exige pagina inicial e links de termos de uso e privacidade de um dominio proprio.
6. **Criar as credenciais OAuth** do tipo **App para computador**. Guardar Client ID e Client secret.
7. **Pedir o nivel Explorer** na
   [Google Ads API Overview](https://console.cloud.google.com/google/ads-apis/overview), com o projeto
   certo selecionado. Sem isso o projeto fica em **Test**: a autenticacao funciona normalmente e **toda
   chamada a conta de producao falha**. A revisao e automatica, costuma sair em minutos.
8. **Gerar o refresh token** com `setup.py oauth` (passo 4 abaixo).
9. **Testar** uma leitura real com `setup.py test`.

A ordem importa: **publicar o app (5) antes de gerar o token (8)**. O prazo de 7 dias e carimbado no
momento em que o token e emitido, e publicar depois nao estende um token que ja existe. Se o usuario
gerou antes, ele precisa gerar de novo.

Preencher no `.env`: `GOOGLE_ADS_CLIENT_ID` e `GOOGLE_ADS_CLIENT_SECRET`. O `LOGIN_CUSTOMER_ID` so
entra se o usuario consulta contas atraves de um MCC, e sempre sem hifens. O `REFRESH_TOKEN` o setup
gera sozinho no proximo passo.

### 4. Gerar refresh token (automatico)

Depois que CLIENT_ID e CLIENT_SECRET estiverem no .env, rodar:

```bash
python3 .claude/skills/google-ads/scripts/setup.py oauth
```

Isso abre o browser, o usuario autoriza, e o refresh token e salvo automaticamente no .env. Sem
copiar/colar nada.

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

### Erros de setup: o que cada um quer dizer

O erro quase sempre aparece longe da causa. Esta tabela e o atalho:

| Sintoma | Causa real | Solucao |
|---|---|---|
| `CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION` (ou `ACTION_NOT_PERMITTED` em versao antiga) | Projeto Cloud em Test, alcanca so contas de teste | Pedir Explorer na Google Ads API Overview, nao na Central de API |
| Pedido de Explorer recusado | Projeto vinculado a conta de faturamento em **Free Trial** ou com billing suspenso | Migrar o projeto pro tier pago ou desvincular o billing dele. A API em si e gratuita |
| Funcionava e parou exatamente 7 dias depois | Token emitido com o app em status "Testes" | Publicar o app e **gerar o refresh token de novo** |
| `Acesso bloqueado: o app nao concluiu o processo de verificacao` / `Erro 403: access_denied` | App externo em "Testes" e o e-mail nao esta na lista de testadores | Adicionar em *Publico-alvo > Usuarios de teste*, ou melhor: publicar o app |
| `Erro 500` na tela de consentimento | Propagacao, o app foi publicado ha poucos minutos | Esperar de 10 a 15 minutos. Nao e erro de configuracao |
| Credencial "invalida" sem motivo aparente | Passo 2: API ativada ou credencial criada no projeto errado | Conferir o seletor de projeto e refazer no projeto certo |
| `DEVELOPER_TOKEN_NOT_APPROVED` | Erro do fluxo antigo, praticamente extinto desde 09/09/2026 | Tratar como nivel de acesso do projeto Cloud |
| `The customer account can't be accessed because it is not yet enabled or has been deactivated` | A conta do Google Ads em si esta desativada | Nao e problema de API. Conferir no painel do Google Ads |
| `PERMISSION_DENIED` / `USER_PERMISSION_DENIED` | A conta do OAuth nao tem acesso ao customer ID, ou falta o login customer ID do MCC | Conferir `GOOGLE_ADS_LOGIN_CUSTOMER_ID` e o acesso no MCC |

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

## Versao da API (sempre usar a mais atual)

A skill usa sempre a versao MAIS RECENTE da Google Ads API suportada pelo SDK `google-ads` instalado. Hoje e **`v25`** (SDK 32.0.0, atualizado em 20/09/2026) -- o `GoogleAdsClient` ja usa a v25 por padrao. Detalhe importante: ate a 31.4.0 a biblioteca **recusava** rodar sem developer token, mesmo com a API ja aceitando sem. Foi a 32.0.0 que removeu essa validacao, entao quem for usar sem token precisa da 32.0.0 ou maior. Detalhes e tabela de sunset em `references/api-reference.md`.

Documentacao oficial do Google baixada para consulta offline: pasta `references/google-docs/` (indice em `references/google-docs/INDEX.md`). Consultar quando precisar confirmar campos, montar GAQL ou checar comportamento da API antes de criar/editar objetos.

## Servidor MCP oficial do Google Ads

Se o usuario perguntar sobre **MCP do Google Ads**, servidor MCP, `google-ads-mcp`, ou como conectar o
Claude direto na conta sem usar os scripts, **ler `references/mcp-server.md`** e seguir de la. E um
playbook completo, testado, com instalacao, autenticacao por Application Default Credentials, registro no
Claude Code e troubleshooting.

Resumo pra responder rapido antes de abrir o playbook:

- O servidor MCP oficial do Google e **somente leitura** e tem so tres ferramentas. Nao cria nem pausa nada.
- Ele **nao substitui esta skill**. Regra curta: ler e explorar, MCP. Escrever e repetir, skill.
- Ele exige o mesmo projeto Cloud e as mesmas credenciais OAuth desta skill. Quem ja rodou
  `/google-ads setup` tem o trabalho pesado feito.
- A pegadinha principal: ele **nao le** `GOOGLE_ADS_CLIENT_ID` e companhia. Ele quer Application Default
  Credentials. O `mcp/criar-adc.py` desta skill monta esse arquivo a partir do `.env`.
- No **Meta Ads e diferente**: existe conector oficial dentro do Claude, um clique, sem app nem token.
  A razao esta na secao 13 do playbook: a Google Ads API autoriza o projeto Cloud, nao a pessoa.

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
7. **Nunca hardcodar tokens** — sempre usar o `.env` da skill ou google-ads.yaml. Nunca colar credencial dentro de comando Bash nem de arquivo versionado
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
