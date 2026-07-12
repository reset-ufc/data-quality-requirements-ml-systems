"""Shared functions and constants used across the analysis notebooks."""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROC = ROOT / "data" / "processed"
DATA_CODEBOOK = ROOT / "data" / "codebook"
FIGURES = ROOT / "figures"
RAW_XLSX_PT = DATA_RAW / "survey_responses.xlsx"
RAW_XLSX_EN = DATA_RAW / "survey_responses_2.xlsx"

for p in (DATA_RAW, DATA_PROC, DATA_CODEBOOK, FIGURES):
    p.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Schema: column index in original XLSX -> short name
# PT raw: 32 rows × 63 cols (extra @dropdown). EN raw: 9 rows × 62 cols.
# After dropping @dropdown from PT, both share 62-col schema indexed 0..61.
# ---------------------------------------------------------------------------
COLUMN_RENAME: dict[int, str] = {
    0: "timestamp",
    1: "consent",
    2: "age",
    3: "state",
    4: "gender",
    5: "education",
    6: "role",
    7: "seniority",
    8: "n_projects",
    # Q8 — data-processing skill (10 items)
    9: "skill_cleaning",
    10: "skill_normalization",
    11: "skill_outliers",
    12: "skill_integration",
    13: "skill_transformation",
    14: "skill_validation",
    15: "skill_pipelines",
    16: "skill_monitoring",
    17: "skill_libs",
    18: "skill_split",
    # Q9 — 5 words associated with data quality
    19: "word_1",
    20: "word_2",
    21: "word_3",
    22: "word_4",
    23: "word_5",
    # Q10 — Requirements Engineering experience (open)
    24: "re_experience",
    # Q11 — importance (13 characteristics)
    25: "imp_precision",
    26: "imp_completeness",
    27: "imp_consistency",
    28: "imp_credibility",
    29: "imp_currentness",
    30: "imp_accessibility",
    31: "imp_compliance",
    32: "imp_reliability",
    33: "imp_efficiency",
    34: "imp_traceability",
    35: "imp_understandability",
    36: "imp_availability",
    37: "imp_recoverability",
    # Q12 — importance justification
    38: "imp_justification",
    # Q13 — priority (13 characteristics, same order)
    39: "pri_precision",
    40: "pri_completeness",
    41: "pri_consistency",
    42: "pri_credibility",
    43: "pri_currentness",
    44: "pri_accessibility",
    45: "pri_compliance",
    46: "pri_reliability",
    47: "pri_efficiency",
    48: "pri_traceability",
    49: "pri_understandability",
    50: "pri_availability",
    51: "pri_recoverability",
    # Q14 — priority justification
    52: "pri_justification",
    # Q15-Q22 — open responses + frequency Likerts
    53: "balance_open",
    54: "versioning_open",
    55: "incorporation_open",
    56: "measurement_open",
    57: "discussion_freq",
    58: "documentation_open",
    59: "challenges_open",
    60: "support_freq",
    # Q23 — email (DROPPED for privacy)
    61: "_email_drop",
}

SKILL_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("skill_")]
WORD_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("word_")]
IMP_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("imp_") and v != "imp_justification"]
PRI_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("pri_") and v != "pri_justification"]

CHARACTERISTICS_EN = {
    "precision": "Precision",
    "completeness": "Completeness",
    "consistency": "Consistency",
    "credibility": "Credibility",
    "currentness": "Currentness",
    "accessibility": "Accessibility",
    "compliance": "Compliance",
    "reliability": "Reliability",
    "efficiency": "Efficiency",
    "traceability": "Traceability",
    "understandability": "Understandability",
    "availability": "Availability",
    "recoverability": "Recoverability",
}

# Backwards-compat alias (formerly PT-only labels)
CHARACTERISTICS_PT = CHARACTERISTICS_EN

# Display labels used in paper figures/tables.
# "precision" is relabelled "Accuracy" because the survey description pointed
# to the ISO 25012 accuracy concept, not ML precision (reproducibility).
# Q9 word normalization is intentionally unaffected.
CHARACTERISTICS_PAPER: dict[str, str] = {**CHARACTERISTICS_EN, "precision": "Accuracy"}

SKILL_LABELS_EN = {
    "skill_cleaning": "Data cleaning",
    "skill_normalization": "Normalization/standardization",
    "skill_outliers": "Outlier detection",
    "skill_integration": "Source integration",
    "skill_transformation": "Transformation (PCA, encoding)",
    "skill_validation": "Data validation",
    "skill_pipelines": "Pipeline automation",
    "skill_monitoring": "Production monitoring",
    "skill_libs": "Libraries (Pandas, etc.)",
    "skill_split": "Train/test split",
}

# Backwards-compat alias
SKILL_LABELS_PT = SKILL_LABELS_EN

# ---------------------------------------------------------------------------
# Likert mappings — PT and EN raw labels share the same ordinal scale
# ---------------------------------------------------------------------------
SKILL_MAP = {
    # PT raw labels
    "Muito baixa": 1,
    "Abaixo da Média": 2,
    "Média": 3,
    "Acima da média": 4,
    "Muito alto": 5,
    "Não se aplica": pd.NA,
    # EN raw labels
    "Very low": 1,
    "Below Average": 2,
    "Average": 3,
    "Above average": 4,
    "Very high": 5,
    "Not applicable": pd.NA,
}
IMPORTANCE_MAP = {
    # PT raw labels
    "Nada importante": 1,
    "Pouco importante": 2,
    "Neutro": 3,
    "Importante": 4,
    "Muito importante": 5,
    # EN raw labels
    "Not important at all": 1,
    "Not very important": 2,
    "Neutral": 3,
    "Important": 4,
    "Very important": 5,
}
PRIORITY_MAP = {
    # PT raw labels
    "Não é uma prioridade": 1,
    "Baixa prioridade": 2,
    "Neutro": 3,
    "Alta prioridade": 4,
    "Essencial": 5,
    # EN raw labels
    "Not a priority": 1,
    "Low priority": 2,
    "Neutral": 3,
    "High priority": 4,
    "Essential": 5,
}
DISCUSSION_FREQ_MAP = {
    # PT raw labels
    "Nunca": 1,
    "Menos de uma vez por mês": 2,
    "Menos de uma vez por semana, mas pelo menos uma vez por mês": 3,
    "Pelo menos uma vez por semana, mas não todos os dias": 4,
    "Todos os dias": 5,
    # EN raw labels
    "Never": 1,
    "Less than once a month": 2,
    "Less than once a week, but at least once a month": 3,
    "At least once a week, but not every day": 4,
    "Every day": 5,
}

SUPPORT_FREQ_MAP = {
    # PT raw labels
    "Raramente": 1,
    "Ocasionalmente": 2,
    "Frequentemente": 3,
    "Sempre": 4,
    # EN raw labels
    "Never": 0,
    "Rarely": 1,
    "Occasionally": 2,
    "Often": 3,
    "Always": 4,
}

VERSIONING_NORM = {
    # PT raw labels — Q16
    "Garante a consistência e rastreabilidade dos dados ao longo do tempo, permitindo que mudanças no dataset sejam documentadas e verificadas.": "ensures_consistency_traceability",
    "Aumenta a quantidade de dados disponíveis, sem necessidade de verificação de consistência entre as versões.": "increases_data_quantity",
    "Elimina a necessidade de documentar alterações no dataset, pois todas as mudanças são automaticamente aplicadas ao modelo.": "eliminates_documentation_need",
    "Reduz a precisão dos dados, pois versões antigas não são mais utilizadas nos modelos.": "reduces_accuracy",
    # EN raw labels — Q16
    "Ensures data consistency and traceability over time, allowing changes to the dataset to be documented and verified.": "ensures_consistency_traceability",
    "Increases the amount of data available, without the need to check consistency between versions.": "increases_data_quantity",
    "Eliminates the need to document changes to the dataset, as all changes are automatically applied to the model.": "eliminates_documentation_need",
    "Reduces data accuracy, as old versions are no longer used in models.": "reduces_accuracy",
    "I have no experience in this regard": "no_experience",
}

# ---------------------------------------------------------------------------
# Text-to-text translation maps — PT+EN → canonical EN label (for quality_analysis.csv)
# Used with pd.Series.replace() so unmapped values pass through unchanged.
# ---------------------------------------------------------------------------

