# Guía — Diseño de archivo batch de saldos

> Fuente: https://psp.bind.com.ar/developers/apis/guia-archivobatchwalletsaldos
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Tiene un registro con el saldo por cada cuenta virtual de la organización.

## Flujo — Uso del archivo de saldos

```
Propósito: snapshot de saldo de cierre de CADA cuenta de la organización
           al final del día hábil. Sirve para verificar que los saldos
           en el sistema de la entidad coincidan con los de Bind PSP.

Publicación: 1 día hábil después de la fecha de proceso
  GET /consultar-archivos-wallet?fecha=DDMMAA → listar archivos disponibles
  GET /descargar-archivo/{id} → descargar zip XXXXXXXSALDOCUENTASDDMMAA.zip

Estructura del archivo (posicional, 1015 caracteres por registro):
  HEADER  → 1 registro (código entidad + fechas + nro lote)
  DATOS   → N registros (1 por cuenta: ID + CUIT + datos + saldo corte + CVU)
  TRAILER → 1 registro (cantidad de cuentas + suma total de saldos con signo)

Uso típico:
  Al recibir el archivo del día D:
  Σ saldos del archivo (TRAILER) ≤ saldo de la cuenta recaudadora
  Si hay diferencia → investigar qué cuentas difieren en el detalle
```

## Diseño de header

| ID_Campo | Nombre | Formato | Desde-Hasta | Descripción |
|----------|--------|---------|-------------|-------------|
| 1 | Tipo de Registro | C6 | 01-06 | HEADER |
| 2 | Código entidad | N7 | 07-13 | código de PSP o código de entidad/Código de Organización |
| 3 | Fecha de Negocios | N8 | 14-21 | AAAAMMDD |
| 4 | Fecha proceso | N8 | 22-29 | AAAAMMDD |
| 5 | Nro de Lote | N5 | 30-34 | Número secuencial, comenzando de 00001. Es el mismo para todos los archivos con la misma fecha de proceso. |

## Diseño de detalle

| ID_Campo | Nombre | Formato | Desde-Hasta | Descripción |
|----------|--------|---------|-------------|-------------|
| 1 | ID_Cuenta | N13 | 01-13 | Identificador de la cuenta. |
| 2 | CuitCuit | N15 | 14-28 | |
| 3 | Nombre | AN100 | 29-128 | Nombre de cliente. |
| 4 | Apellido | AN200 | 129-328 | Apellido del cliente. |
| 5 | Razón Social | AN500 | 329-828 | Nombre de Persona Jurídica. |
| 6 | Tipo Persona | N1 | 829-829 | 0 = Persona Humana, 1 = Persona Jurídica |
| 7 | Código de Organización | AN7 | 830-836 | |
| 8 | Correo | AN100 | 837-936 | Correo electrónico del cliente. |
| 9 | Fecha Alta | N8 | 937-944 | Fecha de alta de la cuenta. |
| 10 | Fecha Baja | N6 | 945-950 | Fecha de baja de la cuenta. |
| 11 | BilleteraId | AN7 | 951-957 | |
| 12 | BancoId | AN7 | 958-964 | |
| 13 | Signo Saldo | N1 | 965-965 | 0= "Positivo" 1= "Negativo" |
| 14 | Saldo | N13 | 966-978 | Saldo de cuenta a la hora de corte. |
| 15 | CVU | N22 | 979-1000 | Número de CVU del cliente. |
| 16 | Teléfono | N15 | 1001-1015 | Teléfono del cliente. |

## Diseño del trailer

| ID_Campo | Nombre | Formato | Desde-Hasta | Descripción |
|----------|--------|---------|-------------|-------------|
| 1 | Tipo de Registro | C7 | 01-07 | TRAILER |
| 2 | Cantidad de registros | N8 | 08-15 | Cantidad de cuentas |
| 3 | Signo Saldo | N1 | 16-16 | 0= "Positivo" 1= "Negativo" |
| 4 | Total de Saldo | N18,2 | 17-36 | 18 enteros, 2 decimales. Suma de "Saldo" teniendo en cuenta el signo (+/-). |

## Fechas

- **Fecha de negocio:** Es la fecha en que se registró el saldo.
- **Fecha de proceso:** Es la fecha legal de rendición. Es el próximo día hábil a la fecha de negocio.
- **Fecha de publicación:** Se genera un día después de la fecha de proceso (sólo días hábiles).

## Nomenclatura

El archivo zip tiene el formato: `XXXXXXXSALDOCUENTASDDMMAA.zip`
- `XXXXXXX` = código de PSP o código de entidad/Código de Organización
- `SALDOCUENTAS` = fijo
- `DDMMAA` = fecha de proceso

El archivo de texto dentro del zip tiene el formato: `XXXXXXXSALDOCUENTASDDMMAA.txt`
- `DDMMAA` = fecha de negocio
