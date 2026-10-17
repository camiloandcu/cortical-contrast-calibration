# Propuesta: elegibilidad y calibración de contrastes corticales

**Protocolo propuesto para revisión del equipo — 2026-10-11.** Destinatarios: las tres personas que decidirán objetivo, alcance y ejecución. No contiene resultados de modelos o simulaciones. **V** = verificado localmente; **F** = fuente primaria; **I** = decisión metodológica propuesta; **U** = pendiente. Las decisiones que siguen son **I**, salvo indicación expresa.

**Título de trabajo:** *Cuándo es estimable y cuándo está calibrado un contraste edad × sexo × diagnóstico: evaluación de armonización cortical condicionada al diseño ABIDE I*.

**Actualización operativa — 2026-10-17:** los [acuerdos comunicados por Camilo](05_TEAM_DECISIONS.md)
conservan objetivo, comparadores y sensibilidad condicionada; proponen auditoría
de covariables antes de congelar elegibilidad. El [plan operativo](06_SCIENTIFIC_DEVELOPMENT_PLAN.md)
contempla tres meses y Colab gratuito de tres integrantes, con revisión conjunta.
No hay aprobación conjunta de G1 ni autorización del piloto; software, reglas,
precisión y coste finales siguen pendientes. Las secciones siguientes conservan
la especificación científica propuesta, sin resultados nuevos.

**Pregunta principal:** para un contraste de interacción definido antes de examinar efectos y condicionado a las covariables y sitios observados, ¿qué relación existe entre soporte del diseño, especificación de la media y cobertura de los intervalos después de armonizar, incluso cuando las estimaciones puntuales coinciden con un ajuste de una etapa?

El [comité independiente](review/02_PEER_REVIEW.md) admite **únicamente la propuesta revisada**, con factibilidad **4/5**, publicabilidad **3/5**, innovación **3/5** y ponderado **3,50/5**. La fórmula es `0,50F + 0,30P + 0,20I`; cada criterio debe alcanzar 3 y ninguna debilidad fatal se compensa por la media. El planteamiento inicial, centrado en «proteger interacciones y comparar significancia», falla publicabilidad e innovación. Este pase autoriza redactar una propuesta, no demuestra novedad, potencia ni probabilidad de aceptación.

**Meta acordada para una reevaluación posterior — 2026-10-12:** mantener el alcance actual y aspirar a factibilidad **4/5**, publicabilidad **4/5** e innovación **4/5** (ponderado **4,00/5**) si el piloto demuestra una contribución útil. Las notas actuales siguen siendo **4/3/3**. La meta requiere ejecución técnicamente viable dentro del presupuesto, conclusiones precisas que orienten una decisión analítica y utilidad de los diagnósticos en escenarios reservados, además de una diferencia defendible respecto de los antecedentes. Una revisión posterior deberá valorar esa evidencia; ejecutar el piloto o completar el protocolo no aumenta automáticamente las notas. Este acuerdo no autoriza ejecutar modelos ni simulaciones.

## 1. Aporte y fundamento

El producto científico será un **mapa reproducible diseño → elegibilidad → equivalencia puntual → calibración**, dirigido al analista de datos multicéntricos. Debe permitir decidir entre estimar un contraste con incertidumbre defendible, reducir el objetivo o declararlo no estimable. ABIDE aporta una estructura real de escasez; la simulación aporta verdad conocida; la demostración empírica ilustra sensibilidad.

No se propone un algoritmo nuevo. Interacciones, ComBat, incertidumbre de dos etapas y desbalance por sexo ya tienen antecedentes. El valor candidato consiste en vincular diagnósticos previos al análisis de efectos con el rendimiento de **un mismo contraste y población**, y comprobar esa relación en condiciones no utilizadas para elegir una regla. La [búsqueda dirigida](../literature/README.md) no demuestra originalidad exclusiva.

