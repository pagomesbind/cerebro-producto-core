# Integración de procesadores de pago (Prisma/GP)

> Estado: en producción (con deuda técnica activa, ver §1).
>
> Fuente: reunión recurrente "Análisis COBRO" (2026-08-20, con Daniela Collia y equipo de Fintexa), minuta Gemini.

## 1. Deuda técnica de grupos de reglas — coexistencia Prisma/GP

El sistema mantiene dos procesadores en paralelo (**Prisma** y **GP**) con grupos de reglas mal estructurados para su coexistencia, lo que genera fricción operativa en las pruebas (pagos y devoluciones no pueden ejecutarse completamente en el entorno actual). Se acordó migrar el enfoque hacia **parámetros de canal dinámicos** en lugar de grupos de reglas rígidos, para evitar ciclos repetitivos de modificación manual. No es bloqueante para el despliegue en curso (v72, ver §5).

## 2. Parámetro "pago único"

Se definió para diferenciar productos:
- `1` = botón de pago.
- `0` = RXT.

## 3. Regla de liquidación de transacciones en línea (same-day)

Las transacciones en línea deben **liquidarse el mismo día**; si no pueden procesarse, se **descartan**. Antes quedaban en una cola de espera incorrecta por un error de lógica de negocio — detectado en la misma reunión junto con el problema de saturación de la base de impuestos de SISCRI (mismo bug/regla discutido desde la perspectiva de Impuestos en [`siscri/calculo_impuesto_online_qr.md §8`](../siscri/calculo_impuesto_online_qr.md)). Ver también el riesgo transversal asociado en `2_areas/riesgos.md`.

## 4. Limitación del panel administrativo con Prisma

El backend ya soporta Prisma como procesador único, pero el **panel de administración no permite seleccionarlo así** porque el sistema habilita GP por defecto. Se decidió aprobar igual el despliegue del ticket de Prisma sin esta funcionalidad de configuración en el admin (no cumple 100% la Definition of Done), gestionando la limitación de la interfaz por separado.

## 5. Hotfix de localidades/códigos postales

Se corrigen inconsistencias de validación en alta/edición manteniendo el alcance acotado (ticket 789). La reestructuración de la API para devolver una lista de localidades (en vez de una sola) queda postergada a un ticket futuro de menor prioridad, fuera de alcance de este hotfix.

## 6. Cronograma

Versión 72 programada para el jueves 2026-08-27 a las 21:00hs, con transferencias salientes y guardado de respuesta de Rebank encaminados.

## Ver también

- [overview_agente_cobros_y_pagos.md](../../../2_areas/overview_productos/overview_agente_cobros_y_pagos.md) — overview funcional/de negocio del producto.
- [siscri/calculo_impuesto_online_qr.md §8](../siscri/calculo_impuesto_online_qr.md) — mismo bug de cola de espera y misma regla de liquidación same-day, desde la perspectiva de SISCRI/Impuestos.
- [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) — otros bugs operativos históricos de este módulo.

---
*Última actualización: 2026-08-27 — `/context_merge`: creación del archivo a partir de la reunión "Análisis COBRO" (2026-08-20) — deuda técnica de reglas Prisma/GP, parámetro "pago único", regla de liquidación same-day, limitación del panel admin con Prisma, hotfix de localidades, cronograma v72.*
