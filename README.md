# Replication Package — Practitioners' Perceptions of Data Quality Requirements in Machine Learning-Enabled Systems: An Exploratory Survey

This repository contains the replication package for the study *"Practitioners' Perceptions of Data Quality Requirements in Machine Learning-Enabled Systems: An Exploratory Survey"*. It provides all data, analysis notebooks, and generated artifacts (figures and tables) needed to reproduce the results reported in the paper.

---

## Research Questions

| RQ | Question |
|----|----------|
| **RQ₁** | How do practitioners perceive and prioritize data quality characteristics in ML-enabled systems? |
| **RQ₂** | How do practitioners evaluate and incorporate data quality requirements throughout the ML lifecycle? |
| **RQ₃** | What challenges do practitioners face when ensuring data quality in practice? |

---

## Repository Structure

```
.
├── data/
│   ├── raw/                        # Original (anonymized), translated and mapped surveys 
│   │   ├── survey_responses.xlsx   # Portuguese form (37 respondents)
│   │   ├── survey_responses_2.xlsx # English form (19 respondents)
│   │   ├── parcial_quali.xlsx      # Categorical responses mappaed to English 
│   │   └── full_quali.xlsx         # Open responses translated and hand-edited
│   ├── processed/                  # Cleaned and normalized data 
│   │   ├── anonymized.csv          # Cleaned data for notebooks
│   │   ├── likert_importance.csv   # Long-format importance ratings 
│   │   ├── likert_priority.csv     # Long-format priority ratings 
│   │   ├── skills.csv              # Long-format skill self-assessments 
│   │   ├── open_responses.csv      # Open-ended responses 
│   │   ├── words.csv               # Q9 word associations with position 
│   │   └── tables/
│   │       └── spearman_imp_vs_pri.tex  # LaTeX table: Spearman correlation results
│   └── codebook/                   # Qualitative coding of open-ended responses
│       ├── Q10.xlsx                # RE experience narratives
│       ├── Q12.xlsx                # Importance justifications
│       ├── Q14.xlsx                # Priority justifications
│       └── Q15.xlsx                # Trade-off balance strategies
├── figures/                        # Publication-ready PDF figures (output of notebooks)
│   ├── skills_diverging.pdf
│   ├── q9_top_words_by_position.pdf
│   ├── importance_priority_diverging.pdf
│   ├── implementation_q17_q20.pdf
│   ├── mc_group_heatmap_2x2.pdf
│   └── challenges_support_q21_q22.pdf
├── notebooks/
│   ├── utils.py                    # Shared utilities (plotting, parsing, statistics)
│   ├── data_cleaning.ipynb         # Step 1 — data normalization and anonymization
│   ├── demographic_characterization.ipynb  # Step 2 — participant characterization
│   ├── RQ1.ipynb                   # Step 3 — perception and prioritization (Q9–Q16)
│   ├── RQ2.ipynb                   # Step 4 — implementation practices (Q17–Q20)
│   └── RQ3.ipynb                   # Step 5 — challenges and support (Q21–Q22)
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Execution Order

Run the notebooks in the following order. Each notebook reads outputs produced by the previous one.

### Step 1 — `data_cleaning.ipynb`

Loads both survey forms (PT and EN), validates consent, normalizes responses, maps Likert text to numeric scales, and exports all processed datasets to `data/processed/` and `data/raw/`
---

### Step 2 — `demographic_characterization.ipynb`

Characterizes the 56 survey respondents (Q1–Q8): demographics (age, gender, country, education, role, seniority, number of projects) and self-assessed skills across 10 data-processing activities.

**Figure generated:**

| File | Element Number |
|------|----------------|
| `figures/skills_diverging.pdf` | Figure 1 |

---

### Step 3 — `RQ1.ipynb` (addresses RQ₁)

Analyzes how practitioners perceive and prioritize data quality characteristics (Q9–Q16).

**Analyses:**
- **Q9** – Word association task: 279 tokens normalized to English, frequency by word position.
- **Q11 & Q13** – Importance vs. priority ratings for 13 data quality characteristics. Spearman's rank correlation coefficient computed for all 13 characteristics.
- **Q16** – Perceptions of data version control impact.

**Figures and tables generated:**

| File | Element Number |
|------|----------------|
| `figures/q9_top_words_by_position.pdf` | Figure 2 |
| `figures/importance_priority_diverging.pdf` | Figure 3 |
| `data/processed/tables/spearman_imp_vs_pri.tex` | Table 3 |

---

### Step 4 — `RQ2.ipynb` (addresses RQ₂)

Analyzes how data quality is incorporated into the ML development process (Q17–Q20).

**Analyses:**
- **Q17** – How data quality is incorporated.
- **Q18** – How model quality impact is measured.
- **Q19** – Frequency of formal data quality discussions.
- **Q20** – Documentation and communication practices.
- **Cross-group breakdowns** – Heatmaps comparing responses across career stage, data vs. product focus, and project volume.

**Figures generated:**

| File | Element Number |
|------|----------------|
| `figures/implementation_q17_q20.pdf` | Figure 4 |
| `figures/mc_group_heatmap_2x2.pdf` | Figure 5 |

---

### Step 5 — `RQ3.ipynb` (addresses RQ₃)

Analyzes the main challenges practitioners face in ensuring data quality and how often they receive support from other teams (Q21–Q22).

**Analyses:**
- **Q21** – Main challenges: inconsistency between sources, missing data, lack of standardization, outdated data, collection errors, traceability difficulties, lack of tools.
- **Q22** – Frequency of support from other teams, e.g., data engineers and data scientists.

**Figure generated:**

| File | Element Number |
|------|----------------|
| `figures/challenges_support_q21_q22.pdf` | Figure 6 |

---

## Setup

**Requirements:** Python ≥ 3.12

```bash
pip install -r requirements.txt
```

---

## Dataset

The raw survey files in `data/raw/` are included for full transparency. The codebooks in `data/codebook/` document the qualitative coding applied to open-ended responses (Q10, Q12, Q14, Q15) following Grounded Theory procedures.
