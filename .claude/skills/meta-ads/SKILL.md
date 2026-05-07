---
name: meta-ads
description: Gerencia campanhas Meta Ads (Facebook/Instagram) via SDK oficial. Le campanhas, conjuntos, anuncios, criativos e insights. Cria, edita, pausa, duplica e deleta objetos. Busca interesses, comportamentos e geolocalizacoes para targeting. Troca url_tags em criativos existentes. Use quando o usuario mencionar meta ads, facebook ads, instagram ads, campanha, conjunto de anuncios, ad set, criativo, targeting, publico, insights, metricas de anuncio, duplicar campanha, url_tags, utm, criar campanha, pausar campanha, orcamento de campanha, audiencia, lookalike, pixel. Tambem dispara com /meta-ads setup.
---

# Meta Ads ClaudePRO

Skill completa para gestao de Meta Ads via SDK oficial (`facebook-business`). Substitui o MCP fb-ads-mcp-server com mais poder: duplicacao de campanhas/ads, swap de url_tags, e acesso total a API.

## Setup (primeira vez)

Quando o usuario pedir para configurar, rodar setup, ou for a primeira vez usando a skill, o Claude deve guiar o setup interativo.

**IMPORTANTE:** Ler `references/setup-meta-app.md` ANTES de comecar o setup. Esse arquivo contem o passo a passo completo para criar o app no Meta Developer Dashboard, gerar o token e resolver problemas. Se o aluno mandar prints ou tiver duvidas sobre alguma tela do Facebook, consultar esse arquivo para orientar.

### 1. Verificar dependencias

```bash
python3 .claude/skills/meta-ads/scripts/setup.py
```

### 2. Verificar .env

Checar se existe `.claude/skills/meta-ads/.env`. Se NAO existir, criar com o template:

```
# Meta Ads ClaudePRO — Configuracao
# Os scripts leem este arquivo automaticamente. NAO precisa adicionar ao ~/.zshrc.

# OBRIGATORIO: Token de acesso da Meta (gerar em developers.facebook.com > Graph API Explorer)
META_ADS_TOKEN=""

# OBRIGATORIO: App ID do app Meta que gerou o token (ver em developers.facebook.com > My Apps)
META_APP_ID=""

# OPCIONAL: Conta de anuncio padrao (evita ter que passar --account toda vez)
META_AD_ACCOUNT_ID=""
```

Depois de criar, orientar o usuario a:
1. Preencher o `META_ADS_TOKEN` (token de acesso)
2. Preencher o `META_APP_ID` (ID do app Meta — ex: 905545132380980)

**IMPORTANTE**: Os scripts leem o `.env` automaticamente. NAO precisa fazer `source` no `~/.zshrc`.
O token fica isolado dentro da skill e nao vaza pra outras sessoes do terminal.

**IMPORTANTE:** O app Meta DEVE estar em modo Live (nao Development) para criar dark posts e criativos via API. Se der erro "app em modo de desenvolvimento", orientar o usuario a mudar o app para modo Live no painel developers.facebook.com. Alem disso, as paginas do Facebook que serao usadas nos anuncios devem estar vinculadas/autorizadas no app.

### 3. Cadastro de contas (contas.yaml) — SETUP CONVERSACIONAL

Depois que o `.env` estiver preenchido e o `setup.py` passar, o Claude DEVE proativamente guiar o cadastro de contas:

1. Rodar `read.py accounts` para listar todas as contas disponiveis
2. Perguntar ao usuario: "Qual a tua principal conta de anuncio? Me passa o nome do cliente, e eu preencho o contas.yaml pra ti."
3. Para cada cliente, perguntar (ou buscar na API se possivel):
   - Nome do cliente
   - Conta de anuncio (act_XXX) — pode escolher da lista
   - Page ID do Facebook
   - Instagram ID e @username
4. Preencher o `contas.yaml` automaticamente com as respostas
5. Perguntar: "Quer cadastrar mais algum cliente?"

Esse fluxo conversacional e o jeito ideal de configurar — o usuario so responde as perguntas e o Claude preenche tudo.

## Cadastro de clientes (contas.yaml)

**Arquivo:** `.claude/skills/meta-ads/contas.yaml`

Antes de executar qualquer operacao, o Claude DEVE ler este arquivo para resolver nomes de clientes para IDs.
Quando o usuario disser "cria campanha pra DobraLabs" ou "insights do Ronnau", consultar o contas.yaml
para obter conta_anuncio, pagina_facebook e instagram_id do cliente.

