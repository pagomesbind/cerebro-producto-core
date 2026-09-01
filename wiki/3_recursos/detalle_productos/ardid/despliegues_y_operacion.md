# Ardid — Despliegues y Operación (lado Bind PSP)

> Estado: en producción — protocolo confirmado por el equipo técnico en un caso real, no documentación teórica.
>
> Fuente: reunión "Análisis de Riesgo - Fix de cambios de estados de las tarjetas" (2026-08-28, docId `1QLWJd6WyUAVTdul2c8tkZbue7eL84ddDZlZs-pJDEOo`), sobre el ticket AD-1374 (fix "actualización estado de pagos, corrección BIN" sobre la versión 1182 de Ardid, afecta los microservicios `transaction API` y `Transaction Service`).

## 1. Protocolo de rollback estándar de un despliegue

Confirmado por el equipo (Matías Alzogaray, Osmel Mata/Fintexa, Mateo Capitanich/Fintexa) ante el ticket AD-1374: **no alcanza con restaurar la imagen Docker anterior** (`docker-compose up -d --force-recreate --no-deps <servicio>` a partir del backup `.tar`) si el despliegue también modificó la base de datos. En ese caso, el rollback requiere **dos pasos**:

1. Restaurar la imagen Docker anterior del/de los microservicio(s) afectado(s).
2. Restaurar el backup de base de datos (SQL Server + Mongo) tomado inmediatamente antes del despliegue — se reserva una ventana de ~30 min previa al despliegue para tomar ese backup.

Es la primera vez que este protocolo de dos pasos (imagen + DB) queda documentado explícitamente para Ardid — antes solo se hablaba de restaurar la imagen. Aplica a cualquier despliegue de Ardid que incluya un script de corrección de datos (no solo cambios de código puro).

## 2. Riesgo de rechazos al activar reglas antifraude que no se estaban aplicando — caso Coto

El fix de AD-1374 activa reglas antifraude que, por un bug previo, no se estaban aplicando. Afecta especialmente a **Coto**, que consume las APIs de Ardid sin bypass — a diferencia de Botón Simple/Wallet, que sí pueden operar en modo bypass durante la ventana de mantenimiento. El equipo clasificó el riesgo como **🟡 amarillo** (cambio funcional, no solo técnico): activar las reglas correctamente puede generar un salto de rechazos de transacciones y reclamos de clientes que antes pasaban sin control.

**Mitigación acordada:** habilitar las reglas de forma gradual en vez de todas de una vez, y monitorear post-implementación la relación entre respuestas 200 y rechazos contra el volumen histórico.

**Deploy:** staging lunes 31/08 9hs, producción martes 01/09 en ventana 6:30-8:00 (media hora previa reservada para el backup de bases). Sin action item de Producto — el seguimiento queda en el equipo técnico (Hernán Clarich monitorea rechazos, Rocío Revelli hace la revisión post-implementación en Ardid).

## Ver también
- [modulo_pagos.md](modulo_pagos.md) — reglas antifraude de pagos con tarjeta que este fix corrige.
- [../../../2_areas/procesos/analisis_de_riesgo_de_despliegue.md](../../../2_areas/procesos/analisis_de_riesgo_de_despliegue.md) — proceso general de análisis de riesgo de despliegue (semáforo, informe), del que este caso es una instancia concreta.

---
*Última actualización: 2026-08-31 — `/context_merge`: archivo nuevo, item de `contexto_vivo/` (reunión "Análisis de Riesgo - Fix de cambios de estados de las tarjetas", 2026-08-28).*