# Q8 — skill level
SKILL_TEXT: dict[str, str] = {
    # PT raw labels
    "Muito baixa":    "Very low",
    "Abaixo da Média":"Below Average",
    "Média":          "Average",
    "Acima da média": "Above average",
    "Muito alto":     "Very high",
    "Não se aplica":  "Not applicable",
    # EN raw labels (normalize casing)
    "Very low":       "Very low",
    "Below Average":  "Below Average",
    "Average":        "Average",
    "Above average":  "Above average",
    "Very high":      "Very high",
    "Not applicable": "Not applicable",
}

# Q11 — importance
IMPORTANCE_TEXT: dict[str, str] = {
    # PT raw labels
    "Nada importante":  "Not important at all",
    "Pouco importante": "Not very important",
    "Neutro":           "Neutral",
    "Importante":       "Important",
    "Muito importante": "Very important",
    # EN raw labels
    "Not important at all": "Not important at all",
    "Not very important":   "Not very important",
    "Neutral":              "Neutral",
    "Important":            "Important",
    "Very important":       "Very important",
}

# Q13 — priority
PRIORITY_TEXT: dict[str, str] = {
    # PT raw labels
    "Não é uma prioridade": "Not a priority",
    "Baixa prioridade":     "Low priority",
    "Neutro":               "Neutral",
    "Alta prioridade":      "High priority",
    "Essencial":            "Essential",
    # EN raw labels
    "Not a priority": "Not a priority",
    "Low priority":   "Low priority",
    "Neutral":        "Neutral",
    "High priority":  "High priority",
    "Essential":      "Essential",
}

# Q16 — versioning (maps to full EN text)
VERSIONING_TEXT: dict[str, str] = {
    # PT raw labels
    "Garante a consistência e rastreabilidade dos dados ao longo do tempo, permitindo que mudanças no dataset sejam documentadas e verificadas.":
        "Ensures data consistency and traceability over time, allowing changes to the dataset to be documented and verified.",
    "Aumenta a quantidade de dados disponíveis, sem necessidade de verificação de consistência entre as versões.":
        "Increases the amount of data available, without the need to check consistency between versions.",
    "Elimina a necessidade de documentar alterações no dataset, pois todas as mudanças são automaticamente aplicadas ao modelo.":
        "Eliminates the need to document changes to the dataset, as all changes are automatically applied to the model.",
    "Reduz a precisão dos dados, pois versões antigas não são mais utilizadas nos modelos.":
        "Reduces data accuracy, as old versions are no longer used in models.",
    # EN raw labels (pass-through)
    "Ensures data consistency and traceability over time, allowing changes to the dataset to be documented and verified.":
        "Ensures data consistency and traceability over time, allowing changes to the dataset to be documented and verified.",
    "Increases the amount of data available, without the need to check consistency between versions.":
        "Increases the amount of data available, without the need to check consistency between versions.",
    "Eliminates the need to document changes to the dataset, as all changes are automatically applied to the model.":
        "Eliminates the need to document changes to the dataset, as all changes are automatically applied to the model.",
    "Reduces data accuracy, as old versions are no longer used in models.":
        "Reduces data accuracy, as old versions are no longer used in models.",
    "I have no experience in this regard": "I have no experience in this regard",
}

# Q19 — discussion frequency
DISCUSSION_TEXT: dict[str, str] = {
    # PT raw labels
    "Nunca": "Never",
    "Menos de uma vez por mês": "Less than once a month",
    "Menos de uma vez por semana, mas pelo menos uma vez por mês": "Less than once a week, but at least once a month",
    "Pelo menos uma vez por semana, mas não todos os dias": "At least once a week, but not every day",
    "Todos os dias": "Every day",
    # EN raw labels
    "Never": "Never",
    "Less than once a month": "Less than once a month",
    "Less than once a week, but at least once a month": "Less than once a week, but at least once a month",
    "At least once a week, but not every day": "At least once a week, but not every day",
    "Every day": "Every day",
}

# Q22 — support frequency
SUPPORT_TEXT: dict[str, str] = {
    # PT raw labels
    "Raramente":    "Rarely",
    "Ocasionalmente": "Occasionally",
    "Frequentemente": "Often",
    "Sempre":       "Always",
    "Nunca":        "Never",
    # EN raw labels
    "Never":        "Never",
    "Rarely":       "Rarely",
    "Occasionally": "Occasionally",
    "Often":        "Often",
    "Always":       "Always",
}

# Q17 — how data quality is incorporated (multiple-choice, term-by-term translation)
# Each cell may contain several options joined by ", ". Use translate_multi(), not str.replace().
Q17_TEXT: dict[str, str] = {
    # PT → EN
    "Avaliação inicial durante a coleta e preparação de dados":
        "Initial assessment during data collection and preparation",
    "Monitoramento contínuo durante todo o ciclo de vida do modelo":
        "Continuous monitoring throughout the model's life cycle",
    "Conjuntos de testes são aplicados para validar a consistência, completude e precisão dos dados antes de serem usados no treinamento.":
        "Test sets are applied to validate the consistency, completeness and accuracy of the data before it is used for training.",
    "Não existe uma estratégia formal para assegurar a qualidade dos dados durante o desenvolvimento.":
        "There is no formal strategy for ensuring data quality during development.",
    # EN → EN (identity — EN respondents already answered in English)
    "Initial assessment during data collection and preparation":
        "Initial assessment during data collection and preparation",
    "Continuous monitoring throughout the model's life cycle":
        "Continuous monitoring throughout the model's life cycle",
    "Test sets are applied to validate the consistency, completeness and accuracy of the data before it is used for training.":
        "Test sets are applied to validate the consistency, completeness and accuracy of the data before it is used for training.",
    "There is no formal strategy for ensuring data quality during development.":
        "There is no formal strategy for ensuring data quality during development.",
}

# Q18 — how model-quality impact is measured (multiple-choice, term-by-term translation)
Q18_TEXT: dict[str, str] = {
    # PT → EN
    "Testes A/B":
        "A/B testing",
    "Análise de métricas de performance (ex.: precisão, recall)":
        "Analysis of performance metrics (e.g. precision, recall)",
    "Revisão manual dos resultados":
        "Manual review of results",
    # EN → EN (identity)
    "A/B testing":
        "A/B testing",
    "Analysis of performance metrics (e.g. precision, recall)":
        "Analysis of performance metrics (e.g. precision, recall)",
    "Manual review of results":
        "Manual review of results",
}

# Q20 — how data quality is documented/communicated (multiple-choice, term-by-term translation)
Q20_TEXT: dict[str, str] = {
    # PT → EN
    "Linguagem estruturada (texto)":
        "Structured language (text)",
    "Ferramentas de Gerenciamento de Projetos (Jira, Trello ou Asana)":
        "Project management tools (Jira, Trello or Asana)",
    "Documentação Centralizada (Sistemas como Confluence, Google Docs ou Notion)":
        "Centralized documentation (systems such as Confluence, Google Docs or Notion)",
    "Reuniões de Alinhamento":
        "Alignment meetings",
    "Relatórios Periódicos":
        "Periodic reports",
    # EN → EN (identity)
    "Structured language (text)":
        "Structured language (text)",
    "Project management tools (Jira, Trello or Asana)":
        "Project management tools (Jira, Trello or Asana)",
    "Centralized documentation (systems such as Confluence, Google Docs or Notion)":
        "Centralized documentation (systems such as Confluence, Google Docs or Notion)",
    "Alignment meetings":
        "Alignment meetings",
    "Periodic reports":
        "Periodic reports",
}

# Q21 — main challenges in guaranteeing data reliability (multiple-choice, term-by-term translation)
Q21_TEXT: dict[str, str] = {
    # PT → EN
    "Inconsistência entre diferentes fontes de dados":
        "Inconsistency between different data sources",
    "Dados incompletos ou ausentes":
        "Incomplete or missing data",
    "Falta de padronização nos formatos de dados":
        "Lack of standardization in data formats",
    "Dados desatualizados ou não confiáveis":
        "Outdated or unreliable data",
    "Erros introduzidos durante a coleta e processamento":
        "Errors introduced during collection and processing",
    "Dificuldade na rastreabilidade e versionamento dos dados":
        "Difficulty in data traceability and versioning",
    "Falta de ferramentas adequadas para validação da qualidade dos dados":
        "Lack of adequate tools for validating data quality",
    # EN → EN (identity)
    "Inconsistency between different data sources":
        "Inconsistency between different data sources",
    "Incomplete or missing data":
        "Incomplete or missing data",
    "Lack of standardization in data formats":
        "Lack of standardization in data formats",
    "Outdated or unreliable data":
        "Outdated or unreliable data",
    "Errors introduced during collection and processing":
        "Errors introduced during collection and processing",
    "Difficulty in data traceability and versioning":
        "Difficulty in data traceability and versioning",
    "Lack of adequate tools for validating data quality":
        "Lack of adequate tools for validating data quality",
}

