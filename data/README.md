# Datos y procedencia

Este repositorio publica el manifiesto histórico de adquisición, no los datos
individuales ni las copias de artículos. Los identificadores de archivos del
manifiesto permiten verificar procedencia; no contienen medidas clínicas.

Cada investigador reconstruye sus archivos siguiendo la
[guía de descarga](../docs/02_DOWNLOAD_GUIDE.md). Las condiciones de los
proveedores siguen aplicando. No compartir credenciales ni subir originales,
derivados por participante, inventarios con ejemplos individuales o logs.

Rutas locales generadas:

- `raw/abide1/`: fenotipos y estadísticas FreeSurfer.
- `sources/`: diccionarios, páginas y literatura descargada.
- `derived/`: tablas individuales, inventarios y verificación de la auditoría.
- `acquisition_logs/`: registro local de incidentes de descarga, si existe.

Los conteos agregados publicados están en `literature/abide_design_*.csv`.
Son descriptivos, incluyen celdas pequeñas y no representan microdatos
anonimizados ni una garantía de privacidad para futuras publicaciones.

`download_manifest.csv` conserva el registro de referencia de 2026-10-11.
El descargador lo actualiza localmente: revisar cualquier diferencia antes
de proponer un cambio. Un hash calculado localmente comprueba coincidencia
con esa copia; no autentica al proveedor. Páginas o archivos remotos pueden
cambiar: documentar las diferencias sin reemplazar silenciosamente la referencia.
