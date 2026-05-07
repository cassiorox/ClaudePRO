# Padroes de Campanha — Meta Ads ClaudePRO

Regras aprendidas por tipo de campanha. O Claude DEVE consultar este arquivo
ANTES de criar qualquer campanha nova e aplicar os padroes correspondentes.

Se o tipo de campanha nao estiver aqui, o Claude DEVE primeiro buscar uma
campanha similar ja existente na conta (via `read.py campaigns` + `read.py ads-by-campaign`
+ `read.py creative`) e usar como template.

---

## Fluxo obrigatorio antes de criar

### 1. Diagnostico (ler antes de criar)

Antes de criar qualquer campanha, o Claude DEVE:

1. **Ler campanhas existentes** da conta com objetivo similar
   ```
   read.py campaigns --account act_XXX --status ACTIVE
   ```
2. **Inspecionar uma campanha similar** (adset + creative + ad)
   ```
   read.py adsets-by-campaign --campaign XXX
   read.py ads-by-campaign --campaign XXX
   read.py creative --id XXX
   ```
3. **Extrair padroes**: destination_type, promoted_object, optimization_goal,
   instagram_user_id, degrees_of_freedom_spec, multi_share_end_card, etc.
4. **Aplicar ao novo**: usar os mesmos valores como base, ajustando apenas o
   que for diferente (nome, orcamento, criativo, targeting)

Se nao houver campanha similar na conta, seguir os padroes documentados abaixo.

### 2. Validacao pos-criacao

Depois de criar uma campanha completa, o Claude DEVE validar:

1. **Ler o ad criado** e verificar se tem `effective_status` != DISAPPROVED
   ```
   read.py ad --id XXX
   ```
2. **Checar preview** para garantir que renderiza
   ```
   read.py preview --creative XXX --format all
   ```
3. Se houver problemas, corrigir ANTES de reportar sucesso ao usuario

---

## Visita ao Perfil Instagram (Instagram Profile Visit)

Campanha para direcionar trafego ao perfil do Instagram.

### Configuracao

| Nivel | Campo | Valor |
|---|---|---|
| **Campaign** | objective | `OUTCOME_TRAFFIC` |
| **Campaign** | special_ad_categories | `[]` (vazio) |
| **Ad Set** | optimization_goal | `VISIT_INSTAGRAM_PROFILE` |
| **Ad Set** | destination_type | `INSTAGRAM_PROFILE` |
| **Ad Set** | billing_event | `IMPRESSIONS` |
| **Ad Set** | promoted_object | `{"instagram_profile_id": "ID_DO_INSTAGRAM"}` |
| **Creative** | instagram_user_id | ID da conta Instagram (OBRIGATORIO) |

### Regras criticas

- **multi_share_end_card: false** — o cartao final "Ver mais" exige uma URL.
  Como nao ha site de destino (o destino e o perfil), esse cartao quebra o
  anuncio em 10+ posicionamentos. SEMPRE desligar.

- **multi_share_optimized: false** — manter a ordem dos slides fixa. O Meta
  reordena os slides se estiver true, o que nao faz sentido pra carrosseis
  com narrativa sequencial.

- **instagram_user_id OBRIGATORIO** — sem isso o ad nao publica no Instagram.
  Passar no nivel do criativo via `create.py creative --instagram-user-id XXX`.

- **degrees_of_freedom_spec** — desligar opcoes de formato que distorcem o
  carrossel (blocos de colecao, midia unica, carousel-to-video):
  ```json
  {
    "creative_features_spec": {
      "carousel_to_video": {"enroll_status": "OPT_OUT"},
      "image_touchups": {"enroll_status": "OPT_OUT"},
      "standard_enhancements": {"enroll_status": "OPT_OUT"}
    }
  }
  ```
  Passar via `create.py ad --degrees-of-freedom-spec '{...}'`.

### Exemplo completo

```bash
# 1. Campanha
create.py campaign --account act_XXX --name "visitas-ig-NOME" \
  --objective OUTCOME_TRAFFIC --daily-budget 1000

# 2. Ad Set
create.py adset --account act_XXX --name "advantage-plus-brasil" \
  --campaign CAMP_ID --optimization-goal VISIT_INSTAGRAM_PROFILE \
  --billing-event IMPRESSIONS --destination-type INSTAGRAM_PROFILE \
  --promoted-object '{"instagram_profile_id":"IG_ID"}' \
  --targeting '{"age_min":18,"age_max":65,"geo_locations":{"countries":["BR"]},"targeting_automation":{"advantage_audience":1}}' \
  --daily-budget 1000

# 3. Creative (carrossel)
create.py creative --account act_XXX --name "carrossel-NOME" \
  --instagram-user-id IG_ID \
  --object-story-spec '{"page_id":"PAGE_ID","link_data":{"message":"LEGENDA","child_attachments":[{"image_hash":"HASH","name":"Slide 01"}],"multi_share_end_card":false,"multi_share_optimized":false}}' \
  --url-tags "utm_source=facebook&utm_medium=cpc&utm_campaign=NOME"

# 4. Ad (com format options desligadas)
create.py ad --account act_XXX --name "carrossel-NOME" \
  --adset ADSET_ID --creative '{"creative_id":"CREATIVE_ID"}' \
  --degrees-of-freedom-spec '{"creative_features_spec":{"carousel_to_video":{"enroll_status":"OPT_OUT"},"image_touchups":{"enroll_status":"OPT_OUT"},"standard_enhancements":{"enroll_status":"OPT_OUT"}}}'
```

---

## Trafego para Site (Website Traffic)

> TODO: documentar quando tivermos padroes validados

## Geracao de Leads (Lead Generation)

> TODO: documentar quando tivermos padroes validados

## Conversoes/Vendas (Sales)

> TODO: documentar quando tivermos padroes validados

---

## Como adicionar novos padroes

Quando um novo tipo de campanha for criado e validado (sem alertas, preview OK,
entregando normalmente), documentar aqui seguindo o formato:

1. Nome e descricao do tipo
2. Tabela de configuracao por nivel (campaign, adset, creative, ad)
3. Regras criticas (o que quebra se nao fizer)
4. Exemplo completo com comandos
