# Ardid/Akurtech — Módulo de Pagos (Tarjeta)

> Estado: en producción.

> Fuente: `Akurtech 3 - Pagos.pdf` (81 páginas), guía funcional oficial del proveedor. Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general.

## 1. Vista general de la pestaña Pagos

En la pestaña **Pagos** del Menú del Dashboard hay dos grandes cards: la superior corresponde a **Pagos** y la inferior a **Reglas de Pago**.

La card **Pagos** muestra:
- Gráfico tipo dona con el **Top 3 de tarjetas más utilizadas** + "Otros" (agrupa el resto).
- **Estado de Pagos**: conteo histórico de **Realizados** y **Rechazados**.
- **Top 5 de Canales de Pago** más utilizados.

La pantalla **Pagos** permite monitorear y analizar todas las transacciones procesadas: ver el estado de cada transacción (rechazadas o realizadas) y revisar si se aplicó alguna regla, para entender la decisión tomada.

> ⚠️ **Nota sobre el estado "Pendiente":** el texto fuente sólo documenta los estados **Realizados/Aprobados** y **Rechazados** (histórico y en tiempo real, actualizado hora a hora). No se encontró mención explícita a un estado "Pendiente" de pagos en esta guía. Este dato queda resuelto/complementado en [reporteria_alertas.md](reporteria_alertas.md#12-reportes-custom): el catálogo de estados de Reportes Custom confirma que el estado **"Pendiente" de pagos sí existe** en el producto (desde la versión 1.17 — ver [historico/historial_versiones.md](historico/historial_versiones.md)), aunque esta guía específica de Pagos no lo mencione en su listado principal.

## 2. Gráficos y paneles de la pantalla de Pagos

| Elemento | Descripción |
|---|---|
| Gráfico de tipos de pago más utilizados | Dona con porcentajes de tipos de tarjeta más usadas en transacciones; "Otros" agrupa el resto. |
| Estado de Pagos | Cantidades de pagos aprobados y rechazados; se actualiza hora a hora. |
| Listado de Pagos | Transacciones interceptadas, listadas de últimas a primeras, 10 por página, paginado inferior. Columnas = campos tildados en "Campos a visualizar". |

Nota funcional: desde **Parametrías Generales → sección Pagos** se configuran los catálogos: Canales de Pago, Tipos de Pago, Tipos de Tarjeta, Grupos de comercio y Grupos de Bin (ver [configuracion_inicial.md](configuracion_inicial.md#3-parametrías-generales), parámetro 3.1.10).

## 3. Campos a visualizar (columnas habilitables del listado)

Nombre y apellido, DNI, ID de Transferencia, Fecha, Email, ID del Ente, Código de entidad, Cuotas, Moneda, Importe, Comercio, ID tx Comercio, BIN, Últimos 4, Mes de Vencimiento, Año de vencimiento, Código de tarjeta, HASH, IP, Dispositivo, Tipo de tarjeta, Canal de pago, Tipo de Pago, Grupo de comercio, Grupo de bin, Estado, Motivo de Rechazo, Nombre de Restricción.

**Buscador / filtros**: al presionar el Buscador (lupa) se activan los filtros de cada columna habilitada, con los mismos campos de arriba. **Resetear valores de búsqueda**: limpia todos los filtros aplicados. **Descargar .csv**: descarga el listado de pagos (o pagos filtrados).

## 4. Pagos – Aciertos

Gráfico tipo dona con líneas porcentuales que clasifican los pagos en: **Aprobada Confiable**, **Aprobada Fraude (Error Tipo II)**, **Rechazada Confiable (Error Tipo I)**, **Rechazada Fraude**.

Incluye dos recuadros: **Nivel de Significancia** y **Nivel de Potencia** (color verde y/o rojo). Ambos valores se configuran previamente en **Parametrías de Entidad** y se usan para comparar contra las líneas porcentuales del gráfico, permitiendo analizar el desempeño del sistema antifraude.

## 5. Contracargo masivo

Carga masiva de **contracargos** mediante archivo CSV. Modal con opciones: **"Descargar ayuda de formato"** (CSV con instrucciones), **"Descargar ejemplo"** (CSV de ejemplo), subir archivo con formato correcto → botón Aceptar → mensaje de confirmación. Ver la API equivalente `/FileProcessController/Process` en [apis_externas.md](apis_externas.md#23a-uploadchargebacktransactionsfile-post).

## 6. Carga masiva de pagos

Mismo mecanismo que el contracargo masivo: modal con "Descargar ayuda de formato" y "Descargar ejemplo", subida de CSV y botón Aceptar, con mensaje de confirmación al completar.

## 7. Marcado manual de pagos ("Marcar")

En la columna **Acciones** hay un botón **Marcar** para dejar asentada una transacción específica como **Fraudulenta** o **Confiable**:
- Al marcar aparece un listado de opciones para elegir (colaboran en el entendimiento de lo marcado).
- Al hacer clic en una o más opciones se habilita una flecha para pasarlas a la columna correspondiente (**Columna NO** – **Columna SI**).
- Hay un campo para escribir un **comentario**.
- Se confirma con el botón **Aceptar**.

**Excepción por marcado "Confiable":** solo cuando un pago se marca como "Confiable" se le puede **habilitar temporalmente**. Esto permite al usuario volver a realizar una transferencia sin que la restrinja la regla que antes la había rechazado. Esta habilitación:
- Se conoce como **excepción**.
- Aplica solo durante el tiempo configurado en la habilitación.
- Es válida para **un solo pago** de ese usuario.

La marca se ve reflejada en el listado de pagos si se habilita la **Propiedad Marca**. Una vez marcado, el botón "Marca" cambia a **"Descripción"**, que al presionarlo abre el modal de detalle de lo marcado (permite seguir agregando comentarios).

## 8. Reglas de Pago — Reglas Estándar

Card con cuatro subcards: **Reglas por cliente**, **Reglas por tarjeta**, **Reglas por comercio** y **Reglas por control de frecuencia**. Cada una muestra una dona con % de reglas habilitadas/deshabilitadas.

### 8.1. Reglas Estándar — Reglas por Cliente

Controles sobre transacciones de clientes dados de alta en Akurtech, basados en CUIT/CUIL/DNI. Detectan actividad inusual (cambio de contraseña + envío de dinero, cambio de dispositivo, recepción con envío inmediato, etc.). Activables/desactivables sin reiniciar servicios.

**Campos al crear ("Crear nueva"):** Nombre de Restricción, Modo de creación de cuenta, Tipo de persona (Física o Jurídica), Tipo de Banca (Cliente o Empresa), Tipo de Cliente, Tipo de Producto, Tipo de Subproducto, Tipo de Comercio (Ninguno / Incluir varios / Todos excepto), Moneda, Monto, Día de la semana, Vigencia horaria (24hs o Desde-Hasta), Vigencia del día.

**Acciones Anteriores disponibles (reglas por cliente):**

| Acción anterior | Qué evalúa |
|---|---|
| Todos | Prosigue directo a la configuración de Acciones |
| Antigüedad de la cuenta | Días que la cuenta lleva activa en Akurtech; si no cumple el mínimo, afecta la transacción |
| Cambio de e-mail | Minutos desde el último cambio de correo |
| Cambio de dispositivo | Minutos desde el último cambio de dispositivo |
| Login fallido | Cantidad de intentos de login fallidos en un período |
| Frecuencia de pagos en tarjetas | Uso de tarjeta en pagos en período corto (segundos) |
| Monto acumulado diario | Total transaccionado en el día |
| Monto acumulado mensual | Total transaccionado en el mes |
| Cantidad de pagos acumulados diarios | Cantidad de pagos en el día |
| Cantidad de pagos acumulados mensuales | Cantidad de pagos en el mes |
| Porcentaje perfil transaccional diario | Desviación vs. perfil transaccional esperado (diario) |
| Porcentaje perfil transaccional mensual | Desviación vs. perfil transaccional esperado (mensual) |
| Porcentaje haber transaccional diario | % del haber disponible transaccionado en el día |
| Porcentaje haber transaccional mensual | % del haber disponible transaccionado en el mes |
| Cantidad de tarjetas emitidas | Cantidad de tarjetas emitidas para la cuenta |

**Acciones:** Bloqueo de cuenta / Rechazo de transacciones / Solicitud de challenge. **Alerta (habilitar/deshabilitar):** Alerta Operativa / Alerta PLAFT.

**Listado de reglas:** columnas Nombre, Fecha, Monto, Moneda, Habilitado (switch), Acciones (Editar / Eliminar).

### 8.2. Reglas Estándar — Reglas por Tarjeta

Controles sobre transacciones con tarjeta, parametrizables por moneda, perfil de cliente, día/hora o destinatario. Activables/desactivables sin modificar código; usan IA para mejorar continuamente en base a históricos.

**Campos al crear:** Nombre de Restricción, Grupo de Bin, Canal de pago, Tipo de pago, Tipo de Tarjeta, Grupo de comercio, Moneda, Monto, Día de la semana, Vigencia horaria, Vigencia del día.

**Acciones Anteriores (reglas por tarjeta)** — todas con opción de período en **minutos, días o meses** salvo donde se indique:

| Acción anterior | Qué evalúa |
|---|---|
| Ninguno | Prosigue directo a Acciones |
| Distancia en KM y Tiempo por tarjeta | Distancia geográfica (km) entre dos transacciones de la misma tarjeta vs. tiempo transcurrido (minutos); si la distancia es ilógica para el tiempo, se marca sospechosa |
| Cantidad máxima de pagos acumulados por tarjeta | Cantidad de pagos por tarjeta en un período |
| Monto acumulado por tarjeta | Total transaccionado por tarjeta en un período |
| Cantidad máxima de correos por tarjeta | Correos distintos usados con la misma tarjeta |
| Cantidad máxima de pagos por correo | Pagos asociados a un mismo correo |
| Monto acumulado por correo | Total transaccionado por correo |
| Cantidad máxima de tarjetas distintas por correo | Tarjetas distintas usadas con un mismo correo |
| Cantidad máxima de pagos por ip | Evalúa pagos/monto por IP *(la descripción textual de la fuente mezcla "cantidad" con "monto" — ver nota de fidelidad abajo)* |
| Monto acumulado por ip | Total transaccionado por IP |
| Cantidad máxima de pagos por dispositivo | Evalúa pagos/monto por dispositivo *(misma observación)* |
| Monto acumulado por dispositivo | Total transaccionado por dispositivo |
| Cantidad máxima de tarjetas distintas por identificación | Tarjetas distintas usadas por una misma identificación (CUIT/DNI) |
| Cantidad máxima de pagos por identificación | Pagos/monto asociado a una misma identificación |

> Nota de fidelidad: la fuente describe "Cantidad máxima de pagos por ip" y "Cantidad máxima de pagos por dispositivo" con un texto que parece corresponder más a un control de **monto** que de **cantidad** — posible inconsistencia o error de redacción en el documento original del proveedor.

**Acciones:** Bloqueo de cuenta / Rechazo de transacciones / Solicitud de challenge. **Alerta:** Alerta Operativa / Alerta PLAFT.

### 8.3. Reglas Estándar — Reglas por Comercio

Parametrizables por monto mínimo, tipo de moneda, día y hora.

**Campos al crear:** Nombre de restricción, Grupo de comercio, Monto mínimo, Monto máximo, Tipo de Moneda, Día de la semana, Vigencia horaria, Vigencia del día.

**Acciones Anteriores (reglas por comercio):**

| Acción anterior | Qué evalúa |
|---|---|
| Todos | Prosigue directo a Acciones |
| Exceso de volumen operado respecto al perfil transaccional | Volumen operado vs. perfil transaccional, en % dentro de un período (días/meses/años) |
| Incremento abrupto del volumen sin justificación comercial | Incremento de volumen en % dentro de un período |
| Porcentaje inusual de operaciones | % de operaciones (cualquier estado) dentro de un período |
| Repetición sistemática de montos idénticos | Cantidad de transacciones exitosas con el mismo monto dentro de un período |
| Porcentaje elevado de devolución promedio anual con el rubro declarado | % de devoluciones promedio anual |
| Porcentaje inconsistente de ticket promedio anual con el rubro declarado | % de exceso del ticket promedio anual respecto al rubro declarado |
| Inconsistencia geográfica por comercio/sucursal | Distancia de la transacción superior a la determinada |
| Rechazo de pagos con la misma titularidad del comercio | Pago rechazado donde la cuenta/medio de pago pertenece al mismo individuo/entidad que opera el comercio |

**Acciones:** Bloqueo de comercio / Rechazo de transacción. **Alerta:** Alerta Operativa / Alerta PLAFT.

### 8.4. Reglas Estándar — Reglas por Control de Frecuencia de Pagos

Controles según frecuencia de transacciones. Parametrizable por monto mínimo, moneda, día y hora.

**Campos al crear:** Nombre de Restricción, Monto mínimo, Monto máximo, Tipo de Moneda, Día de la semana, Vigencia horaria, Vigencia del día.

**Acciones Anteriores (control de frecuencia):**

| Acción anterior | Qué evalúa |
|---|---|
| Todos | Prosigue directo a Acciones |
| Cantidad de intentos de pagos con un mismo dispositivo con distintas tarjetas | Intentos (cualquier estado) con mismo dispositivo + distintas tarjetas |
| Cantidad de pagos realizados con un mismo dispositivo con distintas tarjetas | Pagos exitosos con mismo dispositivo + distintas tarjetas |
| Cantidad de intentos de pagos con un mismo dispositivo con distintos correos | Intentos con mismo dispositivo + distintos correos |
| Cantidad de pagos realizados con un mismo dispositivo con distintos correos | Pagos exitosos con mismo dispositivo + distintos correos |
| Cantidad de intentos de pagos con la misma IP con distintas tarjetas | Intentos con misma IP + distintas tarjetas |
| Cantidad de pagos realizados con la misma IP con distintas tarjetas | Pagos exitosos con misma IP + distintas tarjetas |
| Cantidad de intentos de pagos con la misma IP con distintos correos | Intentos con misma IP + distintos correos |
| Cantidad de pagos realizados con la misma IP con distintos correos | Pagos exitosos con misma IP + distintos correos |
| Cantidad de intentos de pagos por dispositivo | Intentos con mismo dispositivo |
| Cantidad de pagos realizados por dispositivo | Pagos exitosos con mismo dispositivo |
| Cantidad de intentos de pagos por IP | Intentos con misma IP |
| Cantidad de pagos realizados por IP | Pagos exitosos con misma IP |
| Cantidad de intentos de pagos por correo | Intentos con mismo correo |
| Cantidad de pagos realizados por correo | Pagos exitosos con mismo correo |
| Cantidad máxima de pagos realizados por identificación | Pagos exitosos con misma identificación (dentro de X minutos) |
| Cantidad máxima de intentos de pagos por identificación | Intentos con misma identificación (dentro de X días) |

Varias de estas reglas contemplan **excepciones**: si el dispositivo o la IP están dentro de las excepciones configuradas, no se activa la regla.

**Regla de unicidad:** una vez que una "acción anterior" se usa para crear una regla, desaparece del listado de opciones disponibles hasta que se elimine la regla que la usa — es imposible tener dos reglas con la misma acción anterior.

## 9. Reglas de Pago — Reglas Reputacionales

Evalúan el riesgo de fraude/abuso construyendo una **reputación dinámica** por usuario/cuenta según su comportamiento en pagos. A mayor puntaje, mayor riesgo; a menor puntaje, mayor confianza. Datos provienen de **Blacklist/Whitelist** (ver [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md)). Cada regla asigna entre **1 y 1000 puntos**.

- **Reglas Negativas** (riesgo, ej. "Dispositivo sospechoso", "IP sospechosa"): suman puntos (+).
- **Reglas Positivas** (confianza, ej. "Tarjeta conocida", "Identificación válida"): restan puntos (-).

**Acciones** — Puntuación Total (Aprobar / Solicitar Challenge / Rechazar / Bloqueo de Cliente, ver [scoring.md](scoring.md) para el detalle completo del modelo de umbrales). Al presionar "Aceptar" se generan **modificaciones pendientes**, que solo un usuario con permisos suficientes puede aprobar/rechazar.

## 10. Reglas de Pago — Reglas IA por Tarjetas

Al ingresar a "Reglas IA por tarjetas": lado izquierdo = reglas disponibles para habilitar/parametrizar; lado derecho = configuración de la regla seleccionada. A medida que se cargan Reglas IA se habilitan las opciones propias de **Reglas Machine Learning**.

| Regla IA | Parámetros de configuración |
|---|---|
| **Comercio habitual** | Cantidad mínima de pagos hacia un destinatario + rango de tiempo (días). Aprende comercios habituales del cliente vía IA. |
| **Día y Horario habitual** | Cantidad mínima de pagos + rango de tiempo (días). Aprende días/horarios habituales. |
| **Dispositivo habitual** | Cantidad mínima de pagos + rango de tiempo (días). Aprende dispositivos habituales. |
| **IP habitual** | Cantidad mínima de pagos + rango de tiempo (días). Aprende IPs habituales. |
| **Geolocalización habitual** | Tipo de geolocalización (País, Región, Ciudad o Código Postal); cantidad mínima de conexiones para considerar "habitual" (ej. 5); Tiempo mínimo en horas desde la última conexión; Rango de tolerancia (%) sobre ese tiempo mínimo. |
| **Monto habitual** | Al Agregar Nuevo: Grupo de bin, Canal de pago, Tipo de Pago, Tipo de Tarjeta, Grupo de comercio, Tipo de moneda, Cantidad de periodos, Rango de monto, Tiempo (días), Activar/desactivar Emisor habitual. |
| **Montos acumulados habituales** | Al Agregar Nuevo: Grupo de Bin, Canal de pago, Tipo de pago, Tipo de tarjeta, Grupo de comercio, Moneda, Cantidad de periodos, Duración del periodo, checkbox Días o Meses, fecha de inicio, activar/desactivar uso de ciclos → si se activa: Cantidad de ciclos y, por cada ciclo, día desde/hasta (ej. ciclos 1-15, 16-20 para ajustar a patrones de inicio/fin de mes). |

Flujo común a todas: configurar parámetros → botón **Guardar** → se activan **modificaciones pendientes** → usuario con permisos puede **aprobar individualmente** (botón "Consulta"), usar **"Aprobar todo"**, o **"Rechazar"** (individual o "Rechazar todo").

## 11. Reglas de Pago — Reglas Machine Learning

Visualiza riesgos potenciales vía modelos de aprendizaje automático de la habitualidad del usuario. Son del tipo **reputacional**. **Dependencia:** si una regla de IA no está activa, tampoco puede activarse la regla de ML correspondiente.

**Tabla de correspondencia Regla ML ↔ Regla IA (según la fuente):**

| Regla ML | Tipo | Regla IA asociada |
|---|---|---|
| Geolocalización no habitual | Negativa | Geolocalización |
| Geolocalización habitual | Positiva | Geolocalización |
| Destinatario no habitual | Negativa | Destinatario |
| Destinatario habitual | Positiva | Destinatario |
| Monto Acumulado no habitual | Negativa | Monto Acumulado |
| Monto Acumulado habitual | Positiva | Monto Acumulado |
| Horario no habitual | Negativa | Día y hora |
| Horario habitual | Positiva | Día y hora |
| Día no habitual | Negativa | Día y hora |
| Día habitual | Positiva | Día y hora |
| Dispositivo no habitual | Negativa | Dispositivo |
| Dispositivo habitual | Positiva | Dispositivo |
| IP no habitual | Negativa | IP |
| IP habitual | Positiva | IP |
| Monto no habitual | Negativa | Monto |
| Monto habitual | Positiva | Monto |

> Nota: la tabla menciona reglas IA de "Destinatario" y "Monto Acumulado" que no aparecen desarrolladas explícitamente como cards individuales en la sección 10 (que documenta Comercio, Día y Horario, Dispositivo, IP, Geolocalización y Monto habitual) — posible desalineación entre el catálogo de Reglas IA y el de Reglas ML en la documentación del proveedor.

Cada regla se activa o no. Según el resultado de las reglas ML se obtiene un valor que se contrarresta con el resultado de los otros tipos de reglas; **el sistema toma la acción más restrictiva**.

## 12. Reglas de Pago — Reglas Comportamentales

Analizan la conducta del usuario en la **Aplicación móvil** de la entidad; se activan por entidad. Requisito previo: la entidad debe tener al menos una **Aplicación** creada y parametrizada con más de una **Acción Comportamental** (ver [configuracion_inicial.md](configuracion_inicial.md#4-parametrías-de-entidad)).

**Crear Nueva:** Nombre de la Regla; Tipo de regla: **Acción vs Acción** o **Acción** — mismos campos y lógica que la Regla Comportamental de Transferencias/Login (ver [modulo_transferencias.md](modulo_transferencias.md#552-crear-nueva-regla-comportamental--campos) para el detalle completo de campos: Rango de tolerancia, Desvío del cálculo de promedio, Superficie/Tiempo de presión/Posición, Puntuación Negativa/Positiva).

**Regla de resolución:** ante una transferencia de cuenta sospechosa o con score negativo, el sistema contrasta el resultado con los demás tipos de reglas parametrizadas y aplica **la acción más restrictiva activada**.

## 13. Sobre "Auditoría de reglas"

El texto fuente no contiene una sección dedicada explícitamente titulada "Auditoría de reglas". Lo más cercano documentado es el mecanismo transversal de **"modificaciones pendientes"**: toda alta, edición o eliminación de reglas Reputacionales, IA, Machine Learning y Comportamentales genera una modificación pendiente que debe ser aprobada o rechazada por un usuario con permisos distintos/adicionales, mostrando en el modal el valor anterior vs. el valor tras la modificación. El módulo formal de "Reporte de Auditoría" (ver [reporteria_alertas.md](reporteria_alertas.md#2-reporte-de-auditoría)) es donde este flujo queda finalmente registrado y consultable.

## 14. Identificación de tarjetas por hash — mecánica real y hallazgos operativos

> Este apartado proviene de reuniones operativas (no del manual del proveedor) — aclara y extiende lo documentado en §3 (columna HASH del listado de pagos).

### 14.1 Criterio real de identificación — hash de los 16 dígitos completos (2026-08-24)

> Fuente: Reunión "ARDID" (2026-08-24), minuta + transcripción Gemini.

En esta reunión, Nicolás Colón le aclaró a Rocío Revelli (Soporte) el criterio real de identificación de tarjetas que usa Ardid, a raíz de una consulta de un cliente (Maru, vía Payway) sobre una tasa alta de rechazos que atribuía a límites diarios por tarjeta.

**Decisión/definición acordada:** la identidad de una tarjeta en Ardid se determina **únicamente por el hash de los 16 dígitos completos** del número de tarjeta — nunca por el DNI del pagador, ni por coincidencia parcial de los primeros seis/últimos cuatro dígitos (formato típico que entregan los procesadores como Payway). Dos operaciones con los mismos primeros/últimos dígitos pero distinto tramo medio son, para Ardid, tarjetas distintas con hashes distintos — y por lo tanto las reglas de límite diario (ej. "máximo 3 pagos por día") se evalúan por hash, no por esos datos parciales. Se validó esto en vivo contra Mongo (vía Cosmos Connect, colección `transaction`): al filtrar por el hash real de una tarjeta puntual solo aparecieron 2 operaciones en ~45 días de retención, mientras que el archivo que había armado Payway con datos parciales mostraba muchas más operaciones "coincidentes" que en realidad correspondían a tarjetas distintas (confirmado además por DNIs y emails distintos entre esas operaciones).

**Dato adicional relevante:** el DNI y el email que se cargan en el botón de pagos son datos de completado libre (no hace falta que sean del titular de la tarjeta/deuda) — no se usan para la identidad de la tarjeta. Ardid sí tiene una función para validar que una tarjeta, la primera vez que se usa, quede asociada a un DNI y exigir que las siguientes veces venga con el mismo DNI — pero está **deshabilitada** para evitar bloqueos por errores de tipeo del usuario final. Hay un proyecto próximo provisto por Modo que permitirá validar los 16 números de tarjeta contra el DNI de la persona usuaria.

### 14.2 Bloqueo permanente de tarjeta por hash ligado al primer vencimiento cargado (2026-08-26)

> Fuente: `/sync_meetings` — reunión "Previa demo mayoristas" (2026-08-26), minuta Gemini. Surgido durante un ensayo (dry-run) de la demo a la cámara de supermercados mayoristas, en pagos con enlace/QR — problema real de plataforma, no simulado.

Si en el **primer pago** con una tarjeta se ingresa una fecha de vencimiento incorrecta, el sistema genera un hash que asocia el número de tarjeta a esos datos erróneos **de forma permanente** — la tarjeta queda bloqueada para siempre con ese error, sin mecanismo de autocorrección.

- El hash se compone **exclusivamente de los 16 dígitos de la tarjeta** (consistente con §14.1), pero una vez generado queda atado al primer vencimiento con el que se registró — si ese dato estaba mal, no hay forma de que el sistema lo corrija solo.
- Diseño histórico heredado de **Billetera Santa Fe**, pensado originalmente como control antifraude (evitar que se reintenten combinaciones de tarjeta+vencimiento).
- Cuestionamiento abierto (Pablo Gomes): vigencia de ese diseño para el caso de una tarjeta **renovada legalmente** (mismo número, nuevo vencimiento) — con la regla actual, esa renovación legítima también quedaría bloqueada.
- **Workaround manual ya conocido por Soporte** (mostrado en vivo por Rocío Revelli): cambiar el estado de la tarjeta de "hash bloqueado" a "inválido" permite que el sistema genere un hash nuevo y el cliente pueda reintentar la operación. Tras aplicar el cambio, la transacción pasa a estado pendiente (confirmado por Adriana Endzeliz).

No quedó registrado en la reunión si existe hoy un ticket o pedido formal para automatizar este workaround o revisar la vigencia de la regla heredada — es un hallazgo de mecánica de producto, no una decisión de rediseño.

### 14.3 Mejora pedida — incluir el ID de regla de Ardid en los códigos de rechazo de TRX

> Fuente: misma reunión "Previa demo mayoristas" (2026-08-26).

Gonzalo Rivera propuso que, cuando una transacción se rechaza por Ardid (ej. código 1001), la base de TRX (transacciones) de Bind PSP incluya además, entre paréntesis, el **ID de la regla específica** que causó el rechazo — hoy para saber qué regla exacta rechazó hace falta consultar manualmente la plataforma Ardid. El equipo lo acordó como requerimiento de auditoría técnica; Gonzalo Rivera queda a cargo de cargar el pedido de mejora al sistema correspondiente (no es una tarea de Producto/PM, la carga él mismo).

---
*Ver también: [scoring.md](scoring.md) para el sistema de puntuación, [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md) para blacklist/whitelist y ráfagas de pagos, y [apis_externas.md](apis_externas.md) para las APIs `/Transaction`, `/ClientCard`, `/Loans` involucradas en este flujo.*
