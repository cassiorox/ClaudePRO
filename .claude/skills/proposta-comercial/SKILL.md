---
name: proposta-comercial
description: Cria propostas comerciais profissionais em PDF para gestores de tráfego, usando a identidade visual configurada pelo usuário (cores, fonte e logo em marca/design-guide.md). Use SEMPRE que o usuário pedir para criar, montar, gerar ou fazer uma proposta comercial para um cliente, independente do nicho ou tipo de serviço. Também acione quando disser "manda proposta para", "preciso de uma proposta", "faz uma proposta de tráfego pago", "gera PDF da proposta", ou variações. Cobre propostas simples (um cliente), duplas (dois clientes no mesmo documento) e multi-artistas (casting de shows). Gera o PDF final com a logo do usuário no rodapé, fonte legível e sem travessões.
---

# Proposta Comercial

Skill para criar propostas comerciais em PDF para clientes de um gestor de tráfego.
Genérica: a identidade visual (cores, fontes, logo) vem do que o usuário configurou, não de uma marca fixa.

## Antes de começar: ler a configuração do usuário

Sempre, antes de montar, ler estes arquivos para calibrar a proposta à marca do usuário:

1. `marca/design-guide.md` — cores, tipografia, logo, estilo. **Fonte de verdade visual.**
2. `_contexto/empresa.md` — nome da agência/gestor, fundador, posicionamento, serviços.
3. `_contexto/preferencias.md` — tom de voz, o que evitar.
4. `clientes/<nome-do-cliente>/contexto.md` — se o cliente já tem pasta, ler antes de criar.

Extrair de `marca/design-guide.md`:
- **Cor de destaque / CTA** → usar em bordas, labels, dots, badges, CTAs. Variável `COR_DESTAQUE`.
- **Cor secundária / texto de destaque** → contraste. Variável `COR_SECUNDARIA`. Se não houver, escurecer a cor de destaque.
- **Fundo alternativo / cards** → fundo dos cards de destaque. Variável `COR_CARD`. Se não houver, usar um tom bem claro da cor de destaque.
- **Tipografia de títulos** e **de corpo**.
- **Logo** → caminho do arquivo (ex: `marca/logo.png`).
- **Nome / handle / site** → para o rodapé (vêm do design-guide ou de `_contexto/empresa.md`).

### Fallback (quando o design-guide está vazio)

Se o design-guide não tiver as cores ou logo preenchidas, **perguntar uma vez**:

> "Teu `marca/design-guide.md` ainda não tem cor de destaque/logo configurada. Quer me passar a cor (hex) e o caminho da logo agora, ou gero com um visual neutro? (azul `#2563eb`, sem logo no rodapé)"

Se o usuário pedir o neutro ou não responder, usar os defaults neutros:
- `COR_DESTAQUE` = `#2563eb`
- `COR_SECUNDARIA` = `#1e40af`
- `COR_CARD` = `#f5f8ff` com borda `#dbe7ff`
- Títulos: `Playfair Display` · Corpo: `DM Sans`
- Rodapé sem logo, apenas a linha de texto com nome/handle/site (se houver).

## Identidade visual obrigatória

- Usar `COR_DESTAQUE` em bordas, labels, dots, badges, CTAs.
- Usar `COR_SECUNDARIA` em valores e elementos de contraste.
- Cards de destaque com fundo `COR_CARD` e borda clara.
- Fonte de corpo legível, **mínimo 15px no body**.
- Fonte de títulos: a configurada (ou `Playfair Display` para propostas elegantes / `Bebas Neue` para entretenimento).
- **Sem travessões (—)** em nenhuma parte do documento.
- **Sem a palavra "contrato"** — substituir sempre por "parceria".
- Rodapé: logo do usuário centralizada (se houver) + linha com nome · handle · site.

## Informações que sempre devem constar

- Nome do cliente
- Nicho/segmento
- Serviços incluídos
- Valor(es) — fee de gestão separado da verba de mídia
- Plataformas de trabalho
- Próximos passos (prazos: dias 1-3, 4-8, 9-12)
- Observações importantes
- CTA final com validade de 15 dias

