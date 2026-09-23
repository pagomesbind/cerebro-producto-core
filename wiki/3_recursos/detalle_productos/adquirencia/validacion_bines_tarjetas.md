# Validación e identificación de BINs de tarjeta — mecanismo transversal

> Estado: discovery activo (proyecto `rechazos_bines_payway`, PRD-251).

> Mecanismo **transversal a cualquier procesamiento de tarjeta** (no específico de un canal) — Bind PSP identifica el BIN de una tarjeta para determinar marca/tipo de producto (crédito, débito, prepaga) y rutear/validar el pago. Aunque el mecanismo nació documentado bajo POS multiadquirencia ([pos_multiadquirencia.md](pos_multiadquirencia.md), hasta 2026-09-14), hoy el mayor impacto por volumen está en **tarjeta no presente vía Botón Simple 1.0/2.0** ([boton_simple_2_0.md](boton_simple_2_0.md)) — este archivo consolida el tema como pieza temática propia en vez de vivir bajo un canal específico.

## 1. Origen — investigación informal de Fintexa (mail, 2026-05/08-2026)

> Fuente: hilo de mail "Análisis BINES Payway/Decidir", Fintexa (Agustín Grau, CTO), mensajes 2026-05-20 a 2026-08-19. Ticket de soporte Fintexa `AD-681` (Jira de Fintexa, no el de Bind) asociado. Contenido movido desde `pos_multiadquirencia.md §6` al mergear este item (2026-09-14) — ver nota de reclasificación al final de esta sección.

Investigación técnica de Fintexa sobre rechazos de transacciones con tarjeta relacionados a la identificación de BINes, cruzando tres fuentes: la configuración/identificación de BINes propia de Bind PSP, la base de datos de BINes de **Payway** (provista por Gonzalo Rivera) y lo que responde **Decidir** cuando rechaza una transacción (Decidir/Payway/Prisma son el mismo gateway, ver [`2_areas/direccion/decisiones.md`](../../../2_areas/direccion/decisiones.md) 2026-07-17).

**Primer análisis (2026-05-20, muestra de un día):** no se pudo concluir que los rechazos se expliquen por las diferencias entre bases — hay transacciones con los mismos atributos que sí están aprobadas. Hace falta ajustar la base de BINes propia, pero no está claro qué cambiar: lo que dice Decidir no coincide con la BD de BINes de Payway, y además hay BINes obtenidos de Global Processing (GP) que sí coinciden con los de Payway.

**Segundo análisis (2026-08-19, muestra completa de aprobadas y rechazadas de un día completo, 18/08 — 14.695 operaciones):** a diferencia del primero (muestra parcial), este análisis concluyó que había acciones concretas que se podían tomar ya y que darían mejoras instantáneas — pendiente en ese momento de una reunión para definirlas e implementarlas. Ese informe (9 hallazgos) es la base cuantitativa que retoma y confirma el discovery de PRD-251 (§3).

**Nota de reclasificación (2026-09-14):** esta investigación vivía documentada bajo `pos_multiadquirencia.md §6` porque el hilo de mail se relevó junto con el resto de la ingesta histórica de POS — pero el mecanismo de identificación de BIN no es específico del canal presente/POS. El PM confirmó (discovery de PRD-251) que hoy el mayor impacto por volumen está en tarjeta no presente (Botón Simple 1.0/2.0), no en POS. Contenido movido íntegro a este archivo; `pos_multiadquirencia.md` mantiene solo una referencia cruzada.

## 2. Causa raíz confirmada — 6 dígitos vs. 8 dígitos (reunión "Weekly - Producto / Operaciones", 2026-09-14)

> Fuente: Reuniones "Weekly - Producto / Operaciones" (2026-09-14) y "Análisis COBRO" (2026-09-14), con antecedente en "Producto" (2026-09-14). Hallazgo de Mariana Nadalin / Gonzalo Damian Rivera.

