---
id: 2026-10-05_gap_cta39_pico_no_ocurrido
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_metrics — análisis semana 202640 (fact_transferencias_agente_cobro, 202625–202640)"
producto: transversal
tema: Actualización del gap de 2026-08-11 sobre "Bind PSP liquidaciones cta 39" — rompió el ciclo mensual que se había inferido, y ya son tres cuentas de la misma familia con comportamiento errático
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## [2026-10-05] — Actualización del gap `[2026-08-11]`: "cta 39" no tuvo el pico de inicio de mes que venía repitiendo, y cta 2/cta 8 siguen en $0

- **Severidad:** Alta
- **Descripción:** El gap abierto el 2026-08-11 preguntaba si "Bind PSP liquidaciones cta 39" era una cuenta
  administrativa interna (como cta 14/cta 2) o un cliente real activándose, a raíz de un salto puntual a
  $6.647 M en la semana 202632. Desde entonces se volvió a observar en las semanas 202636 ($4.993 M) y, antes,
  202627 ($4.853 M) — un patrón de **pico de $4.850–6.650 M en la primera semana de cada uno de los últimos
  tres meses** (julio, agosto, septiembre), con caída a $140–240 M al cierre de cada mes (último registro,
  semana 202639: $142 M — ya reportado como "ruido, ciclo mensual habitual" en el reporte de esa semana).
  Siguiendo ese ciclo, la semana 202640 (primera semana de octubre) debería haber repetido el pico — en
  cambio, quedó en **$404 M**, un 83,1% por debajo de su promedio de 4 semanas y muy lejos de los $4.800+ M
  esperables. El patrón mensual que se venía dando por confirmado **se rompió esta semana**, sin explicación
  disponible en la wiki.
  Esto se suma a un patrón más amplio, ya documentado en el gap del 2026-09-28 (Credicuotas/cta 2): otras dos
  cuentas de la misma familia — "Bind PSP liquidaciones cta 2" y "cta 8" — están en **$0 desde la semana del
  7 de septiembre** (202637), ya cuatro semanas consecutivas, sin que nadie haya confirmado todavía si se
  dieron de baja, se reemplazaron por otra cuenta, o migraron sus flujos.
- **Pregunta para el usuario:** (1) ¿"cta 39" es una cuenta administrativa interna o corresponde a un
  cliente real? Si es una cuenta administrativa, ¿por qué dejó de seguir su propio ciclo mensual esta
  semana? (2) ¿Administración puede confirmar de una vez el estado de las tres cuentas (cta 2, cta 8, cta
  39) — bajas, reemplazos o migraciones de flujos?
- **Estado:** Pendiente — tercera semana que pasa sin respuesta desde la pregunta original de agosto.
