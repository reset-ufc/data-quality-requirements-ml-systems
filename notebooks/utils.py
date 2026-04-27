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
FIGURES = ROOT / "figures"
RAW_XLSX = DATA_RAW / "survey_responses.xlsx"

for p in (DATA_RAW, DATA_PROC, DATA_CODEBOOK, FIGURES):
    p.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Schema: column index in original XLSX -> short name
# 32 rows x 63 columns confirmed
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
    62: "_dropdown_drop",
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
    "Muito baixa": 1,
    "Muito baixo": 1,
    "Abaixo da Média": 2,
    "Abaixo da média": 2,
    "Média": 3,
    "Acima da média": 4,
    "Acima da Média": 4,
    "Muito alto": 5,
    "Muito alta": 5,
    "Não se aplica": pd.NA,
}
SKILL_LABELS_ORDER = ["Muito baixa", "Abaixo da média", "Média", "Acima da média", "Muito alto"]

IMPORTANCE_MAP = {
    "Nada importante": 1,
    "Pouco importante": 2,
    "Neutro": 3,
    "Importante": 4,
    "Muito importante": 5,
}
IMPORTANCE_LABELS_ORDER = list(IMPORTANCE_MAP.keys())

PRIORITY_MAP = {
    "Não é uma prioridade": 1,
    "Sem prioridade": 1,
    "Baixa prioridade": 2,
    "Neutro": 3,
    "Alta prioridade": 4,
    "Essencial": 5,
}
PRIORITY_LABELS_ORDER = list(PRIORITY_MAP.keys())

DISCUSSION_FREQ_MAP = {
    "Nunca": 1,
    "Menos de uma vez por mês": 2,
    "Menos de uma vez por semana, mas pelo menos uma vez por mês": 3,
    "Pelo menos uma vez por semana, mas não todos os dias": 4,
    "Todos os dias": 5,
}

SUPPORT_FREQ_MAP = {
    "Raramente": 1,
    "Ocasionalmente": 2,
    "Frequentemente": 3,
    "Sempre": 4,
}

# ---------------------------------------------------------------------------
# Demographics normalization
# ---------------------------------------------------------------------------
SENIORITY_ORDINAL = {
    "Estagiário": 1,
    "Júnior (até 5 anos)": 2,
    "Pleno (6 a 9 anos)": 3,
    "Sênior (10+ anos)": 4,
}

# Sêniores (>= mid) vs Juniores
SENIORITY_GROUP = {
    "Estagiário": "junior",
    "Júnior (até 5 anos)": "junior",
    "Pleno (6 a 9 anos)": "senior",
    "Sênior (10+ anos)": "senior",
}

ROLE_GROUP = {
    "Cientista de dados": "data_scientist",
    "Desenvolvedor de Software (Backend, front-end, fullstack)": "developer",
    "Engenheiro de Machine Learning": "ml_engineer",
    "Engenheiro de dados": "data_engineer",
    "Product owner": "other",
    "Gerente de Dados e IA": "manager",
    "Pesquisador e Desenvolvedor Fullstack": "developer",
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
def load_raw() -> pd.DataFrame:
    """Lê XLSX bruto e renomeia colunas via índice (mais robusto que match por string)."""
    if not RAW_XLSX.exists():
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado em {RAW_XLSX}. "
            "Verifique se data/raw/survey_responses.xlsx está presente."
        )
    df = pd.read_excel(RAW_XLSX, sheet_name="Respostas ao formulário 1")
    if df.shape != (32, 63):
        raise ValueError(f"Esperado (32, 63), obtido {df.shape}")
    df.columns = [COLUMN_RENAME[i] for i in range(len(df.columns))]
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
    return float(delta), classify_cliffs_delta(delta)


def classify_cliffs_delta(delta: float) -> str:
    """Classificação Romano et al. (2006) para |delta|."""
    a = abs(delta)
    if a != a:  # NaN
        return "undefined"
    if a < 0.147:
        return "negligible"
    if a < 0.33:
        return "small"
    if a < 0.474:
        return "medium"
    return "large"


# ---------------------------------------------------------------------------
# Paired tests (Wilcoxon signed-rank + matched-pairs rank-biserial)
# ---------------------------------------------------------------------------
def wilcoxon_paired(g1, g2) -> dict:
    """Wilcoxon signed-rank pareado + matched-pairs rank-biserial r (Kerby 2014).

    H0: distribuição de g1 - g2 é simétrica em torno de zero.
    Effect size: r_rb = (W_pos - W_neg) / (W_pos + W_neg) ∈ [-1, 1].
    Classificação aproximada: |r| < 0.1 negligible, < 0.3 small, < 0.5 medium, ≥ 0.5 large.
    """
    import numpy as np
    from scipy import stats as sp_stats

    a = pd.Series(g1).reset_index(drop=True)
    b = pd.Series(g2).reset_index(drop=True)
    paired = pd.concat([a, b], axis=1).dropna()
    n = len(paired)
    if n < 5:
        return {"W": float("nan"), "p": float("nan"), "r_rb": float("nan"),
                "n": n, "magnitude": "insufficient", "med_diff": float("nan")}

    diffs = (paired.iloc[:, 0] - paired.iloc[:, 1]).to_numpy()
    nonzero = diffs[diffs != 0]
    if len(nonzero) == 0:
        return {"W": float("nan"), "p": 1.0, "r_rb": 0.0,
                "n": n, "magnitude": "negligible", "med_diff": 0.0}

    ranks = sp_stats.rankdata(np.abs(nonzero))
    w_pos = float(ranks[nonzero > 0].sum())
    w_neg = float(ranks[nonzero < 0].sum())
    r_rb = (w_pos - w_neg) / (w_pos + w_neg) if (w_pos + w_neg) > 0 else 0.0

    res = sp_stats.wilcoxon(paired.iloc[:, 0], paired.iloc[:, 1],
                            zero_method="wilcox", alternative="two-sided")

    ar = abs(r_rb)
    if ar < 0.1:
        magnitude = "negligible"
    elif ar < 0.3:
        magnitude = "small"
    elif ar < 0.5:
        magnitude = "medium"
    else:
        magnitude = "large"

    return {"W": float(res.statistic), "p": float(res.pvalue), "r_rb": float(r_rb),
            "n": n, "magnitude": magnitude, "med_diff": float(pd.Series(diffs).median())}
