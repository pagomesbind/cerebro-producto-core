---
id: 2026-08-15_wallet_fci_duplicados_w71
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15), ticket WS-1284; atribución WS-1296, WS-730, WS-1306, WS-1305, WS-1304, WS-1303 (mismo release, ya documentados vía minuta de reunión)"
producto: wallet
tema: FCI — registros duplicados en CuentasRemuneradas por condición de carrera entre PODs
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9306bc6b7cffeb57db264f132b0e0e6a1ec53d8e
---

**Contenido nuevo:** bug de condición de carrera en FCI (WS-1284, estado "EN QA" al momento del release — igual publicado en W 71, criterio de versión no de ticket): dos PODs del microservicio `Shared.Remunera` consumen el mismo mensaje de cola y ambos insertan un registro en la tabla `FCICuentasRemuneradas` para el mismo `IdCuenta`, generando duplicados. Objetivo del fix: evitar la duplicación (constraint o lock a nivel de `IdCuenta`).

**Solo atribución de versión, sin contenido nuevo (ya documentados vía `/sync_meetings`, minuta de reunión):**
- WS-1296 (PRD-185, validar misma titularidad de Suscripciones de Debin) — ya en `debin_y_fondeo.md`.
- WS-730 (endpoint `GET .../investment/settlement/info`), WS-1306 (`Sort` case-sensitive), WS-1305 (`IdCuentaComitente` no valida numérico), WS-1304 (inconsistencia formato de fecha), WS-1303 (nomenclatura de parámetros mezclada) — ya en `cuenta_remunerada_fci.md` (líneas 244-251 aprox.), quedaban con "release W 71 sin fecha aún"; esta ingesta confirma **releaseDate 2026-07-15**.