Se o cliente nao estiver cadastrado, perguntar os dados e oferecer para adicionar ao arquivo.

## Como usar

Todos os scripts estao em `.claude/skills/meta-ads/scripts/`. O padrao e:

```
python3 <script>.py <subcomando> [argumentos]
```

O Claude deve interpretar o pedido do usuario e executar o script correto via Bash.

---

## Referencia rapida de operacoes

### Leitura (read.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `accounts` | Lista contas de anuncio | `read.py accounts` |
| `account-details` | Detalhes de uma conta | `read.py account-details --id act_123` |
| `campaigns` | Lista campanhas | `read.py campaigns --account act_123 --status ACTIVE` |
| `campaign` | Detalhes de uma campanha | `read.py campaign --id 123` |
| `adsets` | Lista ad sets de uma conta | `read.py adsets --account act_123` |
| `adsets-by-campaign` | Ad sets de uma campanha | `read.py adsets-by-campaign --campaign 123` |
| `adset` | Detalhes de um ad set | `read.py adset --id 123` |
| `adsets-by-ids` | Varios ad sets por IDs | `read.py adsets-by-ids --ids 123,456` |
| `ads` | Lista ads de uma conta | `read.py ads --account act_123 --status ACTIVE` |
| `ads-by-campaign` | Ads de uma campanha | `read.py ads-by-campaign --campaign 123` |
| `ads-by-adset` | Ads de um ad set | `read.py ads-by-adset --adset 123` |
| `ad` | Detalhes de um ad | `read.py ad --id 123` |
| `creative` | Detalhes de um criativo | `read.py creative --id 123` |
| `creatives-by-ad` | Criativos de um ad | `read.py creatives-by-ad --ad 123` |
| `preview` | Preview HTML de criativo | `read.py preview --creative 123 --format INSTAGRAM_STORY` ou `--format all` |
| `images` | Lista imagens da conta | `read.py images --account act_123` |
| `videos` | Lista videos da conta | `read.py videos --account act_123` |
| `activities` | Log de atividades da conta | `read.py activities --account act_123` |
| `activities-by-adset` | Atividades de um ad set | `read.py activities-by-adset --adset 123` |
| `custom-audiences` | Lista audiencias custom | `read.py custom-audiences --account act_123` |
| `lookalike-audiences` | Lista audiencias lookalike | `read.py lookalike-audiences --account act_123` |
| `paginate` | Busca URL de paginacao | `read.py paginate --url "https://..."` |

### Insights (insights.py)

| Subcomando | Exemplo |
|---|---|
| `account` | `insights.py account --id act_123 --date-preset last_7d` |
| `campaign` | `insights.py campaign --id 123 --date-preset last_30d --breakdowns age,gender` |
| `adset` | `insights.py adset --id 123 --time-range '{"since":"2026-03-01","until":"2026-03-31"}'` |
| `ad` | `insights.py ad --id 123 --date-preset yesterday` |
| `async` | `insights.py async --id act_123 --date-preset maximum --level campaign` |

Parametros de insights:

| Parametro | O que faz | Exemplo |
|---|---|---|
| `--date-preset` | Periodo relativo | `last_7d`, `last_30d`, `today`, `maximum` |
| `--time-range` | Periodo especifico (JSON) | `'{"since":"2026-01-01","until":"2026-01-31"}'` |
| `--time-ranges` | Comparacao entre periodos (JSON) | `'[{"since":"2026-01","until":"2026-01-31"},{"since":"2026-02-01","until":"2026-02-28"}]'` |
| `--time-increment` | Granularidade | `1`, `7`, `monthly`, `all_days` |
| `--breakdowns` | Segmentar resultados | `age,gender`, `country`, `publisher_platform` |
| `--action-breakdowns` | Segmentar acoes | `action_type`, `action_device` |
| `--action-report-time` | Quando acoes contam | `impression`, `conversion`, `mixed` |
| `--action-attribution-windows` | Janela de atribuicao | `1d_view,7d_click`, `28d_click`, `dda` |
| `--level` | Nivel de agregacao | `account`, `campaign`, `adset`, `ad` |
| `--filtering` | Filtrar resultados (JSON) | `'[{"field":"spend","operator":"GREATER_THAN","value":50}]'` |
| `--sort` | Ordenar | `spend_descending`, `impressions_ascending` |
| `--default-summary` | Incluir totais | (flag, sem valor) |
| `--locale` | Idioma dos resultados | `pt_BR`, `en_US` |
| `--limit` | Limite por pagina | `25` (default) |
| `--offset` | Pular N resultados | `50` |
| `--since` / `--until` | Paginacao temporal | `2026-01-01` |
| `--use-account-attribution` | Usar atribuicao da conta | (flag) |

