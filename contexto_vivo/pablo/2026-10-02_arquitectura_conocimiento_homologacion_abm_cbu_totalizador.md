---
id: 2026-10-02_arquitectura_conocimiento_homologacion_abm_cbu_totalizador
pm: pablo
fecha_captura: 2026-10-02
fuente: "/sync_mails — hilo \"Homologación ABM de CBU\" (threadId 1a0f7c4a7d26484a), Coelsa (icm@coelsa.com.ar), 2026-10-01"
producto: transversal
tema: Coelsa actualiza el servicio ABM de CBU vinculado al Totalizador de cuentas — registro de fecha de alta/baja de cuentas bancarias
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/integracion_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75ba8d792351add07011499b503adabf55d5e4bd
---

Coelsa notificó a Banco Industrial (Pablo Gomes en copia) una actualización del servicio **ABM de CBU vinculado al Totalizador de cuentas**: la nueva versión incorpora el registro de **fecha de alta y fecha de baja** de las cuentas bancarias, en línea con requerimientos normativos vigentes (sin especificar cuál — a confirmar si se relaciona con alguno de los requisitos ya trackeados en `cumplimiento_normativo/`).

**Cronograma:**
- Ambiente de **Homologación** disponible desde el **24/08/2026** hasta el **16/10/2026** inclusive.
- Salida a **Producción** a partir del **18/10/2026**.

**Documentación técnica publicada por Coelsa:**
- API nuevo: `https://documentacion.coelsa.com.ar/aliascbu/#api-cbu-nuevo`
- Batch nuevo: `https://documentacion.coelsa.com.ar/aliascbu/#batch-cbu-nuevo`

Destinatarios principales: equipo de desarrollo/productos de Banco Industrial (`desarrollo@bancoindustrial.com.ar`, `productos@bancoindustrial.com.ar`) e Implementaciones de Bind PSP — no se identificó una acción puntual asignada a Producto en el propio mail; de requerirse homologar antes del 16/10, es responsabilidad operativa del equipo de Implementaciones/Integraciones, no se registra tarea personal por no estar asignada explícitamente a Pablo Gomes.

> Fuente: mail "Homologación ABM de CBU" — Coelsa (`icm@coelsa.com.ar`), 2026-10-01, threadId `1a0f7c4a7d26484a`.
