---
name: novo-cliente
description: Cadastra um novo cliente no workspace ClaudePRO. Pede o contexto do cliente, cria a pasta dele em `clientes/<nome>/` e salva um `contexto.md`. Use quando o usuario disser "novo cliente", "cadastrar cliente", "adicionar cliente", "criar cliente", "entrou cliente novo" ou rodar /novo-cliente.
---

# novo cliente — Cadastro de cliente no ClaudePRO

Esta skill cria a pasta de um cliente e salva o contexto dele em `clientes/<nome-do-cliente>/contexto.md`.
Esse `contexto.md` vira a fonte de verdade pra qualquer coisa criada pra esse cliente depois.

---

## Passo a passo

### 1. Perguntar o nome do cliente

> "Beleza! Qual o nome do cliente?"

A partir da resposta, montar um slug em kebab-case minúsculo pra pasta
(ex: "Clínica Sorriso Reto" → `clinica-sorriso-reto`).

Antes de criar, verificar se já existe `clientes/<slug>/`. Se existir, avisar:
> "Já tem uma pasta pra esse cliente. Quer atualizar o contexto dele ou é outro cliente?"

### 2. Pedir o contexto

> "Me manda o contexto desse cliente — pode colar do jeito que tiver (briefing, áudio transcrito, anotações soltas). Quanto mais melhor: o que vende, pra quem, ticket, objetivo de mídia, tom da marca, o que não pode aparecer. Se faltar algo importante eu te pergunto depois."

Esperar o usuário enviar.

### 3. Organizar e salvar

1. Ler `clientes/_template/contexto.md` como base da estrutura.
2. Preencher os campos do template com o que o usuário enviou, sem inventar dados —
   deixar em branco o que não foi informado.
3. Jogar no fim, em "Contexto adicional", qualquer coisa relevante que não coube nos campos.
4. Salvar em `clientes/<slug>/contexto.md`.

### 4. Confirmar e fechar lacunas

Mostrar onde salvou e listar (no máximo 3) campos importantes que ficaram vazios:

> "Pronto, salvei em `clientes/<slug>/contexto.md`. Ficou faltando: ticket médio, pixel/contas e tom de voz. Quer preencher agora ou deixa pra depois?"

Não travar o cadastro por causa de campos faltando — o contexto pode ser completado depois.

---

## Observações

- Se o usuário já estiver falando de um cliente que **não** tem pasta, sugerir rodar esta skill.
- Um cliente = uma pasta com (no mínimo) um `contexto.md`. Arquivos extras do cliente
  (criativos, propostas, planilhas) podem morar na mesma pasta.
- Calibrar o tom da conversa pelas `_contexto/preferencias.md` do workspace.
