---
id: 2026-08-15_wallet_contracargo_debin_w71
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15), tickets WS-1252, WS-816"
producto: wallet
tema: Contracargos de DEBIN — fix de CoelsaId y endpoint de inserción manual
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/debin_y_fondeo.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Ampliar la sección "Contracargos de DEBIN Recurrente" con 2 tickets nuevos:

- **`CoelsaId` mapeado mal en `dbo.ContracargoDebines` (WS-1252):** el webhook de contracargo trae el ID del contracargo en sí en el campo raíz `id` (formato `"DebinContracargo-<coelsaId>"`) y el ID de la operación original DEBIN dentro de `data.id`/`data.transaction_ids[]`. El sistema estaba guardando el ID de la **operación original** en la columna `CoelsaId` de `dbo.ContracargoDebines`, en vez del ID del contracargo. Fix: tomar el `id` del mensaje, quitarle el prefijo `"DebinContracargo-"`, y guardar eso como `CoelsaId` del contracargo.
- **Endpoint para insertar contracargos manualmente (WS-816):** nuevo endpoint de Wallet pensado para Administración/Soporte, para los casos donde el contracargo no llegó por el webhook del banco. Recibe un ID Coelsa de contracargo, dispara internamente una consulta a Coelsa (`GET .../debins/{id}/psp/{idPsp}`) para obtener la operación DEBIN original (`operacion.detalle.idOperacionOriginal`), valida que esa operación exista en la base de Bind PSP y que el contracargo no esté ya registrado, y si todo es válido replica el flujo normal de contracargo (mismo comportamiento que si hubiera llegado por webhook: débito de saldo disponible, envío a Recycle del remanente si no alcanza, deshabilitación de cuenta si corresponde, webhooks pertinentes). Responde 422 si el contracargo ya existe o si la operación original no se encuentra en la base.
