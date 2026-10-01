---
id: 2026-10-01_arquitectura_informe_coe_septiembre
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_mails — mail \"RE: INFORME Mensual Comité de Arquitectura COE\" (septiembre 2026), Alejandro Sfrede (Fintexa), 2026-10-01"
producto: transversal
tema: "Informe mensual COE septiembre 2026 — zero-downtime pasa a estándar obligatorio, desarrollo de interoperabilidad entre billeteras (Open Finance/BCRA)"
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/relacion_con_fintexa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Alejandro Sfrede (Fintexa) compartió el 2026-10-01 el informe mensual del Comité de Arquitectura COE correspondiente a septiembre 2026 (período 09/2026, consolidado sobre 4 sesiones del mes). Continúa la serie de informes mensuales ya conocida (julio y agosto ya capturados en el mismo hilo histórico `19fdd426c2490389`).

**Tres frentes de fondo señalados para septiembre:**

1. **Despliegues sin interrupción de servicio (zero-downtime) pasan a estándar obligatorio** — sus tickets de implementación están en revisión final antes del pasaje a producción. Esto confirma y formaliza el roadmap que en el informe de agosto figuraba como "en progreso, ampliado a 40+ servicios de Wallet".
2. **Desarrollo de interoperabilidad entre billeteras** (marco regulatorio del Banco Central) avanzó, con una estrategia de despliegue diseñada explícitamente para no arriesgar la operación actual. En el detalle por estado figura como "Interoperabilidad entre billeteras Auth2 (AUTH EXTERNAL para Open Finance)" dentro de 🟢 En desarrollo.
3. **Exposición de seguridad real identificada en un panel administrativo**, con la corrección ya definida y lista para implementarse — coincide con el hallazgo del Admin Centralizador (CVSS 8.7) ya capturado y tratado como hotfix en corridas anteriores (`contexto_vivo/` 2026-09-28/29); este informe no aporta detalle nuevo sobre ese punto, solo lo confirma a nivel de reporte ejecutivo de arquitectura.

**Detalle completo por estado (septiembre 2026):**
- ✅ Completado: corrección del cuello de botella de performance en Notificaciones por base de datos · sanitización de datos sensibles en registros técnicos · autenticación externa en Wallet.
- 🟢 En desarrollo: interoperabilidad entre billeteras Auth2 (Open Finance) · migración de colas de mensajería · simulación de proveedores externos para pruebas (primer proveedor: GP) · estándar único de registro de eventos (logs) · monitoreo de salud de servicios.
- 🟡 En revisión y aprobación: despliegues sin interrupción de servicio por vertical · notificaciones/webhooks (estabilidad de envío) · estándar de desarrollo seguro.
- 🔵 Listo para iniciar desarrollo: optimización de la base de datos de Deuda · regla de control de cambios de contrato de API · certificación ISO 9001 · fix de red (DNS) para dos servicios.

**Certificaciones:** las tres certificaciones en curso (ISO 9001, ISO 27001 y el programa de seguridad exigido por el socio de procesamiento) están en preparación — ver item separado `2026-10-01_cumplimiento_normativo_certificaciones_iso_coe.md` para el detalle de ese punto (va a un destino distinto, `cumplimiento_normativo/`).

> Fuente: mail "RE: INFORME Mensual Comité de Arquitectura COE" — Alejandro Sfrede (Fintexa), 2026-10-01, threadId `19fdd426c2490389`.
