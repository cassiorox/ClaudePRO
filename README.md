# ClaudePRO — Kit de Boas-Vindas

Framework **ClaudePRO** pra usar o Claude Code com contexto do seu negócio.

---

## Como instalar

**1. Clone o repositório**
```bash
git clone https://github.com/cassiorox/ClaudePRO.git
cd ClaudePRO
```

**2. Abra no VS Code**
```bash
code .
```

**3. Abra o terminal integrado** (Ctrl + ` no Windows / Cmd + ` no Mac) e rode:
```bash
claude
```

**4. Chame o setup**
```
/setup
```

---

O Claude vai te fazer algumas perguntas e configurar o sistema pro seu negócio. Em 5 minutos você tem tudo pronto.

---

## O que vem no kit

**Skills prontas pra usar:**
- `/setup` — configura o sistema pro seu negócio (comece por aqui)
- `/novo-cliente` — cadastra um cliente novo (cria a pasta e o contexto.md)
- `/meta-ads` — gerencia campanhas Meta Ads (Facebook/Instagram) via SDK oficial
- `/google-ads` — gerencia campanhas Google Ads via SDK oficial
- `/proposta-comercial` — cria propostas comerciais em PDF com a identidade visual da sua marca

**Pastas geradas pelo `/setup`:**
- `_contexto/` — contexto do seu negócio e preferências
- `marca/` — guia de identidade visual da sua marca
- `templates/ferramentas/catalogo.md` — APIs, CLIs e MCPs disponíveis pra usar em skills

**Pasta `dados/`:**
- Drop zone pra arquivos que você quer analisar (CSV, XLSX, TXT, PDF)
- Útil quando você não tem MCP de Google Drive instalado

