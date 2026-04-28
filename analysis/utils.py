"""Funções e constantes compartilhadas entre notebooks de análise."""
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
FIGURES = ROOT / "2026-Research-paper" / "figures"
RAW_XLSX_PT = DATA_RAW / "survey_responses.xlsx"
RAW_XLSX_EN = DATA_RAW / "survey_responses_2.xlsx"
RAW_XLSX = RAW_XLSX_PT  # legacy alias

for p in (DATA_PROC, DATA_CODEBOOK, FIGURES):
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
    # Q8 — habilidade em processamento (10 itens)
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
    # Q9 — 5 palavras associadas a qualidade de dados
    19: "word_1",
    20: "word_2",
    21: "word_3",
    22: "word_4",
    23: "word_5",
    # Q10 — experiência em ER (aberta)
    24: "re_experience",
    # Q11 — importância (13 características)
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
    # Q12 — justificativa importância
    38: "imp_justification",
    # Q13 — prioridade (13 características, mesma ordem)
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
    # Q14 — justificativa prioridade
    52: "pri_justification",
    # Q15-Q22 — abertas e Likerts de frequência
    53: "balance_open",
    54: "versioning_open",
    55: "incorporation_open",
    56: "measurement_open",
    57: "discussion_freq",
    58: "documentation_open",
    59: "challenges_open",
    60: "support_freq",
    # Q23 — email (DROP por privacidade)
    61: "_email_drop",
}

SKILL_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("skill_")]
WORD_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("word_")]
IMP_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("imp_") and v != "imp_justification"]
PRI_COLS = [v for k, v in COLUMN_RENAME.items() if v.startswith("pri_") and v != "pri_justification"]

CHARACTERISTICS_PT = {
    "precision": "Precisão",
    "completeness": "Completude",
    "consistency": "Consistência",
    "credibility": "Credibilidade",
    "currentness": "Atualidade",
    "accessibility": "Acessibilidade",
    "compliance": "Conformidade",
    "reliability": "Confiabilidade",
    "efficiency": "Eficiência",
    "traceability": "Rastreabilidade",
    "understandability": "Compreensibilidade",
    "availability": "Disponibilidade",
    "recoverability": "Recuperabilidade",
}

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

SKILL_LABELS_PT = {
    "skill_cleaning": "Limpeza de dados",
    "skill_normalization": "Normalização/padronização",
    "skill_outliers": "Detecção de outliers",
    "skill_integration": "Integração de fontes",
    "skill_transformation": "Transformação (PCA, encoding)",
    "skill_validation": "Validação de dados",
    "skill_pipelines": "Automação de pipelines",
    "skill_monitoring": "Monitoramento em produção",
    "skill_libs": "Bibliotecas (Pandas, etc)",
    "skill_split": "Divisão treino/teste",
}

# ---------------------------------------------------------------------------
# Likert mappings
# ---------------------------------------------------------------------------
SKILL_MAP = {
    # PT
    "Muito baixa": 1, "Muito baixo": 1,
    "Abaixo da Média": 2, "Abaixo da média": 2,
    "Média": 3,
    "Acima da média": 4, "Acima da Média": 4,
    "Muito alto": 5, "Muito alta": 5,
    "Não se aplica": pd.NA,
    # EN
    "Very low": 1,
    "Below average": 2,
    "Average": 3,
    "Above average": 4,
    "Very high": 5,
    "Not applicable": pd.NA,
}
SKILL_LABELS_ORDER = ["Muito baixa", "Abaixo da média", "Média", "Acima da média", "Muito alto"]

IMPORTANCE_MAP = {
    # PT
    "Nada importante": 1,
    "Pouco importante": 2,
    "Neutro": 3,
    "Importante": 4,
    "Muito importante": 5,
    # EN
    "Not important": 1,
    "Slightly important": 2,
    "Neutral": 3,
    "Important": 4,
    "Very important": 5,
}
IMPORTANCE_LABELS_ORDER = ["Nada importante", "Pouco importante", "Neutro", "Importante", "Muito importante"]

PRIORITY_MAP = {
    # PT
    "Não é uma prioridade": 1, "Sem prioridade": 1,
    "Baixa prioridade": 2,
    "Neutro": 3,
    "Alta prioridade": 4,
    "Essencial": 5,
    # EN
    "No priority": 1, "Not a priority": 1,
    "Low priority": 2,
    "High priority": 4,
    "Essential": 5,
}
PRIORITY_LABELS_ORDER = ["Sem prioridade", "Baixa prioridade", "Neutro", "Alta prioridade", "Essencial"]

DISCUSSION_FREQ_MAP = {
    # PT
    "Nunca": 1,
    "Menos de uma vez por mês": 2,
    "Menos de uma vez por semana, mas pelo menos uma vez por mês": 3,
    "Pelo menos uma vez por semana, mas não todos os dias": 4,
    "Todos os dias": 5,
    # EN
    "Never": 1,
    "Less than once a month": 2,
    "Less than once a week, but at least once a month": 3,
    "At least once a week, but not every day": 4,
    "Every day": 5,
}

