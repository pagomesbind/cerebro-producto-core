---
id: 2026-10-01_ardid_webhook_bloqueo_cuenta_y_fix_antifraude_recurrente
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_meetings — reunión 'W 73 - Análisis de riesgos' (docId 1k3Fqt1CNGhgnLkEi_rfg5slLUW80YNWO6c0MqWvS7jo), 2026-10-01 14:59, compartida (malzogaray)"
producto: ardid
tema: Nuevo webhook de aviso de bloqueo de cuenta y fix de control antifraude en débito recurrente con tarjeta de crédito (V73)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Dos mecánicas de integración Ardid↔Wallet confirmadas en el análisis de riesgos de la versión 73 (despliegue 08/10/2026, ver `getnet_oauth2_resolve/proyecto.md §8`):

**WS-1398 — Deshabilitación automática de cuentas bloqueadas en Ardid (semáforo rojo):** cuando Ardid marca una cuenta como bloqueada, Wallet ahora la deshabilita automáticamente para evitar cashouts no autorizados — hoy esa sincronización no es automática. Se agrega además un **webhook nuevo** que avisa a los clientes integrados cuando una cuenta queda bloqueada por este motivo. Tarea previa comprometida: documentar el webhook en la plataforma de developers y notificar a los clientes antes de la publicación — a cargo de Pablo Gomes (ver `tareas.md` T-160). Clasificado en rojo por su impacto directo sobre la operatoria de cuentas ya existentes.

**WS-1718 — Corrección de cobertura antifraude en débito recurrente con tarjeta de crédito:** se detectó que las operaciones de **débito recurrente con bin de crédito** no estaban pasando por el monitoreo antifraude de Ardid — gap de cobertura que se corrige en esta versión. El cambio de lógica requiere una regresión específica coordinada por Andrea Orsini (QA) antes del despliegue — reclasificado de verde a amarillo en la propia reunión por ese motivo.

**Contexto del acuerdo general de control antifraude:** en la misma reunión, Nicolás Colón confirmó que dar de alta todas las cuentas faltantes en Ardid (saneamiento previo al despliegue) fue una medida autorizada por Emma Vignoles para garantizar el control antifraude al 100% antes de V73 — ligado también al ticket WS-1520 (rechazo automático de operaciones si Ardid responde con error o timeout, en vez de dejarlas pasar sin control).

> Fuente: reunión "W 73 - Análisis de riesgos", 2026-10-01, minuta Gemini (detalles, sección "Ticket WS 1398" y "Ticket WS 1718").
