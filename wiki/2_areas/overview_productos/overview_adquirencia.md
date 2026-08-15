# Adquirencia — Overview de Producto

> Fuente: `raw/Product overview_Adquirencia.docx` (ingesta Fase 1, 2026-07-02). Área de negocio: [equipo.md](../overview_empresa/overview_equipo.md).

## Qué es

Producto de adquirencia de pagos. El cliente es una **Entidad**, que puede crear **comercios**; cada comercio puede crear **sucursales**, y cada sucursal, **cajas**. El objeto principal del sistema es la **Transacción** (con la forma de pago como atributo). Toda transacción acreditada o rechazada dispara una notificación **webhook** a la entidad.

## Origen del producto (histórico)

Nació enfocado en el cobro por **QR**. Para eso se necesitaba licencia de **Aceptador** en el BCRA (solo Bancos y PSP pueden ser Aceptadores). Como Bind PSP aún no tenía licencia de PSP, operó inicialmente bajo la licencia de Aceptador de **Banco Industrial** (**ID 164**). Al obtener la propia licencia de PSP, pasó a operar como **Bind PSP (ID 184)**. Ver decisión registrada en [decisiones.md](../direccion/decisiones.md).

Al principio, el cobro con QR creaba CVUs por comercio desde una cuenta recaudadora fija de titularidad de Banco Industrial; se cursaba con **Coelsa** y se hacía split automático a un CBU de titularidad del propio comercio dentro del mismo banco. QR se sigue procesando directo con Coelsa porque **API Bank no tiene esa funcionalidad**.

> 📄 La mecánica técnica completa del cobro QR (normativa CIMPRA/BCRA, flujo de mensajería con Coelsa, alta de comercio, comisiones de Interchange) está documentada en [mecanica_interna_productos/](../../3_recursos/detalle_productos/adquirencia/index.md) — es la misma infraestructura de Transferencia 3.0/3.1 que sustenta tanto el **cobro con QR de Adquirencia** (este documento) como el **pago con QR de Wallet** (ver [wallet_overview.md](overview_wallet.md)), ya que Bind PSP participa del mismo ecosistema interoperable en ambos roles (aceptador y billetera).

## Canales de cobro

| Canal | Descripción |
|---|---|
| **QR** | Vía Coelsa (directo). |
| **Botón simple 1.0** | Links de pago no presentes con checkout de tarjeta (débito/crédito/prepaga según reglas de pago del comercio). Checkout PCI compliant, marca blanca y customizable por comercio/entidad. |
| **Recaudación por transferencia** | Sinergia con **Agente de cobros y pagos** (ver [cobros_overview.md](overview_agente_cobros_y_pagos.md)). El comercio obtiene CVUs para que sus clientes transfieran; se conecta asociando un Collector a un comercio (todas las transferencias van a caja/sucursal/comercio/entidad fija) o asociando la entidad al collector con un CVU por caja. |
| **Botón simple 2.0** | Combina checkout de Botón simple 1.0 con pago por QR o transferencia a CVU, sobre el mecanismo de **Deuda de pago único** (un link = una deuda, pago único). El CVU solo se asigna si el usuario elige pagar por transferencia, con lógica de **reciclaje de CVUs** desde un lote precreado en Agente de cobros (se evita crear un CVU por cada deuda/link). La deuda puede tener varios vencimientos/montos y admite pagos parciales o múltiples transacciones si el canal es transferencia. |
| **POS (tarjeta presente)** | Cobro con tarjeta física en dispositivo. Bind PSP provee **SmartPOS marca Topwise, modelo T3**, con app Android embebida. El comercio se loguea en el POS y cobra desde allí con **QR o tarjeta**. Es el único canal donde hoy es posible ofrecer **planes de cuotas** para tarjeta. Se procesa con **Global Processing**. Cada POS (por *serial number*) se asocia a una **caja** — cobrar en un POS es cobrar en esa caja. Los cobros del POS también pueden gestionarse y consultarse en línea vía APIs. |

> **Nota — Planes de cuotas:** en **tarjeta no presente** (Botón simple 1.0/2.0) actualmente **no** es posible ofrecer planes de cuotas. Solo está disponible en el canal **POS** (tarjeta presente).

## Liquidaciones e impuestos (SISCRI)