SUPPORT_FREQ_MAP = {
    # PT
    "Raramente": 1,
    "Ocasionalmente": 2,
    "Frequentemente": 3,
    "Sempre": 4,
    # EN
    "Rarely": 1,
    "Occasionally": 2,
    "Often": 3,
    "Always": 4,
}

# ---------------------------------------------------------------------------
# Demographics normalization
# ---------------------------------------------------------------------------
SENIORITY_ORDINAL = {
    # PT
    "Estagiário": 1,
    "Júnior (até 5 anos)": 2,
    "Pleno (6 a 9 anos)": 3,
    "Sênior (10+ anos)": 4,
    # EN
    "Intern": 1,
    "Junior (up to 5 years)": 2,
    "Mid (6 to 9 years)": 3,
    "Senior (10+ years)": 4,
}

# Sêniores (>= mid) vs Juniores
SENIORITY_GROUP = {
    # PT
    "Estagiário": "junior",
    "Júnior (até 5 anos)": "junior",
    "Pleno (6 a 9 anos)": "senior",
    "Sênior (10+ anos)": "senior",
    # EN
    "Intern": "junior",
    "Junior (up to 5 years)": "junior",
    "Mid (6 to 9 years)": "senior",
    "Senior (10+ years)": "senior",
}

ROLE_GROUP = {
    # PT
    "Cientista de dados": "data_scientist",
    "Desenvolvedor de Software (Backend, front-end, fullstack)": "developer",
    "Engenheiro de Machine Learning": "ml_engineer",
    "Engenheiro de dados": "data_engineer",
    "Product owner": "other",
    "Gerente de Dados e IA": "manager",
    "Pesquisador e Desenvolvedor Fullstack": "developer",
    "Pesquisador": "researcher",
    # EN
    "Data scientist": "data_scientist",
    "Software Developer (Backend, front-end, fullstack)": "developer",
    "Machine Learning Engineer": "ml_engineer",
    "Data engineer": "data_engineer",
    "Researcher": "researcher",
    "Data and AI Manager": "manager",
}

# Demographics normalization (language-agnostic derived columns)
GENDER_NORM = {
    "Homem": "male", "Men": "male", "Man": "male",
    "Mulher": "female", "Woman": "female",
    "Outro": "other", "Other": "other",
    "Prefiro não responder": "undisclosed", "Prefer not to say": "undisclosed",
}

AGE_BAND = {
    "18-24 anos": "18-24", "18-24 years old": "18-24",
    "25-34 anos": "25-34", "25-34 years old": "25-34",
    "35-44 anos": "35-44", "35-44 years old": "35-44",
    "45-54 anos": "45-54", "45-54 years old": "45-54",
    "55-64 anos": "55-64", "55-64 years old": "55-64",
    "65+ anos": "65+", "65+ years old": "65+",
}

EDUCATION_NORM = {
    # PT
    "Ensino médio": "high_school",
    "Ensino superior": "undergraduate",
    "Estudante de Mestrado": "ms_student",
    "Mestrado": "master",
    "Estudante de Doutorado": "phd_student",
    "Doutorado": "doctorate",
    "Especialização": "specialization",
    # EN
    "High school": "high_school",
    "Undergraduate": "undergraduate", "Higher education": "undergraduate",
    "Master's student": "ms_student",
    "Master": "master",
    "Doctoral student": "phd_student",
    "Doctorate": "doctorate",
    "Specialization": "specialization",
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
    "AC": "Norte", "AM": "Norte", "AP": "Norte", "PA": "Norte",
    "RO": "Norte", "RR": "Norte", "TO": "Norte",
    "AL": "Nordeste", "BA": "Nordeste", "CE": "Nordeste", "MA": "Nordeste",
    "PB": "Nordeste", "PE": "Nordeste", "PI": "Nordeste",
    "RN": "Nordeste", "SE": "Nordeste",
    "DF": "Centro-Oeste", "GO": "Centro-Oeste", "MT": "Centro-Oeste",
    "MS": "Centro-Oeste",
    "ES": "Sudeste", "MG": "Sudeste", "RJ": "Sudeste", "SP": "Sudeste",
    "PR": "Sul", "RS": "Sul", "SC": "Sul",
}


def normalize_state(value: str | float) -> str | None:
    """Mapeia respostas livres de estado para UF (sigla 2 letras)."""
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
    "brasil": "Brasil", "brazil": "Brasil",
    "germany": "Germany", "alemanha": "Germany",
    "france": "France", "frança": "France",
    "colombia": "Colombia", "colômbia": "Colombia",
    "portugal": "Portugal",
    "spain": "Spain", "espanha": "Spain",
}


