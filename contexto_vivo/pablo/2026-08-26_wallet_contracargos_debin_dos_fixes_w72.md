---
id: 2026-08-26_wallet_contracargos_debin_dos_fixes_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), tickets WS-1420, WS-1057"
producto: wallet
tema: Contracargos de DEBIN recurrente — dos fixes de robustez (Epic WS-810, mismo Epic que PRD-140)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/debin_y_fondeo.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

⚠️ **Ambos tickets están bajo el Epic [WS-810](https://bindpsp.atlassian.net/browse/WS-810), el mismo que alimenta el proyecto vivo `1_proyectos/.../prd-140_contracargos_debin_recurrente/`.** Por alcance de esta skill no se cruza contra ese proyecto ni se edita su `proyecto.md` — queda señalado en el reporte del barrido para que el PM lo refresque si corresponde.

**1. Endpoint de conciliación manual de contracargos usaba la consulta incorrecta a Coelsa ([WS-1420](https://bindpsp.atlassian.net/browse/WS-1420), 3 SP):**

`POST /api/v1/Operaciones/ConciliarContracargoDebin` (el mismo endpoint manual para Soporte/Administración ya documentado en la sección "Contracargos de DEBIN Recurrente" — ver ticket WS-816, W71) consultaba Coelsa vía `/debins5` (`GetDebin5`) para resolver el `IdOperacionOriginal`, pero ese endpoint de Coelsa trae un código numérico donde el sistema esperaba el `IdCoelsa` alfanumérico de 22 caracteres real del contrato Debin. Resultado: la búsqueda de la operación original en base fallaba con 422 ("operación original inexistente") aunque la operación sí existiera en Wallet. Fix: usar `/debins` (`GetDebinById`) en su lugar, que sí trae el ID alfanumérico correcto. Sin cambio de contrato HTTP del endpoint ni de esquema de base.

**2. Contracargo perdido si llegaba antes de que la operación original quedara Aprobada ([WS-1057](https://bindpsp.atlassian.net/browse/WS-1057), 3 SP):**

Caso real: el webhook `debin.refunded` de Coelsa podía llegar mientras la operación original todavía estaba en estado `AConsultar` (no `Aprobada` = "2") — el flujo de contracargo exigía ese estado y el aviso se perdía.

Nueva lógica en `WebhookRefundedDebinCommandHandler`:
- Si el estado ya es Aprobada → flujo normal sin cambios.
- Si está en `AConsultar` → reconsulta a Coelsa vía `GetDebin4`. Si Coelsa responde `ACREDITADO`, se actualiza la operación a Aprobada y continúa el flujo de contracargo (comprobante, `Devuelta`/`Devuelta parcial`, notificación). Si responde `INICIADO`/`EN CURSO`, dispara un retry in-process del consumer con backoff **10s/30s/60s** (config de cola `WebhookRefundedDebin-Quorum`, replicada en los 6 `appsettings` de cada ambiente), liberando antes el cache de dedup para que el reintento no se descarte como duplicado. Si Coelsa devuelve un estado final rechazado, la operación pasa a `Auditar` con log explícito, sin crear contracargo. Si se agotan los reintentos sin `ACREDITADO`, también pasa a `Auditar` (sin ir a cola de error).
- Idempotencia (RF-004): se verifica que no exista ya un `ContracargoDebin` para la operación antes de crear uno nuevo, para no duplicar en reprocesos.

Sin cambios de contrato, endpoint ni esquema de base. Validado en STG por Nicolás Colón el 2026-08-14 (dos caminos: contracargo por webhook simulado y por endpoint conciliador manual, ambos con débito de saldo confirmado).

**Al mergear:** agregar ambos como nueva subsección dentro de "Contracargos de DEBIN Recurrente" (después de "Corrección de mapeo y endpoint manual (W 71)" y antes de "Deshabilitación de cuenta..."), y avisar al PM del proyecto PRD-140 sobre la novedad del Epic WS-810 compartido.
