---
id: 2026-08-26_wallet_eliminar_cvu_deshabilita_cuenta_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), ticket WS-1437"
producto: wallet
tema: Eliminar CVU deshabilitaba la cuenta como efecto colateral (contraparte del cluster W71 "eliminar cuenta debe deshabilitar")
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

El archivo ya documenta (tramo W71) el cluster "eliminar cuenta debe deshabilitar" (WS-1077/WS-1078): los endpoints de eliminar cuenta/cuenta+CVU **no** deshabilitaban la cuenta, dejándola con `habilitado = 1`. [WS-1437](https://bindpsp.atlassian.net/browse/WS-1437) (W 72) es el bug espejo, del lado opuesto: el endpoint `DELETE /api/v1/CVU/{id}` (eliminar **solo** el CVU, sin tocar la cuenta) estaba deshabilitando la cuenta como efecto colateral no deseado — solo `DELETE Cuenta` y `DELETE CuentaYCVU` deben deshabilitar la cuenta.

**Causa:** en `CuentaCVU.DeleteCuentaCVU` se asignaba `cuentaCVU.Cuenta.Habilitado = false` (la entidad hija CVU mutando el agregado padre Cuenta) y `DeleteCuentaCVUCommandHandler` persistía con `_cuentaRepository.UpdateAsync(cuentaCVU.Cuenta)` (EF marcaba toda la fila de `Cuentas` como modificada).

**Fix:** se remueve esa mutación cruzada — eliminar un CVU ya no toca `Cuentas.Habilitado`. Nicolás Colón pidió explícitamente que el ticket pasara como hotfix (2026-07-28). Sin cambio de status HTTP; el cambio es solo de efecto en base. Las cuentas ya dañadas antes del fix **no se corrigen** con este PR (no hay migración de datos retroactiva). Validado por Andrea Orsini el 2026-08-14 (batería de casos: CVU activo→DELETE CVU→cuenta sigue habilitada; DeleteCuentaYCVU sigue inhabilitando como antes — regresión crítica cubierta).

**Al mergear:** agregar como nueva subsección "Bugs y pedidos operativos — tramo W72" (mismo patrón que la de W71 ya existente), dejando explícita la relación con WS-1077/WS-1078 — son dos mitades del mismo problema de acoplamiento CVU↔Cuenta detectado en dos releases consecutivas.
