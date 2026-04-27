# Replication Package — Survey on Data Quality Requirements in ML Systems

Companion artifact for the SBES 2026 paper *"Percepção sobre Requisitos de Qualidade de Dados para Sistemas Baseados em Aprendizado de Máquina: Um Survey com Profissionais Brasileiros"*.

> Este pacote permite reproduzir todas as figuras, tabelas, números e citações do paper a partir dos dados brutos anonimizados.

---

## 1. Estrutura

```
replication-package/
├── README.md                       # este arquivo (PT/EN)
├── LICENSE                         # CC-BY 4.0
├── requirements.txt                # dependências mínimas (pip-compatible)
├── pyproject.toml                  # ambiente uv-compatível
├── data/
│   ├── raw/survey_responses.xlsx              # 32 respostas, 63 colunas (sem PII)
│   ├── processed/anonymized.csv               # base limpa, schema estável
│   ├── processed/likert_importance.csv        # long form Q11
│   ├── processed/likert_priority.csv          # long form Q13
│   ├── processed/skills.csv                   # long form Q8
│   ├── processed/words.csv                    # tokens Q9
│   ├── processed/checkboxes.csv               # binárias Q17/Q18/Q20/Q21
│   ├── processed/open_responses.csv           # respostas abertas (long)
│   ├── processed/tables/*.tex                 # tabelas LaTeX geradas
│   ├── processed/tables/*.csv                 # tabelas auxiliares
│   └── codebook/
│       ├── codebook_pt.md                     # schema documentado
│       ├── coding_scheme.csv                  # 90 códigos × 6 temas axiais
│       └── coded_responses.csv                # (respondente, código) pairs
├── notebooks/
│   ├── 01_data_cleaning.ipynb                 # Fase 1
│   ├── 02_descriptive.ipynb                   # Fase 3 (descritiva) + reliability (α, ω)
│   ├── 03_inferential.ipynb                   # Fase 4 (inferencial)
│   ├── 04a_multiple_choice.ipynb              # Q17/Q18/Q20/Q21 + meta-finding Q16 + Fisher
│   ├── 04b_qualitative.ipynb                  # Grounded Theory + lematização Q9
│   ├── 05_robustness.ipynb                    # Análise de poder post-hoc (Monte Carlo)
│   └── utils.py                               # paleta, paths, helpers estatísticos
└── figures/                                   # PDFs gerados (idênticos aos do paper)
```

## 2. Como reproduzir

### Pré-requisitos
- Python ≥ 3.12

### Setup

Recomendamos `uv` (mais rápido) mas `pip` funciona:

