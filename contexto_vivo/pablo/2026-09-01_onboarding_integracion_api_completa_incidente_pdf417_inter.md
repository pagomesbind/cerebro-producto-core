---
id: 2026-09-01_onboarding_integracion_api_completa_incidente_pdf417_inter
pm: pablo
fecha_captura: 2026-09-01
fuente: "/sync_mails — hilo 'Fwd: Onboarding INTER-BIND' (threadId 1a05968fc3bc2daa), Emma Vignoles / Cristian Bonafede (Fintexa-Sandinas) / Alberto Murad, 2026-08-31"
producto: onboarding
tema: mecánica de integración por API "completa" (organización invoca todo, sin front de Bind) + incidente PDF417/nuevo DNI en cliente Inter
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/onboarding_por_api.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Mecánica: integración por API "completa" (distinta de "Onboarding en partes por API")

`onboarding_por_api.md` ya documenta el producto "Onboarding en partes por API" (caso COTO CICSA — la entidad invoca pasos puntuales, ej. solo Renaper Datos, desde su propio front). El caso de **Inter** (cliente Wallet, ver `casos_de_uso_clientes.md`) es un modelo de integración distinto que no está documentado todavía: la **organización invoca las APIs de Onboarding directamente con todos los datos y con las imágenes del DNI ya capturadas por su propia app** — no hay ningún paso del flujo que pase por el front de Onboarding de Bind PSP.

Confirmado explícitamente por Cristian Bonafede (Fintexa/Sandinas) el 2026-08-31: *"en el flujo de inter, la captura de las imágenes no la realiza onboarding, la organización es quien invoca a las apis con todos los datos y con las imágenes. No es por front la integración que tienen."*

**Consecuencia de diseño:** en este modelo, es **Bind PSP quien debe interpretar el documento de identidad (PDF417 o QR/MRZ) del lado servidor** a partir de la imagen recibida por API, y validar contra Renaper — no hay oportunidad de que el propio front de Bind guíe al usuario a repetir la foto si la lectura falla, como sí puede pasar en el flujo con front propio. Cualquier cascada de fallback de lectura de documento (ver `prd-113_leer_nuevo_dni/proyecto.md §3`) tiene que cubrir explícitamente este camino de alta por API para que no queden clientes de integración completa (como Inter) sin cobertura.

## Incidente asociado (contexto, no resuelto al momento de la captura)

Desde el 2026-08-31, Inter reporta una caída sustancial de su tasa de aprobación de onboarding (de 85% a 32%), con 352 rechazos en los últimos 3 días atribuidos al error **"No se pudo encontrar el PDF417 en las imágenes procesadas"**. Ninguna de las partes (Inter, Bind PSP, Fintexa) había identificado la causa raíz al cierre de este mail (2026-08-31 21:02). Fintexa (Cristian Bonafede) sugirió inicialmente que faltaba el dato "Género" en el alta, pero Emma Vignoles (Bind PSP) aclaró que el género es opcional — el punto que falla es específicamente la interpretación del PDF417 de la imagen que envía Inter, y "este punto falla hace más de 1 mes".

**Nota del Cerebro (no confirmada, ver `prd-113_leer_nuevo_dni/proyecto.md §6` y `tareas.md` T-052):** el síntoma coincide con el que motivó `prd-113_leer_nuevo_dni` (el DNI argentino nuevo, vigente desde 2026-02-01, no tiene PDF417 — solo QR+MRZ). El posible pase a producción del fix (OB-193) fue el mismo lunes 2026-08-31, pero el incidente de Inter siguió reproduciéndose esa misma noche — sin confirmar todavía si el fix cubre el camino de alta por API o solo el front.

Contexto de negocio: Inter lanza el comunicado de prensa de su app el jueves 2026-09-03 — la urgencia de resolución es alta independientemente de la causa raíz final.
