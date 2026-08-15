# Guía — ¿Cómo integrar botón simple? (Adquirencia)

> Extraído el: 2026-07-01
> Fuente: https://psp.bind.com.ar/developers/apis/guia-boton-simple
> Producto: Adquirencia — Botón Simple 1.0

---

Esta solución permite cobrar a partir de la generación de un link de pago desde donde cualquier persona puede iniciar un procesamiento de pago con tarjeta de forma no presente.

Se trata de crear un link de pago a donde debes redireccionar a tu usuario para que concrete el pago. Si el mismo es pagado, su estado cambia a un estado definitivo. A su vez, cada vez que se procesa un pago desde un link de pago por una entidad el sistema crea una transacción en el sistema asociado al comercio correspondiente.

Se puede determinar una url diferente a la que queres que redirijamos al usuario en el caso de que el pago sea aprobado o rechazado.

Este canal se encuentra integrado a una herramienta de monitoreo transaccional que realiza rechazos o alertas de transacciones que cumplan con ciertas reglas que podes configurar (contamos con ciertas reglas standard). Es posible reforzar aún más la seguridad si conoces al usuario que está realizando el pago, permitiendo así configurar restricciones más personales y efectivas.

Por defecto, el sistema cursa todos los cobros ante el procesador de pagos bajo los números de comercio agrupador de Bind PSP. Sin embargo, admite usar códigos y credenciales propias de la entidad en el procesador.

En este esquema de cobro pueden realizarse devoluciones de cobros realizados por el monto parcial o total.

---

## Flujo de cobro con link de pago

## 🔀 Diagrama de Flujo (interpretado)
<!-- img-src: https://framerusercontent.com/images/28EgivofA4K9ylETL6jkCvtQE.png -->
> Fuente: https://framerusercontent.com/images/28EgivofA4K9ylETL6jkCvtQE.png
> Nota: transcripción interpretada por Claude Code a partir de un diagrama visual. No es texto literal del portal.

Actores: Usuario (pagador), Entidad (integrador), Bind PSP, Red de pagos (procesador externo)

1. Usuario → Entidad: "Quiere pagar con tarjeta"
2. Entidad → Bind PSP: `POST Crear link de pago`
3. Bind PSP → Entidad: `HTTP 201 {url}` (URL del checkout generada)
4. Entidad → Usuario: "Redirige al checkout" (usando la URL recibida)
5. Usuario → Bind PSP: "Completa el formulario de pago"
6. Bind PSP (interno): "Monitorea por fraude" (proceso interno de Bind PSP)
7. Bind PSP → Red de pagos: "Procesa pago en la red"
8. Red de pagos → Bind PSP: resultado del procesamiento
9. Bind PSP → Usuario: "Confirma estado de la transacción"
10. Bind PSP → Usuario: "Redirige a url indicada según resultado" (URL de éxito o rechazo configurada por la Entidad)
11. Bind PSP → Entidad: `POST Webhook aviso de cobro` (notificación asíncrona vía línea punteada)

---

## Endpoints disponibles

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Crear link de pago | endpoint_post_crear_link_pago.md |
| `GET` | Consultar link de pago por guid | endpoint_get_consultar_link_pago.md |
| `EVENT` | Aviso de transacción botón simple 1.0 | endpoint_event_transaccion.md |
| `EVENT` | Aviso de devolución botón simple 1.0 | endpoint_event_devolucion.md |
