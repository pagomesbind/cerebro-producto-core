# Ardid/Akurtech — Reportería y Alertas

> Estado: en producción.

> Fuente: `Akurtech 5 - Reportería - Alertas.pdf` (71 páginas), guía funcional oficial del proveedor. Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general.

## Índice de contenidos del módulo

1. Reportes Operativos (Clientes, Tarjetas, Custom, Comercio)
2. Reporte de Auditoría (usuarios, reglas, excepciones, blacklist/whitelist, rubros)
3. Alertas (Operativas y PLAFT)

---

## 1. Reportes Operativos

Se accede desde el menú de Akurtech, ícono "Reportes Operativos". Incluye reportes de gestión sobre pagos, transferencias, dispositivos y excepciones en las operaciones de los clientes: visión gráfica, detalle de dispositivos y actividad por cliente, estadísticas de uso de tarjeta, generación de **reportes custom**, y **reportes de comercio** (información de comercios, sucursales, grupos de comercio, rubros, pagos y excepciones).

### 1.1. Reporte de Clientes

Contiene información detallada de la actividad de los clientes: pagos, transferencias, dispositivos usados y excepciones. Permite identificar patrones de comportamiento y profundizar en detalles.

**Bloqueo del cliente**: columna "Bloqueado" (lado izquierdo del listado) con switch para activar/desactivar el bloqueo del cliente directamente desde el listado.

**Consulta cliente**: al presionar sobre un cliente se abre un panel derecho con detalle, organizado en solapas:

| Solapa | Campos / contenido |
|---|---|
| **General** | Nombre; Correo; Identificación; Tipo de cliente; Último ingreso; Último ID de TX; Haber mensual ($, editable); Perfil transaccional ($, editable); Transferencias — Entrantes/Salientes (montos acumulados diarios y mensuales); Pagos — Monto acumulado diario/mensual |
| **Cuentas** | Cuenta; Producto; Subproducto; Estado operativo (editable: Opera, No opera, No opera entrante, No opera saliente); Acciones |
| **Transferencias** | Fecha; Tipo; Ámbito; Moneda; Monto; Id de transacción; Estado; Nombre de restricción; Tiempo de Respuesta |
| **Excepciones de Transferencias** | Fecha; CBU Destino; Moneda; Monto; Excepción usada (Sí/No) |
| **Pagos** | Fecha; Moneda; Monto; ID tx Comercio; ID de Transferencia; Estado; Motivo |
| **Excepciones de Pagos** | Fecha; ID de Comercio; Moneda; Monto; Excepción usada (Sí/No) |
| **Login** | Fecha; IP; ID de Dispositivo; Ubicación; Estado |
| **Alertas** | Número de alerta; Fecha; Nombre; Estado |
| **Documentación** | Fecha de carga; Usuario; Nombre del Documento; Descripción; Vencimiento; iconos Descargar/Eliminar |
| **Relaciones** | Visualización gráfica (grafo) de las relaciones del cliente |

**Subir documento** (dentro de Documentación): botón "Subir Documento" → modal de carga. Switch "Vencimiento" habilita un campo de fecha; al cumplirse esa fecha el documento se elimina automáticamente.

**Buscador**: lupas de filtro sobre cada columna de la tabla. Botón "reestablecer valores de búsqueda". **Descarga CSV** del listado. **Carga masiva**: importar clientes vía CSV, con "Descargar ayuda de formato" y "Descargar ejemplo". **Configurar excepciones**: ícono en columna Acciones abre modal donde se selecciona el/los tipos de reglas de las que el cliente queda exceptuado.

### 1.2. Reporte de Tarjetas

Estadísticas y detalles del uso de cada tarjeta, para detectar actividad sospechosa y gestionar tarjetas conforme a políticas de la entidad.

**Acciones** (columna del listado): **Editar** (modal para editar DNI y fecha de vencimiento de la tarjeta) y **Cambiar estado** (modal para cambiar entre: Validado, Bloqueado, Inválido, Blacklist).

**Consulta de tarjetas**: panel derecho con solapas:

