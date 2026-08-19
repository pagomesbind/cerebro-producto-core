---
id: 2026-08-14_wallet_fci_mvp2_avance
pm: pablo
fecha_captura: 2026-08-17
fuente: "/sync_mails — mail \"Informe Estado Proyectos Emisión al 14/08/2026\" (threadId 1a001fd354c0211d), Nicolás Pomponio (Fintexa), 2026-08-14"
producto: wallet
tema: Informe semanal Emisión — avance Épica FCI MVP2
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9306bc6b7cffeb57db264f132b0e0e6a1ec53d8e
---

**Contexto:** informe semanal recurrente de Fintexa sobre el proyecto Wallet — esta semana no hubo despliegue de versión (se planifica W 72 a PROD el miércoles 19/08 por la mañana, ver el ítem separado sobre el mail de pre-despliegue del mismo día).

**Épica FCI (Fondos Comunes de Inversión):**
- Estado: 🟢 en curso. Se espera entregar el MVP2 en PROD para fines de agosto 2026 (fecha original de publicación del MVP1 fue 10/12/25).
- Se repitieron problemas productivos por cambio de IP de los servicios de Poincenot (mismo patrón de incidente ya documentado en el archivo) — se lograron salvar y el proceso del 14/08 terminó OK.
- Desarrollo en curso: orquestador para alta de nuevos clientes desde Soporte, y una nueva forma de iniciar los procesos de FCI para todas las organizaciones con remuneración de cuentas.
- También en curso: mejoras complementarias para configuración de organizaciones por API, y análisis de alertas ante fallas de los procesos.
- Bloqueo/alerta activa: hay que controlar diariamente el proceso de **Coppel** y **La Virginia** en PROD (relacionado con el problema de finalización tardía reportado el mismo día por Soporte — ver ítem separado `2026-08-14_wallet_fci_webhook_finalizacion_virginia.md`).
