---
id: 2026-09-22_iniciativa-ardid-limites-pj-solucion-v2-aprobada
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Análisis técnico-funcional /idea_solution (2026-09-22, v2.0-v2.2)"
producto: ardid
tema: Segmentación de personas jurídicas en Ardid — análisis técnico-funcional reescrito y aprobado (arquitectura de 6 segmentos + Calculador de Costos)
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
proyecto: ardid_limites_pj
---

El proyecto `ardid_limites_pj` reescribió por completo su análisis técnico-funcional (de v1.3 a v2.2) para reflejar la arquitectura definitiva cerrada en la reunión "Ardid - Persona Jurídica" (2026-09-21, con Rocío Revelli y Pablo Gomes) — y este proyecto pasó a absorber también la directiva del directorio sobre límites de PJ (antes tratada como frente separado de Pablo Gomes, T-041/T-042).

**Arquitectura confirmada:** por cada Organización, 3 tipos de banca (Standard, Menor, Persona Jurídica) × 2 segmentos (normal, restrictivo) = 6 `ClientBankType` en Ardid, replicados como 6 segmentos en el Calculador de Costos (contrato confirmado: `{tipo, codigo, descripcion, ardidClientBankTypeId, entidadIdExterno}`). Persona Jurídica nace en el segmento restrictivo (tope $1.000, cumple la directiva del directorio); Standard y Menor nacen en normal.

**Corrección de diseño relevante:** inicialmente se había asumido que el cambio manual de restrictivo→normal era un toggle a nivel de la Organización completa. El PM corrigió: es una **modificación puntual sobre una Cuenta individual**, ejecutada por Rocío Revelli vía `PATCH /api/v1/Cuenta/{id}/ActualizarSegmento` (WalletCuenta) — dos mecanismos distintos que no hay que confundir con la Especificación (que solo fija el default de cuentas nuevas).

**Estado:** documento aprobado por el PM (`status: approved`) pese a quedar 3 gaps sin cerrar: G1/G2 (valores de catálogo Ardid y punto de integración exacto, trabajo de Ingeniería/Fintexa) y G8 (proceso operativo del cambio manual — responsable formal, registro, plazos — sigue sin definir, riesgo real con el deadline del 1° de octubre, ver T-065). El PM ya está implementando la estructura en Wallet en paralelo a la aprobación de Emma Vignoles, todavía pendiente. Próximo paso: `/idea_prd`.

> Fuente: `wiki/1_proyectos/ardid_limites_pj/artefactos/ardid_limites_pj-solution.md` (v2.2), `decisiones.md`, `gaps.md`.