def parse_country_state(value: str | float) -> tuple[str | None, str | None]:
    """Devolve (country, UF). País 'Brasil' assumido quando string é UF/estado BR.

    Para entradas tipo 'Germany, Bavaria' devolve ('Germany', None).
    Para 'SP' ou 'Ceará' devolve ('Brasil', 'SP'/'CE').
    """
    if not isinstance(value, str):
        return (None, None)
    s = value.strip()
    if not s:
        return (None, None)

    # Try direct UF or BR state name first
    uf = normalize_state(s)
    if uf is not None:
        return ("Brasil", uf)

    # Try country-only token
    key = s.lower()
    if key in COUNTRY_ALIASES:
        return (COUNTRY_ALIASES[key], None)

    # Two-part "Country, State" or "State, Country"
    if "," in s:
        parts = [p.strip() for p in s.split(",", maxsplit=1)]
        a_uf = normalize_state(parts[0])
        b_uf = normalize_state(parts[1])
        a_country = COUNTRY_ALIASES.get(parts[0].lower())
        b_country = COUNTRY_ALIASES.get(parts[1].lower())
        if a_country == "Brasil" and b_uf is not None:
            return ("Brasil", b_uf)
        if b_country == "Brasil" and a_uf is not None:
            return ("Brasil", a_uf)
        if a_uf is not None:
            return ("Brasil", a_uf)
        if b_uf is not None:
            return ("Brasil", b_uf)
        if a_country is not None:
            return (a_country, None)
        if b_country is not None:
            return (b_country, None)
        # Unknown country, keep first token capitalized
        return (parts[0].title(), None)

    return (s.title(), None)


def country_to_region(country: str | None, uf: str | None) -> str | None:
    """Macroregião BR para respondentes nacionais; 'Internacional' caso contrário."""
    if country == "Brasil" and isinstance(uf, str):
        return UF_TO_REGION.get(uf)
    if country is None:
        return None
    if country == "Brasil":
        return None
    return "Internacional"


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
    """Aplica config padrão pros gráficos do paper (acmart)."""
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


def save_fig(fig: plt.Figure, name: str) -> Path:
    """Salva figura em PDF na pasta de figures do paper."""
    out = FIGURES / f"{name}.pdf"
    fig.savefig(out, bbox_inches="tight")
    return out


# ---------------------------------------------------------------------------
# Loading helpers
# ---------------------------------------------------------------------------
def _read_one(path: Path, language: str, expected_cols: int) -> pd.DataFrame:
    df = pd.read_excel(path)
    if expected_cols == 63:
        # PT form has artefato @dropdown como última coluna; descarta antes do rename.
        df = df.iloc[:, :62]
    if df.shape[1] != 62:
        raise ValueError(f"{path.name}: esperado 62 cols após drop, obtido {df.shape[1]}")
    df.columns = [COLUMN_RENAME[i] for i in range(62)]
    df.insert(0, "language", language)
    return df


def load_raw() -> pd.DataFrame:
    """Concatena formulários PT (nacional) e EN (internacional) num único frame.

    PT bruto: 32 × 63 (col extra `@dropdown` removida). EN bruto: 9 × 62.
    Saída: 41 × 63 (62 cols originais + `language`).
    """
    pt = _read_one(RAW_XLSX_PT, "pt", expected_cols=63)
    en = _read_one(RAW_XLSX_EN, "en", expected_cols=62)
    df = pd.concat([pt, en], ignore_index=True)
    if df.shape != (41, 63):
        raise ValueError(f"Esperado (41, 63), obtido {df.shape}")
    return df


def load_anonymized() -> pd.DataFrame:
    """Lê CSV anonimizado já processado (output do notebook 01)."""
    return pd.read_csv(DATA_PROC / "anonymized.csv", parse_dates=["timestamp"])


# ---------------------------------------------------------------------------
# Stats helpers
# ---------------------------------------------------------------------------
def wilson_ci(successes: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    """Intervalo de confiança Wilson (95%) para proporção. Mais robusto que normal pra n pequeno."""
    from statsmodels.stats.proportion import proportion_confint
    if n == 0:
        return (float("nan"), float("nan"))
    return proportion_confint(successes, n, alpha=1 - conf, method="wilson")


def cliffs_delta(x, y) -> tuple[float, str]:
    """Cliff's Delta (effect size não-paramétrico) + classificação Romano et al. (2006)."""
    import numpy as np
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]
    if len(x) == 0 or len(y) == 0:
        return (float("nan"), "undefined")
    greater = sum((xi > yi) for xi in x for yi in y)
    less = sum((xi < yi) for xi in x for yi in y)
    delta = (greater - less) / (len(x) * len(y))
    a = abs(delta)
    if a < 0.147:
        magnitude = "negligible"
    elif a < 0.33:
        magnitude = "small"
    elif a < 0.474:
        magnitude = "medium"
    else:
        magnitude = "large"
    return float(delta), magnitude
