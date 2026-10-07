---
id: 2026-10-07_adquirencia_conocimiento_request_compra_a_prisma_fintexa
pm: pablo
fecha_captura: 2026-10-07
fuente: "ingesta de raw/ — Excel 'PRISMA-CAMPOS-cliente-20261007' (2 hojas: 'Campos Prisma' = respuesta, 'Request a Prisma' = solicitud de compra), armado por Fintexa a partir del código de CardOrchestrator, ambiente producción, fechado 2026-10-07; entregado por el PM"
producto: adquirencia
tema: qué campos envía Fintexa a Prisma en la solicitud de compra del POS (de dónde sale cada valor y qué valor manda), y hallazgos al contrastarla con el manual ISO 8583 de Prisma
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/integracion_prisma_conexion_directa.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

> **Alcance y límites.** La hoja "Request a Prisma" sale del código de `CardOrchestrator` (Fintexa), no de una especificación de Prisma. La hoja "Campos Prisma" (la respuesta) es la misma tabla ya capturada en `2026-10-07_adquirencia_conocimiento_mapeo_respuesta_prisma_a_transaccion`; el Excel aclara además que las filas marcadas "(ISO 8583)" son "el significado habitual del campo en mensajería de tarjetas, pendiente de confirmar con la documentación de Prisma/Zpay" — no están validadas por Prisma. Los hallazgos del §2 son análisis del Cerebro contrastando el Excel con el manual ISO 8583 de Prisma (ya en canon) y con las pruebas en vivo de PRD-70; **ninguno está confirmado con Fintexa ni con Payway**.

## 1. La solicitud de compra que Fintexa manda a Prisma

Origen del dato: **POS** = lo informa la terminal en el pago · **Fintexa** = lo genera o calcula Fintexa · **Configuración** = sale de la configuración del comercio y del adquirente · **Fijo** = constante, igual para todos los pagos · **Vacío** = se envía sin valor.

**Raíz**

| Campo | Origen | Qué se manda |
|---|---|---|
| `accountType` | Fijo | `"1"` |
| `acquiringInstitutionContryCode` | Fijo | `"032"` (Argentina) |
| `transactionType` | Fijo | `"SOLICITUD_COMPRA"` |
| `functionCode` | Fintexa | `"112"` si la marca es VISA, `"119"` para cualquier otra |
| `inputModeData` | POS | Modo de lectura: manual, banda, chip o contactless |
| `fallbackIndicator` | Fijo | `"N"` |
| `pointOfServiceConditionCode` | Fijo | `"00"` |
| `terminalCapability` | Fijo | `"1"` |
| `networkInternationalIdentifier` | Vacío | Vacío |

**`cardData` y `cardData.securityData`**

| Campo | Origen | Qué se manda |
|---|---|---|
| `panNumber` | POS | Número de tarjeta |
| `cardExpirationDate` | POS | Vencimiento |
| `cardSequenceNumber` | POS | Secuencia de la tarjeta; vacío si viene `"0"` |
| `track2Data` | POS | Track 2 |
| `iccData` | POS | Datos EMV del chip |
| `cardholderData.cardholderName` | POS | Nombre del titular |
| `brand` | Fijo | `"Unknown"` |
| `securityData.pinblockData` | POS | PIN cifrado |
| `securityData.ksnData` | POS | KSN del cifrado del PIN |
| `securityData.cardholderVerificationMethod` | Vacío | Vacío |

**`controlData`, `financialData`, `installmentData`**

| Campo | Origen | Qué se manda |
|---|---|---|
| `controlData.ticket` | Fintexa | Número de ticket generado por Fintexa |
| `controlData.trace` | Fintexa | Número de trace generado por Fintexa |
| `controlData.dateTimeLocalTransaction` | Fintexa | Fecha y hora de la operación generada por Fintexa, **enviada en UTC** |
| `controlData.dateTimeTransmission` | Fintexa | La misma fecha y hora que `dateTimeLocalTransaction` |
| `controlData.stan` | Vacío | Vacío |
| `controlData.referenceNumber` | Vacío | No se completa |
| `financialData.amountTransaction` | POS | Importe total de la operación, como texto |
| `financialData.transactionCurrencyCode` | POS | Código de moneda, completado a 3 dígitos |
| `installmentData.number` | POS | Cantidad de cuotas, a 2 dígitos (`"01"` si no viene) |
| `installmentData.code` | Fijo | `"0"` |

**`merchantData` (comercio) y `merchantData.subMerchantData` (subcomercio)**

| Campo | Origen | Qué se manda |
|---|---|---|
| `merchantData.merchantId` | Configuración | Número de establecimiento en Prisma **según la marca** |
| `merchantData.merchantCategoryCode` | Configuración | MCC (rubro) del comercio |
| `merchantData.name` | POS | Nombre corto del comercio, sin el prefijo `BIN*` |
| `merchantData.postalCode` | POS | Código postal del comercio |
| `merchantData.streetAddress` | POS | Dirección del comercio |
| `merchantData.identificationMerchant` | Fijo | `"00000009000"` |
| `merchantData.typeIdentificationMerchant` | Fijo | `"2"` (según el código, 2 = DNI) |
| `subMerchantData.identificationSubMerchant` | Configuración | Código de comercio del subcomercio |
| `subMerchantData.merchantId` | Configuración | Id del adquirente |
| `subMerchantData.merchantCategoryCode` | Configuración | MCC (rubro) del comercio |
| `subMerchantData.name` | POS | Nombre corto del comercio |
| `subMerchantData.streetAddress` | POS | Dirección del comercio |
| `subMerchantData.submerchantCity` | Fijo | `"B"` |
| `subMerchantData.submerchantCityCode` | Fijo | `"ARG"` |
| `subMerchantData.submerchantCountrySubdivision` | Fijo | `"ARB"` |
| `subMerchantData.gobermentSubmerchantCountryCode` | Fijo | `"000"` |
| `subMerchantData.typeIdentificationSubMerchant` | Fijo | `"0"` (según el código, 0 = CUIT) |
| `subMerchantData.phoneCSSubmerchant` | Vacío | Vacío |
| `subMerchantData.urlSubmerchant` | Vacío | Vacío |

