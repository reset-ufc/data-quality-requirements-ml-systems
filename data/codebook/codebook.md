# Codebook — Data Quality Requirements in ML Survey

**N**: 41 respondents (32 from PT-BR form + 9 from EN international form)
**Collection window**: 2025-02-14 → 2025-03-15

> Free-text responses and demographic categoricals are kept in their original language (PT or EN). For cross-language analyses use the derived columns: `gender_norm`, `age_band`, `education_norm`, `seniority_group`, `role_group`. Likert items (Q8/Q11/Q13/Q19/Q22) are mapped to identical ordinal scales across both subsets via bilingual lookup tables in `notebooks/utils.py`.

## Schema

| Column | Type | Domain | Source (Q) |
|---|---|---|---|
| `language` | categorical | pt, en | source subset |
| `timestamp` | datetime | Forms timestamp | - |
| `age` | categorical | raw label (PT "anos" / EN "years old") | Q1 |
| `age_band` | categorical | 18-24 / 25-34 / 35-44 / 45-54 / ... | derived |
| `country` | categorical | Brazil, Germany, France, Colombia, ... | derived (Q2) |
| `state` | UF (2 letters) | AC..TO (only when country=Brazil) | Q2 |
| `region` | categorical | North / Northeast / Central-West / Southeast / South / International | derived |
| `gender` | categorical | raw label (PT or EN) | Q3 |
| `gender_norm` | categorical | male, female, other, undisclosed | derived |
| `education` | categorical | raw label (PT or EN) | Q4 |
| `education_norm` | categorical | high_school / undergraduate / ms_student / master / phd_student / doctorate / specialization | derived |
| `role` | categorical | raw label (PT or EN) | Q5 |
| `role_group` | categorical | data_scientist / developer / ml_engineer / data_engineer / researcher / manager / other | derived |
| `seniority` | ordinal | Intern / Junior / Mid / Senior (PT or EN label) | Q6 |
| `seniority_ordinal` | int 1-4 | 1=Intern .. 4=Senior | derived |
| `seniority_group` | categorical | junior, senior | derived |
| `n_projects` | int | 0..40 (EN ranges parsed to midpoint) | Q7 |
| `skill_cleaning` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_normalization` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_outliers` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_integration` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_transformation` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_validation` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_pipelines` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_monitoring` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_libs` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `skill_split` | Likert 1-5 | 1=Very low .. 5=Very high | Q8 |
| `word_1` | string | free token, lowercased | Q9 |
| `word_2` | string | free token, lowercased | Q9 |
| `word_3` | string | free token, lowercased | Q9 |
| `word_4` | string | free token, lowercased | Q9 |
| `word_5` | string | free token, lowercased | Q9 |
| `imp_precision` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_completeness` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_consistency` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_credibility` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_currentness` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_accessibility` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_compliance` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_reliability` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_efficiency` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_traceability` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_understandability` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_availability` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `imp_recoverability` | Likert 1-5 | 1=Not important .. 5=Very important | Q11 |
| `pri_precision` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_completeness` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_consistency` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_credibility` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_currentness` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_accessibility` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_compliance` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_reliability` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_efficiency` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_traceability` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_understandability` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_availability` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `pri_recoverability` | Likert 1-5 | 1=No priority .. 5=Essential | Q13 |
| `re_experience` | string (open) | free-text response in PT or EN | varies |
| `imp_justification` | string (open) | free-text response in PT or EN | varies |
| `pri_justification` | string (open) | free-text response in PT or EN | varies |
| `balance_open` | string (open) | free-text response in PT or EN | varies |
| `versioning_open` | string (open) | free-text response in PT or EN | varies |
| `incorporation_open` | string (open) | free-text response in PT or EN | varies |
| `measurement_open` | string (open) | free-text response in PT or EN | varies |
| `documentation_open` | string (open) | free-text response in PT or EN | varies |
| `challenges_open` | string (open) | free-text response in PT or EN | varies |
| `discussion_freq` | Likert 1-5 | 1=Never .. 5=Every day | Q19 |
| `support_freq` | Likert 1-4 | 1=Rarely .. 4=Always | Q22 |

## Anonymization

- Email column (Q23): dropped from both forms. 20 respondents provided an email overall. Not redistributed.
- `@dropdown` column: empty Google Forms artefact (PT only). Removed in `load_raw`.
- `country` × `state`: Brazilian respondents normalized to 2-letter UF codes; non-BR respondents (Germany, France, Colombia) keep `country` only with `region='International'` — no identification beyond country level.
- Open responses: regex sweep for emails and proper-name candidates. No personal identifier was found. See cell 7 of notebook 01 for the procedure.