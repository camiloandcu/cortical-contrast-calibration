# Índice de evidencia de la propuesta

Comprobación: **2026-10-11**. Decisión que apoya: determinar si una evaluación de recuperación y calibración de interacciones de grosor cortical en un diseño multicéntrico desbalanceado merece desarrollo. Población: personas autistas y controles; modalidad: T1/grosor cortical regional; dataset de trabajo: ABIDE I PCP. Esta es una revisión dirigida, no una búsqueda sistemática exhaustiva.

## Archivos y convenciones

- `papers.csv`: fuentes primarias, DOI, pregunta, población/modalidad, métodos, resultados documentados, limitaciones y relación con esta propuesta. `verification_level` distingue texto completo abierto, resumen/ficha y texto primario indexado cuya apertura falló. Un hallazgo indexado no verifica los suplementos.
- `datasets.csv`: acceso, campos/grupos y tamaños observados o documentados. ABIDE II es opcional y no inspeccionado; no se suman cohortes.
- `software.csv`: capacidades comprobadas en documentación/código primarios; ningún paquete se instaló ni ejecutó en esta revisión.
- `abide_design_group_summary.csv`, `abide_design_site_groups.csv`, `abide_design_age_cells.csv`, `abide_design_support.csv`: conteos descriptivos; reproducir con `python3 literature/audit_design_coverage.py` desde la raíz.
- [Entrega al comité](../docs/review/01_EVIDENCE_AND_CANDIDATES.md): candidatos, estimando, solapamiento y condiciones para continuar.

**V**: observado localmente. **F**: fuente primaria documentada. **I**: inferencia/propuesta del comité. **U**: desconocido o pendiente. Los límites propios de un artículo se separan de nuestra interpretación en las columnas `author_limitations` y `reviewer_interpretation`.

## Cobertura de búsqueda

Periodo de interés: desde los antecedentes fundacionales hasta **2026-10-11**. Se consultó búsqueda web general con comprobación posterior en PubMed/PMC, editores originales (NeuroImage, NeuroImage: Clinical, Scientific Data, Human Brain Mapping, Molecular Psychiatry, Scientific Reports, Biostatistics), repositorios ABIDE/PCP/FreeSurfer y documentación de neuroHarmonize, ComBatFamily y CRAN ComBatFamQC. Se siguieron referencias relevantes de los artículos ComBatLS y Bayer/Sun. Se deduplicó por DOI; las distintas versiones de ComBatLS y ComBat-Predict no se cuentan como trabajos independientes.

Consultas dirigidas utilizadas (se conserva la redacción de las familias de consulta más relevantes):

| Área | Consultas |
|---|---|
| Núcleo metodológico | `ComBat harmonization nonlinear interactions age sex diagnosis ABIDE cortical thickness 2024 2025 2026`; `ComBat-GAM interactions sex diagnosis simulation`; `ComBat-GAM interaction simulation ABIDE` |
| ABIDE y población | `ABIDE cortical thickness sex age 2024 2025 2026 harmonization`; `autism cortical thickness age sex interaction ABIDE females 2025 2024`; `Large-scale analyses 31028290 autism morphometry`; `Normative age modelling of cortical thickness in autistic males` |
| Antecedentes cercanos | `Bayer 2022 harmonization site effects biological variability ComBat NeuroImage 36272672`; `Sun 2022 ABIDE cortical thickness harmonization sex age 35917919`; `ComBatLS location scale preserving harmonization DOI Human Brain Mapping 2025`; `ComBat Harmonization: Empirical Bayes versus fully Bayes approaches DOI` |
| Inferencia/calibración | `ComBat GAM confidence intervals coverage inference simulation harmonization misspecification`; `harmonization ComBat interactions confounding type I error uncertainty cortical thickness sex diagnosis simulation`; `ComBat harmonization confidence interval bootstrap two stage type I error 2024 2025 2026`; `ComBat harmonization interaction effects false positives covariance induced 2024 2025`; `Methods that remove batch effects Nygaard full text` |
| Soporte/desbalance | `ComBat common support harmonization interactions`; `ComBat common support neuroimaging`; `harmonization common support MRI`; `Challenges and best practices when using ComBAT authors doi` |
| Software | `neuroHarmonize smooth_terms interaction`; `ComBatFamily formula gam`; `ComBatFamQC publication Hu 2025 2026`; `ComBatFamQC harmonization quality assessment paper`; `ComBat-Predict Xin`; `ComBat-Predict Enhances Generalizability doi`; `ComBat-Predict 10.1002` |
| Actualización 2026 | `ComBat interaction 2026 neuroimaging`; `ComBat-Predict harmonization unseen sites 2026`; búsquedas anteriores con 2024–2026 y seguimiento de artículos/preprints recientes |
| Acceso | `ABIDE Creative Commons data`, páginas originales ABIDE I/II, instrucciones PCP y formato FreeSurfer |

Inclusión: evidencia que modifica la pregunta, el comparador, la validez inferencial o la viabilidad; estudios primarios sobre grosor cortical/armonización y autismo; otros dominios solo cuando ofrecen un antecedente estadístico directamente relevante. Exclusión: recomendaciones comerciales, agregadores como sustento final, papers funcionales que no responden la pregunta estructural y métodos voxel-wise/deep learning sin implicación inmediata para el benchmark regional.

Se detectaron también preprints 2026 de Psy-ShareD, Tensor-ComBat, Robust-ComBat y CREB, además de trabajo sobre fuga de información en predicción. Su existencia actualiza el panorama; **no** se usan para verificar capacidades, resultados o superioridad cuando no pudo abrirse la fuente primaria completa. Tensor-ComBat/Robust-ComBat responden preguntas de imagen/DTI diferentes. No se realizó extracción sistemática de citas posteriores ni comprobación exhaustiva de cada suplemento. Algunas aperturas de PMC, PCP y DOI fueron bloqueadas o fallaron; las limitaciones se registran. PCP QA se comprobó en la copia primaria local `data/sources/abide_quality_assessment.html` obtenida por el agente principal.

## Límites de la conclusión de novedad

La preservación de interacciones ya se configura mediante fórmulas/matrices de diseño. El desbalance por sexo, la mala especificación y la incertidumbre de dos etapas ya tienen antecedentes. La aportación candidata debe ser **una evaluación conjunta de estimandos de interacción definidos en soporte común, con diseño ABIDE observado, verdad simulada y cobertura de todo el procedimiento**. No se encontró una réplica exacta de ese conjunto en las fuentes inspeccionadas; esa ausencia es una señal para revisión adicional, no una prueba de novedad. No hay garantía de publicación ni un resultado biológico obtenido.

## Comprobación adicional del antecedente cercano

Después del dictamen se recuperaron e inspeccionaron el XML primario y el suplemento de Reynolds 2023 mediante Europe PMC. La apertura directa de PMC seguía fallando; el acceso alternativo resolvió esta incertidumbre. Ver [la comprobación y sus límites](../docs/review/04_COMPETITOR_VERIFICATION.md). No se inspeccionaron todos los suplementos de los demás competidores.
