# Ardid/Akurtech — Módulo de Login

> Estado: en producción.

> Fuente: `Akurtech 4 - Login.pdf` (31 páginas), guía funcional oficial del proveedor. Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general y [configuracion_inicial.md](configuracion_inicial.md) para el login del propio operador de Ardid (distinto de este módulo, que analiza los logins de los **clientes finales** de la entidad).

## 1. Pantalla Login (monitoreo)

Accesible desde el Dashboard General, card **Login** (gráfico tipo dona con % de estados + Top 5 clientes con logins exitosos/fallidos).

### 1.1. Gráfico — Estados de login (dona, en %)

| Estado | Significado |
|---|---|
| Aprobado ✅ | Logins exitosos |
| Aprobado ❌ | Logins exitosos que solicitaron 2FA al cliente |
| Rechazado | Intentos de login rechazados |
| Fallido | Intentos que fallan antes de ser rechazados |

### 1.2. Top 5 clientes
Login exitoso y fallido, actualizado minuto a minuto, con cortes por hora.

### 1.3. Listado de Login
- Columnas visibles = Propiedades tildadas en "Campos a visualizar".
- **Buscador**: filtros por columna habilitada (ícono lupa).
- **Resetear valores de búsqueda**: limpia todos los filtros.
- **Descargar .csv**: descarga listado completo o filtrado.

## 2. Reglas estándar — Login

Controles atómicos basados en identificadores únicos (CUIT, CUIL, DNI) sobre intentos de autenticación. Objetivo: detectar patrones como ubicaciones incompatibles en poco tiempo, cambios frecuentes de dispositivo, accesos repetitivos en intervalos cortos, o logins inmediatamente posteriores a cambio de contraseña (señales de toma de control de cuenta).

**Crear nueva regla** (botón "Crear nueva" → modal):

| Campo | Detalle |
|---|---|
| Nombre de Restricción | Texto |
| Modo de creación de cuenta | Select |
| Tipo de persona | Select |
| Tipo de Banca | Select |
| Tipo de Cliente | Select |
| Aplicar día de la semana | Checkbox múltiple (uno, varios o todos) |
| Vigencia horaria | Habilitar/deshabilitar: Vigencia 24hs. o rango Desde–Hasta |
| Vigencia del día | Desde – Habilitar/deshabilitar Hasta |

**Acciones Anteriores** (condición previa a evaluar):

| Opción | Descripción |
|---|---|
| Ninguno | El sistema prosigue directo a la parametrización de Acciones |
| Distancia en KM y Tiempo | Evalúa si dos logins del mismo usuario ocurren dentro de un rango lógico de distancia geográfica/tiempo. Si la distancia es físicamente imposible para el tiempo transcurrido, se considera sospechoso |
| Intervalo de tiempo de cambio de dispositivo | Analiza tiempo transcurrido entre logins desde distintos dispositivos del mismo usuario |
| Intervalo de tiempo entre login | Monitorea frecuencia de intentos de login; múltiples logins en poco tiempo puede indicar comportamiento automatizado, fuerza bruta o validación masiva de credenciales |

**Acciones** (resultado de la regla): Bloqueo de cuenta / Rechazo de transacciones / Solicitud de 2FA.
**Alerta** (habilitar/deshabilitar): Alerta Operativa, Alerta PLAFT.

Al presionar "Aceptar" se crea la regla (mensaje de confirmación en verde).

**Listado de reglas** — columnas: Nombre, Fecha de creación, Habilitado (switch on/off), Acciones (Editar, Eliminar). Editar reabre el modal con datos cargados; Eliminar pide confirmación. El recuadro derecho muestra el **Detalle** de la regla seleccionada.

## 3. Reglas Reputacionales — Login

Asignan puntuaciones de riesgo a intentos de login según criterios como dispositivo, IP, cuenta o identificación. Suman o restan puntos a la reputación del evento según el nivel de confianza. **Los datos se toman de Blacklist/Whitelist** (ver [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md)): si el dato no está en las listas, el control no se realiza.

| Tipo de regla | Efecto en score | Ejemplos |
|---|---|---|
| Reglas Negativas (riesgo) | Suman puntos (+) | "Dispositivo sospechoso", "IP sospechosa" |
| Reglas Positivas (confianza) | Restan puntos (−) | "Cuenta conocida", "Identificación válida" |

- Rango de puntuación por regla: **1 a 1000 puntos**.
- A mayor puntuación, mayor riesgo del login; a menor puntuación, más confiable.
- Interactúan con Blacklist (penalización adicional) y Whitelist (bonificación reputacional).

**Acciones (umbrales de Puntuación Total):**

| Acción | Condición | Nivel de riesgo | Alerta |
|---|---|---|---|
| Aprobar Login | score ≤ máximo permitido | Riesgo Aceptado | Opcional |
| Solicitar Challenge (2FA) | score ≥ mínimo | Riesgo Bajo | Opcional |
| Rechazar login | score ≥ mínimo permitido | Riesgo Medio | Opcional |
| Bloqueo de Cliente | score ≥ mínimo permitido | Riesgo Alto | Opcional |

