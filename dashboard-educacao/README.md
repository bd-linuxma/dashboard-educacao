# Dashboard Educação Listada Brasil — +A Educação

Dashboard automatizado de acompanhamento do setor de educação listada no Brasil.

**Atualização automática toda segunda-feira às 6h BRT** via GitHub Actions.

## O que monitora

### Brasil (B3)
| Ticker | Companhia | Foco |
|--------|-----------|------|
| COGN3 | Cogna | Kroton + Vasta (B2B) + Saber |
| YDUQ3 | Yduqs | Estácio + IBMEC + IDOMED |
| ANIM3 | Ânima | Inspirali (medicina) + São Judas |
| SEER3 | Ser Educacional | Uninassau + saúde (NE/N) |
| CSED3 | Cruzeiro do Sul | Presencial + EAD |

### Global Comps
| Ticker | Companhia | Relevância |
|--------|-----------|------------|
| LAUR | Laureate | LatAm higher ed |
| ATGE | Adtalem | Healthcare education |
| LOPE | Grand Canyon | Ed services B2B |
| STRA | Strategic Ed | Adult learners online |
| COUR | Coursera | Edtech plataforma |
| AFYA | Afya | Medicina BR + digital |

## Seções do Dashboard (34 gráficos)

1. **Executive Summary** — 7 key takeaways
2. **Visão de Mercado** — Preços, múltiplos, variações
3. **Financeiro** — P&L, balanço, lucro
4. **Alavancagem & Caixa** — DL/EBITDA, FCF, conversão, goodwill
5. **Segmentos** — Abertura por vertical com crescimento
6. **Radar Comparativo** — 6 eixos multidimensionais
7. **Base de Alunos** — Mix presencial/EAD/medicina
8. **Tickets** — Precificação por modalidade
9. **Inadimplência** — PDD, PMR, mix de funding
10. **Medicina** — Enamed, vagas, M&A
11. **Pós-Graduação** — Receita e crescimento
12. **Global Comps** — Benchmarking internacional
13. **Valuation Scatter** — EV/EBITDA × Margem EBIT
14. **Regulatório** — Marco EAD, Enamed, exposição EAD
15. **M&A** — Histórico e referências de múltiplo
16. **Analistas** — Target vs preço, recomendações
17. **Notícias** — Feed recente

## Setup (5 minutos)

### 1. Criar repositório no GitHub

```bash
# Clone este projeto
git clone <url-do-repo>
cd dashboard-educacao

# Ou inicie do zero
git init
git add .
git commit -m "Dashboard educação v1"
git remote add origin https://github.com/SEU_USUARIO/dashboard-educacao.git
git push -u origin main
```

### 2. Ativar GitHub Pages

1. Vá em **Settings → Pages** no repositório
2. Em **Source**, selecione **GitHub Actions**
3. Salve

### 3. Rodar a primeira vez

1. Vá em **Actions** no repositório
2. Clique em **Atualizar Dashboard Educação** na sidebar
3. Clique **Run workflow** → **Run workflow**
4. Aguarde ~1 minuto
5. Acesse: `https://SEU_USUARIO.github.io/dashboard-educacao/`

### 4. Pronto!

O dashboard agora atualiza **automaticamente toda segunda às 6h BRT**.

Também pode rodar manualmente a qualquer momento pelo botão "Run workflow".

## Atualização de dados operacionais

Os **dados de mercado** (preço, múltiplos, P&L, balanço) são buscados automaticamente do Fundamentus a cada execução.

Os **dados operacionais** (base de alunos, tickets, segmentos, captação, evasão, M&A) são curados e precisam ser atualizados manualmente no `build_dashboard.py` após cada trimestre:

1. Abra `build_dashboard.py`
2. Encontre a seção `SUPPLEMENTARY` (~linha 70)
3. Atualize os números do trimestre novo
4. Commit + push → o próximo workflow vai usar os dados novos

Ou peça ao Claude: *"atualiza os dados operacionais do dashboard com o 1T26 da Cogna"* e ele gera o bloco atualizado.

## Estrutura

```
dashboard-educacao/
├── .github/workflows/update.yml   ← GitHub Actions (cron semanal)
├── build_dashboard.py              ← Script principal
├── template.html                   ← HTML base (gerado pelo Claude)
├── output/                         ← Gerado automaticamente
│   ├── index.html                  ← Dashboard final
│   └── data.json                   ← Snapshot dos dados
└── README.md
```

## Fontes de dados

| Fonte | Tipo | Frequência |
|-------|------|------------|
| Fundamentus | Preços, múltiplos, balanço | Diária (scraping) |
| Earnings Releases (RI) | Operacional, segmentos | Trimestral (manual) |
| BTG, Santander, JP Morgan | Recomendações | Trimestral (manual) |
| MEC/Inep | Enamed, regulatório | Eventual (manual) |
| maisaedu.com.br | Logo | Na build |

## Licença

Uso interno +A Educação.
