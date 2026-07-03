# Practitioners' Perceptions of Data Quality Requirements in Machine Learning-Enabled Systems: An Exploratory Survey

This repository contains the replication package for the study ["Practitioners' Perceptions of Data Quality Requirements in Machine Learning-Enabled Systems: An Exploratory Survey"](paper/SBES___2026___Kevin___Data_Quality_Requirements_in_ML_Enabled_Systems.pdf). It provides all data, analysis scripts, and generated documents (figures and tables) of the results reported in the paper.


## Context

Data quality is an essential factor for the performance, reliability, and security of machine learning-based systems, yet it is still treated implicitly and inconsistently in practice. This study investigates—through an exploratory survey of 56 professionals from seven countries—how these professionals perceive, prioritize, and manage data quality throughout the ML system lifecycle.

---

## Research Questions

| RQ | Question |
|----|----------|
| **RQ₁** | How do practitioners perceive and prioritize data quality characteristics in ML-enabled systems? |
| **RQ₂** | How do practitioners evaluate and incorporate data quality requirements throughout the ML lifecycle? |
| **RQ₃** | What challenges do practitioners face when ensuring data quality in practice? |


## Instalation and Usage

### Requirements

* Python ≥ 3.12
* An environment compaible with .ipynb format, like: Jupyter, JupyterLab, Google Colab, VSCode (with Jupyter extension), etc

### Clone the repository

```bash
git clone https://github.com/reset-ufc/qualidade-de-dados-em-sistemas-aprendizado-de-maquina.git
cd qualidade-de-dados-em-sistemas-aprendizado-de-maquina
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Test the setup
To confirm that everything is working:

1. Open `notebooks\data_cleaning.ipynb`
2. Run all cells.

The environment is set up correctly and the code is executing as expected if all cells run without executing errors, and the output of the fifth cell is exactly this:
```
norm_country
Brazil           42
United States     5
Germany           4
France            2
Ireland           1
Colombia          1
China             1
Name: count, dtype: int64
```

### Hardware Setup Used

* CPU: Intel Core i5-13450HX
* RAM: 16 GB
* GPU: NVIDIA RTX 3050  6 GB


The project does not require significant computing power, so there are likely no obstacles to running it, even on lower-end hardware.

### Software environments

The entire project was carried out and executed using only the Windows 11 operating system; therefore, there is no guarantee - as we have not tested it - that the same results can be achieved using another system.


## Repository Structure

```
.
├── data/
│   ├── raw/                        # Original (anonymized), translated and mapped surveys 
│   │   ├── survey_responses.xlsx   # Portuguese form 
│   │   ├── survey_responses_2.xlsx # English form 
│   │   ├── parcial_quali.xlsx      # Categorical responses mapped to English 
│   │   └── full_quali.xlsx         # Open responses translated to English
│   ├── processed/                  # Cleaned and normalized data 
│   │   ├── anonymized.csv          # Cleaned data for notebooks
│   │   ├── likert_importance.csv   # Long-format importance ratings 
│   │   ├── likert_priority.csv     # Long-format priority ratings 
│   │   ├── skills.csv              # Long-format skill self-assessments 
│   │   ├── open_responses.csv      # Open-ended responses 
│   │   ├── words.csv               # Q9 word associations with position 
│   │   └── tables/
│   │       └── spearman_imp_vs_pri.tex  # LaTeX table: Spearman correlation results
│   └── codebook/          # Qualitative coding of open-ended responses
│       ├── Q10.xlsx       # RE experience narratives
│       ├── Q12.xlsx       # Importance justifications
│       ├── Q14.xlsx       # Priority justifications
│       └── Q15.xlsx       # Trade-off balance strategies
├── figures/   # Publication-ready PDF figures (output of notebooks)
│   ├── skills_diverging.pdf
│   ├── q9_top_words_by_position.pdf
│   ├── importance_priority_diverging.pdf
│   ├── implementation_q17_q20.pdf
│   ├── mc_group_heatmap_2x2.pdf
│   └── challenges_support_q21_q22.pdf
├── notebooks/
│   ├── utils.py                            # Shared utilities (plotting, parsing, statistics)
│   ├── data_cleaning.ipynb                 # Step 1 — data normalization and anonymization
│   ├── demographic_characterization.ipynb  # Step 2 — participant characterization
│   ├── RQ1.ipynb                           # Step 3 — perception and prioritization (Q9–Q16)
│   ├── RQ2.ipynb                           # Step 4 — implementation practices (Q17–Q20)
│   └── RQ3.ipynb                           # Step 5 — challenges and support (Q21–Q22)
├── paper /
│   └── SBES___2026___Kevin___Data_Quality_Requirements_in_ML_Enabled_Systems.pdf
├── survey artifacts/               # Consent forms and survey scripts
│   ├── Free and Informed Consent Form (FICF)_data_quality_en.pdf
│   ├── Script_survey_data_quality_EN.pdf
│   ├── Script_survey_data_quality_PT_BR.pdf
│   └── Termo_de_Consentimento_Livre_e_Esclarecido_(TCLE)_data_quality_pt_br.pdf
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## Running the package, step by step

Run the notebooks (all cells) in the following order. Each notebook reads outputs produced by the previous one.

### Step 1 — ```data_cleaning.ipynb```

(You don't need to run it again if, you already ran it to test the setup.)

Loads both survey forms (PT and EN), validates consent, normalizes responses, maps Likert text to numeric scales, and exports all processed datasets to `data/processed/` and `data/raw/`

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

## Dataset

The responses of the two surveys (english and portuguese) are included in `data/raw/` for transparency, but the field email was removed from the files to preserve participants privacy. The codebooks in `data/codebook/` document the qualitative coding applied to open-ended responses (Q10, Q12, Q14, Q15).

**Free and Informed Consent Form and Survey Script** of PT-BR and EN-US versions are in /survey artifacts.