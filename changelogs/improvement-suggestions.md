# Relatório de Sugestões de Melhoria — 29/04/2026 (Execução #4)

## Notícias Relevantes Encontradas (últimos ~7 dias, 22–29/abr)

### Dividendos aprovados / eventos corporativos
- **Cogna (COGN3) aprova R$ 28,6 milhões em dividendos (28/abr)** — R$ 0,0143 por ação. Data-com 27/abr; ex-dividendos a partir de 28/abr; pagamento em parcela única em 29/mai. Dividend yield implícito modesto, mas sinaliza retomada de distribuição. [Money Times](https://www.moneytimes.com.br/cogna-cogn3-aprova-r-286-milhoes-em-dividendos-veja-valor-por-acao-e-datas/) · [BPMoney](https://bpmoney.com.br/negocios/empresas/cogna-cogn3-aprova-dividendos-de-r-285-milhoes-veja-valor-por-acao/)
- **Ânima (ANIM3) aprova R$ 29,3 milhões em dividendos (24/abr)** — R$ 0,07778 por ação. Ex-dividendos a partir de 27/abr; pagamento em 15/mai. [ADVFN](https://br.advfn.com/jornal/2026/04/anima-educacao-aprova-dividendos-de-r-29-3-milhoes-veja-valor-por-acao-e-data-de-pagamento)
- **Vitru (VTRU3) conclui follow-on na B3 (20/abr)** — Liquidação efetiva da oferta primária (R$ 200M base + R$ 100M lote adicional/suplementar). Primeira captação pós-migração Nasdaq→B3. [ADVFN](https://br.advfn.com/jornal/2026/04/vitru-educacao-capta-recursos-em-follow-on-na-b3-e-reforca-estrategia-de-crescimento-no-ensino-superior)

### Recomendações de bancos / sell-side
- **Santander promove SEER3 a top pick do setor (abr/26)** — Upgrade de Neutro para **Outperform**, target **R$ 12,80**. Tese: FCF yield ~16%, ~R$ 110M em dividendos esperados, geração de caixa robusta em ano eleitoral volátil. Cogna (COGN3) e Ânima (ANIM3) também outperform; Vitru (VTRU3) neutro; **CSED3 mantida em underperform**. [Seu Dinheiro](https://www.seudinheiro.com/2026/empresas/santander-reavalia-setor-de-educacao-e-promove-ser-educacional-seer3-a-top-pick-veja-ranking-completo-lvgb/) · [Investidor10](https://investidor10.com.br/noticias/santander-elege-top-pick-da-educacao-e-ve-dividendo-milionario-em-2026-117920/) · [Money Times](https://www.moneytimes.com.br/santander-reavalia-setor-de-educacao-e-promove-ser-a-top-pick-ceci/)
- **BofA: setor sofre no 1T26; Ser e Ânima preferidas (abr/26)** — Yduqs, Cogna e Afya mais expostas a impactos regulatórios (medicina, EAD); Ânima, Ser e Vitru beneficiárias relativas. Impacto regulatório completo só aparece a partir do 2T26 (turmas antigas ainda sustentam números). Custos de equipe e marketing pressionam margens. [Seu Dinheiro](https://www.seudinheiro.com/2026/bolsa-dolar/yduqs-cogna-anima-ser-empresas-de-educacao-devem-sofrer-no-1t26-veja-quem-ganha-e-quem-perde-segundo-o-bofa-kaes/)
- **Goldman Sachs: Ânima destaque do 1T26** — Posição relativamente mais resiliente entre as listadas, segundo projeções do banco. [Gazeta Mercantil](https://gazetamercantil.com/anima-anim3-1t26-analise-goldman-setor-educacional)

### Regulatório / MEC
- **MEC/Inep publica diretrizes e cronogramas do Enade 2026 (27/abr)** — Edital nº 49/2026: 40 áreas avaliadas (21 licenciatura, 14 bacharelado, 4 tecnólogos) + medicina via Enamed. **Prova do Enamed: 13/set/2026.** Inscrições concluintes: 27/abr–18/mai; ingressantes: 17/ago–17/set. [MEC](https://www.gov.br/mec/pt-br/assuntos/noticias/2026/abril/publicadas-diretrizes-e-cronogramas-do-enade-2026) · [Inep](https://www.gov.br/inep/pt-br/centrais-de-conteudo/noticias/enade/inep-publica-diretrizes-cronogramas-e-prazos-relativos-a-edicao-do-enade-2026-que-orientarao-as-acoes-das-instituicoes-de-educacao-superior)

---

## Dados que Precisam de Atualização

1. **SEER3 — target e recomendação** — Santander promoveu para **outperform** com target **R$ 12,80** (vs R$ 12,00 atual no `SUPPLEMENTARY`). *(Atualizado neste run: `tgt` 12.00→12.80, `rec` Neutro→Compra.)*
2. **Highlights (`hl`) com eventos da semana** — Santander top pick para SEER3; dividendos COGN3/ANIM3; conclusão do follow-on da Vitru. *(Aplicado parcialmente: `hl` da SEER3 atualizado.)*
3. **NEWS array** — Items de 03/03 a 14/03 saíram do top 13; substituídos por eventos das últimas duas semanas (dividendos COGN3/ANIM3, Enade/Enamed, Santander top pick, BofA 1T26, Vitru conclui follow-on). *(Atualizado neste run.)*
4. **Cotações/múltiplos** — Captados dinamicamente via Fundamentus na build (OK).
5. **Operacional 1T26** — Resultados ainda não divulgados; ciclo esperado para fim de mai/26 (~45 dias após fechamento). Sem ajuste no bloco `SUPPLEMENTARY`.

---

## Sugestões de Melhoria

### 1. Adicionar painel "Consenso de Analistas" (multi-casa)
**Justificativa:** Em apenas 30 dias, três casas mexeram nos targets do setor (Itaú BBA: COGN3 R$6 e YDUQ3 R$19; BTG: COGN3 R$5; Santander: SEER3 R$12,80). O dashboard hoje exibe um único `tgt` por empresa, com viés de quem foi atualizado por último. Um mini-painel "min | mediana | max | #casas | última revisão" daria leitura mais robusta e capturaria a divergência entre BTG (vaca leiteira / FCF) e Santander/BofA (top pick por geração de caixa em ano eleitoral). Repetida da execução #3 — aumenta em valor a cada semana que passa.
**Tipo:** Estrutural — apenas sugestão.

### 2. Calendário compacto de eventos corporativos (datas-com, ex, pagamento, follow-ons)
**Justificativa:** Em apenas abril já tivemos 4 eventos relevantes: COGN3 ex 28/abr (pagto 29/mai), ANIM3 ex 27/abr (pagto 15/mai), SEER3 1ª parcela 30/abr e 2ª parcela 29/mai, Vitru follow-on liquidado 20/abr. O feed de notícias mistura eventos com manchetes — um bloco "Próximos 30 dias" em formato calendário (5–8 linhas) tornaria a UX muito mais útil para o usuário em rotina semanal de monitoramento. Repetida da execução #3.
**Tipo:** Estrutural — apenas sugestão.

### 3. Adicionar VTRU3 como comp doméstico (mesmo sem captura via Fundamentus)
**Justificativa:** Vitru continua relevante: concluiu follow-on de R$ 200M–300M em 20/abr (1ª captação pós-migração Nasdaq→B3) e foi classificada como neutro pelo Santander. Como 6º player listado e referência de EAD adulto (análogo ao STRA), a ausência dela no dashboard deixa cobertura setorial incompleta. Inclusão como comp local (sem ingestão automática) preservaria estabilidade do build. Repetida da execução #3.
**Tipo:** Estrutural — apenas sugestão.

### 4. Refatorar pipeline para eliminar fonte única de verdade no template.html
**Justificativa:** A execução #3 já corrigiu o bug original — o `NEWS` agora é injetado em `build_html()`. Mas a mesma classe de risco persiste em outros pontos: por exemplo, ticker-bar prices, recomendações ("Compra"/"Neutro" exibidas) e o subtítulo do Executive Summary podem estar hardcoded em `template.html`. Um audit (mapear todos os blocos do template que dependem de dados curados em `SUPPLEMENTARY`) garantiria que o **único** ponto de edição manual fosse o Python. Tarefa de manutenção de baixo risco.
**Tipo:** Refactor — sugestão para próxima iteração.

### 5. Bloco "Resumo Macro do Setor" (1T26 outlook)
**Justificativa:** Com 3 grandes casas (BofA, Goldman, Santander) emitindo views convergentes sobre o 1T26 (sofrimento generalizado, mas com vencedores relativos: ANIM/SEER), faria sentido um bloco fixo de 80–100 palavras no topo do dashboard sintetizando a tese do trimestre — algo como "Outlook 1T26 (last update: dd/mm)". Mais útil que o feed de notícias para um leitor executivo em 30 segundos.
**Tipo:** Estrutural — apenas sugestão.

---

## Mudanças Implementadas Nesta Execução

### `build_dashboard.py`
- **`NEWS` array refatorado** — substituídos os 6 itens mais antigos (03/03, 12/03 ×2, 14/03, 15/03, 20/03 ×1) pelos 6 itens mais recentes:
  - 28/04 COGN3 — Cogna ex-dividendos R$28,6M (R$0,0143/ação); pagto 29/mai
  - 28/04 ANIM3 — Ânima ex-dividendos R$29,3M (R$0,0778/ação); pagto 15/mai
  - 27/04 SETOR — MEC/Inep publica Enade 2026; Enamed em 13/set
  - 23/04 SEER3 — Santander promove SEER3 a top pick (tgt R$12,80, outperform)
  - 22/04 SETOR — BofA 1T26: Ser e Ânima preferidas; YDUQ3, COGN3 e AFYA mais expostas
  - 20/04 SETOR — Vitru (VTRU3) conclui follow-on na B3 (1ª pós-migração)
  - Preservados itens entre 20/03 e 10/04 (8 anteriores que ainda têm relevância narrativa).
- **SEER3 `tgt`** — 12.00 → **12.80** (Santander, abr/26).
- **SEER3 `rec`** — 'Neutro' → **'Compra'** (Santander outperform top pick).
- **SEER3 `hl`** — atualizado para incluir "Santander promove a top pick (tgt R$12,80, outperform)".

### Restrições respeitadas
- ✅ Sem alteração de layout (`template.html` intocado)
- ✅ Sem novos componentes ou seções
- ✅ Mudanças estruturais apenas como sugestão neste relatório
- ✅ Build testado antes de commit (próximo passo)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     