# ---------------------------------------------------------------------------
# Multi-choice translation helper
# ---------------------------------------------------------------------------

def translate_multi(value, mapping: dict, sep: str = ", ") -> str:
    """Translate a comma-separated multi-choice field term by term.

    Iterates through the cell string using greedy longest-match so that terms
    which themselves contain the separator (e.g. "precision, recall") are never
    split mid-way. Unrecognised tokens pass through unchanged.

    Use this instead of a str.replace() loop for multi-choice columns.
    """
    import pandas as pd  # local import keeps this usable before module-level pd

    if not isinstance(value, str) or pd.isna(value):
        return value

    sorted_keys = sorted(mapping, key=len, reverse=True)
    result: list[str] = []
    remaining = value

    while remaining:
        matched = False
        for key in sorted_keys:
            if remaining.startswith(key):
                result.append(mapping[key])
                remaining = remaining[len(key):]
                if remaining.startswith(sep):
                    remaining = remaining[len(sep):]
                matched = True
                break
        if not matched:
            # Unknown token (free-text addition or unmapped option): consume to next sep
            idx = remaining.find(sep)
            if idx == -1:
                result.append(remaining)
                remaining = ""
            else:
                result.append(remaining[:idx])
                remaining = remaining[idx + len(sep):]

    return sep.join(result)


# ---------------------------------------------------------------------------
# Demographics normalization
# ---------------------------------------------------------------------------
SENIORITY_ORDINAL = {
    # PT raw labels
    "Estagiário": 1,
    "Júnior (até 5 anos)": 2,
    "Pleno (6 a 9 anos)": 3,
    "Sênior (10+ anos)": 4,
    # EN raw labels
    "Trainee": 1,
    "Junior (up to 5 years)": 2,
    "Full (6 to 9 years)": 3,
    "Senior (10+ years)": 4,
}

SENIORITY_NORM = {
    # PT raw labels
    "Estagiário":             "Trainee",
    "Júnior (até 5 anos)":    "Junior (up to 5 years)",
    "Pleno (6 a 9 anos)":     "Full (6 to 9 years)",
    "Sênior (10+ anos)":      "Senior (10+ years)",
    # EN raw labels
    "Trainee": "Trainee",
    "Junior (up to 5 years)": "Junior (up to 5 years)",
    "Full (6 to 9 years)": "Full (6 to 9 years)",
    "Senior (10+ years)": "Senior (10+ years)",
}

SENIORITY_GROUP = {
    # PT raw labels
    "Estagiário": "Trainee",
    "Júnior (até 5 anos)": "Junior (up to 5 years)",
    "Pleno (6 a 9 anos)": "Full (6 to 9 years)",
    "Sênior (10+ anos)": "Senior (10+ years)",
    # EN raw labels
    "Trainee": "Trainee",
    "Junior (up to 5 years)": "Junior (up to 5 years)",
    "Full (6 to 9 years)": "Full (6 to 9 years)",
    "Senior (10+ years)": "Senior (10+ years)",
}

ROLE_GROUP = {
    # PT raw labels — Q5
    "Cientista de dados": "Data Scientist",
    "Desenvolvedor de Software (Backend, front-end, fullstack)": "Developer",
    "Engenheiro de Machine Learning": "ML Engineer",
    "Engenheiro de dados": "Data Engineer",
    "QA engineer": "QA Engineer",
    # EN raw labels — Q5
    "Data scientist": "Data Scientist",
    "Software Developer (Backend, front-end, fullstack)": "Developer",
    "Machine Learning Engineer": "ML Engineer",
    "Data engineer": "Data Engineer",
    "DevOps engineer": "DevOps Engineer",
    "Tech manager": "Tech manager",
    "Product owner": "Product owner",
    "QA engineer": "QA Engineer",
}

# Demographics normalization (language-agnostic derived columns)
GENDER_NORM = {
    "Homem": "male", "Men": "male",
    "Mulher": "female", "Woman": "female",
}

AGE_BAND = {
    "18-24 anos": "18-24", "18-24 years old": "18-24",
    "25-34 anos": "25-34", "25-34 years old": "25-34",
    "35-44 anos": "35-44", "35-44 years old": "35-44",
    "45-54 anos": "45-54", "45-54 years old": "45-54",
}

EDUCATION_NORM = {
    # PT raw labels — Q4
    "Ensino médio": "High School",
    "Ensino superior": "Undergraduate",
    "Especialização": "Specialization",
    "Estudante de Mestrado": "Master's student",
    "Mestrado": "Master",
    "Estudante de Doutorado": "Doctoral student",
    "Doutorado": "Doctorate",
    # EN raw labels — Q4
    "High school": "High School",
    "Higher education": "Undergraduate",
    "Specialization": "Specialization",
    "Master's student": "Master's student",
    "Master": "Master",
    "Doctoral student": "Doctoral student",
    "Doctorate": "Doctorate",
}

STATE_TO_UF: dict[str, str] = {
    "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM",
    "Bahia": "BA", "Ceará": "CE", "Distrito Federal": "DF", "Espírito Santo": "ES",
    "Goiás": "GO", "Maranhão": "MA", "Mato Grosso": "MT", "Mato Grosso do Sul": "MS",
    "Minas Gerais": "MG", "Pará": "PA", "Paraíba": "PB", "Paraná": "PR",
    "Pernambuco": "PE", "Piauí": "PI", "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS", "Rondônia": "RO",
    "Roraima": "RR", "Santa Catarina": "SC", "São Paulo": "SP",
    "Sergipe": "SE", "Tocantins": "TO",
}
UF_VALID = set(STATE_TO_UF.values())

UF_TO_REGION = {
    "AC": "North", "AM": "North", "AP": "North", "PA": "North",
    "RO": "North", "RR": "North", "TO": "North",
    "AL": "Northeast", "BA": "Northeast", "CE": "Northeast", "MA": "Northeast",
    "PB": "Northeast", "PE": "Northeast", "PI": "Northeast",
    "RN": "Northeast", "SE": "Northeast",
    "DF": "Central-West", "GO": "Central-West", "MT": "Central-West",
    "MS": "Central-West",
    "ES": "Southeast", "MG": "Southeast", "RJ": "Southeast", "SP": "Southeast",
    "PR": "South", "RS": "South", "SC": "South",
}
def normalize_state(value: str | float) -> str | None:
    """Map free-text state responses to a 2-letter UF code (Brazilian states)."""
    if not isinstance(value, str):
        return None
    s = value.strip()
    if not s:
        return None
    upper = s.upper()
    if upper in UF_VALID:
        return upper
    title = s.title()
    if title in STATE_TO_UF:
        return STATE_TO_UF[title]
    for full, uf in STATE_TO_UF.items():
        if full.lower() == s.lower():
            return uf
    return None


# Cells in the international form mix country + (optional) state, e.g.
# "Germany, Bavaria", "Rio de Janeiro, Brasil", "SP", "Brazil".
COUNTRY_ALIASES = {
    "brasil": "Brazil", "brazil": "Brazil",
    "germany": "Germany", "alemanha": "Germany",
    "france": "France", "frança": "France",
    "colombia": "Colombia", "colômbia": "Colombia",
    "portugal": "Portugal",
    "spain": "Spain", "espanha": "Spain",
    "usa": "United States", "united states": "United States",
    "prc": "China", "china": "China",
    "ireland": "Ireland", "irlanda": "Ireland",
    "fora, dublin/irlanda": "Ireland",
}


