# Revisión verificable de los datos

Comprobado: 2026-10-11. Destinatarios: las tres personas que decidirán si esta propuesta puede ejecutarse. Este documento describe archivos y variables; el comité evalúa la contribución en [su revisión](review/02_PEER_REVIEW.md) y el diseño se presenta en [la propuesta refinada](03_REFINED_PROPOSAL.md).

**Conclusión:** ABIDE I permite estudiar la recuperación de interacciones bajo un diseño multicéntrico real y desbalanceado. Los datos no permiten atribuir diferencias entre armonizaciones a biología verdadera, inferir poda sináptica ni establecer trayectorias longitudinales. La escasez de participantes femeninas con autismo limita las interacciones con edad.

## 1. Archivos disponibles

Las observaciones siguientes proceden de la auditoría local de octubre de 2026.
El repositorio público no incluye microdatos ni derivados individuales:
reconstruirlos con la [guía de descarga](02_DOWNLOAD_GUIDE.md).

| Dataset o derivado | Observación local | Uso y límite |
|---|---|---|
| Fenotipos ABIDE I (`data/raw/abide1/phenotypic.csv`, generado localmente) | 1.112 filas, 106 columnas | Identificadores, sitio, diagnóstico, sexo, edad y medidas clínicas; cobertura distinta según centro. |
| `data/raw/abide1/freesurfer/<FILE_ID>/{lh,rh}.aparc.stats` | 2.070 archivos, 1.035 participantes bilaterales | Estadísticos FreeSurfer 5.1, atlas aparc/Desikan–Killiany. No contienen las superficies para inspección visual. |
| Grosor regional derivado (`data/derived/abide1_freesurfer_thickness.csv`, generado localmente) | 1.035 filas, 80 columnas; 68 medidas | Unión por `FILE_ID`, identificadores, campos de auditoría y regiones ausentes preservadas. |
| Disponibilidad (`data/derived/abide1_freesurfer_availability.csv`, generado localmente) | 1.112 filas | Cobertura de archivos y completitud regional. |
| [Inventario de columnas](04_COLUMN_INVENTORY.md) | 106 fenotípicas + 80 derivadas | Tipos, faltantes y rangos; CSV (`data/derived/column_inventory.csv`, generado localmente). |
| [Diseño observado](../literature/abide_design_site_groups.csv) | Sitio × diagnóstico × sexo | Respaldo de los contrastes; [edades](../literature/abide_design_age_cells.csv) y [soporte](../literature/abide_design_support.csv). |
| ABIDE II | Solo diccionario descargado | CSV y derivados compatibles no inspeccionados. No es validación externa disponible. |

Los datasets fuente ocupan aproximadamente 13,45 MB; las copias de literatura añaden 45,16 MB. Procedencia, fecha y SHA-256: [manifiesto](../data/download_manifest.csv). No se han ajustado modelos de investigación ni simulado resultados.

