# Novidades do ClaudePRO

Para trazer as novidades pro teu kit sem perder nada, rode `/atualizar-kit`.

---

## 2026-10-12

- **Correção de segurança no `/meta-vv-publicos`**: o setup pedia o token da Meta no chat e recebia por argumento (`--token`), o que deixava o token exposto na transcrição da conversa e no histórico do terminal. Agora o token entra só no `.env` da skill, preenchido por você num editor, e o arquivo fica protegido (permissão 600). Se você já colou o token no chat alguma vez, revogue e gere outro.
- Nova regra no `AGENTS.md`: token, chave ou senha nunca passa pelo chat.
- Obrigado ao **Carlos Sarmento** por ter avisado do problema.

---

## 2026-10-09

- **`/onboarding`**: onboarding completo de cliente novo. Puxa site, Instagram e Google Meu Negócio, cria a pasta do cliente, o `contexto.md` e gera os estudos de persona e de mercado.
- **`/estudo-persona`**: estudo de persona profundo (medos, dores, objeções, níveis de consciência), calibrado pelas reviews e redes do cliente.
- **`/estudo-mercado`**: concorrentes, o que eles anunciam na Biblioteca de Anúncios, demanda de busca, canais e riscos do nicho.
- **`/atualizar-kit`**: atualiza o kit com as novidades sem sobrescrever o que é teu.
- **`/novo-cliente` saiu**: o cadastro de cliente agora é só pelo `/onboarding`, que também aceita apenas um briefing colado.
- Modelo de `contexto.md` do cliente ganhou as seções Fontes, Provas e reputação, Contato, Estudos e Lacunas.