**Bind PSP identifica el BIN de una tarjeta tomando los primeros 6 dígitos, mientras que Payway usa 8 dígitos** para el mismo campo. Consecuencia concreta: tarjetas prepagas quedan mal clasificadas como tarjetas de crédito (y viceversa) porque el 7º/8º dígito es justamente el que distingue el tipo (ej. BIN `454622`: Bind lo tiene cargado como prepaga, pero en el archivo de Payway aparece 4 veces con distintos 7º-8º dígitos — 3 como crédito, 1 como prepaga real — ver también el caso puntual confirmado en §3.2, mismo BIN). Esto genera **rechazos operativos en producción hoy**: *"a nivel operativo estamos fallando, no estamos cobrando un montón de tarjetas por error de no tener la tabla de bines actualizada"* (Gonzalo Damian Rivera).

**Antigüedad del problema:** la tabla de BINs de Bind no se actualiza, según estimación de Gonzalo Damian Rivera, desde que se creó (~3-4 años atrás) — Payway deja un archivo actualizado todos los lunes en un portal propio, pero Bind nunca automatizó ni programó su descarga/carga.

**Decisiones tomadas en la reunión:**
- **Prioridad 1 (acordada):** actualización **manual** de la tabla de BINs con el archivo que provee Payway — Pablo Gomes toma la tarea de revisar el acceso al portal de Payway y evaluar la carga inmediata del archivo más actualizado que le pasen Gonzalo Damian Rivera / Mariana Nadalin.
- **Prioridad 2 (diferida):** automatizar la descarga/actualización semanal del archivo (hoy manual, "una fiaca" según Mariana Nadalin, pero viable como hábito semanal mientras no se automatice).
- **Requiere más debate (sin cerrar, se aplaza con Pablo Gomes):** si conviene además cambiar la lógica de evaluación de BIN de 6 a 8 dígitos en el motor de pagos — impacto no evaluado todavía (afecta procesos de validación en Payway y potencialmente en la lógica propia de determinar bines nuevos/soportados). Mismo tema aplazado también en la reunión "Análisis COBRO" (2026-09-14) por ausencia de Pablo Gomes, y consultado de nuevo por Nicolás Colón en la reunión "Producto" (2026-09-14) sin resolución ("no se toma una decisión final").

**Nota de alcance:** el mismo BIN de 6 dígitos también es relevante para el proyecto `titularidad_tarjeta` (consulta a MODO usa BIN + últimos 4 + DNI) — la ambigüedad de 6 vs. 8 dígitos podría afectar la implementación de esa validación también, a confirmar cuando se cierre esta definición.

## 3. Discovery completo PRD-251 — análisis cuantitativo, cruce propio y bug de datos (2026-09-14)

> Fuente: `/idea_start` — discovery del proyecto `rechazos_bines_payway` (PRD-251), completa el hilo de mails de §1 y corrige el alcance heredado de `pos_multiadquirencia.md §6`. Detalle completo del discovery, la consulta técnica enviada a Fintexa (12 preguntas) y los 4 CSV del cruce BIN a BIN en [`1_proyectos/rechazos_bines_payway/proyecto.md`](../../../1_proyectos/rechazos_bines_payway/proyecto.md) (PRD-251, PM Pablo Gomes).

### 3.1 Los 9 hallazgos del informe de Fintexa (19/08/2026, 14.695 operaciones del 18/08 completo)

**Refutación de la hipótesis de mayo:** el mapeo BIN→código de medio de pago que Bind envía a Decidir es correcto en el **98,14%** de los casos, y corregir el resto **no bajaría el rechazo general** — las operaciones con código discordante rechazan al 16,94% contra 19,15% de las concordantes (z=-0,976, p=0,33, no significativo). El rechazo real es estructural por tipo de producto (crédito 27,6% vs. débito 13,4%) y por motivo del emisor (denegada, fondos insuficientes), no por el mapeo BIN→código.

