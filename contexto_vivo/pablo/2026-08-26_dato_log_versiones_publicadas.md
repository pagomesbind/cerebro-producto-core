---
id: 2026-08-26_dato_log_versiones_publicadas
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — barrido incremental 2026-08-26 (delta desde 2026-08-15)"
producto: transversal
tema: Filas nuevas para el log de control de versiones publicadas
tipo: dato
destino_propuesto: 3_recursos/datos/log_versiones_publicadas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Aplicar byte a byte (append a la tabla "Versiones ingestadas", y actualizar la cabecera de "Último barrido"):

**Cabecera** — reemplazar la línea `> **Último barrido:** 2026-08-15 ...` por:

```
> **Último barrido:** 2026-08-26 — barrido incremental completo vía API, sin novedades en OB/ARD/SER; 3 versiones nuevas (1 AD, 2 WS)
```

**Filas nuevas** (agregar al final de la tabla "Versiones ingestadas"):

```
| AD | AD 71.3 | 2026-08-24 | 2026-08-26 | AD-1528 | Pasaje a PROD AuthExternal V2, etapa 3/3 — cierra la migración iniciada en W 71.4 FIX/W 71.6 FIX (WS-1429/WS-1444). Migra Shared.Cvu, Shared.Debin, Shared.Coelsa.Alias → resuelve gap de `wallet/organizaciones_y_configuracion.md §7` (ver item de contexto_vivo `2026-08-26_wallet_authexternal_v2_etapa3_cierre_migracion`). |
| WS | W 71.8 (PagosFX) | 2026-08-10 | 2026-08-26 | WS-1484 | Config AppSetting PROD: hosts faltantes de MsComprobante/MsCuentaQueries/MsInvestmentService/MsOperaciones/Mastercard/MsArdid. Ticket sin desarrollo funcional ("no requiere pruebas", cerrado directo). ⚠️ La descripción del ticket incluye ClientSecret y OcpApimSubscriptionKey de Ardid en texto plano — mismo patrón de exposición ya señalado en WS-313 (W68, 2026-03). Sin merge de wiki (ruido operativo de config). |
| WS | W 72 | 2026-08-18 | 2026-08-26 | 18 tickets: WS-1461, WS-1447, WS-1441, WS-1437, WS-1420, WS-1416, WS-1374, WS-1351, WS-1317, WS-1315, WS-1313, WS-1308, WS-1287, WS-1273, WS-1191, WS-1113, WS-1083, WS-1057 | Tanda grande: bug de cache Redis de AuthExternal V2 nunca funcional + fix de path Ardid en alta de org (WS-1461/WS-1447 → `organizaciones_y_configuracion.md §7`); validación de longitud CVU/CBU 22 dígitos en 3 microservicios (Wallet.Bind/Cuenta/Operaciones, hallazgo crítico: columna CVU era `nvarchar(100)`) (WS-1191/WS-1113/WS-1083 → nueva sección `organizaciones_y_configuracion.md`); eliminar CVU deshabilitaba la cuenta, contraparte del cluster W71 WS-1077/1078 (WS-1437 → `pedidos_de_clientes_y_hallazgos_operativos.md`); 2 fixes de contracargos DEBIN, Epic WS-810 = mismo Epic de PRD-140 vivo — avisar al PM (WS-1420/WS-1057 → `debin_y_fondeo.md`); migración EasyNet de transferencias entrantes completada (cierra deuda de §10) + tiempo de reconsulta parametrizable (aún EN QA) (WS-1416/WS-1273 → `historial_confiabilidad_transferencias_y_comprobantes.md §10`); resiliencia FCI paso 6 ante 502 de PCNT (WS-1374 → `cuenta_remunerada_fci.md §4.2`); cierra 1 de los 5 defectos abiertos de `Settlement/Info` + 1 hallazgo nuevo (WS-1317/WS-1315 → `cuenta_remunerada_fci.md §4.5`); ventana de `OperacionByIdExterno` de 3 a 180 días, cambio de comportamiento 404→200 (WS-1287 → `pedidos_de_clientes_y_hallazgos_operativos.md`); identifica el ticket sin nombrar de `dolar_ccl.md §3.6bis` (WS-1351 → `dolar_ccl.md`). WS-1441 "No aplica" (soporte viejo, pendiente de análisis) y WS-1313/WS-1308 ya documentados en PRD-200/PRD-193 vivos (solo atribución) — sin merge de wiki. |
```
