# Coelsa DEBIN — payloads reales (Anexo técnico)

> Estado: en producción (documentación de referencia). Partido desde [coelsa_debin_api_referencia.md](coelsa_debin_api_referencia.md) por umbral de fisión (>300 líneas) — mismo tema, separado en archivo propio para no mezclar la referencia conceptual con el anexo extenso de ejemplos literales. Fuente: documentación pública de Coelsa (VPN habilitada), https://documentacion.coelsa.com.ar/debin/. Consultada 2026-09-11.
>
> Se preservan tal cual figuran en la fuente (valores de prueba de Coelsa), quitando solo el JWT de ejemplo de los headers `Authorization` (irrelevante, es de testing). Sirven como referencia directa para debugging o para armar un mock de pruebas. Ver [coelsa_debin_api_referencia.md](coelsa_debin_api_referencia.md) para el catálogo de endpoints, autenticación, ambientes y flujos conceptuales.

## API BANCOS (Bind expone, Coelsa invoca para gestión)

**Alta Cuenta Recaudadora Concepto Particular** — `POST /apiDebinV1/Bancos/CuentaEspecial`
```json
{
  "cuenta": { "cbu": "9980025700000000000284", "cuit": "20333048494" },
  "activo": true
}
```

**Aviso de Contracargo a Entidad del Vendedor** — `POST [EP]/AvisoDeContracargo`
```json
{
  "operacionOriginal": {
    "id": "MRD06ZO9WEWKXJX95GP7XY",
    "tipo": "debin",
    "detalle": { "importe": 45.0, "moneda": "80", "motivo": "razon" }
  },
  "id": "123",
  "fechaNegocio": "2019-12-20T19:22:02.204Z",
  "comprador": { "cuit": "30576124275", "cuenta": { "cbu": "1980001730000000568679" } },
  "vendedor": { "cuit": "33711585619", "cuenta": { "cbu": "1980001730000001136251" } }
}
```
Response esperada del banco: HTTP 200 (solo confirma recepción — Coelsa ya movió las garantías, este mensaje es informativo).

**Establecer Estado Online/Offline** — `POST /apiDebinV1/Bancos/ModoBanco`
```json
{ "estado": { "codigo": "ON" } }
```

**Crear Endpoint** — `POST /apiDebinV1/Bancos/PostEndPoint`
```json
{
  "EndPointAlta": {
    "Id": "TEST330",
    "Descripcion": "TESTING330",
    "Primario": "https://testdebin.coelsa.com.ar/apiDebinV1/CoelsaTest/",
    "Secundario": "https://testdebin.coelsa.com.ar/apiDebinV1/CoelsaTest/",
    "Red": "COELSA",
    "Default": false,
    "creditoti": null,
    "contraCargo": null,
    "aviso_cvu": null,
    "tic": null
  }
}
```

**Eliminar Endpoint** — `DELETE /apiDebinV1/Bancos/DeleteEndPoint`
```json
{ "EndPointBaja": { "Id": "CLIENTES PABLO" } }
```

## API COELSA — avisos/webhooks que Coelsa envía y Bind debe responder

**`POST [EPBanco]/AvisoDebinPendiente`** — nuevo DEBIN, aviso al banco del comprador:
```json
{
  "operacion": {
    "comprador": {
      "cuenta": { "banco": "999", "sucursal": "2798", "alias": "|", "cbu": "9992798100000000001003", "esTitular": 0, "moneda": "032", "tipo": "20" },
      "codigo": "", "titular": "PRUEBA PostMan - CoelsaTest 20000000990", "cuit": "20000000990"
    },
    "vendedor": {
      "cuenta": { "banco": "999", "sucursal": "9226", "terminal": "", "alias": "", "cbu": "9999226600000000000031", "esTitular": 0, "moneda": "032", "tipo": "20" },
      "codigo": "", "titular": "PRUEBA PostMan - CoelsaTest 20000000990", "cuit": "20000000990"
    },
    "detalle": {
      "fecha": "2019-12-20T17:58:07.307Z", "fechaExpiracion": "2019-12-20T17:58:07.307Z",
      "concepto": "ALQ", "idUsuario": 0, "idComprobante": 0, "moneda": "032", "importe": 1000.0, "mismoTitular": 0
    }
  },
  "debin": {
    "id": "80V1JXON1733JY1NZ64EL7",
    "estado": { "codigo": "00", "descripcion": "PERSISTIDO" },
    "estadoComprador": { "codigo": "00", "descripcion": "ADHERIDO" }
  },
  "preautorizado": false,
  "evaluacion": { "puntaje": 0, "reglas": "" }
}
```
Response esperada: HTTP 200 — luego el banco debe pedir la autorización al cliente y, una vez obtenida, debitar.

