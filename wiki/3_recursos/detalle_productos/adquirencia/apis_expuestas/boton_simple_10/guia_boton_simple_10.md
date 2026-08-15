# Guía: Botón Simple 1.0 — Adquirencia

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-boton-simple
> Producto: Adquirencia / Soluciones de Cobro

---

## Descripción

Solución para generar enlaces de pago para cobros mediante tarjeta en modalidad no presente (tarjetas de débito, crédito o prepaga).

## Características

- Generación de links de pago individuales.
- Configuración de URLs de redirección para aprobación y rechazo del pago.
- Monitoreo transaccional con rechazos/alertas automáticas según reglas configurables.
- Seguridad personalizable: restricciones específicas si se conoce al usuario final.
- Uso de comercio agrupador (números Bind PSP por defecto).
- Soporte para devoluciones parciales y totales.

## Medios de Pago Soportados

- Tarjeta de débito
- Tarjeta de crédito
- Tarjeta prepaga

## Flujo — Cobro con link de pago (Botón Simple 1.0)

```
1. Entidad → POST /boton-crearlinkdepago
   → Body: monto + moneda + externalRefId + redirect_ok + redirect_fail
           + [opcional] datos del usuario para restricciones de seguridad
   → Respuesta: {url} del checkout de pago generado

2. Entidad redirige al usuario a la URL del checkout

3. Usuario completa el formulario de pago con su tarjeta (débito/crédito/prepaga)

4. Bind PSP evalúa monitoreo transaccional (anti-fraude)
   → Si rechazado: usuario es redirigido a redirect_fail

5. Bind PSP procesa el pago en la red (procesador externo)
   → Bajo números de comercio agrupador de Bind PSP (por defecto)
   → O bajo códigos propios de la entidad si está configurado

6. Resultado:
   → Aprobado: usuario redirigido a redirect_ok + EVENT webhook "aviso de transacción"
   → Rechazado: usuario redirigido a redirect_fail + EVENT webhook

DEVOLUCIÓN (posterior al cobro):
   → La entidad puede solicitar devolución parcial o total del cobro
   → EVENT webhook "aviso de devolución"

CONSULTAR ESTADO:
   GET /consultar-link-de-pago?guid={guid} → estado actual del link
```

## Endpoints Disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/boton-crearlinkdepago` | Crear link de pago |
| GET | `/consultar-link-de-pago` | Consultar por GUID |
| EVENT | `/webhook-adboton10` | Webhook — Aviso de transacción |
| EVENT | `/webhook-addevbs10` | Webhook — Aviso de devolución |

> **Nota**: El portal no expone parámetros de request/response, ejemplos JSON ni status codes en esta guía.
