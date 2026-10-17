# Plan operativo científico — propuesta para revisión conjunta

Estado: **borrador; no autoriza ejecución científica**. Complementa el
[protocolo](03_REFINED_PROPOSAL.md), sin reemplazar sus fórmulas, escenarios
o reglas. Los [acuerdos y pendientes](05_TEAM_DECISIONS.md) distinguen decisiones
comunicadas por Camilo de aprobación conjunta. Las tres personas revisan todo.

Objetivo operativo: en tres meses producir una evaluación reproducible de
elegibilidad y calibración del contraste Θ o una conclusión de inviabilidad
bien documentada. Un manuscrito y una recomendación dependen de precisión y
utilidad demostradas; no son entregables garantizados.

## Pregunta, datos y resultado interpretable

| Pregunta | Entradas verificadas | Trabajo previsto | Decisión apoyada |
|---|---|---|---|
| ¿El diseño sostiene el contraste? | Edad, sexo/diagnóstico codificados, sitio e identificadores ABIDE I | W=[X,Z], rango, condición, celdas y concentración; regla previa a efectos | Estimar Θ, evaluar C̄ o abstenerse de interpretación empírica |
| ¿Se preserva el punto y se calibra incertidumbre? | Covariables fijas; 68 medidas para calibrar escala/dependencia; verdad generada | E1/H0/H1, control OLS, escenarios y bootstrap completos | Elegir procedimiento para ese objetivo/diseño, sin atribuir biología verdadera a ABIDE |
| ¿Es útil fuera del desarrollo? | Escenarios y semillas reservados, definidos previamente | Sesgo, cobertura, anchura, fallos y error MC | Recomendar condicionalmente o entregar solo diagnósticos/límites |

Mantener unidad persona y dependencia regional, valores ausentes y procedencia.
La referencia de 1.027 filas completas no es una muestra empírica confirmatoria.
El filtro anatómico de 773 es sensibilidad; no certifica superficies. No añadir
FIQ, ADOS, medicación, ABIDE II ni imágenes originales sin revisar selección,
estimando y alcance. Edad transversal no es desarrollo longitudinal.

## Secuencia y aceptación

Semanas relativas al inicio acordado, dentro del plazo de tres meses. Si el
proyecto ya tiene fecha límite externa, prevalece y se ajusta el alcance.

| Semanas | Tarea y dependencia | Entregable para revisión de los tres | Aceptación / parada |
|---|---|---|---|
| 1–2 | SD1: reconstrucción y auditoría de covariables; autorización descriptiva existente | Procedencia verificada; configuraciones de soporte; matriz y exclusiones propuestas | Elegir regla sin efectos; registrar no estimabilidad cuando corresponda |
| 2 | SD2: cerrar G1 con SD1 y protocolo | Configuración de contraste, pesos, edades, regiones, 16 celdas, parámetros reservados y tolerancias; autorización del piloto | Tres revisiones y acuerdo explícito; sin acuerdo no comenzar SD3 |
| 3–4 | SD3: implementación mínima y controles, después de G1 | Entorno fijado, identidad OLS, matrices protegidas H0/H1, generador con verdad calculable y fallos explícitos | Recuperación numérica y reproducibilidad; reparar antes del piloto |
| 5 | SD4: piloto técnico; controles aprobados | R=30 por las cuatro primeras celdas de A, pocas réplicas internas; tiempo/RAM, estabilidad y coste proyectado | No usar cobertura del piloto para validar método ni prometer potencia |
| 6 | SD5: decisión de coste/precisión y congelación final | Plan R/B costeado, tareas independientes, semillas y configuración versionadas | Autorizar evaluación; reducir solo con acuerdo y manteniendo EB de 68 regiones, o parar |
| 7–9 | SD6: evaluación autorizada | Lotes reanudables, métricas pareadas, incertidumbre MC y denominadores de fallos | Reservados sin usarse para retocar reglas; si R/B no alcanza, declarar imprecisión |
| 10 | SD7: sensibilidad empírica si elegible | Misma población/X/edades/pesos entre métodos; sensibilidad de selección e influencia | Θ/C̄ solo si defendibles; de lo contrario solo auditoría |
| 11–12 | SD8: síntesis y reproducción | Tablas/figuras, límites, reproducción por otro integrante y borrador metodológico si procede | Revisión conjunta; utilidad demostrada o conclusión negativa/inconclusa explícita |

Cada tarea tendrá un ejecutor temporal para evitar ediciones simultáneas,
sin dividir la autoridad científica por disciplina. Una PR registra objetivo,
archivos, comprobaciones, incertidumbres y revisión conjunta. La persona que
no ejecutó reproduce al menos un lote antes de aceptar resultados finales.

## Cómputo en Colab gratuito

**Hecho verificado el 2026-10-17:** Colab no garantiza recursos ni publica una
cuota fija; las sesiones pueden interrumpirse y sus máquinas son temporales.
Fuente: [FAQ oficial](https://research.google.com/colaboratory/faq.html).
Tres integrantes no equivalen a un presupuesto garantizado de horas por día.

**Diseño propuesto:** CPU primero; no asumir aceleración GPU para GLS/ComBat.
Cada integrante trabaja interactivamente en su propia sesión con unidades
independientes previamente asignadas. No convertir las sesiones en workers
distribuidos ni usar cuentas adicionales para eludir límites del servicio.

Antes de evaluación, implementar tareas identificadas por
`scenario_id / replicate_id / config_hash / seed`. Una réplica genera las
68 regiones y alimenta los tres métodos, preservando comparación pareada.
Semillas derivadas de identificadores estables; no de la persona, hora o sesión.
No dividir EB por regiones para abaratarlo.

Guardar por lote resultados y checkpoints atómicos, commit, configuración,
versiones, verdad, semillas, estado/fallos, tiempo, RAM y denominadores. La
reanudación debe saltar solo tareas completas con configuración idéntica;
agregar sin duplicados y rechazar mezclas de versiones. Estas capacidades
están **por implementar**, no disponibles en los scripts descriptivos actuales.

La ubicación persistente la decide el equipo antes de correr; autorizar por
separado cualquier conexión de cuenta (por ejemplo Drive). No guardar tokens
en notebooks ni comprometer checkpoints individuales en Git. Los notebooks
que se publiquen deben revisarse con salidas limpias.

El piloto medirá segundos por estudio/bootstrap, RAM y coste de recuperación.
Proyectar `16 × R × coste por réplica completa`, incluyendo sensibilidad de B,
fallos, transferencia y margen de interrupciones declarado. Compararlo con
horas realmente disponibles medidas por los integrantes. R=1.000–2.000 y
B=499/999 siguen siendo propuestas sujetas a precisión; no promesas de ejecución.

Si no cabe: priorizar una evaluación menor previamente acordada y precisa,
posponer sensibilidades opcionales o declarar que no se puede responder.
No rebajar R/B silenciosamente, borrar fallos ni usar escenarios reservados
para elegir una regla. La adquisición de cómputo queda fuera del presupuesto.

## Trabajo antes de la aprobación

Permitido ahora: compartir el repositorio, reconstruir/verificar fuentes,
revisar documentos y auditar descriptivamente covariables. Pendiente de G1:
instalar implementaciones de investigación, ajustar modelos, calibrar el
generador con ajustes o ejecutar simulaciones. Este turno solo prepara y
planifica; no inicia SD1 ni SD3–SD8.
