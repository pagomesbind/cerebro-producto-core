# Mecánica Interna QR/Coelsa — Normativa, Flujo de Pago, Alta de Comercio e Interchange

> Estado: en producción.

> ⚠️ **Infraestructura compartida con Wallet.** Todo lo documentado en este archivo (normativa Transferencia 3.0/3.1, IEP/API Resolve, flujo de mensajería con Coelsa, alta de comercio, interchange/comisiones) es la mecánica técnica que sustenta tanto el **cobro con QR de Adquirencia** (este documento) como el **pago con QR de Wallet** — Bind PSP participa del mismo ecosistema interoperable en ambos roles: como **aceptador** (cuando un comercio de Adquirencia cobra) y como **billetera/emisor** (cuando un usuario de Wallet paga el QR de otro aceptador). Un agente en paralelo puebla la porción equivalente en `wiki/3_recursos/detalle_productos/wallet/` — no duplicar, este es el detalle de referencia para el rol de Adquirencia/Aceptador.
>
> Fuente original: `wiki/3_recursos/mecanica_interna_productos/` (qr_interoperable_transferencia3.md, flujo_pago_qr_coelsa.md, alta_comercio_qr_coelsa.md, interchange_comisiones_qr.md). Ver también [wiki/0_direccion/producto/adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md) para el overview funcional/de negocio.

---

## Parte 1 — Normativa Transferencia 3.0/3.1 y QR Interoperable

> ⚠️ **Corrección de nomenclatura (2026-07-02):** la sesión de capacitación original nombraba a la norma como "Simpra", que resultó ser una mala transcripción/mishearing de **CIMPRA** — la **Comisión Interbancaria para los Medios de Pago de la República Argentina**, el organismo real detrás de esta normativa. El boletín específico que define el mecanismo de resolución de QR es el **Boletín CIMPRA 525**, no "Simpra 530/525" como se dudaba en la sesión original.

### Qué es Transferencia 3.0 / 3.1

- **Transferencia 3.0** es el programa normativo aprobado por el Directorio del BCRA mediante la **Comunicación SINAP "A" 7153**, vigente desde el **7 de diciembre de 2020**, con el objetivo de impulsar los pagos digitales y la inclusión financiera, expandiendo el alcance de las transferencias inmediatas hacia un ecosistema de pagos abierto, universal e interoperable.
- Es lo que ocurre técnicamente detrás de un pago con QR: una **transferencia** de billetera (o CBU/CVU a CBU/CVU) instruida mediante el escaneo de un QR. Por eso también se lo conoce como **PCT (Pago con Transferencia)**.
- La **Comunicación "A" 7175** (que derogó la 7153) fijó los textos ordenados de "Sistema Nacional de Pagos — Transferencias", implementados en 2 fases (1-7 diciembre 2020, y hasta el 29 de noviembre de 2021 para el resto).
- La **Comunicación "A" 7462** (2022) estableció normas sobre Proveedores de Servicios de Pago (PSP), la definición de billetera digital y creó el **Registro de billeteras digitales interoperables**.
- La **Comunicación "A" 7463** (2022) estableció medidas para mitigar, prevenir y gestionar el fraude — de esta comunicación surge la evolución hacia **Transferencia 3.1**, que hace **síncrono** el mensaje de confirmación de débito al aceptador (antes era asíncrono) para eliminar falsos positivos donde la billetera consultaba el estado antes de que el aceptador confirmara realmente el cobro. Ver el flujo completo en la Parte 2.
- Antes de esta norma, los QR **no eran interoperables**: cada billetera (Mercado Pago, etc.) solo podía leer y pagar su propio QR. El BCRA convocó durante más de un año a representantes de todo el ecosistema (con consultoras como PwC facilitando el proceso técnico) para acordar el estándar único.
- Quedó documentada bajo boletines de la **CIMPRA** — el **Boletín CIMPRA 525** específicamente define "Transferencias 3.0 / Interfaz Estandarizada de Pagos, versión de transición" y quedará vigente hasta que sea reemplazado por otro boletín CIMPRA.

### QR estático vs QR dinámico

| Tipo | Definición | ¿Lo usa Bind PSP? |
|---|---|---|
| **Estático** | Siempre el mismo QR, puede usarse muchas veces, está asociado a algo fijo (una caja/punto de venta). Puede tener o no una orden de venta asociada (monto abierto o monto cerrado). | **Sí** — todos los QR de Bind PSP son estáticos. |
| **Dinámico** | Los datos del pago (monto, vencimiento) viajan dentro del propio QR (según el Boletín CIMPRA 525: "el 100% de los datos necesarios para invocar una transferencia inmediata"). Se paga una sola vez; cualquiera que lo lea lo puede pagar mientras no esté vencido, sin necesidad de consultar a un sistema externo. | **No** — Bind PSP no tiene QR dinámicos. |

- El QR estático **no necesita persistir nada nuevo al generarse**: es un string armado de forma estándar con datos ya existentes (nombre de comercio, CUIT, ID de caja, etc.). Se pueden generar infinitos strings de QR sin que eso implique creación de registros — la validez real se determina al momento de la consulta/pago.
- ⚠️ **Riesgo operativo:** si se modifican ciertos datos del comercio o la caja asociados a un QR estático ya emitido (nombre, CUIT, código postal), el QR **deja de ser válido tal cual estaba impreso** — el sistema detecta una discrepancia entre lo codificado en el QR y los datos actuales, y lo rechaza. Esto afecta directamente a comercios que ya tenían el QR impreso en cartelería o facturas.

### Estructura del QR (estándar EMVCo Merchant Presented Code)

Según el Boletín CIMPRA 525, sección 2.1 "Consulta a través de códigos QR estáticos":

1. Ante la lectura de un código QR, la billetera envía el contenido completo del stream a su backend para ser procesado.
2. El backend de la billetera **analiza el QR bajo el estándar EMVCo Merchant Presented Code**, y determina el adquirente buscando en qué campo de **Merchant Account Information (identificadores 26 a 49)** está contenido — las demás posiciones ya están reservadas por el propio estándar EMVCo o por resolución del BCRA.
3. Cada template de Merchant Account Information contiene, bajo el **sub-id `00`**, un identificador universalmente único: el **dominio invertido**.
4. El backend de la billetera usa el dominio invertido como **clave de entrada a la tabla de resolución de URL** (ver más abajo).
5. El usuario confirma el pago desde su billetera, y la transferencia a CVU/CBU se dispara contra el banco, usando la leyenda **"PCT QR" + contenido del campo 59** (o el `collector/name` de la API del adquirente) en la descripción/detalle de la operación.
6. **Si no se encuentra un adquirente en los identificadores 26 a 49**, se asume que es un **QR dinámico** con el 100% de los datos necesarios para la transferencia — el control de vinculación entre emisor y aceptador se hace en el momento de generación de la transacción, por interpretación del código de PSP del aceptador.

#### Ejemplo real de QR (Anexo I del Boletín CIMPRA 525)

```
00020101021141390016com.adquirente0115info_adquirente50130009123456789520497005303032580 2AR5909FULL NAME6010CITY LEGAL63045BE9
```

Desglose posicional (formato TLV — Tag/Length/Value):

| Tag | Longitud | Valor | Significado |
|---|---|---|---|
| 00 | 02 | 01 | Payload Format Indicator |
| 01 | 02 | 11 | Point of Initiation Method |
| **41** | 39 | `00 16 com.adquirente` + `01 15 info_adquirente` | **Merchant Account Information** — sub-tag `00` = dominio invertido (`com.adquirente`), sub-tag `01` = info adicional del adquirente |
| 50 | 13 | `00 09 123456789` | Merchant Category Code / datos adicionales |
| 52 | 04 | 9700 | Merchant Category Code (MCC) |
| 53 | 03 | 032 | Código de moneda (ARS) |
| 58 | 02 | AR | Country Code |
| 59 | 09 | FULL NAME | Nombre del comercio |
| 60 | 10 | CITY LEGAL | Ciudad |
| 63 | 04 | 6725 | CRC (checksum) |

### Dominio inverso y tabla de resolución de URL

- El **dominio invertido** (ej. `com.bin`, `ar.com.modo`, `ar.com.mercadopago`) es la pieza clave que le permite a cualquier billetera saber **a quién preguntarle** si el QR se puede pagar.
- Cada billetera mantiene internamente una **"tabla de resolución URL"**: dominio invertido (clave) → URL completa del adquirente para resolución de datos (resultado). Formalmente definida en el Boletín CIMPRA 525:

  | Campo | Tipo de dato | Descripción |
  |---|---|---|
  | `id` | String(99) | Campo 26-49 del QR, sub-id 00 (el dominio invertido) |
  | `url` | String(1024) | URL completa del adquirente |
  | `sec_xx` | A definir | Datos de seguridad |

