---
id: 2026-08-25_coto-gap-campos-cuentacorriente-vs-comprobantes-operacion
pm: nicolas
fecha_captura: 2026-08-25
fuente: "Charla directa con el usuario sobre migración de COTO de GET Movimientos a GET /CuentaCorriente; comparación 1:1 con payloads reales para el mismo ComprobanteId (14648633) aportados por el usuario, contrastados contra la documentación pública en https://psp.bind.com.ar/developers (2026-08-25)"
producto: wallet
tema: Campos que se pierden en GET /CuentaCorriente respecto al legacy GET Movimientos, confirmado con payload real
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/apis_expuestas/conciliaciones/endpoint_get_consultar_movimientos_cuenta_corriente.md (nota comparativa)
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

## Contexto

El cliente **COTO** fue transicionado del endpoint legacy `GET Movimientos` (ya no existe en el portal público actual — `https://psp.bind.com.ar/developers/apis/movimientos` redirige a home) al endpoint vigente `GET /CuentaCorriente` (`walletentidad-operaciones/v1/api/v1.201/CuentaCorriente`) de la API pública de Wallet.

El usuario aportó dos payloads reales para el **mismo `ComprobanteId` (14648633)**, uno de cada endpoint, lo que permitió un diff 1:1 confirmado (no inferido).

## Diff confirmado — nivel comprobante (raíz de `movimientos[]`)

Sin pérdida de datos, solo renombres: `tipoComprobanteId`→`idTipoComprobante`, `cuentaId`→`idCuenta`. El resto de los campos (`idComprobante`, `descripcionTipoComprobante`, `fecha`, `importe`, `saldo`, `signo`, `referencia`) se mantienen igual.

## Diff confirmado — nivel operación (`operacion{}` en Movimientos vs. `datosOperacion{}` en CuentaCorriente)

**Ausentes del payload real de `datosOperacion`, pese a estar documentados como parte de su esquema en el portal público:**
- `fechaCreacion` (era `FechaCreacion` en Movimientos, con valor real no nulo)
- `fechaActualización` (era `FechaActualizacion` en Movimientos, con valor real no nulo)
- `comprobanteDevolucionId` (era `null` en Movimientos para este caso, pero la key ni aparece en CuentaCorriente)

**Esto es más que un renombre: es una discrepancia entre lo que documenta `https://psp.bind.com.ar/developers/apis/consultarmovimientoscuentacorriente` (que sí lista estos 3 campos como parte de `datosOperacion`) y lo que la API devuelve en la práctica.** Ver item hermano [2026-08-25_gap-doc-vs-real-cuentacorriente-datosoperacion](2026-08-25_gap-doc-vs-real-cuentacorriente-datosoperacion.md) (`tipo: gap`).

**Ausente por diseño (nunca documentado para `datosOperacion`):**
- `importeOperacion`

## Diff confirmado — array `detalle` (Movimientos) vs. `detalles` (CuentaCorriente)

Mismo shape clave-valor, contenido distinto para la misma operación:

| Nombre en `Movimientos.detalle` | Presente en `CuentaCorriente.detalles` |
|---|---|
| `CuitCuilContraparte` | Sí, igual |
| `NombreContraparte` | Sí, igual |
| `CvuCbuContraparte` | Sí, igual |
| `CoelsaId` | Sí, pero renombrado a `IdTxProcesador` — **confirmado que es el mismo valor exacto** (`"0V1JXON17R6K3QPNZ64EL7"` en ambos) |
| `MotivoRechazo` | **No — ausente, sin equivalente** |
| `EstadoExterno` (`"COMPLETED"`/`"FAILED"`/etc.) | **No — ausente, sin equivalente real** (lo más cercano es `EstadoOperacionId`/`ProcesoCoelsa`, que no es lo mismo) |

`CuentaCorriente.detalles` agrega campos nuevos que `Movimientos.detalle` no tenía: `AliasContraparte`, `CodigoBancoContraparte`, `ComprobanteId`, `EstadoOperacionId`, `IdExterno`, `TipoOperacionCodigo`, `ProcesoCoelsa`.

## `idComprobanteRelacionado` — el problema principal (confirmado por el usuario, no solo por el ejemplo)

El ejemplo de payload real comparado no es un caso de devolución, así que no muestra `idComprobanteRelacionado` en ninguno de los dos endpoints. Sin embargo, el usuario confirmó directamente que este es **el problema principal** que motivó todo este análisis: `GET Movimientos` sí lo traía (a nivel raíz de cada comprobante) y `GET /CuentaCorriente` no. Se toma como dato confirmado por el usuario, no como inferencia a partir de `GET /ComprobantesByFilters` (que también lo documenta, con el mismo nombre, pero es un endpoint distinto usado solo como referencia de que el campo existe en la plataforma).

## Recomendación (orden de prioridad si se decide extender `/CuentaCorriente`)

1. `idComprobanteRelacionado` a nivel raíz de `movimientos[]` — el problema principal reportado por COTO.
2. `MotivoRechazo` dentro de `datosOperacion.detalles[]` — crítico para visibilidad de rechazos.
3. `EstadoExterno` dentro de `datosOperacion.detalles[]` — estado del procesador externo, distinto del estado interno.
4. `importeOperacion` dentro de `datosOperacion` — importe de la operación, distinto del importe del comprobante a nivel raíz.
5. `fechaCreacion` / `fechaActualización` / `comprobanteDevolucionId` en `datosOperacion` — esto es reportar/reproducir un bug contra la documentación existente, no pedir desarrollo nuevo.
