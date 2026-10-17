# Comprobación del antecedente decisivo

Fecha: 2026-10-11. Comprobación adicional del agente principal, posterior al dictamen independiente. Resuelve el obstáculo de acceso a Reynolds; no equivale a una búsqueda sistemática ni aumenta las puntuaciones del comité.

## Fuente y acceso

[Reynolds et al., 2023, artículo original](https://doi.org/10.1016/j.nicl.2023.103472), PMID 37506457, PMCID PMC10412957. La apertura web de PMC falló, pero se recuperaron el XML primario y el archivo de suplementos/figuras mediante la API de Europe PMC:

- [Texto completo XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10412957/fullTextXML).
- [Archivo de suplementos](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10412957/supplementaryFiles); se inspeccionó `mmc1.docx`, incluidas sus seis secciones.

Copias originales locales en `data/sources/`, con tamaños y SHA-256 en [el manifiesto](../../data/download_manifest.csv). El artículo declara CC BY-NC-ND; las copias originales no se modificaron. El archivo de suplementos contiene también figuras del artículo y ocupa aproximadamente 44,98 MB.

## Qué se comprobó y qué implica

**Fuente primaria comprobada:** §3.11 usa datos semisintéticos ADNI, diagnóstico asignado aleatoriamente, efectos de diagnóstico y diagnóstico×edad añadidos, sexo como efecto principal y 500 repeticiones. Evalúa coeficientes, sensibilidad y error tipo I. El suplemento amplía priors, muestreo, predicción del escáner, incertidumbre regional, coeficientes simulados y sensibilidad a priors.

**Inferencia de revisión:** esto impide reivindicar simulación, recuperación de interacciones o incertidumbre como aportaciones nuevas por sí solas. En el texto y suplemento inspeccionados no se identificó la misma evaluación conjunta de elegibilidad de cuatro grupos, contraste condicionado `Θ`, equivalencia puntual y cobertura frente a una etapa. Es una diferencia candidata delimitada, no evidencia de que esa unidad de contribución sea inédita en toda la literatura.

| Componente de la propuesta revisada | Estado tras inspección |
|---|---|
| Simulación de interacción y evaluación de error | Antecedente cercano confirmado; no reclamar novedad |
| Incertidumbre después de armonizar | Antecedente confirmado; un bootstrap tampoco es innovación automática |
| Elegibilidad del contraste y soporte de cuatro grupos | Diferencia candidata respecto de esta fuente; evaluar utilidad y antecedentes restantes |
| Regla que permita elegir o detener una estrategia | Resultado aún desconocido; validar fuera de las condiciones usadas para desarrollarla |

## Actualización de G2

La lectura dirigida de Reynolds y su suplemento está **completada**. El dictamen registraba esa lectura como pendiente porque el acceso directo había fallado. Su condición de veto se mantiene: si otra fuente ya cubre la misma decisión, reevaluar innovación; si el piloto reproduce únicamente consecuencias conocidas, detener la aspiración de artículo. No se inspeccionaron por este procedimiento todos los suplementos de los demás competidores.

No se ejecutó el código del artículo ni se reprodujeron resultados. La implementación y la validez del protocolo de esta propuesta siguen pendientes de aprobación y evaluación. [Dictamen original](02_PEER_REVIEW.md) y [respuesta a revisión](03_REVISION_RESPONSE.md).
