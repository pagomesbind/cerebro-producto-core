---
id: 2026-10-15_adquirencia_conocimiento_diseno_validacion_titularidad_modo
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-10-15, 12:01)"
producto: adquirencia
tema: Diseño técnico completo de la integración con MODO (VATA) para validar titularidad de tarjeta en Botón Simple y prevenir contracargos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/integracion_modo_vata.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto

`integracion_modo_vata.md` ya documenta que el reenvío de una propuesta de MODO de enero 2025 (2026-09-10) disparó el discovery del proyecto `titularidad_tarjeta` (PRD-25). **Ni PRD-25 ni `titularidad_tarjeta/` aparecen hoy en la tabla maestra de `1_proyectos/index.md`** — este item documenta el diseño técnico completo que Nicolás Colón presentó en la reunión "Análisis COBRO" del 15/10, sin que exista un proyecto vivo donde colgarlo directamente; de ahí que nazca acá como conocimiento de producto en vez de una actualización de `proyecto.md`. Señalado como posible anomalía de índice a revisar.

## Problema que resuelve

Ni Ardid ni el procesador de pagos validan hoy de forma confiable si quien paga con tarjeta en Botón Simple es realmente el titular — origen de contracargos por "tarjeta no propia".

## Diseño acordado

- **Orden de evaluación:** la consulta a MODO se hace **después** de que Ardid no rechace la transacción — la consulta a MODO es ~50 veces más costosa que la de Ardid.
- **Datos enviados a MODO (nunca el número completo de tarjeta):** BIN (8 primeros dígitos), últimos 4 dígitos, vencimiento, tipo de tarjeta (crédito/débito), marca (Visa/Mastercard/Cabal/Maestro) y documento de identidad del pagador.
- **Hash nuevo y distinto del de Ardid:** para Ardid se sigue calculando el hash de la tarjeta completa descartando el resto; para MODO se genera un hash conjunto con todos los datos requeridos (BIN + últimos 4 + vencimiento + tipo + marca + DNI), por motivos de seguridad.
- **Camino feliz:** Ardid no rechaza → MODO confirma correspondencia tarjeta↔documento → el pago sigue al procesador.
- **Manejo de errores/excepciones de MODO (regla de negocio):**
  - `400`/`401` (datos malformados/credenciales inválidas) → el pago sigue normalmente al procesador, sin frenarse.
  - `404` (banco emisor, ej. BIND, no cubierto por la red de MODO) → el pago sigue normalmente; MODO no cobra por estas consultas.
  - Caída del servicio de MODO tras 2 reintentos → el pago sigue normalmente al procesador.
  - `409` (tarjeta no corresponde al documento, o rechazo genérico sin cuerpo detallado) → la transacción se **rechaza sin enviarse al procesador**. Mensaje al checkout **genérico** (no se expone el motivo real, por seguridad, para no revelar a quien intenta pagar con tarjeta ajena qué fue lo que falló).
- **Caché de combinaciones positivas:** se evita reconsultar a MODO cuando una combinación tarjeta+documento ya fue confirmada positiva (hash propio, incluye DNI, independiente de la bóveda de pagos recurrentes). Las combinaciones **rechazadas siempre se reconsultan** (un rechazo, ej. tarjeta deshabilitada, puede cambiar con el tiempo).
- **Arquitectura:** se construye como **servicio externo e independiente**, reutilizable a futuro desde otros canales de pago (Post, productos de bóveda en Wallet), no acoplado a Botón Simple.
- **Configuración:** habilitación por entidad/comercio vía el mecanismo existente de especificaciones (Grupo 447) — **no requiere pantalla nueva en el administrador** en esta primera iteración (decisión que generó objeción de Daniela Collia por deuda técnica; se compensa con documentación de soporte para configurar por base de datos, y una historia de usuario de menor prioridad para integrarlo al alta de canales desde el administrador más adelante, a pedido de Pablo Gomes).

## Dependencias pendientes (bloquean el arranque del desarrollo)

- Credenciales de MODO.
- Contrato comercial con MODO.
- **Ambiente de pruebas de MODO** — reclamado por correo sin respuesta; Nicolás Colón retoma el pedido el mismo día de la reunión.
- Determinación correcta de marca y tipo de tarjeta a partir del BIN.

## Fuera de alcance de esta primera iteración

Evitar reconsultas complejas más allá del caché simple descripto arriba; extender la validación a canales fuera de Botón Simple.

> Fuente: reunión "Análisis COBRO", 2026-10-15 12:01hs (Nicolás Colón, Daniela Collia/Fintexa, Pablo Gomes, Luciana Rudaz, Matías Alzogaray).