## Coleta de informações

Antes de montar, verificar se há informações suficientes. Se faltar alguma das abaixo, perguntar:

1. Nome e nicho/segmento do cliente
2. Serviços incluídos
3. Valor da gestão (fixo, % do lucro, ou fee por artista)
4. Plataformas (Meta Ads, Google Ads, TikTok Ads, etc.)
5. Objetivo principal (vendas, seguidores, leads, ingressos, etc.)
6. Itens extras: relatórios, reuniões, escopo detalhado, tabela de investimento?
7. Verba mínima de mídia (se houver)

Se o pedido já tiver informações suficientes, ir direto para a montagem sem perguntar.

## Tipos de proposta

### Proposta simples (1 cliente)

Seções padrão:
1. Header (gestor/agência, título, cliente, data, badge de parceria)
2. Sobre a proposta (objetivo)
3. Plataformas de trabalho
4. Serviços incluídos (grid de cards)
5. Modelo de remuneração / Investimento
6. Escopo dos serviços (se solicitado)
7. Próximos passos (timeline)
8. Observações importantes
9. CTA + rodapé com logo

**Modelos de remuneração:**
- Fee fixo mensal: exibir valor em destaque com a fonte de títulos
- Revenue share (% do lucro líquido): exibir % em destaque + explicação de como funciona na prática
- Fee por artista (casting): usar tabela com colunas Artista / Badge / Fee mensal

### Proposta dupla (2 clientes do mesmo empresário)

Adicionar seção "As empresas" com dois cards lado a lado:
- Card 1: cor `COR_DESTAQUE`
- Card 2: cor `COR_SECUNDARIA`
- Cada card: nome, nicho, descrição, objetivo
- Tabela de investimento com as duas empresas + total consolidado

### Proposta de casting (shows/entretenimento)

Tabela de fees com:
- Artistas de "Volume ampliado" (badge na cor de destaque): R$ X
- Demais artistas do casting (badge cinza, "Por artista"): R$ Y
- Nota explicando a diferença de forma neutra, sem criar hierarquia negativa
- Usar fonte `Bebas Neue` para o título

## Geração do PDF

### Dependência

```bash
pip install weasyprint --break-system-packages -q
```

### Fluxo obrigatório

1. Ler a logo do usuário em base64 a partir do caminho configurado no design-guide (se existir):
```python
import base64, os
logo_path = 'marca/logo.png'  # caminho vindo do design-guide
logo_b64 = None
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode()
```

2. Criar o HTML completo com a logo embutida em base64 no rodapé (omitir o `<img>` se não houver logo).
3. Salvar o HTML em `propostas/proposta-CLIENTE.html` (criar a pasta `propostas/` se não existir).
4. Gerar o PDF com weasyprint:
```python
from weasyprint import HTML
HTML(filename='propostas/proposta-CLIENTE.html').write_pdf('propostas/Proposta_Comercial_CLIENTE.pdf')
```
5. Confirmar o caminho do PDF gerado para o usuário.

### Estrutura HTML base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=DM+Sans:wght@300;400;500&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'DM Sans', Arial, sans-serif;
    background: #ffffff;
    color: #1a1a1a;
    padding: 52px 60px;
    max-width: 820px;
    margin: 0 auto;
    font-size: 15px;
    line-height: 1.65;
  }
  /* Substituir as cores abaixo pelas variáveis do design-guide:
     COR_DESTAQUE, COR_SECUNDARIA, COR_CARD e borda do card.
     Ver seções de estilo abaixo. */