**`POST [EP]/AvisoOperacionFinalizada`** — cierre de operación (éxito o reversa):
```json
{
  "resultado": { "codigo": "string", "descripcion": "string" },
  "operacion": {
    "estado": { "codigo": "string", "descripcion": "string" },
    "ori_trx": "string", "ori_terminal": "string", "ori_adicional": "string", "tipo": "string", "id": "string"
  },
  "comprador": { "cuit": "string", "cbu": "string" },
  "vendedor": { "cuit": "string", "cbu": "string" }
}
```

**`POST [EP]/AvisoAdhesionRecurrencia`**:
```json
{
  "recurrencia": {
    "id": 115,
    "vendedor": { "cuit": "20000000192" },
    "comprador": { "cuit": "27375575847", "cbu": "9982879600000000000338", "estado": "00" },
    "debin": {
      "moneda": "032", "detalle": "prueba", "concepto": "ALQ",
      "prestacion": "PRUEBA PostMan - CoelsaTest", "referencia": "prueba recurrencia"
    }
  }
}
```
Response esperada: HTTP 200.

**`POST [EP]/Credito`** — Coelsa pide acreditar al vendedor (síncrono):
```json
{
  "objeto": { "tipo": "transferencia", "ori_trx_id": 51616187 },
  "credito": {
    "cuit": "20333048494", "banco": "998", "sucursal": "8851",
    "cuenta": { "cbu": "9988851800000000000628" }, "titular": "PAYLINK PRUEBA"
  },
  "debito": {
    "cuit": "20000000141", "banco": "999", "sucursal": "2589",
    "cuenta": { "cbu": "9992589300000000000154" }, "titular": null
  },
  "concepto": "ALQ", "descripcion": null, "idUsuario": 0, "idComprobante": 0,
  "importe": { "moneda": "032", "importe": 7.77 },
  "mismoTitular": 0, "ori_trx": "", "ori_terminal": "", "ori_adicional": "20191001",
  "datosGenerador": {
    "ipCliente": "", "tipoDispositivo": "", "plataforma": "", "imsi": "", "imei": "",
    "ubicacion": { "lat": 0, "lng": 0, "precision": 0 }
  }
}
```
`CreditoCVU` usa exactamente el mismo esquema — se distingue solo por el endpoint (`/CreditoCVU`) que la entidad configuró para operaciones destino-CVU.

**`POST [EP]/Debito`** — Coelsa pide debitar al comprador (síncrono):
```json
{
  "objeto": { "tipo": "DEBIN", "id": "X76V4MR2Z1J5MO8NDEZOL1", "preautorizado": false },
  "credito": { "cuit": "20333048494", "banco": "998", "sucursal": "0000", "cuenta": { "cbu": "9984353300000000000017" } },
  "debito": { "cuit": "27375575847", "banco": "998", "sucursal": "2879", "cuenta": { "cbu": "9982879600000000000338" } },
  "importe": { "moneda": "032", "importe": 500000.0 },
  "fechaHora": "2019-12-20T18:57:38.990Z", "fechaNegocio": "2019-12-20T18:57:38.990Z",
  "ori_trx": "string", "ori_terminal": "string", "ori_adicional": "string",
  "evaluacion": { "puntaje": 0, "reglas": "" }
}
```

**`POST [EP]/AvisoCVU`** — aviso a PSP/banco cuando interviene una CVU:
```json
{
  "operacionCVU": {
    "tipo": "PENDIENTE", "id": "EZ4K6DVNOGM7PE495J8LQ7", "cbu": "9988851800000000000628",
    "fecha_negocio": "2019-12-20T19:15:01.254Z", "moneda": "032", "importe": 7.77,
    "id_psp": 4, "cuit_psp": "20333048494", "cvu": "0000004800000000014461", "cuit_cvu": "20000014452",
    "titular_cvu": "PRUEBA PostMan - CoelsaTest",
    "url_psp": "https://muxiplacetest.firstdata.com.ar:9443/muxigateway/v1/notifications/"
  }
}
```

## API COMPRADOR (Bind invoca sobre Coelsa)

**Adhesión** — `POST /apiDebinV1/Comprador/Adhesion`:
```json
{
  "comprador": {
    "cuenta": { "cbu": "9983560600000000000024" },
    "contacto": { "email": "pabloabecasis@gmail.com" },
    "cuit": "20333048494",
    "endpoint": "localhost"
  }
}
```

