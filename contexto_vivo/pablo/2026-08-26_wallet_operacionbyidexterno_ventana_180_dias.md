---
id: 2026-08-26_wallet_operacionbyidexterno_ventana_180_dias
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), ticket WS-1287"
producto: wallet
tema: Endpoint GET OperacionByIdExterno amplía la ventana de búsqueda de 3 días a 180 (configurable sin deploy)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

[WS-1287](https://bindpsp.atlassian.net/browse/WS-1287), W 72, Epic WS-518. Pedido de negocio: `GET /api/v1/OperacionByIdExterno/{IdExterno}` solo encontraba operaciones de hasta **3 días** de antigüedad — insuficiente para que una organización conozca el estado real de una operación más vieja.

**Cambio de comportamiento (relevante para Soporte/integraciones):**
- Ventana ampliada a **180 días (6 meses)**, configurable en caliente vía la Especificación de Wallet `Operaciones/DIAS_CONSULTA_ID_EXTERNO` (sin deploy) — si la especificación no existe o no es parseable, cae a `appsettings.DíasConsultaIdExterno = 180`.
- **Antes de esta versión, una operación entre 3 y 180 días devolvía 404. Ahora devuelve 200 con datos.** Es el cambio de comportamiento más relevante para QA/Soporte de esta entrega.
- El mensaje de error 404 ahora incluye la cantidad de días consultados: `"No se encontró la operación para el id externo: {IdExterno}, ó es anterior a los {N} días"`, y el logging distingue `Warning` (existe pero excede la ventana) de `Information` (no existe).
- Mejora de performance acompañante: nuevo índice `IX_Operaciones_IdExterno_OrganizacionId` sobre la tabla de Operaciones — **prerequisito externo gestionado por DBA**, no incluido en este PR de código; el valor de 180 días no debe activarse operativamente hasta que DBA confirme índice + especificación en cada ambiente (orden de deploy: el código puede desplegarse antes, pero sin efecto real hasta ese paso).
- Se corrigió además `DateTime.Now` → `DateTimeOffset.Now` (alineado con `FechaCreacion`) y se agregó cache de 15 minutos a la lectura de la especificación.

**Alcance del PR:** solo `Wallet.Operaciones.Queries`. Los scripts de base de datos (índice + fila de especificación) quedaron fuera de esta entrega, gestionados por DBA como prerequisito externo — a verificar en cada ambiente antes de confiar en la ventana completa de 180 días.

**Al mergear:** agregar como nueva entrada dentro de "Operación de Wallet (pedidos de Soporte)" o como parte de una subsección "tramo W72" (mismo patrón que la de W71 ya existente en este archivo) — el cambio es relevante para cualquiera que use este endpoint para conciliación o troubleshooting de operaciones viejas.