**Hallazgos de severidad Alta:**
- **H-1 — 60 BINs con resolución no determinística:** filas de la tabla interna con distinto tipo de tarjeta y la misma `PrioridadBusqueda` — el resultado depende del orden en que la consulta devuelva las filas. 23 más tienen conflicto resuelto por prioridad (no empatado, pero sí duplicado).
- **H-2 — 25 BINs inexistentes en la tabla de Payway, 100% de rechazo:** 25 BINs de la muestra no caen en ningún rango activo de Payway; las 25 operaciones fueron rechazadas, todas por el mismo motivo (ISO 1, "PEDIR AUTORIZACION"). El perfil (1 intento, siempre rechazado, BIN no reconocido) es compatible con tanteo de tarjetas/fraude, no con clientes confundidos — z=10,267, p≈1e-24.

**Hallazgos de severidad Media:**
- **H-3 — Amex sin regla de negocio:** la tabla interna identifica Amex como `"AMERICAN EXPRESS"`, pero `CardBusinessRules` tiene la regla como `AMERICANCREDITO` — la clave combinada no existe. En producción las operaciones Amex igual se envían correctamente (código 111), así que hay una normalización de nombre no documentada corriendo en algún punto. Mismo riesgo para Cencosud, CMR, Cordobesa, Tarshop y Nativa Vieja (marcas que la tabla interna reconoce pero `CardBusinessRules` no tiene entrada).
- **H-4 — MasterCard crédito concentra el mayor rechazo:** código 104, 42,34% de rechazo (más del doble del promedio), 24% de todo el rechazo del día — motivos del emisor, no de mapeo.
- **H-5 — 8 BINs donde 6 dígitos no alcanzan:** el mismo BIN6 abarca rangos activos de Payway de distinto tipo de producto (y en `589657`, hasta distinta marca — MasterCard y Cabal conviven). Premisa rota: 6 dígitos no identifican unívocamente marca+tipo para estos casos — mismo mecanismo raíz que §2.

**Hallazgos de severidad Baja / sin riesgo:**
- **H-6 — 2 BINs con desacuerdo real de código** (`589657` y `250058`) — bajo volumen, corregibles por prolijidad de dato.
- **H-7 — código de error 12035 no catalogado** (5 dígitos, "Terminal no disponible", espacio de numeración de gateway, no de emisor).
- **H-8/H-9 — controles de higiene limpios:** sin reintentos duplicados, rechazo estable 15-23% durante todo el día (descarta incidente puntual).

### 3.2 Caso puntual confirmado (mail "Fwd: Error en BIN", 2026-09-07/14)

El BIN6 `454622` tiene 4 registros en el archivo de Payway bajo 4 BINs de 8 dígitos distintos: `45462200`=Prepaga, `45462201`/`45462202`/`45462203`=Crédito. Una tarjeta real (BBVA Visa Signature, confirmada por foto del cliente) corresponde a `45462210` (Crédito) — el sistema la toma como Prepaga porque solo mira los primeros 6 dígitos y encuentra el primer registro cargado (`45462200`).

### 3.3 Cruce BIN a BIN propio (tabla interna del 14/09/2026 vs. archivo Payway `BINES_T1952.TXT` del 19/08/2026)

De los **1.408 BINs activos** en `dbo.IssuerIdentification`: 1.016 (72,2%) correctos, 23 (1,6%) con discrepancia corregible, 163 (11,6%) en BIN6 estructuralmente ambiguos en el propio archivo de Payway (más de un tipo real conviviendo bajo el mismo BIN6 — irresolubles a 6 dígitos sin importar la frecuencia de actualización), 206 (14,6%) ausentes del archivo activo de Payway (199 de esos porque Payway los dio de baja y nunca se reflejó, 7 nunca existieron en su archivo). En la dirección inversa: de los **99.846 BIN6 que Payway declara activos, solo 1.408 (1,4%) están representados** en la tabla interna — 98.644 BIN6 son huecos totales de cobertura (sin cruzar todavía contra volumen transaccional real para saber cuántos importan).

### 3.4 Hallazgo nuevo — bug de datos en el mecanismo de override a Prepaga

