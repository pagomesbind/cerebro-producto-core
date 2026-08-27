---
id: 2026-08-25_gap-doc-vs-real-cuentacorriente-datosoperacion
pm: nicolas
fecha_captura: 2026-08-25
fuente: "Comparación entre la documentación pública de GET /CuentaCorriente (https://psp.bind.com.ar/developers/apis/consultarmovimientoscuentacorriente) y un payload real aportado por el usuario para el ComprobanteId 14648633 (2026-08-25)"
producto: wallet
tema: La documentación pública de /CuentaCorriente promete campos en datosOperacion que el payload real no devuelve
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/wallet/apis_expuestas/conciliaciones/endpoint_get_consultar_movimientos_cuenta_corriente.md (y la página pública equivalente), que documentan fechaCreacion, fechaActualización y comprobanteDevolucionId como campos de datosOperacion"
confianza: alta
estado: ingestado
---

## Descripción de la contradicción

La documentación pública del endpoint `GET /CuentaCorriente` (`walletentidad-operaciones/v1/api/v1.201/CuentaCorriente`), tanto en el portal (`https://psp.bind.com.ar/developers/apis/consultarmovimientoscuentacorriente`) como en su espejo en la wiki (`endpoint_get_consultar_movimientos_cuenta_corriente.md`), documenta los siguientes campos como parte de `movimientos[].datosOperacion`:

- `fechaCreacion`
- `fechaActualización`
- `comprobanteDevolucionId`

Sin embargo, un payload real de este endpoint (aportado por el usuario, para `ComprobanteId` 14648633, fecha `2026-08-18`) **no incluye ninguno de los tres campos** dentro de `datosOperacion`. Se contrastó contra el payload real del endpoint legacy `GET Movimientos` para la misma operación, donde `FechaCreacion` y `FechaActualizacion` sí tenían valores reales no nulos (`2026-08-18T20:28:32.2107147+00:00`) y `comprobanteDevolucionId` era explícitamente `null` (pero la key sí estaba presente). En `CuentaCorriente`, las tres keys no aparecen en absoluto — ni con valor, ni como `null`.

Esto descarta la hipótesis de "campo omitido por ser null": `fechaCreacion`/`fechaActualización` tenían valores reales conocidos y aun así no se devolvieron.

## Por qué importa

Si un cliente (como COTO) migra a `/CuentaCorriente` confiando en la documentación pública, va a esperar recibir `fechaCreacion`, `fechaActualización` y `comprobanteDevolucionId` en `datosOperacion` y no los va a recibir — un gap de integración que no está señalizado en ningún lado hoy.

## No resuelto — pendiente de decidir con el usuario/equipo técnico

- ¿Es un bug de la implementación real de `/CuentaCorriente` (no está seteando esos campos aunque el contrato lo prometa), o la documentación pública quedó desactualizada respecto a un cambio deliberado de contrato?
- Si es un bug, ¿se corrige agregando los campos al response real, o se actualiza la documentación pública para reflejar que no vienen?