- **Esta tabla debe refrescarse con una frecuencia mínima de una vez al día**, consultando a la API que cada administrador disponibiliza para tal fin. Los administradores pueden proveer un sistema de suscripción para avisar de novedades en URLs/adquirentes.
- Bind PSP usa el mismo dominio invertido (`com.bind`) tanto para el histórico PSP 164 (**CUIT 30685029959**, a nombre de Banco Industrial) como para el PSP 184 (**CUIT 30717449076**, licencia propia) — Coelsa reportó esto como una anomalía ("¿cómo tienen dos PSP con el mismo dominio inverso?"), pero la explicación es intencional: Bind PSP expone **una sola IEP** para ambos PSP, por lo que da igual desde qué PSP se emitió el QR — la consulta llega al mismo lugar y responde lo mismo.
- ⚠️ **Incidente real derivado de este diseño (ticket Coelsa #458653, reportado desde mayo 2026, resuelto/explicado el 2026-07-13) — causa raíz confirmada del lado de un tercero, no de Bind PSP.** Billeteras que procesan sus PCT a través de **NewPay** (proveedor tecnológico detrás de la billetera PVS, entre otras) sufrían rechazos sistemáticos (`INTEROPERABLE_VALIDATIONS_ERROR`, `ADQUIRIENTE_NO_VINCULADO`, y a nivel Coelsa el código `7901 – ERROR DATOS PAYMENT VALIDATIONS FAIL`) en QRs de comercios de Bind Pago, con tasas de rechazo puntuales de hasta 92%. **Mecanismo confirmado:**
  1. El **CUIT del aceptador no es un dato devuelto por la IEP/API Resolve** — no es parte del contrato estándar de la IEP (confirmado por Fintexa/Agustín Grau en el ticket: "no devolvemos ese dato porque no es estándar IEP"). Cada administrador/procesador del ecosistema tiene que resolverlo por su cuenta.
  2. Coelsa identifica a un aceptador por la combinación **CUIT + `reverse_domain`**, dato que en este flujo se lo hace llegar **NewPay** vía su propio endpoint (`payments/validations`), no Bind.
  3. Como PVS/NewPay identifican unívocamente a los aceptadores **solo por el dominio inverso** (no consultan el CVU/código de PSP real devuelto por la IEP en cada transacción puntual), y Bind PSP tiene un único dominio inverso (`com.bind`) mapeado a **dos** CUIT distintos (164 y 184), el sistema de NewPay tenía **hardcodeado un único CUIT (el de PSP 164, `30685029959`)** para todas las operaciones contra `com.bind` — incluidas las que en realidad correspondían a un comercio dado de alta bajo PSP 184. Coelsa comparó ese CUIT enviado por NewPay contra el CVU real del comercio (que resolvía a 184) y rechazó la inconsistencia con `7901`.
  - **No es un bug de Bind PSP**: los datos que expone la IEP de Bind son consistentes y correctos para ambos PSP; el problema es que ningún estándar obliga a devolver el CUIT del aceptador, y NewPay optó por una tabla de mapeo estática (dominio→CUIT) en vez de derivar el PSP dinámicamente por transacción — algo que solo se manifiesta como error para billeteras que procesan vía NewPay (otras billeteras que sí resuelven correctamente, como MODO, nunca mostraron el problema).
  - **Resolución:** queda del lado de NewPay corregir su mapeo (dejar de asumir un único CUIT por dominio inverso). Ver hilo completo del ticket #458653 (Gmail, asunto "Re: Nueva respuesta en tu ticket #458653 - Rechazos sistemáticos en pagos QR — Aceptador BIND", 2026-07-13) para la traza completa de la investigación conjunta Bind/Fintexa/Coelsa/NewPay/PVS. Gap cerrado en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).
  - **Seguimiento (2026-08-06):** PVS (Andrés Musicco) repreguntó sobre el ticket, ya cerrado por Coelsa como encuesta de satisfacción automática, con 2 pedidos pendientes de respuesta de Bind PSP: (1) si se avanzó con el desarrollo de NewPay para "normalizar al protocolo CIMPRA y manejar un dominio inverso por cuenta" (mencionado en una reunión previa no documentada en la wiki) — de confirmarse, resolvería la causa raíz de fondo sin depender de que NewPay corrija su mapeo caso a caso; (2) pedido nuevo de que la **API Resolve devuelva el CUIT del aceptador** en la respuesta — hoy explícitamente fuera del contrato estándar IEP (ver arriba), simplificaría la resolución del lado de NewPay/PVS. Ninguno de los 2 puntos tiene respuesta de Bind PSP en el hilo. Tarea T-090 (`tareas_producto.md`).

### IEP / API Resolve (antes "JEP") — contrato técnico oficial

- **IEP = Interfaz Estandarizada de Pagos.** Norma bajo la Comunicación SINAP "A" 7153, es la API que cada aceptador (todo el que emite QRs — bancos y PSPs) está obligado a exponer para que cualquier billetera pueda consultar si un QR se puede pagar y con qué datos.
- También conocida como **API Resolve**; nació llamándose **JEP/YEP** y evolucionó junto con Transferencia 3.1 para mitigar fraude.
- **No existe una IEP centralizada en Coelsa** — cada aceptador expone la suya propia. Coelsa cumple un rol de coordinación/homologación, no de servidor central de consultas.
- En producción, la IEP de Bind PSP está expuesta bajo `api.binpagos.com.ar` (documentada en el portal público como **API Resolve**).

#### Contrato de la llamada (Boletín CIMPRA 525, sección 2.3)

```
GET https://[url_obtenida de la tabla de resolución]
```

| Parámetro | Requerido | Descripción |
|---|---|---|
| `data` | Sí | Contenido crudo del QR |
| `elapsed_time` | No | Tiempo en ms desde que se escaneó el QR por primera vez |
| `attempt` | No | Cantidad de reintentos de resolver el pago |
| `access_token` | Sí | Token de identificación entre billetera y adquirente — gestionado formalmente al aceptar las condiciones de uso del ecosistema, al integrarse con Coelsa |

**Response status:**

| Status HTTP | Descripción |
|---|---|
| 200 | El QR ha sido interpretado exitosamente |
| 401 | El `access_token` utilizado no es válido para esta operación |
| 403 | No se ha enviado el `access_token` |

#### Escenarios de respuesta (campo `status` del root node)

| `status` | Escenario | Ejemplo/Notas |
|---|---|---|
| `open_amount` | El vendedor no tiene integración ni usa la app de cobro — el comprador debe ingresar el monto manualmente. También aplica cuando el cobro permite elegir un monto dentro de un rango (`min_amount`/`max_amount` opcionales en el `order`). |
| `closed_amount` | El vendedor usa herramientas de cobro y la información de venta ya está disponible — el pagador tiene todo lo necesario para confirmar. |
| `pending` | El vendedor usa integración directa pero la info aún no está disponible (ej. pedido cargándose, carga de combustible). Incluye `retry_delay` (segundos) — puede variar según cantidad de reintentos y tipo de local (petroleras, comida rápida, etc.) y **debe respetarse**. |
| `unsupported_qr_code` | El QR escaneado no es válido (debería filtrarlo la app al analizar el EMVCo, pero puede llegar igual). |
| `timeout` | Se excedió el límite de reintentos del escenario `pending`. |
| `unsupported_merchant` | El vendedor aún no verificó su identidad ni generó su CVU/alias — no se puede proceder. |
| `error` | Ocurrió un error al procesar el QR del lado del adquirente. |
| `empty_order` | El vendedor tiene integración directa pero aún no hay nada por cobrar (ej. período de gracia en un estacionamiento) — el pagador debe reintentar reescaneando. |

Estructura de datos del `order`/`collector` (Anexo II): `collector.name` (string 50), `collector.identification_number` (string 11), `collector.account` (string 22), `order.id` (string 68), `order.total_amount`/`max_amount`/`min_amount` (decimal), `items[]` con `title`/`unit_price`/`currency_id`/`quantity`/`picture_url`/`description`.

### Proceso de homologación de nuevos participantes

Según el **Reglamento Operativo de Integración de Participantes** (CIMPRA), el ecosistema tiene 3 tipos de actores:

| Actor | Rol |
|---|---|
| **Billeteras digitales** | Ofrecidas por entidades financieras o PSP, capturan credenciales para instruir débitos/créditos. |
| **Aceptadores** | Integran comercios al ecosistema, les dan de alta y les ofrecen las herramientas para recibir pagos. |
| **Administradores** | Definen reglas operativas/técnicas/comerciales de su esquema de pago (ej. Coelsa), gestionan el alta de nuevos participantes. |

#### Requisitos mínimos

- **Billeteras:** estar en el registro de PSP (PSPCP o PSI) o ser entidad financiera; brindar datos mínimos de alta, facturación, cuenta de destino y documentación técnica; indicar el banco de conexión al Sistema Nacional de Pagos si no es entidad financiera.
- **Aceptadores:** estar registrado como PSP/entidad financiera/proveedor de servicios (sujeto a supervisión BCRA); **estar inscripto como agente de recaudación de impuestos nacionales o provinciales**; mismos requisitos de datos que las billeteras.

#### Proceso de adhesión — 2 etapas

1. **Alta** — relación comercial, onboarding, pruebas y homologación con **un** administrador (ej. Coelsa). El nuevo participante debe demostrar cumplimiento de los requisitos mínimos. Datos mínimos a comunicar al resto del ecosistema:
   - *Billetera digital:* Nombre, CUIT, CBU, contacto técnico, alias, Public Key.
   - *Aceptador:* Nombre, CUIT, **reverse domain** (dominio invertido), contacto técnico, flag de uso de API Resolve QR Payment, URL de la API Resolve QR Payment.
   - El administrador que dio de alta al participante debe comunicar la novedad a los demás administradores del ecosistema **dentro de las 48 horas hábiles**.

2. **Integración** — interconexión con el resto del ecosistema hasta el pasaje a producción:
   - Gestión de firmas en homologación: **72 horas hábiles** desde la notificación de adhesión.
   - Calendarización de ventanas de homologación para pruebas: **máximo 14 días hábiles** desde la notificación.
   - **Casuísticas de prueba obligatorias:** Pago, Devolución total, Devolución parcial, QR estático (open amount y closed amount), QR dinámico, parseo del código QR.
   - Al concluir las pruebas, se emiten **Certificados de Interoperabilidad** (para un nuevo Aceptador: certificado incremental a las billeteras del ecosistema; para una nueva Billetera: un certificado por cada administrador del esquema).
   - Un nuevo Aceptador queda habilitado a recibir pagos con QR una vez que el administrador constata que sus QR pueden ser leídos por todas las billeteras inscriptas en el Registro del BCRA.

⚠️ Riesgo conocido en la práctica: puede haber QRs interoperables **válidos en formato** pero de un aceptador que Bind PSP específicamente no tiene registrado en su tabla (ej. anécdota real con un aceptador identificado como "PW"/Prisma). En ese caso el QR es rechazado como "inválido" desde la perspectiva de Bind PSP, aunque el QR en sí sea correcto — el aceptador simplemente no fue homologado (u homologado tarde) con Bind PSP.

### Troubleshooting: QR que no se puede leer o pagar

Protocolo de diagnóstico sugerido en la sesión de capacitación, en orden:

1. **¿El QR es interoperable?** Verificar el formato a simple vista (estructura EMVCo TLV descripta arriba), o pegar el string en un generador de QR / consultarlo contra la documentación CIMPRA (incluso vía asistentes de IA con el documento adjunto). Un QR "no interoperable" (ej. un link tipo menú de restaurante) es un problema distinto — nunca fue pensado para ser leído por cualquier billetera.
2. **¿Se puede leer con Mercado Pago?** Si sí, probar con otra billetera (ej. Modo). Si ninguna otra billetera lo puede leer tampoco, el problema está en el QR en sí (formato roto).
3. **¿Se puede leer con Mercado Pago pero no con la propia billetera?** Es interoperable, pero el aceptador probablemente no está homologado/registrado en la tabla de dominio inverso de la billetera que falla.
4. **Caracteres especiales rompen el estándar.** Tildes, espacios, o símbolos raros en nombre de comercio, razón social o domicilio (ej. "Córdoba" mal codificado) pueden romper el parseo del string y volverlo un QR inválido pese a parecer interoperable a simple vista. Casos reales reportados con el nombre/apellido del comercio.
5. **Caída de la API Resolve propia** = nadie puede leer ni pagar los QR de Bind PSP, porque no hay servidor al que consultar (response `status: "error"` o directamente sin respuesta). También se reportó un bug histórico donde la API Resolve "mezclaba" respuestas entre consultas concurrentes (cache cruzada entre distintos QRs consultados casi al mismo tiempo).
6. **Rechazo `7901`/`INTEROPERABLE_VALIDATIONS_ERROR`/`ADQUIRIENTE_NO_VINCULADO` solo con billeteras puntuales (ej. las que procesan vía NewPay), mientras otras billeteras (MODO, MP) pagan sin problema.** No es un problema del QR ni de la API Resolve de Bind — es la billetera/procesador enviándole a Coelsa un CUIT de aceptador mal derivado (ver caso real documentado arriba, "Dominio inverso y tabla de resolución de URL"). Señal distintiva: el error nunca llega a los logs de Bind PSP (Coelsa lo rechaza en la validación de datos antes de que la consulta llegue al aceptador), y las transacciones exitosas/fallidas se pueden dar sobre el mismo comercio en la misma franja horaria según qué billetera/procesador paga.

**Trazabilidad:** las comunicaciones de la IEP/API Resolve pueden reconstruirse en herramientas de logging estructurado (Elastic) para diagnosticar reclamos de "no puedo pagar este QR".

### Nueva funcionalidad de Coelsa: COELSA.PREVENT — ON HOLD (anuncio 2026-07-17)

> Fuente: mail "ON HOLD | Nueva funcionalidad COELSA.PREVENT" — coelsateinforma@coelsa.com.ar (2026-07-16).

Coelsa suma a **COELSA.PREVENT** (su capa de prevención de fraude para el ecosistema de transferencias inmediatas/QR interoperable) una instancia preventiva llamada **ON HOLD**: permite detener temporalmente una operación que presente indicadores de riesgo, dejándola en espera para análisis adicional antes de procesarla, en vez de solo detectar el fraude después del hecho. **Disponible a partir del 2026-07-28.**

**Driver regulatorio:** la Comunicación "A" 7463 del BCRA exige que los esquemas de transferencias inmediatas cuenten con herramientas para identificar patrones sospechosos, garantizar trazabilidad de extremo a extremo y compartir información para prevenir/detectar/mitigar fraude — ON HOLD es la respuesta de Coelsa a esa exigencia.

**Pendiente de confirmar** (no está en el cuerpo del mail, solo mencionado como aviso general a todo el ecosistema): si Bind PSP (como aceptador/billetera) necesita optar-in, configurar algo de su lado, o si el hold lo gestiona Coelsa de forma transparente. Sin acción de Producto registrada todavía — ver `../../../2_areas/gaps_y_preguntas.md` si se necesita seguimiento.

### Ejemplo real de homologación de un nuevo aceptador — WAYA vía NewPay (2026-07-31)

> Fuente: mail "PRODUCCION: Aceptador WAYA (Newpay) – Billetera BIND PSP (COELSA)" — MGamarra@newpay.com.ar, 2026-07-31.

Caso concreto del proceso de alta de aceptador descripto en "Proceso de homologación de nuevos participantes" más arriba: NewPay avisó que el BCRA habilitó al aceptador **WAYA** (CUIT `33-71833017-9`, dominio inverso `ar.waya`, vía el proxy `wallet.newpay.com.ar/external/resolve` de NewPay como Administrador) para operar en producción, y pidió a Bind PSP (como billetera) dar de alta esos datos en su tabla de resolución. Bind (Alan Martínez) lo configuró el mismo día y pidió un QR de prueba; WAYA compartió un QR estático de monto abierto y Bind confirmó un pago de prueba de $10 con `estadoExterno: "ACREDITADO"` — WAYA validó la transacción en su sistema, cerrando la homologación end-to-end en menos de 6 horas.

### Ticket #469781 — Error de SPLIT / acreditación diferida — resuelto por Coelsa (2026-08-03)

> Fuente: mail "Nueva respuesta en tu ticket #469781 - Error de SPLIT - Acreditación diferida" — soporte@coelsa.com.ar, 2026-07-21 a 2026-08-03.

Ticket abierto el 2026-07-21 por un caso de **SPLITQR** (ver modelo "Con split" en Parte 3) donde el CashOut hacia el CBU externo del comercio se generaba varias horas después de finalizada la operación, en vez de en el momento. Coelsa confirmó (23/07) que había elevado la casuística a su equipo de desarrollo sin ETA. **Resolución (2026-08-03):** Coelsa aplicó una mejora en el servicio de SPLITQR y confirmó, tras monitoreo propio, mejoras evidentes en el procesamiento durante horarios de picos operacionales — no deberían volver a verse casos donde una operación genere su CashOut de SPLITQR horas después de finalizada. Sin caso puntual de Bind PSP confirmando el cierre a la fecha de este barrido.

---

## Parte 2 — Flujo de Pago QR con Coelsa (Transferencia 3.0/3.1)

> Documento oficial: `Transferencias_3.1_-_Pagos_con_QR_v1.pdf` — "FLUJO TRX3.1 PAGOS QR v1.0" (COELSA, Gerencia de Ingeniería y Datos, Nivel de seguridad: Restringido).

### Participantes del flujo

| Rol (norma) | Quién es en la práctica |
|---|---|
| **Plataforma adquirente** (Aceptador) | El backend/APIs de la entidad que cobra (ej. Bind PSP como aceptador de su propio comercio, o un cliente adquirente). |
| **Dispositivo de punto de venta** | El front del comercio que expone el QR (ej. nuestro POS, o el portal comercio). |
| **Billetera (front)** | La app del pagador (ej. app Bind, Mercado Pago, Modo). |
| **Plataforma billetera (backend)** | Los servicios de Wallet que instruyen el pago. |
| **Coelsa** | El procesador/cámara compensadora que orquesta el flujo entre bancos. |
| **Banco débito** | El banco donde está la cuenta recaudadora del CVU de la **billetera pagadora**. |
| **Banco crédito** | El banco donde está la cuenta recaudadora del CVU del **comercio cobrador**. |

### CVU vs CBU — la plata no vive donde parece

- Un **CVU es una etiqueta**, no una cuenta con saldo propio. La plata transferida va realmente a una **cuenta recaudadora** (identificada por el CBU real); el CVU es solo el pedacito que identifica a quién corresponde dentro de esa recaudadora.
- Bind PSP, cuando recibe pagos a CVUs, **no lleva el saldo por su cuenta** — el saldo real vive en el banco de la recaudadora, no en un sistema interno de Bind (excepto en el modelo de "acreditación en línea/wallet", ver Parte 3).
- En una transferencia QR: hay un **débito en la cuenta recaudadora de la billetera pagadora** y un **crédito en la cuenta recaudadora del comercio cobrador**.

### ⚠️ Cambio clave en Transferencia 3.1: el mensaje de confirmación pasa a ser SÍNCRONO

El documento oficial de Coelsa contrasta explícitamente el **circuito actual (pre-3.1)** contra el **circuito propuesto (3.1)**:

| | **Antes de 3.1** | **Con Transferencia 3.1** |
|---|---|---|
| Mensaje de confirmación de débito al Aceptador (`QRConfirmaDebito`) | **Asincrónico** | **Sincrónico** — el Aceptador responde en el momento con `APPROVED`/`REJECTED` |
| Código de referencia único | No existía | **Payment Reference** — código único que vincula la operación tanto del lado Billetera como Aceptador |
| Mensaje de Intención de Pago | No contemplado explícitamente | Se agrega `QRIntenciondepago`, donde el Aceptador valida el Interchange y responde MCC + Código Postal |
| Falsos positivos en Billeteras (por consultar el estado antes de que el Aceptador confirmara) | Ocurrían | Se eliminan — el estado no pasa a "ACREDITADO" hasta que el Aceptador confirma explícitamente |
| Diferenciación reversa técnica vs. devolución | No | Sí, ahora es posible distinguirlas |

### Secuencia completa del pago — mensajes reales (Transferencia 3.1)

1. **Datos iniciales**: la plataforma adquirente le da al punto de venta los datos para mostrar el QR (ya generado, ver Parte 1).
2. **Lectura**: la billetera escanea el QR y consulta la IEP/API Resolve del aceptador (según dominio inverso) para obtener los datos del pago.
3. **Instrucción de pago a Coelsa**: la billetera instruye el pago mediante `POST /apiDebinV1/QR/QRDebin`. **Coelsa no acciona nada hasta que la billetera se lo instruye explícitamente** — la sola lectura del QR (paso 2) no dispara nada en Coelsa.
4. **`POST [EPPSP]/QRIntenciondepago`** — Coelsa llama al endpoint del Aceptador. **Mensaje síncrono, el Aceptador tiene 3 segundos para responder.** Envía los datos de la intención de pago de la billetera y los datos del interchange a realizar (según los códigos MCC configurados para el comercio). El Aceptador responde:
   - `validation_status.status`: `"PASS"` o `"FAIL"`.
   - `validation_data`: MCC a utilizar, código postal del comercio, y el `payment_reference` si ya está disponible en esta instancia.
5. Si la respuesta es `"PASS"`, Coelsa continúa: **`POST [ep]/AvisoDebinPendiente`** al **banco débito**.
6. El banco débito responde con **`POST /Debin/ConfirmaDebito`** confirmando el débito exitoso.
7. Coelsa realiza el **control de garantía débito**.
8. **`POST [ep]/Credito`** al **banco crédito**, acreditando el monto en su cuenta recaudadora.
   > ⚠️ **Nota importante del documento oficial:** este aviso de crédito es **"forzado"** — se asume que cualquier código de respuesta distinto a `03`, `04` y `06` son problemas *temporales* de la entidad para aplicar el crédito, y la operación **queda igualmente compensada** (no se envían mensajes de reverso a ninguno de los dos extremos). Se espera que la entidad aplique el crédito por su cuenta, reintentando vía una API dedicada hasta el cierre del producto, o tomando la información del archivo de conciliación si no logró aplicarlo a tiempo.
9. **`POST [epPSP]/QRConfirmaDebito`** al Aceptador — **ahora síncrono en 3.1** (antes era asíncrono), el Aceptador tiene **3 segundos** para responder. Envía básicamente el mismo payload que la Intención de Pago, con el campo `interchange` reducido solo al MCC ya informado.
   - El Aceptador responde `transaction_status.status`: `"APPROVED"` o `"REJECTED"`, y el mismo `payment_reference` informado en la Intención de Pago.
10. **Recién cuando el Aceptador responde `"APPROVED"`**, Coelsa cambia el estado de la transacción de **"EN CURSO"** a **"ACREDITADO"**, y dispara automáticamente el mensaje final **`POST [epBilletera]/QROperacionFinalizada`** a la billetera, confirmando que la operación finalizó y los fondos fueron acreditados.

**SLA normativo: todo el circuito debe completarse en menos de 15 segundos** desde la recepción del mensaje de Intención de Pago (cada mensaje síncrono individual — `QRIntenciondepago` y `QRConfirmaDebito` — tiene 3 segundos de timeout propio).

### Payment Reference — código único de vinculación

- Es un identificador que el **Aceptador genera/informa** (idealmente ya en la respuesta de `QRIntenciondepago`, o a más tardar en `QRConfirmaDebito`) y que **debe ser el mismo en ambas respuestas**.
- Coelsa lo reenvía a la Billetera en el mensaje final `QROperacionFinalizada`, permitiendo que **tanto el Aceptador (comercio) como la Billetera (usuario) tengan un único código de referencia** para identificar la misma operación en sus respectivos sistemas — antes de 3.1 no existía este puente formal entre ambos lados.

### Flujos de error y reversa

#### Error en `QRIntenciondepago` (3 posibilidades)

| Caso | Consecuencia |
|---|---|
| El Aceptador no responde en 3 segundos (timeout) | Se envía `POST [epPSP]/QRReverso` al Aceptador, y a la Billetera se le responde con error en `POST /apiDebinV1/QR/QRDebin` indicando reversa. |
| El Aceptador responde `"FAIL"` | A la Billetera se le responde con error en `POST /apiDebinV1/QR/QRDebin` indicando reversa. |
| El Aceptador responde `"PASS"` pero los datos son rechazados por las validaciones de Coelsa | Igual tratamiento que el timeout: `QRReverso` al Aceptador + error a la Billetera. |

#### Error después de un `"PASS"` exitoso (4 posibilidades: `AvisoDebinPendiente`, `ConfirmaDebito`, proceso de Garantías Débito, o `Credito`)

En cualquiera de estos 4 casos, se dispara la misma secuencia de reversa completa:
1. `POST [ep]/AvisoOperacionFinalizada` al **Banco Crédito**, indicando reversa.
2. `POST [epPSP]/QRReverso` al **Aceptador**, indicando reversa.
3. `POST [ep]/AvisoOperacionFinalizada` al **Banco Débito**, indicando reversa.
4. `POST [epBilletera]/QROperacionFinalizada` a la **Billetera**, indicando reversa.

#### Error en `QRConfirmaDebito` (3 posibilidades)

| Caso | Consecuencia |
|---|---|
| El Aceptador no responde en 3 segundos (timeout) | Reversa completa (mismos 4 mensajes que arriba). |
| Error en el proceso de Garantías Crédito | Reversa completa. |
| El Aceptador responde `"REJECTED"` | Reversa completa. |

#### Recuperación ante mensajes no recibidos

Si el Aceptador, por alguna razón, **no recibe** el mensaje `QRConfirmaDebito` ni `QRReverso`, debe **consultar el estado del DEBIN** proactivamente, respetando la ventana de 15 segundos de duración total de la transacción contada desde la recepción del mensaje de Intención de Pago.

### Impacto en el sistema interno al recibir la confirmación

- El evento **`QRConfirmaDebito`** (respondido con `"APPROVED"`) es el disparador de todo lo que pasa del lado de Bind PSP como comercio/aceptador:
  - Se **inserta la transacción** en las tablas internas (pasa de un estado "en proceso" a **acreditada**).
  - Si había una **orden de venta** asociada, se marca como pagada.
  - Un **microservicio interno queda escuchando permanentemente a Coelsa** para hacer esta inserción — no es un polling manual, es un listener de eventos.
- Antes de esta confirmación, ante demoras se muestra un estado intermedio "en proceso" (cartelito amarillo en el front) — el sistema **consulta proactivamente a Coelsa** para confirmar el estado real ante la duda, ya que hubo casos históricos donde el aviso de Coelsa llegaba pero la transacción no estaba realmente completa del lado bancario (lección aprendida documentada como buena práctica: "hay que ir a consultar sí o sí").
- **Trazabilidad:** todas las comunicaciones con Coelsa (los `POST` salientes y entrantes de este flujo) se registran en **Elastic**, lo que permite reconstruir el camino completo de un pago QR específico para troubleshooting.

### Errores comunes y cómo diagnosticarlos

| Error reportado | Dónde está el problema | Notas |
|---|---|---|
| **Error débito** | Entre Coelsa y el **banco débito** (`AvisoDebinPendiente`/`ConfirmaDebito`) | El motivo puede variar (ej. falta de fondos) aunque el código de error mostrado sea siempre el mismo — no hay garantía de que el código distinga la causa raíz. |
| **Error crédito** (también visto como "error emisor"/"error aceptador") | Al intentar acreditar al **banco crédito** (`POST [ep]/Credito`) | Puede indicar un problema puntual del lado del comercio/billetera receptora. Ver la nota sobre créditos "forzados" arriba — no todo código de error implica reversa real. |
| **Error de datos / QR inválido** | `QRIntenciondepago` o antes | Puede originarse en la lectura inicial del QR — ver troubleshooting en Parte 1. |
| **Comercio inexistente** (código `7156`) | Validación agregada en `POST /apiDebinV1/QR/QRDebin` | El comercio debe existir y estar dado de alta en la operatoria — ver Parte 4 (Interchange). |
| **Comercio inactivo** (código `0562`) | Validación en `ConfirmaDebito` | Ver Parte 4 (Interchange). |
| **CVU vendedor no habilitado** (código `7154`) | Validación de Coelsa sobre el vendedor en `QRIntenciondepago` | **Causa real confirmada** (caso Soporte 2026-07-14, comercio C18807/GST): no es (solo) que falte la adhesión de vendedor — el CVU asignado al comercio pertenecía a una **titularidad (CUIT) distinta** a la del comercio creado. Coelsa exige que el CVU del vendedor sea de la misma titularidad que el comercio. Detalle completo en §Acreditación en línea/wallet más abajo. |

- **Caso particular:** cuando Bind PSP paga su propio QR con su propia billetera (pruebas internas), **Bind PSP es tanto el banco débito como el banco crédito** — porque la billetera de pruebas tiene como banco sponsor la cuenta recaudadora del banco BIN, igual que el comercio que cobra.
- **Acceso a la documentación oficial de errores de Coelsa está restringido**: solo accesible conectado a la VPN de producción o al WiFi de las oficinas de BIN. El equipo señaló esto como una fricción operativa (no se puede consultar remotamente sin VPN), y recomendó armar una tabla propia (Excel) con los códigos de error y su significado para tener a mano, ya que la documentación oficial lista los códigos pero no siempre explica su causa en profundidad.

---

## Parte 3 — Alta de Comercio para Cobro QR en Coelsa

> Fuente: sesiones de capacitación del 2026-01-09 y 2026-01-13. Complementa la Parte 2 (qué requisitos previos hacen posible ese flujo) y la decisión ya registrada en [log_decisiones.md](../../../2_areas/direccion/decisiones.md) (migración de licencia PSP 164 → 184).

### Requisitos mínimos para cobrar con QR

Para que un comercio (con entidad → comercio → sucursal → caja ya creados en la base de Bind PSP) pueda efectivamente cobrar con QR, hacen falta dos cosas que **Coelsa no conoce automáticamente por más que exista el registro interno**:

1. Un **CVU** asociado a la caja/comercio.
2. El comercio **dado de alta en Coelsa** (vía la API de Coelsa "Alta de Comercios" / API CBU).

Ambos pasos ocurren durante el **alta del canal QR** en el sistema interno (botón "habilitar canal QR" / "habilitar QR con o sin split") — crear el registro en la base propia (entidad/comercio/sucursal/caja) **no habilita el cobro por sí solo**.

### Datos requeridos en el alta de comercio en Coelsa

| Campo | Notas |
|---|---|
| ID PSP | 164 (Banco Industrial, histórico) o 184 (Bind PSP propio) |
| CUIT | Debe coincidir siempre con lo que Coelsa tiene registrado — ver riesgos abajo |
| Tamaño del comercio | Chico / Mediano / Grande — en función de la transaccionalidad esperada |
| Actividad comercial | Código de actividad (ver Parte 4) |
| Comisión | Numérica, dos decimales, debe respetar el rango asociado a la actividad comercial |
| Razón social / nombre de fantasía | — |
| Fecha de alta | — |
| **Tramo gratuito** (`true`/`false`) | Ver abajo |

#### Tramo gratuito

- Es un beneficio propio de la **normativa Transferencia 3.0**: los comercios de categoría **"CHICO"** pueden operar sin comisión de Interchange durante **3 meses calendario** desde el inicio de la operación, siempre que las transferencias acumuladas **no superen las 1.000 UVAS** — cifra confirmada por la especificación técnica oficial de Coelsa (ver Parte 4), que precisa lo que en la sesión de capacitación había quedado como una referencia aproximada ("no me acuerdo el número exacto").
- **Bind PSP da de alta a todos los comercios como "chico" y "tramo gratuito = true" por defecto**, independientemente del tamaño real esperado. Esto genera la necesidad de **actualizar manualmente en Coelsa** cuando un comercio efectivamente crece o se sabe de antemano que va a ser grande (ejemplo citado: Coto no se dio de alta como gratuito porque ya se sabía que sería un comercio grande).
- Coelsa fuerza (o "putea", en palabras de la sesión) a actualizar el estado cuando corresponde — no hay automatización confirmada de este control al momento de la sesión.

#### Actividades comerciales y comisiones

> Detalle técnico completo en Parte 4. Resumen:
> - Cada **actividad comercial (rubro)** tiene, a nivel PSP, un **rango de comisión mínimo/máximo** configurado vía API de Coelsa.
> - Cada **comercio individual** puede tener su propia comisión, siempre que caiga dentro de ese rango — si no se informa, cae en cascada a la comisión de su actividad comercial, y si tampoco está informada ahí, al default de **0,8%**.
> - La comisión de Coelsa es **fija: 2,5% de la comisión del comercio**, y el resto se reparte entre Adquirente/Billetera según el tamaño del comercio (CHICO 75/25, MEDIANO 50/50, GRANDE 25/75).
> - Actualizar la comisión de un comercio o de una actividad comercial requiere gestionarlo **en Coelsa vía API**, no solo en el sistema interno de Bind PSP — a diferencia de otros medios de pago, donde la comisión se calcula solo internamente.
> - ⚠️ Persiste una pregunta abierta sobre el caso real documentado originalmente (comercio con mismo CUIT, comisión 0,8% vs. 0,05% declarada, terminó operando con 0,8%): la especificación oficial deja dos explicaciones posibles (rechazo por estar fuera de rango, o el campo quedó `NULL` y cayó al fallback de la actividad comercial). Ver gap abierto en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).

