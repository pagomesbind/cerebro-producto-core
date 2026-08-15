# Onboarding en Partes por API

> Estado: en producción.

> Contenido destilado de la Epic de Notion "Onboarding en partes por API" (PRD completo + 6 tickets).

## 1. Qué es y por qué

Producto pensado para entidades que **no quieren consumir el onboarding completo de Bind PSP como caja negra**, sino invocar solo los pasos puntuales que necesitan desde su propio front — el más demandado es únicamente **Renaper Datos**.

- **Cliente de referencia**: COTO CICSA, que pidió poder hacer el onboarding en 2 pasos separados en el tiempo (potencialmente meses entre uno y otro): primero Renaper Datos, y luego retomar esa misma solicitud para completar el alta en Wallet.
- **Propuesta de valor**: la mayor parte del valor no es el onboarding en sí, sino que Bind PSP ya tiene las credenciales de Renaper (difíciles de conseguir administrativa y legalmente) — el cliente evita ese trámite y acelera su time-to-market apoyándose en Bind PSP solo para esa validación puntual.
- **Objetivo de producto**: tener un "Onboarding por API customizable" como producto de góndola propio, para sumar más entidades al negocio de Onboarding en general.

## 2. Funcionalidades (MoSCoW del PRD)

**Must have:**
- Flujos por partes: pasos de onboarding customizables e invocables por API de forma independiente.
- Autenticación vía **OAuth2**.
- Actualizar solicitud: la entidad puede completar el legajo con datos que Bind PSP no necesita validar/obtener (ej. si no van a validar OTP de email con los servicios de Bind PSP, pueden enviar ese dato ya validado por su lado).

**Should have:**
- Creación de solicitud con **externalId** propio de la entidad (no puede haber dos solicitudes con el mismo externalId).
- Consulta de solicitud por externalId.
- Legajo completo persistido en Legajo Digital.
- Cada respuesta de paso debe indicar el estado de la solicitud y la respuesta cruda del servicio externo correspondiente (ej. en el paso Renaper Datos, devolver el objeto que respondió Renaper).

**Could have:**
- Completar el legajo digital de forma parcial, a medida que la entidad va cargando información en partes.
- Que una solicitud rechazada por una validación real (ej. Renaper no valida al usuario) no devuelva HTTP 422 — el sistema funcionó correctamente, el resultado de negocio es el que es.
- Duración configurable de solicitudes pendientes: poder retomar una solicitud iniciada hasta X días después.

**Time to market planteado**: MVP en abril (solo crear solicitud + consultar Renaper Datos), producto completo en mayo.

## 3. Bugs y pendientes del backlog

- **[US] El GET solicitud por ID responde diferente que el por ID externo** — inconsistencia entre las dos formas de consultar la misma solicitud (por id interno vs. externalId), quedó Pendiente.
- **[US] Invocar endpoints intermedios con externalId** — Pendiente, parte del alcance "Could have" de reutilizar el externalId en más endpoints del flujo.
- **🕷 Bug de seguridad — aislamiento entre entidades**: con el consumer OAuth2 de una Entidad era posible consultar solicitudes de **otra** Entidad — bug de autorización cross-tenant, quedó registrado como Pendiente al cierre del relevamiento.

---
*Fuente: Notion histórico, Epic "Onboarding en partes por API" — ingesta 2026-07-06.*