Fuentes primarias: [ABIDE I](https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html), [descarga PCP](https://preprocessed-connectomes-project.github.io/abide/download.html), [estadísticos FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/mris_anatomical_stats). Las 20 etiquetas observadas de sitio no equivalen al número de instituciones de los portales.

## 2. Flujo de participantes

`DX_GROUP=1`: autismo; `DX_GROUP=2`: control. `SEX=1`: masculino; `SEX=2`: femenino, según el proveedor. Estos códigos no describen identidad de género.

| Estado | Autismo masculino | Autismo femenino | Control masculino | Control femenino | Total |
|---|---:|---:|---:|---:|---:|
| CSV original | 474 | 65 | 474 | 99 | 1.112 |
| Ambos archivos FreeSurfer | 443 | 62 | 435 | 95 | 1.035 |
| 68 medidas positivas y finitas | 437 | 62 | 433 | 95 | 1.027 |
| Además, evaluadores anatómicos 2 y 3 = `OK` | 323 | 52 | 318 | 80 | 773 |

Los 77 `FILE_ID=no_filename` no son fallos del descargador: el índice no les asigna un archivo procesado. Ocho participantes tienen regiones ausentes, enumerados en audit_summary.json (`data/derived/audit_summary.json`, generado localmente). No se rellenaron con cero.

**La fila de 773 es una sensibilidad ilustrativa**, no una muestra final aprobada. Según [PCP QA](https://preprocessed-connectomes-project.github.io/abide/quality_assessment.html), los evaluadores 2 y 3 inspeccionaron anatomía y función originales; el 1 se concentró en función procesada. Un `OK` anatómico no certifica la superficie FreeSurfer. Ese QC sigue pendiente.

## 3. Variables que deben discutir los tres revisores

| Campo literal o grupo | Situación observada | Decisión sugerida |
|---|---|---|
| `SUB_ID`, `FILE_ID` | Identificadores y clave de los archivos | Validar unicidad y correspondencia; no usarlos como predictores. |
| `SITE_ID` | 20 etiquetas | Proxy de lote; no necesariamente identifica escáner o secuencia. |
| `DX_GROUP` | Autismo/control | Especificar contraste e interacción; no es una exposición aleatorizada. |
| `SEX` | Dos códigos del proveedor | No extender conclusiones a categorías no recogidas. |
| `AGE_AT_SCAN` | 6,47–64 años en el CSV | Diseño transversal. Predefinir intervalo y soporte; evitar extrapolaciones. |
| `AGE_AT_MPRAGE` | 91,01 % faltante | No sustituir con ella la edad principal. Documentar incertidumbre de edad específica del T1. |
| `FIQ` | 35 vacíos + 37 códigos `-9999` | Ajuste solo si el estimando lo requiere; puede cambiar contraste y selección. |
| `ADOS_TOTAL` | 670 vacíos + 27 códigos `-9999` | No exigirlo para controles; análisis secundario según instrumento y elegibilidad. |
| `qc_anat_rater_2`, `qc_anat_rater_3` | Evaluaciones anatómicas originales | Comparar inclusión y selección por sitio/grupo; no declarar QC de superficies. |
| `anat_*` | Métricas anatómicas automatizadas | Explorar cobertura; justificar cada covariable. |
| `func_*`, `qc_func_*` | Función, movimiento y QC funcional | No usarlos como criterios estructurales automáticos. |
| `lh_*_thickness_mm`, `rh_*_thickness_mm` | 68 columnas de grosor medio cortical, mm | Preservar hemisferios y nombre de región. |
| Campos derivados de completitud | Bilateralidad, número de regiones y valores inválidos | Control de integridad, no variables biológicas. |

Todos los nombres y porcentajes están en [el inventario](04_COLUMN_INVENTORY.md). Los códigos especiales cuentan como faltantes sin modificar el CSV original.

## 4. Diez campos originales de FreeSurfer

| Campo | Significado |
|---|---|
| `StructName` | Región |
| `NumVert` | Número de vértices |
| `SurfArea` | Área superficial, mm² |
| `GrayVol` | Volumen de sustancia gris, mm³ |
| `ThickAvg` | Grosor medio, mm; resultado de esta propuesta |
| `ThickStd` | Desviación dentro de la región, mm; no error estándar entre participantes |
| `MeanCurv` | Curvatura media |
| `GausCurv` | Curvatura gaussiana |
| `FoldInd` | Índice de plegamiento |
| `CurvInd` | Índice de curvatura |

Rangos: inventario específico (`data/derived/freesurfer_stats_column_inventory.csv`, generado localmente). Los encabezados comentados aportan contexto adicional; la tabla derivada conserva `ThickAvg`, identificadores y auditoría. La disponibilidad de otros campos no obliga a ampliar el objetivo.

## 5. Cobertura e identificabilidad

En la cohorte de 1.027, 14 de 20 sitios tienen las cuatro celdas diagnóstico × sexo; 11 tienen intersección de rangos de edad de ancho positivo. Con el filtro ilustrativo son 12 y 9. Una intersección en un punto no tiene ancho positivo. Tabla (`data/derived/abide1_common_support_by_site.csv`, generado localmente).

**El diagnóstico min–max es débil:** no demuestra densidad común, rango de la matriz de diseño ni precisión. Un rango amplio puede ocultar celdas casi vacías. En edades 10–18, el comité encuentra solo 31 participantes femeninas con autismo tras el filtro ilustrativo. Un modelo triple flexible sin restricciones no está respaldado por esos conteos.

No excluir centros por significación ni presentar un centro omitido como escáner nuevo validado. Especificar la distribución de edad/sitios del contraste y qué ocurre cuando faltan grupos. Una simulación puede tener verdad conocida; ABIDE empírico no la tiene.

## 6. Hoja de discusión para tres personas

Actualización 2026-10-17: Camilo comunicó acuerdos parciales en el
[registro vigente](05_TEAM_DECISIONS.md). Las tres revisiones conjuntas y la
autorización de ejecución siguen pendientes; esta tabla no registra votos.

Completar columnas por separado y después acordar decisiones. Esta hoja evalúa datos; la puntuación científica está en el dictamen del comité.

| Decisión | Revisor 1 | Revisor 2 | Revisor 3 | Acuerdo y evidencia |
|---|---|---|---|---|
| Contraste primario y población objetivo | Pendiente | Pendiente | Pendiente | |
| Edad y política de soporte predefinidas | Pendiente | Pendiente | Pendiente | |
| QC defendible con los archivos disponibles | Pendiente | Pendiente | Pendiente | |
| Covariables imprescindibles y efecto sobre el estimando | Pendiente | Pendiente | Pendiente | |
| Necesidad de datos externos | Pendiente | Pendiente | Pendiente | |
| Hallazgo negativo útil/publicable | Pendiente | Pendiente | Pendiente | |
| Evidencia que impediría continuar | Pendiente | Pendiente | Pendiente | |

La revisión asistida por agentes no equivale a tres revisores humanos independientes. El equipo puede aceptar, cambiar o rechazar el dictamen. No se garantiza novedad ni aceptación editorial.
