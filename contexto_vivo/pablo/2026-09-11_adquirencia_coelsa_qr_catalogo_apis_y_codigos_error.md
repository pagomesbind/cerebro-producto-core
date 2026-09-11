---
id: 2026-09-11_adquirencia_coelsa_qr_catalogo_apis_y_codigos_error
pm: pablo
fecha_captura: 2026-09-11
fuente: "Ingesta manual de documentación pública de Coelsa (VPN habilitada) — https://documentacion.coelsa.com.ar/debin/ secciones 'API COELSA QR', 'API Billetera QR', 'APIs General', 'APIs Comercio Split', 'APIs Billetera', 'Sistema de notificaciones' y 'Código QR'. Consultado 2026-09-11."
producto: adquirencia
tema: Catálogo técnico completo de la API COELSA QR (DebinQR/PCT) — endpoints, códigos de error de la transacción, Notification Push y estructura EMVCo con control de firma
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 201b3e0
---

## Por qué este documento

`adquirencia/mecanica_qr_coelsa.md` ya es excelente y muy completo (Partes 1-5: normativa Transferencia 3.0/3.1, flujo de pago con Coelsa, alta de comercio, Interchange con especificación técnica detallada, parametrización de timeouts). Leyendo la documentación pública completa de Coelsa (sección DEBIN, que es donde vive realmente toda la mensajería de "DEBIN QR"/PCT — el sitio "Comercio" de Coelsa es una API distinta, más chica, solo de ABM), confirmo que el contenido narrativo de las Partes 2 y 4 ya existentes es **consistente y más preciso** que la documentación pública genérica (usa la especificación técnica interna v1.15, con tablas de reparto y ejemplos numéricos que el sitio público no tiene). Este item **no reemplaza nada existente** — agrega como nueva **Parte 6** el catálogo de endpoints y códigos de error de la transacción QR en sí (`QRDebin`, `QRReverso`, `QROperacionFinalizada`), que no estaba cubierto, más la mecánica de reintentos de notificaciones y el detalle de firma digital del QR EMVCo.

## Parte 6 (propuesta) — Catálogo de API COELSA QR / Billetera QR y códigos de error de la transacción

### Esquema del mensaje `QRDebin` (inicio de pago con DEBIN QR)

`POST /apiDebinV1/QR/QRDebin` — lo instruye la billetera para iniciar el pago (recién acá se dispara todo el circuito de Parte 2; la sola lectura del QR no hace nada en Coelsa):

```json
{
  "operacion": {
    "vendedor": { "cuit": "string(11)", "cbu": "string(22) — CVU del comercio", "banco": "000", "sucursal": "0000", "terminal": "string(50) opcional" },
    "comprador": { "cuenta": { "cbu": "string(22)", "alias": "string(20)" }, "cuit": "string(11)" },
    "detalle": {
      "concepto": "CCT (Compra con Transferencia) | PCT (Pago con Transferencia)",
      "id_usuario": 0, "id_comprobante": 0,
      "moneda": "032", "importe": "0.01 a 9999999999999.99",
      "tiempo_expiracion": "minutos, 1 a 10",
      "descripcion": "hasta 100 caracteres — formato sugerido para resumen de billetera: 'COMPRA QR NombreFantasiaComercio'",
      "qr": "string(7089) — datos crudos del QR", "qr_hash": "hash de seguridad opcional",
      "qr_id_trx": "string(99), id de transacción del adquirente — no se puede repetir por PSP, valida idempotencia",
      "id_billetera": "código que identifica a la billetera (debe existir en la base de billeteras registradas)"
    },
    "datos_generador": { "ubicacion": {"lat":0,"lng":0,"precision":0}, "ip_cliente":"", "tipo_dispositivo":"01 PC/02 Celular/03 Tablet", "plataforma":"01 Windows/02 Android/03 Linux/04 MacOS/05 iOS", "imsi":"", "imei":"" }
  }
}
```

Response incluye `debin.id`, `debin.estado` (`INICIADO`/`EN CURSO`/`RECHAZO CLIENTE`/`SIN SALDO`/`ERROR DATOS OPERACION`/`ERROR DATOS VENDEDOR`/`ERROR DATOS COMPRADOR`/`ERROR DEBITO`/`VENCIDO`), `debin.addDt`/`fechaExpiracion`, y `evaluacion.puntaje`/`reglas` (el **mismo score de COELSA PREVENT**, 0-100 — ver item separado sobre Prevent/CPF).

### Catálogo de endpoints — API COELSA QR (expuestos por Coelsa, los invoca Bind)

| Endpoint | Función |
|---|---|
| `POST /apiDebinV1/QR/QRDebin` | Iniciar pago con DEBIN QR (ver schema arriba) |
| `GET /apiDebinV1/QR/QRDebin/{qr_id_trx}/{id_psp}` | Consultar estado — **usar solo tras timeout/falta de aviso**, nunca en el camino síncrono normal (ver recomendación general anti-polling en `wallet/coelsa_debin_api_referencia.md`) |
| `POST /apiDebinV1/QR/QRSolicitudContraCargo` | Iniciar contracargo de una operación QR existente |
| `POST /apiDebinV1/QR/QROperacionOk` | Confirmar que la operación se realizó correctamente, dispara el split de fondos |
| `POST /apiDebinV1/QR/CashOut` / `POST /apiDebinV1/QR/ConfirmaCashOut` | Pedido y confirmación de Cashout (split de fondos hacia CBU externo) |
| `POST /apiDebinV1/QR/SplitQR` | Generar los DEBIN internos de comercio + adquirente para el modelo con split |