**Baja Cuenta** — `POST /apiDebinV1/Comprador/BajaCuenta`:
```json
{ "comprador": { "cuit": "20000000117", "cuenta": { "cbu": "9981595600000000000123" } } }
```

**Adhesión a Recurrencia** — `POST /apiDebinV1/[Comprador|Vendedor]/AdherirRecurrencia`:
```json
{
  "recurrencia": {
    "vendedor": { "cuit": "20000000583" },
    "comprador": { "cuit": "27375575847", "cbu": "9984788700000000000420" },
    "debin": {
      "moneda": "032", "detalle": "pruebarecurrencia", "concepto": "ALQ",
      "prestacion": "PruebasMica", "referencia": "string"
    },
    "id": 127, "activo": true, "tipo_adhesion": 0
  }
}
```

**Solicitud de Contracargo Comprador** — `POST /apiDebinV1/Comprador/SolicitudContraCargo` (síncrono):
```json
{
  "operacionOriginal": {
    "id": "WORD6LEN8QGDRE09M1Y30V", "tipo": "debin",
    "detalle": { "importe": 10560.00, "moneda": "840", "motivo": "inicia" }
  },
  "comprador": { "cuit": "27375575847", "cuenta": { "cbu": "9984788700000000000420" } },
  "vendedor": { "cuit": "20000000583", "cuenta": { "cbu": "9985188000000000000611" } }
}
```
Secuencia completa: banco débito llama `SolicitudContraCargo` → Coelsa responde 200-OK al banco débito y en paralelo llama `POST [EP]/AvisoDeContraCargo` al banco crédito/vendedor → se debita dentro de garantías al banco crédito y se acredita dentro de garantías al banco débito.

## API VENDEDOR (Bind invoca sobre Coelsa)

**Adhesión** — `POST /apiDebinV1/Vendedor/Adhesion`:
```json
{
  "vendedor": {
    "cuit": "20309267789", "sucursal": "8056", "nombre_fantasia": "EmilianoMior",
    "rubro": "VARIOS", "endpoint": "TESTING ALE",
    "cuenta": { "cbu": "9998056600000000000109" },
    "contacto": { "email": "emior@coelsa.com.ar" }
  }
}
```

**Alta de Prestaciones** — `POST /apiDebinV1/Vendedor/Prestacion`:
```json
{
  "vendedor": {
    "cuit": "30000000015",
    "prestaciones": { "nombre": "Prestacion02", "ayuda_referencia": "Prestacion02Referencia01", "min": 0, "max": 0 }
  }
}
```

## Secuencia completa — DEBIN SPOT origen CBU destino CVU (ejemplo de flujo paso a paso)

1. Banco Vendedor: `POST /apiDebinV1/Debin/Debin` (destino = una CVU) → Coelsa valida CVU, PSP y cuenta recaudadora del PSP.
2. Coelsa → PSP Comprador (Billetera): `POST [EPPSP]/AvisoDebinPendienteCVU` (mismo esquema que `AvisoDebinPendiente` de arriba). Plazo de aprobación por el usuario: 1 minuto a 3 días (según `fechaExpiracion`); pasado ese plazo, el DEBIN pasa a `VENCIDO`.
3. Usuario acepta en la Billetera → Billetera: `POST /apiDebinV1/Debin/ConfirmaDebitoCVU`.
4. Coelsa → Banco Comprador: `POST [EPBanco]/AvisoDebinPendiente` (genera un DEBIN Recurrente interno para mover fondos de la CBU origen a la CBU recaudadora de la CVU destino).
5. Banco Comprador responde: `POST /apiDebinV1/Debin/ConfirmaDebito` → Coelsa mueve garantías y llama `POST [EP]/Credito` al Banco Vendedor.
6. Ante error en cualquier paso, se dispara `AvisoOperacionFinalizada` a los actores ya notificados hasta ese punto (vendedor+PSP si falló el paso 2; vendedor+comprador+PSP si falló desde el paso 4 en adelante).

(Los otros 3 circuitos — DEBIN recurrente CBU-CVU, SPOT/recurrente CVU-CBU, SPOT/recurrente CVU-CVU — siguen la misma lógica de pasos, cambiando solo qué actor es CBU vs. CVU en cada punta; documentados con el mismo nivel de detalle en la fuente original si hace falta reconstruirlos.)

---
*Creado: 2026-09-11 — `/context_merge`, desde ingesta manual de documentación pública de Coelsa (Pablo Gomes) — separado de `coelsa_debin_api_referencia.md` por umbral de fisión.*
