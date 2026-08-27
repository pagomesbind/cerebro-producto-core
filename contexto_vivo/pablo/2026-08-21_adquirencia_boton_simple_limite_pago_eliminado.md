---
id: 2026-08-21_adquirencia_boton_simple_limite_pago_eliminado
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Análisis de riesgos AD V72' (2026-08-21 14:02, docId 1cuABvOG3eEhMaN3XDQtF5ofpEqHmXewlt85OeXfC7EY)"
producto: adquirencia
tema: Botón Simple 2.0 — eliminación del límite de $9M en la creación de links de pago
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En la reunión de riesgo de AD V72 (despliegue 27/08/2026) se aprobó eliminar la validación que hoy limita la creación de links de pago de Botón Simple 2.0 a un monto máximo de **$9.000.000**. Matias Alzogaray lo presentó como un ticket de soporte, sin motivo de negocio específico documentado en la minuta — se retira directamente la restricción, sin reemplazo por un tope configurable. Clasificado con semáforo verde (bajo riesgo).

Dato relevante para contexto histórico: este mismo límite de $9M ya había sido señalado como punto sin resolver por un cliente (Provincia NET preguntó en julio si el tope "podía ser más" — ver `wiki/1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §2`, aunque ese caso es sobre el monto máximo de un QR de pago único, no necesariamente el mismo límite de Botón Simple 2.0; a confirmar si son el mismo control o distinto al mergear este item).

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — sección Decisiones, "Eliminación de límite de pago" y Detalles ([00:42:44]).