| Solapa | Campos |
|---|---|
| **Pagos** | Fecha; Moneda; Monto; ID de comercio; ID de TX; Estado; Motivo |
| **Comercio** | Fecha; ID de comercio; Cantidad de pagos diarios/mensuales; Monto acumulado diario/mensual; Total de pagos |
| **Alertas** | Número de alerta; Fecha; Nombre; Estado |

Buscador (lupas por columna + restablecer valores) y descarga CSV.

### 1.3. Reportes Custom

Suministran información de actividad en distintas áreas, en un período de tiempo solicitado. Configurable para generación periódica y envío automático por correo.

**Crear reporte — Paso 1**: botón "Crear nuevo reporte" abre un modal multi-paso. Paso 1: nombre del reporte + selección de áreas (la cantidad de pasos siguientes depende de las áreas elegidas). Luego se seleccionan campos de búsqueda para filtrar (disponibles según áreas elegidas).

**Combinaciones de áreas y campos de búsqueda disponibles:**

| Área(s) seleccionada(s) | Campos de búsqueda disponibles |
|---|---|
| **Transferencias** | Fecha; Ámbito; Cantidad; CBU destino; CBU origen; CUIT destino; CUIT origen; Dispositivo; Estado; Importe; IP; Marca; Moneda; Motivo de rechazo; Restricción; Tiempo de respuesta; Tipo |
| **Pagos** | Fecha; Año/Mes de vencimiento; BIN; Canal de pago; Comercio; Correo; Cuotas; Dispositivo; Estado; Grupo de bin; Grupo de comercio; HASH; ID del ente; Identificación; Importe; IP; Marca; Moneda; Motivo de rechazo; Restricción; Tiempo de respuesta; Tipo de pago; Tipo de tarjeta; Últimos 4 |
| **Login** | Fecha; Dispositivo; Estado; Identificación; IP; Tiempo de respuesta; Tipo de cliente; Ubicación |
| **Transferencias - Pagos** | Fecha; Dispositivo; Estado; Importe; IP; Marca; Moneda; Motivo de rechazo; Restricción; Tiempo de respuesta |
| **Transferencias - Login** | Fecha; Dispositivo; Estado; IP; Tiempo de respuesta |
| **Pagos - Login** | Fecha; Dispositivo; Estado; Identificación; IP; Tiempo de respuesta |
| **Transferencias - Pagos - Login** | Fecha; Dispositivo; Estado; IP; Tiempo de respuesta |

Nota: al combinar áreas, el set de campos de búsqueda disponibles es la **intersección** (los campos compartidos entre las áreas), no la unión.

**Comportamiento detallado de los campos de búsqueda más relevantes** (al agregarse con "+" se ubican debajo del buscador; se quitan con "−"):

| Campo | Comportamiento al agregarlo |
|---|---|
| Fecha | Select: Último día, Última semana, Último mes, Últimos 3/6 meses, Último año, Personalizado (habilita Desde/Hasta). Si se elige fecha relativa, se puede programar el envío periódico del reporte |
| Cantidad | **Comportamiento especial**: al seleccionarlo desaparecen los steps siguientes (áreas/campos quedan fijos) y no se pueden agregar más campos hasta eliminarlo. Muestra checkboxes Entrante y/o Saliente, input "Porcentaje superior al promedio mensual diario", select de estado de transferencias, y el campo Fecha queda bloqueado en "Último día" |
| Importe / Tiempo de respuesta / BIN | Dos inputs: Desde / Hasta |
| Estado | Opciones dependen de las áreas elegidas (ver tabla siguiente) |

**Campo Estado — opciones según combinación de áreas:**