def parse_country_state(value: str | float) -> tuple[str | None, str | None]:
    """Return (country, UF). Country defaults to 'Brazil' when value is a Brazilian UF/state.

    Examples:
        'Germany, Bavaria' -> ('Germany', None)
        'SP' or 'Ceará'    -> ('Brazil', 'SP'/'CE')
    """
    if not isinstance(value, str):
        return (None, None)
    s = value.strip()
    if not s:
        return (None, None)

    uf = normalize_state(s)
    if uf is not None:
        return ("Brazil", uf)

    key = s.lower()
    if key in COUNTRY_ALIASES:
        return (COUNTRY_ALIASES[key], None)

    if "," in s:
        parts = [p.strip() for p in s.split(",", maxsplit=1)]
        a_uf = normalize_state(parts[0])
        b_uf = normalize_state(parts[1])
        a_country = COUNTRY_ALIASES.get(parts[0].lower())
        b_country = COUNTRY_ALIASES.get(parts[1].lower())
        if a_country == "Brazil" and b_uf is not None:
            return ("Brazil", b_uf)
        if b_country == "Brazil" and a_uf is not None:
            return ("Brazil", a_uf)
        if a_uf is not None:
            return ("Brazil", a_uf)
        if b_uf is not None:
            return ("Brazil", b_uf)
        if a_country is not None:
            return (a_country, None)
        if b_country is not None:
            return (b_country, None)
        return (parts[0].title(), None)

    return (s.title(), None)


def country_to_region(country: str | None, uf: str | None) -> str | None:
    """Macro-region for Brazilian respondents; 'International' otherwise."""
    if country == "Brazil" and isinstance(uf, str):
        return UF_TO_REGION.get(uf)
    if country is None:
        return None
    if country == "Brazil":
        return None
    return "International"

# ---------------------------------------------------------------------------
# Plot styling — color-blind safe
# ---------------------------------------------------------------------------
# Wong (2011) palette — color-blind safe; Nature recommended
PALETTE_WONG = [
    "#000000",  # black
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#F0E442",  # yellow
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#CC79A7",  # reddish purple
]

# Diverging Likert (5 levels) — RdBu-derived, color-blind aware
PALETTE_LIKERT_5 = ["#3B1F6E", "#9B72CF", "#D9D9D9", "#7BC67E", "#1A6B3C"]


def setup_matplotlib() -> None:
    """Apply default styling for the paper figures (acmart-friendly)."""
    mpl.rcParams.update({
        "font.family": "serif",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "figure.dpi": 110,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
        "axes.axisbelow": True,
    })


def save_fig(fig, name: str) -> Path:
    """Save a figure as PDF in the paper's figures folder.

    Accepts both matplotlib Figure (uses savefig) and Plotly Figure (uses
    write_image, requires kaleido).
    """
    out = FIGURES / f"{name}.pdf"
    if hasattr(fig, "write_image"):
        w = fig.layout.width or None
        h = fig.layout.height or None
        fig.write_image(str(out), width=w, height=h)
    else:
        fig.savefig(out, bbox_inches="tight")
    return out


# ---------------------------------------------------------------------------
# Loading helpers
# ---------------------------------------------------------------------------
def _read_one(path: Path, language: str) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found at {path}.")
    df = pd.read_excel(path)
    df.columns = [COLUMN_RENAME[i] for i in range(61)]

    for c in ("age", "gender", "education", "role", "seniority", "discussion_freq", "support_freq"):
        df[c] = df[c].astype("string").str.strip()
    df.insert(0, "language", language)
    return df


def load_raw() -> pd.DataFrame:
    """Concatenate the PT (national) and EN (international) forms into a single frame.
    """
    pt = _read_one(RAW_XLSX_PT, "pt")
    en = _read_one(RAW_XLSX_EN, "en")
    df = pd.concat([pt, en], ignore_index=True)
    return df


def load_anonymized() -> pd.DataFrame:
    """Read the anonymized CSV produced by notebook 01."""
    return pd.read_csv(DATA_PROC / "anonymized.csv", parse_dates=["timestamp"])


# ---------------------------------------------------------------------------
# Word-association helpers (Q9)
# ---------------------------------------------------------------------------
WORD_PT_TO_KEY: dict[str, str] = {
    "consistência":       "consistency",
    "consistencia":       "consistency",
    "completude":         "completeness",
    "confiabilidade":     "reliability",
    "precisão":           "precision",
    "precisao":           "precision",
    "balanceamento":      "balance",
    "quantidade":         "quantity",
    "atualização":        "currentness",
    "atualizacao":        "currentness",
    "outliers":           "outliers",
    "integração":         "integration",
    "integracao":         "integration",
    "normalização":       "normalization",
    "normalizacao":       "normalization",
    "relevância":         "relevance",
    "relevancia":         "relevance",
    "acurácia":           "accuracy",
    "acuracia":           "accuracy",
    "distribuição":       "distribution",
    "distribuicao":       "distribution",
    "acessibilidade":     "accessibility",
    "qualidade":          "quality",
    "qualidade de dados": "data quality",
    "confiança":          "reliability",
    "confianca":          "reliability",
    "validade":           "validity",
    "validação":          "validation",
    "validacao":          "validation",
    "integridade":        "integrity",
    "rastreabilidade":    "traceability",
    "disponibilidade":    "availability",
    "segurança":          "security",
    "seguranca":          "security",
    "privacidade":        "privacy",
    "conformidade":       "compliance",
    "processamento":      "processing",
    "pipeline":           "pipeline",
    "estrutura":          "structure",
    "volume":             "volume",
    "frescor":            "freshness",
    "atualidade":         "currentness",
    "ruído":              "noise",
    "ruido":              "noise",
    "análise":            "analysis",
    "analise":            "analysis",
    "representatividade": "representativeness",
    "proveniência":       "provenance",
    "proveniencia":       "provenance",
    "origem":             "provenance",
    "clareza":            "clarity",
    "compreensibilidade": "understandability",
    "eficiência":         "efficiency",
    "eficiencia":         "efficiency",
    "duplicatas":         "duplicates",
    "metadados":          "metadata",
    "documentação":       "documentation",
    "documentacao":       "documentation",
    "governança":         "governance",
    "governanca":         "governance",
    "monitoramento":      "monitoring",
    "auditoria":          "audit",
    "credibilidade":      "credibility",
    "recuperabilidade":   "recoverability",
    "sigilo":             "confidentiality",
    "confidencialidade":  "confidentiality",
    "criptografia":       "cryptography",
    "anonimização":       "anonymization",
    "anonimizacao":       "anonymization",
    "consentimento":      "consent",
    "controle":           "control",
    "controle de acesso": "access control",
    "pessoas":            "people",
    "lgpd":               "lgpd",
    "proteção":           "protection",
    "protecao":           "protection",
    "padronização":       "standardization",
    "padronizacao":       "standardization",
    "transformação":      "transformation",
    "transformacao":      "transformation",
    "esquema":            "schema",
    "valores ausentes":   "missing values",
    "dados faltantes":    "missing values",
    "nulos":              "null values",
    "valores nulos":      "null values",
    "observabilidade":    "observability",
    "limpeza":            "cleaning",
}

EXTRA_DISPLAY: dict[str, str] = {
    "balance":            "Balance",
    "quantity":           "Quantity",
    "outliers":           "Outliers",
    "integration":        "Integration",
    "normalization":      "Normalization",
    "relevance":          "Relevance",
    "accuracy":           "Accuracy",
    "distribution":       "Distribution",
    "quality":            "Quality",
    "data quality":       "Data Quality",
    "validity":           "Validity",
    "validation":         "Validation",
    "integrity":          "Integrity",
    "security":           "Security",
    "privacy":            "Privacy",
    "processing":         "Processing",
    "pipeline":           "Pipeline",
    "structure":          "Structure",
    "volume":             "Volume",
    "freshness":          "Freshness",
    "noise":              "Noise",
    "analysis":           "Analysis",
    "representativeness": "Representativeness",
    "provenance":         "Provenance",
    "clarity":            "Clarity",
    "duplicates":         "Duplicates",
    "metadata":           "Metadata",
    "documentation":      "Documentation",
    "governance":         "Governance",
    "monitoring":         "Monitoring",
    "audit":              "Audit",
    "cryptography":       "Cryptography",
    "anonymization":      "Anonymization",
    "consent":            "Consent",
    "control":            "Control",
    "access control":     "Access Control",
    "people":             "People",
    "lgpd":               "LGPD",
    "confidentiality":    "Confidentiality",
    "protection":         "Protection",
    "standardization":    "Standardization",
    "transformation":     "Transformation",
    "schema":             "Schema",
    "missing values":     "Missing Values",
    "null values":        "Null Values",
    "observability":      "Observability",
}

