# P5 — Evidencia y candidato para revisión de pares

Fecha: **2026-10-11**. Primer dictamen del comité: revisión de literatura, datos y capacidades. Destinatarios: revisor estadístico/metodológico y equipo de tres personas. Finalidad: decidir si la contribución merece un protocolo; no presenta resultados de investigación ni aprueba ejecución.

**Recomendación:** abandonar la afirmación de que ComBat-GAM borra una señal biológica conocida. Avanzar a revisión de un **benchmark de recuperación y calibración de contrastes de interacción, definido sobre soporte común y calibrado al diseño real de ABIDE I**. Es viable con datos accesibles, pero su innovación es condicional: los componentes aislados ya tienen antecedentes cercanos.

Convenciones: **V** observado localmente; **F** documentado por fuente primaria; **I** interpretación/propuesta; **U** desconocido. Cobertura, acceso y nivel de verificación por fuente: [índice bibliográfico](../../literature/README.md), [papers.csv](../../literature/papers.csv), [datasets.csv](../../literature/datasets.csv), [software.csv](../../literature/software.csv).

## 1. Datos realmente disponibles y límite determinante

El CSV PCP contiene 1.112 `SUB_ID` únicos, 106 columnas, 20 etiquetas `SITE_ID` y edades 6,47–64. `AGE_AT_SCAN`, `SEX`, `DX_GROUP` y `SITE_ID` no tienen vacíos/-9999. Hay 77 `FILE_ID=no_filename`. **V** No identificar las 20 etiquetas automáticamente como 20 escáneres independientes.

| Muestra observada | Autistas masculinos | Autistas femeninos | Controles masculinos | Controles femeninos | Total |
|---|---:|---:|---:|---:|---:|
| Ambos `.stats` | 443 | 62 | 435 | 95 | 1.035 |
| 68 regiones positivas y finitas | 437 | 62 | 433 | 95 | 1.027 |
| Completos + ambos evaluadores anatómicos `OK` | 323 | 52 | 318 | 80 | 773 |
| Filtro anterior + edad 10–18 inclusive | 183 | 31 | 171 | 49 | 434 |

