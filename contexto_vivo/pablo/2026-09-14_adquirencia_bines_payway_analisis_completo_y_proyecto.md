---
id: 2026-09-14_adquirencia_bines_payway_analisis_completo_y_proyecto
pm: pablo
fecha_captura: 2026-09-14
fuente: "/idea_start — discovery del proyecto rechazos_bines_payway (PRD-251), corrige el alcance y completa el hilo de mails 'Análisis BINES Payway/Decidir' ya mergeado el 2026-08-20"
producto: adquirencia
tema: Desalineación entre la base de BINES de Payway y la tabla interna — mecanismo transversal a todo procesamiento de tarjeta (no específico de POS), hoy más afectado por volumen en tarjeta no presente (Botón Simple 1.0/2.0). Análisis completo del informe de agosto de Fintexa + cruce BIN a BIN propio + hallazgo de bug de datos en segmentoTarjeta
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "pos_multiadquirencia.md §6 — esa entrada (2026-08-20/21) mergeó la misma investigación bajo el módulo de POS multiadquirencia; el PM aclaró (2026-09-14) que el mecanismo de identificación de BIN no es específico de POS, es compartido por cualquier procesamiento de tarjeta, y hoy el mayor impacto por volumen está en tarjeta no presente (Botón Simple 1.0/2.0), no en POS. Corresponde mover/rescopar §6 al mergear este item, no solo agregar contenido nuevo en paralelo"
confianza: alta
estado: ingestado
merge_commit: 0b463d974f85a1b19919f0b7ae5d338c8da68ec8
---

**Corrige el alcance de lo ya mergeado en `pos_multiadquirencia.md §6` (2026-08-20/21), además de completarlo.** Esa entrada registró el hilo de mails de Agustín Grau (Fintexa) bajo el módulo de POS multiadquirencia — pero el PM confirmó (2026-09-14) que el mecanismo de identificación de BIN (`SharedIssuerIdentification`) es **transversal a cualquier procesamiento de tarjeta**, no específico del canal POS/presente. Hoy el mayor impacto por volumen está en **tarjeta no presente vía Botón Simple 1.0/2.0**, no en POS. Al mergear, `/context_merge` debería mover el contenido de `pos_multiadquirencia.md §6` a `boton_simple_2_0.md` (o al archivo temático que corresponda si en el futuro se documenta la mecánica de BINs como tema propio, dado que también afecta a POS) en vez de dejarlo duplicado en ambos lados. Este item vuelca además el contenido completo del informe de agosto (marcado antes como "no leído"), un cruce de datos propio y un hallazgo nuevo de calidad de datos, generados en el discovery del proyecto [`1_proyectos/rechazos_bines_payway/`](../rechazos_bines_payway/proyecto.md) (PRD-251, PM Pablo Gomes).

## 1. Los 9 hallazgos del informe de Fintexa (19/08/2026, 14.695 operaciones del 18/08 completo)

**Refutación de la hipótesis de mayo:** el mapeo BIN→código de medio de pago que Bind envía a Decidir es correcto en el **98,14%** de los casos, y corregir el resto **no bajaría el rechazo general** — las operaciones con código discordante rechazan al 16,94% contra 19,15% de las concordantes (z=-0,976, p=0,33, no significativo). El rechazo real es estructural por tipo de producto (crédito 27,6% vs. débito 13,4%) y por motivo del emisor (denegada, fondos insuficientes), no por el mapeo BIN→código.

**Hallazgos de severidad Alta:**
- **H-1 — 60 BINs con resolución no determinística:** filas de la tabla interna con distinto tipo de tarjeta y la misma `PrioridadBusqueda` — el resultado depende del orden en que la consulta devuelva las filas. 23 más tienen conflicto resuelto por prioridad (no empatado, pero sí duplicado).
- **H-2 — 25 BINs inexistentes en la tabla de Payway, 100% de rechazo:** 25 BINs de la muestra no caen en ningún rango activo de Payway; las 25 operaciones fueron rechazadas, todas por el mismo motivo (ISO 1, "PEDIR AUTORIZACION"). El perfil (1 intento, siempre rechazado, BIN no reconocido) es compatible con tanteo de tarjetas/fraude, no con clientes confundidos — z=10,267, p≈1e-24.

**Hallazgos de severidad Media:**
- **H-3 — Amex sin regla de negocio:** la tabla interna identifica Amex como `"AMERICAN EXPRESS"`, pero `CardBusinessRules` tiene la regla como `AMERICANCREDITO` — la clave combinada no existe. En producción las operaciones Amex igual se envían correctamente (código 111), así que hay una normalización de nombre no documentada corriendo en algún punto. Mismo riesgo para Cencosud, CMR, Cordobesa, Tarshop y Nativa Vieja (marcas que la tabla interna reconoce pero `CardBusinessRules` no tiene entrada).
- **H-4 — MasterCard crédito concentra el mayor rechazo:** código 104, 42,34% de rechazo (más del doble del promedio), 24% de todo el rechazo del día — motivos del emisor, no de mapeo.
- **H-5 — 8 BINs donde 6 dígitos no alcanzan:** el mismo BIN6 abarca rangos activos de Payway de distinto tipo de producto (y en `589657`, hasta distinta marca — MasterCard y Cabal conviven). Premisa rota: 6 dígitos no identifican unívocamente marca+tipo para estos casos.

