# P5: descargas realizadas y pendientes

Auditoría local comprobada: 2026-10-11. **El repositorio público no incluye datos
individuales ni copias de fuentes**. Las cifras siguientes describen la copia
auditada; cada investigador debe reconstruirla para inspeccionar esos archivos.
Consultar la [política de datos](../data/README.md).

## Disponible localmente

- CSV fenotípico: 1.112 filas y 106 columnas.
- 2.070 archivos regionales FreeSurfer 5.1/aparc, 1.035 participantes bilaterales.
- Diccionarios ABIDE I y II, páginas PCP de descarga y calidad.
- Tabla de grosor, inventarios y auditorías en `data/derived/`.
- Texto completo y suplemento del antecedente Reynolds 2023, recuperados mediante Europe PMC y revisados en [la comprobación dirigida](review/04_COMPETITOR_VERIFICATION.md).

Procedencia y hashes: [manifiesto](../data/download_manifest.csv). Los 77 `no_filename` no tienen identificador procesado; los intentos transitorios resueltos están en `data/acquisition_logs/`.

## Reproducir la descarga pública

Desde la raíz, con Python 3 y biblioteca estándar:

```bash
python3 scripts/download_datasets.py --mode metadata
python3 scripts/download_datasets.py --mode abide-freesurfer --workers 8
python3 scripts/download_datasets.py --mode p5-evidence
python3 scripts/profile_datasets.py
python3 literature/audit_design_coverage.py
python3 scripts/verify_audit.py
```

Ejecutar cada modo de descarga por separado: actualizan el mismo manifiesto. Se conservan archivos existentes y se calcula SHA-256. `--limit 10` permite un piloto, no reproduce la cobertura completa. `abide-ants` es una opción del descargador, no una fuente utilizada o validación equivalente a FreeSurfer.

Las copias de literatura son opcionales para reproducir el dataset, pero ya están locales y forman parte del manifiesto. Reproducirlas con `python3 scripts/download_datasets.py --mode p5-evidence` antes de la verificación final. El suplemento incluye figuras y ocupa 44,98 MB; datasets y literatura suman aproximadamente 58,62 MB de fuentes.

Fuentes: [PCP descarga](https://preprocessed-connectomes-project.github.io/abide/download.html), [PCP calidad](https://preprocessed-connectomes-project.github.io/abide/quality_assessment.html), [ABIDE I](https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html). Revisar acuerdos antes de redistribuir; ABIDE I declara uso investigador no comercial y CC BY-NC-SA.

## Recursos pendientes

| Recurso | Estado | Necesidad |
|---|---|---|
| T1 originales ABIDE I | No locales; acceso NITRC | No para simulaciones con las medidas publicadas; sí para reprocesamiento nuevo. |
| Superficies/archivos completos FreeSurfer | Solo tenemos estadísticas aparc | Definir protocolo y coste; no pueden inspeccionarse superficies desde una tabla. |
| CSV ABIDE II | Enlace compuesto solicita autenticación | Opcional para verificar una extensión. |
| Grosor ABIDE II compatible | No verificado ni descargado | No es requisito ni validación externa comprometida. |

## ABIDE II: pasos manuales si el equipo decide extender P5

1. Abrir [ABIDE II](https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html), seguir los enlaces NITRC y crear cuenta o iniciar sesión personalmente. No compartir contraseñas.
2. Revisar y aceptar los acuerdos pertinentes. El [CSV compuesto](https://www.nitrc.org/frs/downloadlink.php/9108) solicitó autenticación; comprobar que el archivo descargado sea CSV, no una página de login.
3. Guardarlo en `data/raw/abide2/`, conservando original y registrando URL, nombre, fecha, licencia y SHA-256.
4. Antes de obtener imágenes, contar diagnóstico × sexo × sitio, edades y faltantes. Identificar sesiones repetidas; no contarlas como sujetos independientes.
5. Verificar atlas, versión de FreeSurfer, QC y disponibilidad de derivados. Si no existen medidas compatibles, estimar coste de reprocesamiento antes de llamarlo réplica.
6. Descargar T1 después de acordar esa extensión. Los totales del portal no garantizan imágenes útiles, grosor comparable ni independencia respecto de ABIDE I.

La propuesta base debe poder concluir con ABIDE I. Incorporar ABIDE II modifica presupuesto, QC y comparabilidad y requiere una decisión explícita del equipo.
