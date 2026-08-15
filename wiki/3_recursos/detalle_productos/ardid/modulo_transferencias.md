# Ardid/Akurtech — Módulo de Transferencias

> Estado: en producción.

> Fuente: `Akurtech 2 - Transferencias.pdf` (120 páginas), guía funcional oficial del proveedor. Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general.

## 1. Dashboard de Transferencias — Cards principales

Al ingresar al Dashboard de Akurtech, la pestaña Transferencias muestra tres cards con resumen gráfico y accesos:

| Card | Contenido |
|---|---|
| **Transferencias** | Gráfico dona: Entrante / Saliente (con %). Estado de Transferencias: Aprobadas, Aprobadas con errores, No realizadas, No realizadas con errores, Rechazadas. |
| **Reglas de Transferencias** | Gráfico dona con desglose de reglas activas por tipo: Comportamentales, Machine Learning, Reputacionales, IA, Estándar (ejemplo dado: Estándar 60.53%). Acceso a pantalla de gestión de reglas. |
| **Simulación de Transferencias** | Gráfico circular con resultados de simulaciones: Simulación de Reglas Estándar, Simulación de Reglas Reputacionales, Simulación de Reglas de Machine Learning. |

Cada card tiene una flecha de acceso (arriba a la derecha) que redirige a la pantalla completa correspondiente.

## 2. Pantalla Transferencias (listado y analítica)

Pantalla central para revisar transferencias individual y conjuntamente. Incluye un recuadro desplegable con gráficos analíticos (varias pestañas), el listado de transferencias por entidad (con selección de campos), y un footer con totales diarios/mensuales.

### 2.1 Pestaña "Ámbito y Tipo"
- Gráfico circular (dona) que clasifica las transferencias de la última hora (o del rango de fecha/hora filtrado) por **Tipo** y **Ámbito**.
- **Actualización continua**: los gráficos y listas se limpian cada hora para reflejar datos recientes.
- **Filtros**: rango de fecha y hora.

### 2.2 Pestaña "Respuestas"
Gráficos 2D y 3D. Casilleros de "Acciones" seleccionables (uno o varios simultáneamente):

| Casillero | Descripción |
|---|---|
| Bloqueo de Cuenta | Transferencias que resultaron en bloqueo de cuenta |
| Rechazo | Transferencias rechazadas |
| 2FA | Transferencias aprobadas que requirieron doble factor |
| Aprobado | Transferencias aprobadas sin requisitos adicionales |

**Gráfico 2D**: estadístico, ejes Cantidad (X) y Hora (Y). Colores: Bloqueo de Cuenta (rojo), Rechazo (amarillo), 2FA (verde), Aprobadas (naranja). Funciones: tooltip, zoom, descarga en .png.

**Gráfico 3D**: dispersión, interacción con mouse (mover/rotar), métricas Días/Horas/Cantidad, botón de descarga .png.

**Cálculo de promedios en Gráfico 3D**: el sistema usa cortes horarios de 4 horas fijos: 00:00–03:59, 04:00–07:59, 08:00–11:59, 12:00–15:59, 16:00–19:59, 20:00–23:59. El promedio de cada corte = suma de transferencias por hora dentro del corte ÷ 4. Ejemplo dado en la fuente: corte 08:00-11:59 con 8 aprobadas repartidas en 0+3+5+0 → promedio = 2.

Tooltip del punto muestra: Promedio por día, Promedio por hora, Promedio a la Cantidad.

**"Promedio de Promedios"**: el sistema puede promediar los promedios obtenidos entre distintos cortes horarios, o entre distintas fechas. Ejemplos numéricos en la fuente: (1+2+3)/3=2 entre cortes; (2+3+4)/3=3 entre fechas.

### 2.3 Pestaña "Reglas"
Gráfico de barras con las **Reglas Estándar** activadas por las transferencias, mostrando cantidad de transferencias afectadas por cada regla y su nombre.

### 2.4 Pestaña "Aciertos"
Gráfico dona + líneas porcentuales con: Aprobada Confiable, Aprobada Fraude (Error Tipo 2), Rechazada Confiable (Error Tipo 1), Rechazada Fraude. Incluye dos recuadros: **Nivel de Significancia** y **Nivel de Potencia** (verde/rojo), cuyos valores se configuran previamente en Parametrías de Entidad, y se usan para comparar las dos líneas porcentuales.

### 2.5 Recuadro derecho
Escala numérica y porcentual de: Aprobadas, Aprobado X, Rechazadas, No realizada, No realizada X.

## 3. Listado de Transferencias