#### Riesgos al modificar datos de un comercio ya operativo

| Cambio | ¿Rompe algo? | Por qué |
|---|---|---|
| **CVU** (eliminar y crear uno nuevo) | Puede romper QRs ya emitidos/impresos si la billetera pagadora quedó con el CVU viejo en su consulta a la IEP — pero **no requiere avisar a Coelsa**, porque Coelsa se entera del CVU vigente en cada consulta a la IEP, no por un registro estático. | La IEP siempre devuelve el CVU *actual*; el problema surge solo si hay un desfasaje temporal entre lo que la billetera cacheó y lo que Coelsa espera. |
| **CUIT** | **Sí rompe** — Coelsa valida el CUIT contra lo que tiene registrado desde el alta del comercio. Si se cambia el CUIT en la base interna sin actualizarlo en Coelsa, la instrucción de pago es rechazada. | Coelsa mantiene su propio registro de comercio por CUIT, no lo re-consulta dinámicamente como al CVU. |
| **Comisión** | Requiere actualización espejada en Coelsa (ver arriba) | — |

### Adhesión de vendedor (alta de cuenta recaudadora)

- Antes de generar cualquier operación, **cada adquirente debe agregar a Coelsa la(s) cuenta(s) recaudadora(s)** que va a usar, mediante el método **"adhesión de vendedor"** — es un proceso **por única vez por cada cuenta recaudadora**.
- Ejemplo citado: se ejecutó al habilitar el PSP 184 con clientes como Coto y La Virginia.
- Si falta este paso, el error típico que aparece al habilitar el canal es de tipo "alta cuenta vendedora".

