# Aprendizados — Google Ads ClaudePRO

Regras aprendidas durante o uso. O Claude DEVE ler este arquivo antes de criar qualquer objeto.

---

## API v23 (SDK 30.0.0) — campos obrigatórios para criar campanha

- `contains_eu_political_advertising` é **enum** (não boolean). Usar valor `3` (DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING)
- `maximize_clicks` não funciona como atributo direto. Usar `manual_cpc.enhanced_cpc_enabled = False` como fallback
- Budget name deve ser único. Script agora usa timestamp no nome pra evitar colisão com budgets órfãos
- Descriptions do RSA: máximo 90 caracteres. Headlines: máximo 30 caracteres

---

## Setembro/2026 — fim do developer token e acesso pelo projeto Cloud

Testado de ponta a ponta com projeto novo em 20/09/2026.

- O Google **aposentou os developer tokens em 09/09/2026**. O nivel de acesso passou a pertencer ao **projeto do Google Cloud** que gerou as credenciais OAuth. Conta MCC deixou de ser obrigatoria. O token ainda e aceito no header, porem ignorado.
- **A lib `google-ads` precisa ser 32.0.0 ou maior.** Ate a 31.4.0 ela recusava a configuracao sem o token, mesmo com a API ja aceitando sem.
- **O seletor de projeto do Cloud Console nao muda sozinho** depois de criar um projeto. Da pra ativar a API, pedir acesso e criar credenciais tudo no projeto errado, sem nenhum aviso. O sintoma aparece depois, e parece "credencial invalida".
- **App OAuth em status "Testes" emite refresh token que expira em 7 dias.** O prazo e carimbado no momento da emissao, entao publicar depois nao estende um token ja existente. Publicar o app ANTES de gerar o token. Sintoma classico: "funcionava e parou sozinho exatamente uma semana depois".
- **Sem o nivel Explorer o projeto fica em Test.** Autentica normalmente e toda chamada a conta de producao falha com `CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION`. Pedir Explorer na Google Ads API Overview do Cloud Console, nao na Central de API do Google Ads.
- **Projeto vinculado a conta de faturamento em Free Trial e recusado no Explorer**, mesmo com tudo certo. Ou migra o projeto pro tier pago, ou desvincula o billing dele. A Google Ads API em si nao cobra nada.
- **Erro 500 na tela de consentimento** nos minutos seguintes a publicacao do app e propagacao, nao erro de configuracao. Esperar de 10 a 15 minutos.
