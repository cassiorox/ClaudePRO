# Playbook: servidor MCP oficial do Google Ads

Guia completo pra ligar o Claude Code direto na sua conta do Google Ads usando o servidor MCP oficial do
Google, rodando na sua máquina. Do primeiro prompt até a primeira consulta funcionando.

Material do **Subido PRO**. Testado e validado em 20/09/2026: macOS 27.0, Python 3.14.7, biblioteca
`google-ads` 32.0.0, servidor `google-ads-mcp` instalado do GitHub oficial.

Documentação oficial: https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server

---

## 1. O que é isso e por que importa

MCP (Model Context Protocol) é o padrão que deixa o Claude conversar com ferramentas externas. Um "servidor
MCP" é um programinha que expõe funções (buscar campanhas, listar contas) e o Claude decide sozinho quando
chamar cada uma.

O servidor MCP do Google Ads é **oficial do Google**, open source, e roda **local**: ele sobe como um
processo filho do Claude Code, conversa por entrada e saída padrão (`stdio`), e não abre nenhuma porta de
rede. Seus dados e suas credenciais não passam por servidor de terceiro.

Três coisas importantes antes de começar:

1. **É somente leitura.** O servidor consulta campanhas, métricas e estrutura de conta. Ele não pausa
   campanha, não cria anúncio, não mexe em lance. Escrita continua sendo pela skill `google-ads`.
