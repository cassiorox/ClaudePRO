# Fonte e créditos

- **Skill:** meta-vv-publicos (públicos de video view na Meta Ads por retenção)
- **Autor:** Igor Poggianella de Oliveira (contato.ifb@gmail.com)
- **Repositório oficial:** https://github.com/igorpoggianella/meta-vv-publicos
- **Licença:** MIT (ver `LICENSE`)
- **Versão importada:** commit `acfcebb` (20/08/2026), trazida pro ClaudePRO em 08/10/2026

Copiada do repositório oficial, com um patch local de segurança (12/10/2026):

- `setup.py`: removidos `--token` e `--insights-token`. O token é lido do `.env`
  preenchido pelo dono (ou por entrada oculta no terminal dele) e o `.env` fica com
  permissão 600.
- `SKILL.md` (passo 1) e `README.md` (Instalação): o Claude não pede mais o token no
  chat; orienta o usuário a preencher o `.env` na mão.

Motivo: token passado pelo chat ou por argumento fica gravado na transcrição e no
histórico do shell. Ao atualizar do repositório oficial, reaplicar este patch se o
autor não tiver incorporado.
Complementa a skill `meta-ads` (que gerencia campanhas); esta só cria públicos de vídeo.
