# Crear Comercio para QR con Acreditación en Wallet

> Estado: en producción. Reubicado desde `detalle_productos/wallet/otros_manuales.md §5-6` en la reestructuración PARA en cascada (2026-08-12). Producto(s) de esta fuente: WALLET, ADQUIRENCIA — el comercio se crea en Adquirencia pero acredita directo en una cuenta Wallet.

## 1. Precondiciones y configuración (interno)

**Objetivo:** crear un comercio que pueda cobrar con QR con acreditación online en wallet.

La entidad donde se crearán los comercios debe tener las siguientes especificaciones (endpoint "Crear una especificación" del swagger de comercios):

| EspecificacionTipoId | Valor | Qué significa |
|---|---|---|
| 2281 | {{OrganizacionId}} | Asocia la entidad de cobro a la organización de wallet. |
| 2350 | 12 | Que al dar de alta un comercio admite setear el CVU externo indicado al crearlo (incluye admitir comercios con CUIT duplicados). |
| 2061 | 11 | Que al habilitar QR en un comercio, sabe que no debe crear el CVU y debe sacarlo del CBU. |
| 3487 | 1 | Indica que por cada cobro QR debe avisar a wallet creando los comprobantes. |

- Debe crearse cada cuenta+CVU en wallet antes de crear el comercio (dato requerido en la creación).
- La cuenta recaudadora asociada a la organización de wallet debe estar adherida como vendedora en Coelsa (endpoint API BANK: `Debin-Alta_BajaCuentaVende`).
- Es recomendable que la entidad tenga configurado el canal por defecto QR, **sin split**.
- ⚠️ **El CVU indicado (`WALLET_CVU`/`Cbu`/`Cvu`) debe pertenecer a la misma titularidad (CUIT) que el CUIT del comercio.** Si no coincide, Coelsa rechaza el pago con `CVU VENDEDOR NO HABILITADO` (código `7154`) aunque la cuenta recaudadora ya esté adherida y el comercio figure habilitado del lado de Bind — caso real confirmado en [detalle_productos/adquirencia/mecanica_qr_coelsa.md](../adquirencia/index.md#mecanica_qr_coelsamd).

**Configuración:** crear comercio por API `POST {{BASE_URL}}/bindentidad-comercio-v2/v2/api/v1.201/comercios`, con `datosWallet.WALLET_CUENTA` (id de la cuenta wallet), `datosWallet.WALLET_ORGANIZACION` (id de la organización wallet), `datosWallet.WALLET_CVU` (CVU asociado), y `Cbu`/`Cvu` a nivel raíz con el mismo CVU.

## 2. Endpoint de alta de comercio (cliente-facing)

**Objetivo:** explicar cómo utilizar el endpoint de alta de comercio para el caso en que el comercio usará QR y acreditará estos cobros en línea en una cuenta del producto Wallet de Bind PSP.

**Flujo funcional:**
1. Crear cuenta en wallet para el comercio.
2. Crear CVU en wallet para el comercio.
3. Crear el comercio utilizando los valores creados en 1 y 2.

**Endpoint** (credenciales de API del producto **COBRO**):

| Ambiente | Método | URL |
|---|---|---|
| STAGING | POST | `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios` |
| PRODUCCIÓN | POST | `https://api.bindpagos.com.ar/bindentidad-comercio-v2/v2/api/v1.201/comercios` |

**Request body — atributos principales:**

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `nombre` | string | REQUERIDO | Razón social del comercio. |
| `calle`, `piso`, `departamento` | string | REQ/OPC | Domicilio del comercio. |
| `codigoPostal`, `codigoLocalidad` | int | REQUERIDO | Ids de provincia/localidad (ver docs públicas). |
| `email` | string | REQUERIDO | Correo del administrador del comercio; no puede repetirse entre comercios. |
| `telefono`, `telefonoSecundario` | string | REQ/OPC | Teléfono(s). |
| `cuit` | string | REQUERIDO | CUIT del comercio. |
| `Cbu` / `Cvu` | string | REQUERIDO | CVU creado en Wallet a asociar (donde se acreditan los cobros). |
| `descripcion` | string | OPCIONAL | Nombre de fantasía; por defecto la razón social. |
| `mcc` | string | REQUERIDO | Código de rubro MCC de VISA. |
| `actividadEconomicaAfip` | string | REQUERIDO | Código de actividad económica AFIP. |
| `categoriaIva` | string | REQUERIDO | RI/CF/INR/RS/EX/PCE/RSS/PCS/EXE/SNC. |
| `rubroRg461419` | string | REQUERIDO | 1=Supermercado … 8=Otros. |
| `tipoCuenta` | string | REQUERIDO | Código de tipo de cuenta RG4614/19 (1-13). |
| `condicionibb` | string | REQUERIDO | 1=Régimen general … 8=No liquida excluído. |
| `sicore` | string | REQUERIDO | Código de jurisdicción Sicore. |
| `tipoPersona` | string | REQUERIDO | "F" (física) / "J" (jurídica). |
| `conSplit` | boolean | REQUERIDO | Valor fijo = false. |
| `sucursal` (objeto) | object | REQUERIDO | Datos de la sucursal + `caja` (`nombre`, `soloOrden` fijo false, `tipoCajaId` fijo 2). |
| `datosWallet` | object | REQUERIDO | `WALLET_CUENTA`, `WALLET_CVU`, `WALLET_ORGANIZACION`. |

Ejemplo de request body:
```json
{
    "nombre": "Razón social del comercio", "calle": "Maipu 1210", "piso": "11",
    "codigoPostal": "1006", "codigoProvincia": 13, "codigoLocalidad": 1355,
    "email": "email@email.com", "telefono": "1234567890", "cuit": "30261234545",
    "Cbu": "0000532609760006498832", "Cvu": "0000532609760006498832",
    "descripcion": "Nombre de fantasía del comercio", "mcc": "5734",
    "actividadEconomicaAfip": "620100", "categoriaIva": "RI", "rubroRg461419": "7",
    "tipoCuenta": "14", "condicionibb": "4", "sicore": "7", "tipoPersona": "F",
    "conSplit": false,
    "sucursal": [{
        "calle": "Maipu 1210", "piso": "11", "nombre": "Nombre de la sucursal",
        "codigoProvincia": 13, "codigoLocalidad": 1355, "email": "email@email.com",
        "telefono": "1234567890", "codigoPostal": "1006",
        "caja": [{ "nombre": "Nombre de la caja", "soloOrden": false, "tipoCajaId": 2 }]
    }],
    "datosWallet": { "WALLET_CUENTA": "1234", "WALLET_CVU": "0000532609760006498832", "WALLET_ORGANIZACION": "32" }
}
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `id` | string | Código del comercio creado. |
| `codigoSucursal` | string | Código de la sucursal creada. |
| `codigoCaja` | string | Código de la caja creada. |

Ejemplo — HTTP 200: `{"id": "C02381", "codigoSucursal": "S04615", "codigoCaja": "B00000330015"}`

## Ver también
- [cuentas_menores_y_eco_cerrado.md](cuentas_menores_y_eco_cerrado.md) — guía técnica de configuración de entidades para el circuito hermano de Eco Cerrado.
- [detalle_productos/adquirencia/mecanica_qr_coelsa.md](../adquirencia/index.md) — troubleshooting real del error `CVU VENDEDOR NO HABILITADO`.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/wallet/otros_manuales.md §5-6` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
