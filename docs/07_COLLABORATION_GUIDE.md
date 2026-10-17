# Colaboración entre investigadores y agentes

## Primera sesión

Instalar Git y Python 3.10 o posterior. Clonar el repositorio público con su URL
de GitHub y entrar en la carpeta. No hace falta cuenta para lectura; una cuenta
con permiso de escritura o un fork permite proponer cambios.

Desde la raíz ejecutar:

```bash
python3 scripts/verify_repository.py
```

Leer [AGENTS.md](../AGENTS.md), [acuerdos](05_TEAM_DECISIONS.md) y el
[plan científico](06_SCIENTIFIC_DEVELOPMENT_PLAN.md). Cada agente debe identificar
la tarea, su autorización y su criterio de aceptación antes de editar. No se
requieren archivos personales ni habilidades de la máquina de Camilo.

## Flujo por tarea

1. Revisar juntos el objetivo y asignar un ejecutor temporal; no editar los
   mismos archivos desde varias sesiones.
2. Crear una rama corta, por ejemplo `docs/support-review` o `feat/design-audit`.
3. Mantener cambios pequeños. Usar commits como `docs: clarify support policy`.
4. Verificar el repositorio; si se cambiaron datos o scripts descriptivos,
   reconstruir y verificar la auditoría local. Revisar `git diff` y
   `git diff --cached --name-only` antes de publicar.
5. Abrir una PR con problema, cambio, comprobaciones y decisiones pendientes.
   Los tres revisan las decisiones científicas; registrar el acuerdo sin
   inventar votos. La ejecución requiere además las puertas del protocolo.
6. Actualizar el estado de la tarea/decisión con commit, PR, verificación y
   trabajo restante antes de cambiar de sesión.

La creación, publicación o actualización de ramas protegidas requiere la
autorización explícita del usuario. La rama de preparación inicial puede ser
la rama predeterminada hasta que se acuerde crear `main` y sus reglas.

## Datos y Colab

Seguir la [guía de descarga](02_DOWNLOAD_GUIDE.md) para generar archivos locales.
Los enlaces a tablas excluidas se presentan como rutas de código, no enlaces
rotos. Los agregados existentes son referencia descriptiva, no umbrales validados.

Para usar Colab, cada persona abre su notebook en su cuenta y reconstruye el
entorno. Una sesión o carpeta de Drive no se comparte por clonar el repositorio.
No se ha creado un notebook ejecutor de investigación: será parte del desarrollo
aprobado. La estrategia de lotes y persistencia propuesta está en el plan.

Antes de añadir notebooks: limpiar salidas, comprobar credenciales/rutas y no
incluir tablas de participantes. Guardar resultados individuales/checkpoints
fuera de Git y revisar cualquier agregado antes de publicarlo.

## Revisión de aceptación de este paquete

- Clon limpio verificable sin datos ni dependencias científicas.
- Ningún archivo individual o fuente descargada versionado.
- Sin referencias a la presentación retirada ni enlaces locales rotos.
- Fuentes reconstruibles con manifiesto y comprobación de integridad local.
- Aprobaciones parciales, revisión conjunta y trabajo futuro diferenciados.

Licencia del trabajo propio, usuarios de los colaboradores, regla de
elegibilidad, software y autorización del piloto siguen en el registro de
decisiones. No bloquear la lectura pública por esas decisiones; tampoco
interpretar la lectura pública como permiso de ejecución científica.
