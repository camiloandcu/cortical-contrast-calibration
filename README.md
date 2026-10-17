# Neuroco 2026-2 — P5-R

Investigación metodológica sobre **cuándo puede estimarse una interacción
edad × sexo × diagnóstico y cuándo sus intervalos están calibrados después
de armonizar grosor cortical multicéntrico**. Usa simulaciones de verdad
conocida calibradas al diseño observado de ABIDE I y una sensibilidad empírica
limitada; no propone un biomarcador ni identifica biología verdadera.

**Estado:** datos auditados y protocolo documentado. Desarrollo científico,
modelos y simulaciones pendientes de aprobación conjunta. Plazo previsto:
tres meses; recursos disponibles: Colab gratuito de los tres integrantes,
sin horas garantizadas ni presupuesto de cómputo de pago.

## Empezar a colaborar

1. Leer el [índice de evidencia](docs/00_INDEX.md) y la
   [propuesta científica](docs/03_REFINED_P5_PROPOSAL.md).
2. Revisar [acuerdos y decisiones pendientes](docs/05_TEAM_DECISIONS.md) y el
   [plan operativo científico](docs/06_SCIENTIFIC_DEVELOPMENT_PLAN.md).
3. Seguir la [guía de colaboración](docs/07_COLLABORATION_GUIDE.md).
   Los agentes deben leer primero [AGENTS.md](AGENTS.md); no necesitan
   las habilidades privadas ni la configuración personal de otro integrante.

El repositorio es público para lectura y clonación. La escritura requiere
invitación como colaborador o un fork y pull request. Las tres personas revisan
las decisiones científicas en conjunto; cada tarea tiene un ejecutor temporal.

## Qué contiene

- `docs/`: protocolo, revisión científica, datos, decisiones y plan de trabajo.
- `literature/`: referencias primarias y conteos agregados de diseño.
- `scripts/`: descarga pública y auditoría descriptiva con biblioteca estándar.
- `data/download_manifest.csv`: procedencia, fecha, tamaño y SHA-256 de referencia.

Los fenotipos, medidas individuales, inventarios con ejemplos individuales,
logs y copias de artículos **se reconstruyen localmente y no se versionan**.
Consultar la [política de datos](data/README.md). Las cifras documentadas
proceden de la auditoría local de octubre de 2026; clonar no descarga datos.

## Verificar el repositorio sin descargar datos

Requiere Git y Python 3.10 o posterior; no hay dependencias externas para las
herramientas descriptivas. Desde la raíz:

```bash
python3 scripts/verify_repository.py
```

Comprueba archivos versionados, enlaces locales, sintaxis Python y separación
de datos locales. No valida integridad de fuentes ausentes ni resultados científicos.

## Reconstruir la auditoría de datos

Revisar primero los términos de los proveedores en la
[guía de descarga](docs/02_DOWNLOAD_GUIDE.md). Ejecutar un modo a la vez porque
comparten manifiesto. Para reproducir las 2.077 entradas históricas completas,
incluir también las copias de evidencia:

```bash
python3 scripts/download_datasets.py --mode metadata
python3 scripts/download_datasets.py --mode abide-freesurfer --workers 8
python3 scripts/download_datasets.py --mode p5-evidence
python3 scripts/profile_datasets.py
python3 literature/audit_design_coverage.py
python3 scripts/verify_audit.py
```

Se reutilizan archivos existentes. `p5-evidence` es opcional para explorar el
dataset, pero necesario para verificar el manifiesto completo de referencia.
Las fuentes originales ocupaban unos 58,62 MB; reservar espacio para derivados.
Los hashes locales no equivalen a firmas del proveedor y las fuentes remotas
pueden cambiar. Revisar errores y diferencias de manifiesto antes de continuar.

La auditoría de referencia encuentra 1.112 registros fenotípicos, 1.035 personas
con archivos bilaterales y 1.027 con 68 medidas completas positivas/finitas.
El filtro anatómico ilustrativo deja 773; no certifica superficies FreeSurfer.
Los conteos y el soporte son descriptivos, no resultados inferenciales.

## Reutilización y atribución

Las referencias y condiciones de terceros se conservan en el índice y la guía
de descarga. No se concede aquí una licencia sobre ABIDE ni artículos ajenos.
La licencia del código y los documentos propios está pendiente de acuerdo
entre autores; publicar el repositorio no sustituye ese acuerdo.