- Proceso diario (días hábiles) que agrupa transacciones por comercio y medio de pago para liquidar el neto recaudado. Requiere que los impuestos ya estén calculados previamente.
- El cálculo de impuestos corre en **SISCRI** (instancia propia de Adquirencia — distinta de la de Wallet, ver [wallet_overview.md](overview_wallet.md)). SISCRI conoce cada comercio/entidad (se replican al crearse) y calcula impuesto según forma de pago, monto, CUIT, domicilio y **agente de retención** (que puede ser Bind PSP o Banco Industrial, asociado a la entidad).
  - Transacciones con **plazo de liquidación = 0**: se informan a SISCRI una por una, en línea.
  - Transacciones con **plazo de liquidación > 0**: se informan para cálculo por **lote**, procesado el día de liquidación.
  - SISCRI también actualiza padrones impositivos por provincia/agente recaudador, y genera automáticamente los archivos de información al fisco.
- El área **Impuestos y Contabilidad** (líder: Natalia Frea) es sponsor de SISCRI: detecta necesidades de actualización del software y gestiona/levanta los requerimientos de desarrollo correspondientes. Ver [equipo.md](../overview_empresa/overview_equipo.md).
- La liquidación física (transferencia del neto al CBU/CVU del comercio) la realiza el equipo de **Administración** (ver [equipo.md](../overview_empresa/overview_equipo.md)). Cada liquidación genera un resumen PDF accesible por Admin, Portal Comercio o APIs.
- En paralelo corre un proceso de **rendición** diario que agrupa rendiciones por comercio y genera archivos batch (por entidad y generales de Bind PSP).

## Configuración por comercio

- **Reglas de pago**: qué procesador usa cada medio de pago y su prioridad si hay más de uno (ej. tarjetas: Decidir o GP).
- **Convenios**: comisión (%), topes mínimo/máximo y plazos de liquidación, uno por forma de pago. Pueden heredarse desde un set definido a nivel entidad.

## Devoluciones y contracargos

- Devoluciones totales o parciales vía API o por canal.
- Un contracargo genera un webhook con el detalle. Si la devolución es el mismo día de la transacción, se anulan/no calculan impuestos; si es en otro día, los impuestos ya informados al fisco no se revierten. No hay devolución de impuestos si la devolución no es total.
- **Desconocimiento**: tipo especial de contracargo cuando el usuario pagador desconoce el pago ante la marca de tarjeta; el comercio se hace cargo y Bind PSP debe contemplarlo en liquidaciones para recuperar el dinero devuelto.

## Aplicaciones

- **Admin**: portal para entidades (incluye superadministradores de soporte Bind PSP) — transacciones, comercios, movimientos, configuraciones, altas y soporte operativo.
- **Portal de comercio**: portal marca blanca (look & feel configurable por entidad) para que el comercio vea transacciones, liquidaciones, movimientos, saldo de wallet asociado, transferencias y links de pago, según rol/permisos del usuario.

## Procesadores por funcionalidad

| Funcionalidad | Procesador |
|---|---|
| Cobro QR | Coelsa |
| Tarjetas no presente | Decidir (o Payway) |
| Tarjetas presente | Global Processing (a futuro también Payway) |
| Recaudación por transferencia | API BANK (Banco Industrial) |

## Integraciones con otros productos

- **Ardid**: cada entidad creada genera una entity en Ardid. Se analiza cada intento de cobro con tarjeta no presente (Botón simple 1.0/2.0) antes de cursarse — únicamente esos canales por ahora. Ver [ardid_overview.md](overview_ardid.md).
- **Wallet**: la entidad puede asociarse al id de organización de Wallet; si el comercio tiene cuenta y CVU de Wallet, Adquirencia crea comprobantes de acreditación/débito sobre esa cuenta para automatizar liquidaciones. Ver [wallet_overview.md](overview_wallet.md).
- **Agente de cobros y pagos**: sustenta el canal de recaudación por transferencia. Ver [cobros_overview.md](overview_agente_cobros_y_pagos.md).

---
*Última actualización: 2026-07-02 — Agregado canal de cobro POS (tarjeta presente, SmartPOS Topwise T3) y nota sobre limitación de planes de cuotas en tarjeta no presente.*
