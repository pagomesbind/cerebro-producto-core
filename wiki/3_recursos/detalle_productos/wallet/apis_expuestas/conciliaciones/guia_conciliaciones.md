# Guía — ¿Qué tener en cuenta para conciliar?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-conciliarwallet
> Producto: Wallet — Consultas y conciliaciones

## Descripción

El sistema pone a disponibilidad distintas herramientas para que la entidad pueda realizar conciliaciones y controles de los movimientos que ocurran en su billetera:

- Para poder hacer un control de absolutamente todos los débitos y créditos de saldo de todas las cuentas se puede consultar el listado de comprobantes.
- Para poder hacer un control de movimientos de procesamiento externo (como transferencias entrantes, pagos qr, etc) se puede consultar el listado de operaciones.
- Para hacer conciliaciones administrativas diarias se disponibiliza todos los días hábiles archivos batch que engloban la operatoria de cada día y se pueden descargar vía API.
- Para controlar la integridad del saldo de la cuenta recaudadora se disponibiliza todos los días hábiles un documento con la cuadratura diaria de los saldos.

Es responsabilidad de la entidad velar porque no haya inconsistencias entre su sistema y el sistema de Bind PSP.

## Flujo — Herramientas de conciliación

```
OPCIÓN 1 — Control de todos los movimientos de saldo (comprobantes):
  GET /comprobantes (filtros: cuenta, fecha, tipo)
  → Devuelve TODOS los débitos y créditos de todas las cuentas
  → Incluye comprobantes internos (impuestos, ajustes) + operaciones externas

OPCIÓN 2 — Control de operaciones de procesamiento externo:
  GET /operaciones (filtros: tipo, fecha, estado)
  → Transferencias entrantes/salientes, pagos QR, DEBIN, etc.
  → Incluye estado de la operación en la red

OPCIÓN 3 — Movimientos de cuenta corriente:
  GET /movimientos-cuenta-corriente (filtros: cuenta, fecha)
  → Vista cronológica de comprobantes de una cuenta específica

OPCIÓN 4 — Archivos batch diarios (conciliación administrativa):
  Proceso automático: cada día hábil Bind PSP genera los archivos
  GET /archivos-wallet (fecha) → lista los archivos disponibles del día
  GET /descargar-archivo/{id} → descarga el archivo (batch movimientos, batch saldos, cuadratura)

  Tipos de archivo:
  - Batch movimientos: todos los débitos/créditos del día (ver guia_archivo_batch_movimientos.md)
  - Batch saldos: saldos de cierre de cada cuenta al fin del día (ver guia_archivo_batch_saldos.md)
  - Cuadratura: integridad diaria de la cuenta recaudadora (ver guia_archivo_cuadratura.md)
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `GET` | Consultar comprobantes | [endpoint_get_consultar_comprobantes.md](endpoint_get_consultar_comprobantes.md) |
| `GET` | Consultar operaciones | [endpoint_get_consultar_operaciones.md](endpoint_get_consultar_operaciones.md) |
| `GET` | Consultar movimientos cuenta corriente | [endpoint_get_consultar_movimientos_cuenta_corriente.md](endpoint_get_consultar_movimientos_cuenta_corriente.md) |
| `GET` | Consultar archivos Wallet | [endpoint_get_consultar_archivos_wallet.md](endpoint_get_consultar_archivos_wallet.md) |
| `GET` | Descargar archivo Wallet | [endpoint_get_descargar_archivo_wallet.md](endpoint_get_descargar_archivo_wallet.md) |

## Guías adicionales

- [Diseño de archivo batch de movimientos](guia_archivo_batch_movimientos.md) — `guia-archivobatchwalletmovimientos`
- [Diseño de archivo batch de saldos](guia_archivo_batch_saldos.md) — `guia-archivobatchwalletsaldos`
- [Diseño de archivo cuadratura](guia_archivo_cuadratura.md) — `guia-archivowalletcuadratura`
