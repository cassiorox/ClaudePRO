# Meta Ads ClaudePRO

Skill de Meta Ads para Claude Code. Gerencia campanhas no Facebook e Instagram via SDK oficial da Meta (`facebook-business`).

**54 operações** organizadas em 7 scripts:
- **read.py** - 22 operações de leitura (campanhas, ad sets, ads, criativos, audiências)
- **insights.py** - 5 operações de métricas e relatórios
- **targeting.py** - 9 operações de busca de interesses, comportamentos e geolocalização
- **create.py** - 8 operações de criação (campanhas, ad sets, ads, criativos, imagens, vídeos, audiências)
- **update.py** - 4 operações de edição
- **delete.py** - 2 operações de exclusão
- **advanced.py** - 4 operações avançadas (duplicação, swap de url_tags)

## Instalação rápida

```bash
# 1. Copiar a skill para a pasta do Claude Code
cp -r . .claude/skills/meta-ads/

# 2. Instalar o SDK da Meta
pip3 install facebook-business

# 3. Configurar as variáveis de ambiente (adicionar ao ~/.zshrc ou ~/.bashrc)
export META_ADS_TOKEN="seu-token-aqui"
export META_AD_ACCOUNT_ID="act_123456789"

# 4. Verificar a instalação
python3 .claude/skills/meta-ads/scripts/setup.py
```

## Como obter o token

1. Acesse [Meta for Developers](https://developers.facebook.com/)
2. Crie um App do tipo "Business"
3. Adicione o produto "Marketing API"
4. No Business Manager, crie um System User e gere um token com permissões `ads_management` e `ads_read`

Documentacao oficial Meta Marketing API: https://developers.facebook.com/docs/marketing-api/get-started

## Uso

Depois de instalada, a skill é ativada automaticamente quando você fala com o Claude Code sobre Meta Ads. Exemplos:

- "lista as campanhas ativas da minha conta"
- "cria uma campanha de leads com orçamento de R$50/dia"
- "pega as métricas dos últimos 7 dias da campanha X"
- "duplica essa campanha e troca os url_tags"

## Disclaimer: use com responsabilidade

Essa skill foi **vibe-codada com Claude Code** a partir da documentação oficial do [facebook-business SDK](https://github.com/facebook/facebook-python-business-sdk) e da [Meta Marketing API](https://developers.facebook.com/docs/marketing-api/). Ela é um projeto experimental que estamos começando a testar agora.

**Pontos importantes antes de usar:**

- **Use por sua conta e risco.** Nós não garantimos que o uso dessa skill não vai resultar em restrições, bloqueios ou qualquer problema na sua conta de anúncios. A Meta tem políticas próprias sobre automação e pode mudar as regras a qualquer momento.
- **Leia as políticas da Meta.** Antes de usar qualquer automação, entenda os [Termos de Serviço da Meta](https://www.facebook.com/policies/ads/) e as [regras de rate limiting da Marketing API](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/). A skill inclui delays entre operações de escrita, mas isso não é garantia de nada.
- **Revise o código.** Essa skill tem acesso de leitura e escrita na sua conta de anúncios. Antes de usar, avalie o código dos scripts pra entender o que cada operação faz. É open source justamente pra isso.
- **Campanhas sempre nascem pausadas.** Por segurança, toda criação via skill é feita com status PAUSED. Mas operações de edição e exclusão agem diretamente nos objetos. Tenha cuidado.
- **Sem garantia de funcionamento.** O SDK e a API da Meta mudam com frequência. Algo que funciona hoje pode quebrar amanhã. Se algo parar de funcionar, provavelmente é uma mudança na API, não no seu setup.

Em resumo: é uma ferramenta poderosa, mas você é o responsável pelo que acontece na sua conta. Use com consciência, teste em contas de teste primeiro se possível, e não faça nada que você não faria manualmente no Ads Manager.

## Parte de

Framework **ClaudePRO**
