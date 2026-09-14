---
id: 2026-09-14_gap_tarjeta_prepaga_crecimiento_rechazo_sin_explicar
pm: pablo
fecha_captura: 2026-09-14
fuente: "/sync_metrics — análisis semanal, semana 202637"
producto: adquirencia
tema: Tarjeta Prepaga (Payway) — segunda semana consecutiva de crecimiento explosivo combinado con rechazo muy por encima de lo habitual, sin causa confirmada
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
---

**Contradicción/inconsistencia detectada:** no hay una explicación documentada en la wiki (procesos,
clientes, estacionalidad) para un patrón que ya lleva dos semanas: el volumen de Tarjeta Prepaga en Payway
(NSM#2) creció con fuerza inusual dos semanas seguidas, y al mismo tiempo la tasa de rechazo subió muy por
encima de lo normal — dos señales que normalmente no van juntas (más volumen exitoso suele ir con rechazo
estable o menor, no mayor).

**Datos:**
- Semana 202636 (31/08 → 07/09): $68,4 M, WoW +483,8% (z=+6,38), rechazo 41,6% vs. media de 8 semanas
  24,9%. Ya se había marcado como hallazgo [ALTA] esa semana, con la acción sugerida "verificar con
  Adquirencia si es un patrón técnico conocido" — sin respuesta registrada hasta ahora.
- Semana 202637 (07/09 → 14/09): $204 M, WoW +197,5% (siguiendo el crecimiento, no revirtiendo), rechazo
  42,8% vs. media de 8 semanas 27,8%. Tendencia de ventana móvil de 4 semanas: +271,4% (acumulado +973,9%
  contra el promedio de las últimas 13 semanas).
- No hay estacionalidad conocida en `2_areas/direccion/estacionalidad_metricas.md` que explique un patrón
  de Tarjeta Prepaga específicamente (los patrones documentados son cobro de servicios días 1-10 y fechas
  comerciales tipo Hot Sale, ninguno de los cuales coincide con las semanas en cuestión).
- No hay proyecto ni lanzamiento conocido en `1_proyectos/` o `3_recursos/detalle_productos/adquirencia/`
  asociado a Tarjeta Prepaga en este período.

**Pregunta para el usuario:** ¿Adquirencia tiene contexto sobre qué está pasando con Tarjeta Prepaga? Las
hipótesis sin confirmar son: (a) un cliente puntual probando algo nuevo o corriendo un batch de reintentos
(lo que explicaría rechazo alto + volumen alto a la vez), (b) un cambio de comportamiento de un procesador
o emisor de tarjetas prepagas, o (c) un problema de integración que genera reintentos duplicados que se
cuentan como más "volumen" pero también más rechazo. Sin este contexto, no se puede escribir una causa en
el reporte semanal — solo se puede seguir reportando el patrón.

**Impacto mientras esté pendiente:** el reporte semanal sigue marcando este hallazgo como [Alta] severidad
cada semana que el patrón se sostenga, sin poder ofrecer una explicación de negocio — riesgo de que se lea
como ruido repetido si no se resuelve pronto.

**Estado:** Pendiente — primera vez que se abre como gap formal (la semana 202636 lo marcó como hallazgo
pero no se registró como gap todavía).