| Antecedente primario | Qué evita reclamar la propuesta revisada | Diferencia candidata que debe sobrevivir al piloto |
|---|---|---|
| [Sun, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9648725/) | Primera comparación cortical de interacciones entre armonizaciones | Verdad generada, elegibilidad y cobertura del contraste triple |
| [Reynolds, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10412957/) | Primera simulación de interacciones o incertidumbre ComBat | Relación soporte de cuatro grupos → calibración y decisión; [texto y suplemento ya inspeccionados](review/04_COMPETITOR_VERIFICATION.md) |
| [Gardner, 2025](https://onlinelibrary.wiley.com/doi/10.1002/hbm.70197) | Primer estudio de desbalance sexual o preservación de escala | Contraste clínico de media; escala biológica diferencial fuera del núcleo |
| [Li, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10449015/) y [Nygaard, 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4679072/) | Descubrimiento de dependencia o confianza excesiva de dos etapas | Cuantificación orientada a un contraste cortical y diagnóstico de elegibilidad |
| [Bayer, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC7614761/) | Primera comparación ABIDE de una frente a dos etapas | Contrastes de media en vez de puntuaciones normativas individuales |

**Motivación biológica F:** [Andrews, 2024](https://www.nature.com/articles/s41380-024-02592-8) estudió edad × sexo × diagnóstico con MRI longitudinales de otra cohorte y procesamiento. Esto justifica la relevancia de la pregunta; ABIDE transversal no replica cambios intraindividuales. Esta propuesta no estudia poda sináptica, pubertad ni mecanismos causales.

## 2. Datos, unidad y población

**V:** [ABIDE I PCP](https://preprocessed-connectomes-project.github.io/abide/download.html) está descargado: CSV de 1.112 personas/106 columnas y 2.070 archivos FreeSurfer **5.1/aparc–Desikan–Killiany**, 68 medidas bilaterales de `ThickAvg`, en mm. [Manifest y hashes](../data/download_manifest.csv), [auditoría de columnas](04_COLUMN_INVENTORY.md) y [revisión de datos](01_DATASET_REVIEW.md) permiten verificarlo. No se necesita una nueva cuenta para el núcleo.

| Flujo V | ASD masculino | ASD femenino | Control masculino | Control femenino | Total |
|---|---:|---:|---:|---:|---:|
| Ambos archivos regionales | 443 | 62 | 435 | 95 | 1.035 |
| 68 medidas positivas/finitas | 437 | 62 | 433 | 95 | 1.027 |
| Además, ambos raters anatómicos `OK` | 323 | 52 | 318 | 80 | 773 |

La unidad es la **persona** (`SUB_ID`/`FILE_ID`); hemisferios y regiones son medidas dependientes. `SEX` usa la codificación binaria del proveedor y `DX_GROUP` autismo/control; no se extrapola a categorías no recogidas. `AGE_AT_SCAN` es edad transversal; `SITE_ID` tiene 20 etiquetas y es un proxy administrativo de lote, sin identidad de escáner verificada por participante. **V/U**

El diseño de referencia de simulación procede de las **1.027 filas completas**, no de una selección por efectos. El filtro de 773 es otra población para sensibilidad. Solo 14/20 sitios completos tienen cuatro grupos, y 11 tienen intersección min–max de edad de ancho positivo; son alertas, no prueba de soporte o potencia. [Conteos](../literature/abide_design_site_groups.csv) y [edades](../literature/abide_design_age_cells.csv). **V**

**QC F/U:** [PCP QA](https://preprocessed-connectomes-project.github.io/abide/quality_assessment.html) describe revisión de anatomía original por los raters 2/3; no certifica superficies corticales. Completitud y valores positivos tampoco lo hacen. El núcleo metodológico puede usar este diseño sin afirmar biología ABIDE verdadera. La rama empírica queda como sensibilidad de derivados heredados; una conclusión anatómica confirmatoria exigiría QC de superficies y un alcance distinto.

FIQ, ADOS, medicación y movimiento funcional no son requisitos del benchmark. Sus faltantes y pertinencia son diferentes por sitio/grupo; incorporarlos cambiaría selección y estimando. ABIDE II, T1 originales y reprocesamiento no son dependencias ni réplica prometida; [acceso manual y límites](02_DOWNLOAD_GUIDE.md).

## 3. Estimando: qué se compara exactamente

Para cada diseño `D`, fijar filas `i`, edades `a_i`, sitio `j_i`, sexo `s_i` y diagnóstico `d_i`. Los sitios son los observados, no una muestra aleatoria de todos los escáneres. Sean `w_j = n_j/N` las proporciones **totales** de sitio en ese diseño, iguales para los cuatro grupos, con suma 1. No usar pesos propios de cada sexo/diagnóstico.

En simulación, `m_rj(a,s,d)` es la media estructural generada sin la perturbación técnica especificada. Definir `μ_r(a,s,d;D) = Σ_j w_j m_rj(a,s,d)`. El objetivo es una asociación estandarizada, no un efecto causal. En el núcleo las asociaciones biológicas se comparten entre sitios: `m_rj = b_rj + f_r(a,s,d)`; un intercepto común de sitio cancela en la diferencia de diferencias. Esta suposición permite combinar celdas vacías; no las convierte en observaciones existentes.

```text
C_r(a;D) = [μ_r(a,femenino,ASD;D) − μ_r(a,femenino,control;D)]
         − [μ_r(a,masculino,ASD;D) − μ_r(a,masculino,control;D)]
Θ_r(D)   = C_r(a1;D) − C_r(a0;D)
```

`Θ` expresa un cambio transversal de una diferencia de diferencias, en mm. No es una tasa longitudinal. Si existen asociaciones biológicas específicas de sitio, el núcleo compartido puede fallar; la sensibilidad correspondiente debe generar y evaluar el mismo promedio de sitios, no redefinir silenciosamente el objetivo. Sin intercambio/modelo compartido, una celda vacía no identifica una media específica de sitio.

En ABIDE, el contraste ajustado se define mediante el mismo modelo y estandarización, **sin identificar un componente técnico verdadero**. Ajustar `SITE_ID` no separa automáticamente diferencias técnicas y composición clínica. La interpretación depende de modelo, selección y soporte.

Un diseño restringido tiene sus propios `w`, edades y verdad. Evaluar sesgo contra esa verdad; no interpretar diferencias entre diseños como pérdida de señal por armonización. El control balanceado es artificial y no aumenta la muestra real.

## 4. Elegibilidad sin mirar efectos

La primera fase usa únicamente identificadores/covariables y reglas de integridad/QC. Generará una ficha por diseño con celdas sitio × sexo × diagnóstico, bins de edad de 2 años, vacíos locales, rango, singularidades, condicionamiento y concentración de información del contraste.

Usar la matriz **conjunta** `W=[X,Z]`: X contiene la media biológica jerárquica descrita en §5; Z contiene los interceptos de sitio parametrizados con una referencia y sin duplicar el intercepto de X. El contraste conjunto `l_W` agrega ceros para los coeficientes de sitio. Examinar X por separado no detectaría confusión con sitio.

1. Codificar factores, centrar/escalar edad y fijar referencia de sitio; construir W sin interceptos redundantes. Exigir rango completo. En el diseño estándar, usar tolerancia relativa de rango `10⁻¹⁰` y comparar `10⁻⁸/10⁻¹²` como sensibilidad numérica; no son umbrales clínicos.
2. Diagnosticar W estandarizada mediante valores singulares/condición. Si `q_i` es la fila conjunta como vector columna, calcular contribución por persona `h_i = l_W'(W'W)⁻¹q_i`; resumir `h_i²/Σh²` por sitio/grupo. Contraste y coeficientes se transforman coherentemente al estandarizar columnas. Son diagnósticos de diseño bajo pesos unitarios, no garantías con escalas desconocidas.
3. Buscar ventanas contiguas en bins de 2 años usando la distribución agrupada de edades: candidata inicial entre percentiles 10/90 y ventanas interiores. Registrar recuentos de los cuatro grupos y cuántos sitios aportan cada grupo. Preferir la ventana más amplia que cumpla las reglas acordadas; desempatar por menor concentración del contraste. Todo ello precede a los grosores/efectos.
4. Elegir `a0/a1` como percentiles 25/75 de la edad conjunta **dentro de esa ventana**, redondeados a 0,1 años; exigir separación positiva y cobertura local alrededor de ambos. No fijar 10/16 por conveniencia biológica. Congelar filas, pesos, edades, base y reglas para la inferencia condicionada.

**Pendiente de acuerdo G3:** los mínimos de recuento local, máximo de condición y concentración aceptable se elegirán antes de resultados. En vez de declarar «cinco personas por celda es suficiente», comparar una grilla finita propuesta: recuento por grupo/bin `3/5/10`, condición `10²/10³/10⁴` y máxima concentración por sitio `0,25/0,50`. Son candidatos de ingeniería estadística, no avales de precisión ni reglas aprobadas. El equipo escogerá una configuración principal antes del piloto y evaluará sensibilidad; si ninguna preserva información suficiente, no forzar elegibilidad empírica.

El diseño observado de simulación puede mantenerse como escenario de **escasez**, aunque una regla lo declare inelegible: esa decisión es un resultado a evaluar, no motivo para borrar escenarios difíciles. Si la matriz no tiene rango, registrar «no estimable», sin fabricar un intervalo. Diferenciar elegibilidad algebraica, soporte de predicciones y precisión; un criterio no sustituye a otro.

**Lotes unitarios:** no estimar una varianza propia con una persona ni inventar escala. Para cualquier diseño con `n_j < 2`, el núcleo común excluye ese lote para **todos** los métodos y redefine población/pesos; se documenta la exclusión y se vuelve a auditar soporte. El filtro ilustrativo deja STANFORD con una fila. No fusionar centros por conveniencia. La matriz de fallos conservará el diseño original como antecedente.

Una regla optimizada usando rendimiento simulado se considera **desarrollada**, no validada. Separar escenarios/semillas de desarrollo y evaluación; congelarla antes de abrir los resultados reservados. El banco de evaluación deberá incluir distinta correlación y curvatura/heterogeneidad, no solo nuevas semillas del mismo generador. Si no generaliza, entregar diagnósticos continuos y abstenerse de recomendar un umbral universal.

## 5. Modelos y comparadores centrales

Edad inicial lineal: `A=(a−centro)/escala`. Modelo biológico común completo por región:

```text
Xβ = β0 + βA A + βS S + βD D
   + βAS A·S + βAD A·D + βSD S·D + βASD A·S·D
```

Codificar `S=1` femenino y `D=1` ASD. Con edad lineal, `Θ = βASD·(a1−a0)/escala`. La extensión pequeña reemplaza `A` por una base común de dimensión 2 (lineal + cuadrática centrada/ortogonalizada), y **cada** función de base interactúa con S/D incluyendo todos los términos inferiores. No cuatro curvas suaves de complejidad libre; no selección por p-valores. Misma `X`, contraste y filas en los tres comparadores.

| Código | Procedimiento puntual | Incertidumbre a comparar |
|---|---|---|
| E1 | Una etapa sobre grosor original: `Xβ + Zγ`; GLS factible con escala residual propia de sitio, estimada iterativamente | Intervalo convencional de GLS y remuestreo completo; convergencia/escalas pequeñas explícitas |
| H0 | ComBat de localización/escala, protegiendo solo `1 + base(edad) + S + D`; después ajustar la **X completa** | Intervalo final ingenuo; intervalo de todo el procedimiento |
| H1 | Misma familia, estimación EB y 68 características que H0, protegiendo la **X completa**; mismo ajuste final | Los mismos dos intervalos; no superioridad anticipada |
| O | Solo simulación: ajuste de una etapa con varianzas técnicas conocidas | Oráculo diagnóstico de precisión/calibración, nunca reemplazo de E1 aplicable |

`Z` representa interceptos de los sitios observados, parametrizados de forma identificable. E1 admite heteroscedasticidad técnica y no es un rival homocedástico artificialmente débil. GLS debe estimar escalas, con límites positivos y criterio de convergencia predeclarados; si falla en lotes pequeños, cuenta como fallo. El oráculo muestra cuánto se pierde por estimar esas escalas y no se presenta como disponible en ABIDE.

H0/H1 eliminan/corrigen el término de lote y ajustan `X` a la salida; E1 lo ajusta conjuntamente. La diferencia intencionada es tratamiento del lote/media protegida, no cambiar el modelo biológico final. Mantener las **68 regiones** en la estimación EB, aunque se evalúen pocos contrastes principales: armonizar solo tres regiones no reproduce ese EB.

**Control M1/G4:** en un escenario aditivo OLS sin EB, sin escalado y con mismas filas/pesos, ajustar `y=Xβ+Zγ+ε`, restar `Zγ̂` y ajustar `X`. Comprobar recuperación de `β̂` por ecuaciones normales con tolerancia `10⁻⁸·max(1,|β̂|)` y sensibilidad numérica. Una diferencia inesperada exige revisar código/parametrización; una igualdad no demuestra un nuevo método. La inferencia puede diferir aunque el punto coincida. No extender la identidad automáticamente a ComBat EB, escalado o penalización. [Antecedente de inferencia F](https://pmc.ncbi.nlm.nih.gov/articles/PMC10449015/).

**Software U:** la capacidad está documentada en [ComBatFamily](https://github.com/andy1764/ComBatFamily) y [ComBatFamQC](https://stat.ethz.ch/CRAN/web/packages/ComBatFamQC/ComBatFamQC.pdf), pero no ejecutada. Antes del piloto fijar una implementación/version/commit que permita inspeccionar la matriz protegida; guardar fórmula, columnas y parámetros. Una lista de `smooth_terms` no crea por sí misma una interacción. No comparar paquetes/configuraciones distintos entre H0 y H1.

## 6. Verdad generada y matriz de escenarios finita

Generador básico, para las 68 regiones conjuntamente y filas fijas:

```text
Y_ir = m_rj(a_i,s_i,d_i) + γ_jr + δ_jr·ε_ir
ε_i ~ distribución multivariante centrada con matriz Σ (personas independientes)
```

Calibrar **solo escala, nivel de medida y dependencia plausibles** con los datos: medianas regionales, un ajuste de referencia sobre originales y covarianza residual regularizada positiva; congelar receta y parámetros. No tomar la salida H1 como biología verdadera. Los coeficientes de señales/interacciones y perturbaciones técnicas se fijan por el protocolo, no por qué estrategia gana. Repetir con covarianza identidad y correlación alterada para no depender de una calibración única.

En el núcleo, la varianza biológica residual es compartida entre grupos; `δ_jr` representa heterogeneidad técnica generada. Imponer escalas/correlaciones y magnitudes alrededor de la calibración, sin llamarlas parámetros verdaderos de ABIDE. Una primera grilla de señal usa `Θ/σ_r = 0` y `0,15`, con signos predefinidos por región; `σ_r` es la escala residual generadora. Es una alternativa metodológica supuesta, sin significado clínico establecido. Una señal sexo×diagnóstico **constante** con `Θ=0` comprueba que no se confunde C distinto de cero con cambio por edad.

Receta candidata a congelar: medias regionales basales iguales a medianas observadas y pendiente compartida `−0,15σ_r·A`; término constante `0,10σ_r·S·D`; alternativa añade `t_r·0,15σ_r·(A−A0)/(A1−A0)·S·D`, con `t_r=±1` alternado por orden alfabético de regiones. Por construcción Θ es el valor declarado. Técnica aditiva: `γ_jr=0,40σ_r·u_jr`, con `u` normales fijados por semilla y centrados con los pesos de sitio; escala: `δ_jr=exp(0,20v_jr)`, con `v` fijados/centrados, siempre positivos. Sin técnica, `γ=0/δ=1`. Estas magnitudes son supuestos acotados que el equipo puede cambiar **antes** de simular.

Dependencia base: `Σ=(1−λ)Σ_residual+λ·diag(Σ_residual)`, con λ=0,20 y ajuste mínimo de autovalores declarado si fuera necesario; conservar diagonal σ². Dependencia alternativa: misma diagonal y λ=1 (regiones sin correlación). Adversario nulo: añadir curva común `0,20σ_r·A²` omitiéndola en el ajuste lineal; adversario de alternativa: sustituir el término triple por `t_r·0,15σ_r·sin[π(A−A0)/(2(A1−A0))]·S·D`; su diferencia entre a0/a1 sigue siendo el Θ declarado. Así la verdad se calcula de la función generada y no del coeficiente ajustado. Una simulación con verdad fuera de base prueba estimación bajo mala especificación, no exclusivamente un fallo de armonización.

Balanceado artificial: en cada sitio usar `K_j=ceil(n_j/4)` edades dadas por cuantiles `(k−0,5)/K_j` de su distribución observada; asignar los mismos K valores a cada uno de los cuatro grupos. Su tamaño será `Σ_j4K_j`, explícitamente diferente del original si procede. Esto balancea grupos dentro de sitio y conserva heterogeneidad de edades entre sitios; no supone edades comunes en todos los centros. Las edades del contraste se seleccionan/congelan por diseño y sus verdades se recalculan.

| Bloque | Diseños/señales/técnica | Alcance obligatorio y decisión |
|---|---|---|
| A: núcleo inicial | Observado + balanceado artificial; Θ nulo/alternativa; sin técnica/localización+escala | 8 celdas; distinguir daño del procedimiento de dificultad del diseño |
| B: control aditivo | Observado; nulo/alternativa; sitio aditivo | 2 celdas más y control algebraico separado; no EB/escalado en el control |
| C: adversarios | Observado; Θ nulo con curva común cuadrática omitida y C constante; alternativa con curva fuera de base; técnica localización+escala | 2 celdas; todos reciben el mismo modelo final limitado; repetir con base 2 como análisis de reparación |
| D: soporte | Diseño restringido por regla congelada; nulo/alternativa; localización+escala | 2 celdas; calcular su propia verdad, nunca compararla como idéntico objetivo al completo |
| E: dependencia | Observado; nulo/alternativa; localización+escala; Σ alternativa | 2 celdas de evaluación reservadas; comprobar transportabilidad limitada del diagnóstico |

Total previsto: **16 celdas principales**, más comprobaciones de implementación y sensibilidad de base. A/B usan media dentro de base; C impide que el generador favorezca por construcción a H1; D/E prueban alcance de la decisión. La variante balanceada conserva un tamaño artificial declarado y sitios comparables, con cuatro grupos y edades comunes generados; no interpreta esas personas como datos nuevos. Guardar todas las covariables y verdades por diseño.

Para E y evaluación de reglas, reservar además una perturbación acotada de correlación/curvatura no utilizada en desarrollo; especificar sus parámetros antes del piloto final. Si el equipo elige optimizar una regla, deberá repartir las 16 celdas en desarrollo/evaluación y añadir solo las condiciones indispensables para que la evaluación no replique el generador de desarrollo. No ampliar un factorial indefinidamente.

**Fuera del núcleo:** heteroscedasticidad biológica por sexo/diagnóstico, pendientes técnicas por sitio, colas pesadas, transferencia a sitios nuevos y métodos normativos/fully Bayes. Si se añade heteroscedasticidad biológica, incluir **ComBatLS** y generadores que separen media/escala; no adjudicar la falta de preservación de escala a un método que solo la protege en media. Escenarios de asociaciones biológicas variables por sitio serían una extensión explícita de los supuestos de población.

## 7. Intervalos: todo el procedimiento, diseño conservado

Separar estimación puntual, anchura y cobertura. Un intervalo H0/H1 ingenuo trata la tabla armonizada como observaciones independientes y no propaga incertidumbre de armonización. No asumir que corregir esa omisión basta para calibrar.

**Estrategia completa propuesta:** bootstrap paramétrico de diseño fijo, basado en un modelo generador ajustado a los originales con X completa, interceptos/escalas de sitio y covarianza regional regularizada. Mantener filas/covariables/sitios y simular los 68 resultados juntos. Para cada réplica volver a estimar E1 o armonización EB H0/H1 y el ajuste final. Guardar fallo, convergencia, contraste y parámetros. La elegibilidad, bases y población permanecen fijas porque el objetivo es condicionado a ellas.

El generador bootstrap tiene objetivo plug-in `Θ̃` propio, **no verdad empírica ABIDE**. Para método m, usar distribución de error `e_m*=Θ̂_m*−Θ̃` y proponer intervalo `[Θ̂_m−q0,975(e*), Θ̂_m−q0,025(e*)]`. Esta construcción modela también sesgo del procedimiento; reportar corrección de centro separada de cambio de anchura. Evaluarla frente al intervalo ingenuo y a la variante básica centrada en `Θ̂_m`, para distinguir propagación de incertidumbre y corrección de sesgo. No atribuir toda mejora al bootstrap por sí solo.

En simulación evaluar esta receta con media bootstrap correctamente especificada (A/B/D) **e incorrecta** (C bajo base lineal). E cambia dependencia dentro de la familia multivariante: prueba estimación de covarianza y transportabilidad del diagnóstico, **no es por sí solo mala especificación**. Si se desea evaluar restricción incorrecta de covarianza, añadir una sensibilidad explícita que fuerce bootstrap diagonal con verdad correlacionada, separada del núcleo. Validez y estimación de escala/covarianza siguen siendo preguntas empíricas. La receta no reemplaza automáticamente inferencia bayesiana completa ni ofrece robustez general. Remuestreo de pares por sitio o centros cambia diseño/objetivo: queda fuera del análisis primario. Selección inferencial de reglas/base exigiría reestimar esa selección en otro protocolo.

Resolución inicial de colas: planificar `B=499` réplicas internas para evaluar coste y repetir un subconjunto predeclarado con `B=999`; no llamar suficiente a B antes de demostrar estabilidad de cuantiles/anchuras. Si la sensibilidad altera conclusiones, aumentar B o declarar la insuficiencia. Para cualquier fallo interno conservar denominador y tasa; ningún intervalo se calcula con menos del 95 % de B réplicas válidas. Ese 95 % es regla de implementación propuesta, sometida a sensibilidad, no criterio de validez estadística.

## 8. Métricas, precisión y multiplicidad

Por celda/método/región: sesgo firmado y relativo a σ, RMSE, anchura media/mediana, cobertura nominal 95 %, error tipo I bajo Θ=0 y tasas de no-identificabilidad/convergencia/fallo. Comparar métodos con mismas simulaciones/semillas para estimar diferencias pareadas. Reportar tanto rendimiento condicionado a éxito como cobertura operativa sobre **todas** las réplicas: un fallo no cuenta como cobertura conseguida. No eliminar escenarios incómodos ni ordenar métodos por cantidad de p-valores significativos.

Antes de ejecutar, fijar tres contrastes regionales principales por una regla anatómica independiente de resultados: **lh superiorfrontal, lh superior temporal y rh precuneus** (confirmar nombres literales en el inventario: `lh_superiorfrontal_thickness_mm`, `lh_superiortemporal_thickness_mm`, `rh_precuneus_thickness_mm`). Representan ejemplos anatómicos, no biomarcadores postulados. Armonizar siempre las 68. El informe descriptivo completo de las 68 será secundario, conservando dependencia.

Para calibración operacional, propuesta de margen de cobertura `[0,93;0,97]`: exigir que el intervalo Monte Carlo de cobertura quede dentro del margen, en lugar de «no rechazar 0,95». Es una tolerancia metodológica a aprobar, no nivel clínico. Declarar impreciso si el intervalo no permite clasificar. Propuesta de sesgo material: `|sesgo|/σ > 0,05`, con intervalo MC; tampoco es una diferencia clínicamente importante. Informar cifras continuas para evitar que un umbral oculte tendencias.

Piloto técnico: `R=30` por las primeras cuatro celdas observadas de A, con pocas réplicas internas, solo para depurar/costear. No evalúa calibración ni potencia. Evaluación prevista: al menos `R=1.000` por celda, ampliar según precisión hasta `R=2.000` y revisar presupuesto antes de más. Para cobertura 0,95, MCSE aproximado es 0,0069/0,0049 respectivamente; para todas las tasas reportar intervalos binomiales y tamaño válido/total. No prometer precisión suficiente para diferencias mínimas.

Se evaluarán contrastes predefinidos, no búsquedas de regiones. Cobertura 95 % regional es **puntual**. Para afirmar resultados sobre la familia de tres contrastes, agregar intervalos Bonferroni al `1−0,05/3` y medir cobertura familiar/error por réplica; la incertidumbre de cuantiles más extremos requiere comprobar B. No reclamar cobertura simultánea de las 68 con intervalos puntuales ni interpretar el resumen regional como 68 replicaciones independientes. No habrá decisiones editoriales basadas en un p-valor agregado de simulación.

## 9. Demostración empírica secundaria y resultados falsables

Aplicar protocolo de elegibilidad sin inspeccionar efectos; usar exactamente las mismas filas, X, edades, pesos y 68 características entre E1/H0/H1. Presentar estimaciones/diferencias e intervalos, sensibilidad a la selección anatómica ilustrativa, mapa de extrapolación y concentración por sitio. Cambios de población se presentan como análisis distintos, no como sesgo estimado. Dejar un centro fuera y volver a ajustar es sensibilidad a influencia; no es validación en escáneres nuevos.

Si Θ no tiene rango/soporte defendible o precisión, **omitir su interpretación empírica**. La alternativa secundaria es `C̄_r = Σ_k v_k C_r(a_k)` sobre una grilla común dentro del soporte, con pesos `v_k` de la distribución conjunta de edades fijados antes de efectos; también debe superar elegibilidad. No cambiarlo después para rescatar significancia. Si tampoco es viable, entregar solo auditoría empírica y benchmark simulado.

| Resultado posible | Interpretación y decisión |
|---|---|
| Punto protegido coincide con una etapa, pero intervalos ingenuos fallan en diseños escasos y la receta completa calibra en pruebas reservadas | Apoya utilidad de distinguir preservación/calibración y una recomendación condicionada; no demuestra biología perdida |
| Una etapa calibra y armonización no aporta precisión o falla bajo adversarios | Favorece recomendar una etapa para ese objetivo/diseño, aunque H1 preserve el punto |
| Diagnósticos previos anticipan fallo fuera del generador de desarrollo | Apoya la contribución operativa propuesta; documentar límites de transporte |
| Ningún método domina, pero límites/equivalencias están estimados con precisión y diagnósticos útiles | Resultado negativo metodológico potencialmente útil, sin garantía editorial |
| Solo se reproduce la identidad OLS o un antecedente; reglas no anticipan rendimiento, o diferencias quedan imprecisas | Debilita aporte: detener aspiración de artículo o reformular, sin añadir métodos para ocultarlo |
| Θ empírico es inelegible | Reduce demostración a C̄/auditoría; no invalida por sí solo el núcleo simulado ni permite una conclusión anatómica |

## 10. Plan finito, recursos y puertas de decisión

No se conoce tiempo/RAM, potencia empírica ni estabilidad del software. La tabla regional es pequeña, pero `celdas × R × B × procedimientos × 68` puede dominar coste. Medir hardware, tiempos por etapa, RAM máxima y almacenamiento en un lote pequeño; extrapolar con incertidumbre antes de autorizar evaluación. Ejecutar localmente primero, sin comprar cómputo ni descargar imágenes para un problema no medido.

| Fase / puerta | Entregable observable | Continuar / detener |
|---|---|---|
| G1: acuerdo del equipo | Contraste/pesos/edad, matriz de escenarios, reglas y presupuesto registrados | Aprobación explícita antes de instalar/ajustar/simular investigación |
| G2: competidor decisivo | [Texto/suplemento Reynolds inspeccionados](review/04_COMPETITOR_VERIFICATION.md); mantener comparación de la misma decisión frente a antecedentes | Esta inspección no identificó el mismo aporte conjunto; si otro antecedente lo cubre, reevaluar innovación y parar propuesta de artículo |
| G3: elegibilidad | Ficha de diseño y regla congelada; explícito objetivo tras excluir lotes unitarios | Sin rango, no estimar; sin soporte, limitar/omitir rama empírica |
| G4/G5: controles/implementación | Identidad OLS, matrices protegidas y recuperación de contrastes; versiones y fallos | Diferencia inexplicada o fórmula no funcional: reparar/reducir antes de continuar |
| G6: coste piloto | Tiempo/RAM medidos y proyección para 16 celdas, R/B | Reducir escenarios opcionales/contrastes evaluados; no alterar EB submuestreando ROIs |
| G7: precisión | Plan R/B y reporte de incertidumbre MC, incluidos fallos | Si no permite distinguir calibración, ampliar dentro de presupuesto o declarar inconcluso |
| G8: utilidad reservada | Sesgo/cobertura/anchura y evaluación no usada para elegir regla | Conclusión precisa que cambia decisión; si solo equivalencias conocidas/ruido, parar aspiración editorial |
| G9: rama empírica | Muestra/soporte/QC y contraste viable, sin afirmación anatómica confirmatoria | Θ, C̄ o auditoría según evidencia; no forzar descubrimiento biológico |

**Estado:** G2 tiene la comprobación dirigida de Reynolds completada; las puertas de aprobación, implementación, piloto y validación siguen **pendientes**. La inspección no encontró la misma unidad de evaluación en ese texto/suplemento, pero no demuestra ausencia en toda la literatura ni aumenta las puntuaciones. La [respuesta al comité](review/03_REVISION_RESPONSE.md) identifica qué cambia y qué evidencia falta por objeción.

Entregables de investigación si se aprueba: registro de protocolo/versiones; matriz de covariables/verdades; semillas y escenarios; controles; resultados con fallos/MC; cuaderno reproducible; propuesta de recomendación y sus límites. No se redactan resultados antes de obtenerlos.

## 11. Producto editorial y revisión de tres personas

Manuscrito candidato de evaluación metodológica: introducción centrada en decisión inferencial; definición de estimando/diseño y control algebraico; métodos de simulación/inferencia; rendimiento y fallos; demostración empírica limitada; discusión de supuestos/QC/transportabilidad. Su argumento debe sostenerse sin un hallazgo ASD significativo.

Figuras previstas, sujetas a resultados: (1) flujo y soporte de cuatro grupos; (2) mapa diagnóstico–cobertura con escenarios reservados; (3) sesgo/anchura/cobertura pareada por estrategia con intervalos MC; (4) estimaciones empíricas y extrapolación, si elegibles. Tablas: competidores/decisión nueva; escenarios y verdad; matriz protegida; fallos/coste; limitaciones. Son un plan de presentación, no figuras de resultados fabricados.

| Persona / responsabilidad propuesta | Decisiones a revisar ahora | Evidencia de aceptación |
|---|---|---|
| 1: estadística | Estimando condicionado, pesos, X, bootstrap, márgenes MC/multiplicidad | Fórmulas y supuestos aprobados; criterios de fallo entendibles |
| 2: neuroimagen/datos | Flujo, atlas/versiones, QC, soporte y significado transversal | Uso de archivos compatible con interpretación; rama empírica limitada |
| 3: aporte/ejecución | Diferencia con vecinos, coste máximo y utilidad de resultados negativos | Contribución falsable y finita; veta ampliaciones sin decisión nueva |

**Decisiones concretas del equipo:** aceptar o modificar Θ como objetivo simulado y la estandarización; aprobar regla de elegibilidad/edades y tres ROIs; confirmar comparadores/intervalos y 16 celdas; fijar tolerancias/presupuesto; decidir si incluir la demostración heredada sin QC de superficies. Estas decisiones preceden al desarrollo del análisis. La revisión asistida documentada no sustituye las tres opiniones humanas ni garantiza novedad/publicación.
