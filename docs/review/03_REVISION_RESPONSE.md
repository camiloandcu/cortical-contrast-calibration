# P5-R — Respuesta a la revisión y evidencia pendiente

Fecha: **2026-10-11**. Destinatarios: equipo de tres personas y revisor del protocolo. Basada en el [dictamen independiente](02_PEER_REVIEW.md), después de la [revisión de evidencia](01_EVIDENCE_AND_CANDIDATES.md). La [propuesta](../03_REFINED_P5_PROPOSAL.md) incorpora cambios **de diseño**; no afirma que hayan sido implementados, simulados o validados.

**Versión admitida:** P5-R, factibilidad 4/5, publicabilidad 3/5, innovación 3/5; ponderado 3,50/5. La formulación genérica no pasa. Estos juicios habilitan un protocolo falsable y pueden bajar ante un antecedente decisivo o un piloto sin aporte útil. Una puntuación global no compensa un criterio inferior a 3.

**Acuerdo posterior — 2026-10-12:** conservar el alcance de P5-R. La meta de reevaluación es **4/4/4**, ponderado **4,00/5**, condicionada a viabilidad técnica/coste comprobados, utilidad analítica precisa y validación en escenarios reservados con aporte adicional a los antecedentes. El dictamen actual permanece en **4/3/3**; la meta no es una puntuación obtenida ni aprobación de ejecución.

## Respuesta a las nueve objeciones mayores

Actualización operativa 2026-10-17: consultar [acuerdos vigentes](../05_TEAM_DECISIONS.md)
y [plan propuesto](../06_SCIENTIFIC_DEVELOPMENT_PLAN.md). Camilo conserva el
alcance y acepta una auditoría previa a la regla; la revisión de las tres
personas, G1 y ejecución científica siguen pendientes. La tabla siguiente
describe el estado científico previo a implementación, que no ha cambiado.

| Objeción del comité | Cambio concreto en la propuesta | Evidencia por producir y estado |
|---|---|---|
| M1. La recuperación puntual puede ser una identidad | §5: control OLS aditivo sin EB/escalado; mismas filas, pesos y columnas; tolerancia numérica; separar punto, media protegida e intervalos | **Pendiente:** derivación/ejecución del control y recuperación numérica. Una igualdad prevista será control, no superioridad |
| M2. Estimando/población preceden a métodos | §3–4: C(a), Θ, objetivo condicionado, pesos comunes `n_j/N`; edades por regla sin efectos; rango/condición/concentración de la matriz conjunta W=[X,Z]; cada restricción tiene verdad propia | **Pendiente:** equipo aprueba reglas/pesos; auditoría conjunta y edades finales. La media técnica verdadera no se identifica en ABIDE |
| M3. Bootstrap completo no garantiza validez | §7–8: generador paramétrico conserva covariables/sitios/68 medidas; reestima cada procedimiento; C prueba media incorrecta, E dependencia/transportabilidad dentro de familia; separa sesgo y anchura; registra fallos | **Pendiente:** cobertura y estabilidad de B. La receta es modelo-dependiente; no se presenta como robusta ni como inferencia sobre sitios nuevos |
| M4. Comparadores/generador deben poder refutar hipótesis | §5–6: E1 GLS con escalas de sitio, H0/H1 misma familia y X final, oráculo diagnóstico; escenarios sin técnica/aditivos/localización–escala, nulos/alternativa y adversarios | **Pendiente:** software y generadores; no se conoce ganador. Escala biológica diferencial requiere ComBatLS y extensión explícita |
| M5. QC de superficie insuficiente | §2/9: completitud y raters originales no certifican superficie; núcleo calibrado a diseño; empírico de derivados heredados sin conclusión anatómica confirmatoria | **Verificado:** origen de raters/cobertura; **pendiente:** QC de superficie solo si se amplía alcance. No necesario para verdad generada |
| M6. Edad transversal no es desarrollo | §1/3: contraste transversal, no tasa individual; Andrews motiva pregunta pero no convierte ABIDE en réplica longitudinal | **Resuelto en alcance propuesto:** prohibida inferencia de poda/pubertad/causalidad; equipo debe preservar interpretación en resultados |
| M7. Selección/covariables/lotes unitarios | §2/4/9: separar poblaciones, excluir `n_j<2` para todos en núcleo de escala, recalcular objetivo/soporte; FIQ/ADOS/medicación no requisitos | **Verificado:** STANFORD unitario bajo filtro ilustrativo; **pendiente:** política aprobada y matrices finales. No se fusionan centros ni inventan varianzas |
| M8. Unidad y multiplicidad | §5/6/8: personas independientes, dependencia de 68 ROIs y EB conjunto; tres contrastes predefinidos, cobertura puntual distinguida de familiar | **Pendiente:** confirmar nombres/selección antes del piloto, comprobar colas para Bonferroni y reportar fallos/MC. No 68 réplicas independientes |
| M9. Ingredientes conocidos no bastan para novedad | §1/4/9–11: aporte diseño→elegibilidad→calibración; regla congelada y escenarios reservados; resultados negativos solo útiles con precisión/decisión | **Completado:** [texto/suplemento Reynolds](04_COMPETITOR_VERIFICATION.md) no identifica misma unidad conjunta. **Pendiente:** piloto reservado y vigilancia de otros antecedentes. Si solo reproduce identidad/consecuencias conocidas, detener aspiración de artículo |

