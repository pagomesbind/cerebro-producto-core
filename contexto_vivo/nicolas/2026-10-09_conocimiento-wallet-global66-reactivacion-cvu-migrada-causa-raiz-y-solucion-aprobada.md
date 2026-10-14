---
id: 2026-10-09_conocimiento-wallet-global66-reactivacion-cvu-migrada-causa-raiz-y-solucion-aprobada
pm: nicolas
fecha_captura: 2026-10-09
fuente: "Sesión /idea_start con Nicolás Colón (2026-10-09), causa raíz validada por el PM con Juan Pablo Carubelli (Fintexa); historia WS-1861 (Gonzalo Rivera, 2026-10-07, caso Fintexa EM-826)"
producto: wallet
tema: Global 66 / CVUs migradas — causa raíz precisa de por qué rehabilitar crea una CVU nueva, estado real de la CVU original, alcance (no aplica a AGCyP) y solución aprobada (PRD-279)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no — completa y actualiza la sección 'Global 66 — reactivar una CVU eliminada crea una CVU nueva (cuentas migradas)', mergeada el 2026-09-11"
confianza: alta
estado: en_cola
---

**Actualiza** la sección "Global 66 — reactivar una CVU eliminada crea una CVU nueva (cuentas migradas)" (desde la Daily del 2026-09-09).

**Causa raíz precisa (validada por Nicolás Colón con Juan Pablo Carubelli, Fintexa, 2026-10-09):** el endpoint de crear y de rehabilitar la CVU es el mismo, tanto en Wallet como en API Bank. Wallet genera la CVU en API Bank con `clientId` = `IdCuenta` de Wallet. Las CVUs migradas (Global 66 migró su PSP de COMAFI a Bind desde oct-2025) no nacieron con esa regla, pero Bind las tomó como válidas; al rehabilitarlas, el endpoint va con `clientId` = `IdCuenta`, no encuentra la original y crea una nueva. El problema no está en cómo opera la organización (Global 66 deshabilita/rehabilita por API correctamente), sino en lo que resuelve internamente el endpoint.

**Estado de la CVU original:** queda deshabilitada para API Bank/Coelsa y no puede operar — "es como si no existiese". El usuario final queda operando con un número nuevo.

**Alcance:** afecta a toda organización con CVUs migradas (Global 66; Astropay tuvo el mismo problema). **No aplica al Agente de Cobros y Pagos** — según el PM, allí no existe esa casuística.

**Novedad de casos:** además de las 3 cuentas del 09/09, el 2026-10-07 se reportó un caso nuevo (Fintexa EM-826) → historia [WS-1861](https://bindpsp.atlassian.net/browse/WS-1861) (Gonzalo Rivera, High, Backlog): pide respetar la CVU original al rehabilitar para Global 66 "o cualquier otra entidad que venga de una migración", y cotizar/ver con Mauro Suppan si lo paga el cliente. La decisión provisional del 09/09 (reactivación manual a pedido) no impide que los casos se sigan generando, porque la organización sigue rehabilitando por API.

**Solución aprobada (shaping, IDEA [PRD-279](https://bindpsp.atlassian.net/browse/PRD-279), 2026-10-09):** el endpoint de rehabilitación, ante una CVU migrada, reactiva usando el identificador que se deriva de la CVU ya guardada en Wallet (`WalletCuentaDB.CuentasCVU.CVU`) en vez del `IdCuenta` — sin agregar un atributo nuevo ni carga masiva (adapta la propuesta original de Pablo Gomes de "incorporar un atributo de identificador de cliente"). Incluye un reproceso único de los casos ya afectados. La reactivación manual (Swagger + script) queda como puente hasta el release. BAU, S–M, 2 SP preliminares. Factibilidad de la derivación para todas las orgs migradas pendiente de validar con Fintexa; si no fuera posible, el repuesto es persistir el identificador original (L, 7–20 SP).

> Fuente: sesión `/idea_start` (2026-10-09); WS-1861.
