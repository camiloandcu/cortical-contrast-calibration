# Acuerdos del equipo y decisiones pendientes

Registro: 2026-10-17. Las decisiones comunicadas por Camilo se distinguen de
la aprobación conjunta del protocolo por las tres personas. Consumidores:
investigadores y sus agentes; permite saber qué ejecutar y dónde detenerse.

Nombre de trabajo: **Calibración de contrastes corticales**. Se usa este nombre
o «esta propuesta» en los documentos, evitando las etiquetas internas anteriores.
Nombre previsto para GitHub: `cortical-contrast-calibration`; publicación todavía
pendiente de confirmación explícita. La carpeta local conserva su ruta actual.

## Acuerdos comunicados por Camilo

| Tema | Acuerdo | Consecuencia observable |
|---|---|---|
| Repositorio | Público; operar GitHub mediante `gh` | Acceso de lectura sin cuenta; escritura requiere colaboradores o fork/PR |
| Datos | Código, documentos, manifiesto y agregados; reconstrucción local de datos individuales | Un clon limpio no contiene fenotipos, medidas individuales ni copias de artículos |
| Objetivo | Mantener Θ y estandarización de la propuesta revisada en simulación | No simplificar la pregunta según significancia |
| Alcance | ABIDE I; sin ABIDE II ni reprocesamiento en el núcleo | No añadir dependencias de datos externos |
| Elegibilidad | Auditar configuraciones propuestas mediante covariables antes de fijar regla | No elegir umbrales mirando grosores, efectos o rendimiento simulado |
| Comparadores | Mantener E1 GLS, H0/H1 ComBat e incertidumbre de todo el procedimiento | Misma población, modelo final y 68 regiones EB |
| Regiones y tolerancias | Conservar las tres regiones y criterios propuestos como base de aprobación estadística conjunta | No sustituir la revisión estadística por este registro |
| Empírico | Sensibilidad secundaria condicionada a soporte; sin afirmaciones anatómicas confirmatorias | Θ, C̄ o solo auditoría según elegibilidad |
| Organización | Las tres personas revisan todo conjuntamente | No hay responsables exclusivos por disciplina; asignar solo ejecutor temporal por tarea |
| Plazo y recursos | Tres meses; Colab gratuito disponible para cada integrante, sin presupuesto de compra autorizado | Medir capacidad efectiva; no asumir cuotas diarias garantizadas |
| Autorización actual | Preparar/publicar el paquete y planificar; auditoría descriptiva ya autorizada | No instalar ni ejecutar modelos/simulaciones de investigación todavía |

## Asuntos por resolver conjuntamente

| Decisión | Propuesta y beneficio | Criterio para cerrarla |
|---|---|---|
| G1: autorización científica | Aprobar primero plan y configuración; evita expandir alcance durante ejecución | Tres revisiones y acuerdo explícito con fecha/commit, incluyendo autorización del piloto |
| Regla de elegibilidad | Comparar grilla de §4 sin resultados; elegir después una principal | Tabla de soporte, población, edades, pesos y límites congelados |
| Software y versiones | Prueba acotada de una implementación inspeccionable para ambos ComBat | Matrices protegidas verificadas, versión/commit y entorno registrados |
| Generación y evaluación reservada | Congelar las 16 celdas, parámetros adversarios y separación desarrollo/evaluación | Configuración revisada antes de generar resultados |
| Inferencia y precisión | Revisar tres regiones, cobertura 93–97 %, sesgo/σ 0,05, B/R y criterio de fallos | Aprobación estadística conjunta; B/R finales sujetos a estabilidad y coste |
| Presupuesto efectivo | Medir sesiones útiles y coste por lote antes de comprometer evaluación completa | Proyección de coste con margen y decisión de continuar/reducir/parar |
| Calendario | Usar 12 semanas operativas dentro de tres meses | Fijar fecha inicial/final al aprobar ejecución; no reiniciar plazo por interrupciones |
| Licencia del trabajo propio | Decidir código/documentos entre autores; una licencia permite reutilización explícita | Acuerdo de titulares; no aplicar esa licencia a datos o fuentes de terceros |
| Acceso de escritura | Invitar a los otros dos investigadores cuando indiquen sus usuarios GitHub | Usuarios confirmados y permisos acordados; mientras tanto pueden leer/clonar/forkear |

## Registro de revisión conjunta

No inventar nombres, votos ni aprobaciones. Cada integrante agrega su revisión
en la PR correspondiente; el acuerdo se resume aquí con fecha y commit.

| Integrante | Revisión del plan científico | Aprobación del piloto |
|---|---|---|
| Camilo | Acuerdos anteriores; plan operativo pendiente de revisión | Pendiente |
| Investigador/a 2 | Pendiente | Pendiente |
| Investigador/a 3 | Pendiente | Pendiente |

## Preparación del repositorio

Plan de preparación aprobado por Camilo el 2026-10-17. Implementado en la rama
`setup/public-repository`: exclusiones, instrucciones portables, guía de
colaboración y plan científico propuesto. Los scripts de presentación ya no
estaban presentes al iniciar esta implementación; se eliminaron sus referencias
documentales restantes. No hay resultados de investigación nuevos.

Verificación local: perfil y conteos descriptivos regenerados sin cambios en
los agregados; 2.077 fuentes con tamaños/hashes coincidentes; 86 enlaces locales
válidos; 30 archivos públicos revisados, sin datos individuales, copias de
fuentes ni credenciales detectadas por las comprobaciones. La comprobación
automática de patrones no sustituye revisión del contenido publicado.

Commit inicial local: `453596c` en `setup/public-repository`. Clon limpio
verificado sin datos locales ni dependencias externas; controles negativos
rechazan enlace roto y derivado excluido añadido al índice.

Publicación **pendiente de confirmación explícita**: el guard personal
`publishing` bloqueó antes de ejecutar `gh repo create ... --public ... --push`.
No se creó el remoto ni se subió contenido. Acción preparada: crear
`camiloandcu/cortical-contrast-calibration` público y subir únicamente `setup/public-repository`.
Reversión posible: hacerlo privado o eliminarlo, sin retirar copias ajenas.
No reintentar bajo otra forma; esperar confirmación. `main` no se crea ni
actualiza sin autorización explícita.