## Puertas G1–G9: comprobación bibliográfica y validación separadas

| Puerta | Registro mínimo requerido | Regla de decisión | Estado actual |
|---|---|---|---|
| G1. Aprobación | Objetivo, pesos, modelos, escenarios, tolerancias y presupuesto aceptados por equipo | Sin aprobación no se implementa investigación | **Pendiente** |
| G2. Competidor decisivo | [Texto y suplemento Reynolds inspeccionados](04_COMPETITOR_VERIFICATION.md) frente a misma decisión P5-R | No se identificó misma evaluación conjunta en esa fuente; otra coincidencia de aporte → reevaluar innovación | **Comprobación dirigida completada**; no todos los suplementos ni búsqueda exhaustiva |
| G3. Elegibilidad | Covariables, soporte local, rango/condición/concentración, política de lotes y edades congeladas | Sin rango: no estimar; sin soporte: limitar rama empírica | **Parcial:** conteos descriptivos; diagnóstico completo pendiente |
| G4. Control algebraico | Identidad OLS y tolerancia fijada; salida ejecutada | Diferencia inesperada: reparar antes de benchmark | **Diseñado, no ejecutado** |
| G5. Núcleo de software | Versión/commit, fórmulas/columnas protegidas, recuperación y fallos | Capacidad no funcional: reparar, reducir o parar con cambio explícito | **Solo documentación comprobada** |
| G6. Recursos | Hardware, tiempo/RAM y proyección R×B×celdas | Coste inviable: reducir alcance acordado, preservar EB de 68 regiones | **No medido** |
| G7. Precisión MC | R/B, intervalos de tasas, sensibilidad de cuantiles y denominadores | Evaluación imprecisa: ampliar dentro de presupuesto o declarar inconclusa | **Plan propuesto** |
| G8. Calibración/utilidad | Rendimiento bajo adversarios y evaluación reservada de la regla | Aporte útil/preciso o parada editorial; no exige que gane H1 | **Sin resultados** |
| G9. Empírico | Misma población/modelo, soporte y QA documentados; Θ o C̄ elegible | Si falla: reducir a auditoría; sin descubrimiento anatómico forzado | **Datos disponibles, elegibilidad/QC cortical no validados** |

## Qué mejoró en cada criterio y qué puede hacerlo fallar

**Factibilidad:** el benchmark usa archivos pequeños ya disponibles y una complejidad de media limitada, con 16 celdas principales y un piloto de coste. Retira dependencias de ABIDE II/reprocesamiento. Sigue condicionado a matrices estimables, software funcional y coste anidado medido; la factibilidad alta no se traslada a una afirmación biológica confirmatoria.

**Publicabilidad:** la pregunta ahora admite que una etapa sea preferible, que armonizar no ayude o que el diagnóstico permita abstenerse. Las salidas tienen una decisión analítica concreta y métricas con precisión MC. Fallará como candidato de artículo si solo hay equivalencias ya conocidas, comparaciones imprecisas o una recomendación incapaz de sobrevivir escenarios reservados. Ningún resultado promete aceptación.

**Innovación:** se reduce el reclamo a evaluación/aplicabilidad de un estimando condicionado. Las configuraciones de interacción, EB y bootstrap no son novedades propias. La posible aportación exige un vínculo diagnóstico→calibración no cubierto por competidores y útil fuera del generador de desarrollo. La búsqueda dirigida no es una prueba exhaustiva de ausencia.

## Incertidumbres decisivas y próximos acuerdos

1. **¿Existe aporte adicional frente a Reynolds y otros vecinos?** La inspección acotada de Reynolds ya se completó, sin identificar la misma unidad de evaluación; no resuelve toda la novedad. Mantener tabla de decisión y vigilancia de antecedentes. Si la unidad de contribución ya está cubierta, reevaluar y detener este diseño editorial.
2. **¿Es identificable el objetivo empírico sin extrapolación excesiva?** Decidir umbrales por covariables, congelar edades/modelos y diagnosticar; si no, Θ queda solo en simulación y C̄ debe evaluarse por separado.
3. **¿El coste y la precisión permiten una conclusión útil?** Solo un piloto autorizado mide recursos/estabilidad; no se inventó runtime, potencia ni cobertura.
4. **¿La regla sirve fuera de sus condiciones de desarrollo?** Evaluación reservada obligatoria para recomendar umbrales; de lo contrario entregar diagnóstico continuo y límites.

**Estado de handoff:** revisión y protocolo listos para discusión humana; análisis de investigación pendiente de aprobación. No se instalaron paquetes ni se ajustaron modelos o simulaciones en esta etapa. La siguiente fase no debe confundir aprobación de este documento con validación de sus controles.
