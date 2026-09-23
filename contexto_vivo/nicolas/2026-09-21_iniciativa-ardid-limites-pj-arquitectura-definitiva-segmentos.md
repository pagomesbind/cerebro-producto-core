---
id: 2026-09-21_iniciativa-ardid-limites-pj-arquitectura-definitiva-segmentos
pm: nicolas
fecha_captura: 2026-09-21
fuente: "Reunión 'Ardid - Persona Jurídica' (2026-09-21)"
producto: ardid
tema: Arquitectura definitiva de segmentación PJ en Wallet (3 tipos de banca × 2 segmentos) cerrada, en implementación
tipo: iniciativa
proyecto: ardid_limites_pj
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

Novedad del proyecto "Segmentación de personas jurídicas en Ardid" ([ardid_limites_pj](../ardid_limites_pj/proyecto.md), sin Jira todavía): en la reunión "Ardid - Persona Jurídica" (2026-09-21), Nicolás Colón cerró con Rocio Revelli (Ardid) y Pablo Gomes la arquitectura definitiva de configuración: por cada organización, 3 tipos de banca (física mayor, física menor, jurídica) × 2 segmentos (estándar, restringido) = 6 combinaciones en Wallet. Las cuentas jurídicas nacen siempre en el segmento restringido (tope $1.000) hasta presentar documentación a PLD.

Esto amplía el diseño técnico ya cerrado el 2026-09-17 (que hablaba de un solo segmento PJ) a las 3 categorías con 2 segmentos cada una. El PM ya empezó a implementar la estructura en Wallet, en paralelo a la aprobación de Emma Vignoles todavía pendiente — es decir, el desarrollo avanza antes del `/idea_prd` formal. Queda sin definir el proceso operativo de cambio de segmento (restringido→estándar) tras la aprobación de documentación.

> Fuente: Reunión "Ardid - Persona Jurídica" (2026-09-21), minuta Gemini.