ALL_DISPLAY: dict[str, str] = {**EXTRA_DISPLAY, **CHARACTERISTICS_EN}

_INVALID_VALUES = {"", "-", "--", "n/a", "na", "none", "null", "nan"}


def normalize_to_en(word: str) -> str:
    """Portuguese data-quality word → English display label."""
    if not isinstance(word, str):
        return word
    w = word.strip().lower()
    key = WORD_PT_TO_KEY.get(w, w)
    return ALL_DISPLAY.get(key, key.capitalize())


def is_valid_word(word) -> bool:
    """False for NaN, None, empty strings, or placeholder dashes."""
    if not isinstance(word, str):
        return False
    return word.strip().lower() not in _INVALID_VALUES


# ---------------------------------------------------------------------------
# Bootstrap CI helpers
# ---------------------------------------------------------------------------
def _bootstrap_ci(
    long_df: pd.DataFrame,
    item_col: str,
    value_col: str,
    items: list,
    top_levels: list,
    bottom_levels: list,
    n_bootstrap: int = 1000,
    ci_level: float = 0.95,
    random_state: int | None = 42,
) -> pd.DataFrame:
    """Bootstrap CI for top/bottom % in a Likert long-format DataFrame."""
    rng   = np.random.default_rng(random_state)
    alpha = 1 - ci_level
    rows  = {}
    for key in items:
        s = long_df.loc[long_df[item_col] == key, value_col].dropna()
        n = len(s)
        if n == 0:
            rows[key] = dict(
                pct_top2=float("nan"), ci_lo=float("nan"), ci_hi=float("nan"),
                pct_bottom2=float("nan"), ci_bottom_lo=float("nan"), ci_bottom_hi=float("nan"),
            )
            continue
        vals        = s.values
        pct_top2    = s.isin(top_levels).mean()    * 100
        pct_bottom2 = s.isin(bottom_levels).mean() * 100
        idx         = rng.integers(0, n, size=(n_bootstrap, n))
        boot_top    = np.isin(vals[idx], top_levels).mean(axis=1)    * 100
        boot_bottom = np.isin(vals[idx], bottom_levels).mean(axis=1) * 100
        rows[key] = dict(
            pct_top2=pct_top2,
            ci_lo=np.percentile(boot_top,    100 * alpha / 2),
            ci_hi=np.percentile(boot_top,    100 * (1 - alpha / 2)),
            pct_bottom2=pct_bottom2,
            ci_bottom_lo=np.percentile(boot_bottom, 100 * alpha / 2),
            ci_bottom_hi=np.percentile(boot_bottom, 100 * (1 - alpha / 2)),
        )
    return pd.DataFrame(rows).T


def _boot_ci(
    values,
    threshold: int = 4,
    n_bootstrap: int = 1000,
    ci_level: float = 0.95,
    random_state: int = 42,
) -> tuple[float, float]:
    """Percentile bootstrap CI for the proportion of values >= threshold."""
    values = np.asarray(values)
    n = len(values)
    if n == 0:
        return float("nan"), float("nan")
    rng   = np.random.default_rng(random_state)
    alpha = 1 - ci_level
    boot_indices = rng.integers(0, n, size=(n_bootstrap, n))
    boot_props = np.mean(values[boot_indices] >= threshold, axis=1)
    return (
        np.percentile(boot_props, 100 * alpha / 2),
        np.percentile(boot_props, 100 * (1 - alpha / 2)),
    )


# ---------------------------------------------------------------------------
# Likert diverging-stacked chart
# ---------------------------------------------------------------------------
def diverging_stacked(
    long_df, item_col, value_col, item_labels, level_labels,
    figsize=(6.5, 5.5), palette=None,
    item_order=None,
    ci_df=None, ax=None, title=None,
    neg_label="Less favourable", pos_label="More favourable",
    show_pct_inside_threshold=4.0, footnote=None,
    show_ytick_labels=True,
):
    n_levels = len(level_labels)
    if palette is None:
        palette = PALETTE_LIKERT_5 if n_levels == 5 else [f"C{i}" for i in range(n_levels)]

    items      = list(item_order) if item_order is not None else list(item_labels.keys())
    items_plot = list(reversed(items))

    counts = (
        long_df.groupby(item_col)[value_col]
        .value_counts().unstack(fill_value=0)
        .reindex(index=items_plot, columns=range(1, n_levels + 1), fill_value=0)
    )
    pct = counts.div(counts.sum(axis=1), axis=0) * 100

    if n_levels == 5:
        neg_levels, neutral_lvl, pos_levels = [1, 2], 3, [4, 5]
    elif n_levels == 4:
        neg_levels, neutral_lvl, pos_levels = [1, 2], None, [3, 4]
    else:
        raise ValueError("diverging_stacked expects 4 or 5 levels")

    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    y            = np.arange(len(items_plot))
    bar_height   = 0.76
    neutral_half = (pct[neutral_lvl].values / 2) if neutral_lvl is not None \
                   else np.zeros(len(items_plot))

    cur = -(neutral_half + pct[neg_levels[1]].values + pct[neg_levels[0]].values)
    for lvl, color in zip(neg_levels, palette[:len(neg_levels)]):
        widths = pct[lvl].values
        ax.barh(y, widths, left=cur, height=bar_height,
                color=color, edgecolor="white", linewidth=0.4,
                label=level_labels[lvl - 1])
        for i, w in enumerate(widths):
            if w < show_pct_inside_threshold:
                continue
            ax.text(cur[i] + w / 2, y[i], f"{w:.0f}%",
                    ha="center", va="center", fontsize=9, color="white", fontweight="bold")
        cur += widths

    if neutral_lvl is not None:
        widths = pct[neutral_lvl].values
        ax.barh(y, widths, left=-widths / 2, height=bar_height,
                color=palette[neutral_lvl - 1], edgecolor="white", linewidth=0.4,
                label=level_labels[neutral_lvl - 1])
        for i, w in enumerate(widths):
            if w < show_pct_inside_threshold:
                continue
            ax.text(-widths[i] / 2 + w / 2, y[i], f"{w:.0f}%",
                    ha="center", va="center", fontsize=10, color="#333333")

    cur = neutral_half.copy()
    for lvl, color in zip(pos_levels, palette[-len(pos_levels):]):
        widths = pct[lvl].values
        ax.barh(y, widths, left=cur, height=bar_height,
                color=color, edgecolor="white", linewidth=0.4,
                label=level_labels[lvl - 1])
        for i, w in enumerate(widths):
            if w < show_pct_inside_threshold:
                continue
            ax.text(cur[i] + w / 2, y[i], f"{w:.0f}%",
                    ha="center", va="center", fontsize=10, color="white", fontweight="bold")
        cur += widths

    if ci_df is not None:
        ci_al  = ci_df.reindex(items_plot)
        band_h = bar_height * 0.55
        if "pct_top2" in ci_al.columns:
            x_lo = neutral_half + ci_al["ci_lo"].values
            x_hi = neutral_half + ci_al["ci_hi"].values
            ax.barh(y, x_hi - x_lo, left=x_lo, height=band_h,
                    color="#888888", alpha=0.30, zorder=5, label="95% CI")
        if "pct_bottom2" in ci_al.columns:
            x_lo = -(neutral_half + ci_al["ci_bottom_hi"].values)
            x_hi = -(neutral_half + ci_al["ci_bottom_lo"].values)
            ax.barh(y, x_hi - x_lo, left=x_lo, height=band_h,
                    color="#888888", alpha=0.30, zorder=5)

    ax.axvline(0, color="#333333", linewidth=0.7, zorder=4, linestyle="--", alpha=0.4)

    ax.set_yticks(y)
    if show_ytick_labels:
        ax.set_yticklabels([item_labels[k] for k in items_plot], fontsize=10.5)
    else:
        ax.set_yticklabels([])
        ax.tick_params(axis="y", length=0)

    ax.set_xlabel("% of responses", fontsize=10.5)
    ax.set_xlim(-50, 100)
    ax.set_xticks([-50, -25, 0, 25, 50, 75, 100])
    ax.set_xticklabels(["50%", "25%", "0", "25%", "50%", "75%", "100%"], fontsize=9.5)
    ax.tick_params(axis="x", length=3)

    ax.grid(axis="x", color="#e0e0e0", linewidth=0.5, zorder=0)
    ax.grid(axis="y", visible=False)
    ax.set_axisbelow(True)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#cccccc")
    ax.margins(x=0.01)

    ax.text(0.167, 1.01, neg_label, ha="center", va="bottom",
            fontsize=10, fontweight="bold", color=palette[0], transform=ax.transAxes)
    ax.text(0.75, 1.01, pos_label, ha="center", va="bottom",
            fontsize=10, fontweight="bold", color=palette[-1], transform=ax.transAxes)

    if title:
        ax.set_title(title, fontsize=11.5, fontweight="bold", pad=38, loc="center")

    handles, labels_leg = ax.get_legend_handles_labels()
    seen = {}
    for h, l in zip(handles, labels_leg):
        if l not in seen:
            seen[l] = h
    ax.legend(list(seen.values()), list(seen.keys()),
              loc="upper center", bbox_to_anchor=(0.5, -0.13),
              ncol=len(seen), frameon=False, fontsize=9.5,
              handlelength=1.3, handleheight=0.85,
              borderpad=0, columnspacing=0.9)

    if standalone and footnote:
        fig.text(0.01, -0.04, footnote, ha="left", va="top",
                 fontsize=8.5, color="#555555",
                 bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#cccccc", lw=0.8))

    return fig


def plot_importance_priority_combined(
    imp_long, pri_long, item_labels,
    imp_item_col="characteristic", imp_value_col="importance",
    pri_item_col="characteristic", pri_value_col="priority",
    figsize=(15.0, 6.5),
    footnote=(
        "Percentages may not sum to 100 % due to rounding.  "
        "95 % CI = 95 % confidence interval of the percentage."
    ),
    save_func=None,
):
    items   = list(item_labels.keys())
    _imp_ci = _bootstrap_ci(imp_long, imp_item_col, imp_value_col, items,
                             top_levels=[4, 5], bottom_levels=[1, 2])
    _pri_ci = _bootstrap_ci(pri_long, pri_item_col, pri_value_col, items,
                             top_levels=[4, 5], bottom_levels=[1, 2])

    fig, (ax_imp, ax_pri) = plt.subplots(1, 2, figsize=figsize,
                                          gridspec_kw={"wspace": 0.04})

    diverging_stacked(
        imp_long, item_col=imp_item_col, value_col=imp_value_col,
        item_labels=item_labels, item_order=items,
        level_labels=["Not important", "Slightly important", "Neutral",
                      "Important", "Very important"],
        ci_df=_imp_ci, ax=ax_imp,
        title="Perceived Importance of 13 Data Quality\nCharacteristics (Q11-Q12)",
        neg_label="Less important", pos_label="More important",
    )

    diverging_stacked(
        pri_long, item_col=pri_item_col, value_col=pri_value_col,
        item_labels=item_labels, item_order=items,
        level_labels=["Not a priority", "Low priority", "Neutral",
                      "High priority", "Essential"],
        ci_df=_pri_ci, ax=ax_pri,
        title="Perceived Priority of 13 Data Quality\nCharacteristics (Q13-Q14)",
        neg_label="Lower priority", pos_label="Higher priority",
        show_ytick_labels=False,
    )

    fig.text(0.01, -0.02, footnote, ha="left", va="top", fontsize=9, color="#555555",
             bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="#cccccc", lw=0.8))

    fig.tight_layout()

    if save_func is not None:
        save_func(fig, "importance_priority_diverging")

    return fig


