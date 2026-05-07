# Aprendizados — Google Ads ClaudePRO

Regras aprendidas durante o uso. O Claude DEVE ler este arquivo antes de criar qualquer objeto.

---

## API v23 (SDK 30.0.0) — campos obrigatórios para criar campanha

- `contains_eu_political_advertising` é **enum** (não boolean). Usar valor `3` (DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING)
- `maximize_clicks` não funciona como atributo direto. Usar `manual_cpc.enhanced_cpc_enabled = False` como fallback
- Budget name deve ser único. Script agora usa timestamp no nome pra evitar colisão com budgets órfãos
- Descriptions do RSA: máximo 90 caracteres. Headlines: máximo 30 caracteres
