# Codebook — Survey Qualidade de Dados em ML (PT)

**N**: 32 respondentes · **Coleta**: 2025-02-14 → 2025-03-15

## Schema

| Coluna | Tipo | Domínio | Origem (Q) |
|---|---|---|---|
| `timestamp` | datetime | timestamp Forms | - |
| `age` | categórica | 18-24, 25-34, 35-44, 45-54 | Q1 |
| `state` | UF (2 letras) | AC..TO | Q2 |
| `region` | categórica | Norte/Nordeste/Centro-Oeste/Sudeste/Sul | derivada |
| `gender` | categórica | Homem, Mulher | Q3 |
| `education` | categórica | 6 níveis | Q4 |
| `role` | categórica | 7 valores livres normalizados | Q5 |
| `seniority` | ordinal | Estagiário<Júnior<Pleno<Sênior | Q6 |
| `seniority_ordinal` | int 1-4 | - | derivada |
| `seniority_group` | categórica | junior, senior | derivada |
| `n_projects` | int | 0..40 | Q7 |
| `role_group` | categórica | data_scientist/developer/... | derivada |
| `skill_cleaning` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_normalization` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_outliers` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_integration` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_transformation` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_validation` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_pipelines` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_monitoring` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_libs` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `skill_split` | Likert 1-5 | 1=Muito baixa..5=Muito alta | Q8 |
| `word_1` | string | palavra livre lowercase | Q9 |
| `word_2` | string | palavra livre lowercase | Q9 |
| `word_3` | string | palavra livre lowercase | Q9 |
| `word_4` | string | palavra livre lowercase | Q9 |
| `word_5` | string | palavra livre lowercase | Q9 |
| `imp_precision` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_completeness` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_consistency` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_credibility` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_currentness` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_accessibility` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_compliance` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_reliability` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_efficiency` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_traceability` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_understandability` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_availability` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `imp_recoverability` | Likert 1-5 | 1=Nada importante..5=Muito importante | Q11 |
| `pri_precision` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_completeness` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_consistency` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_credibility` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_currentness` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_accessibility` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_compliance` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_reliability` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_efficiency` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_traceability` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_understandability` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_availability` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `pri_recoverability` | Likert 1-5 | 1=Sem prioridade..5=Essencial | Q13 |
| `re_experience` | string (open) | resposta livre | varia |
| `imp_justification` | string (open) | resposta livre | varia |
| `pri_justification` | string (open) | resposta livre | varia |
| `balance_open` | string (open) | resposta livre | varia |
| `versioning_open` | string (open) | resposta livre | varia |
| `incorporation_open` | string (open) | resposta livre | varia |
| `measurement_open` | string (open) | resposta livre | varia |
| `documentation_open` | string (open) | resposta livre | varia |
| `challenges_open` | string (open) | resposta livre | varia |
| `discussion_freq` | Likert 1-5 | 1=Nunca..5=Todos os dias | Q19 |
| `support_freq` | Likert 1-4 | 1=Raramente..4=Sempre | Q22 |

## Anonimização

- Coluna `email` (Q23): removida. 15 respondentes informaram e-mail. Não publicada.
- Coluna `@dropdown`: artefato Google Forms (sempre vazia). Removida.
- Estado: padronizado para UF de 2 letras + região derivada — não identifica indivíduo.
- Abertas: revisão por regex pra emails e nomes próprios (ver alertas no notebook).