```bash
# Opção A — uv
uv sync
uv run jupyter lab

# Opção B — pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

### Execução

Os notebooks devem ser executados em ordem (cada um produz CSVs consumidos pelos seguintes):

```bash
cd notebooks
uv run jupyter nbconvert --to notebook --execute 01_data_cleaning.ipynb --output 01_data_cleaning.ipynb
uv run jupyter nbconvert --to notebook --execute 02_descriptive.ipynb --output 02_descriptive.ipynb
uv run jupyter nbconvert --to notebook --execute 03_inferential.ipynb --output 03_inferential.ipynb
uv run jupyter nbconvert --to notebook --execute 04a_multiple_choice.ipynb --output 04a_multiple_choice.ipynb
uv run jupyter nbconvert --to notebook --execute 04b_qualitative.ipynb --output 04b_qualitative.ipynb
uv run jupyter nbconvert --to notebook --execute 05_robustness.ipynb --output 05_robustness.ipynb
```

Tempo total esperado: ~7 minutos (a maior parte: bootstrap BCa em §3-4 e simulação Monte Carlo em 05).

## 3. Mapa: figura/tabela do paper → notebook

| Item do paper | Notebook | Célula |
|---|---|---|
| Tabela 2 (demografia) | `02_descriptive.ipynb` | seção 1 |
| Figura — skills diverging | `02_descriptive.ipynb` | seção 3 |
| Figura — importância diverging | `02_descriptive.ipynb` | seção 4 |
| Figura — prioridade diverging | `02_descriptive.ipynb` | seção 5 |
| Figura — importância × prioridade | `02_descriptive.ipynb` | seção 6 |
| Figura — frequências (Q19, Q22) | `02_descriptive.ipynb` | seção 7 |
| Figura — palavras Q9 top-15 | `02_descriptive.ipynb` | seção 8 |
| Figura — heatmap subgrupos | `02_descriptive.ipynb` | seção 10 |
| Tabela 3 (IC 95% características) | `02_descriptive.ipynb` | seção 9 |
| Tabela — confiabilidade interna (α, ω) | `02_descriptive.ipynb` | seção 13 |
| Figura — palavras Q9 por posição | `04b_qualitative.ipynb` | seção 1 |
| Tabela inferencial (com IC95% para δ) | `03_inferential.ipynb` | seção 6 |
| Tabela — Wilcoxon pareado importância × prioridade | `03_inferential.ipynb` | seção 8 |
| Tabela — Friedman + Nemenyi (Q11/Q13) | `03_inferential.ipynb` | seção 9 |
| Figura — Q17/Q18 implementação | `04a_multiple_choice.ipynb` | seção 4 |
| Figura — Q20/Q21 desafios | `04a_multiple_choice.ipynb` | seção 4 |
| Tabela implementação | `04a_multiple_choice.ipynb` | seção 5 |
| Tabela — Fisher exact Q17–Q21 × subgrupos | `04a_multiple_choice.ipynb` | seção 9 |
| Figura — curvas de poder (sensibilidade) | `05_robustness.ipynb` | seção 3 |
| Tabela — MDE por subgrupo | `05_robustness.ipynb` | seção 2 |
| Codebook qualitativo | `04b_qualitative.ipynb` | seção 7 |

## 4. Anonimização

- Coluna **e-mail (Q23)**: removida (15 de 32 respondentes informaram e-mail). Não é redistribuída.
- Coluna **`@dropdown`**: artefato vazio do Google Forms, removido.
- **Estado**: padronizado para sigla UF de duas letras + região derivada — não-identificante.
- **Respostas abertas**: revisão por regex para emails e nomes próprios. Nenhum identificador pessoal foi encontrado. Veja célula 7 do notebook 01 para o procedimento.

## 5. Achado anômalo: Q16 (versionamento)

30 de 32 respostas a Q16 são literalmente idênticas, indicando provavelmente uma opção pré-selecionada como *default* no Google Forms. Este achado meta sobre o instrumento é discutido na Seção 6 do paper (Threats to Validity → Validade de Constructo). Reproduzimos a observação no notebook `04a_multiple_choice.ipynb`, seção 6, com **teste binomial** formal (H₀: sorteio uniforme entre 4 opções; p ≈ 2.5×10⁻¹⁶).

## 6. Métodos estatísticos

Sumário dos testes aplicados, premissas e onde rodam. Helpers em `notebooks/utils.py`.

| Teste | Aplicação | Notebook (seção) | Helper / lib |
|---|---|---|---|
| Wilson 95% CI | proporções (Tabela 3) | `02` (§9) | `U.wilson_ci` (statsmodels) |
| Cronbach α + 95% CI bootstrap | confiabilidade Q11/Q13/Q8 | `02` (§13) | `pingouin.cronbach_alpha` |
| McDonald ω total | confiabilidade (1-factor) | `02` (§13) | `U.mcdonald_omega` (sklearn FA) |
| Mann–Whitney U (two-sided) | comparações entre subgrupos em Q11/Q13 | `03` (§1–2, §6) | `scipy.stats.mannwhitneyu` |
| Cliff's δ + IC95% bootstrap (BCa) | effect size pós-MWU | `03` (§1, §6) | `U.cliffs_delta_with_ci` |
| Wilcoxon signed-rank pareado | importância × prioridade (within-subject) | `03` (§8) | `U.wilcoxon_paired` |
| Matched-pairs rank-biserial *r* | effect size pós-Wilcoxon | `03` (§8) | `U.wilcoxon_paired` |
| Spearman ρ + IC95% bootstrap (BCa) | n_projects/seniority × Likerts | `03` (§4) | `U.spearman_with_ci` |
| Friedman χ² | ranqueamento global das 13 características | `03` (§9) | `scipy.stats.friedmanchisquare` |
| Nemenyi post-hoc | pares pós-Friedman | `03` (§9) | `scikit_posthocs.posthoc_nemenyi_friedman` |
| Holm–Bonferroni | correção por família | `03` (§3, §8); `04a` (§9) | `statsmodels.stats.multitest.multipletests` |
| Fisher's exact + OR (IC Wald) | Q17–Q21 (binárias) × subgrupos | `04a` (§9) | `U.fisher_or_ci` |
| Teste binomial | anomalia Q16 | `04a` (§6) | `scipy.stats.binomtest` |
| Monte Carlo de poder (MWU) | sensibilidade post-hoc | `05` (§1–4) | simulação própria |

Convenções:
- **Bootstrap**: 10k resamples, IC95% via BCa; fallback automático para percentile quando jackknife BCa degenera.
- **Família Holm**: definida por `(comparison, dimension)` em §6 do `03`; por `(question, comparison)` em §9 do `04a`; pelas 13 características em §8 do `03`.
- **Effect-size**: classificação de Cliff's δ por Romano et al. (2006); rank-biserial por Kerby (2014).
- **Subgrupos não testados**: `role` e `region` em modo multi-grupo (Kruskal–Wallis) — descartado por `n ≤ 1` em algumas categorias (`ml_engineer`, `manager`, `data_engineer`, Norte). Apenas comparações binárias robustas reportadas.

Análise de poder post-hoc (§ `05_robustness.ipynb`) mostra que o desenho **só detecta efeitos large** (\|δ\| ≥ 0.60) em comparações 2-amostras com poder 80%; pareado (Wilcoxon, N=32) detecta a partir de medium (\|δ\| ≥ 0.45). Resultados não-significativos abaixo desses limiares devem ser interpretados como **subpoder**, não como evidência de ausência de efeito.

## 7. Codebook qualitativo

`data/codebook/coding_scheme.csv` contém 90 códigos organizados em 6 temas axiais:
- **T1 Contextualismo** — equilíbrio depende do domínio/aplicação (44% dos respondentes)
- **T2 Garbage-in-out** — má qualidade compromete o pipeline (16%)
- **T3 Trade-offs** — explicitamente nomeados (28%)
- **T4 Hierarquia da qualidade** — subconjunto essencial-universal (16%)
- **T5 Práticas/Ferramentas** — feature selection, monitoramento, plataformas (25%)
- **T6 Lacuna ER → ML** — experiência limitada/informal em ER (56%)

Codificação por **um único codificador** — limitação reportada como ameaça à validade de constructo. O codebook está aberto para re-codificação por terceiros.

## 8. Citação

```bibtex
@inproceedings{souza2026perception,
  author    = {Anonymous},
  title     = {Percep{\c{c}}{\~a}o sobre Requisitos de Qualidade de Dados para Sistemas Baseados em Aprendizado de M{\'a}quina: Um Survey com Profissionais Brasileiros},
  booktitle = {Proceedings of the 40th Brazilian Symposium on Software Engineering (SBES)},
  year      = {2026},
  doi       = {pending}
}
```

## 9. Licença

Os dados e o código são licenciados sob **Creative Commons Attribution 4.0 International (CC-BY 4.0)**. Veja [LICENSE](LICENSE).

## 10. Contato

Anonimizado durante o processo de revisão do SBES 2026. Após aceite, o pacote será publicado no Zenodo com DOI permanente.
