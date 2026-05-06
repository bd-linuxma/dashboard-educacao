# Relatório de Sugestões de Melhoria — 06/05/2026 (Execução #5)

## Notícias Relevantes Encontradas (últimos ~7 dias, 29/abr–06/mai)

### Sell-side / regulatório — destaque da semana
- **JP Morgan liga alerta para YDUQ3 e SEER3 após notas do Enamed (mai/26)** — Banco classifica como "surpresa ruim": empresas sob cobertura tiveram desempenho fraco em vários cursos avaliados no Enamed; até **15% das vagas da Yduqs e 11% das da Ser** podem ser impactadas por sanções. **BTG pede calma** — argumenta que efeito real depende de prazos regulatórios e não invalida a tese de FCF do setor. [Seu Dinheiro – JP Morgan alerta](https://www.seudinheiro.com/2026/empresas/surpresa-ruim-jp-morgan-liga-alerta-para-yduqs-yduq3-e-outras-depois-das-notas-do-enademed-btg-pede-calma-bdap/) · [Seu Dinheiro – prova surpresa](https://www.seudinheiro.com/2026/empresas/anima-anim3-cogna-cogn3-yduqs-yduq3-e-outras-quem-ganhou-10-na-prova-surpresa-do-jp-morgan-bdap/) · [Metrópoles – 107 cursos reprovados](https://www.metropoles.com/brasil/veja-as-notas-dos-cursos-de-medicina-no-enamed-107-sao-reprovados)
- **Itaú BBA corta preço-alvo de YDUQ3 (mai/26)** — Casa que havia elevado para top pick em 10/abr (target R$19) agora reduz target citando "cenário desafiador em 2026" — captação EAD pressionada e impacto regulatório de medicina. *Reversão de mensagem em ~3 semanas; conflita com `tgt:19.00` e `rec:'Compra'` no `SUPPLEMENTARY`.* [Money Times](https://www.moneytimes.com.br/itau-bba-corta-preco-alvo-de-yduqs-yduq3-com-perspectiva-de-cenario-desafiador-em-2026-entenda-apsa/)
- **YDUQ3 — dividendos R$ 80M aprovados (29/mai)** — R$ 0,2737/ação aprovados em assembleia 26/abr; data-base 26/abr; pagamento 29/mai. [Money Times — visão geral YDUQ3](https://www.moneytimes.com.br/cotacao/yduq3/)

### Calendário / agenda corporativa
- **Ânima — release 1T26 em 6/mai (após mercado) e teleconferência 7/mai 9h00** — primeiro grande release operacional do trimestre no setor. [RI Ânima](https://ri.animaeducacao.com.br/)
- **SEER3 — 1ª parcela de dividendos paga em 30/abr** (R$ 30,5M); 2ª parcela em 29/mai. [Money Times](https://www.moneytimes.com.br/ser-educacional-seer3-aprova-r-611-milhoes-em-dividendos-pagamento-sera-em-duas-parcelas-ate-maio-de-2026-kda/)

### Regulatório / MEC
- **MEC — Portaria 224/2026 (publicada 02/mar/26)** — Calendário Anual de processos regulatórios no e-MEC e SEI para 2026. *Já em vigor; relevante como contexto.* [MEC](https://www.gov.br/mec/pt-br/assuntos/noticias/2026/marco/mec-divulga-prazos-dos-processos-regulatorios-no-e-mec-e-sei) · [AMIES](https://amies.org.br/mec-divulga-calendario-regulatorio-2026-para-a-educacao-superior/)
- **Decreto 12.456/2025 + Portarias 378 e 381/2025 — vigência segue até mai/2027** — Marco EAD: medicina, direito, odontologia, enfermagem e psicologia exclusivamente presenciais; transição de 2 anos para IES adequarem cursos. [MEC](https://www.gov.br/mec/pt-br/politica-regulacao-supervisao-educacao-superior/ead) · [Mattos Filho](https://www.mattosfilho.com.br/unico/regras-marco-regulatorio-ead/)

---

## Dados que Precisam de Atualização

1. **YDUQ3 `tgt`/`rec`/`hl`** — Itaú BBA cortou target após classificá-la como top pick em 10/abr. Sem número específico no resumo de imprensa; **mantido em `19,00`/`'Compra'`** nesta execução por falta de dado preciso. Sugestão: revisar manualmente após release do 1T26 (~3ª semana de mai/26) quando o consenso se reorganizar.
2. **SEER3 — risco regulatório no `hl`** — JP Morgan estima 11% das vagas em risco. `hl` atual da SEER3 não menciona o risco regulatório, só o upside Santander. Sem alteração nesta execução (preferi não diluir a tese positiva sem update completo das casas que reagem ao Enamed).
3. **`NEWS` array** — Adicionados 2 itens (JP Morgan/BTG, Itaú BBA cut), removidos 2 itens mais antigos de 20/03 (recompra YDUQ3 e MEC pune medicina — esta última está superada pela narrativa Enamed mais recente). *Aplicado nesta execução.*
4. **Cotações/múltiplos** — Captados via Fundamentus na build (OK).
5. **Operacional 1T26** — Ânima divulga em 6–7/mai. Demais (COGN3, YDUQ3, SEER3, CSED3) esperadas até fim de mai/26. Sem ajuste no `SUPPLEMENTARY` neste run.

---

## Sugestões de Melhoria

### 1. Capturar e exibir consenso multi-casa de targets/recomendações
**Justificativa:** A volatilidade do call sell-side está alta — Itaú BBA elevou YDUQ3 a top pick em 10/abr (R$19) e cortou em 02/mai (~3 semanas depois). O dashboard hoje mostra apenas o último `tgt`, criando viés de leitura. Exibir um resumo "min | mediana | max | #casas | última revisão" daria leitura mais robusta. Repetida das execuções #3 e #4 — **valor sobe a cada semana** com a dispersão de calls (BTG: vaca leiteira; Santander: SEER3 top pick; JP Morgan: alerta YDUQ3/SEER3; Itaú BBA: oscila).
**Tipo:** Estrutural — apenas sugestão.

### 2. Bloco "Risco Regulatório por empresa" (% de vagas/cursos sob supervisão)
**Justificativa:** O JP Morgan publicou métrica concreta (15% YDUQ3 e 11% SEER3 das vagas em risco) que é exatamente o tipo de número que faltava ao dashboard. Hoje há `ead_exp` (% receita EAD), mas nada que quantifique exposição a sanções regulatórias específicas (Enamed, supervisão de cursos de medicina, Decreto 12.456). Um KPI "% vagas em supervisão" + "% receita medicina" daria leitura imediata do risco em ano regulatório intenso.
**Tipo:** Estrutural — apenas sugestão.

### 3. Calendário compacto de eventos corporativos (releases, ex-dividendo, follow-ons)
**Justificativa:** Apenas em maio temos: 6/mai release ANIM3 + 7/mai call ANIM3 + 15/mai pagto dividendos ANIM3 + 29/mai pagto dividendos COGN3/YDUQ3/SEER3 (2ª parcela). Um bloco "Próximos 30 dias" (5–8 linhas em formato calendário) torna a UX muito mais útil em rotina semanal. Repetida das execuções #3 e #4.
**Tipo:** Estrutural — apenas sugestão.

### 4. Adicionar VTRU3 como comp doméstico
**Justificativa:** Vitru concluiu follow-on em 20/abr e está classificada como neutra pelo Santander. Inclusão como 6º player listado (sem ingestão Fundamentus automática, mantendo build estável) preservaria cobertura completa do setor. Repetida das execuções #3 e #4.
**Tipo:** Estrutural — apenas sugestão.

### 5. Bloco "Outlook do trimestre" no topo (sintese sell-side)
**Justificativa:** Com 4 casas (BofA, Goldman, Santander, JP Morgan) emitindo views convergentes-divergentes sobre 1T26, faria sentido um bloco fixo de 80–100 palavras sintetizando a tese consolidada (sofrimento generalizado mas com vencedores relativos: ANIM/SEER em FCF; YDUQ3 sob pressão regulatória após Enamed). Mais útil que o feed de notícias para um leitor executivo em 30 segundos. Repetida da execução #4.
**Tipo:** Estrutural — apenas sugestão.

---

## Mudanças Implementadas Nesta Execução

### `build_dashboard.py`
- **`NEWS` array** — adicionados 2 itens novos no topo:
  - `05/05 SETOR` — JP Morgan alerta YDUQ3 e SEER3 pós-Enamed (107 cursos reprovados); BTG pede calma `↓`
  - `02/05 YDUQ3` — Itaú BBA corta preço-alvo de YDUQ3 — cenário desafiador em 2026 `↓`
- **`NEWS` array** — removidos 2 itens mais antigos de 20/03 (mantém 13 itens):
  - `20/03 YDUQ3 — Yduqs aprova recompra de até R$100M` (datado; substituído pela narrativa de mai/26)
  - `20/03 SETOR — MEC pune 50+ cursos de medicina por baixo Enamed 2025` (superado pela cobertura mais recente do Enamed em 27/abr e 05/mai)

### Correção operacional
- **`build_dashboard.py`** estava com últimas 3 linhas truncadas no mount Linux (`if __name__ == "__m`) — provável artefato de execução anterior; corrigido para `if __name__ == "__main__":\n    main()\n`. Sem essa correção, o build falharia com `SyntaxError`.

### Restrições respeitadas
- ✅ Sem alteração de layout (`template.html` intocado)
- ✅ Sem novos componentes ou seções
- ✅ Mudanças estruturais apenas como sugestão neste relatório
- ✅ Build testado: `python build_dashboard.py` completou OK (5 tickers, 34 gráficos, 71.446 chars)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                