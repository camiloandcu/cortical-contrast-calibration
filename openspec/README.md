# Propuestas de work items

Esta configuración usa el esquema OpenSpec `spec-driven` para
**Codex y Antigravity**. Las habilidades y workflows se incluyen en Git.
No hace falta la configuración personal de quien preparó el repositorio.

## Preparar un clon

Seguir el [paso 0 del README](../README.md) solo si falta OpenSpec. Usar el
CLI global existente cuando ya está instalado; no hay dependencias npm locales.
La referencia verificada es OpenSpec 1.6.0. Las auditorías Python mantienen
sus requisitos independientes.

```bash
openspec --version
openspec list --json
```

En PowerShell se puede usar `openspec.cmd`. Abrir la raíz como workspace y
reiniciar el agente/editor para detectar habilidades y el PATH actualizado.
Antigravity >=1.20.5 usa `.agents/`; versiones anteriores requieren actualizarse.
No ejecutar `init` al clonar: las integraciones ya están versionadas.

## Iniciar y revisar

En cualquiera de los dos agentes se puede pedir:

> Inicia el work item SD1. Lee AGENTS.md y prepara la propuesta OpenSpec para
> revisión humana. Detente antes de implementar.

También se puede invocar explícitamente:

- Codex: `$openspec-propose` seguido del ID y objetivo del work item.
- Antigravity: `/opsx-propose` seguido del ID y objetivo del work item.

El agente consulta el [plan científico](../docs/06_SCIENTIFIC_DEVELOPMENT_PLAN.md)
y los [acuerdos](../docs/05_TEAM_DECISIONS.md). Si el ID no existe o su alcance
es ambiguo, solicita la aclaración material. Si el item agrupa varios resultados,
propone uno delimitado e identifica la cobertura restante para revisión.
Una petición de inicio genera una sola propuesta; no ejecuta tareas científicas.

La carpeta `openspec/changes/<nombre>/` contendrá:

- `proposal.md`: ID, alcance, exclusiones, dependencias, criterios numerados y evidencia prevista.
- `design.md`: decisiones, contratos afectados, alternativas, riesgos y pendientes.
- `specs/<capacidad>/spec.md`: requisitos y escenarios de comportamiento propuestos.
- `tasks.md`: pasos trazados a los criterios y verificaciones previstas.

El agente valida antes de presentar los documentos:

```bash
openspec validate <nombre> --strict
openspec status --change <nombre>
```

Las personas revisan los archivos mediante diff/PR y solicitan cambios o aprueban
explícitamente el alcance presentado. El agente conserva evidencia de quién
aprobó, qué revisión y cuándo, sin inventarla. Los acuerdos científicos se
registran en el documento de decisiones; las tres personas deben aprobar G1
y el plan de ejecución antes de implementar investigación. Un estado técnico
`apply-ready` solo indica que existen artefactos, no una autorización humana.
OpenSpec no impone por sí solo una barrera técnica que sustituya esta revisión.

Tras la aprobación, una petición explícita puede iniciar implementación con
`$openspec-apply-change` en Codex o `/opsx-apply` en Antigravity. La aceptación
humana, sincronización de specs, archivo y merge conservan sus gates separados;
no ejecutar sync/archive automáticamente al terminar tareas.

`docs/` conserva protocolo, decisiones y planificación científica. Las specs
principales de OpenSpec solo reflejarán comportamiento adoptado tras revisión;
las propuestas no reemplazan el protocolo ni convierten borradores en acuerdos.
No se crea una propuesta científica de ejemplo ni se aprueba SD1 con este setup.

## Mantenimiento

Las habilidades y workflows se generaron con OpenSpec 1.14.3; su flujo de
artefactos se comprueba con la instalación global existente 1.6.0.
Las carpetas `.agents/skills/`, `.agents/workflows/` y la regla de Antigravity
`.agents/rules/project.md` están versionadas; no contienen configuración personal.
No se necesita `node_modules/`, `package.json` o un lockfile npm.

La regeneración de integraciones es mantenimiento explícito, no un paso de
cada clon. Puede cambiar rutas y migrar o limpiar prompts globales heredados;
revisar siempre el diff y conservar las reglas de aprobación de este proyecto.
Fuente: [OpenSpec](https://github.com/Fission-AI/OpenSpec).
