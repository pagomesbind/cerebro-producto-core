# 🧾 Casos de Uso por Cliente — Bind PSP

> Fichas de contexto de producto por cliente, generadas desde los brochures de Notion ("Legajos de clientes"). Solo tienen ficha los clientes con contenido sustantivo (contenido de página más allá del template, o propiedad `STATUS Detallado` con texto). El listado completo de clientes vive en [log_clientes.md](log_clientes.md).
>
> **Formato de cada ficha:** mini-cabecera con propiedades + campos: Modelo de negocio · Status detallado (Comercial) · Cómo opera los productos · Pricing · Volúmenes/datos duros · Particularidades/cronología. Acá **no** se guardan datos identificatorios (CUIT, CBU, contactos) ni documentación legal.

<!-- Las fichas siguen el orden del log maestro (por grupo de estado, orden de creación en Notion). Se agregan por tanda durante la carga inicial y luego se mantienen vía /sync_customers (fuente primaria, Notion). /sync_meetings y /sync_mails complementan la sección "Particularidades / cronología" de fichas ya existentes con hallazgos de reuniones y mails (decisión del usuario, 2026-07-15) — nunca crean ni dan de baja clientes. -->

# EN PRODUCCIÓN + EVOLUTIVO

## DESARROLLOS DEL LITORAL (MCMoviles)
> Estado: En producción + Evolutivo en Intg · Productos: QRI, POS, Botón de Pago, RxT (→ Adquirencia) · Rubro: Impuestos y Servicios, Recargas · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-05-26 · Fuente: https://app.notion.com/267bbcfd4b8340aea4155508e494acbc

**Modelo de negocio:** red de cobranza tipo **Pago24** (Santa Fe, Entre Ríos, Córdoba) — recarga de celulares/SUBE y cobranza de impuestos y servicios por cuenta y orden de terceros con **convenios propios** (arancel reducido por recaudar impuestos/servicios). ~4.000 puntos de venta activos (kioscos con negocio anexo).
**Cómo opera:** todos los ~30 comercios bajo el CUIT de Desarrollos del Litoral, liquidación única a su CBU; sucursales y cajas reales creadas por Portal Web; comercios/agencias usan el Portal Web, la entidad usa el Admin; POS logueables con el mismo usuario de caja.
**Volúmenes:** facturación mensual $4.500-5.000 millones, 25-30% vía Bind PSP, mayoría por QR.
**Pricing:** QR 0,8% · POS TC/prepaga 1,75% · TD 0,75% · setup integración USD 3.000 · mínimo mensual USD 2.500 · módulo Agrupador bonificado. Plazos: PCT inmediato, transferencia 24hs, TD 48hs, TC 18 días.
**Particularidades / cronología:** 11/06 pide sumar RxT (adenda pendiente); comercio de venta presente con arancel reducido para impuestos (código 1920); mayo-2026 evalúan (y luego descartan) sumar POS para otra empresa mayorista del mismo grupo ("Emprendimientos Móviles").

## La Virginia
> Estado: En producción + Evolutivo en Intg · Productos: Wallet, Onboarding, POS (→ Wallet + Onboarding + Adquirencia) · Rubro: Retail · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-06-08 · Última edición (Cerebro): 2026-08-06 · Fuente: https://app.notion.com/18bb3646c94b803096d4cd40a737309d

**Modelo de negocio:** cadena retail (16 sucursales, +300 productos) con **billetera digital propia de ecosistema cerrado**: todo lo acreditado en la CVU de personas físicas/jurídicas queda como crédito para compras dentro de La Virginia. Evolutivo: **app de repartidores** — cada repartidor tiene su propia "Caja" con QR estático de monto cerrado, todas asociadas al mismo comercio/CVU de La Virginia; flujo con Daxia como integrador (orden de cobro → webhook con ID de caja/orden → identificación del repartidor y la factura).
**Cómo opera — Onboarding:** para personas físicas lo hace Bind (app + recolección de documentación); para personas jurídicas Bind no tenía circuito diseñado — abr-2026 el cliente rechaza seguir usando el OB PJ de Bind (frustración con el producto) y evalúan alternativas (google forms rechazado por PLD, batch, proceso manual).
**Pricing:** licencia PSP mensual USD 3.500 · Onboarding USD 0,3 · CVU mensual USD 0,05 · cash in/out 0,25% (mín $50, máx $250). **Cuenta Remunerada** (FCI): setup USD 10.000 (3 cuotas) + fee mensual USD 2.000 + retrocesión del 30% de la comisión neta que Bind cobra al proveedor de inversión.
**Particularidades / cronología:** abr-2026 factura USD 3.500 (abono) + USD 157,05 (Wallet service); FCI en discovery con Daxia (ene-2026), credenciales de PROD en curso (jun-2026). **2026-07-24:** avanza el bridge operativo del OB PJ rechazado en abril — mientras no exista automatización batch (ETA fin de septiembre 2026), el alta de cuentas comitentes pendientes (~100 hoy, hasta 1.400 en total) se hace manualmente a partir del ID de cuenta, con una herramienta de soporte en construcción (ver [`detalle_productos/onboarding/manuales_operativos.md §5`](../../3_recursos/detalle_productos/onboarding/index.md)). **2026-08-05 (reunión "OB PJ"):** el problema de fondo del OB PJ rechazado en abril se cuantifica — de ~120-250 intentos de alta, solo el 5% (12) resultó exitoso; el cliente tiene **2.000 personas jurídicas pendientes de dar de alta** y no se anima a salir a producción con el flujo actual (riesgo de pérdida del cliente). Se aprueba un nuevo flujo: un oficial de negocio de La Virginia (whitelist de 15 personas) carga la documentación en lugar del cliente final, con MVP comprometido a 1 mes (ver [`detalle_productos/onboarding/manuales_operativos.md §6`](../../3_recursos/detalle_productos/onboarding/index.md) y `tareas_producto.md` T-086). **2026-08-06:** el discovery de este rediseño se trackea como proyecto dedicado — ver [`proyecto-la-virginia-ob-pj`](../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md).

## OCTAGON
> Estado: En producción + Evolutivo en Intg · Productos: QRI, Wallet, Onboarding (→ Adquirencia + Wallet + Onboarding) · Rubro: Agente de cobros y pagos · Tamaño: Pequeño · Riesgo: Medio · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/1bcb3646c94b80968f4ce5c901f738ae

**Modelo de negocio:** billetera digital para **PyMEs y autónomos** — plataforma web para transacciones online (transferencias, DEBIN, pagos/cobros QR) y **retiro de efectivo en cajeros (ATM) sin tarjeta**: el usuario muestra un QR de Bind en el ATM y extrae efectivo (une "mundo presente y no presente"). Modelo alternativo: una estación de servicio fondea el ATM con cash físico y Octagon acredita en la CVU de la estación para compensar. Etapa 2 evaluada: tarjetas prepagas para PyMEs, avales para venta de cheques (solo canal de comercialización, sin transacción real), FCI y compra de dólares.
**Cómo opera:** usa el OB de Bind (PF y PJ) mientras desarrolla uno propio; un OB exitoso da de alta cuenta+CVU+comercio vinculado. Tope PLD por CUIT en QR Aceptador: $2.000.000.
**Volúmenes (proyección):** 200 cuentas a 6 meses / 500 a 12 meses; saldo promedio acumulado $7M/$16M; 4.000/10.000 trx mensuales; 1.600/3.000 trx en cajeros.
**Pricing:** QR 0,80% · OB PF USD 2 · OB PJ USD 3.
**Particularidades / cronología:** 11/06 Cuenta Remunerada en standby · 18/06 Bind autoriza a Octagon a usar su API de validación RENAPER desde OB propio · 25/06 se da de baja el servicio de Cuenta Remunerada (van con otro proveedor) · 02/07 Octagon migrará su OB a integración directa con RENAPER, dejando de usar el de Bind (requerirá re-validación PLD) · **19/08:** Bind hace una demo completa del flujo de onboarding propio (persona jurídica) a representantes de Octagon y al equipo de **Compliance de Banco Industrial** (banco vinculado a la operatoria de Octagon) — el equipo de Compliance de Banco Industrial pidió acceso directo a la plataforma de onboarding para auditar el legajo digital de los clientes sin solicitar la documentación manualmente, y Bind acordó otorgarlo. Se definió además avanzar en un "paquete de datos" para automatizar (post-aprobación del onboarding) la creación de la CBU y el alta del comercio en los sistemas de Bind — hoy ese paso es manual. Ver detalle técnico completo de la demo en [`detalle_productos/onboarding/onboarding_personas_juridicas.md §8`](../../3_recursos/detalle_productos/onboarding/index.md).