# ---------------------------------------------------------------------------
# Spearman correlation helpers
# ---------------------------------------------------------------------------
def _salkind_strength(rho: float) -> str:
    r = abs(rho)
    if r >= 0.80:   return "Very Strong"
    elif r >= 0.60: return "Strong"
    elif r >= 0.40: return "Moderate"
    elif r >= 0.20: return "Weak"
    return "Very Weak"


def _salkind_color(val) -> str:
    if not isinstance(val, (int, float)) or pd.isna(val):
        return ""
    r = abs(val)
    if r >= 0.80:   return "background-color: #1a6b3c; color: white"
    elif r >= 0.60: return "background-color: #7bc67e"
    elif r >= 0.40: return "background-color: #ffe066"
    elif r >= 0.20: return "background-color: #e57373; color: white"
    return ""


# ---------------------------------------------------------------------------
# Checkbox parsing and proportions (Q17–Q21)
# ---------------------------------------------------------------------------
def parse_checkboxes(series: pd.Series, options: dict) -> tuple[pd.DataFrame, pd.Series]:
    """Binary-encode multi-choice checkbox fields (PT+EN aliases).

    Returns (binary df, residual series with matched text removed).
    """
    binary = pd.DataFrame(index=series.index, columns=list(options.keys()), dtype=bool)
    binary[:] = False
    residual = series.copy()
    for key, raw in options.items():
        labels = [raw] if isinstance(raw, str) else list(raw)
        present = pd.Series(False, index=series.index)
        for lab in labels:
            present = present | series.fillna("").str.contains(lab, regex=False)
            residual = residual.fillna("").str.replace(lab, "", regex=False)
        binary[key] = present
    residual = residual.str.replace(r"^[,\.\s]+|[,\.\s]+$", "", regex=True)
    residual = residual.str.replace(r"^[,\.]\s*", "", regex=True)
    residual = residual.where(residual.str.len() > 2, "")
    return binary, residual


def proportions_with_ci(binary: pd.DataFrame, labels: dict, n_total: int) -> pd.DataFrame:
    """Proportion and bootstrap CI for each binary column."""
    rows = []
    n_rows = len(binary)
    for key in binary.columns:
        vals = binary[key].astype(int).values
        lo, hi = _boot_ci(vals, threshold=1)
        rows.append({
            "key":    key,
            "label":  labels[key],
            "n":      int(binary[key].sum()),
            "pct":    binary[key].mean() * 100,
            "ci_lo":  lo * 100,
            "ci_hi":  hi * 100,
            "ci_lo_n": lo * n_rows,
            "ci_hi_n": hi * n_rows,
        })
    return pd.DataFrame(rows).sort_values("pct", ascending=False).reset_index(drop=True)


# ---------------------------------------------------------------------------
# Bar chart helpers (RQ2/3)
# ---------------------------------------------------------------------------
def ci_band_barh_plot(p: pd.DataFrame, title: str, color: str, ax) -> None:
    p_sorted = p.sort_values("pct")
    y     = np.arange(len(p_sorted))
    pct   = p_sorted["pct"].values
    ci_lo = np.clip(p_sorted["ci_lo"].values, 0, 100)
    ci_hi = np.clip(p_sorted["ci_hi"].values, 0, 100)

    ax.barh(y, pct, color=color, alpha=0.75, height=0.75)
    ax.barh(y, ci_hi - ci_lo, left=ci_lo, color="black", alpha=0.15)

    ax.set_yticks(y)
    ax.set_yticklabels(p_sorted["label"], fontsize=14)
    ax.set_xlim(0, 108)
    ax.set_xlabel("% of occurrences", fontsize=14)
    ax.set_title(title, fontsize=15)

    for i, (v, n) in enumerate(zip(pct, p_sorted["n"])):
        ax.text(min(v + 2, 106), i, f"{int(n)}", va="center", fontsize=13)


