# Dictamen independiente de revisión de pares

Fecha: **2026-10-11**. Destinatarios: equipo de tres personas y responsable de redactar el protocolo. Es una evaluación asistida con tres perspectivas disciplinarias; no representa tres revisores humanos ni una revisión editorial real. Se realizó después de cerrar la etapa de evidencia y sin modificar su índice. No se ajustaron modelos ni se ejecutaron simulaciones.

**Dictamen: pasa a elaboración de propuesta únicamente la versión revisada descrita aquí.** La comparación genérica de «proteger interacciones para recuperar señal» no pasa por innovación/publicabilidad insuficientes. Esta propuesta estudia **calibración de intervalos y elegibilidad de un contraste de interacción condicionado al diseño**, incorpora un control de equivalencia algebraica y deja ABIDE como diseño de referencia y demostración empírica secundaria. El pase permite redactar el protocolo; no demuestra resultados, potencia, originalidad exclusiva ni probabilidad de aceptación.

Convenciones: **V** comprobación local; **F** fuente primaria; **I** juicio/propuesta; **U** pendiente. Base revisada: [candidato y evidencia](01_EVIDENCE_AND_CANDIDATES.md), [cobertura de búsqueda](../../literature/README.md), [artículos](../../literature/papers.csv), [datasets](../../literature/datasets.csv) y [software](../../literature/software.csv).

## 1. Verificación independiente de datos antes de puntuar

Se recontaron directamente los CSV fuente/derivado y los archivos `.stats` con biblioteca estándar, sin reutilizar los conteos como única evidencia. Se inspeccionó además la documentación primaria de QA descargada.

