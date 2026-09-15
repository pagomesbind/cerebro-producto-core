---
id: 2026-09-14_clientes_grupo_desa_solo_boton_simple_1_0
pm: pablo
fecha_captura: 2026-09-14
fuente: "/idea_problem — discovery del proyecto rechazos_bines_payway (PRD-251), declaración directa del PM"
producto: adquirencia
tema: Corrección de dato en la ficha de Grupo DESA — la entidad opera solo Botón Simple 1.0 (tarjeta), no Botón Simple 2.0 como dice el canon hoy
tipo: gap
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "casos_de_uso_clientes.md, ficha 'GRUPO DESA (Edelap/Edesa/Edea/Eden)' — encabezado dice 'Productos: QRI, RxT, Botón de Pago (→ Adquirencia, Botón 2.0)'. El PM confirmó (2026-09-14) que esta entidad opera únicamente Botón Simple 1.0 (solo tarjeta), sin la variante 2.0 que combina QR/transferencia dentro del mismo flujo de pago."
confianza: alta
estado: en_cola
---

Durante el discovery de `/idea_problem` (proyecto `rechazos_bines_payway`, PRD-251), al evaluar si Grupo DESA tiene alguna alternativa/fallback cuando un link de Botón de Pago se rechaza, el PM aclaró: **"Esta entidad no usa bs2.0. Solo usa Bs1.0 (solo tarjeta)"**.

Esto corrige el encabezado de la ficha existente (`casos_de_uso_clientes.md`, sección "GRUPO DESA"), que hoy clasifica el producto como "Botón de Pago (→ Adquirencia, Botón 2.0)". La corrección importa más allá del dato en sí: significa que cuando un link de pago de este cliente se rechaza, **no hay ningún fallback automático a QR o transferencia dentro del mismo flujo** — el pago queda perdido en esa instancia, sin reintento. (El cuerpo de la misma ficha sí menciona que el cliente tiene collectors separados para QR y RxT como productos aparte — pero no como alternativa dentro del flujo del Botón que falla.)

Este dato es relevante para el problem statement del proyecto `rechazos_bines_payway` (ver [`1_proyectos/rechazos_bines_payway/proyecto.md`](../rechazos_bines_payway/proyecto.md)) — la ausencia de reintento es parte de por qué el rechazo, aunque sea una porción menor del total, genera tanta fricción visible para el cliente.

## Ver también

- [`1_proyectos/rechazos_bines_payway/proyecto.md`](../rechazos_bines_payway/proyecto.md) (PRD-251).
- [`contexto_vivo/2026-09-14_clientes_grupo_desa_riesgo_continuidad_escalado_dir.md`](2026-09-14_clientes_grupo_desa_riesgo_continuidad_escalado_dir.md) — item relacionado sobre el riesgo de continuidad de la misma cuenta.