### Modelo con split vs sin split

Ambos modelos requieren los mismos dos pasos base (CVU + comercio en Coelsa). La diferencia está en qué pasa **después** de que la plata entra a la cuenta recaudadora.

| Modelo | Qué pasa con la plata | Cómo se liquida |
|---|---|---|
| **Sin split** | Queda en la cuenta recaudadora de Bind PSP (el comercio no la controla directamente). | Bind PSP arma la liquidación diaria: junta todo lo cobrado en el día y hace **una transferencia bancaria manual/batch** al día siguiente con el neto total. Este fue el modelo original con el PSP 164. |
| **Con split** | Coelsa transfiere automáticamente, **uno a uno por cada cobro**, el 100% neto de comisiones desde el CVU a un **CBU externo** indicado por el comercio (ej. Banco Galicia, Banco Francés). | Automático, vía la funcionalidad **split** de la API de comercio de Coelsa. |

- La habilitación con split requiere indicar el CBU externo (ej. `endpoint habilitar split` de Coelsa: CVU del comercio, CBU final, porcentaje a transferir — hoy siempre 100% del neto).
- **Restricciones del split, según Coelsa:** el destino debe ser sí o sí un **CBU** (no se puede hacer split a otro CVU), y ese CBU debe ser de **la misma titularidad** que el CVU de origen.
- El split se puede habilitar/deshabilitar por comercio de forma independiente — Bind PSP puede ofrecer split a algunos comercios y no a otros según lo que se negocie comercialmente.

