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
│   ├── 02_descriptive.ipynb                   # Fase 3 (descritiva)
│   ├── 03_inferential.ipynb                   # Fase 4 (inferencial)
│   ├── 04a_multiple_choice.ipynb              # Q17/Q18/Q20/Q21 + meta-finding Q16
│   ├── 04b_qualitative.ipynb                  # Grounded Theory + lematização Q9
│   └── utils.py                               # paleta, paths, helpers
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
```

Tempo total esperado: ~3 minutos.

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
| Figura — palavras Q9 por posição | `04b_qualitative.ipynb` | seção 1 |
| Tabela inferencial | `03_inferential.ipynb` | seção 6 |
| Figura — Q17/Q18 implementação | `04a_multiple_choice.ipynb` | seção 4 |
| Figura — Q20/Q21 desafios | `04a_multiple_choice.ipynb` | seção 4 |
| Tabela implementação | `04a_multiple_choice.ipynb` | seção 5 |
| Codebook qualitativo | `04b_qualitative.ipynb` | seção 7 |

## 4. Anonimização

- Coluna **e-mail (Q23)**: removida (15 de 32 respondentes informaram e-mail). Não é redistribuída.
- Coluna **`@dropdown`**: artefato vazio do Google Forms, removido.
- **Estado**: padronizado para sigla UF de duas letras + região derivada — não-identificante.
- **Respostas abertas**: revisão por regex para emails e nomes próprios. Nenhum identificador pessoal foi encontrado. Veja célula 7 do notebook 01 para o procedimento.

## 5. Achado anômalo: Q16 (versionamento)

30 de 32 respostas a Q16 são literalmente idênticas, indicando provavelmente uma opção pré-selecionada como *default* no Google Forms. Este achado meta sobre o instrumento é discutido na Seção 6 do paper (Threats to Validity → Validade de Constructo). Reproduzimos a observação no notebook `04a_multiple_choice.ipynb`, seção 6.

## 6. Codebook qualitativo

`data/codebook/coding_scheme.csv` contém 90 códigos organizados em 6 temas axiais:
- **T1 Contextualismo** — equilíbrio depende do domínio/aplicação (44% dos respondentes)
- **T2 Garbage-in-out** — má qualidade compromete o pipeline (16%)
- **T3 Trade-offs** — explicitamente nomeados (28%)
- **T4 Hierarquia da qualidade** — subconjunto essencial-universal (16%)
- **T5 Práticas/Ferramentas** — feature selection, monitoramento, plataformas (25%)
- **T6 Lacuna ER → ML** — experiência limitada/informal em ER (56%)

Codificação por **um único codificador** — limitação reportada como ameaça à validade de constructo. O codebook está aberto para re-codificação por terceiros.

## 7. Citação

```bibtex
@inproceedings{souza2026perception,
  author    = {Anonymous},
  title     = {Percep{\c{c}}{\~a}o sobre Requisitos de Qualidade de Dados para Sistemas Baseados em Aprendizado de M{\'a}quina: Um Survey com Profissionais Brasileiros},
  booktitle = {Proceedings of the 40th Brazilian Symposium on Software Engineering (SBES)},
  year      = {2026},
  doi       = {pending}
}
```

## 8. Licença

Os dados e o código são licenciados sob **Creative Commons Attribution 4.0 International (CC-BY 4.0)**. Veja [LICENSE](LICENSE).

## 9. Contato

Anonimizado durante o processo de revisão do SBES 2026. Após aceite, o pacote será publicado no Zenodo com DOI permanente.
