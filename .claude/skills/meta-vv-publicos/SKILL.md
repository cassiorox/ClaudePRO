---
name: meta-vv-publicos
description: Cria públicos de video view na Meta Ads por retenção (3s/ThruPlay/25%/50%/75%/95%), a partir dos vídeos orgânicos do Instagram ou dos vídeos dos anúncios de uma campanha específica. Use quando o usuário pedir "público de video view", "público de quem assistiu X% do vídeo", "público de engajamento de vídeo", "audiência dos vídeos da campanha", "custom audience de vídeo", ou /meta-vv-publicos.
---

# meta-vv-publicos

Skill de criação de públicos de engajamento por retenção de vídeo na Meta.
Dois módulos, Python puro (sem dependências): `vv_publicos.py` (vídeos orgânicos
do Instagram, por ano × corte de views) e `vv_campanha.py` (vídeos dos criativos
dos anúncios de uma campanha específica).

## Fluxo obrigatório (wizard conversacional)

1. **Setup, se necessário**: se não existir `.env` nesta pasta ou o `META_TOKEN`
   estiver vazio, rodar `python setup.py` (sem argumentos). Ele cria o `.env` a
   partir do `.env.example` e para. Mostrar ao usuário o caminho do `.env` e pedir
   que **ele mesmo** abra o arquivo num editor, cole o token em `META_TOKEN` e
   salve (permissões no README). Esperar o "pronto" e rodar `python setup.py` de
   novo. Mostrar o resumo que o setup imprime (contas de anúncio e páginas
   encontradas): os `act_...` listados são os candidatos pro passo 3.
   **Token nunca passa pelo chat:** não pedir o token na conversa, não aceitar
   se o usuário colar (orientar a revogar e gerar outro), não passar por
   argumento, não ler nem imprimir o conteúdo do `.env`.
2. **Perguntar a fonte** (se o pedido não deixar claro): vídeos orgânicos do
   Instagram (`vv_publicos.py`) ou vídeos dos anúncios de uma campanha
   (`vv_campanha.py`).
3. **Perguntar os parâmetros**, sugerindo defaults:
   - Sempre: conta(s) de anúncio (`--contas act_...`), retenções
     (`--retencoes`, default 75,95 no orgânico / 75 no de campanha), janela em
     dias (`--janela`, default 365).
   - Orgânico: anos (`--anos`, default ano atual) e corte de views
     (`--min-views`, default 100000).
   - Campanha: id numérico ou trecho do nome (`--campanha` — a busca ignora
     colchetes; se casar com mais de 5 campanhas o script lista e pede um termo
     mais específico).
4. **SEMPRE rodar com `--dry-run` primeiro** e mostrar ao usuário o que seria
   criado (nomes e contagem de vídeos).
5. **Só executar de verdade após OK explícito do usuário.**
6. Ao final, dar o placar: criados / já existiam / falhas — e avisar que o
   público fica "Atualizando" por algumas horas até a Meta popular.

## Notas de execução

- No Windows, rodar com `PYTHONIOENCODING=utf-8`.
- Varreduras do orgânico são lentas (1 chamada por vídeo) — considerar rodar em
  background; o cache `vv_cache.json` permite retomar.
- Máximo 100 vídeos por regra (limite da Meta); o script corta e avisa.
- Criação é idempotente por nome: rodar de novo não duplica.
- Nunca deletar público existente.


---

*Criada por Igor Poggianella de Oliveira (contato.ifb@gmail.com) em 20/08/2026*