| Requisito | Comprobación independiente | Implicación |
|---|---|---|
| Identificadores y diseño | CSV fuente: 1.112 filas, 106 columnas, 1.112 `SUB_ID` únicos; sin vacíos/-9999 en `SUB_ID`, `AGE_AT_SCAN`, `SITE_ID`, `SEX`, `DX_GROUP` | **V:** suficiente para construir un diseño observado; no prueba separación de efectos de sitio/biología |
| Resultado cortical | 2.070 archivos; tabla bilateral: 1.035 filas, 80 columnas, 68 grosores regionales y 1.035 IDs únicos | **V:** acceso real, sin descarga nueva para el núcleo metodológico |
| Cuatro grupos bilaterales | ASD masculino 443; ASD femenino 62; control masculino 435; control femenino 95 | **V:** interacción formulable; subgrupo femenino autista limita estimación |
| Completos positivos/finitos | 1.027: 437/62/433/95 en el mismo orden | **V:** completitud no equivale a calidad cortical |
| Filtro ilustrativo de anatomía | 773: 323/52/318/80 | **V:** filtro reduce representación; todavía no constituye QC de superficies |
| Soporte observado por sitio | Tabla independiente de evidencia: 14 sitios con cuatro grupos y 11 intersecciones min–max de ancho positivo en completos; 12 y 9 bajo filtro ilustrativo | **V:** alerta de soporte; rangos no prueban densidad local, rango matricial ni potencia |
| Edad y lote | `AGE_AT_SCAN` y `SITE_ID`; 20 etiquetas observadas | **V/U:** edad transversal y etiqueta administrativa; no equivale a pubertad, cambio individual ni escáner único |
| QC requerido para biología | Raters 2/3 revisaron anatomía cruda, según [PCP QA](https://preprocessed-connectomes-project.github.io/abide/quality_assessment.html) | **F/U:** no hay certificación de reconstrucción cortical ni Euler verificado |
| Verdad y replicación | No hay señal técnica/biológica verdadera ni réplica ABIDE II verificada | **U:** verdad solo en simulación; II no puede sostener una promesa de validación externa |

La codificación `SEX` es binaria según el repositorio; las etiquetas de esta tabla describen esa variable, sin asumir identidad de género. Fuentes de acceso: [ABIDE I](https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html) y [PCP](https://preprocessed-connectomes-project.github.io/abide/download.html). No se usaron cuentas. **F/V**

**Conclusión de datos:** el diseño de simulación y una comparación descriptiva secundaria son factibles. Una investigación confirmatoria de curvas triples regionales en mujeres autistas, especialmente con cuatro curvas suaves complejas, no queda respaldada por estas verificaciones. Restringir a sitios con cinco personas por celda tampoco garantiza suficiencia: después del filtro ilustrativo solo NYU, UM_1 y YALE cumplen ese conteo. **I/V**

## 2. Perspectiva estadística: objeciones mayores

### M1. Recuperación puntual puede ser una identidad, no una contribución

En el caso aditivo OLS, sin shrinkage ni corrección de escala, ajustar conjuntamente `y = Xβ + Zγ + ε`, restar `Zγ̂` y volver a ajustar exactamente `X` puede devolver `β̂` por las ecuaciones normales. Esto requiere parametrización identificable y las mismas filas, pesos y columnas. No se extiende automáticamente a EB ComBat, cambios de escala, bases penalizadas o diseños distintos. **I**

La igualdad de estimaciones con inferencia diferente está explicada en §2.1 de [Li, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10449015/). La incertidumbre de dos etapas tiene antecedentes: su mera observación no sería nueva. **F**

**Cambio obligatorio:** incluir este caso límite como control numérico/algebraico con tolerancia declarada. Separar tres preguntas: equivalencia de estimación, efecto de especificar la media protegida y calibración de incertidumbre. Si una rama coincide por construcción, reportarla como control; no presentarla como método que recupera mejor una interacción.

### M2. Estimando y población deben preceder a métodos y significancia

Mantener `C_r(a)` y `Θ_r(a0,a1) = C_r(a1) − C_r(a0)` definidos en la evidencia, pero precisar si `μ` representa una media estandarizada sobre sitios observados y qué supuestos permiten compartir asociaciones entre sitios. Estimar con una población y comparar contra la verdad de otra produce un falso sesgo. **I**

**Cambio obligatorio:** objetivo primario de simulación condicionado a una matriz de covariables fija y sitios observados. Fijar pesos comunes de sitios para los cuatro grupos, edades del contraste y codificación de factores dentro de cada diseño. Todos los métodos reciben exactamente esas filas/objetivo. Un diseño restringido es otro objetivo, con su propia verdad; se compara rendimiento dentro de él y nunca cambios de estimando como pérdida por armonización. El efecto técnico no se identifica en ABIDE solo por introducir `SITE_ID`.

Las edades 10/16 no están aprobadas por soporte. Una regla basada únicamente en covariables debe elegir el intervalo antes de examinar grosores/efectos; si no existe intervalo defendible, el contraste empírico dependiente de edad se omite. Elegibilidad necesita recuentos locales, rango matricial, condicionamiento y concentración/influencia del contraste, no únicamente intersección min–max. Sin supuestos de intercambio entre centros, celdas sexo×diagnóstico vacías no permiten medias de sitio específicas. **I**

### M3. Bootstrap completo no implica bootstrap válido

Reestimar armonización reduce una omisión, pero no garantiza cobertura. Con objetivo condicionado a covariables/sitios, un bootstrap de pares dentro de sitio cambia la composición del diseño; no corresponde automáticamente a esa inferencia. Un bootstrap de centros tiene otro objetivo y muy pocos centros efectivos para generalizaciones fuertes. **I**

**Cambio obligatorio:** distinguir intervalos ingenuos, referencia de una etapa y una estrategia de remuestreo completo que conserve el diseño objetivo, por ejemplo bootstrap paramétrico bajo un modelo generador explícito. Debe mantener dependencia regional y heterogeneidad técnica; su validez se mide en simulación bajo especificación correcta e incorrecta. No asumir que este bootstrap es robusto ni que sustituye un tratamiento bayesiano completo. Si se usa remuestreo de pares como sensibilidad, etiquetar el cambio de objetivo y posibles réplicas singulares.

Congelar regla de soporte, bases y población una vez construida la matriz para el objetivo condicionado. Si se pretende inferencia sobre selección de esas reglas, simular y reestimar también esa selección; es una extensión fuera del núcleo. Fallos/singularidades deben contarse sobre todas las réplicas, sin retirarlos silenciosamente del denominador.

### M4. Comparadores y generador deben permitir perder a la hipótesis

El núcleo necesita: una etapa con ajuste de sitio, armonización con edad compartida y armonización de la misma familia con interacción protegida. El modelo biológico final debe ser idéntico en los tres; conservar efectos principales y todos los términos de orden inferior a la interacción. Bases de dimensión reducida y parametrizaciones fijadas, sin selección por p-valores. **I**

Una etapa con interceptos de sitio y errores homocedásticos no es un rival suficiente para un generador con escalas técnicas distintas. **Cambio obligatorio:** referencia de una etapa que permita esas escalas, o explicar y complementar su limitación con una referencia/oráculo de varianza conocida en simulación. El oráculo es un límite diagnóstico, no un método aplicable a datos reales. No reemplazar el comparador viable por el oráculo.

Separar núcleos con y sin efecto técnico y escenarios aditivos frente a localización/escala. Incorporar nulo y alternativa conocida, curva común mal especificada y cambios en correlación regional/calibración. El generador no debe ser exclusivamente el modelo de la estrategia protegida. No estimar una «verdad ABIDE» de la salida de esa estrategia. Si se estudia varianza biológica por sexo/diagnóstico, incluir ComBatLS; alternativamente, dejar esa extensión fuera del núcleo y reconocer la limitación. **I**

## 3. Perspectiva de datos corticales y autismo

**M5. QC de superficies limita la demostración empírica.** Los `.stats` pueden ser completos y erróneos. Sin superficies/QC específico, la demostración debe describirse como sensibilidad metodológica de derivados heredados, sin conclusiones sobre neurobiología. El objetivo metodológico primario puede continuar sin resolver ese QC: usa ABIDE para calibrar diseño y escalas aproximadas, no para establecer la verdad biológica. Una afirmación anatómica confirmatoria requeriría otro protocolo de QC y posiblemente adquisición/reprocesamiento autorizado. **I**

**M6. No convertir edad transversal en desarrollo.** Hay evidencia biológica primaria de una interacción triple en datos longitudinales con otra muestra/procesamiento ([Andrews, 2024](https://www.nature.com/articles/s41380-024-02592-8)); eso motiva el contraste pero no hace a ABIDE una réplica longitudinal. No estudiar poda sináptica, pubertad ni trayectorias individuales con estas columnas. **F/I**

**M7. Selección y covariables.** El filtro dual-rater altera fuertemente algunos sitios; STANFORD queda con una sola fila. En ese conjunto, un método puede no admitir el lote y estimar su escala sería imposible. No tratar filtros como muestras listas para ComBat. Predefinir política de lotes unitarios y recalcular población/soporte para todos los comparadores; no rellenar parámetros técnicos ficticios. FIQ/medicación/ADOS no deben hacerse requisitos del benchmark. Incorporarlos en una extensión empírica cambia el objetivo y exige evaluación de faltantes/confusión. **V/I**

**M8. Unidad y multiplicidad.** Son personas, no hemisferios ni regiones independientes. La matriz de 68 características debe conservarse en armonización EB porque reducir regiones altera la estimación conjunta. Se pueden seleccionar unos pocos contrastes de evaluación antes del piloto para limitar coste, sin escogerlos después por efectos. Reportar métricas regionales y sus dependencias; intervalos puntuales al 95% no son cobertura simultánea de 68 regiones. Si se hace inferencia familiar, precisar error familiar/FDR y medirlo por réplica. **I**

## 4. Perspectiva editorial: aporte y vecinos más cercanos

La tabla contrasta objetivos, no reclama que cada suplemento haya sido descartado exhaustivamente.

| Antecedente primario | Qué ya cubre | Qué podría aportar la propuesta revisada |
|---|---|---|
| [Sun, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9648725/) | Comparación cortical empírica; edad×diagnóstico y sexo×diagnóstico | Cobertura de un contraste triple conocido en diseños de soporte variable, sin identificar verdad empírica |
| [Reynolds, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10412957/) | Simulación ComBat, diagnóstico×edad e incertidumbre | Relación entre soporte de cuatro grupos, equivalencia puntual y calibración de un contraste definido; verificar suplementos antes del piloto |
| [Gardner, 2025](https://onlinelibrary.wiley.com/doi/10.1002/hbm.70197) | Desbalance sexual y preservación de escala/centiles corticales | Inferencia de un contraste de media clínica, no replicar conservación normativa |
| [Li, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10449015/), Nygaard en el índice | Problema de dependencia/inferencia de dos etapas y relevancia del diseño | Cuantificarlo para un objetivo neuroimaginológico con diseño observado y una decisión de elegibilidad |
| [Bayer, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC7614761/), [Marzi, 2024](https://www.nature.com/articles/s41597-023-02421-7) | ABIDE/modelado normativo; soporte de edad, simulaciones y otros fines | Evaluación de inferencia de interacción, con referencia de una etapa y misma población entre métodos |

Se reabrieron independientemente los textos de Li, Sun y ComBatLS. La apertura directa de Reynolds/DOI falló; sus afirmaciones se mantienen al nivel declarado por el índice, no como suplemento inspeccionado. En ComBatLS el beneficio fue menos marcado para grosor que para otras medidas: evita anticipar fallos universales de ComBat sobre sexo. **F/U**

**M9. La intersección de ingredientes no basta para novedad.** Añadir sexo a una simulación edad×diagnóstico es incremental. El resultado editorial defendible sería una evaluación falsable que distinga: contraste no estimable, estimable con incertidumbre mal calibrada y estimable/calibrado, junto con diagnósticos del diseño que ayuden a decidir cuándo usar armonización o una etapa. Es innovación de evaluación/aplicabilidad; no un algoritmo nuevo. **I**

**Cambio obligatorio:** el protocolo debe enlazar cada salida con una decisión del analista. Para que sea algo más que una réplica, necesita estudiar si los diagnósticos predefinidos anticipan fallo de cobertura/error fuera de un único generador. Una regla elegida después de ver resultados se desarrolla en unas condiciones y se evalúa en otras condiciones/semillas separadas. No anunciar umbrales universales derivados de ABIDE ni inventar un mínimo muestral.

Un resultado nulo puede ser publicable si delimita equivalencia y calibración con precisión suficiente y aporta un recurso reproducible útil. «Ningún método gana» con intervalos Monte Carlo grandes o controles triviales no satisface ese estándar. La novedad permanece condicionada a la búsqueda dirigida documentada hasta 2026-10-11; no se garantiza originalidad ni publicación. **I/U**

## 5. Candidato revisado que sí se evalúa

**Pregunta revisada:** para un contraste de interacción edad×sexo×diagnóstico definido antes de examinar efectos y condicionado a sitios/covariables observados, ¿cuándo el soporte del diseño y la especificación de la media permiten estimación precisa, y cuándo los intervalos después de armonizar presentan cobertura distinta de su nivel nominal, incluso cuando sus estimaciones puntuales coinciden con una referencia de una etapa?

**Unidad de contribución:** mapa reproducible diseño → elegibilidad/equivalencia → calibración de inferencia. ABIDE I aporta un patrón real de escasez; simulación aporta verdad conocida; la comparación empírica ilustra sensibilidad sin decidir qué biología es verdadera. **I**

El protocolo debe incorporar M1–M9. El alcance principal se limita a contrastes de media, lotes observados, base lineal inicial y una extensión pequeña de curvatura, escenarios técnicos aditivos/localización-escala y dependencia regional. No incluye método nuevo, nuevas cohortes, normas clínicas individuales, centros nunca observados ni resultado anatómico confirmatorio. Esto mantiene la contribución metodológica si la demostración empírica triple resulta inelegible. **I**

## 6. Puntuación y puertas de evidencia

Escala: **1 muy bajo; 2 bajo; 3 medio; 4 alto; 5 muy alto**. Fórmula: `0,50 × factibilidad + 0,30 × publicabilidad + 0,20 × innovación`. Una media alta no compensa una nota inferior a 3 ni una debilidad fatal. Son juicios de mérito de diseño, no probabilidades de publicar.

| Versión | Factibilidad 50% | Publicabilidad 30% | Innovación 20% | Ponderado | Decisión |
|---|---:|---:|---:|---:|---|
| planteamiento inicial: proteger interacción y comparar resultados empíricos | 3 | 2 | 2 | 2,50/5 | **No pasa**: réplica/riesgo de circularidad; sin verdad empírica ni QC suficiente para descubrir biología |
| Propuesta revisada: elegibilidad y calibración condicionadas al diseño, con los cambios exigidos | 4 | 3 | 3 | 3,50/5 | **Pasa a propuesta**, con puertas de piloto y veto definidos abajo |

**Factibilidad 4 — alta para la propuesta revisada:** campos, participantes y archivos son reales y accesibles; no precisa neuroimágenes crudas ni cuenta nueva. La matriz es pequeña. La carga dominante de bootstrap anidado, rango/condicionamiento y versión funcional del software siguen sin medirse. La puntuación se refiere al benchmark acotado; la biología confirmatoria tendría factibilidad menor. Riesgo fatal para ese componente: exigir QC de superficie inexistente o curvas sustentadas en celdas sin información. La revisión evita hacerlo obligatorio para el núcleo.

**Publicabilidad 3 — media:** pregunta inferencial útil, comparadores pertinentes y posibilidad de resultado negativo informativo. Sus vecinos ya cubren piezas sustanciales y no existe evidencia de que el benchmark producirá una conclusión nueva. Riesgo fatal: solo reproducir un mecanismo conocido o mostrar una identidad como superioridad; falta de calibración/generadores alternativos; diferencias demasiado imprecisas para guiar una decisión. M1–M4/M9 eliminan esos errores de diseño, pero el piloto puede demostrar que no queda contribución suficiente.

**Innovación 3 — media y condicional:** originalidad candidata en la relación operativa entre soporte de cuatro grupos, equivalencia puntual y cobertura del contraste condicionado; no en ComBat, interacciones, bootstrap ni ABIDE. La revisión dirigida no identificó una réplica exacta de esta unidad de contribución, pero no se completó lectura de todos los suplementos cercanos. Riesgo fatal: antecedente que ya evalúe la misma decisión o resultados totalmente explicables por el caso límite conocido. Si aparece, baja a 2 y se detiene la síntesis de futuras versiones hasta rediseñar. El pase actual es defendible para redactar un estudio falsable, no una afirmación de novedad demostrada.

## 7. Condiciones obligatorias antes de ejecución y piloto

| Puerta | Evidencia/acción necesaria | Criterio de continuar o parar |
|---|---|---|
| G1. Protocolo aprobado | Equipo acuerda objetivo condicionado, pesos, bases, familias/contrastes y presupuesto | No ejecutar investigación antes de aprobación; documentar cambios de población |
| G2. Competidor decisivo | Inspeccionar métodos/suplementos de Reynolds y secciones cercanas; contrastar en tabla el mismo estimando/decisión | Si ya cubren la unidad de contribución, **parar y reevaluar innovación**, no compensar con más métodos |
| G3. Elegibilidad | Evaluar covariables sin buscar significancia: soporte local, lote unitario, rango y condicionamiento de matriz estandarizada, influencia del contraste | Si falta rango, no estimar ese contraste. Umbrales de densidad/condicionamiento/influencia se predeclaran y se someten a sensibilidad; cinco por celda no es un aval |
| G4. Control algebraico | Caso aditivo OLS, mismo diseño/modelo/pesos; tolerancia de error numérico fijada | Diferencia inesperada implica error de implementación hasta explicar su causa; una igualdad esperada no es un hallazgo de superioridad |
| G5. Núcleo de software | Fijar versión/commit, comprobar fórmula realmente protegida y contrastes, registrar singularidades/fallos | Si la capacidad documentada no funciona, reducir familia/modelo o parar; no sustituirla silenciosamente por otra pregunta |
| G6. Recursos | Medir tiempo/RAM de un lote pequeño que incluya reestimación de armonización y 68 características | Extrapolar coste de simulaciones × remuestreos antes de expandir. Reducir escenarios/contrastes de evaluación, sin tratar subconjunto de regiones como EB idéntico |
| G7. Precisión Monte Carlo | Separar prueba técnica pequeña de evaluación final; fijar precisión deseada y regla de ampliación | Para cobertura 0,95, `R=1.000` tiene MCSE aproximado 0,0069; no llamar evidencia calibrada a 100 réplicas. Informar intervalos MC y fallos con denominador total |
| G8. Calibración y utilidad | Evaluar sesgo/RMSE/cobertura/error tipo I y anchura, tanto cuando supuestos favorecen como cuando perjudican cada estrategia | No exigir que gane protección; exigir una conclusión precisa que cambie una decisión, o caracterice sus límites. Si solo quedan equivalencias conocidas/ruido, **parar como candidato a artículo** |
| G9. Demostración empírica | Elegibilidad sin efectos; misma población/modelo; sensibilidad de QA; ausencia de QC cortical explícita | Si `Θ` es inelegible, omitirlo o usar `C` promedio predefinido como ilustración. Si solo cambia esa rama, el benchmark puede seguir; no rescatar un descubrimiento biológico |

El criterio de calibración no es «no rechazar 0,95»: intervalos Monte Carlo amplios también pueden no rechazarlo. Predeclarar margen tolerable, precisión de evaluación y cómo se tratan múltiples regiones/escenarios. Para amplitud/error, definir una escala de referencia y tolerancia de relevancia antes de ver qué método gana. La magnitud de señal pequeña/moderada simulada es un supuesto, no un umbral clínico validado. **I**

No se prescribe una cantidad universal de réplicas bootstrap: su resolución de colas y estabilidad necesitan sensibilidad, especialmente si se anida en numerosas simulaciones. No comprar cómputo ni ampliar descargas para solucionar un coste no medido. **I**

## 8. Cambios menores y artefactos de salida

- Mantener explícito FreeSurfer 5.1/Desikan–Killiany y unidades mm; limitar generalización a otros atlas/procesamientos.
- No usar «eliminación de sesgo biológico» ni número de hallazgos significativos como criterio de éxito. Reducción de clasificación de sitio es auxiliar y puede reflejar composición de la muestra.
- Presentar diagrama de selección, soporte por grupo/sitio/edad, diferencias entre QC ilustrativo y cortical, fórmulas protegidas completas y mapa de extrapolación.
- Entregar matriz de escenarios con verdad generada, tabla de contrastes/objetivos, control algebraico, reporte de fallos y resultados con error Monte Carlo; el equipo debe poder repetirlos desde el manifest.
- La respuesta a revisión debe mapear M1–M9/G1–G9 a decisiones concretas del protocolo, y marcar lo que sigue pendiente; no afirmar que redactar una regla equivale a validarla.

**Recomendación final del comité:** elaborar únicamente la propuesta revisada bajo las condiciones anteriores. Rechazar la formulación genérica y cualquier propuesta que convierta diferencias empíricas en pérdida biológica conocida. La incertidumbre decisiva es si la relación soporte → calibración aporta una decisión más allá de los competidores; la resuelven la inspección dirigida pendiente y un piloto autorizado con controles, no una media ponderada favorable.