### Catálogo — API Billetera QR (los expone Bind/la billetera, los invoca Coelsa)

| Endpoint | Función |
|---|---|
| `POST [endpointADQUIRIENTE]/QRConfirmaDebito` | Confirmación del débito — respuesta inmediata esperada (DEBINQR es recurrente) |
| `POST [endpointBILLETERA]/QROperacionFinalizada` | Aviso de cierre de operación (éxito o reversa) |
| `POST [ep]/AvisoCashOutPendiente` | Aviso de nuevo Cashout pendiente al banco débito |

### Catálogo — APIs de administración (Comercio Split y Billetera)

CRUD idéntico para ambas entidades — habilitar (`POST`), listar (`GET`), eliminar (`DELETE`), modificar (`PUT`), consultar por clave (`GET`):

- **Comercio** (para split): `/apiDebinV1/QR/Comercio` (alta/lista), `/apiDebinV1/QR/Comercio/{CVU}/{CUIT}` (baja/modificación/consulta), `/apiDebinV1/QR/Comercio/{CBU}` y `/{CUIT}` (consultas alternativas).
- **Billetera**: `/apiDebinV1/QR/Billetera` (alta/lista), `/apiDebinV1/QR/Billetera/{id}` (baja/modificación/consulta).
- Usuario de **split** debe tener habilitados como mínimo: `Vendedor/Adhesion`, `Debin/ConfirmaCashout`, `QR/SplitQR`, `QR/CashOut`, `QR/Comercio`.
- Mínimas configuraciones para operar **DEBINQR** (billetera): alta de PSP + cuenta recaudadora + CVU (sistema CVU), alta de billetera (sistema DEBIN), alta de endpoint con campo `cashout`, adhesión como vendedor de la cuenta recaudadora.

### Códigos de error propios de la transacción QR (distintos de los códigos de ABM de Comercio/Actividad ya documentados en Parte 4)

**`POST [epPSP]/QRReverso`** (motivo del reverso informado al Aceptador):

| Código | Descripción |
|---|---|
| 6200 | Reversar operación (timeout) |
| 6201 | Operación expirada |
| 6203 | Error crédito |
| 6204 | Error débito |
| 6205 | Error comunicación con adquiriente |
| 6206 | Falla validación contra adquiriente |
| 6299 | Error general |

**`POST [epBilletera]/QROperacionFinalizada`** (incluye ahora los campos `payment_reference` y el nodo `contracargo` con `IdHash`/`ori_trx_id`/`importe`):

| Código | Descripción |
|---|---|
| 5705 | Devolución total |
| 5708 | Devolución parcial |
| 5709 | Error comunicación con adquiriente |
| 5710 | Adquiriente deniega operación |
| 5711 | Falla validación contra adquiriente |
| 5712 | Reversar operación (timeout) |
| 5713 | Operación expirada |

### Sistema de Notificaciones — Notification Push (créditos forzados)

Cuando un crédito queda "forzado" (ver `wallet/coelsa_debin_api_referencia.md §3`), Coelsa encola el aviso en `NOTIFICATION_PUSH` y reintenta con política **retry cada 15s, multiplicador x2, timeout de 5s por intento**, hasta las 17hs del día de negocio (después, la fuente de verdad pasa a ser el archivo de conciliación). Headers de reintento: `Coelsa-Msg-Type: Aviso`, `Coelsa-Retry-Count: <n>` — permiten a la entidad detectar que un mensaje es un reenvío. Coelsa **no revisa el contenido de la respuesta**, solo el código HTTP — cualquier 2xx cierra el reintento.

### Estructura del Código QR EMVCo — control de firma (detalle no documentado hasta ahora)

Complementa la sección ya existente "Estructura del QR" de la Parte 1 (que cubre el formato TLV general). El control de firma **solo aplica a QR dinámicos** (Bind PSP no los usa hoy, ver Parte 1 — información de referencia si se evaluara soportarlos a futuro):

- `dataToVerify`: string de **220 bytes**, compuesto por la concatenación de `DataObjectID + DataObjectLength + DataObjectValue` de los tags **00, 01, 43, 50, 51, 52, 53, 54, 58, 59, 60, 61, 62, 80** (en ese orden).
- `signedData`: string de **172 bytes**, compuesto solo por los `DataObjectValue` de los tags **81, 82, 83**.
- La presencia de cada objeto de datos puede ser Mandatory/Conditional/Optional — la ausencia de un tag Mandatory/Conditional invalida el QR.

## Confianza

Alta. Ninguno de estos catálogos contradice lo ya documentado; son un nivel de detalle adicional (nombres de endpoint exactos y códigos de error de la transacción) que la documentación narrativa existente no necesitaba para su propósito de negocio, pero que sirve directo para debugging/soporte técnico.