### Targeting (targeting.py)

| Subcomando | Exemplo |
|---|---|
| `interests` | `targeting.py interests --q "design grafico"` |
| `interest-suggestions` | `targeting.py interest-suggestions --ids 123,456` |
| `behaviors` | `targeting.py behaviors --locale pt_BR` |
| `demographics` | `targeting.py demographics` |
| `geolocations` | `targeting.py geolocations --q "Porto Alegre" --types city` |
| `validate` | `targeting.py validate --account act_123 --spec '{...}'` |
| `reach` | `targeting.py reach --account act_123 --spec '{...}'` |
| `delivery` | `targeting.py delivery --account act_123 --spec '{...}' --daily-budget 5000` |
| `describe` | `targeting.py describe --account act_123 --spec '{...}'` |

### Criacao (create.py)

| Subcomando | Exemplo |
|---|---|
| `campaign` | `create.py campaign --account act_123 --name "LEADS-Teste" --objective OUTCOME_LEADS` |
| `adset` | `create.py adset --account act_123 --name "Publico-Frio" --campaign 123 --optimization-goal LINK_CLICKS --targeting '{...}' --daily-budget 5000` |
| `ad` | `create.py ad --account act_123 --name "Carrossel-V1" --adset 123 --creative '{"creative_id":"456"}' --degrees-of-freedom-spec '{...}'` |
| `creative` | `create.py creative --account act_123 --name "Criativo-V1" --instagram-user-id 123 --object-story-spec '{...}' --url-tags "utm_source=facebook&utm_medium=cpc"` |
| `image` | `create.py image --account act_123 --url "https://exemplo.com/imagem.jpg"` |
| `video` | `create.py video --account act_123 --url "https://exemplo.com/video.mp4"` |
| `custom-audience` | `create.py custom-audience --account act_123 --name "Compradores-2026"` |
| `lookalike` | `create.py lookalike --account act_123 --name "LAL-Compradores" --source 123 --spec '{"country":"BR","ratio":0.01}'` |

**IMPORTANTE:** Todas as criacoes sao feitas com status PAUSED. Revisar antes de ativar.

### Edicao (update.py)

| Subcomando | Exemplo |
|---|---|
| `campaign` | `update.py campaign --id 123 --status ACTIVE --daily-budget 10000` |
| `adset` | `update.py adset --id 123 --targeting '{...}' --daily-budget 5000` |
| `ad` | `update.py ad --id 123 --status PAUSED` |
| `audience-users` | `update.py audience-users --id 123 --schema EMAIL --data '[["hash1"]]' --action add` |

### Exclusao (delete.py)

| Subcomando | Exemplo |
|---|---|
| `object` | `delete.py object --id 123` |
| `audience` | `delete.py audience --id 123` |

### Avancado (advanced.py) -- NOVIDADES

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `swap-url-tags` | Troca url_tags de um ad existente | `advanced.py swap-url-tags --ad 123 --url-tags "utm_source=facebook&utm_medium=cpc&utm_campaign=leads"` |
| `duplicate-ad` | Duplica ad com novos url_tags | `advanced.py duplicate-ad --id 123 --adset 456 --url-tags "utm_source=facebook"` |
| `duplicate-adset` | Duplica ad set | `advanced.py duplicate-adset --id 123 --campaign 456` |
| `duplicate-campaign` | Duplica campanha inteira | `advanced.py duplicate-campaign --id 123 --deep` |

O `swap-url-tags` resolve o problema de nao poder editar url_tags em criativos existentes: cria um criativo novo identico com os url_tags corretos e troca no ad.

O `--deep` no `duplicate-campaign` duplica tambem todos os ad sets e ads da campanha.

### Datasets / Pixels (dataset.py)

Operações sobre AdsPixel (signal diagnostics): listar, detalhes, criar, stats de eventos, share/unshare e diagnóstico de saúde.

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `list` | Lista pixels da conta | `dataset.py list --account act_123` |
| `get` | Detalhes de um pixel | `dataset.py get --id 456` |
| `create` | ⚠️ Cria pixel novo (1 por conta) | `dataset.py create --account act_123 --name "Pixel Site"` |
| `stats` | Stats agregadas de eventos | `dataset.py stats --id 456 --aggregation event --start 2026-04-01 --end 2026-04-30` |
| `events` | Resumo de eventos únicos no período | `dataset.py events --id 456 --start 2026-04-23` |
| `share` | ⚠️ Compartilha pixel com outra conta | `dataset.py share --id 456 --account act_789` |
| `unshare` | ⚠️ Remove compartilhamento | `dataset.py unshare --id 456 --account act_789` |
| `shared-accounts` | Lista contas com acesso ao pixel | `dataset.py shared-accounts --id 456` |
| `diagnostics` | Health check completo do pixel | `dataset.py diagnostics --id 456` |

