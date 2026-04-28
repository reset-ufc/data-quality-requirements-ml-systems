# Replication Package — Survey on Data Quality Requirements in ML Systems

Companion artifact for the paper *"Practitioners' Perceptions of Data Quality Requirements in Machine Learning-Enabled Systems: An Exploratory Study"*.

> This package allows full reproduction of every figure, table, number, and citation from the paper from the anonymized raw data.

---

## 1. Structure

```
replication-package/
├── README.md                       # this file (English)
├── LICENSE                         # CC-BY 4.0
├── requirements.txt                # minimal dependencies (pip-compatible)
├── pyproject.toml                  # uv-compatible environment
├── data/
│   ├── raw/survey_responses.xlsx              # 32 PT-BR responses (national form)
│   ├── raw/survey_responses_2.xlsx            # 9 EN responses (international form)
│   ├── processed/anonymized.csv               # unified dataset (n=41), stable schema
│   ├── processed/likert_importance.csv        # Q11 long form
│   ├── processed/likert_priority.csv          # Q13 long form
│   ├── processed/skills.csv                   # Q8 long form
│   ├── processed/words.csv                    # Q9 tokens
│   ├── processed/checkboxes.csv               # binary Q17/Q18/Q20/Q21
│   ├── processed/open_responses.csv           # open responses (long)
│   ├── processed/tables/*.tex                 # generated LaTeX tables
│   ├── processed/tables/*.csv                 # auxiliary tables
│   └── codebook/
│       ├── codebook.md                        # documented schema
│       ├── coding_scheme.csv                  # 90+ codes × 6 axial themes
│       └── coded_responses.csv                # (respondent, code) pairs
├── notebooks/
│   ├── 01_data_cleaning.ipynb                 # Phase 1 — cleaning + anonymization
│   ├── 02_descriptive.ipynb                   # Phase 3 (descriptive) + reliability (alpha, omega)
│   ├── 03_inferential.ipynb                   # Phase 4 (inferential)
│   ├── 04a_multiple_choice.ipynb              # Q17/Q18/Q20/Q21 + Q16 meta-finding + Fisher
│   ├── 04b_qualitative.ipynb                  # Grounded Theory + Q9 stemming
│   ├── 05_robustness.ipynb                    # post-hoc power analysis (Monte Carlo)
│   └── utils.py                               # palette, paths, statistical helpers
└── figures/                                   # generated PDFs (identical to the paper)
```

## 2. How to reproduce

### Prerequisites
- Python ≥ 3.12

### Setup

We recommend `uv` (faster), but `pip` works too:

