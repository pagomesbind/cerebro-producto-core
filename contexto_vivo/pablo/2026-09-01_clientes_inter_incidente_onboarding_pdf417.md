---
id: 2026-09-01_clientes_inter_incidente_onboarding_pdf417
pm: pablo
fecha_captura: 2026-09-01
fuente: "/sync_mails — hilo 'Fwd: Onboarding INTER-BIND' (threadId 1a05968fc3bc2daa), Emma Vignoles / Cristian Bonafede (Fintexa-Sandinas) / Alberto Murad / Rodrigo Rodrigues Rocha (Inter), 2026-08-31"
producto: onboarding
tema: incidente de PROD en el onboarding de INTER — caída de tasa de aprobación por PDF417
tipo: conocimiento
destino_propuesto: wiki/2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Fusionar en la ficha "INTER" (§ existente, `casos_de_uso_clientes.md` línea ~58) — sección "Particularidades / cronología"

**2026-08-31 — Incidente de producción, onboarding con caída sustancial de aprobación:** Inter reporta que desde el 2026-08-26 la tasa de aprobación de altas de onboarding cayó de **85% a 32%**, con **352 rechazos en los últimos 3 días** por el error "No se pudo encontrar el PDF417 en las imágenes procesadas" (265 de esos rechazos en la ventana informada por Rodrigo Rodrigues Rocha, M&A & Strategy de Inter, el 28/08). El problema viene arrastrándose "hace más de un mes" según Emma Vignoles (Bind PSP), pero se agravó fuertemente desde el 26/08.

**Contexto de negocio crítico:** Inter tiene programado el **comunicado de prensa de su app para el jueves 2026-09-03** — la resolución del incidente es urgente por el impacto de imagen/negocio del lanzamiento, no solo por el volumen de rechazos.

**Causa raíz sin identificar al 2026-08-31 (21:02):** ni Inter, ni Bind PSP, ni Fintexa la habían encontrado. Fintexa (Cristian Bonafede) sugirió inicialmente que faltaba el dato "Género" en el alta; Emma Vignoles corrigió que el género es opcional para Inter y que el problema real es la interpretación del PDF417 de la imagen del DNI que Bind PSP debe hacer server-side (Inter integra por API completa, sin pasar por el front de Onboarding — ver detalle del modelo de integración en el item de contexto_vivo `2026-09-01_onboarding_integracion_api_completa_incidente_pdf417_inter`). Se acordó una reunión de diagnóstico conjunto con casos concretos (imágenes de ejemplo ya compartidas por Fintexa). Seguimiento en `1_proyectos/tareas.md` T-052.

**Posible causa (hipótesis del Cerebro, no confirmada):** correlación con el DNI argentino nuevo (sin PDF417, ver `prd-113_leer_nuevo_dni`) — ver detalle en el item de contexto_vivo mencionado arriba.
