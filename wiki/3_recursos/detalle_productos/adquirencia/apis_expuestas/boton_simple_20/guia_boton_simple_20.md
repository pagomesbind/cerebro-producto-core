# Guía — ¿Cómo integrar botón simple 2.0? (Adquirencia)

> Extraído el: 2026-07-01
> Fuente: https://psp.bind.com.ar/developers/apis/guia-boton-simple-20
> Producto: Adquirencia — Botón Simple 2.0

---

Esta solución permite cobrar una deuda puntual a partir de la generación de un link de pago desde donde cualquier persona puede pagarlo con tarjeta, con QR interoperable o con transferencia a un CVU.

Se trata de crear un link de pago a donde la entidad puede redireccionar a su usuario para que concrete el pago.

El checkout que presenta el link es marca blanca y puede customizarse con conceptos de la marca de la entidad. Esta configuración la hace el equipo de soporte de integraciones.

Si el mismo es pagado por cualquiera de los medios de cobro, su estado cambia a un estado definitivo y ya no puede volver a ser pagado.

A su vez, cada vez que se procesa un pago desde un link de pago por una entidad el sistema crea una transacción en el sistema asociado al comercio correspondiente, la cual se liquidará de la forma correspondiente al medio de pago con la que se procesó.

Se puede determinar una url diferente a la que queres que redirijamos al usuario en el caso de que el pago sea aprobado o rechazado.

Por cada link de pago creado con este producto la entidad puede elegir cobrar con uno, algunos o todos los medios de pago disponibles.

Al registrarse pagos, se registran transacciones en el sistema asociadas a cada deuda (link de pago) según corresponda.

Tanto para el medio de pago tarjetas como para el medio de pago QR, el usuario es obligado a pagar el monto cerrado indicado para el link de pago. Entonces, cada deuda de estos medios de pago no tendrá más de una transacción en estado ACREDITADO asociada.

Por otro lado, por su naturaleza, para el medio de pago transferencia a CVU el usuario puede pagar un monto parcial o incluso pagar un monto mayor ya que no se puede controlar el monto que transfiere el usuario desde su banco o billetera. También, al poder hacer transferencias por montos menores, pueden registrarse más de un pago parcial para una deuda hasta completar el monto total, o superando el monto total o incluso sin llegar a completarlo. Entonces, para este medio de pago pueden existir más de una transacción en estado ACREDITADO asociadas a la deuda.

Por defecto, para cobro con tarjetas, el sistema cursa todos los cobros ante el procesador de pagos bajo los números de comercio agrupador de Bind PSP. Sin embargo, admite usar códigos de comercio y credenciales propias de la entidad en el procesador.

En este esquema de cobro pueden realizarse devoluciones de cobros realizados por el monto parcial o total.

Este canal se encuentra integrado a una herramienta de monitoreo transaccional que realiza rechazos o alertas de transacciones que cumplan con ciertas reglas que podes configurar (contamos con ciertas reglas standard). Es posible reforzar aún más la seguridad si conoces al usuario que está realizando el pago, permitiendo así configurar restricciones más personales y efectivas.

---

## Flujo de cobro con link de pago 2.0 y usuario paga con tarjeta

## 🔀 Diagrama de Flujo — Pago con tarjeta (interpretado)
<!-- img-src: https://framerusercontent.com/images/b5oM3Bgu3rrRgJNwJ5AN20YUGQ.png -->
> Fuente: https://framerusercontent.com/images/b5oM3Bgu3rrRgJNwJ5AN20YUGQ.png
> Nota: transcripción interpretada por Claude Code a partir de un diagrama visual. No es texto literal del portal.

Actores: Usuario (pagador), Entidad (integrador), Bind PSP, Red de pagos (procesador externo)

1. Usuario → Entidad: "Quiere pagar una deuda"
2. Entidad → Bind PSP: `POST Crear link de pago 2.0`
3. Bind PSP → Entidad: `HTTP 201 {id, url}` (ID de deuda y URL del checkout)
4. Entidad → Usuario: "Redirige al checkout"
5. Usuario → Bind PSP: "Completa formulario y paga con tarjeta de débito"
6. Bind PSP (interno): "Monitorea por fraude"
7. Bind PSP → Red de pagos: "Procesa pago en la red"
8. Red de pagos → Bind PSP: resultado del procesamiento
9. Bind PSP (interno): "Imputa deuda"
10. Bind PSP → Usuario: "Confirma estado de la transacción"
11. Bind PSP → Usuario: "Redirige a url indicada según resultado"
12. Bind PSP → Entidad: `POST Webhook aviso de cobro [..., FormaPago=TTDD, ...]` (asíncrono, línea punteada)

---

## Flujo de cobro con link de pago 2.0 y usuario paga con transferencia

## 🔀 Diagrama de Flujo — Pago con transferencia a CVU (interpretado)
<!-- img-src: https://framerusercontent.com/images/PnQC1goFtESZ5NKR1eebG2sAVrw.png -->
> Fuente: https://framerusercontent.com/images/PnQC1goFtESZ5NKR1eebG2sAVrw.png
> Nota: transcripción interpretada por Claude Code a partir de un diagrama visual. No es texto literal del portal.

Actores: Usuario (pagador), Entidad (integrador), Bind PSP, Red (notificación de transferencia entrante)

1. Usuario → Entidad: "Quiere pagar una deuda"
2. Entidad → Bind PSP: `POST Crear link de pago 2.0`
3. Bind PSP → Entidad: `HTTP 201 {id, url}`
4. Entidad → Usuario: "Redirige al checkout"
5. Usuario → Bind PSP: "Transfiere un monto mayor o igual al CVU"
6. Red → Bind PSP: "Red informa transferencia entrante" (asíncrono, línea punteada)
7. Bind PSP (interno): "Imputa deuda"
8. Bind PSP → Usuario: "Confirma estado de la transacción"
9. Bind PSP → Usuario: "Redirige a url indicada según resultado"
10. Bind PSP → Entidad: `POST Webhook aviso de cobro [..., FormaPago=Transfer, ...]` (asíncrono, línea punteada)

---

## Endpoints disponibles

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Crear un link de pago 2.0 | endpoint_post_crear_link_pago.md |
| `GET` | Consultar un link de pago 2.0 | endpoint_get_consultar_link_pago.md |
| `POST` | Devolver un link de pago 2.0 | endpoint_post_devolver_link_pago.md |
| `GET` | Consultar devolución | endpoint_get_consultar_devolucion.md |
| `EVENT` | Aviso de transacción botón simple 2.0 | endpoint_event_transaccion.md |
| `EVENT` | Aviso de devolución botón simple 2.0 | endpoint_event_devolucion.md |
