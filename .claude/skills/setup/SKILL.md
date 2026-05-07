---
name: setup
description: Configura o workspace ClaudePRO pela primeira vez. Faz uma entrevista rapida com o usuario (agencia ou eugencia, perfil de clientes, servicos, tom de voz, foco atual) e preenche os arquivos de contexto em `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`. Use quando o usuario rodar /setup, mencionar "configurar o sistema", "primeira vez", "preencher contexto" ou "configuracao inicial".
---

# /setup — Configuracao inicial do workspace ClaudePRO

Esta skill e executada uma vez, na primeira entrada do usuario no framework. Faz uma entrevista conversacional curta e preenche os arquivos de contexto.

---

## Antes de comecar

1. Cumprimentar e explicar o que vai acontecer:

   > "Beleza! Vou te fazer algumas perguntas rapidas pra configurar o ClaudePRO pro teu negocio. Leva uns 5 minutos. Depois disso, todo trabalho que voce fizer aqui ja vai chegar com contexto."

2. Antes de cada pergunta, fazer **UMA pergunta por vez**, esperar a resposta, e so depois passar pra proxima. Nao despejar lista de perguntas de uma vez.

3. Se o usuario ja tiver respondido algo nas conversas anteriores (ler `_contexto/*.md` antes de comecar), pular essa pergunta.

---

## Bloco 1 — Perfil do negocio

### Pergunta 1: Tipo de operacao

> "Voce e uma **agencia** (tem equipe — gestores, atendimento, criacao) ou uma **eugencia** (gestor de trafego solo atendendo varios clientes)?"

Aceitar variacoes ("sou solo", "trabalho sozinho", "tenho time") e mapear para `agencia` ou `eugencia`.

**Apos a resposta**, ler o template correspondente como referencia interna (sem mostrar pro usuario):
- `agencia` → `templates/perfis/claude-md-agencia.md`
- `eugencia` → `templates/perfis/claude-md-eugencia.md`

### Pergunta 2: Nome

> "Qual o nome [da agencia / que voce usa profissionalmente]?"

### Pergunta 3: Especialidade em trafego

> "Qual o foco principal do teu trabalho? (Meta Ads / Google Ads / ambos / e-commerce / lancamentos / servicos locais / B2B / outro)"

Aceitar combinacoes e descricoes livres.

---

## Bloco 2 — Clientes

### Pergunta 4: Perfil de clientes

> "Que tipo de cliente voce atende? (PMEs locais, e-commerces, infoprodutores, B2B, profissionais liberais, etc)"

### Pergunta 5: Ticket / faixa de investimento

> "Qual a faixa media de investimento mensal em midia que esses clientes rodam? (ate 5k, 5-20k, 20-50k, 50k+)"

Pergunta opcional. Se o usuario nao quiser responder, seguir.

### Pergunta 6: Numero de clientes ativos

> "Quantos clientes voce atende hoje?"

---

## Bloco 3 — Servicos e entregas

### Pergunta 7: Servicos principais

> "Quais sao os 3 servicos principais que voce entrega? (ex: gestao de campanhas Meta, gestao Google Ads, relatorios mensais, criativos, consultoria)"

### Pergunta 8: Equipe (apenas se `agencia`)

> "Quem trabalha com voce? (lista rapida de funcoes — atendimento, gestor de trafego, designer, etc)"

Pular se `eugencia`.

---

## Bloco 4 — Comunicacao

### Pergunta 9: Tom de voz

> "Como voce gosta de se comunicar com clientes e no conteudo? (formal, descontraido, direto, tecnico, didatico, etc)"

### Pergunta 10: O que evitar

> "Tem alguma palavra, estilo ou abordagem que voce **nao** quer ver no que o Claude produzir pra voce? (ex: emojis, gerundio, jargao, frases muito longas)"

---

## Bloco 5 — Foco atual

### Pergunta 11: Prioridade do momento

> "O que e prioridade pra voce nos proximos 30-60 dias? (ex: prospectar mais clientes, melhorar relatorios, padronizar processos, reduzir CPA medio)"

### Pergunta 12: Algum prazo ou projeto importante

> "Tem algum projeto ou prazo importante pra registrar?"

Pergunta opcional.

---

## Salvar respostas

Apos coletar tudo, escrever os arquivos:

### `_contexto/empresa.md`

Substituir o conteudo por:

```markdown
# Contexto da Empresa

**Nome:** {{nome}}
**Negocio:** {{agencia ou eugencia — descrever em 1 linha}}
**O que faz:** {{especialidade em trafego — Meta/Google/etc}}
**Perfil:** {{agencia | eugencia}}
**Atende clientes:** {{perfil de clientes + numero atual}}
**Ticket medio:** {{faixa de investimento, se respondido}}
**Equipe:** {{equipe se agencia, "trabalho sozinho" se eugencia}}
**Servicos principais:**
- {{servico 1}}
- {{servico 2}}
- {{servico 3}}

## Contexto adicional

{{qualquer info livre relevante que o usuario tenha dado}}
```

### `_contexto/preferencias.md`

Substituir por:

```markdown
# Preferencias de Comunicacao

## Tom de voz

{{resposta da pergunta 9}}

## O que evitar

{{resposta da pergunta 10}}

## Estilo geral

- Respostas {{curtas/diretas | detalhadas}} conforme tom escolhido
- {{outras preferencias inferidas}}

## Preferencias adicionais

{{vazio — sera preenchido conforme aprendizado}}
```

### `_contexto/estrategia.md`

Substituir por:

```markdown
# Foco Atual

## Fase

{{inferir da resposta 11 — ex: "expansao", "consolidacao", "otimizacao operacional"}}

## Prioridade principal

{{resposta da pergunta 11}}

## O que pode esperar

- Tarefas relacionadas a {{prioridade}} devem ter peso maior
- {{outras inferencias}}

## Contexto com prazo

{{resposta da pergunta 12, com data absoluta se foi mencionado prazo relativo}}
```

---

## Confirmar com o usuario

Antes de salvar, mostrar um **resumo curto** das respostas e perguntar:

> "Tudo certo? Salvo assim ou quer ajustar algo?"

Apos confirmacao, escrever os 3 arquivos.

---

## Proximos passos (mostrar ao final)

Depois de salvar, mostrar:

> "Pronto! Workspace ClaudePRO configurado.
>
> Proximos passos:
> 1. Configurar credenciais Meta Ads: `python3 .claude/skills/meta-ads/scripts/setup.py`
> 2. Configurar credenciais Google Ads: `python3 .claude/skills/google-ads/scripts/setup.py full`
> 3. Comecar a trabalhar — me chame quando precisar de algo."

---

## Regras importantes

1. **Uma pergunta por vez.** Nunca enviar lista de 12 perguntas de uma so vez.
2. **Nao inventar respostas.** Se o usuario nao responder algo, deixar o campo vazio ou colocar `[a definir]`.
3. **Sem emojis** nas perguntas, a menos que o usuario sinalize estilo descontraido na pergunta 9.
4. **Confirmar antes de salvar.** Sempre mostrar resumo antes de escrever os arquivos.
5. **Datas relativas viram absolutas.** Se o usuario disser "ate o fim do mes", converter para `2026-05-31` (usar a data atual como referencia).
6. **Nao oferecer outros perfis.** So `agencia` ou `eugencia`. Se o usuario disser "sou freelancer/solopreneur/empresa", explicar que mapeamos isso pra `eugencia` (se solo) ou `agencia` (se tem equipe).