Aggregations suportadas em `stats`: `event`, `host`, `url`, `device_os`, `device_type`, `pixel_fire`, `browser_total_counts_unique_users`, `event_total_counts`.

O `diagnostics` combina vários endpoints num resumo amigável: status do pixel, último fire, eventos dos últimos 7 dias, automatic matching, CAPI, e classifica saúde como `HEALTHY` / `DEGRADED` / `UNHEALTHY` listando os problemas encontrados.

**Permissões:** o token precisa ter `ads_management` ou `ads_read` no scope, e a ad account precisa ter o pixel vinculado e estar com o app autorizado.

---

## Aprendizados (memória persistente)

**Arquivo:** `aprendizados.md` (na raiz da skill, `.claude/skills/meta-ads/aprendizados.md`)

O Claude DEVE:

1. **Ler `aprendizados.md` no início de QUALQUER operação de criação** (campanha, ad set, criativo, ad). Aplicar todas as regras listadas.

2. **Quando o usuário corrigir algo** (ex: "faltou o CTA", "tinha que ser carrossel", "botão errado"), o Claude DEVE perguntar:
   "Quer que eu registre isso nos aprendizados pra não esquecer nas próximas vezes?"

3. **Quando o usuário pedir explicitamente** ("lembra disso", "registra isso", "anota pra próxima"), registrar imediatamente.

4. **Formato de cada entrada** no aprendizados.md:
   ```markdown
   ### {DATA} — {título curto}
   **Regra:** {o que fazer sempre/nunca}
   **Contexto:** {o que aconteceu pra gerar esse aprendizado}
   ```

5. **Não duplicar** — antes de adicionar, verificar se já existe regra similar.

Exemplo de aprendizados.md:
```markdown
# Aprendizados — Meta Ads ClaudePRO

### 2026-04-03 — Sempre incluir CTA no criativo
**Regra:** Ao criar criativos (create.py creative), SEMPRE incluir call_to_action_type. Padrão: LEARN_MORE pra tráfego, SIGN_UP pra leads, SHOP_NOW pra vendas.
**Contexto:** Criou carrossel sem botão de CTA. Usuário teve que corrigir manualmente.

### 2026-04-03 — Carrossel Instagram: multi_share_end_card=false
**Regra:** Em campanhas de visita ao perfil Instagram, SEMPRE usar multi_share_end_card=false e multi_share_optimized=false.
**Contexto:** Cartão "Ver mais" sem URL quebrou o anúncio em 10 posicionamentos.
```

## Registro no historico (apos acoes de escrita)

Depois de qualquer acao que modifica a conta (create, update, delete, pause, activate),
o Claude DEVE perguntar:

> "Quer que eu registre essa acao no historico de otimizacoes?"

Se o usuario confirmar, registrar num arquivo `historico.md` na raiz do workspace com:
- Cliente, o que foi feito (com IDs), motivo, hipotese e metricas antes.

Essa regra garante que o historico de otimizacoes nao se perde.

## Regras de seguranca

O Claude DEVE seguir estas regras ao executar operacoes:

1. **Criar sempre PAUSED** -- nunca criar objetos com status ACTIVE diretamente
2. **Confirmar antes de deletar** -- perguntar ao usuario antes de executar delete
3. **Confirmar antes de ativar** -- perguntar antes de mudar status para ACTIVE
4. **Ativar TODOS os niveis** -- ao ativar uma campanha, SEMPRE ativar tambem todos os ad sets e ads dentro dela. Nunca ativar so a campanha e esquecer os niveis abaixo. Ordem: campaign → adsets → ads
5. **Respeitar rate limits** -- o SDK ja inclui delays entre operacoes de escrita (1s). Se receber erro de rate limit (codigos 17, 32, 80004), aguardar 60 segundos antes de tentar novamente
6. **Orcamento com cuidado** -- ao alterar daily_budget ou lifetime_budget, confirmar o valor com o usuario. Valores sao em centavos (5000 = R$50,00)
7. **Nunca hardcodar tokens** -- sempre usar a env var META_ADS_TOKEN
8. **Nunca assumir origem de dados** -- ao mostrar insights no nivel da conta, SEMPRE quebrar por campanha antes de atribuir resultados a uma campanha especifica. Nunca dizer "esse gasto e da campanha X" sem ter confirmado com insights por campanha