La tabla interna no tiene un valor "Prepaga" en el campo `TipoTarjeta` (solo Débito/Crédito/Otra) — el override a Prepaga se aplica vía `dbo.AtributoValor`, `AtributoNombre='segmentoTarjeta'`, `Valor='P'` (confirmado cruzando la metodología del informe de Fintexa contra la estructura real de datos). De los 2.359 registros de `segmentoTarjeta` vinculados a un BIN activo hoy, solo **170 (7%)** tienen el valor real `'P'` — **2.052 (87%) tienen literalmente el string `"16"`**, el mismo valor típico del atributo `digitosTarjeta` (cantidad de dígitos del PAN). Patrón compatible con un bug de carga que pisó el valor de `segmentoTarjeta` con el de `digitosTarjeta` en algún proceso de importación histórico — pendiente de confirmación técnica de Fintexa (pregunta 5 de la consulta técnica del proyecto).

### 3.5 Contrato de la API (`Shared.IssuerIdentification.Api` v2, Swagger 09/04/2025)

Expone solo 2 endpoints, ambos de **consulta** (sin ABM/escritura): `GET /Bin/{bin}/{pan}` (recibe BIN + PAN completo + `digits`) y `GET /BINChecker/{bin}`. El patrón de validación del BIN acepta explícitamente 6 u 8 dígitos en ambos — el contrato ya anticipaba 8 dígitos, la tabla de datos nunca se pobló así. Sin confirmar si la lógica de resolución interna usa los dígitos adicionales del PAN.