2. **Ele não substitui a skill `google-ads`.** O MCP é bom pra pergunta solta ("quanto gastei essa semana
   na conta X"). A skill é boa pra rotina repetível (criar campanha, subir criativo, relatório padrão).
3. **Não é plug and play.** A documentação oficial tem duas divergências em relação ao que o servidor
   realmente faz hoje. As duas estão resolvidas aqui embaixo.

> **Antes de investir tempo aqui:** se você só quer ler dados e já configurou a skill `google-ads`, a skill
> já faz tudo o que o MCP faz e mais. O MCP vale como exercício de "como um servidor MCP se conecta" e pra
> quem gosta de perguntar em linguagem solta sem pensar em script.

---

## 2. O primeiro prompt

Abra o Claude Code na pasta do projeto e cole:

```
Quero rodar o servidor MCP oficial do Google Ads local, conectado ao Claude Code.
Já tenho (ou vou gerar) as credenciais da API do Google Ads.

Faça na ordem:
1. Confira se tenho Python 3.12+ e pipx instalados.
2. Instale o servidor a partir do GitHub oficial (googleads/google-ads-mcp),
   não a versão do PyPI.
3. Monte o arquivo de credenciais no formato Application Default Credentials
   a partir do meu client_id, client_secret e refresh_token.
4. Registre o servidor no Claude Code em escopo local.
5. Teste de ponta a ponta listando minhas contas acessíveis.

Antes de cada passo me diga o que vai fazer. Se algo falhar, me mostre o erro
real em vez de tentar outro caminho por conta própria.
```

Esse prompt funciona porque dá a ordem, fixa as duas decisões que a documentação erra (GitHub em vez de
PyPI, credenciais em formato ADC) e proíbe o Claude de improvisar em cima de um erro.

---

## 3. Pré-requisitos

| Item | Como conferir | Como resolver |
|---|---|---|
| Python 3.12 ou maior | `python3 --version` | Instalar pelo site oficial ou `brew install python` |
| pipx | `pipx --version` | macOS: `brew install pipx && pipx ensurepath`. Linux: `sudo apt install pipx && pipx ensurepath`. Windows: `pip install pipx && pipx ensurepath` |
| Claude Code | `claude --version` | claude.com/code |
| Acesso de saída HTTPS | | Liberar `googleads.googleapis.com` e PyPI na rede |

Depois de rodar `pipx ensurepath`, **feche e abra o terminal**. O `PATH` novo não vale na sessão que já
estava aberta.

---

## 4. As credenciais

> **Mudou em setembro de 2026.** O Google aposentou os developer tokens em 09/09/2026. Quem manda agora no
> nível de acesso é o **projeto do Google Cloud** que gerou as credenciais OAuth, não mais o token. Você
> também **não precisa mais de conta MCC** para usar a API. Quem já tinha integração rodando não precisa
> mexer em nada: o token continua sendo aceito no header, só que ignorado.
> Fonte: https://developers.google.com/google-ads/api/docs/api-policy/developer-token

São três valores, mais um opcional:

1. **Client ID** (OAuth2, tipo Desktop) — Google Cloud Console, projeto com a Google Ads API ativada.
2. **Client secret** — mesma tela do Client ID.
3. **Refresh token** — gerado pelo fluxo OAuth uma única vez.
4. **Login customer ID** (opcional) — só preencha se for consultar contas através de um MCC.
   **Só dígitos, sem hífen** (`1234567890`, não `123-456-7890`).

O ID da conta que você vai consultar (customer ID) também é sempre sem hífen.

**Se você já rodou `/google-ads setup`, esses três valores já estão no `.env` da skill.** Pule para a
seção 5.

### Do zero: a sequência completa, em nove passos

Testado de ponta a ponta em 20/09/2026, com projeto novo. Três destes passos não aparecem na documentação
oficial nem nos tutoriais, e são justamente os que quebram tudo: o **2**, o **5** e o **7**.

1. **Criar o projeto** no [Google Cloud Console](https://console.cloud.google.com/).
2. **Entrar no projeto criado.** O seletor de projeto no topo da tela **não muda sozinho** depois de criar.
   Se você seguir direto, vai ativar a API, pedir acesso e criar credenciais tudo no projeto anterior, sem
   nenhum aviso. Confirme o nome no seletor antes de continuar.
3. **Ativar a Google Ads API** no projeto.
4. **Configurar a tela de consentimento** (tipo Externo, nome do app, e-mail de contato).
5. **Publicar o app.** Em *Google Auth Platform > Público-alvo*, botão **Publicar app**. Enquanto o status
   for "Testes", o refresh token **expira em 7 dias** e a integração morre sozinha na semana seguinte.
   Publicar exige uma página inicial e links de termos de uso e privacidade de um domínio seu.
6. **Criar as credenciais OAuth** do tipo **App para computador**. Guarde Client ID e Client secret.
7. **Pedir Explorer** na
   [Google Ads API Overview](https://console.cloud.google.com/google/ads-apis/overview), com o projeto
   certo selecionado. Sem isso o projeto fica em **Test**: a autenticação funciona, e **toda chamada a
   conta de produção falha**.
8. **Gerar o refresh token** pelo fluxo OAuth:
   `python3 .claude/skills/google-ads/scripts/setup.py oauth`
9. **Testar** uma leitura real:
   `python3 .claude/skills/google-ads/scripts/setup.py test`

A ordem importa: **publique o app (5) antes de gerar o token (8)**. O prazo de 7 dias é carimbado no
momento em que o token é emitido, e publicar depois não estende um token que já existe. Se você gerou
antes, gere de novo.

> **Erro 500 na tela de consentimento?** Acontece nos minutos seguintes à publicação do app: o backend do
> consentimento ainda está alcançando a mudança de status. Não é erro de configuração. Espere de 10 a 15
> minutos e repita. Se insistir, confirme em *Público-alvo* se o status ficou mesmo "Em produção".

### Por que esses três passos enganam

O erro acontece num passo e só aparece muito depois, num lugar que não aponta para a causa:

| Passo pulado | Quando você descobre | O que parece ser |
|---|---|---|
| 2, projeto errado | ao pedir acesso ou gerar token | credencial inválida |
| 5, app não publicado | 7 dias depois, do nada | "quebrou sozinho" |
| 7, sem Explorer | na primeira chamada real | problema de permissão na conta |

### O nível de acesso do projeto

Antes de a primeira chamada funcionar numa conta de produção, o projeto Cloud precisa estar em **Explorer**
ou acima. Confira e peça o upgrade na página nova:
[Google Ads API Overview](https://console.cloud.google.com/google/ads-apis/overview). O pedido de Explorer
é revisado automaticamente, em minutos, na maioria dos casos.

Projeto em **Test** chamando conta de produção devolve `CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION` na v25
(`ACTION_NOT_PERMITTED` em versões anteriores).

**Projeto em Free Trial do Cloud, ou com billing suspenso, é rejeitado** no Explorer e no Basic, mesmo com
tudo o resto correto. Ou você migra o projeto para o tier pago, ou remove o billing dele. A Google Ads API
em si não cobra nada.

---

## 5. Instalação do servidor

```bash
pipx install "git+https://github.com/googleads/google-ads-mcp.git"
```

### Por que GitHub e não `pipx install google-ads-mcp`

A versão publicada no PyPI está bem atrasada. Ela usa a API do Google Ads v21 e a API antiga da biblioteca
`mcp`, então na instalação limpa ela quebra assim:

```
ModuleNotFoundError: No module named 'mcp.server.fastmcp'.
This is mcp 2.x, where FastMCP was renamed to MCPServer
```

O que acontece: o pacote pede `mcp>=1.2.0`, o pip instala a 2.x, e o código só funciona na 1.x. Dá pra
remendar com `pipx runpip google-ads-mcp install "mcp<2"`, mas você fica preso numa versão velha do
servidor. A do GitHub usa a API v25 e instala redonda.

Detalhe de versionamento: o `pipx` reporta essa instalação do GitHub como **0.0.1**. O projeto não versiona
direito o pacote, então não se assuste com o número baixo. O que importa é ter instalado do GitHub.

### Conferir a instalação

```bash
google-ads-mcp --help
```

Se der "command not found", o `pipx` instalou certo mas o `PATH` não recarregou. Teste com o caminho
absoluto:

```bash
~/.local/bin/google-ads-mcp --help
```

Se esse funcionar, é só reabrir o terminal (ou `source ~/.zshrc`).

---

## 6. Autenticação: a pegadinha principal

A documentação diz pra passar `GOOGLE_ADS_CLIENT_ID`, `GOOGLE_ADS_CLIENT_SECRET` e
`GOOGLE_ADS_REFRESH_TOKEN` como variáveis de ambiente. **O servidor não lê essas três.** Olhando o código
dele (`ads_mcp/utils.py`), ele chama `google.auth.default()`, ou seja, ele quer **Application Default
Credentials**. Só o login customer ID vem por variável de ambiente.

Sem isso, o servidor sobe e morre com:

```
google.auth.exceptions.DefaultCredentialsError:
Your default credentials were not found.
```

Você tem dois caminhos.

### Caminho A: reaproveitar o refresh token que você já tem (recomendado)

O `google.auth` aceita um arquivo JSON do tipo `authorized_user` apontado pela variável
`GOOGLE_APPLICATION_CREDENTIALS`. É só montar esse arquivo com as credenciais que você já tem:

```json
{
  "type": "authorized_user",
  "client_id": "SEU_CLIENT_ID.apps.googleusercontent.com",
  "client_secret": "SEU_CLIENT_SECRET",
  "refresh_token": "SEU_REFRESH_TOKEN"
}
```

A pasta `mcp/` desta skill tem o `criar-adc.py`, que gera esse arquivo lendo o `.env` da skill e já deixa a
permissão em `600`:

```bash
python3 .claude/skills/google-ads/mcp/criar-adc.py
```

Vantagem: não precisa instalar o `gcloud` e reaproveita o token que a skill `google-ads` já usa.

O `adc.json` gerado tem credencial de verdade dentro. Ele está no `.gitignore` da skill e nunca deve ser
commitado nem compartilhado.

### Caminho B: gcloud

```bash
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/adwords,https://www.googleapis.com/auth/cloud-platform
```

Funciona, mas exige instalar o Google Cloud CLI e refazer o login quando o token expira.

---

## 7. Registrar no Claude Code

Nunca escreva credencial dentro de arquivo de configuração. Use um launcher que lê o `.env` e passa tudo
por ambiente. O `mcp/servidor.sh` desta skill faz exatamente isso: exporta as variáveis `GOOGLE_ADS_*`,
aponta o `GOOGLE_APPLICATION_CREDENTIALS` pro `adc.json` e executa o servidor.

```bash
chmod +x .claude/skills/google-ads/mcp/servidor.sh
claude mcp add google-ads-local --scope local -- /caminho/absoluto/.claude/skills/google-ads/mcp/servidor.sh
```

Use caminho absoluto. O Claude Code pode subir o servidor a partir de outro diretório de trabalho.

### Qual escopo escolher

| Escopo | Onde grava | Quando usar |
|---|---|---|
| `local` | `~/.claude.json`, atrelado a este projeto | Padrão. Vale só pra você, neste projeto. É o certo quando envolve credencial |
| `project` | `.mcp.json`, versionado com o repo | Só quando o servidor não precisa de segredo e todo mundo do time deve ter |
| `user` | Sua configuração global | Quando você quer o servidor em todos os projetos da máquina |

### Conferir

```bash
claude mcp list
```

Você deve ver:

```
google-ads-local: /caminho/.../servidor.sh - ✔ Connected
```

Se estiver como `Failed to connect`, rode o `servidor.sh` direto no terminal: o erro real aparece na tela,
coisa que o Claude Code esconde.

Depois de registrar, **reinicie o Claude Code**. Servidor MCP só carrega na inicialização.

---

## 8. As três ferramentas (e o que a documentação diz errado)

Dentro do Claude Code, `/mcp` mostra o servidor e as ferramentas. São três, todas somente leitura:

### `customers_list_accessible_customers`
Sem argumentos. Devolve os IDs de todas as contas que suas credenciais alcançam. É a primeira a chamar
quando você não sabe o ID.

### `metadata_get_resource_metadata`
Argumento: `resource_name` (por exemplo `campaign`, `ad_group`, `keyword_view`).
Devolve quais campos, métricas e segmentos existem naquele recurso. Serve pro Claude não chutar nome de
campo.

### `search_search`
É a ferramenta principal. Argumentos:

- `customer_id` (obrigatório): 10 dígitos, sem hífen
- `resource` (obrigatório): o recurso, por exemplo `campaign`
- `fields` (obrigatório): lista de campos, por exemplo `["campaign.name", "metrics.cost_micros"]`
- `conditions`: lista de filtros combinados com AND, por exemplo `["segments.date DURING LAST_7_DAYS"]`
- `orderings`: ordenação
- `limit`: máximo de linhas

Atenção: várias documentações dizem que os nomes são `list_accessible_customers`,
`get_resource_metadata` e `search`, e que o `search` recebe uma string GAQL inteira no argumento `query`.
**Na versão atual não é assim.** Os nomes têm prefixo e o `search_search` monta a query a partir de campos
separados. Se o Claude insistir em mandar `query`, mande ele chamar `/mcp` e reler a assinatura real.

Um detalhe de leitura: valores de dinheiro voltam em **micros**. `metrics.cost_micros: 94144455` são
R$ 94,14. Divida por 1.000.000.

---

## 9. Primeiros prompts de uso

Depois de conectado, você fala normal. Exemplos que funcionam bem (troque os IDs pelos seus):

```
Liste as contas do Google Ads que eu tenho acesso pelo MCP.
```

```
Na conta 1234567890, me traga as campanhas ativas dos últimos 7 dias com
custo, cliques e conversões. Converta os valores de micros pra reais e
ordene por gasto.
```

```
Na conta 1234567890, quais termos de busca gastaram mais de R$ 50 nos
últimos 30 dias sem gerar conversão? Sugira negativas.
```

```
Compare o CPA das campanhas de Search da conta 1234567890 entre os últimos
7 dias e os 7 anteriores, e me diga onde piorou.
```

Duas manias que valem a pena:

- **Sempre diga o ID da conta.** Com várias contas acessíveis, sem o ID o Claude vai listar tudo e gastar
  contexto à toa.
- **Peça o recorte de data explícito.** Sem `WHERE segments.date`, a API devolve o período padrão e você
  compara coisas diferentes sem perceber.

---

## 10. Quando usar o MCP e quando usar a skill

| Situação | Use |
|---|---|
| Pergunta solta sobre desempenho | MCP |
| Explorar uma conta que você não conhece | MCP |
| Descobrir que campos existem num recurso | MCP |
| Criar campanha, ad group, RSA | Skill `google-ads` |
| Pausar, alterar orçamento, mexer em lance | Skill `google-ads` |
| Relatório recorrente com formato fixo | Skill própria |
| Auditoria completa de conta | Skill própria |

Regra curta: **ler e explorar, MCP. Escrever e repetir, skill.**

---

## 11. Troubleshooting

| Sintoma | Causa | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'mcp.server.fastmcp'` | Instalou do PyPI (versão velha) e o pip trouxe `mcp` 2.x | Reinstale do GitHub: `pipx install --force "git+https://github.com/googleads/google-ads-mcp.git"` |
| `DefaultCredentialsError` | Falta o ADC | Rode o `criar-adc.py` e confira o `GOOGLE_APPLICATION_CREDENTIALS` |
| `command not found: google-ads-mcp` | `PATH` sem `~/.local/bin` | `pipx ensurepath` e reabra o terminal |
| `spawn ... ENOENT` | Caminho relativo na configuração | Registre com caminho absoluto |
| Ferramentas não aparecem | Claude Code não foi reiniciado | Feche e abra o Claude Code, depois `/mcp` |
| `PERMISSION_DENIED` ou `USER_PERMISSION_DENIED` | A conta do OAuth não tem acesso ao customer ID, ou falta o login customer ID do MCC | Confira o `GOOGLE_ADS_LOGIN_CUSTOMER_ID` e o acesso da conta no MCC |
| `CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION` (v25) ou `ACTION_NOT_PERMITTED` | O projeto Cloud está em Test e só alcança contas de teste | Peça Explorer na [Google Ads API Overview](https://console.cloud.google.com/google/ads-apis/overview), não na Central de API |
| Pedido de Explorer recusado | Projeto vinculado a billing em Free Trial ou suspenso | Migre pro tier pago ou remova o billing do projeto |
| `DEVELOPER_TOKEN_NOT_APPROVED` | Erro do fluxo antigo, praticamente extinto desde 09/09/2026 | Trate como nível de acesso do projeto Cloud |
| Servidor "Connected" mas toda query falha | Refresh token revogado | Gere outro com `/google-ads setup` e rode o `criar-adc.py` de novo |
| `Acesso bloqueado: o app não concluiu o processo de verificação` / `Erro 403: access_denied` | App externo em status "Testes" e seu e-mail não está na lista de testadores | Adicione-se em *Público-alvo > Usuários de teste*, ou melhor: publique o app |
| `Erro 500` na tela de consentimento do Google | Propagação: o app foi publicado há poucos minutos | Espere de 10 a 15 minutos e repita |
| Funcionava e parou exatamente 7 dias depois | O token foi emitido com o app em status "Testes" | Publique o app e **gere o refresh token de novo** |
| `The customer account can't be accessed because it is not yet enabled or has been deactivated` | A conta do Google Ads em si está desativada | Não é problema de API. Confira a conta no painel do Google Ads |

Pra depurar de verdade, rode o launcher direto no terminal. O servidor manda log pro `stderr` (o `stdout` é
reservado pro protocolo), então o erro aparece na tela.

---

## 12. Manutenção

Atualizar o servidor:

```bash
pipx install --force "git+https://github.com/googleads/google-ads-mcp.git"
```

Depois reinicie o Claude Code. Vale conferir `/mcp` e reler os nomes das ferramentas: esse projeto ainda
muda de assinatura entre versões.

Remover:

```bash
claude mcp remove google-ads-local
pipx uninstall google-ads-mcp
```

---

## 13. E no Meta Ads, é igual?

Não, e o contraste ajuda a entender o porquê da chatice do Google.

O **Meta tem conector oficial dentro do Claude**: você conecta pela tela de conectores, faz login com sua
conta, e pronto. Nenhum app, nenhum projeto, nenhum token manual. Ele também é focado em leitura e
operações guiadas.

A diferença não é capricho de um ou de outro. **A Google Ads API autoriza o projeto, não a pessoa.** O
login com e-mail só responde "quem é você"; o nível de acesso (Explorer, Basic, Standard) está carimbado no
projeto do Google Cloud que emitiu as credenciais. Como o servidor MCP do Google é código aberto que você
mesmo hospeda, ele não vem com projeto nenhum embutido, então o projeto tem que ser seu.

É exatamente por isso que existem conectores pagos de terceiros que prometem "faça login com o Google e
acabou": o projeto aprovado é deles, e você entra de carona. Funciona, custa mensalidade, e seus dados
passam pelo servidor deles.

Resumo das três opções pra quem está começando:

| Caminho | Esforço | Custo | Dados passam por terceiro |
|---|---|---|---|
| Montar seu projeto Cloud (este playbook, ou a skill `google-ads`) | ~40 min, uma vez | Grátis | Não |
| Conector hospedado de terceiro | ~2 min | Mensalidade | Sim |
| Exportar CSV e jogar no chat | Zero | Grátis | Não, mas nada é automático |

Pra Meta Ads, a skill `meta-ads` deste kit continua sendo o caminho quando você precisa **escrever** (criar
campanha, subir criativo, pausar). O conector oficial resolve leitura.
