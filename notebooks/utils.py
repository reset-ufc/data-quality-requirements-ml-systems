"""Shared functions and constants used across the analysis notebooks."""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
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
PALETTE_LIKERT_5 = ["#762a83", "#af8dc3", "#f7f7f7", "#7fbf7b", "#1b7837"]


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
def _read_one(path: Path, language: str, has_dropdown_artefact: bool) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found at {path}.")
    df = pd.read_excel(path)
    if has_dropdown_artefact:
        df = df.iloc[:, :62]
    if df.shape[1] != 62:
        raise ValueError(f"{path.name}: expected 62 cols, got {df.shape[1]}")
    df.columns = [COLUMN_RENAME[i] for i in range(62)]
    # Strip trailing whitespace on categorical columns (Forms occasionally leaves
    # extra spaces in option labels, e.g. "Machine Learning Engineer ").
    for c in ("age", "gender", "education", "role", "seniority", "discussion_freq", "support_freq"):
        df[c] = df[c].astype("string").str.strip()
    df.insert(0, "language", language)
    return df


def load_raw() -> pd.DataFrame:
    """Concatenate the PT (national) and EN (international) forms into a single frame.
    Output: N × 63 (62 original cols + `language`).
    """
    pt = _read_one(RAW_XLSX_PT, "pt", has_dropdown_artefact=True)
    en = _read_one(RAW_XLSX_EN, "en", has_dropdown_artefact=False)
    df = pd.concat([pt, en], ignore_index=True)
    return df


def load_anonymized() -> pd.DataFrame:
    """Read the anonymized CSV produced by notebook 01."""
    return pd.read_csv(DATA_PROC / "anonymized.csv", parse_dates=["timestamp"])