</style>
</head>
<body>
  <!-- Header, seções, CTA, rodapé com logo -->
  <!--
    ESTRUTURA DO GRID DE SERVIÇOS (obrigatório para evitar quebra de página):

    <div class="services-grid">
      <div class="services-row">
        <div class="service-card">
          <span class="service-icon">&#9678;</span>
          <p class="service-title">Serviço 1</p>
          <p class="service-desc">Descrição.</p>
        </div>
        <div class="service-card" style="padding-left:6px; padding-right:6px;">
          <span class="service-icon">&#9648;</span>
          <p class="service-title">Serviço 2</p>
          <p class="service-desc">Descrição.</p>
        </div>
        <div class="service-card">
          <span class="service-icon">&#9672;</span>
          <p class="service-title">Serviço 3</p>
          <p class="service-desc">Descrição.</p>
        </div>
      </div>
      <div class="services-row">
        <div class="service-card" style="padding-top:12px;">...</div>
        <div class="service-card" style="padding-left:6px; padding-right:6px; padding-top:12px;">...</div>
        <div class="service-card" style="padding-top:12px;">...</div>
      </div>
    </div>
  -->
</body>
</html>
```

### CSS padrão dos componentes

> Onde aparece `COR_DESTAQUE`, `COR_SECUNDARIA`, `COR_CARD` e `BORDA_CARD`, substituir pelos valores do design-guide (ou pelos defaults neutros).

```css
/* HEADER */
.prop-header { border-left: 3px solid COR_DESTAQUE; padding-left: 20px; margin-bottom: 44px; }
.prop-header .agency { font-size: 11px; letter-spacing: 0.13em; text-transform: uppercase; color: #888; margin-bottom: 6px; }
.prop-header h1 { font-family: 'Playfair Display', Georgia, serif; font-size: 32px; font-weight: 600; color: #111; margin-bottom: 5px; }
.prop-header .client { font-size: 15px; color: #555; margin-bottom: 8px; }
.badge { display: inline-block; font-size: 11px; font-weight: 500; padding: 3px 10px; border-radius: 20px; background: COR_CARD; color: COR_SECUNDARIA; }

/* LABELS DE SEÇÃO */
.section { margin-bottom: 30px; }
.section-label { font-size: 10px; letter-spacing: 0.15em; text-transform: uppercase; color: COR_DESTAQUE; font-weight: 500; margin-bottom: 12px; }

/* CARDS */
.card { background: #fff; border: 0.5px solid #ddd; border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; }
.card-title { font-size: 15px; font-weight: 500; margin-bottom: 5px; color: #111; }
.card-desc { font-size: 13px; color: #555; line-height: 1.7; }

/* CARDS DE SERVIÇO — usar display:table para evitar quebra de página entre linhas */
.services-grid { display: table; width: 100%; border-spacing: 0; page-break-inside: avoid; }
.services-row { display: table-row; }
.service-card { display: table-cell; width: 33.33%; background: COR_CARD; border-radius: 10px; padding: 16px; border: 0.5px solid BORDA_CARD; vertical-align: top; page-break-inside: avoid; }
.service-icon { font-size: 18px; margin-bottom: 10px; color: COR_DESTAQUE; line-height: 1; display: block; }
.service-title { font-size: 14px; font-weight: 500; margin-bottom: 6px; color: #111; }
.service-desc { font-size: 12px; color: #666; line-height: 1.55; }
/* Cards do meio recebem padding lateral: style="padding-left:6px; padding-right:6px;" */
/* Segunda linha de cards recebe: style="padding-top:12px;" */

/* PLATAFORMAS */
.ptag { display: inline-block; font-size: 12px; font-weight: 500; padding: 5px 14px; border-radius: 20px; background: COR_CARD; color: COR_SECUNDARIA; border: 0.5px solid BORDA_CARD; }

/* INVESTIMENTO DESTACADO (fee fixo) */
.invest-box { border-left: 3px solid COR_DESTAQUE; background: COR_CARD; border-radius: 0 10px 10px 0; padding: 16px 20px; }
.invest-value { font-family: 'Playfair Display', Georgia, serif; font-size: 34px; font-weight: 600; color: COR_SECUNDARIA; line-height: 1; margin-bottom: 4px; }
.invest-sub { font-size: 13px; color: #555; }

/* TIMELINE */
.timeline-dot { width: 8px; height: 8px; border-radius: 50%; background: COR_DESTAQUE; margin-top: 6px; flex-shrink: 0; }
.timeline-text { font-size: 13px; color: #555; line-height: 1.6; }
.timeline-text strong { color: #111; font-weight: 500; }

/* DOTS DE OBSERVAÇÕES */
.obs-dot { width: 8px; height: 8px; border-radius: 50%; background: COR_DESTAQUE; margin-top: 6px; flex-shrink: 0; }
.obs-text { font-size: 13px; color: #555; line-height: 1.6; }

/* CTA */
.cta-box { border: 0.5px solid BORDA_CARD; border-radius: 10px; padding: 18px 22px; display: flex; align-items: center; justify-content: space-between; margin-bottom: 44px; background: COR_CARD; }
.cta-text { font-size: 15px; font-weight: 500; color: #111; }
.cta-sub { font-size: 12px; color: #888; }
.cta-brand { font-size: 14px; color: COR_DESTAQUE; font-weight: 500; }
.cta-details { font-size: 12px; color: #888; }

/* CONTEXT BOX */
.context-box { background: COR_CARD; border: 0.5px solid BORDA_CARD; border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; }
.context-box p { font-size: 13px; color: #555; line-height: 1.7; margin-bottom: 10px; text-align: justify; }
.context-box p:last-child { margin-bottom: 0; }
.context-highlight { font-size: 13px; font-weight: 500; color: COR_SECUNDARIA; }

/* RODAPÉ COM LOGO */
.footer { border-top: 0.5px solid #e5e5e5; padding-top: 28px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; }
.footer img { width: 90px; height: 90px; object-fit: contain; }
.footer .footer-line { font-size: 12px; color: #888; }
```

## Regras de conteúdo

- Nunca usar travessão (—) em nenhum texto
- Nunca usar a palavra "contrato" — sempre "parceria"
- Verba de mídia sempre separada do fee de gestão, com explicação clara de que são valores distintos — mencionar SOMENTE UMA VEZ (na nota abaixo do card de investimento, nunca nas observações)
- Data da proposta: usar o mês atual
- Validade: 15 dias a partir do envio
- Observação sobre criativos: sempre indicar que fotos/vídeos são de responsabilidade do cliente
- Se o cliente for pesquisável na web (site, Instagram), buscar antes de montar para personalizar o texto de apresentação
- Textos dentro de `.context-box` devem ter `text-align: justify`

## Texto de apresentação do gestor/agência

Quando o contexto pedir apresentar quem está propondo, montar o texto a partir de `_contexto/empresa.md` (nome, posicionamento, diferenciais, fundador). Não inventar credenciais que não estejam no contexto. Modelo neutro de base:

> "A **[NOME DA AGÊNCIA/GESTOR]** é especializada em tráfego pago, com foco em [DIFERENCIAL/POSICIONAMENTO descrito em empresa.md]."

Se `_contexto/empresa.md` estiver vazio, perguntar ao usuário como ele quer se apresentar (ou omitir o parágrafo de apresentação).

## Personalização por nicho

> A cor de destaque padrão é a do design-guide. As linhas abaixo só sugerem fonte de título e ajustes de tom; só trocar a cor se o usuário pedir um tratamento especial para o nicho.

| Nicho | Fonte título | Observações |
|---|---|---|
| Entretenimento/Shows | Bebas Neue | Tabela de casting com badges |
| Joias/Luxo | Cormorant Garamond | Tom refinado; cor âmbar `#BA7517` se fizer sentido |
| Turismo/Lifestyle | Playfair Display | Destacar experiência |
| Saúde/Terapia | Playfair Display | "pacientes" no lugar de "clientes" |
| Infoproduto | Playfair Display | Mencionar revenue share se for % |
| Outros | Playfair Display (ou a fonte do design-guide) | Padrão da marca do usuário |

> Quando o empresário já é cliente com outras propostas feitas, manter consistência visual entre as propostas do mesmo grupo.
