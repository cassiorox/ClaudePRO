@AGENTS.md

## Claude Code

O arquivo real de instruções deste workspace é o `AGENTS.md`, importado acima. Ele é lido também por
Codex, Cursor, Gemini CLI e qualquer outro agente que siga o padrão aberto.

**Não escreva instrução nova aqui.** Regra de comportamento, estrutura de pasta, fluxo de trabalho: tudo
vai no `AGENTS.md`. Este arquivo existe só para o Claude Code, e só para duas coisas:

1. **Garantir o carregamento.** O Claude Code lê `AGENTS.md` sozinho desde a v2.1.277, mas em algumas
   sessões (Amazon Bedrock, telemetria desativada) ele não consegue. O import acima cobre esses casos.
   Quando o Claude lê pelos dois caminhos, ele não duplica: o conteúdo entra uma vez só.
2. **Guardar o que for exclusivo do Claude Code**, abaixo desta linha. Hooks, comandos, MCPs, qualquer
   coisa que só faça sentido aqui e não valha para os outros agentes.

<!-- Instruções exclusivas do Claude Code entram daqui pra baixo. -->
