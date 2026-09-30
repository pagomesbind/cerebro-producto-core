---
id: 2026-09-28_gap_actualizacion_tarjeta_prepaga_cuarta_semana
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_metrics — análisis semana 202639"
producto: adquirencia
tema: Tarjeta Prepaga (Payway) — cuarta semana de crecimiento con rechazo alto; se suma rechazo de Débito en alza; posible relación con PRD-251 (BINes)
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 3492d04
---

**Actualiza el gap `[2026-09-14] — Tarjeta Prepaga (Payway): crecimiento explosivo combinado con rechazo muy
por encima de lo habitual, sin causa confirmada`** en `2_areas/gaps_y_preguntas.md`.

**Actualización (2026-09-28, semana 202639):** cuarta semana consecutiva del patrón. Tarjeta Prepaga en NSM#2:
$139 M en la semana (WoW −7,4%), tendencia de ventana móvil de 4 semanas +566,6% (ventana previa $84,1 M),
tendencia de regresión de 6 semanas +34,0% por semana (acumulado +210,9% vs. baseline 13s). Rechazo 37,8% vs.
media de 8 semanas 32,9% (202638: 43,2%; 202637: 42,8%; 202636: 41,6%) — baja algo, pero sigue arriba.

**Señal nueva:** el rechazo de **Tarjeta de Débito** subió por segunda semana (202638 18,5% → 202639 20,2%,
media de 8 semanas 16,7%). Crédito, en cambio, bajó (27,3% vs. 31,3%).

**Pista disponible en `1_proyectos/` (no confirma causa):** el proyecto PRD-251 (`rechazos_bines_payway/`)
documenta que la base de identificación de BINes está desactualizada y genera **rechazo garantizado del 100%
de los intentos** en ciertos BINes, con impacto visible especialmente en prepagas (Servicios/Pago Fácil no
puede cerrar pruebas con prepagas reales desde hace más de un mes) y un ~40% de las altas pendientes
clasificadas como Débito/Prepaga. La corrección (v73, eliminación de la validación de bines del frontend +
script de carga de ~80.000 BINes) se canceló el 24/09 y quedó reprogramada al **martes 29/09 20:30hs**. Eso
explicaría el rechazo alto, pero **no** el crecimiento del volumen de Prepaga. También hay registro (minuta
Western Union 12/8) de que Tarjeta Prepaga "configurada como Tarjeta de Crédito" pasó a producción la semana
del 17/08 para ese cliente — posible origen del crecimiento, sin confirmar.

**Preguntas para el usuario:**
1. ¿Adquirencia confirma si el crecimiento de Prepaga viene del alta de Tarjeta Prepaga para Western Union
   (agosto) u otro cliente puntual?
2. ¿Se toma el despliegue de v73 (29/09) como punto de control para medir si el rechazo de Prepaga y Débito
   baja en 202640–202641? (propuesta: sí, se revisa en las próximas dos corridas).

**Estado:** Pendiente — cuarta semana sin causa confirmada del crecimiento; hipótesis de rechazo ligada a
PRD-251 a validar después del 29/09.
