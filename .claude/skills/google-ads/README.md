# Google Ads ClaudePRO

Skill de execucao para Google Ads no ecossistema ClaudePRO. Usa o SDK oficial `google-ads` do Python com queries GAQL.

## Instalacao

```bash
pip3 install "google-ads>=32.0.0" google-auth-oauthlib protobuf
```

A versao minima importa: ate a 31.4.0 a lib recusava rodar sem developer token, que o Google
aposentou em 09/09/2026.

## Configuracao

### Opcao 1: Setup automatico (recomendado)

```bash
cd .claude/skills/google-ads/scripts

# Verifica o que falta
python3 setup.py check

# Copie o modelo e preencha CLIENT_ID e CLIENT_SECRET no .env
#   cp ../.env.example ../.env
# Depois gere o refresh token automaticamente:
python3 setup.py oauth

# Teste a conexao:
python3 setup.py test

# Ou faca tudo de uma vez:
python3 setup.py full
```

Documentacao oficial Google Ads API: https://developers.google.com/google-ads/api/docs/get-started/introduction

### Opcao 2: Manual

Copie `.env.example` para `.env` na pasta da skill e preencha:

```
GOOGLE_ADS_CLIENT_ID="seu-client-id.apps.googleusercontent.com"
GOOGLE_ADS_CLIENT_SECRET="seu-client-secret"
GOOGLE_ADS_REFRESH_TOKEN="gerado pelo setup.py oauth"
GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"   # so se usar MCC, sem hifens
```

Ou use o formato padrao `google-ads.yaml` na mesma pasta.

**Nao existe mais developer token.** O Google aposentou em 09/09/2026. O nivel de acesso agora
pertence ao projeto do Google Cloud que gerou essas credenciais OAuth, e ele precisa estar em
**Explorer** ou acima. O passo a passo completo, com as pegadinhas, esta no `SKILL.md`.

## Scripts

| Script | Funcao |
|--------|--------|
| `read.py` | Leitura de campanhas, ad groups, keywords, ads, search terms |
| `insights.py` | Metricas e breakdowns (account, campaign, daily, device, hourly) |
| `create.py` | Criar campanhas, ad groups, keywords, RSAs, extensoes |
| `update.py` | Editar status, orcamento, bids |
| `delete.py` | Remover keywords, negativas, ads |
| `keyword_planner.py` | Pesquisa de keywords (volume, CPC, competicao) via KeywordPlanIdeaService |

## Uso

```bash
cd .claude/skills/google-ads/scripts

# Listar contas
python3 read.py accounts

# Campanhas de uma conta
python3 read.py campaigns --customer-id 1234567890

# Insights dos ultimos 30 dias
python3 insights.py account --customer-id 1234567890 --date-range LAST_30_DAYS

# Criar campanha (sempre PAUSED)
python3 create.py campaign --customer-id 1234567890 --name "Search-Leads" --type SEARCH --budget 5000

# Pesquisa de keywords (Keyword Planner)
python3 keyword_planner.py ideas --keywords "marketing digital|automacao com ia" --limit 50
python3 keyword_planner.py historical-metrics --keywords "claude code|cursor ai"
```

## Estrutura

```
google-ads/
├── SKILL.md              # Orquestrador (instrucoes pro Claude)
├── README.md             # Esta documentacao
├── contas.yaml           # Cadastro de contas/clientes
├── .gitignore
├── .env.example          # Modelo de credenciais (copie pra .env e preencha)
├── references/
│   ├── api-reference.md  # Referencia de GAQL queries uteis
│   └── mcp-server.md     # Playbook do servidor MCP oficial do Google Ads
└── scripts/
    ├── lib/
    │   └── __init__.py     # Auth, .env loader, helpers
    ├── setup.py            # Setup interativo (check, oauth, test)
    ├── read.py             # Leitura
    ├── insights.py         # Metricas e breakdowns
    ├── create.py           # Criacao
    ├── update.py           # Edicao
    ├── delete.py           # Exclusao
    └── keyword_planner.py  # Keyword Planner (descoberta + metricas historicas)
```