### Evolución PSP 164 → PSP 184

| | **PSP 164** (histórico) | **PSP 184** (actual) |
|---|---|---|
| Quién es el aceptador legal | Banco Industrial (Bind operaba "prestado" bajo su licencia) | Bind PSP con licencia propia |
| Cuentas recaudadoras | **Una sola**, compartida por todas las entidades/comercios — todos los cobros QR caían en la misma "bolsa" | **Múltiples**, una por organización/cliente (multiPSP) |
| Agente de retención de impuestos | El banco (Banco Industrial), por ser el titular de la licencia | Bind PSP — responsabilidad propia |
| Modelo de acreditación disponible | Con split o sin split únicamente | Con split, sin split, **o acreditación en línea/wallet** (nuevo) |

#### Acreditación en línea / acreditación wallet (nuevo con el 184)

- Aplica cuando el comercio **ya tiene cuenta y CVU en Wallet** de Bind PSP y se quiere que sus cobros QR se reflejen **en tiempo real** en esa cuenta wallet, sin pasar por el circuito de split.
- Diferencia clave respecto a "sin split": en el modelo tradicional sin split, el CVU se crea nuevo y es controlado por Bind PSP (el comercio no tiene visibilidad/control directo). En **acreditación en línea**, el comercio **ya tiene su propio CVU** (el de su cuenta wallet) y ese es el que se usa directamente al dar de alta el comercio en Coelsa — no se crea uno nuevo.
- Técnicamente a nivel Coelsa es equivalente al modelo "sin split" (la plata entra y queda en la recaudadora), pero el CVU usado ya es propiedad/control del cliente final vía su cuenta wallet, por lo que ve el saldo reflejado inmediatamente.
- Una vez creado el comercio con el CVU fijo del cliente, el sistema interno detecta (por una especificación de la entidad) que corresponde generar automáticamente los comprobantes de acreditación en Wallet.