**Hallazgos de severidad Baja / sin riesgo:**
- **H-6 — 2 BINs con desacuerdo real de código** (`589657` y `250058`) — bajo volumen, corregibles por prolijidad de dato.
- **H-7 — código de error 12035 no catalogado** (5 dígitos, "Terminal no disponible", espacio de numeración de gateway, no de emisor).
- **H-8/H-9 — controles de higiene limpios:** sin reintentos duplicados, rechazo estable 15-23% durante todo el día (descarta incidente puntual).

## 2. Caso puntual confirmado (mail "Fwd: Error en BIN", 2026-09-07/14)

El BIN6 `454622` tiene 4 registros en el archivo de Payway bajo 4 BINs de 8 dígitos distintos: `45462200`=Prepaga, `45462201`/`45462202`/`45462203`=Crédito. Una tarjeta real (BBVA Visa Signature, confirmada por foto del cliente) corresponde a `45462210` (Crédito) — el sistema la toma como Prepaga porque solo mira los primeros 6 dígitos y encuentra el primer registro cargado (`45462200`).

## 3. Cruce BIN a BIN propio (tabla interna del 14/09/2026 vs. archivo Payway `BINES_T1952.TXT` del 19/08/2026)

De los **1.408 BINs activos** en `dbo.IssuerIdentification`: 1.016 (72,2%) correctos, 23 (1,6%) con discrepancia corregible, 163 (11,6%) en BIN6 estructuralmente ambiguos en el propio archivo de Payway (más de un tipo real conviviendo bajo el mismo BIN6 — irresolubles a 6 dígitos sin importar la frecuencia de actualización), 206 (14,6%) ausentes del archivo activo de Payway (199 de esos porque Payway los dio de baja y nunca se reflejó, 7 nunca existieron en su archivo). En la dirección inversa: de los **99.846 BIN6 que Payway declara activos, solo 1.408 (1,4%) están representados** en la tabla interna — 98.644 BIN6 son huecos totales de cobertura (sin cruzar todavía contra volumen transaccional real para saber cuántos importan).

## 4. Hallazgo nuevo — bug de datos en el mecanismo de override a Prepaga

La tabla interna no tiene un valor "Prepaga" en el campo `TipoTarjeta` (solo Débito/Crédito/Otra) — el override a Prepaga se aplica vía `dbo.AtributoValor`, `AtributoNombre='segmentoTarjeta'`, `Valor='P'` (confirmado cruzando la metodología del informe de Fintexa contra la estructura real de datos). De los 2.359 registros de `segmentoTarjeta` vinculados a un BIN activo hoy, solo **170 (7%)** tienen el valor real `'P'` — **2.052 (87%) tienen literalmente el string `"16"`**, el mismo valor típico del atributo `digitosTarjeta` (cantidad de dígitos del PAN). Patrón compatible con un bug de carga que pisó el valor de `segmentoTarjeta` con el de `digitosTarjeta` en algún proceso de importación histórico — pendiente de confirmación técnica de Fintexa (pregunta 5 de la consulta técnica del proyecto).

## 5. Contrato de la API (`Shared.IssuerIdentification.Api` v2, Swagger 09/04/2025)

Expone solo 2 endpoints, ambos de **consulta** (sin ABM/escritura): `GET /Bin/{bin}/{pan}` (recibe BIN + PAN completo + `digits`) y `GET /BINChecker/{bin}`. El patrón de validación del BIN acepta explícitamente 6 U 8 dígitos en ambos — el contrato ya anticipaba 8 dígitos, la tabla de datos nunca se pobló así. Sin confirmar si la lógica de resolución interna usa los dígitos adicionales del PAN.

## Ver también

- [`1_proyectos/rechazos_bines_payway/proyecto.md`](../rechazos_bines_payway/proyecto.md) (PRD-251) — proyecto vivo con el detalle completo del discovery, la consulta técnica enviada a Fintexa (12 preguntas) y los 4 CSV del cruce BIN a BIN.
- [`1_proyectos/contexto_vivo/2026-09-14_gap_tarjeta_prepaga_crecimiento_rechazo_sin_explicar.md`](2026-09-14_gap_tarjeta_prepaga_crecimiento_rechazo_sin_explicar.md) — gap de `/sync_metrics` sobre crecimiento anómalo de Tarjeta Prepaga, posiblemente explicado por este mismo problema (hipótesis sin confirmar).