## Encode
> Estado: En producción + Evolutivo en Intg · Productos: Botón de Pago, QRI, RxT (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-09-02 · Fuente: https://app.notion.com/1c8b3646c94b80f788e0f40fbdffd691

**Modelo de negocio:** certificaciones de firma digital usadas principalmente por **entes estatales**; el pago del trámite lo realiza el usuario solicitante vía Botón de Pago, RxT o QR.
**Status detallado (Comercial):** 11/08 integrando Botón de Pago.
**Pricing:** RxT 0,5% · TD 2,5% · TC 2,5% · QR 0,80% · TP (prepaga) 2,5% sumada set-02/2025.

## Cuoma (Pax Manager)
> Estado: En producción + Evolutivo en Intg · Productos: Botón de Pago, QRI, RxT (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Grande · Riesgo: Bajo · Última edición (Notion): 2026-06-11 · Fuente: https://app.notion.com/25db3646c94b80eaa4dfca7084682787

**Modelo de negocio — "modelo Gallo" de integrador (⚠️ no es el cliente final):** plataforma de gestión para empresas de **turismo estudiantil** (clientes: Baxter, Travel Rock, Freestyle y ~20 empresas más). Cuoma **no es cliente de Bind**, es el integrador — cada empresa usuaria de Cuoma firma su propio acuerdo con Bind para usar la solución de cobros, y Cuoma recibe una porción de lo cobrado como comisión de integrador.
**Pricing (revenue share con Cuoma):** setup 10% del bruto cobrado por Bind a cada cliente (mín. USD 3.000 por cliente, única vez) · QR: Cuoma recibe 20% del bruto (arancel mínimo 0,8%) · TC: 20% (mín. 2,5%) · TD: 20% (mín. 1,5%) · RxT: 25% (mín. 0,35%).
**Particularidades:** 3/11 se crean credenciales PROD para que Cuoma como entidad consuma RxT directamente. Ver también fichas TRAVEL ROCK y Freestyle (clientes de Cuoma).

## Global PIX
> Estado: En producción + Evolutivo en Nego · Productos: Botón de Pago, QRI, POS, Onboarding, Wallet (→ Adquirencia + Onboarding + Wallet) · Última edición (Notion): 2025-07-21 · Fuente: https://app.notion.com/21fb3646c94b80f5b8bdfdef6c47e062

**Status detallado (Comercial):** 14/07 — en producción, negociando servicios nuevos adicionales.

# EN INTEGRACIÓN

## INTER
> Estado: En integración · Productos: Wallet, Dolar CCL (→ Wallet + FX) · Última edición (Notion): 2025-12-02 · Fuente: https://app.notion.com/13db3646c94b808aa5a8fb650fd00936

**Modelo de negocio:** banco/broker brasilero (**Inter Securities / Banco Inter**) integrando Wallet y compra de dólar CCL — partnership regional de escala.
**Pricing:** margen de spread del 2% sobre TC, repartido 75% Inter / 25% Sr. Bind (del 25%: 20% Bind PSP, resto IVSA); mínimos garantizados los primeros 3 años.
**Particularidades / cronología:** múltiples acuerdos a firmar (Marco, Sign Letter, Aagi, PSP/IVSA, Bind UY) con distintas sociedades del grupo Inter — requiere revisar con cuál firma cada acuerdo.

## RGM (Red Global Monetaria)
> Estado: En integración · Productos: Botón de Pago 2.0, Botón de Pago, QRI (→ Adquirencia) · Tamaño: Mediano · Última edición (Notion): 2026-05-28 · Fuente: https://app.notion.com/716182d74e6a4de2b84face87560815d

**Modelo de negocio:** red de cobranzas de **Banco Columbia**, recauda para las entidades con acuerdo: Cuotitas SA, Meplife Salud, Asoc. Mutual de Trabajadores Argentinos Estatales, Asoc. Mutual 13 de Mayo.
**Volúmenes:** ~30.000 trx/mes, ~$1.500.000.000.
**Pricing:** TD 0,7% (48hs) · TC 1,65% (18 días) · prepaga 1,65% (18 días) · QR 0,75% (24hs) · RxT 0,39% (24hs). Requieren arancel reducido para sus códigos de comercio.

## PIX GLOBAL
> Estado: En integración · Productos: Onboarding, Wallet, QRI (→ Onboarding + Wallet + Adquirencia) · Rubro: Billetera · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2024-12-17 · Fuente: https://app.notion.com/af7a9218966842edb5adcaaee003a498

**Modelo de negocio:** uso de rieles PSP de Bind para aceptar pagos **PIX (Brasil)** en comercios argentinos.
**Pricing:** personalización/implementación USD 1.500 · Onboarding USD 0,60/proceso, mínimo facturación USD 1.000/mes.

## APPLIKO
> Estado: En integración · Productos: QRI (→ Adquirencia) · Rubro: Agente de cobros y pagos · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/154b3646c94b809995cefd0504c9f07c

**Modelo de negocio:** plataforma de cobranza que también da servicio a **Telwinet** (mismo dueño). Recauda en su CBU de Banco Industrial y acredita a cada comercio post-conciliación. QR disponible presencial en sucursal y digital en las facturas.
**Volúmenes:** 12.000 clientes, ~$360.000.000, ticket promedio $30.000.
**Status detallado (Comercial):** proceso largo — 16/07/25 contrato firmado, setup pago · varios meses de idas y vueltas con carta oferta y compliance · 12/03/26 contrato firmado · 25/06/26 aún pendiente validación PLD final antes de pedir pase a PROD.
**Pricing:** QR 0,8% en línea.

## BNKA (Block Digital Services SA)
> Estado: En integración (con período frenado por el cliente) · Productos: Wallet (solo lectura de QR) · Rubro: Billetera · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-05-26 · Fuente: https://app.notion.com/168b3646c94b80d4823aee1b0587d465

**Modelo de negocio:** billetera virtual multi-país para freelancers y estudiantes (cambio de monedas, tarjetas internacionales, pago de servicios). Tiene **licencia PSP propia** con Banco Industrial (Bind) como banco sponsor. Bind **no** provee CVUs a los usuarios de BNKA — solo el servicio de **lectura de QR**: BNKA debe crear y fondear una CVU propia desde la cual se ejecutan los pagos QR de sus usuarios.
**Volúmenes:** estimado $50.000.000/mes, 10.000 trx, ticket promedio $5.000.
**Pricing:** setup USD 3.000 (3 cuotas) · arancel iniciador para Bind por cada pago QR · mínimo mensual escalonado USD 500 (meses 1-3) → USD 2.000 (desde mes 13).
**Particularidades / cronología:** 14/07 frenado por el cliente · set-2025 acuerdo y manual de APIs enviados · 18/02/26 OK informal de PLD · 27/03/26 contrato firmado.

## CB Pay
> Estado: En integración · Productos: Agente de Cobros y Pagos · Rubro: Cripto, Billetera · Tamaño: Mediano · Riesgo: Alto · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/17bb3646c94b80d191aadfd0e619e777

**Modelo de negocio:** wallet crypto-fiat chilena (Grupo CB) para pay-in/pay-out entre usuarios — modelo mesa OTC (USDT→fiat, giro Chile↔otros países) + modelo retail tipo Lemon (compra de USDT/BTC, manejo en moneda local). Necesitan un **dispersor** que baje USDC a pesos/dólares argentinos vía CCL/USDT.
**Cómo opera — dos alternativas evaluadas:** (a) **Agente de CyP simple**: una cuenta única o CVUs solo para conciliar cash-in (sin onboarding de usuarios, el cash-out lo maneja la entidad); (b) **PSP as a Service/Wallet Services**: licencia PSP de Bind con CVU de libre disponibilidad por usuario (requiere onboarding completo de cada uno).
**Status detallado (Comercial):** 14/07 credenciales en PROD.

## Tecnoaccion
> Estado: En integración · Productos: Botón de Pago, QRI, RxT, Agente de Cobros y Pagos (→ Adquirencia + Agente de CyP) · Rubro: Gambling · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2025-12-12 · Fuente: https://app.notion.com/1c8b3646c94b80a8a387dff297bafee0

**Modelo de negocio:** operador de **loterías provinciales** (Santiago del Estero, Neuquén, La Pampa, Santa Cruz, La Rioja, Catamarca, Tierra del Fuego, Corrientes, Río Negro, Jujuy, Salta con licencia exclusiva — 900+ puntos de venta) y del sistema de apuestas hípicas del **Hipódromo Argentino de Palermo** (integración con el totalizador).
**Cómo opera — plataforma "ilotery":** etapa 1, Onboarding + validación de titularidad para usuarios (el flujo NO termina en alta de CVU/comercio); 11 provincias → 22 entidades (11 de alta con OB completo sin CVU, 11 de retiro solo con validación contra listas). Etapa 2 (futura): soluciones de cobro (RxT/Botón/POS/QR) para recaudar apuestas de loterías provinciales, juego online y agencias. **Tecnoacción 2** (proyecto separado, nov-2025): validación de DNI/mayoría de edad para apuestas presenciales de lotería (SAA, vía QR ya que Bind no presta Renaper solo) y OB+validación de vida para pago de premios en la app **LotLine**.
**Pricing:** setup USD 5.000 · OB sin biometría USD 0,6 · OB con biometría USD 1,1 · validación de titularidad $50.
**Status detallado (Comercial):** 12/12 contrato firmado.

## Maxiconsumo
> Estado: En integración · Productos: QRI, RxT, Wallet (→ Adquirencia + Wallet) · Rubro: Retail · Última edición (Notion): 2025-10-08 · Fuente: https://app.notion.com/1c8b3646c94b80dbb516c28b24a1218a

**Modelo de negocio:** mayorista retail — etapa 1 QR "modelo de cercanía" (N comercios, cada uno con su propio CUIT/CBU, acreditación con split), etapa 2 "modelo Kellerhoff" (N comercios todos con CUIT/CBU del cliente central), etapa 3 Wallet Services eco cerrado (futura).
**Status detallado (Comercial):** 28/08/25 — Solo QR (0,6%) integrado a sus propias cajas (no se lo dan a mayoristas), 100% vía API, en homologación; Wallet para etapa futura · 08/10/25 — QR Aceptador integrado, faltan pruebas; WS recién arrancando.
**Pricing:** QR 0,6%.

## COPPEL
> Estado: En integración · Productos: Wallet, Onboarding (→ Wallet + Onboarding) · Rubro: Retail · Tamaño: Grande · Última edición (Notion): 2026-06-08 · Fuente: https://app.notion.com/209b3646c94b80078826f1ef66f60dae

**Modelo de negocio:** retail con financiamiento al consumo (préstamos personales, pago de servicios, tarjetas prepagas). La **billetera virtual** da a cada cliente una CVU para centralizar pagos, retiro de efectivo, consumo con tarjeta y **recepción inmediata de préstamos otorgados**. Bind (PSP y Banco) solo provee infraestructura de cuentas — el lending completo (aprobación, fondeo) lo gestiona Coppel exclusivamente.
**Cómo opera:** en producción con Wallet, integrando QR, avanzando con **Cuenta Remunerada (FCI)** propia (abandonaron la intención de integrarse con Delta). Requisito del cliente: la TNA ofrecida al usuario debe igualar la de Mercado Pago (±0,01 pb) — implica resignar revenue share o subsidiar rendimiento.
**Pricing:** abono mensual USD 3.000 (desde puesta en PROD) · setup USD 5.000 · cash in/out 0,4% · costo fijo por CVU activa USD 0,05/mes · lectura QR 0,20% · mínimo mensual USD 4.500. (Propuesta alternativa con Delta: setup USD 5.000, abono USD 2.500.)
**Particularidades / cronología:** dic-2025 en PROD con Wallet, integrando QR; may-2026 pruebas de FCI con IVSA, salida a PROD 18/05; PLD dio OK para acreditación de préstamos personales en CVU (20/05); jun-2026 negociación del flujo de revenue share de Cuenta Remunerada, avance con QR Aceptador.

## Sociedad Militar (SMSV)
> Estado: En integración · Productos: Wallet · Rubro: Billetera · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-06-03 · Fuente: https://app.notion.com/211b3646c94b80ee9bbde743d1c4d41c

**Modelo de negocio:** billetera para asociados de una sociedad militar (~40.000 CVU esperados). La CVU de SMSV funciona como **cuenta rampa/puente** para movimientos internos (no alcanzada por impuesto a débitos y créditos); la CVU del asociado, donde "pica" el dinero en cada transacción, sí tributa. Mismo flujo de cobro de impuestos que **COOP UNION**.
**Cómo opera — flujo IN:** transferencia externa entra a la CVU del asociado → transferencia interna debita al asociado y acredita en la CVU de SMSV → SMSV transfiere externamente a su propia CBU (desfondeando la CBU recaudadora del PSP). **Flujo OUT:** inverso.
**Status detallado (Comercial):** 14/07 en espera de firma de contrato, ya integrando · 12/12 sigue esperando firma · abr-2026 diseño del flujo de impuestos (misma lógica que Coop Unión) · may-2026 migran ~80 cuentas de colaboradores (~600 totales), luego socios; piden SLA de soporte en el contrato.

## VUPRA
> Estado: En integración · Productos: POS, Botón de Pago 2.0 (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Mediano · Última edición (Notion): 2026-05-11 · Fuente: https://app.notion.com/242b3646c94b8037ae0ae5452ca2ba2c

**Modelo de negocio:** integrador tecnológico para la **DNRPA (Ministerio de Justicia y DDHH)** — cobros de trámites vía Botón Simple 2.0/POS, operando bajo el mismo patrón "comercio con CUIT de un tercero" ya visto (aquí, **RIPSA** presta el CUIT/razón social, nombre de fantasía DNRPA).
**Status detallado (Comercial):** 11/08 en análisis de flujo, en espera de licitación; luego largo ciclo de bugs de integración de Botón Simple 2.0 resueltos entre abr-may 2026 (deudas vencidas sin conciliar, endpoint de detalle de productos, IDs de comercio).
**Pricing:** RxT 0,05% + IVA · TD 0,58% + IVA (4 días) · TC 1,28% + IVA (10 días) · QR 0,36% (mismo día).

## GST (ERP de gambling) — Hipódromo de Palermo
> Estado: En integración · Productos: Onboarding, Wallet, QRI (→ Onboarding + Wallet + Adquirencia + Agente de CyP) · Rubro: Gambling · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2026-06-12 · Última edición (Cerebro): 2026-08-04 · Fuente: https://app.notion.com/245b3646c94b80b8ab76c13a8fc3ac36

**Modelo de negocio:** proveedor tecnológico de un ERP de apuestas presenciales (similar a Tecnoacción pero en el mundo presente); clientes: Hipódromo de Palermo, Grupo DACMA, Lotería de Río Negro, Casino Club, Casino de Mendoza, Casinos Río, Golden Jack. Para "Socios del Club" de la app de GST: Wallet da una CVU a cada usuario, con **dos saldos** (CVU y saldo de juego) — el usuario convierte pesos en puntos de juego (comprar puntos) y viceversa cuando gana un premio (con análisis PLD del "blanqueo" de pesos). En las máquinas de slots reemplazan el QR de **TotalCoin** por el de Bind (requerimiento de Bind, no del cliente) para dar volumen a la app.
**Cómo opera — dos cuentas recaudadoras:** (1) Cuenta Rec Wallet: suma de saldo CVU + saldo de juego, con umbral de posición neta ($5M) validado por PLD y transferencia diaria del remanente; (2) CBU Agente de CyP: recibe la conversión CVU↔juego, la liquidación de QR (24hs), y paga cross-border/nacional a las empresas de la **UTE** que conforma el Hipódromo (con distinto tratamiento impositivo según residencia).
**Volúmenes:** Netwin $17B, venta total $51B, cash-in estimado app $10B (20% de venta). Estimación app: 30.000 usuarios/mes, cash-in $70M/mes, cash-out $39M/mes.
**Pricing:** setup USD 20.000 · licencia PSP mensual USD 10.000 · CVU activa USD 0,5 · cash in/out 0,3% · lectura QR bonificada · QR 0,7% · módulo Agente de Pagos: mínimo USD 35.000, pago de premios 0,5%, cross-border 1%.
**Particularidades / cronología:** 15/07/26 (reunión "Join Soporte Clientes") — el cliente (bajo el nombre "Hipódromo") reporta complicaciones con su integración de GST y percibe falta de soporte adecuado; el equipo técnico está dedicado a resolver los inconvenientes reportados.
- **2026-08-04 (reunión "Repaso Semanal líderes"):** planean integrar QR en las máquinas de slots, lo que **duplicará en el corto plazo el volumen transaccional de QR** del cliente. Bind se compromete a proveer herramientas administrativas para reducir la dependencia técnica del cliente y facilitar su autogestión. Motivó además el pedido de stress test del módulo de cobros (Melisa Belpassi) para anticipar el aumento de volumen — ver `wallet/otros_manuales.md §13`.

## INFINIA
> Estado: En integración · Productos: Agente de Cobros y Pagos · Tamaño: Grande · Última edición (Notion): 2026-02-26 · Fuente: https://app.notion.com/24fb3646c94b807c87fdc28845e65e91

**Perfil corporativo:** fintech uruguaya de infraestructura de pagos (fundada 2022, CEO ex-equipo fundador de dLocal, alumni de Y Combinator W23, inversores incl. Y Combinator/Decacorn/Flucas/Kube VC) — "tubería" que conecta bancos con infraestructura digital (on/off-ramp bancario↔cripto/stablecoins) en Argentina, Brasil, Uruguay.
**Modelo de negocio:** partner de **Bridge** (a su vez partner de Stripe); Bind recolecta pesos, se los pasa a **Manteca** (o dólares vía FV Bank), y Manteca entrega USDC a Infinia. Detrás de Infinia opera **Despegar** como cliente final.
**Riesgo/Compliance:** riesgo inherente alto (AML/financiamiento del terrorismo por operar en la intersección bancaria/cripto); mitigación vendida como producto (KYC, validación bancaria en tiempo real, listas OFAC). PLD evalúa merchant por merchant a los subclientes de Infinia: **Pockyt** (pasarela de creadores de contenido) rechazado; **Jeeves, Tuyo, Open FX, ugly.cash** rechazados por PLAFT (feb-2026).
**Volúmenes proyectados:** USD 2M/mes → USD 6M → USD 50M a fin de año.
**Pricing:** fijo mensual en discusión (USD 10.000 propuesto por Bind, alternativas de USD 5.000 o 2.500 con mayor variable).
**Particularidades / cronología:** feb-2026 el flujo de recolectar pesos y expatriar (vía Bridge/Stripe) está OK; el flujo inverso (recibir USD afuera y liquidar pesos en Argentina) aún no.

## Terra BlockChain (Gallo)
> Estado: En integración · Productos: Wallet · Rubro: ALyCs · Tamaño: Pequeño · Riesgo: Medio · Última edición (Notion): 2026-07-06 · Fuente: https://app.notion.com/250b3646c94b80418cd3db7664224fa7

**Modelo de negocio:** usa la plataforma Wallet de **Gallo** para generar una CVU a cada usuario de Terra — "modelo simil IEB" (mismo esquema white-label que otros clientes del ecosistema Gallo).
**Status detallado (Comercial):** 12/12 Gus conversa con Gallo por este cliente · PLD OK 18/12/2025 (restricción: no puede operar con arbitrajistas de activos virtuales ya relevados negativamente, ni los que no operen entre cuentas propias).
**Particularidades / cronología:** 2026-07-29 (reunión "Join Soporte Clientes") — revisión de riesgo detecta irregularidades en el proceso de vinculación y falta de justificación en los movimientos, con alto volumen de reclamos de PLD. Compliance solicitó el legajo completo y está validando la firma de los apoderados; si no se confirma que el alta se hizo correctamente, se evalúa el cierre de las cuentas. Sujeto además al nuevo tope operativo mensual de $300.000.000 para personas jurídicas (ver `decisiones.md`, 2026-07-29).

## FIDEICOMISO PRIVADO CENFIDE (ex Centaurus)
> Estado: En integración · Productos: QRI, RxT, Botón de Pago (→ Adquirencia + Agente de CyP) · Rubro: préstamos de consumo · Tamaño: Pequeño · Última edición (Notion): 2026-07-06 · Fuente: https://app.notion.com/26bb3646c94b80a69e48c8f3fd9d03b3

**Modelo de negocio:** idéntico a CREDITIA Fideicomiso Financiero (ver ficha) — cobro de deudas de terceros adquiridas por el fideicomiso, con el mismo ciclo de vida de CVU por deudor (depuración al cancelar/rotar de agencia).
**Volúmenes:** ticket promedio $190.000, ~737 trx promedio.
**Pricing:** QR 0,8% (1 día) · TD 1,75% (2 días) · TC 2,5% (20 días) · RxT 0,3% (1 día) · Ag CyP bonificado (máx 1-2 transferencias/día).
**Particularidades / cronología:** proceso de compliance largo — 12/03/26 contrato firmado · 21/04 PLD pide APF extendido · 22/05 enviado · 26/06 cambio de nombre Centaurus→Cenfide · 06/07 **conformidad de PLD**.

## Super Tour ⚠️ (página duplicada, confirmada vacía — ver gaps)
> Estado: En integración · Productos: RxT · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-09-30 · Fuente: https://app.notion.com/277b3646c94b8041be28d0a1beadecc2

Página confirmada **en blanco** (sin contenido). Duplicado exacto de la fila "En producción" de Super Tour (ver ficha arriba en la sección En Producción, `27eb...ddac`) — mismo Cliente, ambas creadas la misma tarde de sep-2025.

# EN NEGOCIACIÓN

## BEM
> Estado: En negociación · Productos: Wallet · Rubro: Cripto · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/18ab3646c94b80f5b54bebc06719b9bc

**Modelo de negocio — matching de mercado FIAT/Cripto:** el cliente A fondea una CVU desde Bind (pata FIAT, sin admitir acreditaciones de terceros); el cliente B fondea una Wallet Address BEM (pata cripto). Cuando hay match en la plataforma BEM, se bloquean fondos FIAT-Cripto y se compensa la operación; al cierre de mercado, tanto la custodia cripto como la CVU deben quedar en cero. Es decir, Bind provee la infraestructura FIAT de un exchange/matching engine de criptoactivos.

## BINANCE
> Estado: En negociación · Productos: Wallet (+ Agente de CyP, RxT, QR, emisión de prepaga con Pomelo) · Rubro: Cripto · Tamaño: Grande · Última edición (Notion): 2026-04-15 · Fuente: https://app.notion.com/1a4b3646c94b8082ab59c797660ec0d6

**Modelo de negocio:** la cuenta se usa exclusivamente para **comprar saldo en Binance** (aclarado tanto en TyC como en el detalle de cada transacción). Límites operativos: 5 trx/día, USD 3.000/mes máx., equivalente a $24.000.000/año (superado esto, se pide información adicional) — tope estimado USD 18.500 anuales del lado de Binance.
**Particularidades:** evalúan además emisión de tarjeta prepaga con **Pomelo**. abr-2026: contrato pendiente de validación legal.

## PLATABUS
> Estado: En negociación · Sin más contenido sustantivo · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/1ddb3646c94b8060851ae56d76c75a83

## Lotería de San Luis
> Estado: En negociación · Sin más contenido sustantivo · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/230b3646c94b80f78fc2fc0aa352830a

## EDETSA
> Estado: En negociación · Productos: QRI, Botón de Pago, POS, RxT (→ Adquirencia) · Tamaño: Grande · Última edición (Notion): 2025-09-03 · Fuente: https://app.notion.com/23bb3646c94b8006b720e64fa25fd0f8

**Modelo de negocio:** distribuidora de energía eléctrica de toda la provincia de **Tucumán**, con 24 oficinas de cobranza (fuerte hábito presencial de pago en caja). Hoy usa QR de Mercado Pago, tarjetas Payway, RxT de ICBC (ICBC Multipay) y de Macro (ex ITAU), y convenios con Redex — costos promedio 1-1,5%. Candidato fuerte a **arancel reducido siendo Bind PSP la Redex** (ya tiene cuenta en Banca Empresa de Tucumán).
**Status detallado (Comercial):** 11/08 en espera de reunión con Banca Empresa de Tucumán.

## Ebury
> Estado: En negociación · Rubro: cross-border · Última edición (Notion): 2025-09-03 · Fuente: https://app.notion.com/23eb3646c94b800385c3c61071c35fbf

**Status detallado (Comercial):** 28/07 — es cross border, empresa con agrupador de Brasil; están por hacer una prueba con un cliente argentino, a la espera de que el cliente indique cómo avanzar y de que Bind envíe la propuesta comercial.

## Chango MAs
> Estado: En negociación · Sin más contenido sustantivo · Última edición (Notion): 2025-09-03 · Fuente: https://app.notion.com/245b3646c94b800e8678e359a6cf3eaf

## Tap Tap Send
> Estado: En negociación · Productos: Agente de Cobros y Pagos, Wallet, Onboarding · Rubro: Billetera · Tamaño: Mediano · Riesgo: Alto · Última edición (Notion): 2026-02-03 · Fuente: https://app.notion.com/24cb3646c94b800ea986dae7d57acfff

**Modelo de negocio:** app de **remesas internacionales** (fundada 2018, +12M usuarios, foco en África/diáspora, fuerte en Brasil y Colombia en LatAm; tesorería centralizada en Londres). Modelo IN: alguien del exterior envía una remesa a un cliente argentino → Bind da al receptor argentino una **CVU** (con Onboarding propio de Bind) y este transfiere/retira. Evalúan también que Tap Tap Send deje USD en el exterior y pida a Bind la **dispersión de pesos** a los beneficiarios en Argentina (Agente de CyP).
**Status detallado (Comercial):** 11/08 core de servicio es envío de remesas · 12/12 contrato firmado, en DDL (due diligence legal).
**Pricing:** setup USD 15.000 · abono mensual licencia PSP USD 3.000 · cash-in transferencias 0,35% · payout nacional 0,35% · payout internacional escalonado 1% (hasta USD 1M) → 0,8% → 0,6% → 0,5% (+USD 6M) · liquidaciones internacionales (CCL) 0,15%.

## Inviu
> Estado: En negociación · Productos: Wallet · Rubro: ALyCs · Tamaño: Pequeño · Riesgo: Medio · Última edición (Notion): 2025-08-11 · Fuente: https://app.notion.com/24cb3646c94b807cb866d6f55c6490da

**Status detallado (Comercial):** 11/08 se envió propuesta.

## GlobalFarm
> Estado: En negociación · Productos: Agente de Cobros y Pagos · Rubro: Retail · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2025-09-03 · Fuente: https://app.notion.com/25db3646c94b80a2bb79f85662c8479b

**Modelo de negocio:** distribuidora farmacéutica (Globalfarma) que agrupa la cobranza de ~25 droguerías clientes, cada una con su propio **CVU (RxT)** para pagar por transferencia; los montos quedan en la cuenta recaudadora de Bind y diariamente Globalfarma instruye transferencias a los laboratorios proveedores — algunos pagos incluso al **exterior** (medicamentos de importación).
**Pricing:** cash-in 0,65% · cash-out nacional 0,65% · cash-out internacional 1% · rendimiento del FCI sobre saldos en la cuenta recaudadora compartido 50/50.

# FRENADO

## BLOX CROSS
> Estado: Frenado (por el cliente) · Productos: Agente de Cobros y Pagos, Agente de Pagos · Rubro: Cripto · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2025-08-11 · Fuente: https://app.notion.com/13db3646c94b807aa3ecd1f04cdac331

**Status detallado (Comercial):** 11/08 frenado por parte del cliente.

## CAJERO 24
> Estado: Frenado · Rubro: soluciones de pagos digitales · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/43a0d5f3cb354f019b455493f8126179

**Pricing:** QR 0,8%.
**Status detallado (Comercial):** 10/07 para revisión.

## COCACOLA ANDINA
> Estado: En licitación activa (reactivada) · Productos: Wallet, Onboarding, Monitoreo (→ Wallet + Onboarding + Adquirencia) · Última edición: 2026-07-23 · Fuente Notion: https://app.notion.com/13eb3646c94b803aa243f2d61a7ddea3

**Modelo de negocio:** licitación pública de **billetera virtual marca blanca (WaaS)** — Bind se presentó como oferente.
**Status detallado (Comercial):** 14/07 en stand-by del cliente, profundizando pruebas con **IniPay** (competidor) · 15/04/26 Bind presentó propuesta técnica y económica a la licitación. Cronograma: consultas hasta 25/03/26, entrega de ofertas 15/04/26, inicio de servicio previsto 01/12/26. Contrato de 24 meses + 12 de renovación.

**Actualización 2026-07-23 (reuniones "Reunión iniciada 09:42" + "andina", minuta Gemini):** la licitación se reactiva con una instancia de demo funcional donde Bind compite directamente contra otros oferentes ("hemos hecho esta instancia con los demás oferentes y que algunos mostrar cosas, algunos no"). El cliente pide separar la app financiera de su aplicativo B2B actual en dos aplicaciones independientes (mobile + web, mayor volumen por mobile). Requisitos explícitos de la agenda del cliente para la demo (10 minutos asignados): alta de usuario, validación de identidad, pagos, transferencias, gestión de reclamos y configuración de promociones (estas dos últimas fuera del alcance actual — quedan como roadmap a comprometer con insumos del cliente) — además demo de consola de administración/monitoreo/CRM, del módulo de prevención de fraude (reglas configurables, alertas, bloqueos — herramienta **Ardid**, referenciada como "Arbit" en la minuta por error de transcripción), y preguntas de continuidad (RTO, esquema de comunicación ante incidentes) e integración con SAP. Storytelling de demo acordado para la sesión definitiva: onboarding por link único (PF, paleta de colores Coca-Cola) → alta de wallet + comercio → app (APK Android, no se publica) → portal de comercio (transferencias, saldo, movimientos, inversión, compra de moneda extranjera) → POS con color rojo Coca-Cola (mismo usuario, QR + acreditación en línea) → Ardid (regla de monto máximo $200 para mostrar bloqueo en vivo). Se descarta mostrar casos de clientes reales de Sur Finanzas/La Virginia como referencia — se ofrecen Carrefour/Coto/McDonald's ("desde los servicios") como comparables. Objetivo: app lista el lunes, ensayo interno el jueves, demo definitiva el viernes (o primera semana de agosto). Ver `tareas_producto.md` T-056.

**Actualización 2026-07-24 — el cliente pasa a tener proyecto propio en el Cerebro:** tras 4 reuniones de relevamiento (Wallet, Cobro, Onboarding y cierre interno con Emma Vignoles y Gonzalo Rivera), todo el contexto de la licitación, la narrativa de la demo, las 12 definiciones cerradas, los 15 riesgos y el checklist ejecutable de configuración viven en [`1_proyectos/proyecto-coca-cola-andina/`](../../1_proyectos/proyecto-coca-cola-andina/proyecto.md). Definiciones de negocio destacadas: demo **en producción** sobre organización de Wallet y entidad de Cobro **nuevas** (cuenta recaudadora 20, PSP 184), reutilizando el flujo de onboarding de Sur Finanzas; onboarding sólo PF con **actividad fiscal excluyente**; **sin logo de Coca-Cola** (sólo su paleta); reclamos, promociones y onboarding de PJ se declaran roadmap. Demo confirmada para el **viernes 2026-07-31 por la mañana**, con corte de configuración el miércoles 29.

## MUTUAL DE EMPRESARIOS DE LA REGIÓN CENTRO
> Estado: Frenado · Sin más contenido sustantivo · Última edición (Notion): 2024-12-02 · Fuente: https://app.notion.com/d9339c37fe1a41e1af3250cffbd0b366

## ARCOR
> Estado: Frenado · Productos: QRI, RxT (→ Adquirencia) · Rubro: Retail · Tamaño: Grande · Riesgo: Bajo · Última edición (Notion): 2026-04-21 · Fuente: https://app.notion.com/150b3646c94b80f7b625cc31c0725c80

**Modelo de negocio — integración de la plataforma "Tokin" (Globant + IniPay + Comafi, hoy 240 comercios activos) con los sistemas de Bind**, para digitalizar pagos a la red mayorista de Arcor: ~180 distribuidores que atienden ~60.000 comercios (proyección 3.500 comercios a fin de año, piloto inicial de 200). Cada comercio se onboardea con Bind PSP (solo clientes de distribuidores, usando el número de cliente de las facturas de Arcor); el onboarding exitoso asocia un POS, un usuario del Portal Web y una **CVU recaudadora**.
**Cómo opera — bot de WhatsApp:** el comercio gestiona pedidos y consulta saldo (compuesto por todas las ventas vía POS de IniPay); solo puede transferir a distribuidores autorizados de Arcor o a sus propias cuentas bancarias. Back office de IniPay muestra detalle de cobranzas y fecha estimada de acreditación. MVP: integración Tokin, OB PH+PJ, POS, Portal Web (solo consulta, no puede operar la CVU salvo desde el chatbot), retenciones impositivas (Conciliador). Roadmap "should have": rentabilidad en cuenta, compra de dólares, adelanto de cupones, lectura QR iniciador, pago en cuotas TD (vía Credicuotas), cobranza de servicios.
**Volúmenes:** 180 distribuidores, volumen mensual estimado USD 90.000.000 (USD 500.000 promedio por distribuidor).
**Pricing:** costo propuesto 0,15%; resultado neto estimado USD 85.000/mes en régimen (arrancando en USD 3.000, progresión mensual).
**Particularidades:** demo realizada sobre la organización de **Sur Finanzas** (PSP 164) mientras no había contrato firmado; integración con Payway pendiente de certificación Mastercard.

## AGUANORT
> Estado: Frenado · Productos: Botón de Pago, POS, RxT (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-12-12 · Fuente: https://app.notion.com/154b3646c94b809d8a29d36ca1ed6c1c

**Pricing:** TD 1,3% · TC 2,3% · QR 0,75% · RxT 0,4%.

## ORDERAR
> Estado: Frenado (por el cliente) · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b8065a9fde4b3f716dd2f

**Status detallado (Comercial):** 14/07 frenado por el cliente — primero van a integrar con el banco.

## PINTECORD
> Estado: Frenado · Rubro: Retail (pinturerías) · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2024-12-06 · Fuente: https://app.notion.com/154b3646c94b803999dbeec4c8e06994

## Beelsur
> Estado: Frenado · Productos: QRI (→ Adquirencia) · Rubro: Transporte · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-07-16 · Fuente: https://app.notion.com/156b3646c94b8033a042c9eee2ece50d

**Modelo de negocio:** empresa de transporte del mismo grupo que **Cruz del Sur** (mismos contactos), recauda con QR interoperable.
**Status detallado (Comercial):** 16/07 homologación frenada, a confirmar con el cliente si continúa.

## IMSA
> Estado: Frenado · Productos: Wallet, Botón de Pago, POS, QRI, RxT (→ Wallet + Adquirencia) · Rubro: ALyCs · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-05-26 · Fuente: https://app.notion.com/165b3646c94b8025b98ff9e0d39e9229

**Modelo de negocio:** ALyC del ecosistema **Gallo** (mismo patrón white-label que IEB y Terra BlockChain) — quiere dar cuentas de pago y solución de cobros a sus merchants.
**Status detallado (Comercial):** 5/9 contrato de cuenta de pago y recaudación electrónica enviado; pendiente reunión con equipo de impuestos.

## BINGO BAHÍA BLANCA (Surfin)
> Estado: Frenado · Productos: QRI (→ Adquirencia) · Rubro: Recargas/Gambling presencial · Tamaño: Pequeño · Riesgo: Medio · Última edición (Notion): 2025-08-28 · Fuente: https://app.notion.com/170b3646c94b80a4acd7d0fcfad74d2a

**Modelo de negocio:** salas de bingo de Bahía Blanca que permiten cargar crédito en una **tarjeta cerrada de su ecosistema** vía QR de monto cerrado/fijo: el cliente escanea el QR (asociado a una orden de venta) desde cualquier billetera, paga y la tarjeta se acredita de inmediato — **sin validar que la billetera pagadora sea de la misma titularidad** que el tenedor del plástico (permite cargas anónimas). Los premios se acreditan en la misma tarjeta y se cobran en caja; el QR solo se usa para el ingreso de dinero. Modelo aprobado por PLD; CBU de acreditación gestionada junto con **Sur Finanzas**.

## CSJ (Honda Motos)
> Estado: Frenado · Productos: Botón de Pago, QRI (→ Adquirencia) · Rubro: Retail · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-12-12 · Fuente: https://app.notion.com/17bb3646c94b80e08150f8d0336e4c69

## KEHKOM
> Estado: Frenado (sin respuesta del cliente) · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/1c8b3646c94b80bb98aaf3e485cdc329

**Pricing:** RxT 0,30%, mínimo de facturación mensual USD 2.500.
**Status detallado (Comercial):** 10/07 en análisis · 14/07 desde abril no contestan.

## Due Network
> Estado: Frenado (en curso de firma) · Productos: RxT · Riesgo: Alto · Tamaño: Pequeño · Última edición (Notion): 2026-01-12 · Fuente: https://app.notion.com/1ceb3646c94b808b84f4f53152f71bd0

**Modelo de negocio:** pagos transfronterizos — Due asigna una **cuenta global** a cada empresa cliente; Bind da a cada usuario de Due un CVU para recaudación por RxT.
**Pricing:** setup USD 5.000 · RxT 0,35% (mín $100, máx $500).
**Status detallado (Comercial):** 14/07 en proceso de firma de contrato · 15/08 en curso revisión del contrato.

## Row Payments SRL (Koywe)
> Estado: Frenado (sin novedades del cliente) · Productos: QRI, Wallet (→ Adquirencia + Wallet) · Rubro: Agente de cobros y pagos · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-06-18 · Fuente: https://app.notion.com/1d7b3646c94b80f080aacd501d57df9a

**Modelo de negocio — dos frentes cross-border cripto:** (1) **QR Aceptador en POS físicos** de comercios en países donde opera Koywe (arranque Chile: Cencosud Chile, Cerro Nevado, cadenas hoteleras en conversación) para que turistas argentinos paguen en el exterior, con Koywe como recaudador por cuenta y orden del merchant; (2) **Lectura de QR** vía contrato con la billetera **Bybit**, integrada en su app para que sus usuarios paguen en comercios locales argentinos. Ambos modelos con KYC/KYB completo.
**Pricing:** QR 0,80% con split, en línea.
**Particularidades / cronología:** ene-2026 PLD nota procesos y seguimiento de clientes "muy flojos", el cliente tiene arbitrajistas de activos virtuales (riesgo); ROW era PSP dado de baja por inactividad, **Lenga** (otra entidad del grupo) solicitando licencia, **Alerce** es el PSAV; 06/04/26 exigencia de que accionistas integren el órgano de dirección de Lenga (PLAFT) · 18/06 pasa a Frenado por falta de novedades del cliente.

## Monnet
> Estado: Frenado (post-firma, avanzando) · Productos: QRI (+ Agente de CyP + RxT en el modelo) (→ Adquirencia + Agente de CyP) · Rubro: Gambling · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2026-02-18 · Fuente: https://app.notion.com/1f1b3646c94b80ca9dbeea9b9c34fe54

**Modelo de negocio — agregador de pagos para operadores de juego (SO):** hace onboarding de cada cliente (entidad PJ con o sin licencia de juego), con **revisión de PLD anual o bianual** y segmentación de riesgo inicial por industria/domicilio/licencias; clientes de alto riesgo operan con Infinitive y son monitoreados. Herramienta local de monitoreo PLD con muestreos por materialidad; ante comportamiento inusual pide documentación de origen y licitud de fondos. Revisión ex-post: entidades de juego anual, otros rubros bianual, clientes finales cada 3 meses.
**Cómo opera:** IN vía RxT/QR; OUT vía transferencia (Agente de CyP); Debit Spot para controlar same-name en tarjetas (no pueden validar titularidad); transferencia saliente sí valida titularidad; OB de cliente final valida entidad + 2FA. El depósito del jugador se convierte en **fichas** (no retirables directamente); solo se pueden retirar premios o un % de las fichas tras un período (varía por entidad).
**Status detallado (Comercial):** 16/07 en negociación por cláusulas de exclusividad/prioridad/mínimos que el cliente no aceptaba · 31/07 contrato firmado, el cliente accedió · 07/08 inicia integración y cobro de setup.
**Pricing:** QR 0,8%, 24hs sin split.

## Refinor
> Estado: Frenado · Sin más contenido sustantivo · Última edición (Notion): 2025-09-22 · Fuente: https://app.notion.com/230b3646c94b804688c7c0e6fd849f36

## 47 Street
> Estado: Frenado (pendiente de definición de créditos) · Productos: Wallet Services + solución de cobro · Última edición (Notion): 2025-09-03 · Fuente: https://app.notion.com/233b3646c94b80329ddcf78564d59298

**Modelo de negocio:** cadena de indumentaria (22 locales propios + 70 franquicias, ~150.000 usuarios, ~10 pagos/día) que quiere Wallet.
**Status detallado (Comercial):** 28/07 se sumó una persona para resolver el tema de créditos antes de avanzar con una propuesta integral.

## Universidad Nacional de Tucumán
> Estado: Frenado (en curso de integración) · Productos: RxT, Botón de Pago (→ Adquirencia) · Tamaño: Mediano · Última edición (Notion): 2025-09-22 · Fuente: https://app.notion.com/23bb3646c94b8082a6aef9076ebd0821

**Status detallado (Comercial):** 28/07 reunión técnica · 11/08 abriendo cuenta en el banco · 15/08 integrando RxT, resta cerrar Botón de Pago. Precio aún sin definir.

## APPA
> Estado: Frenado · Productos: POS, QRI (→ Adquirencia) · Riesgo: Bajo · Última edición (Notion): 2026-04-21 · Fuente: https://app.notion.com/211b3646c94b806d898df001a75f0f93

## CREDITIA S.A.
> Estado: Frenado (contrato pendiente por múltiples sociedades) · Productos: RxT, QRI, Botón de Pago (→ Adquirencia) · Rubro: préstamos de consumo, Resumen de Tarjetas de Crédito · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-03-10 · Fuente: https://app.notion.com/216b3646c94b80c1b3f7f1bd7607a725

**Status detallado (Comercial):** el cliente opera con **3 razones sociales distintas** — 10/07 pendiente confirmar contrato, call por las 3 sociedades · 31/07 a la espera de firma · 07/08 avanzarán con la firma de los 3 contratos.

## Taxes Software
> Estado: Frenado (por tipo de cuenta) · Productos: QRI, Botón de Pago, RxT (→ Adquirencia, modelo agrupador) · Última edición (Notion): 2025-12-29 · Fuente: https://app.notion.com/264b3646c94b80b8af24e55b5cd09c61

**Modelo de negocio:** ERP que da solución de cobros (Botón Simple, QR, RxT) a sus clientes, liquidando todo a una única CBU de Taxes Software (modelo agrupador).
**Pricing:** RxT/CVU Collector 0,35% (1 día) · QR 0,8% (1 día) · TD 1,5% (2 días) · TC 2,5% (18 días).
**Status detallado (Comercial):** 3/9 contrato firmado · 3/10 finalmente solo solución de cobros (no Agente de CyP), liquidación a una sola CBU · 15/12 intentó tramitar cuenta exenta de impuestos, rechazada — **se frena el proyecto por no ser viable sin ese tipo de cuenta**.

## Paymake
> Estado: Frenado (no cubre facturación mínima) · Productos: Botón de Pago, RxT, Agente de Cobros y Pagos (→ Adquirencia + Agente de CyP) · Rubro: E-commerce · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-11-06 · Fuente: https://app.notion.com/264b3646c94b80e3b6eac8ac9c51c3ad

**Modelo de negocio:** plataforma marca blanca (Wemake) de cobros para comercios e-commerce clientes — vía módulo de Agente de CyP instruye el pago de su comisión a su CBU y el pago de la transacción al comercio.
**Pricing:** setup USD 1.500 · CVU Collector 0,35% · QR interoperable 0,8% · Botón TC 2,5%/TD 1,5%/prepaga 2,5% · Ag CyP pay-out nacional 0,3% con mínimo mensual USD 5.000.
**Status detallado (Comercial):** 4/9 contrato enviado · 22/9 firmado · 3/10 envío de contrato de Agente de CyP · **22/10 no llega a cubrir la facturación mínima y no quiere asumir el compromiso — se retoma más adelante**.

## CW Pagos
> Estado: Frenado (perdido por precio) · Productos: Botón de Pago, QRI (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-12-23 · Fuente: https://app.notion.com/26fb3646c94b8070a99fc9495b99994e

**Modelo de negocio:** Botón Simple + QR Aceptador para integrar a su app de viajes **Moviplus**.
**Pricing:** RxT 0,30% (1 día) · TD 1,5% (2 días) · TC 2,5% (18 días) · QR 0,8% (1 día) · setup USD 3.000 (2 cuotas).
**Status detallado (Comercial):** 15/9 contrato enviado · 25/9 firmado · **1/10 finalmente no avanza — Bind resultó más caro que la solución actual del cliente con Fiserv**.

# CLIENTE NO CERRADO

## IOL
> Estado: Cliente no cerrado · Última edición (Notion): 2025-08-11 · Fuente: https://app.notion.com/13db3646c94b80c29f47de2bd9c81b6f

**Status detallado (Comercial):** 14/07 analizando modelos de negocio.

## PAYAMIGO
> Estado: Cliente no cerrado · Productos: RxT · Última edición (Notion): 2026-01-12 · Fuente: https://app.notion.com/143b3646c94b801b9ab7ff9cda9a9e09

**Modelo de negocio:** en un primer momento querían Wallet Services, luego lo desestimaron; interesados en RxT.
**Pricing propuesto:** RxT 0,5%, mínimo USD 5.000.
**Particularidades:** ver también ficha PAY & THINK — hay un correo de Banco Industrial sobre "lanzamiento de PayAmigo en Argentina" archivado en esa página, posible relación entre ambos clientes (a confirmar, gap).

## BLM
> Estado: Cliente no cerrado · Rubro: servicios financieros · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/78c1794ec00541b293ee610899539bf7

**Pricing:** transferencia 0,80% · TD 2,5% · TC 2,5% · Servicios Billetera 0,4% por consumo de API · Onboarding USD 1,5/alta.

## CASA EL GATO
> Estado: Cliente no cerrado · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/256ad535dea74b61bb8d2b5c597c9fa5

**Pricing:** QR 0,8%.

## WAYA
> Estado: Cliente no cerrado · Productos: Botón de Pago, RxT, QRI (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/f41749df3122468e8ff46cbc7efa7cd2

**Pricing:** TD 1,3% · TC 2,3% · QR 0,8% · RxT 0,4%.

## COOPERATIVA ELÉCTRICA
> Estado: Cliente no cerrado · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/154b3646c94b80b3898ef960e782dcd9

**Status detallado (Comercial):** 16/07 interesados en QR, reunión pendiente, contrato aún no firmado · 31/07 sin novedades, reunión no se realizó.

## FLEX FINTECH
> Estado: Cliente no cerrado · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b80bb9ad3db764e74c21e

**Status detallado (Comercial):** 14/07 integró APIs del Banco.

## INSRED
> Estado: Cliente no cerrado · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b8049a70acda5bf3e3ca2

**Status detallado (Comercial):** 14/07 pendiente de seguimiento interno.

## LA ANÓNIMA
> Estado: Cliente no cerrado · Productos: Wallet · Última edición (Notion): 2025-11-13 · Fuente: https://app.notion.com/154b3646c94b80cbb393ced9e15a1b0d

**Modelo de negocio:** supermercado con app propia; quiere **saldo en cuenta sin CVU** (Comercial intenta convencerlos de usar CVU) y **tarjetas embebidas en la app**, exclusivas de La Anónima.
**Particularidades / cronología:** 13/11/25 — consultas a Payway sobre **tokenización**: si el token de la bóveda de tarjetas de Bind (contra Decidir) es único por PSP, si puede usarse con distintos números de establecimiento (incluso de un comercio directo con CUIT distinto a Bind), y si una entidad no-PCI-compliant puede pedir a Decidir un token de cliente conocido para uso frecuente — caso de referencia sobre límites técnicos de tokenización compartida.

## OSEBAL
> Estado: Cliente no cerrado · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/a8cff0b9c130480b822a7301031c34eb

**Status detallado (Comercial):** 10/07 se dio por finalizado el ticket por falta de respuesta del cliente.

## WEBOND
> Estado: Cliente no cerrado · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b8038b21aecec848be72a

**Status detallado (Comercial):** 14/07 no se llegó a acuerdo comercial.

## TECH GROUP
> Estado: Cliente no cerrado · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b80f099becda66b168c3a

**Status detallado (Comercial):** 14/07 no cerrado por costos.

## PAY & THINK
> Estado: Cliente no cerrado · Rubro: Agrupadores de Pago · Riesgo: Alto · Última edición (Notion): 2025-12-23 · Fuente: https://app.notion.com/1fab3646c94b8024bdb3c79c1ebb182f

**Modelo de negocio:** agrupador de pagos. Página incluye referencia a correo de Banco Industrial sobre "lanzamiento de PayAmigo en Argentina" — posible vínculo con el cliente PAYAMIGO (a confirmar, gap).

## DIRECTA (ERON)
> Estado: Cliente no cerrado (compliance pendiente) · Productos: Agente de Cobros y Pagos, QRI, RxT, Wallet · Rubro: Gambling · Tamaño: Grande · Última edición (Notion): 2026-02-10 · Fuente: https://app.notion.com/231b3646c94b80bfa4daf41a9dbefe72

**Modelo de negocio:** app del exterior (**Directa**, procesador de pagos con sociedad en Bahamas) usada para pagar juego y OF del exterior por residentes locales — necesita una **rampa FIAT** para colectar y liquidar pesos, compensando el balance local. RxT + Agente de Cobros y Pagos al exterior. El OB con Bind lo tiene **Glosa INC** (empresa relacionada).
**Pricing:** setup USD 70.000 (bonif. 10%) · abono mensual USD 50.000 escalonado (USD 10.000 mes 1 → USD 50.000 desde mes 5, tomado como mínimo de facturación) · cash in/out 1,8%.
**Status detallado (Comercial):** 28/07 propuesta cerrada, pendiente devolución económica del cliente · 11/08 acuerdo comercial cerrado, integración por iniciar · **22/09 no pasan compliance — no aceptan tener que hacer OB a sus clientes finales**.

## Mirgor
> Estado: Cliente no cerrado · Productos: RxT · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/232b3646c94b802981dfc16fd436e5d5

**Status detallado (Comercial):** 31/07 el cliente no tiene tiempo por el momento para avanzar con el desarrollo de la integración.

## House4you
> Estado: Cliente no cerrado (en negociación) · Productos: Agente de Cobros y Pagos, Wallet · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2025-09-22 · Fuente: https://app.notion.com/263b3646c94b80c6a596eb8f0383aaad

**Modelo de negocio:** Wallet Services con **CVU única a nombre de House4You** para recolectar los ARS de usuarios que consumen en Argentina; consulta de cotización y operatoria **CCL** para comprar USD y transferir al exterior a una cuenta de House4You, bajo la figura de Bind como **Agente de Cobros y Pagos** de la entidad.

## Diarco
> Estado: Cliente no cerrado · Productos: POS, Botón de Pago, Onboarding, Wallet · Rubro: Retail · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2026-02-10 · Fuente: https://app.notion.com/271b3646c94b8039a45dfba0d784a956

**Modelo de negocio:** retail que pide una **app de billetera** para que todos sus clientes puedan descargarla y usarla para pagos, solicitud de créditos (vía Credicuotas), pago de servicios y **FCI** — superapp retail similar en alcance a lo que ya hicieron Coppel y La Virginia.

## Vaygu S.A. (Dubalu)
> Estado: Cliente no cerrado (standby PLD) · Productos: Botón de Pago, RxT, QRI, Wallet · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/273b3646c94b809fbb3df186834ccb53

**Status detallado (Comercial):** 15/01 en standby hasta ~primera semana de febrero por verificación de PLD.

## Vecinos app
> Estado: Cliente no cerrado (presupuesto no alcanza) · Productos: Wallet, Botón de Pago, QRI · Rubro: E-commerce · Tamaño: Pequeño · Última edición (Notion): 2025-12-29 · Fuente: https://app.notion.com/27ab3646c94b808ea829e34a40ba3160

**Modelo de negocio:** marketplace que quiere desarrollar una billetera para transferencias en una primera etapa, y sumar solución de cobros después.
**Status detallado (Comercial):** quieren marca blanca para operar en **Argentina, México, Colombia y EEUU** · 27/11 el costo pasado está muy lejos de su presupuesto — están en etapa inicial de la startup.

## PMI Pagos Más Inteligentes Américas Argentina SA
> Estado: Cliente no cerrado · Productos: QRI · Rubro: Agrupador · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/284b3646c94b807fbc42c0054c1f0562

**Status detallado (Comercial):** 09/10 pendiente correo para facturar setup y habilitar tickets JIRA · 16/10 sin novedades, push continuo.

## CRAYON WEB
> Estado: Cliente no cerrado · Productos: Botón de Pago, RxT, QRI, Wallet · Rubro: Desarrollo de Software · Tamaño: Pequeño · Última edición (Notion): 2026-02-10 · Fuente: https://app.notion.com/1eeb3646c94b80b9ab78cc06cb1b835a

Sin contenido de modelo de negocio ni pricing más allá de los datos de la entidad.

# DADO DE BAJA

## ASTROPAY
> Estado: Dado de baja · Productos: QRI, Onboarding, Wallet, Agente de Cobros y Pagos (→ Adquirencia + Onboarding + Wallet + Agente de Cobros y Pagos) · Rubro: Agente de cobros y pagos · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2026-04-24 · Fuente: https://app.notion.com/13db3646c94b80888ff5d4b363919478

**Modelo de negocio:** Astropay migrando sus contratos locales a Bind PSP para que Bind sea su partner oficial en Argentina; opera Wallet Services (PSPaaS), Onboarding y Solución de Cobros (QRI).
**Pricing:** QRI arancel aceptador 0,8% · PSPaaS setup bonificado · CVU activa mensual USD 0,10 (primeros 6 meses bonificadas hasta 30.000 CVUs activas) · cash in/out $17 · QRI módulo USD 5.000/mes · Onboarding escalonado: $25/validación (hasta 200.000/mes) → $20 (200.001-500.000) → $15 (+500.000).
**Particularidades:** clasificado como "Dado de baja" en el estado pero la última observación indica proyecto activo de migración de contratos — posible desalineación entre el `Estado del Cliente` y la realidad operativa (gap a verificar con Comercial).

## LA AMISTAD
> Estado: Dado de baja · Última edición (Notion): 2026-06-18 · Fuente: https://app.notion.com/149b3646c94b805daa63f9a89987b1b3

**Status detallado (Comercial):** 10/07 se da de baja de los servicios, ya devolvieron los POS.

## PRONTO PAGO
> Estado: Dado de baja · Productos: QRI (→ Adquirencia) · Rubro: Agente de cobros y pagos · Tamaño: Mediano · Última edición (Notion): 2026-04-29 · Fuente: https://app.notion.com/6b24056a401442bfbcfd18f33cf18111

**Pricing:** transferencia 0,8% · TC 3% · TD 2,5% · POS USD 10.000/mes (gratis si supera 1M de transacciones) · QR extrabancaria (según contrato).

## MALAGA (MoPago)
> Estado: Dado de baja · Productos: Botón de Pago, QRI, POS, RxT, Onboarding, Wallet (→ Adquirencia + Onboarding + Wallet) · Tamaño: Mediano · Riesgo: Alto · Última edición (Notion): 2026-06-08 · Fuente: https://app.notion.com/17ab3646c94b80638a49e00c92c30921

**Modelo de negocio:** agrupador de pagos (One Pay S.A.) con red de subcomercios — todos con CUIT de One Pay, cuenta acreditadora CBU de One Pay, que reliquida a cada subcomercio vía CVU propia y front desarrollado por ellos, consumiendo Wallet Services de Bind. Dos comercios operados en paralelo: uno con arancel reducido (MCC 9311) y otro con arancel regular (MCC 5411).
**Pricing:** setup USD 10.000-25.000 (50% a la firma, resto al pase a producción) · módulo Agrupador + Licencia PSP USD 1.500-5.000/mes · Onboarding USD 1/alta · abono CVU activo $10 · cash in/out 0,20-0,30% (mín $20, máx $350) · lectura/interpretación QR 0,2% · TD 1,10-2% · TC 2,10-2,5% · QRI aceptador 0,8%.
**Particularidades / cronología:** requerían activación automática de Botón de Pago para todos sus comercios y webhook por alta de caja (hoy manual/por polling). Se les fijó un piloto productivo de 10 comercios con actividad AFIP para habilitar el link de pago; no cumplieron el alcance del piloto y **se les notificó la baja de servicio el 29/05/26** por incumplimiento.

## BINCO (Plexo)
> Estado: Dado de baja · Productos: QRI, RxT (→ Adquirencia) · Rubro: Expensas · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-07-02 · Fuente: https://app.notion.com/18fb3646c94b80a9bab5da707166bae8

**Modelo de negocio:** grupo uruguayo (Binco / Plexo / Paypunta) que cobra expensas y alquileres de Punta del Este a propietarios argentinos. Flujo cross-border: el propietario transfiere ARS a la cuenta de Binco en Bind → Binco opera CCL (con Bind o alternativamente Balanz) → los dólares se reciben en Binco Uruguay → Binco Uruguay paga en dólares a las administraciones de Punta del Este, usando Plexo (PSP con licencia del Banco Central del Uruguay) como agente de dispersión. Mercado de referencia: Punta del Este mueve ~USD 50M/mes en expensas, meta de captar 10% en 2 años; ticket promedio ~USD 3.000.
**Pricing:** QR 0,80% (en línea) · RxT 0,35% (24 hs) · setup USD 1.500 · mínimo USD 1.000 de facturación (primeros 3 meses bonificados 50%).

## TICKET QR
> Estado: Dado de baja (baja solicitada 16/03/26) · Productos: RxT (→ Adquirencia) · Rubro: Eventos · Tamaño: Pequeño · Riesgo: Medio · Última edición (Notion): 2026-04-27 · Fuente: https://app.notion.com/19fb3646c94b801cafe2d7d50aec883a

**Modelo de negocio:** plataforma de venta de entradas para eventos (fiestas de egresados, boliches) que usa RxT en una única caja compartida (no genera 1 caja por CVU).
**Status detallado (Comercial):** 11/07 RxT en producción, gestionando homologación de QR (pendiente apertura de cuenta) · 27/04 se solicitó la baja desde el 16/03/26.

## E-COBRO
> Estado: Dado de baja (por inactividad) · Productos: Wallet (→ Wallet) · Rubro: Impuestos y Servicios · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-06-11 · Fuente: https://app.notion.com/27ab3646c94b8007938bf7c9b245122d

**Modelo de negocio:** TCash, billetera virtual con Banco Industrial (Bind) como banco sponsor, orientada a retail — integra CVU para personas físicas y jurídicas, pagos/transferencias, tarjeta prepaga Visa (Prisma), inversiones (alianza con DMA Broker/Manteca para dólar MEP), PIX en tratativas (Braza Bank) y pago de impuestos/servicios (Pago Mis Cuentas). De Bind consume lectura e interpretación de QR para pagos en comercios retail (Wallet Services).
**Status detallado (Comercial):** 02/10 contrato firmado, facturación de SetUp iniciada · 16/10 la entidad reportó datos incorrectos en la factura (razón social/CUIT) · 26/02 sin respuesta del cliente sobre onboarding · **11/06 dado de baja por el equipo de Integraciones el 01/06 por inactividad**.

# EN PRODUCCIÓN

## INSWITCH
> Estado: En producción · Productos: RxT, QRI, Wallet (→ Adquirencia + Wallet) · Rubro: Cripto · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2026-04-22 · Fuente: https://app.notion.com/13cb3646c94b805ba2acdea1e6020c5c

**Modelo de negocio:** "recaudador de recaudadores" — presta servicios de recaudación y expatriación de fondos a otros players. Su cliente estrella es **Binance**: desde nov-2024 Inswitch recauda con QR para Binance; desde abr-2025 busca sumar RxT para Binance (evaluando límites de $24M por cliente/año solo con KYC, contrato Binance-Inswitch).
**Cómo opera los productos:** integración vía APIs. Wallet Services/PSP + Solución de Cobros (QR, RxT) + Onboarding. Modelo tipo Depay para clientes brasileros (oct-2025): lectura de QR para un banco y una fintech de Brasil — el usuario brasilero lee y paga a un comercio argentino; prefondean pesos en CVUs (una CVU por comercio) y CBU.
**Pricing:** Wallet: setup fee USD 5.000 (50% a la firma, 50% al go-live) + costo fijo por CVU activa/mes escalonado ($25 hasta 50k → $19 hasta 150k → $13 hasta 500k → $10 en adelante) + cash in/out CBU-CVU 0,35% + facturación mínima mensual. Cobros: TD 0,95% · TC 1,95% · QR 0,8% · RxT 0,49%. Onboarding: USD 2.000 implementación + abono USD 1.250/mes (incluye 1.000 trx) + excedente USD 0,7423/trx + logueo sin biometría USD 0,035 y con biometría USD 0,09. Plazos: PCT 24hs, TD 48hs, TC 20 días hábiles.
**Particularidades / cronología:** feb-2026 suma **Agente de Cobros y Pagos**: Bind recauda en cuenta Reca, compra USDT con los ARS y envía a una address propia de Inswitch (cripto-expatriación). Abr-2026: piden adendar contrato por Ag CyP; quieren sumar a **Temu** (recaudar en Argentina y liquidar en USD/stablecoin desde FV — Bind pagaría a Temu); también recolección de efectivo por Pago Fácil (piden fecha y precio).

## DEPAY
> Estado: En producción · Productos: Wallet, QRI (→ Wallet + Adquirencia) · Rubro: Billetera · Tamaño: Mediano · Riesgo: Alto · Última edición (Notion): 2026-02-02 · Fuente: https://app.notion.com/13db3646c94b804f8e7ed79bf395456c

**Modelo de negocio:** infraestructura regional de pagos para que partners (billeteras de LatAm y EEUU, generalmente ligadas a bancos) consuman sus servicios y realicen **pagos QR en Argentina**. Rol emisor en Colombia, Perú, Brasil y Argentina; pagos cruzados siempre con rol billetera.
**Cómo opera los productos:** integración vía API. Bind presta **lectura e interpretación de QR** (QRI). Alta de billetera: Depay hace el KYC, presenta legajo a PLD Bind → OK → Depay crea una **CVU por billetera** (alias/nombre = nombre de la wallet). Operación: los fondos entran por CCL o dólar cripto, asignan saldo a la CVU de la billetera y validan saldo (billetera y cliente final) **antes** de ejecutar el PCT. Bind puede requerir info de clientes finales.
**Pricing:** abono mensual USD 2.000 (1er bimestre -50%, 2do -25%) + módulo QR (lectura e interpretación) 0,2%.
**Particularidades:** es el modelo de referencia ("modelo Depay") que luego replicó Inswitch para sus clientes brasileros.

## SUR FINANZAS
> Estado: En producción · Productos: Wallet, Adquirencia (QR/POS/Botón) — plataforma white-label multi-comercio · Fuente: Notion histórico, 6 Epics (no viene de la base "Legajos de clientes" de `/sync_customers` — ficha cargada manualmente, ver [ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md](../../3_recursos/detalle_productos/ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md) para la mecánica técnica completa)

**Modelo de negocio:** cliente/marca white-label que combina Wallet (cuentas+CVU) y Adquirencia (POS/QR/Botón) bajo un Portal comercio, Admin y APK propios — cada comercio de SUR FINANZAS puede tener cuenta y saldo propios, canales de cobro configurables independientemente, y multi-credencial (más de una cuenta+CVU por comercio/usuario).
**Casos de uso reales:** venta de entradas de eventos (incluida la Selección Argentina de fútbol), links de pago en el portal de comercio.
**Cumplimiento:** se reporta como entidad normativamente separada ante Worldsys/BCRA (ver [cumplimiento_normativo/reporteria_worldsys_bcra.md](../../3_recursos/cumplimiento_normativo/index.md)), no mezclada con el resto de las organizaciones de Wallet.
**Particularidades / cronología:** deuda pendiente real (no confirmado si se resolvió) de facturación automática contra AFIP y automatización de Régimen Informativo BCRA/AFIP. Bug de segmentación cruzada conocido con el cliente **TIN** (cuentas de TIN se daban de alta con el segmento de costos de SUR FINANZAS).

## COINBASE
> Estado: En producción (saliendo) · Productos: Agente de Cobros y Pagos, Agente de Pagos (→ Agente de CyP) · Rubro: Cripto · Tamaño: Grande · Riesgo: Alto · Última edición (Notion): 2026-01-20 · Fuente: https://app.notion.com/13db3646c94b80369e8dd5ce6bf53eb7

**Modelo de negocio:** exchange cripto global usando a Bind como Agente de Cobros y Pagos para su operatoria en pesos. Integración vía APIs.
**Particularidades / cronología:** ⚠️ **Roadmap de salida**: 31/01/2026 cortan la operatoria en PESOS; 31/03/2026 se cierra la cuenta.

## TIN
> Estado: En producción · Productos: (sin etiquetar en Notion) · Rubro: — · Última edición (Notion): 2025-04-08 · Fuente: https://app.notion.com/13db3646c94b80adac3fcc1e95bc8b15

**Modelo de negocio (propuesta):** solución integral de pagos y cobros para el **transporte**: Wallet marca blanca + agrupador de cobranzas. QR disponible en la app de TIN para ser leído por el sistema de **micronauta**; la wallet permite pagar con tarjetas de crédito/débito y lectura de QR.
**Cómo opera los productos:** TIN actúa como **agrupador de cobranzas**, acreditando montos en el CVU de las empresas de transporte según aranceles y plazos, obteniendo resultado financiero. Se evalúa remunerar los saldos de la cuenta recaudadora de TIN (con las ALyCs que TIN elija).
**Nota:** ver también ficha TECNOINT (mismo ecosistema TIN — volúmenes del interurbano).

## CREDICUOTAS
> Estado: En producción · Productos: Botón de Pago, Wallet, RxT, QRI, Monitoreo (→ Adquirencia + Wallet) · Título en Notion: "CREDICUOTAS - incompleto" · Última edición (Notion): 2026-04-15 · Última edición (Cerebro): 2026-07-14 · Fuente: https://app.notion.com/13db3646c94b8082a752c2cd6fd02e49

**Modelo de negocio:** lending de consumo. QR y RxT para la **cobranza de sus resúmenes** (van en los resúmenes al cliente). Wallet Services para la **billetera de Credicuotas**: acredita el lending y luego el cliente consume.
**Cómo opera los productos:** establecimientos de Bind PSP, ídem modelo Astro(pay) — ~**3 millones de trx/mes** que no quedan en la BD de Bind. CBU de Bind PSP con acceso Credicuotas (distinta a la /2). **Agente de CyP**: Credicuotas retira los fondos cuando quiere. Conciliación: prueba de 10 trx con generación manual de archivos desde el Portal de Payway, colgados en un SFTP de Credicuotas para su validación.
**Particularidades / cronología:** abr-2026: facturación con NC pendiente; costo de API Bank +15%; contrato pendiente. El propio título del brochure dice "incompleto". 14-jul-2026: identificado como uno de los clientes que generan **consultas inusuales en horas de madrugada**, presionando la base de datos junto con Global 66 — el equipo técnico evalúa contactarlo para pedir que distribuya mejor su carga de trabajo (ver `wallet/otros_manuales.md §11`).

## FAVACARD
> Estado: En producción · Productos: POS, Botón de Pago, QRI (→ Adquirencia) · Rubro: Resumen de Tarjetas de Crédito · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2026-04-22 · Fuente: https://app.notion.com/13db3646c94b80388083cab94f916128

**Modelo de negocio:** cobranza de resúmenes de su tarjeta de crédito regional (Mar del Plata). Solo operan con débito (dieron de baja crédito).
**Cómo opera los productos:** conviven **3 comercios/entidades**: "F" (QR Portal Web en las cajas de Fava, PSP 164), "K" (POS TD y Botón 1.0, PSP 184) y "A129" (Botón 2.0, PSP 184). Plan de migración a arancel reducido: tomar la entidad "K", habilitar Portal Web + Botón 2.0 (mismas credenciales para QR Integrado y toda la solución de cobros) y crear comercios bajo **CUIT de Bind PSP** con rubro red extrabancaria (MCC QR 8999) — un comercio por producto (POS / Botón 2.0-QRI / RxT), replicando las 45 sucursales y cajas. Todos liquidan a una única cuenta recaudadora.
**Pricing:** RxT 0,25% (24hs) · QR: fee COELSA 0,05% + 0,55% facturado como costo administrativo (1 día hábil) · TD 0,65% (2 días hábiles). Sin split en QR de cajas.
**Particularidades / cronología:** caso testigo de la **migración PSP 164 → 184** y del modelo "comercios bajo CUIT Bind PSP con MCC de red extrabancaria". 06-ago-2026: bug detectado de asignación automática de CBU corta — Botón Simple 2.0 toma indistintamente CBU de RxT y de Botón 2.0 por falta de filtro `pago_unico`, generando transacciones mal etiquetadas; fix en análisis, ver [`adquirencia/configuracion_entidades_y_comercios.md`](../../3_recursos/detalle_productos/adquirencia/index.md).

## GALLO
> Estado: En producción · Productos: QRI, Onboarding, Wallet (→ Adquirencia + Onboarding + Wallet) · Rubro: ALyCs · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-06-01 · Fuente: https://app.notion.com/13db3646c94b80979b2cc1ce3421ed14

**Modelo de negocio:** ALyC que integra billetera digital a las cuentas de inversión de sus clientes: carga/descarga/transferencia de fondos + lectura de QR para convertir los saldos de inversión en herramienta de pago cotidiano.
**Cómo opera los productos:** Wallet Services integrado a cuentas comitentes; QRI para adquirencia/pagos; **API PIX** (vía PagBrasil) para pagos instantáneos con Brasil.
**Pricing:** integración PIX con 6% de spread, del cual se comparte 1% a Gallo.
**Particularidades / cronología:** abr-2026: avanzar firma de contrato con PagBrasil para PIX en Gallo. Jun-2026: ticket por QR interoperable (BP-46563). Relacionados: IEB (Gallo) y Terra BlockChain (Gallo) — mismo grupo.

## BEST BUS
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2024-11-29 · Fuente: https://app.notion.com/102605c1653e4bcda4ffdf58e7afc4c1

**Modelo de negocio:** venta de pasajes de corta y media distancia; cobra con QR.
**Pricing:** QR 0,80%.

## CENCOSUD
> Estado: En producción · Productos: QRI, RxT (→ Adquirencia; en integración de Wallet as a Service) · Rubro: Retail · Tamaño: Grande · Última edición (Notion): 2026-04-29 · Fuente: https://app.notion.com/345b7594cd074e3cb4454b006591d387

**Modelo de negocio:** retail grande (Tarjeta Cencosud). Además de cobros (QRI/RxT), avanza como **PSP propio ("PSP Cenco") sobre la infraestructura Wallet de Bind** — multi-PSP.
**Pricing (Wallet):** costo por cuenta activa escalonado: $17 (1-100k) → $15 (100-300k) → $13 (300-500k) → $10 (+500k). Cash in/out 1% con tope $250. Consumo de APIs mensual: USD 0,002 (1-5M llamadas) → USD 0,00175 (5-10M) → USD 0,0014 (10-15M).
**Particularidades / cronología:** abr-2026: alta del nuevo PSP lista (14/04); se creó la Organización "PSP Cenco" en Wallet y se enviaron credenciales de PROD; pendiente homologación de **Billetera Interoperable en COELSA** (DDJJs de uso de credenciales para la carta del banco sponsor, firma pendiente).

## COBRO EXPRESS
> Estado: En producción · Productos: QRI, POS (+ RxT en contrato) (→ Adquirencia + Agente de CyP) · Rubro: Impuestos y Servicios, Recargas · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2026-02-19 · Fuente: https://app.notion.com/da4009a3c8e14075b61397e0b95bc50a

**Modelo de negocio:** cobranza extrabancaria de impuestos y servicios por cuenta y orden de terceros (TINSA S.A.).
**Status detallado (Comercial):** 31/07 productivos con QR, homologando QR para entes y RxT · 06/10 falta contrato para la solución donde Spena será un comercio más de Cobro Express · 16/10 primer comercio productivo compartido · 19/02 no avanzaron con RxT; Spena ya productivo a través de ellos.
**Cómo opera los productos — modelo "nueva entidad CE para Spena"** (sub-agregación): Bind crea N comercios todos con CUIT/razón social TINSA y nombre de fantasía del comercio real, cada uno con QR asignado (rubro impuestos y servicios) y acceso al Portal Web (solo sus trx, sin liquidaciones). Los cobros van a una CBU recaudadora de Bind asignada a TINSA (Agente de Cobros). Spena lleva las cuentas corrientes de los comercios, recibe el efectivo de los agentes y entrega efectivo en los retiros; TINSA transfiere a los Entes desde la CBU recaudadora (Agente de Pagos; único destino permitido: los Entes). Impositivo: todos los comercios bajo CUIT TINSA en la misma provincia (Santa Fe) para no distorsionar liquidaciones (SIRTAC/CM). Mientras no integren las APIs de Ag CyP, consultan saldo por acceso B24 en modo consulta.
**Pricing (contrato 16/10):** PCT 0,6% (arancel COELSA 0,05% con MCC de la entidad + 0,55% facturado como gastos administrativos) · TD 0,8% · TC 1,8% · RxT 0,6% · Ag CyP: pay-in bonificado, pay-out 0,05%. Plazos: PCT 1 día hábil, TD 2, TC 18, RxT en línea. (Contrato previo: transf 0,8 / crédito 3 / débito 2,5 / POS $10.000-mes gratis si supera 1M trx.)

## BANZA
> Estado: En producción · Productos: Wallet, QRI, Onboarding (→ Wallet + Adquirencia + Onboarding) · Rubro: ALyCs · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-02-04 · Fuente: https://app.notion.com/143b3646c94b8006927ec1852b05cb28

**Modelo de negocio:** PSPCP (PSP as a Service) para ofrecer servicios de pago a los usuarios de su plataforma de inversiones.
**Cómo opera los productos — "adelantamiento de fondos":** cuando el usuario tiene activos en su cuenta comitente pero su CVU está sin saldo, Banza emite un **comprobante de crédito** vía API de Bind PSP y Bind asigna los fondos al CVU (los fondos deben estar previamente disponibles en la cuenta recaudadora de Bind). Regla de cierre: antes del corte diario, el saldo de la recaudadora debe ser ≥ suma de saldos de todas las CVUs (se genera un débito al CVU de Banza por el total adelantado en el día).
**Pricing:** setup USD 5.000 · PSPaaS: abono USD 1.500/mes + mantenimiento CVU USD 0,25/mes + cash in/out según tarifario API Bank + lectura QR 0,12% · facturación mínima creciente (USD 1.000 mes 1 → USD 5.000 desde mes 8) · Onboarding: mismo esquema estándar (USD 2.000 implementación, USD 1.250/mes por 1.000 trx, excedente USD 0,7423, logueos USD 0,035/0,09).
**Particularidades / cronología:** ago-2025: **migración de Banza a ADCAP** en validación legal. ADCAP quiere dar a sus clientes Pago QR, FCI propio y pago de servicios con **TAPI** (Bind firma con TAPI, pide 0,10%; factura 100% a TAPI y bonifica a ADCAP el 100% menos 0,10% menos IIBB). Esquema de descubierto: USD 2.000 + tasa de cobertura + tasa de colchón, respaldado con colateral (PF endosado o caución).

## TRAVEL ROCK
> Estado: En producción · Productos: RxT (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2025-09-30 · Fuente: https://app.notion.com/145b3646c94b80fe9bc3e072c787adb3

**Modelo de negocio:** agencia de viajes minorista; recaudación de **cuotas de viajes de egresados** vía RxT, a través de una plataforma desarrollada por Globant/Daxia.
**Cómo opera los productos:** Transferencias 3.0 / transferencia a "CVU Collector".
**Pricing (escalonado por volumen mensual):** hasta $3.000M: 0,3% · $3.000-5.000M: 0,27% · +$5.000M: 0,25%. Acreditación 24hs.

## ALIMENTOS SOFIA
> Estado: En producción · Productos: QRI, Botón de Pago, POS (→ Adquirencia) · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2024-12-09 · Fuente: https://app.notion.com/145b3646c94b804496edd514e19301b7

**Modelo de negocio:** alimenticia (Productos Sofía); cobros con QR, Botón y POS.
**Pricing:** débito 2,5% · crédito 2,5% · transferencia 0,80%.

## TIPEANDO
> Estado: En producción (comercio dado de baja) · Productos: QRI (→ Adquirencia) · Rubro: Propinas · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-04-23 · Fuente: https://app.notion.com/de99a69af7e841ceb17e8123b9ff852a

**Modelo de negocio:** app de propinas digitales cobradas con QR.
**Status detallado (Comercial):** ⚠️ "Se dio la baja del comercio, por pedido de PLD" (el estado de la base sigue diciendo En producción — contradicción registrada en gaps).
**Pricing:** QR 0,80%, acreditación inmediata.

## TECNOINT
> Estado: En producción · Productos: (sin etiquetar en Notion) · Última edición (Notion): 2025-04-07 · Fuente: https://app.notion.com/4ed48a8e3c3a463aae537a616fcae8bf

**Contexto (ecosistema TIN / transporte interurbano):** TIN mueve ~$3.000 millones por las tarjetas; 6.000 usuarios de boleto estudiantil y beneficios sociales; el resto compra en boletería. Total del interurbano: ~$14.000 millones.

## TARJETA VALOR
> Estado: En producción · Productos: POS, Botón de Pago, QRI, RxT (→ Adquirencia) · Rubro: Resumen de Tarjetas de Crédito · Tamaño: Pequeño · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/29f6fb7696114311bc01a1c2ab400b15

**Modelo de negocio:** tarjeta regional (LAZONAL S.A.); cobranza de resúmenes.
**Pricing:** TD 0,75% · TC 1,70% (dada de baja a pedido del comercio) · QR 0,8% **con split** (Banco de Santa Fe) · CVU Collector Debin 0,75%.
**Particularidades:** ejemplo de QR con split hacia banco provincial.

## TARJETA UNICA
> Estado: En producción · Productos: QRI, RxT (→ Adquirencia) · Rubro: Resumen de Tarjetas de Crédito · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2024-12-02 · Fuente: https://app.notion.com/59cf760193554273a9d89b96bb34e2aa

**Modelo de negocio:** cobranza de resúmenes de tarjeta de crédito regional.
**Pricing:** QR 0,75% en línea · RxT 0,45% 24hs hábiles.

## SUCREDITO
> Estado: En producción · Productos: Botón de Pago, QRI, POS, RxT (→ Adquirencia) · Rubro: Resumen de Tarjetas de Crédito · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-04-22 · Fuente: https://app.notion.com/eff179fb4d054fecad97a6b639290f68

**Modelo de negocio:** tarjeta regional del NOA (Tarjeta Sucrédito); cobro de resúmenes con Botón de Pago y QR.
**Pricing:** POS/Botón 0,7% (24/48hs) · QR 0,75% en línea.
**Particularidades / cronología:** abr-2026 — quieren **Wallet Services y Onboarding propio**; se acordó darles el Onboarding de Bind PSP con front de Bind PSP y Prueba de Vida (expansión de tarjeta regional hacia billetera).

## RIPSA
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Grande · Riesgo: Bajo · Última edición (Notion): 2024-12-02 · Fuente: https://app.notion.com/baf6f261eb8b4482a6dc82ea60e48dd5

**Modelo de negocio:** red de cobranza extrabancaria de impuestos y servicios (Red Informática de Pago).
**Pricing:** transferencia 0,8% · crédito 3% · débito 2,5% · POS $10.000/mes (gratis si supera 1M trx) · QR extrabancaria (según contrato).

## RAPICUOTAS
> Estado: En producción · Productos: RxT, Botón de Pago (→ Adquirencia) · Rubro: préstamos de consumo · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2025-01-27 · Fuente: https://app.notion.com/43f1cebb7c0d4e02be0f5228a25675d1

**Modelo de negocio:** lending de consumo; cobro de cuotas con RxT y Botón.
**Pricing:** RxT 0,45% (24hs) · Botón débito 0,75% (48hs) · crédito 1,74%.

## PMC
> Estado: En producción · Productos: (sin etiquetar; el servicio descripto corresponde a **Liquidador**) · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/292900cbc0104cfca36d7cd1149e1c32

**Modelo de negocio — servicio Liquidador impositivo:** Bind PSP realiza el cálculo de retenciones y percepciones impositivas, rendición, liquidación y **pago a los ENTES** de la cobranza de impuestos y servicios que PMC hace por cuenta y orden de ellos, entregando archivos de output para presentaciones fiscales y controles.
**Cómo opera:** INPUT diario — PMC publica las novedades/transacciones a liquidar antes de las 9 am (SFTP con archivo plano, mail, o APIs de Bind PSP; diseño de archivo definido por la empresa). OUTPUT diario — Bind publica las liquidaciones realizadas antes de las 11 pm (SFTP/mail/eventos a URL del cliente) + resumen de liquidación para los ENTES. Condición: PMC acredita los fondos recaudados en la cuenta de Bind PSP antes de las 16 hs de cada día hábil.
**Particularidades:** único brochure que documenta en detalle el producto **Liquidador** como servicio standalone.

## PAGOS DIGITALES
> Estado: En producción · Productos: QRI, Wallet, Botón de Pago (→ Adquirencia + Wallet) · Rubro: Billetera, Retail · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-03-27 · Fuente: https://app.notion.com/cb243125244542e5ac9fa6f4eb2662f1

**Modelo de negocio:** emisor de **Tarjetas Prepagas VISA para operatoria corporativa** de comercios (empleados/socios consumen con saldo asignado; 95% tarjetas virtuales). Necesitan de Bind la CVU y cuenta recaudadora para el fondeo por parte de los comercios y para pagarle a VISA: una **CVU por comercio** (todas CUIT Pagos Digitales) recibe transferencias *same name*, los pesos van a la cuenta 322 de Pagos Digitales y desde ahí pagan a VISA; mientras tanto invierten los saldos. Comercios ejemplo: Sushipop, Elephant, Rabieta, Moura, Grupo San Miguel.
**Status detallado (Comercial):** 19/03/2026 — todas las nuevas facturas con bonificación del 25%.
**Volúmenes / datos duros:** mueven ~$1.200 millones/mes; a ago-2025 tenían 900 CVUs de Wallet Service con endpoint de eventos configurado.
**Pricing:** TC y prepaga 2,5% (18 días hábiles) · TD 1,5% (2 días) · cuenta activa $10/mes · cash in/out 0,3% (mín $20, máx $350) · licencia PSP USD 2.500/mes (bonif. 50% primeros 6 meses) · Onboarding USD 0,9/trx · facturación mínima USD 2.500.
**Particularidades / cronología:** **Moura** — POS con operatoria agrupadora (talleres cobran, acredita en Pagos Digitales, que reliquida a Moura y a los talleres con solución propia); inicio pruebas abr con 20 comercios. **Bingo Ciudadela** — POS (TD 1,5%) y QR (0,7%) para compra de fichas. **MUTE** — app en testing interno de Android.

## TRADENEO
> Estado: En producción · Productos: QRI, POS, RxT (→ Adquirencia) · Rubro: Retail · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2024-12-09 · Fuente: https://app.notion.com/153b3646c94b806f8c67dfae07c0fcc4

**Modelo de negocio:** supermercados.
**Pricing:** QR 0,8% en línea · RxT 0,35% (1 día hábil) · débito y crédito 2,66% (2 y 18 días hábiles).

## CONSEJO DE CIENCIAS ECONOMICAS
> Estado: En producción · Productos: QRI (→ Adquirencia) · Última edición (Notion): 2025-07-31 · Fuente: https://app.notion.com/154b3646c94b80e78743c56fbbfe381c

**Status detallado (Comercial):** 14/07 — QR productivo, negociando Botón de Pago · 31/07 — negociación por Botón de Pago frenada.

## CREDIMAS
> Estado: En producción · Productos: Botón de Pago, POS, QRI (+ RxT adquirido) (→ Adquirencia) · Rubro: Resumen de Tarjetas de Crédito · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-05-07 · Fuente: https://app.notion.com/154b3646c94b80ed9b9acca822a08d7e

**Modelo de negocio:** tarjeta regional (Tucumán); cobro de cuotas crediticias con soluciones de cobro presentes y no presentes. Integración API.
**Status detallado (Comercial):** 12/03 — suman QR (desintegrado primero, luego integrado por API) y RxT · 26/03 — carta de aceptación recibida para usar QR en sus POS · 23/04 — **ya operan con QR en el POS**.
**Pricing:** Transferencias 3.0: 0,5% · TD 0,7%.

## CRUZ DEL SUR
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: Transporte · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2024-12-12 · Fuente: https://app.notion.com/154b3646c94b805bafcfddb19ca874e1

**Modelo de negocio:** empresa de transporte (Victor Masson); recauda con QR interoperable en rubro transporte.
**Pricing:** QR 0,8%, acreditación inmediata.

## ELEBAR (Santa Mónica)
> Estado: En producción · Productos: Botón de Pago, QRI, RxT (+ POS adquirido) (→ Adquirencia) · Rubro: Resumen de Tarjetas de Crédito · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-03-06 · Fuente: https://app.notion.com/154b3646c94b80068680cbe5562a401e

**Modelo de negocio:** Santa Mónica S.A. administra la **Tarjeta Elebar** (financiación de consumo en PBA, red de comercios adheridos, fideicomisos financieros). Usa RxT y Botón de Pago para el cobro de resúmenes.
**Pricing:** Botón de Pago débito 0,7% (2 días hábiles) · RxT 0,5% (1 día hábil).

## GO CUOTAS
> Estado: En producción · Rubro: préstamos de consumo · Tamaño: Pequeño · Última edición (Notion): 2025-12-04 · Fuente: https://app.notion.com/154b3646c94b805a9ed5f2ba16f5ae4a

**Particularidades / cronología:** dic-2025 — el cliente separó sus modelos de negocio **GOCuotas y GOqr** con una nueva razón social (Finanzas Digitales SAS, fantasía "GOqr"): se creó una nueva cuenta + CVU **dentro de la organización existente** de GOCuotas a nombre de la nueva razón social. Caso de multi-razón-social dentro de una misma organización Wallet.

## GRUPO SLOTS - Jugadon
> Estado: En producción · Productos: RxT, Agente de Cobros y Pagos (→ Adquirencia + Agente de CyP) · Rubro: Gambling · Tamaño: Mediano · Riesgo: Alto · Última edición (Notion): 2025-08-11 · Fuente: https://app.notion.com/154b3646c94b8077b642c419c4f18344

**Modelo de negocio:** juego online (**Jugadón**, marca de Grupo Slots) — el cliente se onboardea en la web y tiene saldo virtual. **RxT fondea el saldo virtual** del jugador; Bind como **Agente de Pagos** paga premios/retiros (evolución del modelo: hoy TotalCoin da el in/out). Grupo de 3 razones sociales con licencias provinciales distintas (CABA, San Luis, Córdoba, Mendoza, La Rioja); la liquidación va a cada razón social.
**Cómo opera los productos:** 3 comercios (San Luis, La Rioja, Córdoba), todos mismo CUIT, cada uno con 1 caja y **1 collector único por caja** (para que RxT aplique), los 3 collectors acreditan en la misma cuenta recaudadora. Transferencias salientes **solo por API** hasta que exista Out por Portal Web en Ag CyP; nunca hay saldo de Ag CyP — el único saldo es el de la cuenta recaudadora y el saldo por provincia lo lleva Jugadón. Convenio: Agente de CyP con N CVUs asignados a clientes pero todos a nombre de la entidad.
**Status detallado (Comercial):** 14/07 — en espera de envío de credenciales de PROD (go-live 13/08/25).
**Volúmenes / datos duros:** 75.000 trx/mes entre las 3 razones sociales · ticket promedio $40.000 · 30.000 clientes.
**Pricing:** 0,36% y 48hs.
**Particularidades:** juego presencial — quieren convertir **Boxy** (sistema de puntos en las máquinas, junto a EVA System) en billetera: cerrada para consumo pero abierta para in/out, CVU a nombre del cliente, lectura de QR solo en slots. Cuidado explícito: NO ofrecer PCT en ese esquema.

## PAY EVOLUTION (Europagos)
> Estado: En producción · Productos: RxT, QRI (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-05-14 · Fuente: https://app.notion.com/154b3646c94b808ea1f6ee19e90c8b61

**Modelo de negocio:** payins/cobranzas (More Payment Evolution).
**Pricing:** RxT 0,3% · QR: 0,05% + escala por volumen: 0,15% (hasta $16.942,5M) → 0,14% → 0,13% → 0,12% (más de $67.770M) · transf 0,8% · crédito 3% · débito 2,5% · POS $10.000/mes (gratis si supera 1M trx).

## TRAVEL DREAMERS
> Estado: En producción · Productos: Botón de Pago (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b802f9571f9c8a6428959

**Modelo de negocio:** conserjería de turismo receptivo — paquetes en Argentina exclusivamente para extranjeros (sin aéreos). La agencia genera **links de pago** para que el viajero pague la excursión desde su país de origen. Un solo número de comercio. Integración API.
**Pricing:** TD 2,5% · TC 2,5% · QR 0,80% · setup USD 1.000. Plazos: PCT 3.0 inmediato, transferencia 24hs, TD 48hs, TC 18 días hábiles.

## WICO
> Estado: En producción · Productos: QRI, POS, RxT, Onboarding, Wallet (→ Adquirencia + Onboarding + Wallet) · Rubro: Refinerías · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/154b3646c94b8066b949fb9dd560f974

**Modelo de negocio — "Fintech as a Service" completo:** Grupo WICO obtuvo licencia PSP del BCRA y necesitaba activarla (regímenes informativos antes de ago-2024). Bind le arma el ecosistema completo: **app billetera marca blanca** (CVU por usuario bajo licencia PSP de Wico, transferencias in/out), Onboarding (Renaper, AFIP, Worldsys), lectura de QR interoperable, y red de adquirencia propia (QR Aceptador, RxT, POS) para rentabilizar el ecosistema. Modelo 2025: Wico Refinería compra crudo y vende a las estaciones de servicio (EESS).
**Pricing:** setup USD 45.000 (25% a la firma, 75% al go-live) · segunda etapa FCI: USD 30.000 en 4 cuotas · abono mensual mantenimiento/alojamiento USD 10.000 · OB USD 2/proceso · cash in/out según API Bank · lectura QR 0,2% · QR Aceptador 0,2% · TC/TD 0,35% + costo arancel adquirente · RxT 0,35% · canon POS $15.000 c/u (bonificado sobre $2M/mes por terminal, actualizable por IPC) · mínimo de facturación USD 5.000 desde el mes 5 · bonificación 50% hasta USD 30.000 al productivizar Cuenta Remunerada. Plazos: QR inmediato, RxT/TD 24hs, TC 20 días.
**Particularidades:** es el contrato white-label Wallet de referencia (junto a Astropay); el gatillo de bonificación atado a **Cuenta Remunerada/FCI** conecta con la Epic WS-1.

## GRUPO DESA (Edelap/Edesa/Edea/Eden)
> Estado: En producción · Productos: QRI, RxT, Botón de Pago (→ Adquirencia, Botón 2.0) · Última edición (Notion): 2026-06-26 · Última edición (Cerebro): 2026-08-04 · Fuente: https://app.notion.com/165b3646c94b80259054d463ab3495b5

**Modelo de negocio:** grupo de 5 distribuidoras eléctricas (servicio público) cuyo **recaudador es RIPSA** (misma razón social/CUIT). Consumen **Botón Simple 2.0** con condiciones comerciales propias por empresa.
**Cómo opera los productos:** 5 entidades / 5 cuentas recaudadoras / 5 collectors — CUIT y razón social RIPSA, nombre de fantasía de cada distribuidora (Edelap, Edesa, Edea, Eden, Edes). Se crean **3 comercios por entidad, uno por medio de pago** (RxT / QR / Botón). Jun-2026: ID Site 00091168 con establecimientos por bandera (VISA, MC, Cabal, Amex, Discover).
**Pricing (+IVA):** QR 0,05% arancel COELSA + 0,55% facturado a fin de mes (24hs; RIPSA debita el 0,55% adicional al cliente) · TD 0,6% a 24hs (fee procesador 0,3%) · TC 1,10% a 18 días (arancel procesador 1%) · RxT 0,29% a 24hs.
**Particularidades / cronología:** seguimientos abr-may 2025: automatización de contracargos, paginación de Consulta Deuda / webhooks de cambios de estado, descripción en resúmenes de tarjeta ("BIND-Red informática de pagos" generaba contracargos → agregar nombre de la distribuidora), altas escalonadas EDESA/EDEN/EDEA/EDES en Payway y COELSA.
- **2026-08-04 (reunión "Repaso Semanal líderes"):** reactiva el pedido de automatización de contracargos (ya mencionado arriba desde 2025, nunca formalizado) — ahora con foco explícito por ser cliente de alto volumen. Ver PRD-146 y `tareas_producto.md` T-085. Aparte, su entidad Edesa reclamó transacciones pendientes del 7 de julio con inconsistencias entre el botón de pago y Payway, vinculadas a problemas previos de infraestructura (Rabbit) — seguimiento 100% de Engineering (Mauricio Campos), sin acción de Producto.

## VITA
> Estado: En producción (con historia de de-risking) · Productos: RxT, Botón de Pago, QRI (→ Adquirencia) · Rubro: Cripto · Riesgo: Bajo · Última edición (Notion): 2026-03-17 · Fuente: https://app.notion.com/168b3646c94b807aafaed30bf2b2ab50

**Modelo de negocio:** billetera para comprar cripto (Vita Wallet, pagos internacionales). Sus usuarios empresa (fintechs, empresas de servicios, startups) generan **links de pago en ARS** pagables con cualquier medio; al completarse el pago, el saldo se refleja en la app. Caso de uso RxT: el merchant genera un **CVU por checkout** para el pago de un producto/servicio.
**Volúmenes / datos duros:** estiman +500 CVUs y +USD 700K de volumen, con miras a crecer.
**Pricing:** PCT/CVU Collector/DEBIN 0,8% sin split (1 día hábil) · TD 2% (2 días) · TC 2,5% (18 días) · prepagas 2,5%.
**Particularidades / cronología:** PLD exige formularios por submerchant (mínimo 4). Ene-2026: Comité de De-Risking decide la baja → feb-2026: el cliente queda "con una amarilla". Mar-2026: la evolución de producto puede orientarse a **Agente de Cobros y Pagos**.

## PAG Brasil
> Estado: En producción · Productos: Agente de Cobros y Pagos, Wallet (→ Agente de CyP + Wallet) · Rubro: ALyCs · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2026-01-09 · Fuente: https://app.notion.com/170b3646c94b80529cf1ef991f22dff9

**Modelo de negocio — cross-border:** agregadora de pagos y subadquirente brasilera: procesa pagos con medios locales de Brasil (tarjetas vía adquirentes, **Pix y Boleto Bancario** vía bancos), actúa como agente de colecta de fondos en Brasil y agente de **eFX** (cambio para remesas al exterior) para comercios internacionales.
**Particularidades / cronología:** jul-2025 — busca darle a **Bancard (Paraguay)** la lectura e interpretación de QR argentino: un paraguayo paga en un comercio argentino con la app de su banco (misma operatoria que ya tienen productiva en PY con Pix — Itaú y Atlas). Los pesos deben debitarse online desde una CVU; Bancard ofrecería garantía en dólares en el exterior (sin riesgo de tipo de cambio). Es también el partner de la integración **API PIX** que usa Gallo.

## RAPIFAST (interfast)
> Estado: En producción · Productos: QRI, RxT, Botón de Pago (+TD/TC) (→ Adquirencia) · Rubro: Expensas · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-08-29 · Fuente: https://app.notion.com/170b3646c94b80b8ac8bc0aa57d780c1

**Modelo de negocio:** cobro de expensas (plataforma Interfast). Integración API.
**Pricing:** RxT 2,5%(*) · QR 0,05% + 0,45% de costo administrativo · TD 0,65% · TC 1,5%. (*) así figura en el brochure; posible tipeo de Comercial.
**Particularidades:** ⚠️ posible duplicado con la fila "INTERFAST" del log (ver gaps).

## Carrefour (BSF) — página sin título en Notion
> Estado: En producción · Productos: Wallet (PSP as a Service) · Rubro: Retail · Tamaño: Grande · Riesgo: Medio · Última edición (Notion): 2026-06-17 · Última edición (Cerebro): 2026-08-14 · Fuente: https://app.notion.com/17cb3646c94b805fb67acb20bd61b73f

**Modelo de negocio:** Bind presta a Carrefour (razón social **Banco de Servicios Financieros S.A.**) el servicio de **PSP as a Service (Wallet)** para ofrecer cuentas de pago a los usuarios de su plataforma. Particularidad clave: Carrefour deja las **CVUs de los clientes en saldo cero** — en cada transferencia entrante ejecutan un comprobante de débito en la CVU del cliente y un comprobante de crédito en la cuenta recaudadora de Bind, concentrando todo el dinero ahí, con el saldo 100% disponible para consumo vía **tarjeta prepaga de Payway**.
**Pricing:** abono mensual USD 5.000 (bonif. 40% meses 1-2, 20% meses 3-4) · cuenta activa $13/mes · cash in $15 · cash out 0,1% · lectura QR 0,2% · actualización trimestral por IPC (base dic-2024, gatillo si acumula +15%). **Ardid** (jun-2026): costo por trx $11 bonificado jun→dic 2026 + fee transaccional 1% con tope creciente ($300 en marzo → $650 desde noviembre).
**Particularidades / cronología:** oct-2025 — roadmap deseado: cuentas para menores, aumento del límite mensual ($2,5M) con PLD, servicio de compliance, Pago QR, PIX, compra de dólar, QR transporte, cripto. Abr-2026: tensión por incidente fraudulento (contexto del alta de Ardid/Monitoreo); pendiente adenda de nuevas condiciones (mientras tanto, bonificación por NC). Integrados con credenciales PROD para prueba de concepto vía waiver.
- **2026-07-20 (mail 2026-07-22):** reunión por las caídas del servicio durante julio (50% de inoperatividad en los primeros 20 días, ver gap `[2026-07-23] Caídas de Bind PSP en julio`) — Carrefour presiona internamente por el impacto en NPS/retención y **pide compensación/bonificación comercial**, escalada a Ema/Gustavo (ver T-051 en `tareas_producto.md`). Bind le ofreció como mitigación la nueva API de conciliación directa con Coelsa para recuperar transferencias entrantes sin notificación (ver [`wallet/debin_y_fondeo.md` §7.2](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md)), con la salvedad de que no cubre QR salientes ni transferencias salientes rechazadas.
- **2026-08-11:** Carrefour probó la API de conciliación ofrecida y recibió el error "Conciliación COELSA deshabilitada para la organización '69'" — la mitigación técnica ofrecida está bloqueada por una configuración pendiente del lado de Bind (ver [`wallet/debin_y_fondeo.md` §7.3](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md)). Sin respuesta en el hilo a la fecha.

## LEAMAX (planbok)
> Estado: En producción · Productos: POS, Botón de Pago, RxT, QRI (→ Adquirencia) · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-07-16 · Fuente: https://app.notion.com/17eb3646c94b80f9badde9cdb5e1ebd3

**Modelo de negocio:** pasarela de pagos con licencia PSP propia (banco sponsor: BIND) que desarrolló su billetera. Usa la solución de cobros de Bind en **modelo agrupador**: primer cliente, una cadena de ferreterías de AMBA — todos los comercios nacen con CUIT/razón social Leamax y nombre de fantasía del comercio real; todas las acreditaciones van a Leamax, que luego liquida a los comercios en CVUs propias (Bind no participa de la liquidación al comercio final).
**Status detallado (Comercial):** 16/07 — en producción con POS; proyecto de no menos de **200 equipos POS**.
**Pricing:** RxT 0,35% (1 día) · TD 2,5% (2 días) · TC 2,5% (18 días) · QR 0,8% en línea.

## CITY GAS
> Estado: En producción · Productos: QRI, POS, RxT (→ Adquirencia) · Rubro: Gas · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-06-18 · Fuente: https://app.notion.com/182b3646c94b801591a9f07f9b3e1309

**Modelo de negocio:** venta y distribución de garrafas y cilindros de gas (50+ años). Integración API.
**Pricing:** TD 1,8% (2 días) · TC 2,5% (18 días) · QR 0,8% (1 día) · CVU 0,3% (1 día).

## SPENA (SERVICIOS VIRTUALES)
> Estado: En producción · Productos: QRI, POS, RxT (→ Adquirencia + Agente de CyP vía Cobro Express) · Rubro: Retail · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2025-09-23 · Fuente: https://app.notion.com/184b3646c94b80b0bd95f647a76a7912

**Modelo de negocio:** red de recaudación (Claudio Spena) con dos entidades:
- **ENTIDAD SPENA COBROS** — N comercios todos CUIT Spena (nombre real del comercio como fantasía), segmentados por sucursales/cajas; RxT recauda por CAJA (la misma que usa el POS); QR sin split acreditando a la CVU de Spena; retenciones a un único sujeto; comercios acceden al Portal Web con **rol restringido** (ven transacciones/QR/RxT/links, NO liquidaciones); Spena consume el Admin y lleva la cuenta corriente de cada cliente (Bind no participa).
- **ENTIDAD SPENA WALLET** — modelo **SurFin**: un único comercio con una CVU para operar desde el Portal (transferencias in/out), justificada para reducir impacto de Imp. débitos y créditos.
**Relación con Cobro Express:** cobros de impuestos/servicios canalizan por CE (deuda de Spena con CE que compensa con el efectivo recaudado); cobros de productos propios son adquirencia de Spena. Sep-2025: evolución a contrato Ag de CyP + QR entre Bind/CE, 1 agente = 1 comercio todos CUIT CE, todo acredita en la CBU de CE (etapas: QR → TD con POS → RxT).
**Pricing:** transferencias 0,80% inmediato · TD 2% (2 días) · TC 2,5% (20 días — el cliente pidió no operar TC por el plazo, abr-2025) · uso del Front del comercio USD 6 (primeros 100 POS).

## COBROSNET (Bertinotti)
> Estado: En producción · Productos: QRI, RxT, POS (→ Adquirencia) · Rubro: Agente de cobros y pagos · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-03-25 · Fuente: https://app.notion.com/185b3646c94b8035b851e15ae1736de6

**Modelo de negocio:** consultora de software (SaaS administrativos, ej. Presta Express) enfocada en **operaciones del ámbito nocturno**; canaliza las cobranzas de sus productos con RxT segmentando clientes, QRI web/presencial y Botón de Pago.
**Volúmenes:** 1.500–2.000 operaciones/mes.
**Pricing:** TC 2,5% (18 días) · TD 1,5% (48hs) · QR 0,8% · RxT 0,5%.

## COTO CICSA
> Estado: En producción · Productos: QRI, Wallet, Onboarding (→ Adquirencia + Wallet + Onboarding) · Rubro: Retail · Tamaño: Grande · Última edición (Notion): 2026-05-26 · Última edición (Cerebro): 2026-08-07 · Fuente: https://app.notion.com/189b3646c94b809390b5f96887d5f325

**Modelo de negocio:** app de COTO en los stores para incentivar el consumo dentro del ecosistema: Bind provee la **cuenta virtual (CVU) con función de billetera interoperable** — pago QR, transferencias in/out, consumo en cajas COTO (eco cerrado) y pagos en otros QR (interoperable). Consumen Wallet Service, OB solo Renaper y QR Aceptador; Daxia integra la solución de caja y Globant construye la app.
**Cómo opera los productos:** QR Aceptador — N comercios (uno por sucursal), todos CUIT COTO, todos liquidando en **la misma CVU de Wallet** (entidad 184, sin split, acreditación online; probado en STG sin romper). **Dos CVUs**: una espeja los consumos en cajas (cada débito del cliente = crédito en la CVU de COTO; la tesorería se lleva los fondos por API Bank, cuidando DyC/SIRCREB por misma titularidad) y otra de acreditación de solución de cobros (SIRTAC descontado en batch). Tope $500M por trx en ambas.
**Pricing:** QR en Coto Digital $17,08/trx · extracción por caja $17,08/trx · tarjetas con QR Coto Digital $6,57/trx · QR interoperable 0,6%.
**Volúmenes / proyección:** 100.000 clientes mes 1 → 225.000 mes 6 → 650.000 mes 12. F&F nov-2025 con 5.000 usuarios. Sucursal Botánico sale al público el 15/06/26: 90.000 clientes, 3.000 clientes/día, 180.000 ventas en caja.
**Particularidades / cronología:** 2026 — **Ardid/Monitoreo Transaccional** a PROD para Wallet (may-26) y Pago Eco Cerrado (30/06), luego tarjetas; interés en FCI, compra de dólar, cripto, cuenta en USD (evolutivos); Onboarding con prueba de vida activa (planifican sept/oct-26); cruce manual contra listas antiterroristas al cierre del día (plazo 30/06); PCT eco abierto debe finalizar antes del 3er trimestre.
- **2026-07-15 (mail):** bug confirmado en el archivo `BOTONLIQ` — no incluía devoluciones de días anteriores a la fecha de liquidación pese al desarrollo ya hecho para eso. Resuelto ad hoc (archivo corregido subido al ticket `BP-48516`) dos semanas después del reporte; sin confirmación de fix de raíz en producción. Detalle técnico en [`detalle_productos/adquirencia/liquidaciones_y_devoluciones.md` §1.1](../../3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md).
- **2026-07-29 (reunión "OB COTO - Validación de Vida Activa"):** Coto incorpora **AWS Rekognition** (liveness/prueba de vida) como capa adicional sobre la validación actual contra RENAPER — reduce el riesgo de suplantación por foto/video/IA; operativo estimado para **septiembre-2026** (fecha ya conocida en la ficha, mencionada primero por Comercial). Umbral de confianza inicial 90% (ajustable). Hasta la entrada en vigencia, Coto mantiene controles manuales reforzados y restricciones al alta de cuentas. Por mandato de Compliance, Bind PSP le pidió a Coto documentación/evidencia del proceso de validación para resguardar el legajo también de su lado — ver `tareas_producto.md` T-072.
- **2026-08-03 (mail, seguimiento ticket `BOTONLIQ`):** Bind (Eugenia Vila) suma a Nicolás Colón al hilo del bug de devoluciones no incluidas — escalamiento interno, sin novedad de contenido. En paralelo, el informe semanal de Adquirencia (31/07) reportó a este ticket (interno 2171/DAD-2171) como reactivado con urgencia por pedido explícito de Coto, con Emma Vignoles calificando la ejecución como "mal organizado el requerimiento, mal el análisis, y peor las demoras — Coto lleva 3 semanas de atraso". Detalle técnico en [`detalle_productos/adquirencia/liquidaciones_y_devoluciones.md` §1.1](../../3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md).
- **2026-08-04 (reunión "Repaso Semanal líderes"):** Emma Vignoles reafirma que el fix del ticket 2171/2209 no debe ampliar su alcance pese a las discrepancias de fecha detectadas — ver `decisiones.md` y `tareas_producto.md` T-074. Aparte, Coto sigue operando de forma conservadora en la sucursal Botánico; la expansión masiva queda supeditada a la estabilidad de Ardid.
- **2026-08-07 (mail, informe semanal Adquirencia):** el fix del ticket 2171 (DAD-2171/BOTONLIQ) salió a producción en la versión 71.1 del 06/08 — devoluciones parciales agregadas al archivo + fixes de idempotencia, transacciones diferidas nocturnas, devoluciones de QR y plazos de liquidación en fin de semana. Fintexa aclara que sigue resolviendo hallazgos menores del desarrollo; el pedido de COTO de exponer el archivo de devoluciones **por API** (en vez de proceso manual) sigue sin atender. Ver `tareas_producto.md` T-018/T-074 y `detalle_productos/adquirencia/liquidaciones_y_devoluciones.md`.

## CUCURU
> Estado: En producción · Productos: Agente de Cobros y Pagos, RxT (→ Agente de CyP + Adquirencia) · Rubro: Billetera · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-01-05 · Fuente: https://app.notion.com/192b3646c94b8060ac4fd7421b5e87d3

**Modelo de negocio:** infraestructura de cobro y automatización (Argentina y México). Da a distintas empresas la posibilidad de generar **CVUs para RxT**; en línea toman los fondos desde la CVU de Bind y los transfieren vía Agente de CyP a las cuentas que las empresas indiquen. **El dinero no pasa por la cuenta de Cucurú.**
**Pricing:** recaudación (RxT o Ag CyP) 0,25% con mínimo mensual USD 1.000 (desde jul-2025) · pagos 0,10% (bonificado si recauda ≥$50M/mes, actualizable por IPC).
**Particularidades:** jul-2025 — operación con **YPF** vía DEBIN spot.

## CAPTAR
> Estado: En producción · Productos: QRI, POS, RxT (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-03-17 · Fuente: https://app.notion.com/198b3646c94b8066b693d57ae8fd81bf

**Modelo de negocio:** red extrabancaria de Mendoza; cobranza de servicios e impuestos por cuenta y orden de terceros (Telecom, Movistar, expensas de consorcios).
**Pricing:** arancel aceptador 0,05% sobre trx de solución de cobros + arancel administrador 0,25% · TC 1,5% (18 días) · TD 0,5% (2 días) · QR en línea. Pendiente habilitar arancel reducido.

## PAGOS DIGITALES (CREDMOURA)
> Estado: En producción · Productos: POS, QRI (→ Adquirencia) · Rubro: Billetera, Retail · Tamaño: Grande · Riesgo: Bajo · Última edición (Notion): 2025-08-04 · Fuente: https://app.notion.com/199b3646c94b80c98d2dc8746254175a

**Modelo de negocio:** operatoria **Moura** (baterías) con **Cuota Simple (3 y 6 cuotas)** — comercio 1916, MCC 5411. Bind da solución de cobros y liquida a una CBU de Pagos Digitales en BIND; de ahí transfieren a una CVU CUIT Pagos Digitales (provista por Bind PSP) y desde allí liquidan a los comercios/talleres. Debería existir 1 CVU por comercio aunque todas sean de Pagos Digitales.
**Pricing:** QR 0,80% (sin split) · lectura QR 0,3% · POS: facturación mínima por terminal $2,5M, si no $15.000 · TC 2,5% · TD 1,5% · mínimo transaccional USD 2.500/mes.

## Benajal S.A (Jony)
> Estado: En producción · Productos: POS, QRI (+ RxT en el modelo) (→ Adquirencia) · Rubro: Retail · Tamaño: Mediano · Riesgo: Alto · Última edición (Notion): 2025-07-21 · Fuente: https://app.notion.com/1a4b3646c94b80d3a7e2c48c22067cc1

**Modelo de negocio — "modelo Spena" aplicado:** Jony tiene una PSP propia (LOHAS, a activar), ~200 **agencias** propias de recaudación de impuestos/servicios (para CE y Ripsa) y ~100 **comercios** no propios (telas/indumentaria de Once, La Salada, Flores). A los comercios se les da la solución de cobros (RxT, QR, POS) todos con CUIT/CBU de Jony (nombre de fantasía real); la liquidación acredita en la CBU de Jony. Con el dinero digital paga a la red extrabancaria, y con el efectivo de las agencias paga en pesos físicos a los comercios cobrando un % por la conversión digital→físico.
**Arquitectura aprobada (v. 23/05):** cada comercio vinculado a una única CVU CUIT Jony (solo cash-in por liquidaciones de Bind y cash-out cuando Jony paga); comercios sin transferencias salientes (la CVU funciona como cta. cte.), con Portal Web para consultar cobranzas/liquidaciones/saldo; Jony gestiona todo desde el Admin con **comprobantes de débito/crédito** espejados contra una CVU operativa propia (segundo segmento, solo transferencias salientes hacia Redex). Condiciones PLD: cadena de contratos Benajal→comercio, Benajal→CE/Pagos Dica, CE/Pagos Dica→SEPSA/GIRE; fondos solo transferibles a CE/Pagos Dica; máx. 100 comercios por razón social; tope $20M/mes por comercio. Arranque: 5 comercios en producción sin contrato firmado (con fecha límite).
**Volúmenes:** entre $10M y $100M por día.
**Pricing:** QR 0,6% arancel + 0,2% facturado a fin de mes (24hs) · TD 2,5% (48hs) · TC 3,5% (20 días) · RxT 0,35% (1 día) · mínimo mensual: USD 20.000 (meses 1-3) → USD 30.000 (mes 4) → USD 40.000 (desde mes 5).

## Peak Travel (Terramundi S.A.)
> Estado: En producción · Productos: Botón de Pago, QRI, RxT (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-04-16 · Fuente: https://app.notion.com/1a7b3646c94b805ca0a3df5b15116a06

**Modelo de negocio:** turismo educativo (viajes de estudio dentro del país); integra RxT, QR y Botón Simple a su web para cobrar las cuotas mensuales de cada alumno. Dos números de comercio separados (uno TC, otro TD) para poder operar **Cuota Simple** por link de pago.
**Status detallado (Comercial):** 12/03 — suma QR y RxT a su operatoria, contrato actualizado.
**Volúmenes:** ~6.500 trx/mes · ~$6.000 millones · ticket promedio ~$90.000 · 9.000-10.000 usuarios.
**Pricing:** QR 0,80% en línea · TC 1,8% (18 días) · TD 0,8% (48hs) · prepagas 1,8% · CVU Collector 0,4% (1 día).

## LOHAS SA
> Estado: En producción · Productos: Wallet · Tamaño: Pequeño · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/1b4b3646c94b808c9aa8e0cc134411c2

**Modelo de negocio:** se asoció a una PSP (es la PSP vinculada a Jony/Benajal) y busca Wallet Service + operación de la PSP. Alcance a confirmar: gestión de PSP propia, PLD, Onboarding, soluciones de cobro, Wallet Services, front comercios. Propuesta de wallet service enviada en mar-2025.

## Latam Recovery
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: Agente de cobros y pagos · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-07-16 · Fuente: https://app.notion.com/1bcb3646c94b804cafcaf3ba7ad0844d

**Modelo de negocio:** empresa de recupero de deudas / contact center / adquisición de créditos non-performing; usa el QR de Bind para el **pago de deudas** por parte de los deudores. Integración API.
**Status detallado (Comercial):** 16/07 — avisado que está en comisión 0.
**Pricing:** QR 0,80%, en línea.

## CONSORCIO ABIERTO
> Estado: En producción · Productos: Botón de Pago, Wallet, QRI, RxT (→ Adquirencia + Wallet) · Rubro: Expensas · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-06-24 · Fuente: https://app.notion.com/1cab3646c94b802198bfc393af8701c3

**Modelo de negocio:** ERP de administración de consorcios que integra cobranza y tesorería: **un CVU exclusivo por administración** (provisto vía Wallet), pagos de expensas por QR/Botón/RxT, y transferencias gestionadas desde el propio front de Consorcio Abierto. Los fondos recaudados en la cuenta recaudadora de Bind se invierten en **FCI/Money Market con ganancia compartida 50/50** entre Bind PSP y CA.
**Status detallado (Comercial):** 22/09 — riesgo de caída del acuerdo de exclusividad si no salen a PROD · 12/12 — salen a PROD el 16/12.
**Volúmenes:** ~$4.000 millones/mes (de $25.000 millones que recaudan los consorcios) · 3.500 consorcios.
**Cómo opera los productos:** PSP 184 para WS y solución de cobros. QR acredita online en la CVU del comercio; Botón y RxT acreditan unificado (2 transferencias/día) a la CVU de Bind en la cuenta /60. Facturación: los comercios facturan vía CA (entidad excluida de facturación normal); Bind calcula manualmente su comisión; la diferencia bruto-neto queda temporalmente en /2 (BP) y /68 (RxT) — comisiones Bind + comisiones CA + retenciones donde CA es agente; Bind emite los TXT para el fisco y CA presenta y paga.
**Pricing:** WS 0,6% cash in sobre todos los movimientos (internos y externos), cash out sin costo · RxT 0,6% mín $20 máx $350 (se configura 1% y el resto se paga contra factura a CA) · MM 50/50.
**Particularidades / cronología:** dic-2025 — no avanzan con el Onboarding de Bind (van con otro proveedor); jun-2026 — integran QR Aceptador, prueban DEBIN nuevos y reactivación de suscripciones OK, lanzamiento en redes; interés futuro en Agente de CyP; plan: evolucionar a FCI cuando CA le dé una wallet a cada unidad funcional.

## Gran Mutual Argentina de Vivienda
> Estado: En producción · Productos: QRI (→ Adquirencia) · Última edición (Notion): 2026-01-09 · Fuente: https://app.notion.com/1cab3646c94b80978402f80cb41be213

**Modelo de negocio:** planes de vivienda — al generarse la cuota de cada suscriptor se crea la orden de pago y **un QR asociado**, que se envía por email con el detalle; al pagarse, usan el **webhook** para conciliar, saldar la cuota y notificar al suscriptor. Alerta de PLD por los montos operados.

## WE COLLAB
> Estado: En producción · Productos: Agente de Cobros y Pagos (+ RxT) · Rubro: Creación de Contenidos · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-01-22 · Fuente: https://app.notion.com/1ceb3646c94b80b7a93fd444be149e3c

**Modelo de negocio:** marketplace que conecta creadores de contenido con marcas/consumidores. Los consumidores pagan por **RxT** (acredita en CBU de Bind PSP) y WeCollab usa **Agente de Cobros y Pagos** para pagarle a los creadores.
**Status detallado (Comercial):** 16/07 — contrato firmado, setup pago, integrando · 31/07 — resta conformidad de PLD y carga de convenios.
**Volúmenes:** 11.000 usuarios, 2.000 marcas, 500 usuarios activos diarios, trx promedio $50.000. Evalúan abrir B2C.

## MECAENPOL SRL
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: pagos · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-06-18 · Fuente: https://app.notion.com/1d7b3646c94b803a9c29e0a758928cb9

**Modelo de negocio:** cobra en pesos con **QR interoperable (Transferencias 3.0)** a usuarios locales que pagan productos/servicios vinculados a Mecaenpol; Bind procesa el cobro y liquida en ARS, y luego los fondos se convierten o transfieren según el circuito financiero de Mecaenpol. Integración API.
**Pricing:** QR 0,80% en línea.
**Particularidades:** al 12/05/25 quedaban preguntas abiertas de Comercial: cómo liquidan a los comercios, cómo expatrían los pesos, convenio modelo con sus comercios.

## AG COBRANZAS
> Estado: En producción · Productos: RxT (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-06-18 · Fuente: https://app.notion.com/1ddb3646c94b80669288e8f598198bef

**Modelo de negocio:** gestora de cobranzas de deudas de tarjetas regionales chicas (ej. Elebar) e impuestos/servicios menores. Uso **no integrado** de RxT: Bind le entrega los CVUs, y AG envía por mail/WhatsApp la deuda + el alias del CVU al deudor para que la pague. Los CVU salen con el nombre de fantasía "AG Cobranzas" (no la razón social).
**Pricing:** RxT 0,39%, acreditación día hábil siguiente.

## Asociación Ohel Abraham (Casa de Abraham)
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: servicios de organizaciones religiosas · Tamaño: Pequeño · Última edición (Notion): 2025-05-27 · Fuente: https://app.notion.com/1e0b3646c94b801daf4ef7eb85077251

**Modelo de negocio:** templo que **imprime el QR** para recibir donaciones de los fieles directo en su CBU.
**Pricing:** QR 0,60% en línea.

## Instituto Fleming
> Estado: En producción · Productos: Botón de Pago (→ Adquirencia) · Rubro: Medicina · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-07-14 · Fuente: https://app.notion.com/1e4b3646c94b80f38e13f25e4fdff0f8

**Modelo de negocio:** venta de actividades académicas médicas (cursos, fellowships, workshops, jornadas) desde su web educativa integrada con **Moodle**, con Botón de Pago integrado. Vigencia del link de pago: 1 día. La validación del pagador es implícita (alumnos que cursan; si desconocen una trx no pueden seguir el curso).
**Pricing:** transferencias 0,30% (1 día) · TD 0,80% (2 días) · TC nacional y prepaga 1,80% (18 días) · TC internacional 4% (20 días) · QR 0,80% en línea.

## GECSA S.A. (Carga al Toque)
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: Luz/Recargas · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-02-02 · Fuente: https://app.notion.com/1e5b3646c94b80a2835beb81e35b6c8e

**Modelo de negocio:** procesamiento y recaudación de **recargas de servicios prepagos** (telefonía celular, transporte público, TV) por cuenta y orden de las telcos; da integración tecnológica a empresas colegas y quiere ofrecerles cobro con QR. Red: 15 distribuidores con ~50 agentes cada uno (PLAFT autorizó mantener al cliente, feb-2026).
**Status detallado (Comercial):** 31/07 contrato firmado, integran QR · 07/08 pruebas en staging validadas por integraciones, faltan convenios.
**Pricing:** QR 0,8% en línea.

## REDDY (AGD)
> Estado: En producción · Productos: Wallet, QRI (→ Wallet + Adquirencia) · Rubro: pagos/agro · Tamaño: Pequeño · Riesgo: Medio · Última edición (Notion): 2026-06-09 · Fuente: https://app.notion.com/1ebb3646c94b80a186dff04647562bac

**Modelo de negocio:** ecosistema **Agripagos (Aceitera General Deheza)** — wallet con **fondos tokenizados de productores agropecuarios** (granos → tokens); los tokens se consumen mediante la **lectura de QR** provista por Bind (Wallet Services, solo lectura e interpretación de QR). El e-cheq es el 80% de las salidas del ecosistema.
**Volúmenes:** ~USD 468 millones/año por el ecosistema · ~USD 33 millones/mes · 3.500-4.000 productores (3.500 CUITs inscriptos, 2.600 activos) · 75 comercios (37 activos).
**Pricing:** lectura de QR sin cargo.

## Latin Express Financial Services
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: remesas · Tamaño: Pequeño · Última edición (Notion): 2025-06-18 · Fuente: https://app.notion.com/1f1b3646c94b8060ac0ff4caa706f341

**Modelo de negocio:** remesadora — el usuario que quiere enviar dinero a un familiar lee el **QR interoperable (desintegrado, mundo presente)**, paga con su billetera, y Latin Express transfiere los fondos al destinatario. Reemplaza cobros en efectivo y transferencias manuales; etapa 2: QR integrado + RxT.
**Pricing:** QR 0,80%, acreditación 24hs hábiles, sin split.

## Compara en Casa
> Estado: En producción · Productos: RxT (etiqueta) — el servicio real es Agente de Cobros y Pagos + débito automático (→ Adquirencia + Agente de CyP) · Rubro: seguros · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-06-05 · Fuente: https://app.notion.com/1f8b3646c94b80509abdc217ae450f0f

**Modelo de negocio:** plataforma web de venta de seguros (acuerdos con 50 aseguradoras). Con **Agente de Cobros y Pagos** recauda las cuotas mensuales por varios medios (RxT, QR, tarjetas — código de comercio propio, acreditando en la recaudadora) y ~15 días después paga a las compañías de seguro vía Agente de Pagos. El rendimiento de los fondos mientras están en la recaudadora se comparte **50/50** con Bind.
**Cómo opera — débito automático con DEBI:** DEBI (integrador de Compara) procesa débitos automáticos recurrentes en **Payway** con números de establecimiento de Bind PSP e informa las trx a liquidar por la **API del Liquidador** (`informar-transaccion-liquidar`); ingresan a la BD TRX (rubro 11, vs 13 de botón), no a payment; recaudaciones liquida a la **subcuenta /90** asociada al collector de Ag CyP. Establecimientos: VISA MCC 4829 / Master MCC 6051 (aranceles red de cobranza: crédito 1 pago 1%, débito 0,30%).
**Status detallado (Comercial):** 14/07 — integrando por Tucuota.
**Pricing:** cash in 0,3% · cash out 0,3% · débito automático: TD 0,8% (1 día), TC/prepaga 1,8% (18 días). Propuesta recurrencia: TD 1% / TC 2%.

## OCTOPUS
> Estado: En producción · Productos: Botón de Pago, RxT (+ PCT, DEBIN Spot, tarjetas) (→ Adquirencia) · Rubro: Expensas · Tamaño: Mediano · Riesgo: Medio · Última edición (Notion): 2026-04-17 · Fuente: https://app.notion.com/207b3646c94b80d7bb1de7046ea1bab5

**Modelo de negocio:** plataforma de cobro de expensas (Collectify). El arancel al consorcio es total (Bind + Octopus) y Bind **retrocede el 0,4%** de los montos procesados a Octopus cada mes (con liquidación detallada y deducción de IIBB) — modelo de revenue share con el partner tecnológico.
**Pricing:** PCT 0,8% · DEBIN Spot 0,8% · TD 1,1% · TC 2,1% · RxT 0,8% + IVA.

## UALA (ALAU)
> Estado: En producción · Productos: Agente de Cobros y Pagos, Dolar CCL (→ Agente de CyP + Wallet/FX) · Última edición (Notion): 2025-09-22 · Fuente: https://app.notion.com/207b3646c94b804591f7c88638529c01

**Modelo de negocio — Servicio de Liquidación de Pagos cross-border:** Bind gestiona bajo mandato de ALAU transferencias por cuenta y orden del cliente, en Argentina y el exterior. Circuito FX: Bind debita semanalmente pesos de la cuenta de ALAU para **recomprar los dólares consumidos vía CCL con IVSA** (cotización coordinada por grupo de WhatsApp ALAU/IVSA/Bind); en el diario, con la información de MC, Bind transfiere **USDC a Lirium**. La garantía en pesos se coloca en Money Market. ALAU accede a la cuenta comitente y a la recaudadora.
**Pricing:** fees de IVSA sumados al precio; fees de Bind resumidos y facturados mensualmente.

## ARCOS DORADOS (McDonald's)
> Estado: En producción · Productos: Onboarding, Wallet, QRI (→ Onboarding + Wallet + Adquirencia) · Última edición (Notion): 2026-06-26 · Última edición (Cerebro): 2026-08-05 · Fuente: https://app.notion.com/211b3646c94b801687bdf13ce6136e37

**Modelo de negocio:** app McDonald's con **saldo prepago de ecosistema cerrado**: el cliente hace cash-in (solo transferencia en etapa 1: pull/DEBIN recurrente same-name o tradicional, tope $400.000/mes por CUIT) y consume únicamente en Arcos; cash-out solo como devolución ("botón de arrepentimiento" al mismo origen, o vía contact center a misma titularidad). Objetivo: migrar pagadores de TC/efectivo a la app. Similar al modelo YPF.
**Cómo opera los productos:** **Onboarding mínimo** (solo escaneo de DNI, listas por detrás, aprobación/rechazo automático sin backoffice); **cuentas para menores 13-18 años** (validación de vínculo filiatorio con adulto usuario de la wallet, atributo de relación entre IDs — desarrollo específico de Bind). Wallet con cuenta recaudadora por organización; en cobros, **dos comercios: QR Eco Cerrado y QR Eco Abierto**, recaudando en una CVU de su propia Wallet. Franquiciados: un comercio + CVU por franquicia con liquidación directa. QR interoperable de Bind en cajas y exclusivo en tótems. Comprobantes internos eco cerrado: 491/492 (PagoOnline crédito/débito, iniciado en app sin QR) y 515/516 (PagoQr débito/reversa).
**Status detallado (Comercial):** MOU firmado 12/09, credenciales completas al 26/09.
**Particularidades / cronología:** procesador de tarjetas Fiserv (evaluaron QR por Fiserv/Bind/mixto); F&F interno 15/05/26; evolutivos: wallet abierta (posible exigencia BCRA) con biometría y límites ampliados, FCI/cuenta remunerada, acompañamiento regional en otros países, MODO leyendo el QR de Bind con tarjetas, plástico embebido en la wallet. Costos en discusión abr-2026: OB de menores, SocialNet USD 2, mejora de costo QR/recarga.
**2026-07-22 (reunión, no brochure):** para su ecosistema cerrado necesitan identificar la sucursal al leer el QR con la billetera (sistemas de ventas y loyalty separados, sin integración entre sí) — piden código externo propio de sucursal. Reveló un gap técnico más amplio en la lectura de QR (productos/sucursal/terminal sin mapear en la respuesta) — ver detalle técnico en [`detalle_productos/adquirencia/botones_de_pago_y_qr.md`](../../3_recursos/detalle_productos/adquirencia/botones_de_pago_y_qr.md#gap-de-mapeo-en-la-lectura-de-qr-productos-sucursal-y-terminal-cliente-arcos-dorados-2026-07-22).
**2026-07-31 (reunión "Veamos Arcos Dorados", no brochure):** repaso general del proyecto — billetera y proceso de onboarding en etapa de prueba "friends and family" (empleados, ~2 meses). Registro liviano solo con DNI+selfie, matriz de riesgo 100% automática sin revisión manual de OB. Confirmación de mecánica de ecosistema cerrado: sin transferencia de fondos entre usuarios ni retiro (salvo excepción manual gestionada por soporte con verificación de identidad, para evitar fraude). QR es técnicamente interoperable pero limitado a los sistemas de Arcos por datos de PSP embebidos — **decisión: sin apertura a interoperabilidad total este año**, pese al riesgo de reclamos de usuarios a futuro. Incorporación de nuevas franquicias requiere documentación formal para su gestión financiera directa (altas vía Jira + asociación de cuentas bancarias, en curso). Roadmap técnico temprano (mesas de trabajo con áreas Legal/Compliance): onboarding para menores de edad y cuentas remuneradas. Límites de consumo mensuales segmentados por cliente, ampliables solo si el usuario cumple validaciones de Prevención de Lavado de Dinero (PLD).
**2026-08-04 (reunión "Repaso Semanal líderes", no brochure):** planea salida a clientes finales en **septiembre**, luego de las pruebas iniciales "friends and family" con empleados (ver entrada 2026-07-31).
**2026-08-05 (minuta "Daxia | Alineamiento validación Renaper", no brochure):** nuevo requerimiento de seguridad para los flujos de **eliminación de cuenta (Wallet) y cash-out** de la billetera de Arcos ("Daxia", desarrollada junto con Globant). Conclusiones: BIND confirmó que no hay obligación específica de re-validar contra RENAPER para eliminar una cuenta, pero sí debe haber evidencia suficiente de que quien pide la operación es el titular; Seguridad y DPO de Bind ratificaron que Arcos/Daxia **no debe almacenar fotos de DNI ni información documental**; el cash-out (devolución) solo puede ir a una cuenta de la misma titularidad. Dos alternativas en evaluación: (1) challenge in-app sobre el usuario ya autenticado (ej. OTP), o (2) flujo específico de BIND para validar el documento contra RENAPER, separado del onboarding, sin que Daxia manipule datos del DNI. Decisión final pendiente de DPO según riesgo y horizonte de uso; Bind (Adriana Endzeliz) se comprometió a responder antes de fin de semana, con una estimación de configuración técnica de ~1 semana una vez definido el mecanismo. Daxia evaluará el impacto en SDK/credenciales/integración si se elige el flujo de BIND.

## Global 66 (Argpagos SA)
> Estado: En producción · Productos: Wallet (+ Agente de CyP + RxT + lectura QR) · Rubro: Billetera · Tamaño: Pequeño · Última edición (Notion): 2026-05-22 · Última edición (Cerebro): 2026-08-05 · Fuente: https://app.notion.com/216b3646c94b80c8bb81f2251ebe8e25

**Modelo de negocio:** wallet regional (Chile, Perú, Colombia, Ecuador, México, Argentina) nacida para remesas y hoy con pagos B2B internacionales; en Argentina opera con licencia PSP propia (Argpagos, remesadora). Bind provee lectura e interpretación de QR para sus clientes, fondeo por RxT, y desde oct-2025 la **migración de su PSP de COMAFI a Bind** ("modelo Max Pay") con gestión de la PSP por Bind PSP. Para expatriar fondos (sin cuenta en el exterior) firma **Agente de CyP**: los pesos de consumos van a la sociedad chilena G81; volumen de expatriación 1,5-2 millones USD/mes (100-150 mil USD/día).
**Arquitectura:** 4 entidades — WS con PSP 184 (única CVU de Global66 para Pago QR), Ag CyP con PSP 184 (expatriación), WS con PSP propio (todas las CVUs de clientes) y Ag CyP con PSP propio.
**Volúmenes:** 300.000 clientes totales, 25.000 activos; 100.000 trx cash-in + 100.000 cash-out; empresas objetivo con facturación USD 1M.
**Pricing:** lectura QR sin costo (arancel iniciador 100% Bind) con mínimo USD 3.000 · WS con escalera: USD 5.000 (feb-abr/26, NC 50% en marzo por incidentes de migración) → USD 10.000 (may-jul) → USD 13.000 (ago-oct) → USD 15.000 (desde nov-26).
**Particularidades / cronología:** fix de collector RxT por CUENTA+SUBCUENTA (abr-26) para PSP propia; reclamo de performance en lectura/pago QR (orquestación PSP Global66 + PSP 184); interesados en tarjetas de crédito, agente de cobros en dólares, monitoreo transaccional (adenda en curso). 14-jul-2026: identificado como el cliente de **mayor impacto de tráfico sobre la infraestructura base** — ráfagas de más de 9.000 comprobantes/minuto que presionan la base de datos compartida; el equipo técnico evalúa contactarlo para pedir que distribuya el envío de comprobantes en vez de enviarlos en ráfaga, y definir rate limits (ver `wallet/otros_manuales.md §11` y tarea T-011). **2026-08-05 (reunión "Bind Global66, proximos pasos"):** el 20-jul-2026 se registraron 732 transacciones QR con 29% de rechazo (212), concentradas después de las 19hs, por inconsistencias de infraestructura con APIBanco/Coelsa durante julio — se abre ticket para pedir postmortem formal. Cliente evalúa homologar **billetera interoperable** (QR interoperable, cotización aparte del contrato vigente, ~2-3 meses de proceso) y **onboarding de personas jurídicas** vía Global (mismos endpoints que PF, documentación de compliance específica ya provista) — Cisc (motor impositivo) ya contempla PJ. Cambio técnico simplificador evaluado a futuro: operar débitos/créditos directo desde la CVU de BM PCP en vez de la cuenta de pagos actual.

## WASSA SRL
> Estado: En producción · Productos: RxT, POS, QRI (→ Adquirencia) · Rubro: Venta de Productos - Bazar · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-03-11 · Fuente: https://app.notion.com/216b3646c94b802d9416c7b6a75f3f5c

**Status detallado (Comercial):** 18/07 — convenios habilitados, POS configurados y enviados, 4 CVUs de alta; capacitación de Admin pendiente · 31/07 — el comercio pidió deshabilitar tarjetas de crédito y prepagas (configurado).

## Max Pay (Max Capital)
> Estado: En producción · Productos: Wallet (con licencia PSP propia) · Rubro: ALyCs · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-06-08 · Fuente: https://app.notion.com/22db3646c94b80e7a292ca1ef91c77c2

**Modelo de negocio:** Max Capital tiene dos razones sociales — Max Capital (ALyC) y **Max Pay** (PSP propio, Nro BCRA 34.584). Hoy opera con Banco Sponsor Coinag y rampa tecnológica Aginco; migra a **Bind como Banco Sponsor y rampa tecnológica**. Existen 2 entidades Wallet Service: Max Capital (PSP = Bind) y Max Pay (PSP = Max Pay). Licencia de las Soluciones Tecnológicas: SaaS, no transferible, no exclusiva (Bind puede licenciar el mismo modelo a otros PSPs terceros).
**Pricing:** setup USD 25.000 (bonif. 40% → USD 15.000) · onboarding USD 0,6/alta · gestión/mantenimiento PSP USD 15.000/mes (bonif. 40% primeros 3 meses → USD 9.000) · lectura QR 0,2%.
**Particularidades / cronología:** abr-2026 — quieren sumar **RxT con su propio PSP** (multiPSP) y volverse Agrupador ante BCRA; discusión de pagos cross-border. Conflicto de facturación: adeudan ~$41,4M desde enero (jun-2026, en renegociación).

## Gimnasios Argentinos (Megatlón)
> Estado: En producción (con baja evaluada) · Productos: RxT, Agente de Cobros y Pagos (→ Adquirencia + Agente de CyP) · Tamaño: Grande · Riesgo: Bajo · Última edición (Notion): 2026-02-19 · Fuente: https://app.notion.com/23eb3646c94b8038aa40d456baa3c66d

**Modelo de negocio:** cadena de gimnasios que recaudará pagos de empresas grandes vía **RxT desintegrado** (alias creados manualmente por Bind), acreditando en subcuenta PSP; el cash-out se haría vía Agente de Cobros y Pagos.
**Status detallado (Comercial):** 31/07 pendiente form de alta · 07/08 en PROD con RxT (6 CVUs), Ag CyP pendiente homologación · 18/12 **cero transacciones**, se evalúa dar de baja · 19/02 finalmente **no homologaron Ag CyP**, quedaron solo con RxT desintegrado.
**Pricing:** RxT 0,25% (1 día) · QR 0,8% en línea · TD 1,8% (2 días) · TC 2,5% (18 días).

## La Agrícola Regional (LAR Coop.)
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: Luz · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-04-16 · Fuente: https://app.notion.com/23fb3646c94b80f6b513c42ed4ce925e

**Modelo de negocio:** cooperativa agropecuaria y de servicios públicos que provee **energía eléctrica urbana directa al usuario** (Libertador San Martín, Puiggari, María Luisa, Racedo, Crespo) en Entre Ríos; usará QR como alternativa adicional de cobro de facturas. No cobra por cuenta y orden de terceros.
**Volúmenes:** ticket promedio $30.000-$50.000; facturación de nov (energía urbana) ~$540 millones (uso de QR estimado bajo al inicio).
**Pricing:** QR 0,8% en línea.

## Confluencia IT
> Estado: En producción · Productos: QRI, RxT, Botón de Pago (→ Adquirencia) · Rubro: Medicina · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-09-11 · Fuente: https://app.notion.com/23fb3646c94b80d5ad21d541d7ceb8a5

**Modelo de negocio:** empresa de tecnología para obras sociales, prepagas, clínicas y hospitales (consultoría, desarrollos a medida, gestión en la nube); procesa **coseguros y facturas** de sus clientes del sector salud y necesita integrarse a los medios de cobro de Bind.
**Status detallado (Comercial):** candidato a **arancel reducido** (TD/TC) por su actividad.
**Pricing:** QR 0,8% en línea · RxT 1 día hábil · TD 0,75% (2 días) · TC 1,75% (20 días).

## MANTECA (Plus Billetera)
> Estado: En producción · Productos: Wallet, Agente de Cobros y Pagos · Rubro: Cripto · Última edición (Notion): 2026-03-18 · Fuente: https://app.notion.com/23fb3646c94b80319305f02d2e54aa78

**Modelo de negocio:** "caso similar a Depay" — Wallet Service para pagos QR (Luzpay, Sixalime), con foco en mitigación de riesgos.
**Status detallado (Comercial):** 11/08 integrando Wallet · 22/09 falta firmar carta oferta para compartir el arancel.

## B&B Gas
> Estado: En producción · Productos: QRI, POS, RxT (→ Adquirencia) · Rubro: Gas · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-09-11 · Fuente: https://app.notion.com/240b3646c94b80e1b2f0dbda714b78b2

**Modelo de negocio:** venta de garrafas de gas en sucursal y reparto con camiones; usa los servicios **desintegrados** (QR web, alias RxT creados por Bind, POS TD/TC).
**Status detallado (Comercial):** 31/07 contrato firmado, acceso a Admin y web de comercios · 08/08 organización de capacitaciones (Admin, web, POS, CVUs).
**Pricing:** QR 0,8% (1 día) · TD 1,8% (2 días) · TC 2,5% (18 días) · RxT 0,3% (1 día).

## COOP UNION (Cooperativa Unión de Justiniano Posse)
> Estado: En producción · Productos: Wallet, Onboarding, Debin Recurrente (→ Wallet + Onboarding + Adquirencia) · Rubro: Billetera · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-06-22 · Fuente: https://app.notion.com/24cb3646c94b80e98ce2eaca91c1eaf8

**Modelo de negocio:** cooperativa **consignataria de granos** que da servicio integral al productor (acopio, fletes, insumos, combustible, seguros). Cada productor tiene una **Cuenta Corriente Cooperativa** (consumos en el debe, liquidaciones de cereal en el haber); el saldo positivo se puede retirar usando la CVU del productor como "puente". Además, socios de la mutual con saldo "mutualista" (hoy solo retirable en efectivo en la mutual) podrán disponibilizarlo a su CVU vía Wallet. La cooperativa desarrolla una **super app** con estas funciones (equipo propio: CF Tech, 10 personas).
**Cómo opera:** OB por "registro único" (solo selfie, sin video, "OB por partes" desde 16/may/25); Debin Recurrente fondea **exclusivamente** la CVU de la cooperativa; flujo de impuestos: Bind envía diariamente los pendientes (manual, mail/JIRA), la coop fondea las CVUs de los productores y debita para dejarlas en cero (sin "recycle"/débito automático).
**Status detallado (Comercial):** 31/10 PLD OK con límite $12.200.000/mes y OB completo en Bind requerido · 7/11 contratos firmados, reactivan integración · 12/12 piden cambios en el flujo de OB · 25/2 buscan salir a PROD fin de marzo · 9/4 piloto productivo con personas físicas · 10/4/26 PLD actualiza límite a $20.000.000/mes con envío previo de liquidaciones de los primeros 80 productores.
**Volúmenes:** ~2.600 transferencias/mes, promedio $6.000.000 (rango $100k-$50M), volumen mensual estimado $15.600.000.000; 1.600 usuarios (600 PJ, 1.000 PF).
**Pricing:** setup USD 5.000 · cash in/out 0,35% (máx $350, IPC) · lectura QR bonificada · mínimo mensual creciente USD 2.000→5.000 (meses 1-10) · Onboarding PF USD 1,1 / PJ USD 2,5.
**Particularidades / cronología:** 15/07/26 (reunión "Join Soporte Clientes") — pendiente de cierre el onboarding de persona jurídica: el equipo debe contrastar el feedback recibido de "Lu" con las notas de reuniones previas, validando las relaciones representativas contra Arca antes de habilitar la salida a producción.

## Crucero del Norte
> Estado: En producción · Productos: QRI, Botón de Pago (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-05-28 · Fuente: https://app.notion.com/24cb3646c94b80bfb4fccbab3906f3a3

**Modelo de negocio — 2 proyectos en paralelo con proveedores tecnológicos distintos:** (1) **QR interoperable** para cobro de pasajes en agencias físicas y a bordo (app de choferes); (2) **Botón Simple vía chatbot de WhatsApp** integrado al sistema de ventas, generando link de pago para TD/TC/prepaga.
**Status detallado (Comercial):** 18/9 contrato firmado, integrando en STG · 10/12 despriorizan QR para enfocarse en el chatbot con proveedor externo · 9/2 retoman ambos proyectos · 10/2 PLD dio el OK.
**Volúmenes:** facturado 2025 con medios electrónicos ~$900.000.000/mes, ~3.500 trx, ticket promedio $255.000.
**Pricing:** QRI 0,8% · TC 1,8% (18 días) · TD 1% (2 días) · TR 1,8% (18 días) · Transferencias 3.0/CVU collector 0,4% (1 día).

## Jardín Colorín Colorado (Selvarolo Julieta)
> Estado: En producción · Productos: RxT (→ Adquirencia) · Rubro: Educación · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-03-16 · Fuente: https://app.notion.com/25bb3646c94b809c9572ddcc36a6e16b

**Modelo de negocio:** jardín de infantes que provee **una CVU por cada alumno** para el pago de la mensualidad, vía RxT desintegrado.
**Pricing:** $150 fijos por transferencia.

## Remitee S.A.
> Estado: En producción · Productos: QRI, Wallet (→ Adquirencia + Wallet) · Rubro: Agrupador · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-06-04 · Fuente: https://app.notion.com/268b3646c94b8030a85cd2c2e71f02eb

**Modelo de negocio:** provee infraestructura para que **bancos, billeteras y adquirentes regionales** hagan cobros y pagos mediante el servicio de QR (lectura y generación) de Bind — un caso de "PSP para PSPs" vía QRI. No tiene OB propio: dará el servicio de lectura/interpretación de QR a sus propios clientes y depende de la firma de contrato de ellos para compartir la información (comparado internamente con el OB de **Getnet**).
**Status detallado (Comercial):** 11/09 ticket de QR levantado, wallet en negociación · 16/10 contratos QR iniciador (clean) y QR aceptador (con comentarios) enviados · 28/10 aceptaciones firmadas · 11/12 en PROD con QRi, prueba exitosa, mayor volumen requiere PLD por caso/comercio; Wallet arranca integración en 2026 · 03/06 credenciales productivas para comercio de prueba propio.
**Pricing:** QR 0,8% en línea.

## DINAMICS SOLUTIONS SA. (Klino)
> Estado: En producción · Productos: RxT, Agente de Pagos, Botón de Pago (→ Adquirencia + Agente de CyP) · Rubro: Limpieza · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-05-13 · Fuente: https://app.notion.com/268b3646c94b80cd8213d1b5b47a92df

**Modelo de negocio:** **Klino**, app que conecta clientes con "Kliners" — trabajadores independientes de limpieza ecológica de vehículos a domicilio (mínimo consumo de agua, productos biodegradables). El cliente paga desde la app (transferencia, TC o TD) vía RxT/Agente de CyP; Bind transfiere desde su CBU a los Kliners (Agente de CyP). Arranca en Rafaela.
**Status detallado (Comercial):** 11/09 OK de PLD, pendiente respuesta del cliente para el contrato · varias rondas de renegociación de contrato (oct-2025) · 11/12 contrato firmado, credenciales de staging enviadas · 26/02 nueva reunión con PLD para revalidar.
**Pricing:** QR 0,8% (1 día) · TD 1,8% (2 días) · TC 2,5% (18 días) · RxT 0,35% (1 día) · Ag CyP cash-out 0,25% · setup USD 2.500 · mínimo mensual escalonado USD 250 (meses 1-6) → USD 500 (7-12) → USD 1.000 (13+).

## CREDITIA FIDEICOMISO FINANCIERO
> Estado: En producción · Productos: QRI, RxT, Botón de Pago, Agente de Cobros y Pagos (→ Adquirencia + Agente de CyP) · Rubro: préstamos de consumo · Riesgo: Bajo · Última edición (Notion): 2026-07-03 · Fuente: https://app.notion.com/26bb3646c94b80d58348f036f71408f4

**Modelo de negocio:** fideicomiso financiero que cobra deudas de **carteras de crédito originadas por terceros** y adquiridas por el fideicomiso. Los ingresos se recaudan en una subcuenta de Bind; diariamente se hacen 1-2 extracciones a la cuenta bancaria de la entidad generante de la deuda, que luego imputa los pagos según el CVU asociado. Un CVU queda activo mientras el cliente pague; si cancela o incumple (rotando de agencia), se depura y se genera uno nuevo.
**Status detallado (Comercial):** proceso largo de compliance — 18/12 en análisis · 12/03/26 contrato firmado · 21/04 PLD pide APF extendido · 22/05 cliente lo envía · 17/06 **OK de PLD**.
**Volúmenes:** ~ARS $1.200M/mes, ticket promedio ARS $250.000.
**Pricing:** QR 0,8% (1 día) · TD 1,75% (2 días) · TC 2,5% (20 días) · RxT 0,3% (1 día) · cash-out Ag CyP bonificado (máx 1-2 transferencias diarias).

## Zona Sur Conectividad
> Estado: En producción · Productos: RxT (→ Adquirencia) · Rubro: Impuestos y Servicios · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-03-18 · Fuente: https://app.notion.com/271b3646c94b8037a953ee2e2897ad0e

**Modelo de negocio:** distribuidora de internet vía aire y cable; usa RxT **desintegrado** (CVU sin integración) para cobrar cuotas mensuales, clasificada en operación especial como empresa de servicios.
**Status detallado (Comercial):** 09/10 falta contrato · 16/10 contrato subido · 18/12 empieza a transaccionar en enero · 26/02 reclamo al banco por falta de transacciones — **finalmente comenzaron a operar**.
**Pricing:** RxT 0,35% (1 día hábil).

## Umbral Holistic Wellness (Coni Friedberg)
> Estado: En producción · Productos: Botón de Pago (solo link de pago, sin integración) · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2025-12-29 · Fuente: https://app.notion.com/273b3646c94b80e3a861f9768f5d1afb

**Modelo de negocio:** centro de bienestar holístico (clases y cursos) que solo usa **links de pago** compartidos manualmente a sus clientes, sin integración técnica.
**Status detallado (Comercial):** 19/9 firmó contrato para generación de link de pago; no se va a integrar.
**Pricing:** TC 2,5% (18 días) · TD 1,5% (2 días).

## Freestyle
> Estado: En producción · Productos: RxT (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-11-17 · Fuente: https://app.notion.com/277b3646c94b80329ad3e1531823cad3

**Modelo de negocio:** agencia de viajes de egresados que consume RxT vía la integración de **Cuoma (Pax Manager)** como intermediario tecnológico — un patrón de "sub-integrador" repetido en el ecosistema de viajes.
**Status detallado (Comercial):** 22/09 firma de contrato.
**Pricing:** RxT 0,5% total (0,35% Bind + 0,15% informado y facturado a Cuoma mensualmente), 24hs.

## Maeba SRL / FINANPRO SRL
> Estado: En producción · Productos: QRI (→ Adquirencia) · Rubro: préstamos de consumo · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-01-02 · Fuentes: https://app.notion.com/279b3646c94b804ea5f2c7ff320d3dff · https://app.notion.com/279b3646c94b80fba421e7355bae2169

**Modelo de negocio:** dos razones sociales distintas (Maeba SRL y Finanpro SRL) de los **mismos referentes/contactos**, dedicadas a préstamos de consumo directo y financiación de bienes (electrodomésticos, indumentaria) canalizados por comercios, con presencia en 15 provincias (~55 sucursales cada una). El **QR se expone en caja** para cobro presencial de cuotas — un comercio con múltiples sucursales/cajas, sin reversos ni e-commerce, sin incidentes masivos de fraude (casos aislados de "quiebra trucha", tema bajo investigación policial mencionado en la ficha).
**Status detallado (Comercial):** 02/10 contratos firmados, en integración · 18/12 credenciales compartidas, en monitoreo transaccional.
**Pricing:** QR 0,8% en línea.

## Fletalo SAS
> Estado: En producción · Productos: Botón de Pago 2.0 (→ Adquirencia) · Rubro: Transporte · Tamaño: Pequeño · Riesgo: Bajo · Última edición (Notion): 2026-01-14 · Fuente: https://app.notion.com/27eb3646c94b80bc896ffe40dca85e2f

**Modelo de negocio:** marketplace de última milla que interconecta **fleteros independientes** con clientes; usa Botón de Pago para tres casos: cobrar el total del flete, cobrar solo el fee/comisión (el resto va directo al fletero), o cobrar fees de viajes a los fleteros. Objetivo: reemplazar Mercado Pago (hoy usado por clientes low/mid de 2-8 viajes/mes) por Bindx. Ticket promedio $60.000.
**Status detallado (Comercial):** 02/10 contrato listo · 23/10 reclamo por demora en apertura de ambientes de homologación (setup ya facturado).
**Pricing:** QR 0,8% (1 día) · TD 2% (2 días) · TC 2,5% (18 días) · RxT 0,35% (1 día) · mínimo transaccional USD 500/mes · setup USD 1.000.

## Super Tour
> Estado: En producción (⚠️ duplicado con fila "En integración" del mismo cliente, ver gaps) · Productos: RxT (→ Adquirencia) · Rubro: Viajes y Turismo · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2025-11-17 · Fuente: https://app.notion.com/27eb3646c94b8025b34cda1edd8addac

**Modelo de negocio:** agencia especializada en viajes de primaria, mismos dueños que **Travel Rock**; se integra vía plataforma de **Daxia**.
**Pricing:** escalonado — 0,3% (hasta $3.000M) → 0,27% ($3.000-5.000M) → 0,25% (+$5.000M).

## EL JUMILLANO S.A. (IVESS)
> Estado: En producción · Productos: QRI, Botón de Pago, RxT (→ Adquirencia) · Rubro: Retail · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-04-22 · Fuente: https://app.notion.com/282b3646c94b801e84e2dd7f9407c3b4

**Modelo de negocio:** venta de aguas y sodas (IVESS) vía carrito de compras en su web, cobrando con QR/TD/TC/RxT.
**Cómo opera:** para RxT quieren que **cada cliente tenga su propio alias y CVU** — proceso encolado que crea individualmente cada caja con su alias (~800.000 clientes potenciales).
**Pricing:** QR 0,75% en línea · TD 1,8% (2 días) · TC 2,3% (18 días) · RxT 0,3% (1 día). Mismo grupo/contactos que Lufran S.A. (NAFA).

## Lufran S.A. (NAFA)
> Estado: En producción · Productos: RxT, QRI, Botón de Pago (→ Adquirencia) · Rubro: Retail · Tamaño: Mediano · Riesgo: Bajo · Última edición (Notion): 2026-01-14 · Fuente: https://app.notion.com/284b3646c94b804d87b7ec04b7a37cff

**Modelo de negocio:** venta de aguas y sodas (NAFA) vía carrito de compras en su web — mismos contactos administrativos que El Jumillano/IVESS.
**Status detallado (Comercial):** 18/12 credenciales productivas compartidas, en monitoreo.
**Pricing:** QR 0,75% (1 día) · RxT 0,30% (1 día) · TD 1,8% (2 días) · TC 2,3% (18 días).
