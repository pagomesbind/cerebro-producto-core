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

## 4. Integración por API "completa" — distinta de "Onboarding en partes por API" (caso Inter)

> Estado: en producción. Fuente: hilo de mail "Fwd: Onboarding INTER-BIND" (Emma Vignoles / Cristian Bonafede, Fintexa-Sandinas / Alberto Murad, 2026-08-31).

Todo lo documentado arriba (§1-3) es el producto "Onboarding en partes por API" (caso COTO CICSA — la entidad invoca pasos puntuales desde su propio front). El caso de **Inter** (cliente Wallet, ver [`2_areas/clientes/casos_de_uso_clientes.md`](../../../2_areas/clientes/casos_de_uso_clientes.md)) es un modelo de integración distinto: la **organización invoca las APIs de Onboarding directamente con todos los datos y con las imágenes del DNI ya capturadas por su propia app** — ningún paso del flujo pasa por el front de Onboarding de Bind PSP.

Confirmado explícitamente por Cristian Bonafede (Fintexa/Sandinas) el 2026-08-31: *"en el flujo de inter, la captura de las imágenes no la realiza onboarding, la organización es quien invoca a las apis con todos los datos y con las imágenes. No es por front la integración que tienen."*

**Consecuencia de diseño:** en este modelo es **Bind PSP quien debe interpretar el documento de identidad (PDF417 o QR/MRZ) del lado servidor** a partir de la imagen recibida por API, y validar contra Renaper — no hay oportunidad de que el propio front de Bind guíe al usuario a repetir la foto si la lectura falla, a diferencia del flujo con front propio. Cualquier cascada de fallback de lectura de documento (ver `1_proyectos/prd-113_leer_nuevo_dni/proyecto.md §3`) tiene que cubrir explícitamente este camino de alta por API, para no dejar clientes de integración completa (como Inter) sin cobertura.

### 4.1 Incidente asociado — caída de tasa de aprobación por error de PDF417 (2026-08-31, sin causa raíz confirmada)

Desde el 2026-08-26, Inter reportó una caída sustancial de su tasa de aprobación de onboarding (de 85% a 32%), con 352 rechazos en los 3 días previos al 31/08, atribuidos al error **"No se pudo encontrar el PDF417 en las imágenes procesadas"** — el problema venía arrastrándose "hace más de un mes" según Emma Vignoles (Bind PSP), agravado fuertemente desde el 26/08. Ninguna de las partes (Inter, Bind PSP, Fintexa) había identificado la causa raíz al cierre del hilo (2026-08-31 21:02). Fintexa (Cristian Bonafede) sugirió inicialmente que faltaba el dato "Género" en el alta; Emma Vignoles aclaró que el género es opcional para Inter y que el punto que falla es específicamente la interpretación del PDF417 de la imagen que envía Inter.

**Hipótesis no confirmada (a verificar):** el síntoma coincide con el que motivó `1_proyectos/prd-113_leer_nuevo_dni` (el DNI argentino nuevo, vigente desde 2026-02-01, no tiene PDF417 — solo QR+MRZ). El posible pase a producción del fix (OB-193) fue el mismo lunes 2026-08-31, pero el incidente de Inter siguió reproduciéndose esa misma noche — sin confirmar si el fix cubre el camino de alta por API o solo el front. Contexto de negocio: Inter lanza el comunicado de prensa de su app el jueves 2026-09-03 — la urgencia de resolución es alta independientemente de la causa raíz final. Seguimiento en `1_proyectos/tareas.md` T-052.

---
*Última actualización: 2026-09-02 — `/context_merge`: nueva §4, modelo de integración "completa" (caso Inter) y el incidente de PDF417 asociado.*
*Fuente: Notion histórico, Epic "Onboarding en partes por API" — ingesta 2026-07-06.*