#### 3 flujos posibles de creación/habilitación de comercio QR (PSP 184)

1. **Sin split** — se crea un CVU nuevo asociado al comercio, se da de alta en Coelsa. Sirve para comercios sin wallet que quieren que Bind PSP les liquide por transferencia periódica a un banco externo de su elección (ej. cliente que insiste en cobrar directo en su banco, como Banco Provincia).
2. **Con split** — igual que el anterior, más la configuración de split hacia un CBU externo.
3. **Con acreditación en línea/wallet** — se usa el CVU ya existente de la cuenta wallet del cliente, sin crear uno nuevo.

⚠️ **Importante para diagnosticar errores de habilitación de QR:** entender cuál de los tres flujos corresponde a un comercio es clave para saber por qué falla un alta (ej. falta el CBU cuando el flujo es "con split", o el CBU pertenece a otro CUIT).

#### Troubleshooting real — "CVU VENDEDOR NO HABILITADO" (código `7154`) en acreditación en línea

> Caso Soporte real, 2026-07-14 — comercio **C18807** (entidad A130, cliente **GST**), CVU `0000184305540040971018`.

- **Síntoma:** el comercio queda creado y habilitado para QR del lado de Bind (specs completas: `WALLET_CUENTA`/`WALLET_CVU`/`WALLET_ORGANIZACION`, comercio dado de alta y activo en Coelsa), pero todo intento de pago del QR devuelve `estadoExterno: "ERROR DATOS"` con `mensajeAdicional`: *"El QR debin fue creado con errores en COELSA. Detalle: CVU VENDEDOR NO HABILITADO | Respuesta: 7154"*.
- **Hipótesis descartadas en el diagnóstico** (documentadas para no repetir el mismo camino en falso en un caso futuro):
  1. Falta de adhesión de vendedor de la cuenta recaudadora — **descartada**: la cuenta ya estaba adherida como vendedora en Coelsa.
  2. Comparación de especificaciones (`EspecificacionTipo`) contra un comercio de la misma entidad que sí funciona — no arrojó diferencias estructurales relevantes (las specs extra 2279/2280/2281 del modelo acreditación en línea son esperables y no un error en sí).
  3. Desalineación entre el `WALLET_ORGANIZACION` interno y la cuenta recaudadora real — **descartada**: el error viene del propio Coelsa (`QRIntenciondepago`), no de una validación interna de Bind, así que una desprolijidad puramente interna no explica un rechazo del lado Coelsa.
