---
id: 2026-09-08_adquirencia_analisis_cobro_provincia_net
pm: pablo
fecha_captura: 2026-09-08
fuente: Mail de Matías Alzogaray (malzogaray@bind.com.ar), threadId 1a07ce68d391b4da, 2026-09-07 17:29:14 — minuta "Análisis COBRO" de reunión del 7/09 12:00-13:00
producto: adquirencia
tema: Decisión arquitectura Provincia Net + prioridades de Adquirencia/Pagos FX/Contracargos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/
tipo_destino: crear (incidente_provincia_net_convivencia_sistemas.md)
contradice: "no"
confianza: Alta
estado: ingestado
merge_commit: 4b0d3d1e684ff33256a33a29f86746dfd5c7cc9a
---

## Análisis COBRO — Decisiones y Prioridades (7/09/2026)

Minuta técnica de reunión con Fintexa/BIND enfocada en validación de comisiones QR y resolución de incidente crítico en Provincia Net.

### Decisión Principal: Convivencia de Sistemas (Provincia Net)

**Contexto:** Existe un error reportado en ticket 1676/DAD-2943 (generación masiva de QR para Provincia Net sin respuesta desde hace semanas). Se justificaba usar el "proceso antiguo" porque el nuevo desarrollo no soporta los volúmenes masivos de velocidad requeridos.

**Decisión Tomada:** Mantener AMBOS sistemas conviviendo operativamente — el antiguo (funcionando, pero masivo) y el nuevo (desarrollado pero con limitaciones de throughput) coexisten en producción. Vincular ambos a PRD-66 si el estado actual refleja esto.

### Comisiones Webhook de QR

**Hallazgo:** Coelsa calcula automáticamente y de forma obligatoria el 21% de IVA sobre el importe de la comisión en todos los casos.

**Estado:** Desarrollo en curso (Daniela Collia, Fintexa). Valida que el webhook refleje el cálculo correcto (DAD-2801, incorporar arancel COELSA).

### Prioridades Confirmadas (Máxima)

1. **Tratamiento de Contracargos** — proyecto de alta prioridad, múltiples tickets iniciados (ej. ehd146, DAD-2209, DAD-2257)
2. **Pagos FX** — urgencia por deadline Mastercard, mayormente en QA tras demora técnica atribuida a Mastercard
3. **CU Collect / Botón Simple 2.0 (Favacard)** — ticket 1512/PRD-235, máxima prioridad en el colector (requerimiento cliente, nivel avanzado de desarrollo)

### Versión 73 — Cierre Oficial

Versión 73 de Adquirencia fue cerrada oficialmente. Se acordó:
- **Funcionalidad "Convivencia reporter"** asignada como Prioridad 2 (fix urgente fuera del paquete principal, ya estaba finalizada previamente)

### Proyecto MODO

Trabajos completados (no requiere acciones pendientes en este período).

### Action Items del Equipo

Múltiples tareas asignadas a Matías Alzogaray, Daniela Collia, Nicolás Colón con deadlines a definir. Ver minuta completa para matriz de responsables.

> **Relacionado:** Este análisis completa la foto de prioridades de Adquirencia para la roadmap de Q3/Q4; impacta calendario de despliegues (ver `2026-09-08_cronograma_septiembre_despliegues.md`).
