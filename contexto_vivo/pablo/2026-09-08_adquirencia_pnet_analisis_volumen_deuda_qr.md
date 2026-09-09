---
id: 2026-09-08_adquirencia_pnet_analisis_volumen_deuda_qr
pm: pablo
fecha_captura: 2026-09-08
fuente: "sesión de análisis de datos con el PM — raw/analisis cantidad de deudas.xlsx (ago-sep) + raw/analisis deudas junio y julio.xlsx (jun-jul, sumado por el PM para ampliar la ventana), export dbo.Deuda por entidad/día/estado + dim_entidades.csv, a raíz de reclamo de DEPAY (WhatsApp) y ticket Jira AD-1676"
producto: adquirencia
tema: Investigación en curso sobre el reclamo de demora en QR de DEPAY/AD-1676 — hipótesis de PNET como causa, todavía sin confirmar
tipo: iniciativa
proyecto: PRD-66
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 4b0d3d1e684ff33256a33a29f86746dfd5c7cc9a
---

**Novedad puntual sobre PRD-66 (Provincia NET: creación masiva de QR) — investigación en curso, sin conclusión cerrada.** A raíz del reclamo de demora en generación de QR de DEPAY (WhatsApp) y el ticket [AD-1676](https://bindpsp.atlassian.net/browse/AD-1676) (atribuido a PNET), un análisis de datos (`dbo.Deuda` por entidad/día/estado, 98 días — junio a septiembre) confirmó que Provincia NET es el mayor generador de Deudas del sistema (2.563.059 en el período, 2,5× la entidad #2), con picos ≥100.000/día tanto antes como después del pase a producción de su carga masiva por SFTP (13/08).

**La hipótesis inicial ("PNET cambió su forma de operar y por eso ahora se satura la cola") quedó en duda tras objeción del PM, verificada con los propios datos**: la concentración de PNET en los picos de junio-julio (94,8%-96,7% del volumen total del sistema esos días) fue igual o mayor que la del pico del 01/09 (78,9%) — si la sola dominancia de PNET saturara la cola de generación de QR, junio y julio deberían haber tenido el mismo síntoma, y no hay evidencia de reclamos esos meses. Se encontró un lead alternativo sin confirmar: un cambio de parametrización de tiempos de **resolución de pagos** QR contra Coelsa (proyecto `bajar-tiempos-pagos-qr`/PRD-199, de Nicolás Colón — ver `3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md §"Parte 5"`) entró en producción el 2026-08-31, un día antes de la ventana de reclamos — mecanismo distinto al que reporta DEPAY (que pregunta por el estado de una Deuda recién creada, no por el resultado de un pago), pero la coincidencia temporal es fuerte y no está descartada.

**Pendiente antes de cualquier conclusión o comunicación a Fintexa/PNET**: confirmar con Ingeniería (Nicolás Colón, Gonzalo Rivera) si ambos mecanismos comparten cola/infraestructura, y si hubo reclamos de latencia de Deuda/QR en junio-julio que no llegaron a escalarse a Jira. Detalle completo, incluyendo el desglose diario por entidad y la tabla de concentración por pico, en [`1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §7`](../prd-66_provincianet_creacion_masiva_qr/proyecto.md) y `gaps.md`. Tarea de seguimiento: T-072 en `tareas.md`.
