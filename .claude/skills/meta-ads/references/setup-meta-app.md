# Setup do App Meta — passo a passo

Guia para criar o app no Meta Developer Dashboard, gerar o token de acesso e
resolver os erros mais comuns. Ler antes de conduzir o setup da skill.

O objetivo final é preencher duas linhas no arquivo
`.claude/skills/meta-ads/.env`:

```
META_ADS_TOKEN="..."
META_APP_ID="..."
```

---

## Pré-requisitos

Antes de abrir o Developer Dashboard, o usuário precisa ter:

- Uma conta pessoal do Facebook (o app fica vinculado a ela).
- Um **Business Manager** (business.facebook.com) com a conta de anúncios dentro.
- Acesso de administrador ao Business Manager e à conta de anúncios.
- A página do Facebook (e o Instagram, se for anunciar lá) dentro desse mesmo
  Business Manager.

Se a conta de anúncios estiver solta na conta pessoal, fora de um Business
Manager, vale resolver isso primeiro — muita coisa da API só funciona com a
conta dentro do Business.

---

## Caminho 1 — Token de usuário do sistema (recomendado)

Esse é o caminho que vale a pena para quem vai usar a skill de verdade. O token
**não expira**, então o setup é feito uma vez e pronto.

### 1.1 Criar o app

1. Ir em https://developers.facebook.com/apps
2. **Criar app**
3. Em "Casos de uso", escolher **Outro** → **Avançar**
4. Tipo de app: **Empresa** (Business) → **Avançar**
5. Dar um nome (ex: "ClaudePRO Ads"), informar email de contato
6. Selecionar o **portfólio empresarial / Business Manager** da agência
7. **Criar app**

### 1.2 Adicionar a Marketing API

1. Dentro do app, ir em **Adicionar produtos** (painel esquerdo)
2. Localizar **Marketing API** → **Configurar**

### 1.3 Copiar o App ID

No topo do painel do app, ou em **Configurações do app → Básico**, está o
**ID do aplicativo**. É um número de 15–16 dígitos. Esse valor vai para
`META_APP_ID` no `.env`.

### 1.4 Criar o usuário do sistema

1. Ir em https://business.facebook.com/settings
2. Menu esquerdo → **Usuários** → **Usuários do sistema**
3. **Adicionar** → nome (ex: "claude-ads") → função **Administrador** → criar

### 1.5 Dar ativos ao usuário do sistema

Ainda na tela do usuário do sistema, clicar em **Adicionar ativos** e conceder,
com **controle total**:

- as **contas de anúncios** que serão gerenciadas
- as **páginas do Facebook** usadas nos anúncios
- as **contas do Instagram**, se for anunciar no Instagram
- os **pixels / datasets**, se for mexer em conversões

Esse passo é o mais esquecido. Sem ele o token é gerado, autentica, e depois
falha com erro de permissão em toda operação.

### 1.6 Gerar o token

1. Na tela do usuário do sistema → **Gerar novo token**
2. Selecionar o **app** criado no passo 1.1
3. Expiração: **Nunca**
4. Marcar as permissões:
   - `ads_management` — criar e editar campanhas
   - `ads_read` — ler campanhas e insights
   - `business_management` — acessar ativos do Business
   - `pages_read_engagement` — ler dados das páginas
   - `pages_manage_ads` — criar dark posts a partir da página
   - `instagram_basic` — se for anunciar no Instagram
   - `read_insights` — métricas orgânicas, se precisar
5. **Gerar token** → **copiar imediatamente**

O token aparece uma única vez. Se a janela fechar sem copiar, é só gerar outro.

### 1.7 Preencher o `.env`

Colar o token em `META_ADS_TOKEN` e o App ID em `META_APP_ID`, e rodar:

```bash
python3 .claude/skills/meta-ads/scripts/setup.py
```

---

## Caminho 2 — Token pelo Graph API Explorer (rápido, expira)

Serve para testar em cinco minutos. O token dura ~1 hora, ou ~60 dias se
estendido. Para uso contínuo, migrar depois para o Caminho 1.

1. Criar o app (passos 1.1 a 1.3 acima)
2. Ir em https://developers.facebook.com/tools/explorer
3. No canto direito, em **Aplicativo Meta**, selecionar o app criado
4. Em **Permissões**, adicionar: `ads_management`, `ads_read`,
   `business_management`, `pages_read_engagement`, `pages_manage_ads`
5. **Gerar token de acesso** → autorizar na janela do Facebook
6. Copiar o token

### Estender para 60 dias

1. Ir em https://developers.facebook.com/tools/debug/accesstoken
2. Colar o token → **Depurar**
3. Clicar em **Estender token de acesso** no rodapé
4. Copiar o token longo que aparece

Quando esse token vencer, o sintoma é erro 190 em qualquer comando — é só gerar
outro pelo mesmo caminho.

---

## Modo Live

Para criar **dark posts** e criativos via API, o app precisa estar em modo
**Live**, não Development.

No painel do app, o seletor fica no topo da página. Se estiver em
"Desenvolvimento", alternar para "Ao vivo". Pode ser exigido informar a URL de
uma política de privacidade nas **Configurações → Básico** antes de liberar a
troca.

Leitura de dados e insights funciona em modo Development. É a escrita de
criativos que trava.

---

## Verificar se deu certo

```bash
python3 .claude/skills/meta-ads/scripts/setup.py
```

O esperado é `TUDO PRONTO!` e a lista de contas de anúncio acessíveis. Se as
contas aparecerem, a permissão está correta.

---

## Erros comuns

**`(#200) Provide valid app ID` / erro de permissão em toda chamada**
O usuário do sistema não recebeu os ativos. Voltar ao passo 1.5 e conceder
controle total sobre a conta de anúncios e a página.

**`Error validating access token: Session has expired` (código 190)**
Token expirado. Típico do Caminho 2. Gerar outro, ou migrar para o token de
usuário do sistema.

**`(#10) Application does not have permission for this action`**
Falta uma permissão na geração do token. Gerar de novo marcando
`ads_management` e `pages_manage_ads`.

**`Your app is in development mode`**
Alternar o app para modo Live (seção acima).

**`(#100) Invalid parameter` ao criar criativo com página**
A página não está vinculada ao app ou ao usuário do sistema. Adicionar a página
como ativo no Business Manager e conceder acesso.

**Nenhuma conta de anúncio listada no `setup.py`**
O token foi gerado por um usuário sem acesso às contas, ou o usuário do sistema
não recebeu os ativos. Conferir em business.facebook.com → Contas de anúncios →
aba Pessoas.

**`Unsupported get request` ao ler um objeto**
Geralmente é ID errado (ex: passar `123456` onde a API espera `act_123456`), ou
o objeto pertence a uma conta fora do token.

---

## Segurança do token

O token dá acesso de escrita às contas de anúncios — trate como senha.

- Fica só no `.env` da skill, que já está no `.gitignore`.
- Nunca colar em prompt, commit, print de tela ou mensagem de suporte.
- Se vazar: Business Manager → Usuários do sistema → **Revogar token**, e gerar
  um novo.