- **Causa raíz real:** el **CVU asignado al comercio** (`datosWallet.WALLET_CVU` / campo `Cbu`/`Cvu` del alta) pertenecía a una **cuenta de titularidad (CUIT) distinta** a la del comercio que se estaba creando. Coelsa exige que el CVU del vendedor sea de la misma titularidad que el comercio/vendedor informado en la operación — mismo principio que la restricción de titularidad ya documentada arriba para el split (el CBU externo debe ser de la misma titularidad que el CVU de origen), aplicado acá al CVU de acreditación en línea.
- **Chequeo rápido para futuros casos:** antes de dar de alta un comercio con acreditación en línea/wallet, confirmar que el titular (CUIT) de la cuenta wallet dueña del CVU indicado coincide exactamente con el CUIT del comercio a crear. Si no coincide, Coelsa rechaza el pago con este mismo código aunque el comercio esté "habilitado" y la cuenta recaudadora esté adherida como vendedora.
- **Confirmación oficial de Coelsa (mismo ticket #466955, cierre 2026-07-15):** Coelsa validó del lado propio la hipótesis con datos concretos — para el CVU `0000184305540040971018`, su base tiene registrado el CUIT `20257910459` (titular Nestor Ariel Romanski), mientras que el request de Bind envió `cuitVendedor: "30715575066"` (CUIT distinto). Cierra el loop iniciado el 07-14: la causa raíz ya documentada arriba queda confirmada con evidencia de ambos lados (Bind y Coelsa), no solo hipótesis de Bind.

> Fuente: Mail "Nueva respuesta en tu ticket #466955 - Rechazo en pago QR interoperable: Error 7154 - CVU VENDEDOR NO HABILITADO" — soporte@coelsa.com.ar (2026-07-15).

#### Mecánica de comprobantes y cluster de bugs de acreditación en línea (Epic histórica "QRI PSP 184 acreditación en wallet")

> Fuente: Notion histórico, Epic **"QRI PSP 184 acreditación en wallet"** (~49 tickets — segundo cluster de bugs más denso de Adquirencia después de Botón Simple 2.0). Detalla la mecánica de comprobantes detrás de §"Acreditación en línea" de arriba.

- **Mecánica de comprobantes**: cada cobro con QR en un comercio de acreditación en línea genera **en el momento** un comprobante de crédito en la cuenta wallet por el importe **neto de comisiones**, más comprobantes de débito por cada retención de impuestos aplicable. Una devolución genera, simétricamente, un comprobante de débito por el importe devuelto.
- **Alcance explícito de esta Epic**: solo aplica al **PSP 184 propio** — al freeze del Notion, la funcionalidad **no estaba habilitada para otros PSP que opera Bind** (ej. SUR FINANZAS) y no generaba webhooks ni operaciones nuevas específicas de Wallet (se apoya en el mecanismo de comprobantes ya existente).
- **Cluster de bugs — mismo patrón que Botón Simple 2.0** (integración nueva sobre flujo de alta de comercio ya maduro): la mayoría de los ~30 bugs relevados son de **alta de comercio por Onboarding que queda a medio camino** — comercio creado sin CVU, sin habilitar, no creado en Access/SISCRI, CVU en null, error 422 al habilitar, falla "CuentaCVU vacío" — o de **inconsistencia entre lo que se cobra/devuelve y lo que se contabiliza**: una devolución debitaba el importe **bruto** cuando el cobro había acreditado el **neto** (asimetría de impuestos no contemplada en la reversa), y los registros de auditoría de impuestos/comprobantes en tablas de "propiedades adicionales" quedaban incompletos en varios escenarios.
- **Decisión de diseño confirmada durante el desarrollo**: la inserción de comprobantes en Wallet debía volverse **asíncrona** (ticket marcado "No aplica" — posiblemente descartado a favor de mantenerlo síncrono, o ya resuelto por otro mecanismo; verificar estado real).
- **Migración de comercios existentes**: se construyó un endpoint y una funcionalidad de Admin dedicados para migrar ágilmente comercios de un modelo viejo (con o sin split) hacia acreditación en línea, sin tener que recrearlos desde cero.

#### Múltiples cuentas recaudadoras — riesgo de ID de cuenta incorrecto

- Con el PSP 184, cada organización cliente (ej. Astropay, Senco) tiene su **propia cuenta recaudadora**, identificada por un campo de especificación **"ID cuenta"** que se define al crear la entidad.
- Ese "ID cuenta" determina en qué cuenta recaudadora Coelsa va a crear el CVU del comercio.
- **Bug real documentado:** por costumbre heredada del PSP 164 (donde solo existía una cuenta recaudadora, siempre "ID 1"), varios comercios se estaban creando con el ID de cuenta por defecto sin que nadie notara que ya existían ~140 cuentas recaudadoras distintas — resultado: comercios de distintas organizaciones terminaban recaudando en la cuenta de "Astro" por error, mezclando fondos que debían estar separados. Corregido como buena práctica: **verificar explícitamente el ID de cuenta recaudadora antes de habilitar el canal QR de una nueva organización.**

---

## Parte 4 — Interchange y Comisiones de QR — Especificación Técnica Coelsa

> Fuente: `Especificación Funcional - Customización Pagos QR v1.15.pdf` (documento técnico de COELSA, proyecto "TRX30 – Pago QR – Customización Interchange", 59 páginas, última revisión 15/09/2021).
> Este documento es la **fuente primaria/oficial** del mecanismo de comisiones — reemplaza y precisa lo que se había documentado de forma más informal (a partir de una capacitación interna) en la Parte 3.
> Ámbito: exclusivamente el producto QR (Anexo II de la norma BCRA A7153, que exige administrar el cobro y pago de comisiones de esta operatoria — "Interchange").

### API de Comercios (ABMC) — `apiCVU/Comercio`

Todos los endpoints requieren `Authorization: Bearer <TOKEN>` y `Content-Type: application/json`.

#### Alta de Comercio — `POST /apiCVU/Comercio/Comercio`

**Condiciones para alta exitosa:**
- El PSP/CUIT debe existir, estar activo y tener cuenta activa en el banco del token.
- La actividad comercial, si se informa, debe existir en la tabla de Actividades Comerciales del PSP (o ser nula → se registra como **"VARIOS"**, creándola si no existe).
- La **comisión** es numérica con 2 decimales (se trunca si se envían más); **valor mínimo 0, máximo 0,8%**. Si no se envía, se toma como "no informada".
- La comisión informada debe estar dentro del **rango mínimo/máximo de la actividad comercial** asociada, o se rechaza.
- Razón Social y Nombre de Fantasía no pueden ser nulos.
- Fecha de alta es opcional (default: hoy; si se informa, debe ser ≤ hoy).

**Campos del request:** `id_psp` (R), `cuit` (R, 11 caracteres), `categoria` (`CHICO`/`MEDIANO`/`GRANDE`, default `GRANDE`), `actividad_comercial` (default `VARIOS`), `comisión`, `razon_social`, `nombre_fantasia`, `fecha_alta`, `tramo_gratuito` (boolean, default `FALSE`).

**Códigos de respuesta:**

| Código | Descripción |
|---|---|
| 5000 | Comercio dado de alta con éxito |
| 5001 | Comercio no dado de alta |
| 5002 | CUIT mal formulado |
| 5003 | Categoría mal formulada |
| 5004 | Actividad comercial mal formulada |
| 5005 | ID PSP erróneo |
| 5007 | Comercio no dado de alta — comercio existente |
| 5008 | PSP no registrado en la entidad |
| 5009 | Comisión mal formulada |
| 5010 | Razón social mal formulada |
| 5011 | Nombre de fantasía mal formulado |
| 5012 | Fecha de alta mal formulada |
| 5013 | Tramo gratuito mal formulado |
| **5014** | **La comisión no se encuentra dentro del rango de comisión mínima y máxima de la actividad comercial** |
| 5098 | JSON incorrecto |
| 5099 | Error general |

También existe **Alta Masiva** (`POST /apiCVU/Comercio/Masivo`, hasta 1000 ítems por llamada, mismas reglas + código `5097` si supera el máximo), **Baja** (`DELETE /apiCVU/Comercio/Comercio/{idPsp}/{cuit}`, baja lógica sobre `COM_ACTIVO`), **Modificación** (`PUT /apiCVU/Comercio/Comercio/{idPsp}/{cuit}`, todos los campos opcionales pero se debe enviar al menos uno) y **Consulta** (`GET /apiCVU/Comercio/Comercio/{idPsp}/{cuit}`).

### API de Actividad Comercial (ABM) — `apiCVU/Actividad`

- **Alta** — `POST /apiCVU/Comercio/Actividad`: crea una actividad comercial **a nivel PSP** con su comisión asociada. Código `6003` si la actividad ya existe para ese PSP.
- **Modificación** — `PUT /apiCVU/Actividad/{idPsp}/{actividad_comercial}`: modifica la **comisión** de una actividad existente. Código `6409` si el nuevo valor no es un rango válido.
- **Consulta por PSP** — `GET /apiCVU/Actividad/{idPsp}/{actividad_comercial}`: devuelve la comisión configurada y el `rango_comision` (`comision_minima`/`comision_maxima`) de esa actividad para ese PSP.
- **Consulta lista por PSP** — `GET /apiCVU/Actividad/{idPsp}`: lista todas las actividades comerciales del PSP con sus rangos.
- **Consulta lista global Coelsa** — `GET /apiCVU/Actividad`: lista todas las actividades comerciales definidas por Coelsa (independiente de PSP) con sus rangos min/max — esta es la tabla maestra de referencia.

> ⚠️ **Matiz técnico importante (aclaración necesaria para reconciliar dos fuentes):** el usuario indicó en conversación (2026-07-02) que "Coelsa solo permite una comisión por rubro para todo el PSP" y que la gestión es centralizada, no por comercio. La especificación técnica formal, sin embargo, muestra que **el endpoint de Alta/Modificación de Comercio sí acepta un campo `comisión` individual por comercio**, con la única restricción de que debe caer dentro del `rango_comision` (mínimo/máximo) que la actividad comercial tiene configurada a nivel PSP. Es decir: **la actividad comercial fija el rango permitido (a nivel PSP), pero cada comercio puede tener su propia comisión dentro de ese rango** — no es necesariamente una comisión única y fija por rubro, sino un techo/piso por rubro. La sección "Customizaciones al Circuito Actual" (más abajo) confirma además un mecanismo de **fallback en cascada**: si la comisión del comercio (`COM_COMISION`) es `NULL`, se usa la de su actividad comercial (`ACP_COMISION`). Esto es consistente con ambas explicaciones, pero deja abierta la pregunta operativa de por qué, en el caso real documentado en Parte 3 (comercio con mismo CUIT, comisión 0,8% vs. 0,05% declarada), no se aplicó la nueva comisión — posiblemente el campo no se seteó correctamente (quedó `NULL` y cayó al fallback de actividad) en vez de ser un rechazo por rango. **Gap registrado en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md)** para confirmar con el equipo cuál de los dos mecanismos rigió en ese incidente real.