| Áreas seleccionadas | Estados disponibles |
|---|---|
| Transferencias + Pagos + Login | Aprobado ✓, Aprobado X, Rechazado |
| Transferencias + Pagos | Aprobado ✓, Aprobado X, Rechazado |
| Transferencias + Login | Aprobado ✓, Aprobado X, Rechazado |
| Pagos + Login | Aprobado ✓, Aprobado X, Rechazado |
| Solo Transferencias | Aprobado ✓, Aprobado X, No realizado ✓, No realizado X, Rechazado |
| Solo Pagos | Aprobado ✓, Aprobado X, Rechazado, Devolución, Devolución parcial, Pendiente |
| Solo Login | Aprobado ✓, Aprobado X, Rechazado, Fallido |

> Nota de correlación: esta tabla confirma que el estado **"Pendiente"** de pagos **sí existe** en el producto (a nivel de reportes custom), aunque la guía de Pagos ([modulo_pagos.md](modulo_pagos.md#1-vista-general-de-la-pestaña-pagos)) no lo mencionaba explícitamente en su listado principal — resuelve parcialmente esa duda de fidelidad entre guías.

**Campos de transferencia / pagos / login** (steps específicos, al menos un campo obligatorio si se eligió esa área):
- Transferencias: Ámbito; CBU destino/origen; CUIT destino/origen; Dispositivo; Estado; Fecha; ID de transferencia; Importe; IP; Marca; Moneda; Motivo de rechazo; Restricción; Tiempo de respuesta; Tipo.
- Pagos: Año/Mes de vencimiento; BIN; Canal de pago; Código de entidad/tarjeta; Comercio; Correo; Cuotas; Dispositivo; DNI; Estado; Fecha; Grupo de bin/comercio; HASH; ID de transacción/ente/tx de comercio; Importe; IP; Marca; Moneda; Motivo de rechazo; Nombre de restricción/y apellido; Tiempo de respuesta; Tipo de pago/tarjeta; Últimos 4.
- Login: Estado; Fecha; ID de dispositivo; Identificación; IP; Nombre y apellido; Tiempo de respuesta; Tipo de cliente; Ubicación.

**Consulta**: al seleccionar un reporte custom en la tabla izquierda se muestra el detalle a la derecha (nombre, fecha de creación, usuario creador), con botones "Ver resultado" (tablas de las áreas seleccionadas) y descarga del reporte completo.

**Configuración de envío de reporte**: disponible solo si el reporte fue creado con fecha relativa. Modal con: Hora de envío, Fecha de envío (primer envío), Frecuencia en día (cada cuántos días se regenera y reenvía), Correo de destino (uno o más, separados por coma). Al aceptar, la aplicación envía automáticamente el reporte a los correos configurados en cada fecha/hora que corresponda.

### 1.4. Reportes de Comercio

Información variada de los comercios registrados, útil para identificar patrones e irregularidades.

**Tabla de comercios**: Fecha de creación; Razón social; CUIT/CUIL; Bloqueado (switch); Acciones.

**Agregar comercio**: modal con Razón social (obligatorio), CUIT/CUIL, switch "Exceptuar control de reglas estándar de comercio", Grupos de comercio (asignación de uno o más — con opción de crear grupos nuevos directamente: Nombre + Código), y tabla de Cuentas asignadas (agregar/editar/eliminar con confirmación).

**Consulta general** (solapa "General" del comercio): Razón social, CUIT/CUIL, Fecha de justificación de última actualización de volumen de facturación, Exceptuar control de regla estándar, Perfil transaccional, y **domicilio fiscal completo** (País, Provincia, Localidad/barrio, Calle, Altura, Código postal — campos que se habilitan progresivamente uno a uno). Razón social, CUIT/CUIL y Perfil transaccional editables inline.

**Sucursales** (solapa): Nombre, Código, domicilio completo, Acciones (agregar/editar/eliminar).

**Grupos de comercio / Rubros** (solapas): select desplegable con checkbox (selección múltiple), botón Guardar, eliminación individual.

**Blacklist/Whitelist IP** (solapa, específica del comercio): tabla IP, Fecha de ingreso, Blacklist/whitelist, Motivo, Acciones. Permite agregar (radiobuttons Blacklist/Whitelist + Motivo), eliminar, y **convertir** una IP entre listas (requiere seleccionar un motivo).

**Pagos / Excepciones / Cuentas / Documentación / Alertas** (solapas): mismo patrón de tablas que en Reporte de Clientes.

## 2. Reporte de Auditoría

Información detallada sobre la gestión de seguridad de la plataforma: registra todas las actividades del sistema (quién las ejecutó y cuándo). Permite seguimiento, filtrado, orden y exportación.

En la pantalla principal hay **5 cards con gráficos tipo dona** que informan el porcentaje de actividades realizadas, correspondientes a las 5 subsecciones siguientes.

### 2.1. Reporte de gestión de usuarios
Visión de los usuarios modificados en el sistema y sus perfiles (permisos). Tabla: Fecha; Usuario ejecutor; Usuario gestionado; Nombre y apellido; Habilitar (switch); Acción (Eliminado/Actualizado/Creado). Consulta: detalle completo con dominio y perfil del usuario gestionado.

### 2.2. Reporte de Reglas
Visión de las reglas modificadas en el sistema. Tabla: Fecha; Usuario Ejecutor; Tipo de regla; Nombre de regla; Acción (creó/eliminó/actualizó). Si la acción fue "Actualización", se muestran solapas **"Era"** (estado anterior) y **"Es"** (estado posterior); botón "Ver más" abre modal comparando ambos estados simultáneamente.

### 2.3. Reporte de Excepciones
Visión de las excepciones utilizadas en transferencias/pagos. Contexto funcional: si una transacción se bloquea/rechaza y luego se verifica como legítima, un operador puede marcar la transferencia como confiable y crear una excepción temporal (con duración configurable) para evitar bloqueos automáticos adicionales a corto plazo. **Estas excepciones retroalimentan el algoritmo de IA para reducir falsos positivos (errores tipo I) y optimizar reglas.**

Tabla: Fecha; Nombre de cliente; Ámbito; Importe; Tiempo (duración asignada a la excepción). Consulta: detalle con CUIT/CBU origen y destino, usuario ejecutor.

### 2.4. Reporte de Blacklist/Whitelist
Visión de los registros de Blacklist y Whitelist aplicados en el sistema. Tabla: Fecha; Usuario ejecutor; Tipo (Blacklist/Whitelist); Categoría (IP, tarjeta, identificación, CBU/alias, etc.); Acción (creación/eliminación). Consulta: incluye Motivo (ej. alta automática, decisión manual del operador) y Valor (el dato bloqueado/autorizado).

### 2.5. Reporte de Rubros
Visión de las modificaciones a los rubros del sistema. Tabla: Fecha; Usuario ejecutor; Rubro; Acción (se considera "Creación" la primera vez que se ingresa un valor en un rubro). Consulta: Ticket promedio anual, Devolución promedio anual — con solapas Era/Es si la acción fue "Actualización" (ver [modulo_pagos.md](modulo_pagos.md) para cómo estos campos afectan reglas por comercio).

## 3. Alertas

Acceso desde el Menú, opción "Alertas". Dos cards: **Alertas Operativas** y **Alertas PLAFT** (Prevención de Lavado de Activos y Financiamiento del Terrorismo). Al ingresar a cualquiera se puede: visualizar, tratar, adjuntar información y/o solicitarla, y justificar cada alerta generada automáticamente.

### Generación de alertas

Cada regla configurada puede generar una alerta al cumplirse su condición. Las alertas se clasifican y gestionan desde esta pantalla, y pueden enviarse a casillas de correo y canales de Telegram (ver [configuracion_inicial.md](configuracion_inicial.md#4-parametrías-de-entidad), sección "Configuración de notificaciones").

**Tipos de alertas (origen/regla que las genera):** Reglas estándares, Reglas de machine learning, Reglas reputacionales, Ráfagas, Reglas comportamentales, Habilitación temporal de transferencias.

**Respuesta configurable por alerta**: puede incluir Solicitud de 2FA, Rechazo de la transacción, Bloqueo de la cuenta del cliente — combinables entre sí (ver el detalle completo de estos umbrales en [scoring.md](scoring.md)).

**Parametría — Tiempo de depuración de alertas**: desde Parametrías de la Entidad se configura el "Tiempo de depuración de alertas" (en días). Al cumplirse ese plazo, todas las Alertas se borran de la base de datos y dejan de existir — no podrán ser filtradas por ningún filtro de la pantalla de Alertas Operativas.

### 3.1. Tablero de Alertas

Diagrama de arco con la cantidad de alertas de la última hora + Total (se limpian los datos al cambiar de hora). **Top 5**: las 5 restricciones que generaron más alertas durante el mes.

### 3.2. Buscador
Filtros por: Fecha, Nombre de la restricción, Estado.

### 3.3. Filtro "Seleccionar Alerta"
Determina qué alertas muestran el tablero y el listado, según la restricción de origen: Todos, Reglas Estándar, Ráfagas, Reglas Reputacionales, Reglas de Machine Learning, Reglas Comportamentales, Autorización temporal de transferencias.

### 3.4. Descargar adjunto
Botón "Descargar Adjunto" descarga un archivo .csv con las Alertas activas.

### 3.5. Filtros Avanzados
Modal con: Tipo y Ámbito de la alerta, Monto (Desde/Hasta), CBU (Origen/Destino), CUIT (Origen/Destino).

### 3.6. Listado de Alertas
Recuadro inferior izquierdo con las alertas activadas en la última hora. Columnas: Fecha y hora, Nombre Restricción, Estado (**Tratar, Justificar, Info, En proceso**). Al seleccionar una alerta se abre el panel de "Consulta de alertas operativas".

### 3.7-3.9. Acciones sobre una alerta

| Acción | Cuándo se usa | ¿Es final? | Flujo |
|---|---|---|---|
| **Tratar** | La alerta **no fue bien generada** (falso positivo) | Sí — no admite edición ni revisiones posteriores | Comentario obligatorio + adjunto opcional → botón "Tratar" → pasa a Historial de acciones realizadas |
| **Justificar** | La alerta **está bien generada**, se explica el motivo | Sí — no se puede volver a actuar sobre esa alerta | Comentario + adjunto **.pdf** obligatorio → botón "Justificar" → pasa a Historial |
| **Solicitar** | La alerta está en análisis y falta información | No — se puede pedir información las veces que sea necesario antes de justificar o tratar | Comentario + adjunto **.pdf** → botón "Solicitar" → la alerta sigue activa, queda en Estado "Info" |

### Resumen de Estados de una Alerta

| Estado | Significado | ¿Es final? |
|---|---|---|
| En Proceso | Sin ninguna acción tomada aún | No |
| Info | Se solicitó información adicional | No (admite nuevas acciones) |
| Tratar | Alerta marcada como mal generada (falso positivo) y tratada | Sí, final |
| Justificar | Alerta confirmada como bien generada y justificada | Sí, final |

---

## Notas de cobertura de la fuente

- No se encontró una sección separada y explícita llamada "Dashboard de Monitoreo" con cards personalizables por el usuario dentro de esta guía específica — esa funcionalidad de dashboards personalizados **sí está documentada** en [configuracion_inicial.md](configuracion_inicial.md#7-dashboard-de-monitoreo-dashboards-personalizados), a partir de la guía "Akurtech 1 - Parámetros iniciales".
- Los "4 tipos de Estados existentes" mencionados en el buscador de Alertas (§3.2) coinciden con los 4 estados documentados en §3.6-3.9 (Tratar, Justificar, Info, En proceso).
- No se encontró en el texto una lista de formatos de exportación más allá de CSV (reportes operativos, de auditoría y comercio) y CSV/adjunto para Alertas — no se menciona exportación en PDF, Excel u otros formatos.

---
*Ver también: [modulo_transferencias.md](modulo_transferencias.md), [modulo_pagos.md](modulo_pagos.md), [modulo_login.md](modulo_login.md) para las reglas que generan las alertas y excepciones documentadas acá, y [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md) para el detalle de blacklist/whitelist referenciado en el Reporte de Auditoría.*