## Padroes de campanha (CRITICO)

**Arquivo:** `references/padroes-campanha.md`

O Claude DEVE ler este arquivo ANTES de criar qualquer campanha. Ele contem regras
aprendidas por tipo de campanha que evitam erros comuns (ex: carrossel sem preview,
ads bloqueados em posicionamentos, etc).

Se o tipo de campanha nao estiver documentado, o Claude DEVE primeiro buscar uma
campanha similar ja existente na conta e usar como template (ver fluxo abaixo).

## Fluxos comuns

### Criar campanha completa

**Passo 0 — Diagnostico (OBRIGATORIO antes de criar)**
1. Ler `references/padroes-campanha.md` para o tipo de campanha desejado
2. Buscar campanhas similares ja existentes na conta:
   ```
   read.py campaigns --account act_XXX --status ACTIVE
   read.py ads-by-campaign --campaign XXX
   read.py creative --id XXX
   ```
3. Extrair padroes: destination_type, promoted_object, optimization_goal,
   instagram_user_id, multi_share_end_card, degrees_of_freedom_spec, etc.
4. Usar como base para a nova campanha

**Passo 1-5 — Criacao**
1. `create.py campaign` -- cria campanha PAUSED
2. `create.py adset` -- cria ad set PAUSED com targeting
3. `create.py image` ou `create.py video` -- sobe midia
4. `create.py creative` -- cria criativo com url_tags e instagram_user_id
5. `create.py ad` -- cria ad PAUSED com degrees_of_freedom_spec

**Passo 6 — Validacao (OBRIGATORIO apos criar)**
1. Ler o ad criado: `read.py ad --id XXX`
2. Checar preview: `read.py preview --creative XXX --format all`
3. Se houver problemas, corrigir ANTES de reportar sucesso

**Passo 7 — Ativacao**
Ativar TODOS os niveis (campanha + ad sets + ads):
   - `update.py campaign --id XXX --status ACTIVE`
   - `update.py adset --id XXX --status ACTIVE`
   - `update.py ad --id XXX --status ACTIVE`

### Corrigir url_tags de ads existentes

**IMPORTANTE:** Criativos na Meta sao imutaveis. Nao da pra editar url_tags, URL de destino, imagem ou texto de um criativo existente via API. Isso vale especialmente pra criativos baseados em posts organicos (effective_object_story_id) -- a URL vem do post original e nao pode ser alterada.

**O fluxo correto e duplicar o ad com criativo novo:**
1. `read.py ads-by-campaign --campaign XXX` -- listar ads
2. `read.py creatives-by-ad --ad XXX` -- ver criativo atual e url_tags
3. Criar novo criativo usando o `object_story_id` do original + url_tags corretos
4. Criar novo ad PAUSED no mesmo ad set com o criativo novo
5. Ativar o novo ad
6. Pausar o ad antigo

Pra criativos de post organico, usar a API direta:
```bash
# Criar criativo com url_tags corretos reusando o post original
POST act_XXX/adcreatives
  name: "nome [url_tags_fix]"
  object_story_id: "PAGE_ID_POST_ID"  (do effective_object_story_id do criativo antigo)
  url_tags: "utm_source=facebook&utm_medium=cpc&utm_campaign=NOME_CAMPANHA"

# Criar novo ad PAUSED
POST act_XXX/ads
  name: "nome [url_tags_fix]"
  adset_id: MESMO_ADSET
  creative: {"creative_id": "NOVO_ID"}
  status: PAUSED
  tracking_specs: (copiar do ad original)

# Ativar novo, pausar antigo
POST novo_ad_id  status=ACTIVE
POST antigo_ad_id  status=PAUSED
```

### Duplicar campanha para teste A/B
1. `advanced.py duplicate-campaign --id XXX --deep` -- copia tudo
2. `update.py adset --id NOVO_ADSET --targeting '{...}'` -- alterar targeting
3. `update.py campaign --id NOVA_CAMPANHA --name "Teste B"` -- renomear
4. Ativar quando pronto

### Puxar relatorio de performance
1. `insights.py campaign --id XXX --date-preset last_30d --breakdowns age,gender`
2. Ou para relatorio pesado: `insights.py async --id act_XXX --date-preset maximum --level ad`
