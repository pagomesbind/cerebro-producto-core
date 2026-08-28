---
id: 2026-08-26_wallet_fci_settlement_info_dos_validaciones_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), tickets WS-1317, WS-1315"
producto: wallet
tema: Endpoint de Liquidaciones por Usuario (Settlement/Info) — se cierran 2 defectos de seguridad/validación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md §4.5 — lista a WS-1317 explícitamente como uno de los 'Defectos de contrato abiertos... ninguno con fix confirmado'. Este ticket lo cierra."
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

§4.5 ya documenta el endpoint `GET /api/v1/Settlement/Info` (Historia WS-730, "en desarrollo, con defectos abiertos") y lista a **WS-1317 explícitamente** como uno de los defectos de contrato pendientes ("No valida que la cuenta esté habilitada para FCI antes de responder"). Esta ingesta cierra ese defecto y suma uno más que no estaba en la lista original:

**1. [WS-1317](https://bindpsp.atlassian.net/browse/WS-1317) — cierra el defecto ya listado (1 SP):** el endpoint devolvía 200 con datos aunque la organización enviada en `x-entidad` no tuviera la funcionalidad de remuneración habilitada, o el `IdCuentaComitente` no perteneciera siquiera a esa organización. Fix: validación de organización habilitada (los campos `FechaHoraBaja`/`Habilitada` de `OrganizacionesParametros` solo son editables manualmente por BD hoy — no hay endpoint de gestión) + validación de que la cuenta comitente exista.

**2. [WS-1315](https://bindpsp.atlassian.net/browse/WS-1315) — defecto nuevo, no estaba en la lista de §4.5 (0.5 SP):** con una cuenta comitente que pertenece a una organización **distinta** de la del header `x-entidad`, el endpoint respondía `200 OK` con resultado vacío (`totalRecords: 0`) en vez de señalar el problema — Nicolás Colón pidió originalmente 403, se resolvió con validación equivalente sin exponer si la cuenta existe o no en otra organización.

Ambos cerrados en la misma tanda de desarrollo, validados por Ana (QA) el 2026-08-07/10.

**Al mergear:** en §4.5, mover WS-1317 de la lista de "defectos abiertos" a texto de cierre (ya no está abierto), y agregar WS-1315 como hallazgo adicional cerrado en la misma versión — dejar claro que de los 5 defectos originalmente listados (WS-1317/1306/1305/1304/1303) solo WS-1317 se resolvió en W72; los otros 4 siguen abiertos salvo que un barrido posterior indique lo contrario.
