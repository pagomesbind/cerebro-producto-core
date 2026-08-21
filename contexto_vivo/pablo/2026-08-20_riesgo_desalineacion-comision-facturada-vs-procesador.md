---
id: 2026-08-20_riesgo_desalineacion-comision-facturada-vs-procesador
pm: pablo
fecha_captura: 2026-08-20
fuente: "Pablo Gomes, directo en chat (sesión /idea_start sobre convenios_configuracion), 2026-08-20"
producto: adquirencia
tema: Riesgo financiero por desalineación entre la comisión facturada a la entidad y la comisión real cobrada por el procesador
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 5f0974a
---

**Patrón de riesgo (no exclusivo de convenios):** si una configuración de comisión queda mal cargada en el sistema interno de Bind PSP y Soporte no lo detecta a tiempo, Bind PSP puede seguir facturando a una entidad/comercio con un arancel más bajo del real (ej. "arancel reducido") mientras el procesador (Coelsa u otro) le está cobrando a Bind PSP el arancel completo por cada transacción — la diferencia es **pérdida neta directa**, no solo un problema de UX/proceso.

**Evidencia cuantificada:** el PM citó un precedente real, de causa distinta a la discutida en el proyecto `1_proyectos/convenios_configuracion/` (no fue por herencia de convenios, pero sigue el mismo patrón de desalineación facturación↔costo real cobrado por el procesador): **pérdida de $15.000.000 ARS en un solo mes**. No se registró fecha exacta ni el detalle técnico de esa causa distinta — solo se aportó como referencia de magnitud.

**Por qué es relevante más allá de este proyecto:** cualquier mecanismo de configuración de comisiones (convenios, arancel reducido/Coelsa, futuros orquestadores) debería incluir una forma de detectar automáticamente esta divergencia, no depender de que Soporte la note manualmente. Ver el riesgo específico y su mitigación esperada para el proyecto de convenios en `1_proyectos/convenios_configuracion/riesgos.md`.

**Estado:** capturado, sin ticket ni dueño de mitigación general asignado todavía.