Estos filtros describen disponibilidad; **no son la muestra final aprobada**. `SEX` se interpreta según codificación del repositorio, sin atribuir identidad de género ni verificar sexo biológico por otros medios. Los raters 2/3 de PCP evalúan anatomía **cruda**; sus etiquetas no certifican superficies FreeSurfer. **F** [PCP QA](https://preprocessed-connectomes-project.github.io/abide/quality_assessment.html), copia local `data/sources/abide_quality_assessment.html`.

Con 68 regiones completas, 14 etiquetas de sitio contienen los cuatro grupos sexo×diagnóstico y 11 tienen una intersección de rangos de edad de **ancho positivo**. Con el filtro anatómico ilustrativo, son 12 y 9 respectivamente. Las intersecciones inclusivas son 13 y 10 porque incluyen puntos aislados; estos no permiten estimar una asociación de edad. **V** Solo **NYU, UM_1 y YALE** tienen al menos cinco personas en cada celda sexo×diagnóstico tras el filtro ilustrativo. Ese mínimo es una descripción, **no** una garantía de potencia o identificabilidad. **I**

| Sitio tras filtro ilustrativo | ASD masculino | ASD femenino | Control masculino | Control femenino | Intersección min–max de edad de los cuatro grupos |
|---|---:|---:|---:|---:|---|
| NYU | 62 | 10 | 68 | 25 | 8,74–29,13 |
| UM_1 | 25 | 7 | 34 | 17 | 9,70–18,00 |
| YALE | 13 | 8 | 5 | 6 | 13,75–15,92 |

Rangos superpuestos pueden esconder huecos de densidad. No hay un rango universal que deba exigirse a los 20 sitios; excluir todos los sitios incompletos puede eliminar casi toda la información femenina. Deben declararse tanto los supuestos de combinación entre centros como los grupos/edades realmente representados. **I**

Evidencia reproducible: [resumen por grupo](../../literature/abide_design_group_summary.csv), [celdas de edad de 2 años](../../literature/abide_design_age_cells.csv), [grupos por sitio](../../literature/abide_design_site_groups.csv), [soporte por sitio](../../literature/abide_design_support.csv). Se obtuvieron contando filas de `data/derived/abide1_freesurfer_thickness.csv`; no se ajustaron modelos.

## 2. Antecedentes que impiden una reivindicación genérica de novedad

| Fuente primaria | Componente ya estudiado | Diferencia que tendría que justificar P5 |
|---|---|---|
| [Fortin, 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5845848/); [Pomponio, 2020](https://pubmed.ncbi.nlm.nih.gov/31821869/) | ComBat cortical y extensión no lineal, respectivamente | Una curva de edad protegida o usar otro paquete no es innovación |
| [Sun, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9648725/) | Comparación empírica de grosor con LME, ComBat y ComBat-GAM; interacciones edad×diagnóstico y sexo×diagnóstico en PTSD | Recuperación de un estimando conocido; separar error de ajuste final y de armonización |
| [Bayer, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC7614761/) | ABIDE, grosor, edad/sexo y HBR de una etapa frente a armonización; calibración de puntuaciones normativas | Contrastes de media sexo×diagnóstico dependientes de edad, no repetir el benchmark normativo |
| [Reynolds, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10412957/) | EB/FB ComBat, verdad simulada, diagnóstico×edad, sensibilidad/error tipo I e incertidumbre | Contraste triple y relación entre soporte del diseño y recuperación/calibración; simulación sola no basta |
| [Gardner, 2025](https://onlinelibrary.wiley.com/doi/10.1002/hbm.70197) | ComBatLS; sitios sintéticos desbalanceados por sexo, grosor y errores de centiles | Inferencia de interacciones en la **media**, con grupos clínicos y soporte observado; no confundir escala y media |
| [Jodoin, 2025](https://www.nature.com/articles/s41598-025-25400-x) | Supuestos ComBat, desbalance y diferencias de pendiente en DTI | Condiciones cuantificadas para un estimando cortical concreto; no extrapolar sus mínimos de muestra |
| [Marzi, 2024](https://www.nature.com/articles/s41597-023-02421-7) | Grosor, soporte de edad, datos simulados y fuga en predicción; centros simulados del mismo tamaño | Diseño sexo×diagnóstico×edad observado y cobertura inferencial de contrastes; predicción de edad/sitio es otra tarea |
| [Nygaard, 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4679072/); [Li, online 2021 / volumen 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10449015/) | Confianza exagerada/correlación inducida por dos etapas en expresión génica | Evaluación específica, sin presentar el mecanismo estadístico como descubrimiento propio |
| [Xin, 2026](https://onlinelibrary.wiley.com/doi/10.1002/hbm.70546) | ComBat-Predict para centros nuevos; existe corrección posterior | Transferencia a sitios nuevos queda fuera del núcleo; no afirmar imposibilidad universal de ComBat |

**F** Las capacidades de interacción ya existen: [ComBatFamily](https://github.com/andy1764/ComBatFamily) acepta modelos y fórmulas; el [manual primario ComBatFamQC](https://stat.ethz.ch/CRAN/web/packages/ComBatFamQC/ComBatFamQC.pdf) documenta interacciones lineales y factor-smooth. Crear una matriz de diseño con interacciones es una configuración verificable, **no un algoritmo nuevo**. `smooth_terms=['AGE']` de [neuroHarmonize](https://github.com/rpomponio/neuroHarmonize) no crea automáticamente curvas diferentes para sexo×diagnóstico. El código maestro inspeccionado utiliza bases cúbicas de edad con `df=10`: no suponer que esa complejidad cabe en la celda femenina escasa. Versiones concretas no se han ejecutado. **F/U**

**Motivación biológica, no resultado de P5:** [Andrews, 2024](https://www.nature.com/articles/s41380-024-02592-8) estudió la interacción edad×sexo×diagnóstico con 918 MRI longitudinales de infancia, incluyendo 88 niñas autistas. [Bedford, 2020](https://www.nature.com/articles/s41380-019-0420-6) ya evaluó heterogeneidad cortical asociada a sexo, edad e inteligencia. Estas preguntas son biológicamente relevantes; ABIDE I transversal no permite estimar trayectorias intraindividuales ni atribuir diferencias a poda sináptica. **F/I**

## 3. Único candidato preferido — recuperación y calibración en soporte común

**Título de trabajo:** *Recuperación de contrastes de grosor cortical por edad, sexo y diagnóstico bajo armonización multicéntrica: benchmark calibrado al diseño ABIDE I*.

**Pregunta:** ¿En qué condiciones de desbalance y soporte de edad la especificación de interacciones durante la armonización cambia el sesgo, el error y la cobertura de contrastes sexo×diagnóstico dependientes de edad, y hasta dónde se sostienen las estimaciones empíricas de ABIDE I dentro del soporte observado? **I**

**Estimando candidato:** sea `μ_r(a,s,d)` el grosor medio esperado de la región `r` en una población objetivo y ponderación de sitios definidas, sin el componente técnico en las simulaciones. Definir:

```text
C_r(a) = [μ_r(a,femenino,ASD) − μ_r(a,femenino,control)]
       − [μ_r(a,masculino,ASD) − μ_r(a,masculino,control)]
Θ_r(a0,a1) = C_r(a1) − C_r(a0)
```

`Θ` mide cómo cambia **la diferencia de diferencias** con edad; no es tasa longitudinal. Las edades `a0,a1` se fijan después de auditar soporte con una regla que use covariables, **antes de observar efectos**. 10 y 16 años serían ejemplos para planificación, no edades ya justificadas. En simulación se puede recuperar `Θ` con verdad conocida. En datos reales `C(a)` y su promedio en soporte común son sensibles al modelo; `Θ` será secundario y de baja complejidad, condicionado a elegibilidad y precisión. **I/U**

No basta con promediar cuatro curvas calculadas sobre distribuciones de sitio diferentes: usar pesos objetivo comunes y documentar qué contrastes requieren extrapolación. Si se restringe la población, definir explícitamente su nuevo estimando. Comparar dos poblaciones objetivo distintas no mide sesgo por armonización. **I**

### Mapa pregunta–variables–acceso

| Necesidad | Evidencia | Estado |
|---|---|---|
| Resultado cortical por región | 68 `*_thickness_mm`, `.stats` originales y `ThickAvg` | V: disponible; QC de superficies U |
| Cuatro grupos clínicos/sexo | `DX_GROUP` 1/2 y `SEX` 1/2 | V: disponibles; cobertura femenina escasa |
| Edad para contraste | `AGE_AT_SCAN` sin faltantes | V: disponible; edad anatómica específica escasa |
| Lote inicial | `SITE_ID` | V: disponible; escáner/protocolo por participante U |
| Unidades independientes | `SUB_ID` único en CSV I | V; no sumar II ni sesiones |
| Diseño observado para simular | edades/grupos/sitios y tabla de disponibilidad | V: sin necesidad de nueva descarga |
| Escala/covarianza/calibración | Grosor regional disponible | V: medidas; U: parámetros a estimar después de aprobación |
| Verdad biológica y clínica longitudinal | No contenida en estos derivados | U: no inferible; verdad **generada** solo para simulación |

ABIDE permite investigación no comercial con reconocimiento de fuentes; originales mediante registro NITRC/FCP. La copia PCP necesaria ya está descargada sin cuenta. **F/V** [ABIDE I](https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html). ABIDE II no es requisito: añadirlo exige verificar variables, independencia, QC y procesamiento compatible. **I/U**

### Comparación acotada que el revisor debe exigir

1. Modelo de una etapa sobre datos originales, con ajuste de sitio y el mismo modelo biológico de interés: referencia estadística, no verdad empírica.
2. ComBat lineal con efectos principales declarados: comparador histórico deliberadamente limitado para edad no lineal.
3. Armonización con curva compartida de edad + sexo + diagnóstico.
4. Misma familia de armonización con la estructura jerárquica de interacciones protegida explícitamente y base de edad de baja complejidad.

El contraste **3 frente a 4**, con igual software/familia, covariables finales y población, debe aislar la especificación protegida. El contraste **1 frente a 4** determina si armonizar aporta algo sobre el ajuste de una etapa. La estrategia 4 no tiene garantizada superioridad. Si se incluyen escenarios con variabilidad biológica distinta por sexo/diagnóstico, añadir ComBatLS como comparador pertinente, o declarar esos escenarios fuera del núcleo. No adjudicar sus fallos a un método diseñado para preservar solamente la media. **I**

Mantener el mismo modelo biológico final permite distinguir un error de armonización de una falsa interacción por curvatura omitida; este segundo problema ya tiene antecedente general. **I/F** [Simonsohn, 2024](https://www.psychologicalscience.org/journals/ampps/25152459231207787/).

### Escenarios mínimos antes de expandir métodos

- **Diseño:** patrón observado de edad×sexo×diagnóstico×sitio; versión restringida por una regla de soporte; control de diseño balanceado. La versión balanceada es artificial y no multiplica la muestra real.
- **Señal conocida:** nulo de interacción; sexo×diagnóstico constante sin `Θ`; contraste que cambia con edad con amplitud y signo conocidos. Variar magnitudes nula/pequeña/moderada sin llamarlas prevalencias reales.
- **Técnica:** sin efecto de sitio y con efectos aditivos/multiplicativos conocidos. Un escenario de mala especificación de curvas es necesario; otros, como pendientes técnicas por sitio o heteroscedasticidad, deben justificarse y acotarse.
- **Dependencia regional:** conservar o simular covarianza plausible entre las 68 regiones; no tratarlas como 68 estudios independientes.

Calibrar sobre diseño observado y medidas de escala/covarianza no equivale a conocer parámetros técnicos verdaderos en ABIDE. Variar parámetros alrededor de la calibración evita que un generador elegido para favorecer ComBat dicte el resultado. Debe existir una rama deliberadamente favorable a cada supuesto y otra que lo viola; no un escenario que siempre favorezca la estrategia propuesta. **I**

**Resultados primarios:** sesgo y RMSE de `Θ` conocido, cobertura de intervalos nominales y error tipo I bajo el nulo. Reportar magnitud/dirección, intervalos y error Monte Carlo; no ordenar métodos por número de p-valores significativos. Informar también convergencia/no-identificabilidad y precisión. **I**

**Incertidumbre:** contrastar intervalos finales que ignoran la estimación de armonización frente a una estrategia que vuelva a estimar **todo** el procedimiento; el bootstrap no se presume válido. Su validez es precisamente lo que se evalúa por cobertura conocida. Definir si la inferencia condiciona a sitios observados; no presentar bootstrap de participantes dentro de sitios como generalización a centros nuevos. Selección de soporte/modelos también se reestima o se condiciona explícitamente. **I**

**Empírico secundario:** mismo estimando/modelo y muestra entre métodos; tamaños e intervalos; sensibilidad a QC, sitios influyentes y restricción de soporte; mapa de extrapolación. No seleccionar regiones por efecto mayor tras armonizar, ni llamar validación externa a dejar un sitio fuera y volver a ajustar. Reducción de señal de sitio es una métrica auxiliar: puede reflejar composición biológica real. **I**

**Entregable mínimo:** una auditoría de elegibilidad/soporte, un contraste escalar `Θ` conocido por escenario y región, tres comparadores centrales (una etapa, curva compartida, interacción protegida) y tablas de sesgo/RMSE/cobertura bajo nulo y alternativa. Comenzar con edad lineal o una base común pequeña; no exigir cuatro curvas suaves densas en los datos reales. El piloto puede limitarse a dos diseños (observado y control balanceado), dos señales (nula y alternativa) y dos condiciones técnicas (sin/con sitio), antes de añadir soporte restringido y curvatura. Si el componente empírico no sostiene `Θ`, conservar como demostración secundaria el promedio de `C(a)` en soporte común con sus pesos definidos. Eso reduce la pregunta empírica y su ambición biológica; no aumenta artificialmente las mujeres disponibles. El benchmark completo propuesto y cualquier simulación quedan sujetos a aprobación del equipo. **I**

## 4. Evaluación de los tres criterios y pruebas que pueden refutar la aportación

| Criterio | A favor | Objeción decisiva | Evidencia requerida |
|---|---|---|---|
| Factibilidad | Tabla regional pequeña, datos esenciales disponibles y simulación sin nuevas cuentas | QC cortical incompleto y soporte femenino reducido | Protocolo de QC alcanzable; rango/base estimables; recursos medidos en piloto |
| Innovación | Estimando triple explícito, soporte auditado y recuperación/calibración conjunta | Desbalance, interacciones, simulación e incertidumbre ya estudiados | Demostrar qué relación diseño→fallo→decisión no cubren competidores; examinar suplementos clave |
| Publicabilidad | Un resultado nulo también puede delimitar cuándo armonizar ayuda | Comparación rutinaria/escenario construido favorable o simple replicación ABIDE | Recomendación cuantificada que cambia una decisión analítica y resiste escenarios alternativos |

**La aportación puede fallar** si las diferencias son triviales por construcción algebraica al proteger los mismos términos que se vuelven a estimar; si toda ventaja se explica por usar mejor el modelo final; si ningún estimando empírico tiene soporte; si las condiciones ya quedaron documentadas en los competidores; o si intervalos válidos requieren un coste desproporcionado sin utilidad adicional. Antes de reclamar innovación, derivar casos de invariancia y separar mala especificación, pérdida de precisión y armonización. **I**

**Desconocido decisivo:** ¿el vínculo entre soporte observado, recuperación del contraste y calibración permite una regla útil que supere un ajuste de sitio de una etapa, o solo reproduce consecuencias conocidas? Debe responderlo el piloto; esta revisión no inventa su resultado. **U**

## 5. Puertas para el revisor y la síntesis

- **Acceso/campos:** pasa para un benchmark ABIDE I; no depende de ABIDE II.
- **Unidad/tamaño:** pasa para calibrar diseño; interacción triple empírica confirmatoria **no está justificada** por el tamaño bruto. Condicionar/reducir complejidad.
- **Biología:** pasa como motivación de contrastes observacionales; fallan afirmaciones de poda, pubertad o trayectoria longitudinal.
- **Implementación:** capacidad de representar interacciones documentada; ejecución/estabilidad por verificar después de aprobación.
- **Novedad/publicabilidad:** **condicional**, no demostrada. El comité debe valorar si el contraste con antecedentes y la decisión que apoya son suficientes.

No se propone un segundo proyecto que rebaje automáticamente la exigencia de innovación. Si el benchmark no supera la puerta de aporte, conservarlo como trabajo de reproducibilidad/curso, reducir la ambición editorial y volver al equipo antes de convertirlo en propuesta de artículo. Si solo falla la cobertura empírica triple, el componente de simulación puede permanecer y la demostración real reducirse a `C(a)` promedio en soporte; eso exige revisar alcance, no declarar una hipótesis confirmada. **I**

**Entrega al revisor:** cuestionar definición de población y pesos, QC superficial alcanzable, complejidad máxima de edad, comparadores de una etapa/ComBatLS, dependencia inducida, invariancias algebraicas, generador y métricas primarias. Emitir *continuar condicional / reformular / rechazar* con bloqueos no compensables por puntuaciones altas en otros criterios. No se ajustó ningún modelo de investigación ni se ejecutó simulación en esta fase.

Actualización posterior al dictamen: [Reynolds y su suplemento se inspeccionaron mediante la API de Europe PMC](04_COMPETITOR_VERIFICATION.md). La evaluación de novedad permanece condicional.