**`terminalData`**

| Campo | Origen | Qué se manda |
|---|---|---|
| `terminalData.id` | Configuración | Id de la terminal en Prisma |
| `terminalData.appVersion` | POS | `"VERSION_SOFT {versión}"`, tomada del protocolo del POS |

Lectura del modelo: Bind PSP opera como **agregador** — manda un bloque de comercio fijo y un bloque de **subcomercio** con los datos de cada comercio real (el manual de Prisma lo prevé en su sección 2.11, "Agregador / Softdescriptor").

## 2. Hallazgos al contrastar con el manual ISO 8583 y las pruebas en vivo

1. **Fecha/hora enviada en UTC, pero Prisma la define en GMT-3 — probable origen del desfase horario ya reportado a QA.**
   - Fintexa envía `dateTimeLocalTransaction` y `dateTimeTransmission` en UTC. El manual de Prisma indica que el campo de fecha y hora de transmisión (ISO 7) va "HHMMSS (GMT-3)" y que los campos de hora y fecha *locales* (ISO 12 y 13) deben coincidir con él.
   - La respuesta devuelve `TransmisionDate`, que Bind guarda como `FechaLocalNegocio`/`HoraLocalNegocio`/`FechaPago` (ver item hermano). Si Prisma devuelve lo que recibió (no verificado), la hora local de negocio queda en UTC.
   - Consistente con lo visto en las pruebas del 2026-09-23: el POS marcó 11:29 y la grilla de Transacciones mostró 14:27 para los primeros cobros rechazados de la misma tanda, +3 horas.
   - **Impacto más allá de la visualización:** un cobro hecho después de las 21:00 (hora Argentina) queda con la fecha de negocio del **día siguiente** en UTC, lo que puede correr `FechaPago` y descuadrar la conciliación contra la liquidación de Payway. A confirmar con Fintexa.
2. **`functionCode`: `112` si es VISA, `119` para cualquier otra marca.** El manual solo documenta el identificador de red (NII) de VISA (`112`) y MASTERCARD (`119`) en producción. Para Cabal, Amex, Discover y Union Pay se manda `119`, el de MasterCard: a validar con Payway si eso es correcto o si esas marcas necesitan otro valor — relevante para la prueba con un rubro de cobertura completa.
3. **`merchantId` según la marca.** Confirma que el establecimiento de Prisma es **uno por marca** (coherente con la tabla `CardBusinessRulesDB`). Refuerza guardar el establecimiento usado en cada cobro: dos cobros del mismo comercio con marcas distintas viajan con establecimientos distintos.
4. **Ticket y trace los genera Fintexa** (manual: los genera el sistema propio). El Excel confirma que se envían; no dice dónde se persisten del lado Bind. Pendiente de confirmar, pues el ticket es obligatorio para una devolución.
5. **`installmentData.code` fijo en `"0"`.** El manual define "plan" (0..9) y cantidad de cuotas en ISO 48; al estar el plan siempre en `0` hoy no hay forma de operar planes de cuotas especiales. Hipótesis a validar con Payway/Comercial, no verificada.
6. **Identificación del subcomercio.** `typeIdentificationSubMerchant` es `"0"` (CUIT según el código), pero `identificationSubMerchant` toma el **código de comercio** de Bind desde la configuración, no un CUIT. Y la identificación del comercio (`"00000009000"`, tipo `"2"` = DNI) es una constante igual para todos los pagos. Preguntar a Payway si esos valores son los que esperan para un agregador.
7. **Ciudad y provincia fijas.** `submerchantCity` = `"B"` y `submerchantCountrySubdivision` = `"ARB"` van iguales para todos los subcomercios, sin importar dónde estén realmente.
8. **El importe es el "total de la operación" informado por el POS**, como texto. Sigue sin saberse si, con cuotas, ese total incluye el financiamiento que mostraba la pantalla del POS (p. ej. $100,00 en 1 pago vs. $122,40 en 3 cuotas); ver tarea T-192.
9. **Posible explicación de los rechazos "05" del comercio de prueba `C20311` (MCC 6051).** Según mi conocimiento, el MCC 6051 es la categoría de *quasi-cash* (divisas, giros, cheques de viajero, entre otros), que muchos emisores restringen o rechazan de forma genérica. Los 7 cobros con MasterCard sobre ese rubro fueron rechazados con `05` ("Denegada", genérico según la tabla de Prisma). Hipótesis, sin verificar: el rechazo podría venir del rubro y no de mala carga de datos en Payway. La prueba que el PM está armando con un rubro de cobertura completa la confirma o la descarta.