Ver el detalle completo de este esquema de scoring (compartido con Transferencias y Pagos) en [scoring.md](scoring.md).

Las alertas activadas se reflejan en la pantalla de **Alertas Operativas**.

**Agregar Regla**: botón "Agregar nueva regla" → modal; al seleccionar un ítem del listado de control, el modal indica si la puntuación es negativa o positiva; se ingresa el score y se presiona "Aceptar".
**Eliminar Regla**: botón Eliminar → modal de confirmación → "Aceptar".
**Actualizar Cambios**: se corrige el puntaje en el campo "Valores" (fila Puntuación) y se presiona "Actualizar" (mensaje de éxito en verde).

## 4. Reglas Comportamentales — Login

Se activan **por entidad**. Requisito: la entidad debe tener al menos una **Aplicación** creada y parametrizada con más de una **Acción Comportamental** (ver [configuracion_inicial.md](configuracion_inicial.md#4-parametrías-de-entidad)).

**Acciones (umbrales de Puntuación Total):**

| Acción | Condición | Nivel de riesgo | Alerta |
|---|---|---|---|
| Aprobar una transferencia | score ≤ máximo permitido | Riesgo Aceptado | Opcional |
| Solicitar Challenge en una transferencia | score ≥ mínimo | Riesgo Bajo | Opcional |
| Rechazar un pago | score ≥ mínimo permitido | Riesgo Medio | Opcional |
| Bloqueo de Cliente | score ≥ mínimo permitido | Riesgo Alto | Opcional |

> ⚠️ **Nota de fidelidad de la fuente:** el texto original de esta sección del PDF de Login usa terminología de "transferencia" y "pago" en varios pasajes (como en la tabla de arriba) en lugar de "login" — sugiere contenido compartido/reutilizado entre los distintos módulos de la documentación del proveedor. Se transcribió tal cual aparece en la fuente, sin corregir.

Al terminar de configurar, se presiona "Aceptar"; luego un usuario con permisos habilitados puede **Aprobar o Rechazar las modificaciones pendientes** (flujo de doble control/aprobación).

**Crear Nueva Regla Comportamental** (botón "Crear Nueva"):

| Campo | Detalle |
|---|---|
| Nombre de la Regla | Texto |
| Tipo de regla | "Acción vs Acción" o "Acción" |

**Si es tipo "Acción vs Acción":**

| Campo | Descripción |
|---|---|
| Aplicación | Seleccionar una previamente creada |
| Acción vs Acción | Seleccionar una Acción vs. otra Acción, ambas previamente creadas |
| Rango de tolerancia de acciones (%) | Margen aceptable de variación respecto al promedio histórico de acciones del usuario. Ej.: tolerancia 20% sobre promedio de 10 transferencias/día → rango aceptable 8-12 |
| Desvío del cálculo de promedio (%) | Mide cuánto se desvía el comportamiento actual del promedio histórico. Ej.: desvío configurado en 90% → si se supera, se considera sospechoso y se aplican las reglas definidas |
| Rango de tolerancia de tiempo (%) | Margen de tiempo (en milisegundos) aceptable entre dos acciones del usuario (ej. entre "Login" y "Transferir") |
| Desvío del cálculo de promedio de tiempo (%) | Cuánto se desvía el tiempo real entre acciones del tiempo promedio histórico (en ms) |

**Si es tipo "Acción":**

| Campo | Descripción |
|---|---|
| Aplicación | Seleccionar una previamente creada |
| Acción | Seleccionar una previamente creada |

Tres checkboxes que despliegan parametrías adicionales — **Superficie**, **Tiempo de touch** (también "Tiempo de presión"), **Posición**. Cada uno con los mismos campos: Rango de tolerancia de acciones (%), Desvío del cálculo de promedio (%), Promedio Histórico, Desvío, admite activación de Alerta.

**Puntuación final de la regla comportamental:**
- **Valor de Puntuación Negativa** y **Positiva**: rango **0 a 1000**. Reglas Negativas → signo +; Reglas Positivas → signo −.
- **Tiempo de vida en segundos** para las acciones de la regla.
- Al presionar "Aceptar" se activan **modificaciones pendientes**, sujetas a aprobación/rechazo por un usuario con permisos.

**Vista Previa de Reglas Habilitadas** (recuadro superior derecho): lista todas las Reglas Comportamentales creadas + sumatoria total de Puntuación Negativa y Positiva.

**Listado de Reglas** (recuadro superior izquierdo): Nombre de la Regla, Aplicación, Acciones, Valor; con acciones de edición y eliminación.

Ante una transacción de cuenta sospechosa/score negativo, el resultado se contrasta con otros tipos de reglas parametrizadas y **el sistema toma la acción más restrictiva activada**.

---
*Ver también: [scoring.md](scoring.md) para el sistema de puntuación compartido entre Login, Transferencias y Pagos, y [configuracion_inicial.md](configuracion_inicial.md) para la configuración de Apps/Actions usadas en Reglas Comportamentales.*
