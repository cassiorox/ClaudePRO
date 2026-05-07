# Google Ads ClaudePRO

Skill de execucao para Google Ads no ecossistema ClaudePRO. Usa o SDK oficial `google-ads` do Python com queries GAQL.

## Instalacao

```bash
pip3 install google-ads google-auth-oauthlib protobuf
```

## Configuracao

### Opcao 1: Setup automatico (recomendado)

```bash
cd .claude/skills/google-ads/scripts

# Verifica o que falta
python3 setup.py check

# Preencha CLIENT_ID, CLIENT_SECRET e DEVELOPER_TOKEN no .env
# Depois gere o refresh token automaticamente:
python3 setup.py oauth

# Teste a conexao:
python3 setup.py test

# Ou faca tudo de uma vez:
python3 setup.py full
```

Documentacao oficial Google Ads API: https://developers.google.com/google-ads/api/docs/get-started/introduction

### Opcao 2: Manual

Crie o arquivo `.claude/skills/google-ads/.env` com:

```
GOOGLE_ADS_DEVELOPER_TOKEN="seu-developer-token"
GOOGLE_ADS_CLIENT_ID="seu-client-id.apps.googleusercontent.com"
GOOGLE_ADS_CLIENT_SECRET="seu-client-secret"
GOOGLE_ADS_REFRESH_TOKEN="seu-refresh-token"
GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"
```

Ou use o formato padrao `google-ads.yaml` na mesma pasta.

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
├── references/
│   └── api-reference.md  # Referencia de GAQL queries uteis
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