def _wrap_tick(label: str, max_chars: int = 18) -> str:
    if len(label) <= max_chars:
        return label
    words = label.split()
    mid = max(1, len(words) // 2)
    return " ".join(words[:mid]) + "\n" + " ".join(words[mid:])


def ci_band_barv_plot(p: pd.DataFrame, title: str, color: str, ax) -> None:
    p_sorted = p.sort_values("n")
    x       = np.arange(len(p_sorted))
    n_vals  = p_sorted["n"].values
    ci_lo_n = np.clip(p_sorted["ci_lo_n"].values, 0, None)
    ci_hi_n = p_sorted["ci_hi_n"].values

    ax.bar(x, n_vals, color=color, alpha=0.80, width=0.7, zorder=2)
    ax.bar(x, ci_hi_n - ci_lo_n, bottom=ci_lo_n,
           color="#888888", alpha=0.45, width=0.7, zorder=3)

    wrapped = [_wrap_tick(lbl) for lbl in p_sorted["label"]]
    ax.set_xticks(x)
    ax.set_xticklabels(wrapped, rotation=30, ha="right", fontsize=13, linespacing=1.3)

    y_max = max(float(ci_hi_n.max()), float(n_vals.max())) if len(n_vals) else 10
    ax.set_ylim(0, y_max * 1.3 + 1)
    ax.set_ylabel("Number of occurrences", fontsize=14)
    ax.set_title(title, fontsize=15)

    for i, v in enumerate(n_vals):
        ax.text(i, float(v) + y_max * 0.04, str(int(v)), ha="center", fontsize=13)


# ---------------------------------------------------------------------------
# Heatmap helpers (RQ2)
# ---------------------------------------------------------------------------
def four_question_heatmaps(questions_data, comparisons):
    import matplotlib.colors as mcolors

    n_q      = len(questions_data)
    n_panels = len(comparisons)

    items_per_q  = [len(bin_df.columns) for _, bin_df, _, _ in questions_data]
    width_ratios = [len(groups) for _, groups in comparisons] + [0.28]

    row_h = 0.40
    fig_h = sum(items_per_q) * row_h + 2.4
    fig_w = 11.5

    fig, axes = plt.subplots(
        n_q, n_panels + 1,
        figsize=(fig_w, fig_h),
        gridspec_kw={
            "height_ratios": items_per_q,
            "width_ratios":  width_ratios,
            "wspace": 0.00,
        },
        squeeze=False,
    )

    cmap = plt.get_cmap("Blues")
    MIN_INTENSITY = 0.05

    for q_idx, (q_label, bin_df, labels, source) in enumerate(questions_data):
        cols         = list(bin_df.columns)
        n_items      = len(cols)
        item_labels_ = [labels.get(c, c) for c in cols]

        global_max = 0
        panel_data = []
        for _, groups in comparisons:
            grp_counts = []
            for _, mask in groups:
                cnts = [int(bin_df.loc[mask, col].sum()) for col in cols]
                grp_counts.append(cnts)
                global_max = max(global_max, max(cnts, default=0))
            panel_data.append(grp_counts)
        if global_max == 0:
            global_max = 1

        for p_idx, (panel_title, groups) in enumerate(comparisons):
            ax       = axes[q_idx, p_idx]
            n_groups = len(groups)
            totals   = [int(mask.sum()) for _, mask in groups]

            raw = np.zeros((n_items, n_groups), dtype=int)
            mat = np.zeros((n_items, n_groups))
            for g_idx, cnts in enumerate(panel_data[p_idx]):
                for i, cnt in enumerate(cnts):
                    raw[i, g_idx] = cnt
                    mat[i, g_idx] = MIN_INTENSITY + (1 - MIN_INTENSITY) * cnt / global_max

            ax.imshow(mat, aspect="auto", cmap=cmap, vmin=0, vmax=1, interpolation="nearest")

            for i in range(n_items):
                for j in range(n_groups):
                    tc = "white" if mat[i, j] > 0.60 else "black"
                    ax.text(j, i, str(raw[i, j]),
                            ha="center", va="center", fontsize=8, color=tc)

            if p_idx == 0:
                ax.set_yticks(range(n_items))
                ax.set_yticklabels(item_labels_, fontsize=8.5)
                ax.text(0.0, 1.04, q_label, transform=ax.transAxes,
                        ha="left", va="bottom", fontsize=9.5, fontweight="bold")
            else:
                ax.set_yticks([])

            ax.set_xticks(range(n_groups))
            ax.set_xticklabels(
                [f"{groups[j][0]}\n(n={totals[j]})" for j in range(n_groups)],
                fontsize=7.5,
            )
            ax.tick_params(left=False, bottom=False)
            for sp in ax.spines.values():
                sp.set_visible(False)

            if q_idx == 0:
                ax.set_title(panel_title, fontsize=10, pad=22)

        cax  = axes[q_idx, n_panels]
        sm   = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=0, vmax=1))
        sm.set_array([])
        cbar = fig.colorbar(sm, cax=cax)

        n_ticks   = min(5, global_max + 1)
        tick_vals = np.linspace(0, global_max, n_ticks).astype(int)
        tick_pos  = MIN_INTENSITY + (1 - MIN_INTENSITY) * tick_vals / global_max
        cbar.set_ticks(tick_pos)
        cbar.set_ticklabels([str(v) for v in tick_vals], fontsize=7.5)
        cbar.ax.tick_params(labelsize=7.5)
        cbar.outline.set_edgecolor((0, 0, 0, 0.3))

        if q_idx == 0:
            cbar.set_label("Count", fontsize=8, labelpad=4)

    fig.tight_layout(pad=0.5, h_pad=2.5, w_pad=0)
    return fig


def four_question_heatmaps_2x2(
    questions_data,
    comparisons,
    row_h=0.65,
    col_w=1.35,
    left_pad=1.6,
    right_pad=0.05,
    top_pad=0.10,
    bot_pad=1.4,
    mid_gap=0.8,
    row_gap=0.5,
    fs_cell=23,
    fs_xtick=18,
    fs_ytick=18,
    fs_panel_title=21,
    fs_question_title=20,
    fs_colorbar=20,
    question_title_pad=40,
    wrap_threshold=24,
    min_intensity=0.05,
):
    import matplotlib.colors as mcolors

    def _wrap_label(text, max_len):
        if len(text) <= max_len:
            return text
        words = text.split()
        half = len(words) // 2
        return " ".join(words[:half]) + "\n" + " ".join(words[half:])

    def _hamilton_round(proportions):
        pct     = np.asarray(proportions, dtype=float) * 100
        floored = np.floor(pct).astype(int)
        deficit = 100 - floored.sum()
        if deficit > 0:
            idx = np.argsort(-(pct - floored))[:deficit]
            floored[idx] += 1
        elif deficit < 0:
            idx = np.argsort(pct - floored)[:(-deficit)]
            floored[idx] -= 1
        return floored

    all_groups       = []
    panel_boundaries = []

    for p_idx, (_, groups) in enumerate(comparisons):
        panel_boundaries.append(len(all_groups))
        for g_label, mask in groups:
            all_groups.append((g_label, mask, p_idx))

    n_cols = len(all_groups)
    totals = [int(mask.sum()) for _, mask, _ in all_groups]
    cmap   = plt.get_cmap("Blues")

    items_per_q   = [len(bin_df.columns) for _, bin_df, _, _ in questions_data]
    hm_w          = n_cols * col_w
    max_items_row0 = max(items_per_q[0], items_per_q[1])
    max_items_row1 = max(items_per_q[2], items_per_q[3])
    hm_h_row0     = max_items_row0 * row_h
    hm_h_row1     = max_items_row1 * row_h
    fig_w = left_pad + hm_w + mid_gap + hm_w + right_pad
    fig_h = top_pad + hm_h_row0 + row_gap + hm_h_row1 + bot_pad

    fig = plt.figure(figsize=(fig_w, fig_h))

    def ax_rect(left_in, bottom_in, w_in, h_in):
        return [left_in / fig_w, bottom_in / fig_h, w_in / fig_w, h_in / fig_h]

    hm1_bot  = bot_pad
    hm0_bot  = bot_pad + hm_h_row1 + row_gap
    hm_left0 = left_pad
    hm_left1 = left_pad + hm_w + mid_gap

    layout = {
        0: (hm_left0, hm0_bot, hm_h_row0),
        1: (hm_left1, hm0_bot, hm_h_row0),
        2: (hm_left0, hm1_bot, hm_h_row1),
        3: (hm_left1, hm1_bot, hm_h_row1),
    }

    for q_idx, (q_label, bin_df, labels, source) in enumerate(questions_data):
        lx, by, hm_h = layout[q_idx]
        ax = fig.add_axes(ax_rect(lx, by, hm_w, hm_h))

        cols_q  = list(bin_df.columns)
        n_items = len(cols_q)
        item_labels_wrapped = [_wrap_label(labels.get(c, c), wrap_threshold) for c in cols_q]

        raw_counts = np.zeros((n_items, n_cols), dtype=int)
        for c_idx, (_, mask, _) in enumerate(all_groups):
            for i, col_name in enumerate(cols_q):
                raw_counts[i, c_idx] = int(bin_df.loc[mask, col_name].sum())

        raw_pct = np.zeros((n_items, n_cols))
        for p_idx, (_, groups) in enumerate(comparisons):
            p_col_idxs  = [ci for ci, (_, _, pi) in enumerate(all_groups) if pi == p_idx]
            panel_total = raw_counts[:, p_col_idxs].sum()
            if panel_total == 0:
                panel_total = 1
            for ci in p_col_idxs:
                raw_pct[:, ci] = raw_counts[:, ci] / panel_total

        display_int = np.zeros((n_items, n_cols), dtype=int)
        for p_idx, (_, groups) in enumerate(comparisons):
            p_col_idxs = [ci for ci, (_, _, pi) in enumerate(all_groups) if pi == p_idx]
            panel_flat = raw_pct[:, p_col_idxs].flatten()
            display_int[:, p_col_idxs] = _hamilton_round(panel_flat).reshape(
                n_items, len(p_col_idxs)
            )

        q_max   = raw_pct.max() if raw_pct.max() > 0 else 1
        pct_mat = min_intensity + (1 - min_intensity) * (raw_pct / q_max)

        ax.imshow(pct_mat, aspect="auto", cmap=cmap, vmin=0, vmax=1, interpolation="nearest")
        ax.grid(False)

        for i in range(n_items):
            for j in range(n_cols):
                tc = "white" if pct_mat[i, j] > 0.60 else "black"
                ax.text(j, i, f"{display_int[i, j]}%",
                        ha="center", va="center", fontsize=fs_cell, color=tc)

        for pb in panel_boundaries[1:]:
            ax.axvline(pb - 0.5, color="white", linewidth=4, zorder=5)

        ax.set_yticks(range(n_items))
        ax.set_yticklabels(item_labels_wrapped, fontsize=fs_ytick)
        if q_idx in [1, 3]:
            ax.yaxis.tick_right()
            ax.yaxis.set_label_position("right")
        if q_idx in [2, 3]:
            ax.set_xticks(range(n_cols))
            ax.set_xticklabels(
                [f"{g_label}\n(n={totals[ci]})" for ci, (g_label, _, _) in enumerate(all_groups)],
                fontsize=fs_xtick,
            )
        else:
            ax.set_xticks([])

        ax.tick_params(left=False, bottom=False)
        for sp in ax.spines.values():
            sp.set_visible(False)

        if q_idx in [0, 1]:
            for p_idx2, (p_title, _) in enumerate(comparisons):
                p_col_idxs = [ci for ci, (_, _, pi) in enumerate(all_groups) if pi == p_idx2]
                center     = np.mean(p_col_idxs)
                ax.text(center, 1.04, p_title,
                        transform=ax.get_xaxis_transform(),
                        ha="center", va="bottom",
                        fontsize=fs_panel_title, color="#333333", clip_on=False)

        _title_pad = question_title_pad if q_idx in [0, 1] else 6
        ax.set_title(q_label, fontsize=fs_question_title, fontweight="bold",
                     loc="left", pad=_title_pad)

    cb_h      = 0.03
    cb_bottom = 0.25 / fig_h
    cb_left_f = left_pad / fig_w
    cb_width  = (hm_left1 + hm_w - left_pad) / fig_w

    cax = fig.add_axes([cb_left_f, cb_bottom, cb_width, cb_h])
    sm  = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=0, vmax=1))
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cax, orientation="horizontal")

    tick_pcts = [0.0, 0.25, 0.50, 0.75, 1.0]
    tick_pos  = [min_intensity + (1 - min_intensity) * p for p in tick_pcts]
    cbar.set_ticks(tick_pos)
    cbar.set_ticklabels([f"{int(p * 100)}%" for p in tick_pcts], fontsize=fs_colorbar)
    cbar.ax.tick_params(labelsize=fs_colorbar)
    cbar.outline.set_linewidth(0.5)
    cbar.set_label("% of respondents within each profile", fontsize=fs_colorbar + 2, labelpad=6)

    return fig