- Muestra transferencias de la última hora; se limpia cada hora para mostrar la siguiente. Permite ver transferencias antiguas filtrando por fecha/hora.
- **Buscador y Propiedades**: botón "Buscador" activa lupas de búsqueda sobre cada propiedad. Se pueden encadenar varios filtros (lógica AND: debe cumplir todos).
- Dato operativo: con el filtro de fecha y el switch "Hasta" desactivado, el listado se autoactualiza cada 30 segundos (se puede detener encendiendo el switch); durante la actualización algunos datos pueden demorar en llegar.
- **Campos a visualizar**: botón que despliega un select para habilitar propiedades adicionales en las columnas (tildar casillero + botón Guardar). Si se habilitan muchas, aparece scroll horizontal.
- **Resetear valores de búsqueda**: limpia los filtros aplicados.
- **Descargar .csv**: descarga las transferencias de la última hora, o solo las filtradas si hay filtros activos.

### 3.1 Columna Acciones: Marcar (Fraudulenta / Confiable)
- La columna "Acciones" tiene 3 botones: dos para "Ver Resultados" y uno para "Marcar".
- Marcar permite asentar una transferencia como **Fraudulenta** o **Confiable**, eligiendo opciones de una lista (que ayudan al entendimiento del motivo), pasándolas a la columna correspondiente (Columna NO / Columna SI) mediante una flecha, más un campo de comentario libre. Se confirma con botón "Aceptar".
- Aplica a transferencias internas y externas (salientes).
- **Caso especial — Excepción**: solo cuando una transferencia "Saliente" está en estado "Rechazado" se puede marcar como "Confiable" y habilitarla temporalmente (y viceversa, si está "Confiable" se puede marcar como fraude). Esto permite al usuario reintentar una transferencia sin que la restrinja la regla que la había rechazado. **Se conoce como "excepción"**: aplica solo durante el tiempo configurado en la habilitación, es válida para una sola transferencia y por parte de ese usuario específico.
- La marca queda visible en el listado (requiere habilitar la Propiedad "Marca"). El botón "Marca" cambia a "Descripción" una vez marcada, permitiendo ver el detalle y seguir agregando comentarios.
- Se pueden marcar transferencias del día en curso o antiguas (estas últimas requieren filtrar por fecha/hora primero).

### 3.2 Footer del listado
- **Tiempo de respuesta del día** (ms): Promedio y rango más alto.
- **Transferencias monitoreadas en el día**: Total, desglosado en Internas, Externas, Debin.
- **Transferencias monitoreadas en el mes**: mismo desglose (Internas, Externas, Debin).
- Nota: este conteo NO incluye transferencias Rechazadas ni Bloqueadas.

## 4. Carga masiva de Transferencias

Permite importar datos vía archivo CSV para insertar múltiples registros sin carga manual uno por uno.

- Modal con opción **"Descargar ayuda de formato"**: CSV con instrucciones para armar el archivo correctamente.
- Opción **"Descargar ejemplo"**: CSV de ejemplo con el formato esperado.
- Tras subir el archivo con formato correcto y presionar Aceptar: confirmación de carga masiva exitosa.
- Opción para elegir **cuándo corre el servicio** (día y hora).
- Switch **"Ofuscar datos"**: reemplaza datos sensibles del cliente para proteger la privacidad.

## 5. Reglas de Transferencias — Tipos

Desde el Dashboard > Transferencias > card "Reglas de Transferencias" > botón Acceder, se listan **cinco cards** para parametrizar tipos de reglas: **Estándar**, **IA**, **Reputacionales**, **Machine Learning**, **Comportamentales**.

### 5.1 Reglas Estándar

**Definición**: configuración que monitorea transferencias para identificar actividad sospechosa, evaluada de forma "atómica" (individual). Se define por ámbito (entrante/saliente), scope (Interna/Externa/Debin) y otras características (moneda, perfil del cliente, día/horario, tipo de destinatario). Se activan/desactivan en tiempo real sin modificar código ni reiniciar el sistema. Pueden simularse antes de producción.

**Ejemplos de reglas atómicas mencionados en la fuente**:
- Recepción de dinero seguida de un envío inmediato
- Cambios de dispositivo antes de la recepción de fondos
- Velocidad entre varias recepciones de dinero en un corto período
- Envío de fondos a un nuevo destinatario no registrado previamente
- Transferencias de grandes sumas en horarios inusuales para el cliente
- Envíos múltiples a diferentes destinatarios en un corto período de tiempo

**Restricción Entrante vs. Restricción Saliente**:

| Aspecto | Entrante | Saliente |
|---|---|---|
| Foco | Fondos que ingresan a la cuenta del cliente | Fondos que salen de la cuenta hacia otros destinatarios |
| Detecta | Montos elevados, frecuencia de recepción, procedencia de fondos | Monto máximo permitido, frecuencia de envíos a nuevos destinatarios, cambio de dispositivo previo a envío |
| Acciones disponibles | Solo "Bloqueo de cuenta" | Bloqueo de cuenta, Rechazo de transacción, Solicitar 2FA (las 3) |

#### 5.1.1 Pantalla de gestión — Lista de Reglas (columnas de la tabla)

| Columna | Descripción |
|---|---|
| Nombre | Nombre asignado a la regla |
| Fecha | Fecha y hora de creación/modificación |
| Moneda | ARS, USD, EUR, etc. |
| Monto mínimo | Límite monetario |
| Monto máximo | Límite monetario |
| Habilitada | Switch on/off (color = activa, gris = inactiva) |
| Acciones | Editar (lápiz), eliminar (basura), otros ajustes |

Botones de acción rápida: Restablecer valores de búsqueda, Activar Todas, Desactivar Todas, Crear Nueva.

#### 5.1.2 Modal "Crear Regla" — Campos

| Campo | Detalle |
|---|---|
| Nombre de la restricción | — |
| Modo de creación de cuenta | *(el texto fuente no detalla las opciones/valores posibles de este campo — ver gap en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md))* |
| Ámbito | Interna, Externa, Debin (u otros parametrizados por la entidad). Selección múltiple posible. |
| Tipo de Persona | Persona Física, Persona Jurídica (segmentación configurable por entidad vía ABM) |
| Tipo de Banca | Banca Personal, Banca Empresa (ABM configurable) |
| Tipo de Cliente | Ej.: jubilados, asalariados, autónomos (ABM configurable) |
| Tipo de Producto | Ej.: cuenta corriente, cuenta nómina (ABM configurable) |
| Tipo de Subproducto | Ej.: cuenta corriente en USD, en EUR (ABM configurable) |
| Moneda | USD, ARS, EUR (ampliable vía ABM de monedas en Parametrías Generales) |
| Monto mínimo | Umbral inferior de aplicación de la regla |
| Monto máximo | Umbral superior de aplicación de la regla |
| Aplicar día de la semana | Selección de uno, varios o todos los días |
| Vigencia de Horario | Switch "Vigencia 24hs" (default ON); si se desactiva, se habilitan campos Desde/Hasta |
| Vigencia de Día | Fecha Desde obligatoria (no puede ser menor a la actual); Fecha Hasta opcional (requiere switch habilitado) |
| Destinatario | Mismo al originante / Distinto al originante / Indistinto |
| Acciones | Ver tabla siguiente |
| Alerta | Switch on/off; tipos: Alerta Operativa, Alerta PLAFT |
| Acciones anteriores | Ver sección 6 |

**Ámbito — detalle**:
- **Interno**: transacciones que se originan y completan dentro de la misma entidad/sistema.
- **Externo**: transacciones entrantes que provienen de fuera de la entidad/sistema.
- **Debin (débito inmediato)**: transacciones con orden de débito en tiempo real, autorizada por el cliente.

**Acciones (qué hace la regla al activarse)**:

| Acción | Efecto | Disponible en |
|---|---|---|
| Bloqueo de cuenta | La transferencia no se ejecuta; recomienda a la entidad bloquear transferencias entrantes y salientes de esa cuenta vía respuesta API | Entrantes y Salientes |
| Rechazo de transacción | Impide la ejecución de la transferencia, sin afectar la cuenta completa | Solo Salientes |
| Solicitar 2FA | Doble autenticación antes de permitir la transferencia | Solo Salientes |

**Nota**: las reglas estándar entrantes solo tienen la acción "Bloqueo de cuenta"; las salientes tienen las 3 acciones.

**Destinatario — detalle**: Mismo al originante (cuentas propias del cliente) / Distinto al originante (cuentas de otros clientes) / Indistinto (no considera origen ni destino).

### 5.2 Reglas IA (Entrantes y Salientes)

Reglas de aprendizaje de comportamiento habitual del usuario mediante IA. Al habilitar cada regla, del lado derecho se abre su configuración específica. A medida que se cargan Reglas IA se habilitan las opciones de parametría de Reglas Machine Learning (dependencia directa: **si una regla IA no está activa, no se puede activar su correspondiente regla ML**).