> ⚠️ **Corrección (2026-09-21):** este párrafo y el análisis técnico-funcional de `rechazos_bines_payway-solution.md §6.3` daban por Supuesto/no confirmado que el backend del checkout de tarjeta no presente "recibe el tipo ya resuelto, no vuelve a consultar la base". Fintexa confirmó que **sí la consulta** — como chequeo de consistencia contra el frontend, no como fuente primaria. Ver mecanismo completo en §4 (nueva). Gap abierto en [`2_areas/gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md) [2026-09-21].

## 4. Checkout de tarjeta no presente — dos sistemas independientes resuelven el tipo de tarjeta, con chequeo de consistencia que rechaza con 400 si discrepan

> Fuente: mail de Melisa Belpassi (Fintexa), hilo del ticket AD-978 — proyecto `rechazos_bines_payway` (PRD-251), 2026-09-21.

Fintexa confirmó, al explicar por qué el ticket de carga masiva de BINs (AD-978, ~89.717 altas) no se puede aplicar todavía en producción, qué componente resuelve marca/tipo de tarjeta en el checkout de tarjeta no presente (Botón Simple) antes de que el pago llegue al backend — gap abierto hasta ahora del proyecto PRD-251.

**Hay dos sistemas independientes que intentan identificar el tipo de tarjeta (Crédito/Débito/Prepaga) a partir del BIN, en dos momentos distintos del mismo pago:**

1. **Frontend — al tipear el número de tarjeta:** la pantalla de pago usa un archivo de configuración estático, `payment_methods.json`. Si no tiene esa tarjeta identificada puntualmente, aplica una regla general de respaldo: "empieza con 4 → Visa Crédito; empieza con 5 → Mastercard Crédito".
2. **Backend — al confirmar el pago:** el servidor vuelve a resolver el tipo de tarjeta, esta vez consultando la base real `IssuerIdentification` (§3.5). Si tampoco la tiene identificada puntualmente, aplica la **misma** regla general de respaldo.

**Chequeo de consistencia:** al confirmar el pago, el backend compara lo que dijo el frontend contra lo que dice `IssuerIdentification`. Si no coinciden, lo trata como inconsistencia sospechosa y corta la operación con **`400`** ("tarjeta no habilitada") — el pago nunca se termina de procesar.

**Por qué hoy funciona (por casualidad, no por estar bien identificado):** para una tarjeta que ninguno de los dos sistemas tiene identificada puntualmente, ambos caen en la misma regla de respaldo genérica, coinciden, y el pago se aprueba — aunque la clasificación sea incorrecta de fondo (el problema real que motiva PRD-251).

**Por qué el INSERT de BINs reales genera rechazos nuevos:** el script de carga de PRD-251 actualiza `IssuerIdentification` con la clasificación real y específica de cada tarjeta (para el 40% de las ~89.717 tarjetas de AD-978, la clasificación real es Débito o Prepaga, no Crédito). El archivo `payment_methods.json` del frontend **no se toca** con ese script — sigue con la regla genérica vieja. Resultado: toda tarjeta que pasa de "sin identificar, ambos coinciden por regla genérica" a "identificada con precisión solo en el backend" genera una discrepancia, y el chequeo de consistencia la rechaza con 400 — aunque sea una tarjeta perfectamente válida.

**Ejemplo real (BIN `480459`, Visa):** hoy — frontend dice "Crédito" (regla genérica) · backend dice "Crédito" (regla genérica) → coinciden → aprobado. Después del INSERT — frontend sigue diciendo "Crédito" (no se tocó) · backend dice "Prepaga" (dato real) → no coinciden → **rechazado**.

**Alternativa de fondo descartada como inmediata por Fintexa:** cambiar el frontend para que `payment_methods.json` se use solo de forma visual (logo/nombre de marca) sin participar en ninguna validación — dejaría de funcionar a ~35.000 tarjetas que hoy están identificadas puntualmente en el json y dependen de esa identificación (detalle sin desarrollar más por Fintexa).

**Preguntas sin responder de Fintexa (PM, 2026-09-21):** (1) ¿se puede actualizar `payment_methods.json` en el mismo momento que `IssuerIdentification`? (2) ¿convendría migrar el checkout para que valide únicamente contra `IssuerIdentification` vía API, en vez de mantener copia estática en el frontend — es una decisión ya evaluada, o hay restricción técnica/de seguridad? Ver `1_proyectos/rechazos_bines_payway/gaps.md` (2026-09-21).

**Fix temporal acordado (reunión "Análisis COBRO", 2026-09-21) — y resolución de fondo (22/09):** ante la urgencia de evitar pérdida de clientes por rechazos de tarjetas válidas, Melisa Belpassi y Matías Sassa (Fintexa) acordaron desarrollar, probar y desplegar en la semana un **ajuste temporal de las expresiones regulares de `payment_methods.json`**, dejando a `IssuerIdentification`/Isure como fuente de verdad al confirmar el pago — sin eliminar la funcionalidad visual del frontend ni permitir que pasen tarjetas inválidas (instrucción explícita de Pablo Gomes). Al día siguiente (22/09, reunión "Repaso Semanal líderes"), Fintexa decidió ir más allá del ajuste temporal: **eliminar la validación de bines del frontend directamente** (responde de facto a la pregunta 2 de arriba), empaquetado en el despliegue de la versión 73 (jueves 24/09) — ver seguimiento completo en [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) (PRD-251). Este mismo trasfondo técnico es el que ya trackea `tareas.md` (T-055) desde el 2026-09-14 como "BIN 6 vs. 8 dígitos" — la fase 2 de ese frente (ampliar de 6 a 11 dígitos la detección de BIN en POS/checkout) sigue sin fecha.

## Ver también

- [`1_proyectos/rechazos_bines_payway/proyecto.md`](../../../1_proyectos/rechazos_bines_payway/proyecto.md) (PRD-251) — proyecto vivo con el detalle completo del discovery, la consulta técnica enviada a Fintexa (12 preguntas) y los 4 CSV del cruce BIN a BIN.
- [`1_proyectos/contexto_vivo`](../../../1_proyectos/contexto_vivo/) `2026-09-14_gap_tarjeta_prepaga_crecimiento_rechazo_sin_explicar.md` — gap de `/sync_metrics` sobre crecimiento anómalo de Tarjeta Prepaga, posiblemente explicado por este mismo problema (hipótesis sin confirmar).
- [pos_multiadquirencia.md](pos_multiadquirencia.md) — integración de Prisma/GP como procesadores de POS (canal donde este mecanismo se documentó originalmente, hasta la reclasificación de 2026-09-14).
- [boton_simple_2_0.md](boton_simple_2_0.md) — canal de tarjeta no presente (Botón Simple 1.0/2.0) donde hoy se concentra el mayor volumen de impacto de este mecanismo.