```bash
# Option A — uv
uv sync
uv run jupyter lab

# Option B — pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

### Execution

Run the notebooks in order (each one produces CSVs consumed by the next):

```bash
cd notebooks
uv run jupyter nbconvert --to notebook --execute 01_data_cleaning.ipynb --output 01_data_cleaning.ipynb
uv run jupyter nbconvert --to notebook --execute 02_descriptive.ipynb --output 02_descriptive.ipynb
uv run jupyter nbconvert --to notebook --execute 03_inferential.ipynb --output 03_inferential.ipynb
uv run jupyter nbconvert --to notebook --execute 04a_multiple_choice.ipynb --output 04a_multiple_choice.ipynb
uv run jupyter nbconvert --to notebook --execute 04b_qualitative.ipynb --output 04b_qualitative.ipynb
uv run jupyter nbconvert --to notebook --execute 05_robustness.ipynb --output 05_robustness.ipynb
```

Expected total runtime: ~7 minutes (mostly: BCa bootstrap in §3-4 and Monte Carlo simulation in 05).

## 3. Map: paper figure/table → notebook

| Paper item | Notebook | Section |
|---|---|---|
| Table 2 (demographics) | `02_descriptive.ipynb` | §1 |
| Figure — skills diverging | `02_descriptive.ipynb` | §3 |
| Figure — importance diverging | `02_descriptive.ipynb` | §4 |
| Figure — priority diverging | `02_descriptive.ipynb` | §5 |
| Figure — importance × priority | `02_descriptive.ipynb` | §6 |
| Figure — frequencies (Q19, Q22) | `02_descriptive.ipynb` | §7 |
| Figure — Q9 top-15 words | `02_descriptive.ipynb` | §8 |
| Figure — subgroup heatmap | `02_descriptive.ipynb` | §10 |
| Table 3 (95% CI per characteristic) | `02_descriptive.ipynb` | §9 |
| Table — internal reliability (alpha, omega) | `02_descriptive.ipynb` | §13 |
| Figure — Q9 words by position | `04b_qualitative.ipynb` | §1 |
| Inferential table (with 95% CI on delta) | `03_inferential.ipynb` | §6 |
| Table — paired Wilcoxon importance × priority | `03_inferential.ipynb` | §8 |
| Table — Friedman + Nemenyi (Q11/Q13) | `03_inferential.ipynb` | §9 |
| Figure — Q17/Q18 implementation | `04a_multiple_choice.ipynb` | §4 |
| Figure — Q20/Q21 challenges | `04a_multiple_choice.ipynb` | §4 |
| Implementation table | `04a_multiple_choice.ipynb` | §5 |
| Table — Fisher's exact Q17–Q21 × subgroups | `04a_multiple_choice.ipynb` | §9 |
| Figure — power curves (sensitivity) | `05_robustness.ipynb` | §3 |
| Table — MDE per subgroup | `05_robustness.ipynb` | §2 |
| Qualitative codebook | `04b_qualitative.ipynb` | §7 |

## 4. Anonymization

- **Email column (Q23)**: dropped from both forms (PT and EN). Not redistributed.
- **`@dropdown` column**: empty Google Forms artefact (PT only), removed in `load_raw`.
- **Country × state**: Brazilian respondents normalized to `country=Brazil` + 2-letter UF + macro-region; non-BR respondents (Germany, France, Colombia) keep `country` only with `region='International'` — no identification beyond country level.
- **Language**: the `language` column (`pt`/`en`) records which form each row came from. Free text (Q10/Q12/Q14/Q15 and Q17/Q18/Q20/Q21 checkboxes) is preserved in the original language. Likerts and ordinals are mapped via bilingual dictionaries in `utils.py` to the same numeric scale across both subsets.
- **Open responses**: regex sweep for emails and proper-name candidates. No personal identifier was found. See cell 7 of notebook 01 for the procedure.

## 5. Anomalous finding: Q16 (versioning)

30 out of 32 PT responses to Q16 are literally identical, indicating most likely a *default* pre-selected option in Google Forms. This meta-finding about the instrument is discussed in Section 6 of the paper (Threats to Validity → Construct Validity). We reproduce the observation in `04a_multiple_choice.ipynb`, §6, with a formal **binomial test** (H0: uniform draw across 4 options; p ≈ 2.5×10⁻¹⁶).

## 6. Statistical methods

Summary of the tests applied, their assumptions, and where they run. Helpers in `notebooks/utils.py`.

| Test | Application | Notebook (section) | Helper / lib |
|---|---|---|---|
| Wilson 95% CI | proportions (Table 3) | `02` (§9) | `U.wilson_ci` (statsmodels) |
| Cronbach alpha + 95% bootstrap CI | reliability of Q11/Q13/Q8 | `02` (§13) | `pingouin.cronbach_alpha` |
| McDonald omega total | reliability (1-factor) | `02` (§13) | `U.mcdonald_omega` (sklearn FA) |
| Mann–Whitney U (two-sided) | subgroup comparisons on Q11/Q13 | `03` (§1–2, §6) | `scipy.stats.mannwhitneyu` |
| Cliff's delta + 95% bootstrap CI (BCa) | effect size after MWU | `03` (§1, §6) | `U.cliffs_delta_with_ci` |
| Paired Wilcoxon signed-rank | importance × priority (within-subject) | `03` (§8) | `U.wilcoxon_paired` |
| Matched-pairs rank-biserial *r* | effect size after Wilcoxon | `03` (§8) | `U.wilcoxon_paired` |
| Spearman rho + 95% bootstrap CI (BCa) | n_projects/seniority × Likerts | `03` (§4) | `U.spearman_with_ci` |
| Friedman chi² | global ranking of the 13 characteristics | `03` (§9) | `scipy.stats.friedmanchisquare` |
| Nemenyi post-hoc | pairs after Friedman | `03` (§9) | `scikit_posthocs.posthoc_nemenyi_friedman` |
| Holm–Bonferroni | family-wise correction | `03` (§3, §8); `04a` (§9) | `statsmodels.stats.multitest.multipletests` |
| Fisher's exact + OR (Wald CI) | Q17–Q21 (binary) × subgroups | `04a` (§9) | `U.fisher_or_ci` |
| Binomial test | Q16 anomaly | `04a` (§6) | `scipy.stats.binomtest` |
| Monte Carlo power (MWU) | post-hoc sensitivity | `05` (§1–4) | custom simulation |

Conventions:
- **Bootstrap**: 10k resamples, BCa 95% CI; automatic fallback to percentile when the BCa jackknife degenerates.
- **Holm family**: defined by `(comparison, dimension)` in `03` §6; by `(question, comparison)` in `04a` §9; by the 13 characteristics in `03` §8.
- **Effect-size**: Cliff's delta classified per Romano et al. (2006); rank-biserial per Kerby (2014).
- **Subgroups not tested**: `role` and `region` in multi-group mode (Kruskal–Wallis) — discarded due to `n ≤ 1` in some categories (`ml_engineer`, `manager`, `data_engineer`, North region). Only robust binary comparisons are reported.

Post-hoc power analysis (§ `05_robustness.ipynb`) shows that the design **only detects large effects** (\|delta\| ≥ 0.60) in two-sample comparisons at 80% power; the paired test (Wilcoxon, N=41) detects from medium (\|delta\| ≥ 0.45). Non-significant results below those thresholds should be interpreted as **underpowered**, not as evidence of absence.

## 7. Qualitative codebook

`data/codebook/coding_scheme.csv` contains 90+ codes organized into 6 axial themes:
- **T1 Contextualism** — balance depends on domain/application (44% of respondents)
- **T2 Garbage-in-out** — poor quality compromises the pipeline (16%)
- **T3 Trade-offs** — explicitly named (28%)
- **T4 Quality hierarchy** — essential-universal subset (16%)
- **T5 Practices/Tools** — feature selection, monitoring, platforms (25%)
- **T6 RE → ML gap** — limited/informal RE experience (56%)

Coding by a **single coder** — limitation reported as a threat to construct validity. The codebook is open for third-party re-coding.

## 8. Citation

```bibtex
@inproceedings{souza2026perception,
  author    = {Anonymous},
  title     = {Practitioners' Perceptions of Data Quality Requirements in Machine Learning-Enabled Systems: An Exploratory Study},
  year      = {2026},
  doi       = {pending}
}
```

## 9. License

Data and code are released under **Creative Commons Attribution 4.0 International (CC-BY 4.0)**. See [LICENSE](LICENSE).

## 10. Contact

Anonymized for review. Once accepted, the package will be published on Zenodo with a permanent DOI.