| Regla IA | Parámetros de configuración |
|---|---|
| **Destinatario habitual** | Cantidad mínima de transferencias hacia un destinatario + rango de tiempo (días). El sistema aprende los destinatarios habituales por frecuencia. |
| **Día y Horario habitual** | Fuente de datos: (a) Información de Transferencias (histórico interno, aprendizaje automático) o (b) Información Externa (API `ChangeUsualSchedule`, carga manual — ver [apis_externas.md](apis_externas.md#12h-changeusualschedule-post)). Advertencia: seleccionar la fuente externa borra irreversiblemente todos los datos internos de habitualidad. Si se usa fuente interna: cantidad de transferencias sobre rango de tiempo en días. |
| **Dispositivo habitual** | Cantidad mínima de transferencias desde un dispositivo específico + rango de tiempo (días). |
| **IP habitual** | Cantidad de transferencias + rango de tiempo (días). |
| **Geolocalización habitual** | Tipo de geolocalización: País, Región, Ciudad o Código Postal. Cantidad mínima de conexiones para considerar habitual (ej. 5). Tiempo mínimo en horas desde la última conexión desde esa ubicación. Rango de tolerancia (%) sobre ese tiempo mínimo (0% = sin tolerancia; ej. 60% = a mitad del tiempo estipulado ya se guarda como habitual). |
| **Monto habitual** | Modal "Agregar Nuevo": Tipo de Banca, Tipo de Cliente (autocompletado), Tipo de Producto (autocompletado), Tipo de Subproducto (autocompletado), Tipo de moneda (autocompletado), Cantidad (monto), Rango, cantidad de Tiempo (días). |
| **Montos acumulados habituales** | Configurable por período Diario o Mensual, con soporte de ciclos específicos dentro del período (ej. del 1 al 15, del 16 al 20). Modal: Tipo de Persona, Tipo de Banca, Tipo de Cliente (auto), Tipo de Producto (auto), Tipo de Subproducto (auto), Moneda (auto), checkbox Días/Meses, cantidad numérica de tiempo, Monto, Fecha y Hora de activación de la regla. |

**Flujo de modificaciones pendientes (común a todas las Reglas IA)**: al guardar una configuración de Regla IA se generan "modificaciones pendientes" que requieren aprobación por un usuario con permisos suficientes. Se aprueban vía botón "Consulta"/"Aprobar" (individual) o "Aprobar todo" (masivo); se descartan vía botón "Rechazar" (individual) o "Rechazar todo" (masivo, mencionado para Geolocalización habitual).

Cada regla de Monto habitual / Montos acumulados habituales creada aparece en un listado con acciones de edición y eliminación (con modal de confirmación).

### 5.3 Reglas Reputacionales

Sistema de scoring: suman o restan puntos a la reputación de una cuenta/cliente. **Mayor reputación = peor** (más riesgo); menor reputación = mejor. Cada regla varía entre **1 y 1000 puntos**. Reglas Negativas → signo "+"; Reglas Positivas → signo "-". Se alimentan de datos cargados en Blacklist/Whitelist (ver [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md)).

#### 5.3.1 Acciones (umbrales de score)

| Acción | Condición de score | Nivel de riesgo | Alerta |
|---|---|---|---|
| Aprobar transferencia | Score ≤ máximo permitido | Riesgo Aceptado | Opcional |
| Solicitar Challenge (2FA) | Score ≥ mínimo | Riesgo Bajo | Opcional |
| Rechazar transferencia | Score ≥ mínimo | Riesgo Medio | Opcional |
| Bloqueo de Cliente | Score ≥ mínimo | Riesgo Alto | Opcional |

Las alertas activadas se reflejan en la pantalla de Alertas Operativas.

#### 5.3.2 Listado de reglas reputacionales — Tipo y origen del dato

| Regla | Tipo | Fuente |
|---|---|---|
| IP sospechosa | Negativa | Blacklist IP |
| IP conocida | Positiva | Whitelist IP |
| Destinatario sospechoso | Negativa | Blacklist Cuenta |
| Destinatario conocido | Positiva | Whitelist Cuenta |
| Dispositivo sospechoso | Negativa | Blacklist Dispositivo |
| Dispositivo conocido | Positiva | Whitelist Dispositivo |
| Geolocalización sospechosa | Negativa | Blacklist Geolocalización |
| Geolocalización conocida | Positiva | Whitelist Geolocalización |
| E-mail sospechoso | Negativa | Blacklist E-mail |
| E-mail conocido | Positiva | Whitelist E-mail |
| Dominio E-mail sospechoso | Negativa | Blacklist Dominio E-mail |
| Dominio E-mail conocido | Positiva | Whitelist Dominio E-mail |
| Identificación sospechosa | Negativa | Blacklist Identificación |
| Identificación válida | Positiva | Whitelist Identificación |

**Agregar Regla**: modal donde se selecciona un ítem del listado de control (arriba); el sistema indica si es puntuación negativa o positiva; se ingresa el score y "Aceptar". Genera modificaciones pendientes.

**Vista Previa de Reglas Habilitadas**: recuadro superior derecho lista todas las reglas creadas con sumatoria total de Puntuación Negativa y Positiva. Recuadro superior izquierdo lista el detalle de cada regla (tipo, puntuación, acción de eliminación).

**Eliminar / Actualizar**: ambas acciones generan modificaciones pendientes sujetas a aprobación con permisos.

### 5.4 Reglas Machine Learning

Desglosa riesgos potenciales de transferencias mediante modelos de aprendizaje automático de la habitualidad del usuario. **Son del tipo reputacional** (misma lógica de scoring que las Reputacionales) y **dependen de las Reglas IA**: si una regla IA no está activa, la correspondiente regla ML tampoco puede activarse.

#### 5.4.1 Catálogo de reglas ML (vinculación con Regla IA)

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
| Dispositivo no habitual | Negativa | Dispositivo |
| Dispositivo habitual | Positiva | Dispositivo |
| IP no habitual | Negativa | IP |
| IP habitual | Positiva | IP |
| Monto no habitual | Negativa | Monto |
| Monto habitual | Positiva | Monto |

Cada regla puede activarse o no. El resultado final del score reputacional se contrarresta con el resultado de otros tipos de reglas; **el sistema aplica la acción más restrictiva**.

**Acciones (mismos 4 umbrales que Reputacionales)**: Aprobar / Solicitar Challenge / Rechazar / Bloqueo de Cliente, cada una con Riesgo Aceptado/Bajo/Medio/Alto y Alerta opcional. Estas acciones impactan en la pantalla de Transferencias, filtrables por "Motivo de Rechazo".

**Agregar Regla**: modal con select de opciones sujeto a las reglas activadas en Reglas IA (si IA no está configurada, el select aparece vacío/deshabilitado). Se marca automáticamente Positiva/Negativa según sea "habitual"/"no habitual", se ingresa un valor de puntuación, y "Aceptar" (genera modificaciones pendientes). Rango de puntuación: **0 a 1000**; Negativas signo "+", Positivas signo "-".

**Vista previa de reglas habilitadas**: igual mecánica que Reputacionales (sumatoria de puntuación negativa/positiva).

**Eliminar / Actualizar Cambios**: generan modificaciones pendientes.

### 5.5 Reglas Comportamentales

Analizan la conducta del usuario dentro de la **aplicación móvil** de la entidad. Se activan por entidad. **Prerrequisito**: la entidad debe tener al menos una Aplicación creada y parametrizada con más de una Acción Comportamental (ambas se configuran desde Parametrías de entidad — ver [configuracion_inicial.md](configuracion_inicial.md#4-parametrías-de-entidad)).

#### 5.5.1 Acciones (mismos 4 umbrales que Reputacionales/ML)
Aprobar transferencia / Solicitar Challenge / Rechazar transferencia / Bloqueo de Cliente — con los mismos niveles de riesgo (Aceptado/Bajo/Medio/Alto) y Alerta opcional. Impactan en pantalla de Transferencias, filtrable por Motivo de Rechazo.

#### 5.5.2 Crear Nueva Regla Comportamental — Campos

- Nombre de la Regla
- Tipo: **Acción vs Acción** o **Acción**

**Si es tipo "Acción vs Acción"**:

| Campo | Descripción |
|---|---|
| Aplicación | Seleccionar una previamente creada |
| Acción vs Acción | Seleccionar una Acción vs. otra Acción, ambas previamente creadas |
| Rango de tolerancia de acciones (%) | Margen aceptable de variación en cantidad de acciones respecto al promedio histórico. Ej.: 20% de tolerancia sobre un promedio de 10 transferencias/día = rango aceptable 8-12. |
| Desvío del cálculo de promedio (%) | Cuánto se desvía el comportamiento actual del promedio histórico. Ej.: desvío configurado en 90% → si se supera, se considera sospechoso y se aplican las reglas definidas (2FA, rechazo, etc.) |
| Rango de tolerancia de tiempo (%) | Margen de tiempo aceptable entre dos acciones del usuario (ms). Ej.: usuario normalmente tarda 1000-2000ms entre "Login" y "Transferir"; si de repente tarda 100ms, es sospechoso. |
| Desvío del cálculo de promedio (tiempo, %) | Desvío del tiempo real entre acciones respecto al tiempo promedio histórico (ms). Ej.: promedio 1000ms, ejecución real 1200ms → desvío 20%. |

**Si es tipo "Acción"**:

| Campo | Descripción |
|---|---|
| Aplicación | Seleccionar una previamente creada |
| Acción | Seleccionar una previamente creada |
| Checkboxes de ajuste | Superficie / Tiempo de touch / Posición (cada uno despliega su propia parametría) |

Cada uno de los tres checkboxes (Superficie, Tiempo de touch, Posición) tiene el mismo set de campos: Rango de tolerancia de acciones (%), Desvío del cálculo de promedio (%), Promedio Histórico (informativo), Desvío (informativo), switch de activación de Alerta.

**Campos finales comunes** (ambos tipos de regla): Valor de Puntuación Negativa y Positiva (rango 0 a 1000; Negativas signo "+", Positivas signo "-"), Tiempo de vida en segundos para las acciones de la regla.

Al presionar "Aceptar" se generan modificaciones pendientes (Aprobar/Rechazar por usuario con permisos).

**Vista previa / Editar / Eliminar**: mismo patrón que las demás familias de reglas (listado con nombre, Aplicación, acciones, Valor; iconos de edición y eliminación; modal de confirmación para eliminar).

La acción final ante una transferencia sospechosa se contrarresta con el resultado de los demás tipos de reglas parametrizadas: **el sistema aplica la acción más restrictiva activada**.

## 6. Acciones Anteriores (variables de comportamiento usadas en Reglas Estándar)

"Acciones Anteriores" son criterios/condiciones previas (historial) que deben cumplirse antes de que se active una regla estándar. Difieren según el ámbito:
- **Entrantes**: analizan historial de ingresos de fondos (detectar anomalías en depósitos).
- **Salientes**: analizan condiciones de envíos de dinero (evitar transferencias no autorizadas).

| Acción Anterior | Ámbito | Campos de configuración |
|---|---|---|
| **NINGUNO** | Ambos | Sin parámetros; el sistema pasa directo a la configuración de Acciones |
| **Antigüedad de la cuenta** | Ambos | Número de días (antigüedad mínima o máxima de la cuenta) |
| **Envío** | Solo Entrantes | Cantidad de envíos en el día (mínimo); Tiempo desde el último envío (segundos) — detecta ráfagas |
| **Recepción** | Solo Salientes | Monto anterior (mínimo recibido); Tiempo anterior de la recepción (segundos) |
| **Cambio de Email** | Ambos | Tiempo desde el último cambio de email (minutos) |
| **Cambio de Dispositivo** | Ambos | Tiempo desde el último cambio de dispositivo (minutos) |
| **Login Fallido** | Ambos | Cantidad de login fallidos al último inicio de sesión (umbral) |
| **Monto Acumulado Diario** | Ambos (Entrantes o Salientes) | Monto acumulado por día (máximo permitido) |
| **Monto Acumulado Mensual** | Ambos | Monto acumulado por mes (máximo permitido) |
| **Porcentaje Perfil Transaccional a Recibir Diario (%)** | Ambos | Porcentaje del perfil transaccional diario; opción "Moneda específica (ARS)" habilita controles adicionales |
| **Porcentaje Perfil Transaccional Mensual (%)** | Ambos | Porcentaje del perfil transaccional mensual |
| **Cantidad de Envíos luego de Acreditación de Préstamos** | — | Cantidad máxima de envíos permitidos tras recibir un préstamo |
| **Recibida por Día / Enviado por Día** | Ambos | Cantidad máxima de transferencias recibidas/enviadas por día |
| **Recibida / Enviado por Mes** | Ambos | Cantidad máxima de transferencias recibidas/enviadas por mes |
| **Porcentaje de Salario Mensual** | Ambos | Porcentaje máximo del salario mensual del cliente |
| **Porcentaje de Salario Diario** | Ambos | Porcentaje del salario diario del cliente |
| **Intervalo de tiempo entre transferencias salientes** | Salientes | Tiempo mínimo entre transferencias (segundos) |
| **Cambio de Contraseña** | Ambos | Tiempo desde el cambio de contraseña — *ver nota de inconsistencia de unidad (segundos vs. minutos) en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md)* |
| **Consulta con Listas de Informados para Emisor** | Ambos | Acción a realizar si se detecta transferencia originada desde un Terrorista, PEP o SO (ver conector Worldsys en [configuracion_inicial.md](configuracion_inicial.md#312-conectores-externos-worldsys)). Incluye configuración de **Timeout**: acción a tomar ante timeout/error de conexión. |

Al finalizar la configuración de Acciones Anteriores, se define la sección **Acciones** (Bloqueo de Cuenta y/o Alerta) y se presiona "Aceptar" para crear la restricción (mensaje de éxito en verde).

## 7. Simulación de Transferencias

Módulo que permite crear y probar reglas sin aplicarlas directamente en producción. Tipos soportados: **Reglas Estándar, Reglas Reputacionales, Reglas Machine Learning**, y **Reglas Propuestas** (simulaciones sugeridas por el sistema que el cliente puede convertir en reglas reales, con optimización agregada por el sistema — ver el "servicio de simulaciones propuestas" en [configuracion_inicial.md](configuracion_inicial.md#3-parametrías-generales), parámetro 3.1.11).

### 7.1 Simulación Restricción Estándar

Procedimiento de creación análogo al de Reglas Estándar reales, variando solo las Acciones disponibles:
- **Entrantes**: Bloqueo de Cuenta y/o Alertas.
- **Salientes**: 2FA, Bloqueo de Cuenta, Rechazo de transacción, y/o Alertas.

**Modal "Crear Simulación" — campos**: Nombre de la restricción, Modo de creación de la cuenta, Ámbito, Banca, Tipo de cliente, Tipo de producto, Tipo de subproducto, Moneda, Monto mínimo, Monto máximo, Aplicar día de la semana, Vigencia de horario, Vigencia 24hs, Vigencia de día (Desde–Hasta), Destinatario, Acciones anteriores, Acciones (Bloqueo de cuenta – Alerta), **Cuándo correr el servicio (Horario - Día)**.

**Listado de simulaciones — columnas**: Nombre, Fecha, Monto mínimo, Monto máximo, Habilitado (switch), Estado, Bloqueos, Acciones (Convertir – Eliminar – Ver Resultados).

**Gráfico de Estado de Simulaciones**: Procesadas, En Proceso, No Procesadas, Inactivas (y "En cola de procesamiento" — ver más abajo en ML).

**Top 5 de Restricciones Simuladas**: ranking de las 5 simulaciones más utilizadas.

**Acciones sobre una simulación**:
1. **Convertir restricción**: transforma la simulación en regla real; desaparece de Simulaciones y pasa a Reglas Estándar (según Ámbito y Tipo), comenzando a regir según lo parametrizado.
2. **Eliminar**: modal de confirmación; se quita también del gráfico de Estados y del Top 5.
3. **Ver Resultados**: redirige a pantalla de detalle.

**Pantalla de Resultados**:
- "Información de consulta": resumen del detalle cargado (izquierda) + gráfico dona de proporción de transferencias afectadas, con Errores Tipo I y Tipo II (derecha).
  - **Error Tipo I** (verde): transferencia legítima incorrectamente identificada como fraudulenta.
  - **Error Tipo II** (rojo): transferencia fraudulenta no detectada, aprobada como legítima.
  - Condición de aceptabilidad: **Alfa (α)** aceptable si ≤ AlfaPrime; **Beta (β)** aceptable si > BetaPrime.
- Gráfico dona con 4 segmentos: Aprobada confiable (azul claro), Aprobada fraude (verde), Rechazada confiable (amarillo), Rechazada fraude (rojo).
- **Campos a visualizar**: destildar propiedades por defecto.
- **Buscador — filtros disponibles**: Fecha (Desde–Hasta con horario), ID de TX, Moneda, Monto (Desde–Hasta), Motivo de Rechazo, Respuesta Realizada, Respuesta Simulada, Marca (Fraudulentas o Confiables), CUIT/CUIL Origen, CUIT/CUIL Destino.

### 7.2 Simulación de Reglas Reputacionales

**Crear Simulación — campos**: Nombre de la simulación, Agregar nueva Regla + puntuación (1-1000), Agregar Whitelist/Blacklist (Tipo y Motivo), Acciones (puntuación total por tipo de riesgo), Vigencia de día (Desde–Hasta), Habilitar/deshabilitar.

**Listado de Simulaciones — columnas**: Nombre, Fecha, Habilitada, Estado, Bloqueos, Acciones.

**Acciones**: Convertir (pasa a Reglas Reputacionales reales, desaparece del listado/gráfico/Top 5 de Simulaciones), Eliminar (confirmación), Resultados (mismo patrón de dona + Errores Tipo I/II que en Reglas Estándar).

**Detalle rápido**: al hacer clic en una simulación del listado se muestra su detalle en el recuadro de Consulta (solo lectura, sin edición).

**Buscador por palabra**: campo de búsqueda por nombre de simulación.

### 7.3 Simulación de Reglas Machine Learning

Sirve para reentrenamiento del algoritmo de IA (múltiples reentrenamientos diarios), ajuste de pesos por variable y rangos de fechas, y detección de errores Tipo I/Tipo II antes de producción.

**Crear Simulación — campos**: Nombre, Agregar nueva regla (tipo de regla + puntuación), Modificar puntuación total por tipo de riesgo, Vigencia de día (Desde–Hasta), Habilitar/deshabilitar, Aceptar.

**Estados de simulación**: Procesadas, En Proceso, No Procesadas, Inactivas, y **"En cola de procesamiento"** (esperando turno).
- **Límite de concurrencia**: el sistema admite correr **hasta 2 simulaciones simultáneas**; si se programan 3 para el mismo horario, 2 corren y la tercera queda en cola.

**Listado de simulaciones — columnas**: Nombre, Fecha, Estado, Bloqueos, Habilitado, Acciones (Convertir, Eliminar, Ver Resultados).

**Buscador — filtros**: Fecha de creación, ID de TX, Moneda, Monto, Motivo de rechazo, Respuesta Realizada, Respuesta Simulada, Marca, CUIT/CUIL Origen, CUIT/CUIL Destino. Incluye botón "Resetear valores de búsqueda", paginado y scroll.

### 7.4 Simulación Propuesta

Herramienta del sistema para replicar escenarios sobre transferencias pasadas sin afectarlas (modelo computacional).

**Listado — columnas**: Tipo (de regla simulada), Fecha, Bloqueos (cantidad de bloqueos de clientes generados), **α y β** (niveles de significancia y potencia, resultado de las mejoras aplicadas), Acciones (Convertir, Eliminar, Ver Resultados).

**Acciones**: Convertir (a regla real, con modal de detalle y acciones), Eliminar (modal de confirmación), Resultados (pantalla de detalle), y Detalle (al seleccionar una simulación propuesta se despliega su información completa a la derecha).

## 8. Reglas de Interentidades

Directrices compartidas entre varias entidades, aplicando las mismas parametrías a todas simultáneamente. Incluye la funcionalidad de compartir o no las segmentaciones con otras entidades.

### 8.1 Reglas Interentidades Estándar de Transferencias

**Propósito**: unificar criterios de riesgo, prevenir fraude de manera homogénea, reducir duplicación de esfuerzo de configuración.

**Características**:
- **Aplicación transversal**: afectan a todas las entidades asociadas a la regla.
- **Configuración única**: se define una vez y se aplica en simultáneo.
- **Condiciones uniformes**: mismo comportamiento (rechazo, bloqueo, alerta) para cada entidad.
- **Segmentación común**: aplicable sobre grupos de clientes compartidos por varias entidades, o de forma individual (desde Parametrías Generales).

**Ejemplo de uso citado en la fuente**: establecer que ninguna entidad permita transferencias salientes mayores a $500.000 sin verificación reforzada, mediante una única regla interentidad saliente en lugar de configurarla entidad por entidad.

**Cuándo conviene usarlas** (según la fuente): cuando varias entidades deben cumplir la misma política de seguridad; para mantener consistencia en los controles; para escalar ajustes rápidamente sin ir entidad por entidad; ante requisitos regulatorios o institucionales comunes.

Se dividen en dos grupos: **Entrantes** y **Salientes**.

#### 8.1.1 Gestión — Lista de reglas (columnas)

Igual estructura que las Reglas Estándar por entidad: Nombre, Fecha, Moneda, Monto mínimo, Monto máximo, Habilitada (switch), Acciones — con la diferencia de que aquí las Acciones son: **editar, rechazar, o asociar entidad** (en vez de editar/eliminar/ajustes).

Botones de acción rápida: Restablecer valores de búsqueda, Crear Nueva.

#### 8.1.2 Crear Regla Interentidad — Campos

Prácticamente idénticos a los de Reglas Estándar entidad-única (sección 5.1.2): Nombre de la restricción, Modo de creación de cuenta, Ámbito (Interno/Externo/Debin), segmentación (Tipo de Persona, Tipo de Banca, Tipo de Cliente, Tipo de Producto, Tipo de Subproducto — todas configurables vía ABM por entidad), Moneda, Monto mínimo, Monto máximo, Aplicar día de la semana, Vigencia de Horario (switch 24hs), Vigencia de Día (Desde obligatorio / Hasta condicional), Destinatario (Mismo al originante / Distinto al originante / Indistinto), Acciones anteriores, Acciones (habilitable o no), Alerta (PLAFT u Operativas).

Se finaliza con el botón **"Guardar"**.

---
*Ver también: [scoring.md](scoring.md) para el sistema de puntuación aplicado a reglas estándar de este módulo, [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md) para la fuente de datos de las Reglas Reputacionales, y [apis_externas.md](apis_externas.md) para la API `/Transfer` que analiza estas transferencias en tiempo real.*