# ---------------------------------------------------------------------------
# Survey question options and display labels (Q17–Q22)
# ---------------------------------------------------------------------------
Q17_OPTIONS: dict[str, list[str]] = {
    "q17_initial_eval": [
        "Avaliação inicial durante a coleta e preparação de dados",
        "Initial assessment during data collection and preparation",
    ],
    "q17_continuous_mon": [
        "Monitoramento contínuo durante todo o ciclo de vida do modelo",
        "Continuous monitoring throughout the model's life cycle",
    ],
    "q17_test_sets": [
        "Conjuntos de testes são aplicados para validar a consistência, completude e precisão dos dados antes de serem usados no treinamento.",
        "Test sets are applied to validate the consistency, completeness and accuracy of the data before it is used for training.",
    ],
    "q17_no_strategy": [
        "Não existe uma estratégia formal para assegurar a qualidade dos dados durante o desenvolvimento.",
        "There is no formal strategy to ensure data quality during development.",
        "There is no formal strategy for ensuring data quality during development",
        "There is no formal strategy for ensuring data quality during development.",
    ],
}
Q17_LABELS: dict[str, str] = {
    "q17_initial_eval":   "Initial assessment in collection/preparation",
    "q17_continuous_mon": "Continuous monitoring across lifecycle",
    "q17_test_sets":      "Test sets before training",
    "q17_no_strategy":    "No formal strategy",
}

Q18_OPTIONS: dict[str, list[str]] = {
    "q18_ab_tests":      ["Testes A/B", "A/B testing"],
    "q18_perf_metrics":  [
        "Análise de métricas de performance (ex.: precisão, recall)",
        "Analysis of performance metrics (e.g. precision, recall)",
    ],
    "q18_manual_review": ["Revisão manual dos resultados", "Manual review of results"],
}
Q18_LABELS: dict[str, str] = {
    "q18_ab_tests":      "A/B testing",
    "q18_perf_metrics":  "Performance metrics",
    "q18_manual_review": "Manual review of results",
}

Q19_LABELS: dict[str, str] = {
    "q19_never":     "Never",
    "q19_rarely":    "<1x/month",
    "q19_sometimes": "1x/month to <1x/week",
    "q19_often":     "≥1x/week",
    "q19_always":    "Daily",
}

Q20_OPTIONS: dict[str, list[str]] = {
    "q20_structured_text":  ["Linguagem estruturada (texto)", "Structured language (text)"],
    "q20_pm_tools":         [
        "Ferramentas de Gerenciamento de Projetos (Jira, Trello ou Asana)",
        "Project management tools (Jira, Trello or Asana)",
    ],
    "q20_central_docs":     [
        "Documentação Centralizada (Sistemas como Confluence, Google Docs ou Notion)",
        "Centralized documentation (systems such as Confluence, Google Docs or Notion)",
    ],
    "q20_alignment_meet":   ["Reuniões de Alinhamento", "Alignment meetings"],
    "q20_periodic_reports": ["Relatórios Periódicos", "Periodic reports"],
}
Q20_LABELS: dict[str, str] = {
    "q20_structured_text":  "Structured language",
    "q20_pm_tools":         "Project management tools",
    "q20_central_docs":     "Centralized documentation",
    "q20_alignment_meet":   "Alignment meetings",
    "q20_periodic_reports": "Periodic reports",
}

Q21_OPTIONS: dict[str, list[str]] = {
    "q21_inconsistency": [
        "Inconsistência entre diferentes fontes de dados",
        "Inconsistency between different data sources",
    ],
    "q21_incompleteness":    ["Dados incompletos ou ausentes", "Incomplete or missing data"],
    "q21_no_standard": [
        "Falta de padronização nos formatos de dados",
        "Lack of standardization in data formats",
    ],
    "q21_outdated":          ["Dados desatualizados ou não confiáveis", "Outdated or unreliable data"],
    "q21_collection_errors": [
        "Erros introduzidos durante a coleta e processamento",
        "Errors introduced during collection and processing",
    ],
    "q21_traceability": [
        "Dificuldade na rastreabilidade e versionamento dos dados",
        "Difficulty in data traceability and versioning",
    ],
    "q21_no_tools": [
        "Falta de ferramentas adequadas para validação da qualidade dos dados",
        "Lack of adequate tools for validating data quality",
    ],
}
Q21_LABELS: dict[str, str] = {
    "q21_inconsistency":     "Inconsistency across sources",
    "q21_incompleteness":    "Incomplete/missing data",
    "q21_no_standard":       "Lack of format standardization",
    "q21_outdated":          "Outdated/unreliable data",
    "q21_collection_errors": "Errors in collection and processing",
    "q21_traceability":      "Difficulty in traceability/versioning",
    "q21_no_tools":          "Lack of validation tools",
}

Q22_ORDER: list[int] = [4, 3, 2, 1, 0]
Q22_LABELS: list[str] = ["Always", "Often", "Occasionally", "Rarely", "Never"]