### Tramo Gratuito (R01-03)

- Aplica a comercios de categoría **"CHICO"**.
- Duración: **3 meses calendario** desde el inicio de la operación.
- Tope: las transferencias acumuladas del comercio **no deben superar las 1.000 UVAS**.
- Se activa/desactiva mediante el campo `tramo_gratuito` en el endpoint de Modificación de Comercio (`PUT /apiCVU/Comercio/Comercio/{idPsp}/{cuit}`), reflejado en `COM_TRAMO_GRATUITO` de la tabla `CCVU_Comercio`.
- Esta definición alimenta directamente el cálculo de liquidación de comisiones (ver abajo): un comercio en tramo gratuito no paga interchange.

### Liquidación de Comisiones (R01-06)

- Coelsa ejecuta el cálculo **cada día hábil**, por fecha de negocio, con **horario de corte a las 17hs**. Toma las transacciones desde las 17hs del día hábil anterior hasta las 17hs del día en curso (fines de semana/feriados se acumulan hasta el siguiente día hábil).
- Para cada operación, valida que el comercio esté habilitado para PCT, deposita el **importe neto** (bruto - comisión) en la cuenta destino, y **reserva** el importe de interchange para distribuirlo al cierre del día.
- **Resolución de la comisión a aplicar (orden de prioridad):** 1) porcentaje definido en el alta del comercio (API); 2) si no está informado, el de la tabla de Actividad Comercial del PSP; 3) si tampoco está informado ahí, **default 0,8%**.
- **Clasificación del comercio (Categoría/Actividad):** se re-evalúa cada mes calendario en base a la recaudación del mes anterior por PCT; el aceptador debe informarla antes de las 16:55hs del primer día hábil del mes — esa clasificación rige todo el mes. Si no está informada, se toma `GRANDE`/`VARIOS` por defecto.

#### Reparto de comisiones por tamaño de comercio

| Categoría del comercio | Adquirente (Bind PSP) | Billetera |
|---|---|---|
| **CHICO** | 75% | 25% |
| **MEDIANO** | 50% | 50% |
| **GRANDE** | 25% | 75% |

- **La comisión de Coelsa es fija: 2,5% de la comisión total del comercio** (no del monto de la operación) — se descuenta primero, y el resto se reparte según la tabla de arriba.
- Concepto `ECT` (Extracción con Transferencia) **no paga comisiones de Interchange** — se trata como si fuera tramo gratuito.

#### Ejemplo numérico completo (del documento oficial)

Operación de **$100,00**, comercio categoría **GRANDE**, comisión del comercio **0,8% + IVA**:

| Concepto | Monto |
|---|---|
| Operación | $100,00 |
| Comisión total (0,8% + IVA) | $0,97 |
| **Neto que recibe el comercio** | **$99,03** |
| Comisión Coelsa (2,5% de $0,97) | $0,0242 |
| Resto a repartir (Adquirente 25% / Billetera 75%, categoría GRANDE) | $0,9438 |
| → Adquirente (25%) | $0,2360 |
| → Billetera (75%) | $0,7079 |
| Total comisión (Coelsa + Adquirente + Billetera) | $0,9680 ≈ $0,97 |

**En una devolución:** se reversan exactamente los mismos montos — débito de $0,7079 en el banco de la Billetera y crédito equivalente al Adquirente; débito de $0,0242 de la cuenta Coelsa y crédito al Adquirente.

### Pago de Comisiones a los Actores (R01-08)

- Tras la liquidación diaria, se realiza **un solo pago consolidado por actor** (Aceptador, Billetera, Coelsa) — la suma de todas las comisiones de la fecha de negocio.
- Se ejecuta como un **CASHOUT** al CBU configurado. Si el CASHOUT no se completa, queda en estado "no finalizado" y activa un mecanismo de excepción donde **Operaciones debe realizar el pago manualmente**.

### Conciliación (R01-05)

- Archivo estándar **"Conciliación DEBIN Fase 4 v5.0"** que Coelsa entrega a las entidades (ya operativo, se le agregaron campos para soportar Interchange).
- Nuevos tipos de movimiento agregados para Interchange:

| Código | Significado |
|---|---|
| RESCO | Rescate Comisión Coelsa |
| DEVRE | Devolución Rescate Comisión Coelsa |
| COMAD | Comisión Adquirente |
| DEVCA | Devolución Comisión Adquirente |
| COMBI | Comisión Billetera |
| DEVCB | Devolución Comisión Billetera |
| COMCO | Comisión Coelsa |
| DEVCO | Devolución Comisión Coelsa |

- El archivo de liquidación también incluye, por cada operación, flags y montos de **retención/percepción de IVA e IIBB** por cada actor (Aceptador, Billetera, Coelsa), con jurisdicción de IIBB — formato de registro posicional de longitud fija (430 caracteres), estructurado en Cabecera de Archivo → Cabecera de Lote → Detalle → Fin de Lote → Fin de Archivo. Se almacena en `root/PSP/{ID}/*.txt` o `root/BILLETERA/{ID}/*.txt`.

### Customizaciones al circuito actual (R01-07) — validaciones agregadas

- **`POST /apiDebinV1/QR/QRDebin`**: se agrega validación de que el comercio exista y esté dado de alta — si no, error **`7156 – COMERCIO INEXISTENTE`**.
- **`POST /Debin/ConfirmaDebito`**: se valida la comisión del comercio (`COM_COMISION` en `CCVU_COMERCIO`); si es `NULL`, se busca en `CCVU_ACTIVIDAD_COMERCIAL_PSP.ACP_COMISION`. También se revalida que el comercio esté activo — si no, error **`0562 – COMERCIO INACTIVO`**.
- **`POST [epPSP]/QRConfirmaDebito`**: se agrega el objeto `interchange` con `importe_bruto`, `importe_neto`, porcentaje y monto de comisión, tamaño del comercio, y porcentaje de comisión Coelsa.
- **Contracargos de comisión**: el Adquirente puede reclamar una diferencia (ej. en la comisión aplicada) vía **`POST /apiDebinV1/QR/QRSolicitudContracargo`**. Estos movimientos usan el mismo ID de operación con prefijo `DCA` (Devolución Comisión Adquirente), `DCB` (Devolución Comisión Billetera) o `DCC` (Devolución Comisión Coelsa).

### Comercio con arancel reducido en QR (menor a 0,6%) — MCC y CUIT de Bind PSP

> Fusionado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` en la reestructuración PARA en cascada (2026-08-12).

Registro de configuración real de comisiones reducidas para comercios propios de Bind PSP (Bind Pagos), por PSP y actividad comercial:

**PSP 184:** Bind Pagos (CUIT 30717449076) — actividad 829100-7321: comisión 0.05; actividad 829900-8999: comisión 0.8 (hoy 0.75 en Coelsa).
**PSP 164:** mismo CUIT — actividad 829100-7321: NO EXISTE COMERCIO EN COELSA; actividad 829900-8999: comisión 0.05.

Ver Parte 4 (arriba) para el mecanismo general de comisiones por actividad comercial y su rango mínimo/máximo.

---
*Ver también: [webhooks_y_notificaciones.md](webhooks_y_notificaciones.md) para cómo se notifica al comercio una vez que el cobro QR (bajo cualquiera de los modelos de esta Parte 3) se acredita.*
*Última actualización: 2026-08-12 — Fusionada sección de arancel reducido desde `configuracion_entidades_y_comercios.md` (reestructuración PARA en cascada).*
