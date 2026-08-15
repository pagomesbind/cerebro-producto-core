# Guía — Diseño de archivo batch de movimientos

> Fuente: https://psp.bind.com.ar/developers/apis/guia-archivobatchwalletmovimientos
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Tiene un registro por cada movimiento de saldo de débito/crédito de cada cuenta de la organización.

## Flujo — Ciclo de publicación y uso del archivo

```
Momento del movimiento (día N):
  → Se registra el comprobante en el sistema

Fecha de proceso (próximo día hábil a fecha de negocio):
  → El movimiento tiene una "fecha de proceso" asignada (puede coincidir con día N si es hábil)

Fecha de publicación (día hábil siguiente a fecha de proceso):
  → Bind PSP genera y publica el archivo batch
  → Disponible vía API: GET /consultar-archivos-wallet?fecha=DDMMAA

Descarga y conciliación:
  GET /descargar-archivo/{id}
  → Archivo zip: XXXXMOVIMIENTOSCUENTASDDMMAA.zip
  → Descomprimir → XXXXMOVIMIENTOSCUENTASDDMMAA.txt (posicional, 648 caracteres por registro)
  → Estructura: HEADER + N registros DATOS + TRAILER
  → Usar TRAILER para validar: cantidad de registros + suma neta de importes
```

## Diseño de header

| ID_Campo | Nombre | Formato | Desde-Hasta | Descripción |
|----------|--------|---------|-------------|-------------|
| 1 | Tipo de Registro | C6 | 01-06 | HEADER |
| 2 | Código entidad | N4 | 07-10 | código de PSP o código de entidad |
| 3 | Fecha de Negocios | N8 | 11-18 | AAAAMMDD |
| 4 | Fecha proceso | N8 | 19-26 | AAAAMMDD |
| 5 | Nro de Lote | N5 | 27-31 | Número secuencial, comenzando de 00001. Es el mismo para todos los archivos con la misma fecha de proceso. |

## Diseño de detalle

| ID_Campo | Nombre | Formato | Desde-Hasta | Descripción |
|----------|--------|---------|-------------|-------------|
| 1 | DATOS | AN5 | 01-05 | Fijo DATOS |
| 2 | Código de entidad | N4 | 06-09 | código de PSP o código de entidad |
| 3 | Tipo Comprobante | N5 | 10-14 | Id Tabla "TipoComprobantes" |
| 4 | Número Comprobante | N13 | 15-27 | IdComprobante |
| 5 | Número Operación | N13 | 28-40 | IdOperacion |
| 6 | Número de cuenta | N20 | 41-60 | IdCuenta |
| 7 | Numero de Organización | N5 | 61-65 | IdOrganizacion |
| 8 | Fecha | N8 | 66-73 | AAAAMMDD |
| 9 | Hora | N6 | 74-79 | HHMMSS |
| 10 | Signo del "Tipo Comprobante" | N1 | 80-80 | 0= "Positivo" 1= "Negativo" |
| 11 | Importe | N13,2 | 81-95 | |
| 12 | Moneda | N1 | 96-96 | 0 Pesos, 1 Dólares |
| 13 | Estado Operación | N3 | 97-99 | IdEstado: 001=A Procesar, 002=Aprobada, 003=Rechazada, 004=A Consultar, 005=Auditar |
| 14 | Procesador de Pago | N3 | 100-102 | 001 Saldo virtual, 002 Coelsa |
| 15 | ID Tx Procesador | AN70 | 103-172 | Id interno. ID COELSA, Id Externo de entidad |
| 16 | CUITContraparte | N11 | 173-183 | CUITContraparte o CuitVendedor en el caso de Pago QR |
| 17 | CVUCBUContraparte | N22 | 184-205 | CVUCBUContraparte o VendedorCBUCVU para el caso de Pago QR |
| 18 | ComprobanteRelacionadoId | N13 | 206-218 | |
| 19 | Relleno 1 | N3 | 219-221 | |
| 20 | Relleno 2 | N15 | 222-236 | |
| 21 | Nombre Contraparte | C100 | 237-336 | |
| 22 | Código Banco Contraparte | C4 | 337-340 | Primeras 3 posiciones del campo "CVUCBUContraparte". Si el "Código Banco Contraparte" = '000' extraer posición 4 a 7 de "CVUCBUContraparte". |
| 23 | Alias Contraparte | C100 | 341-440 | |
| 24 | Referencia de comprobante | C200 | 441-640 | |
| 25 | Fecha Externa | N8 | 641-648 | AAAAMMDD |

## Diseño de trailer

| ID_Campo | Nombre | Formato | Desde-Hasta | Descripción |
|----------|--------|---------|-------------|-------------|
| 1 | Tipo de Registro | C7 | 01-07 | TRAILER |
| 2 | Cantidad de registros | N8 | 08-15 | Cantidad de movimientos |
| 3 | Signo | N1 | 16-16 | 0= "Positivo" 1= "Negativo" |
| 4 | Importe | N18,2 | 17-36 | 18 enteros, 2 decimales. Suma teniendo en cuenta el signo (+/-) de cada movimiento. |

## Fechas

- **Fecha de negocio:** Es la fecha en que tuvo lugar el movimiento.
- **Fecha de proceso:** Es la fecha legal de rendición. Es el próximo día hábil a la fecha de negocio (pudiendo ser igual a la fecha de negocio si esta ocurrió en un día hábil).
- **Fecha de publicación:** Es la fecha en que se genera y publica el archivo. Sólo se genera los días hábiles, y se generan un día después de la fecha de proceso. Es decir, que una transacción aparecerá en el archivo que será publicado el próximo día hábil a su fecha de proceso.

## Nomenclatura

El archivo zip tiene el formato: `XXXXMOVIMIENTOSCUENTASDDMMAA.zip`
- `XXXX` = código de PSP o código de entidad
- `MOVIMIENTOSCUENTAS` = fijo
- `DDMMAA` = fecha de proceso

El archivo de texto dentro del zip tiene el formato: `XXXXMOVIMIENTOSCUENTASDDMMAA.txt`
- `DDMMAA` = fecha de negocio
