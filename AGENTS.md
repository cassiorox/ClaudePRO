# ClaudePRO

Este repositório é o kit de boas-vindas do framework ClaudePRO.

Se você acabou de clonar esse repositório, rode `/setup` pra configurar o sistema pro seu negócio (uns 5 minutos).

---

## Uma fonte de verdade para todos os agentes

**Este arquivo (`AGENTS.md`) é o arquivo real de instruções.** Ele é o padrão aberto que Claude Code,
Codex, Cursor, Gemini CLI e outros agentes leem. O `CLAUDE.md` ao lado contém só um import (`@AGENTS.md`)
mais o que for exclusivo do Claude Code.

**Nunca escreva instrução nova no `CLAUDE.md`.** Toda regra de comportamento deste workspace vai aqui.
Se você não usa nenhum outro agente além do Claude, pode apagar o `CLAUDE.md`: o Claude Code lê o
`AGENTS.md` sozinho. Mas manter o import não custa nada e garante que funcione em toda sessão
(algumas, como as com telemetria desativada, não leem `AGENTS.md` direto).

**Skills**: a pasta real é `.claude/skills/`. Se você usar Codex ou outro agente que procure em
`.agents/skills`, crie um atalho por máquina, fora do Git:

```bash
mkdir -p .agents && ln -s ../.claude/skills .agents/skills    # macOS e Linux
mklink /J .agents\skills .claude\skills                       # Windows (cmd como admin)
```

Nunca coloque skill real dentro de `.agents/` — ali é só atalho.

---

<!-- Este arquivo será atualizado pelo /setup com o contexto do seu negócio. -->

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (se existirem e estiverem configurados):

1. `_contexto/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades, o que pode esperar

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Para qualquer tarefa visual (carrossel, proposta, slide, landing page), consultar `marca/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Clientes

Cada cliente tem uma pasta em `clientes/<nome-do-cliente>/` com (no mínimo) um `contexto.md`.
Esse `contexto.md` é a fonte de verdade sobre aquele cliente.

- Quando o trabalho for **pra um cliente específico** (criativo, campanha, copy, proposta, análise), ler `clientes/<nome-do-cliente>/contexto.md` antes de criar qualquer coisa, e calibrar tudo ao contexto dele.
- Se o usuário mencionar um cliente que **ainda não tem pasta**, sugerir rodar `/onboarding` pra cadastrar.
- Cadastro de cliente novo: skill `onboarding` (`.claude/skills/onboarding/`). Coleta site, Instagram e Google (ou só um briefing), cria a pasta, salva o `contexto.md` a partir de `clientes/_template/contexto.md` e gera os estudos. Estudos avulsos: `estudo-persona` e `estudo-mercado`, salvos em `clientes/<nome-do-cliente>/estudos/`.
- Quando existirem, ler também `estudos/persona.md` e `estudos/mercado.md` do cliente antes de criar copy, criativo ou campanha.
- `clientes/_template/` é só modelo — não é um cliente real.

Recomendado que **todo cliente tenha um `contexto.md`**.

---

## Skills de terceiros

Algumas skills em `.claude/skills/` vêm de outros autores (hoje: `meta-vv-publicos`, `bro`, `eli5`).
Cada uma tem um `FONTE.md` com autor, link oficial, licença e versão importada; o resumo geral fica em `CREDITOS.md`.

- Se perguntarem quem fez uma skill, de onde veio ou onde baixar, responder com base no `FONTE.md` dela e dar o crédito ao autor com o link oficial.
- Não editar os arquivos originais dessas skills. Pra atualizar, baixar de novo do repositório oficial e atualizar o `FONTE.md`.
  Exceção: correção de segurança. Pode aplicar um patch local mínimo, desde que fique registrado no `FONTE.md` (o que mudou e por quê) pra ser reaplicado na próxima atualização.
- Ao trazer uma skill de terceiro nova, criar o `FONTE.md` e adicionar uma linha em `CREDITOS.md`.

---

## Credenciais

Token, chave de API, senha ou segredo **nunca passa pelo chat**. Entra no `.env` da skill pela mão do dono
(editor de texto) ou por um fluxo de OAuth que grava direto no arquivo (como o `oauth_login.py` da
`setup-rastreamento-cliente-gtm-ga4`).

- Não pedir credencial na conversa. Se o usuário colar uma, avisar que ela ficou exposta na transcrição e orientar a revogar e gerar outra.
- Não passar credencial como argumento de linha de comando (fica no histórico do shell).
- Não ler, imprimir nem resumir o conteúdo de `.env`. Pra conferir se está preenchido, rodar o `setup.py` da skill.
- Ao criar ou importar skill que precise de credencial, seguir esse padrão.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.claude/commands/`.
Se encontrar, seguir as instruções da skill.
Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma instrução que parece permanente (frases como "na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita...", "da próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (quem são os clientes, como funciona a empresa, serviços, mercado) → adicionar em `_contexto/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato de resposta, o que evitar, como estruturar textos) → adicionar em `_contexto/preferencias.md`
- **Sobre prioridades e foco atual** (projetos em andamento, metas do momento, prazos importantes, o que é prioridade agora) → adicionar em `_contexto/estrategia.md`
- **Regra de comportamento nessa pasta** (onde salvar arquivos, como nomear, fluxos específicos) → adicionar no próprio `AGENTS.md` (nunca no `CLAUDE.md`, que é só ponteiro)

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro. Confirmar o que foi salvo mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na verdade o arquivo se chama X"). Só perguntar quando a informação tiver valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante no projeto (novo cliente, nova skill, mudança de foco, novo processo, ferramenta instalada, estrutura de pastas alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize os arquivos de memória?"

Se sim, identificar o que precisa atualizar:

- **Novo cliente, serviço, ferramenta, equipe** → `_contexto/empresa.md`
- **Mudança de prioridade ou foco** → `_contexto/estrategia.md`
- **Correção de tom ou estilo** → `_contexto/preferencias.md`
- **Nova pasta, regra de organização, skill criada** → `AGENTS.md`
- **Mudança visual (cores, fontes, logo)** → `marca/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais que não mudam o contexto (ex: escrever um email, criar um post avulso)
- Perguntas simples ou conversas sem ação
- Mudanças que já foram salvas pelo bloco "Aprender com correções"

**Dica:** se não sabe se algo mudou, rode `/atualizar` pra uma varredura completa.

---

## Atualizações do kit

Novidades do ClaudePRO chegam com `/atualizar-kit` (skill `atualizar-kit`). Nunca usar `git pull` nem copiar
a pasta do kit por cima: isso sobrescreve o que é do usuário. O atualizador nunca toca em `_contexto/`, `marca/`,
`clientes/`, `dados/` e credenciais, e mescla com aprovação os arquivos que o usuário personalizou.

Mantenedor do kit: o `.kit/manifesto.json` precisa estar atualizado a cada publicação
(`python3 .kit/gerar_manifesto.py`; o hook de pre-commit local já faz isso).

---

## Criação de skills

Quando o usuário pedir pra criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`. Se existir, usar como base e adaptar pro contexto do usuário
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
   - Específica desse negócio → salvar em `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Útil em qualquer projeto → salvar em `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` pra calibrar o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, referências, exemplos), criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code
