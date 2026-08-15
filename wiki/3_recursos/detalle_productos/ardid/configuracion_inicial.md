# Ardid/Akurtech — Configuración Inicial

> Estado: en producción.

> Fuente: `Akurtech 1 - Parámetros iniciales.pdf` (98 páginas), guía funcional oficial del proveedor (Akurtech/Pentass). Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general del módulo y la nota Ardid=Akurtech.

## 1. Login y 2FA (acceso a la plataforma)

**Pasos de inicio de sesión:**
1. Introducción de credenciales: usuario válido + contraseña válida.
2. Presionar el botón **"Iniciar Sesión"**.
3. **Verificación de Dos Factores (2FA)**: solo se solicita si está activa en Parametrías Generales y no está desactivada para el usuario puntual. Se pide un código de 6 dígitos generado por **Google Authenticator**, con validez limitada (normalmente 30 segundos); el sistema solo acepta el código más reciente y válido.

**Panel de usuario** (se abre al presionar el nombre de usuario logueado):

| Campo/opción | Descripción |
|---|---|
| Nombre de usuario | Usuario logueado |
| Email | Email del usuario logueado |
| Habilitar/Deshabilitar tours | Switch, habilitado por defecto en usuarios nuevos; al deshabilitar y rehabilitar reinicia el tour de Akurtech |
| Versión | Versión actual de Akurtech |
| Último ingreso | Fecha y horario del último ingreso |
| Cerrar sesión | Botón de logout |
| Cambiar contraseña | Abre modal: contraseña actual, nueva contraseña, confirmación. Requisitos parametrizables en "Parametrías de seguridad de cuentas de usuario". Solo usuarios **LOCALES** pueden cambiar contraseña desde este panel |
| Temas | Paleta de temas del sistema (incluye tema oscuro); se selecciona y se presiona "Aplicar" |

## 2. Dashboard (pantalla "General")

Al iniciar sesión correctamente, el sistema dirige a la pantalla **General** (Dashboard), compuesta por "cards":

| Card | Contenido | Acción del botón de acceso |
|---|---|---|
| Gestión de Alertas | Listado de alertas activadas en la última hora + gráfico del mes vigente | Redirige a pantalla de Alertas (Operativas y PLAFT) |
| Gestión de Usuarios | Total de usuarios asignados a la entidad actual | Redirige a Gestión de Usuarios (listado completo bajo administración del usuario) |
| Gestión de Perfiles | Total de perfiles creados para la entidad seleccionada | Redirige a Gestión de Perfiles |
| Blacklist/Whitelist | Gráfico ajustado por escala con cantidades totales en Blacklist/Whitelist de la entidad seleccionada + listado de novedades fraudulentas | Redirige a pantalla Blacklist/Whitelist |

**Elementos adicionales del Dashboard:**
- **Select de Entidades** (esquina superior izquierda): lista entidades donde el usuario tiene permisos de administrador; buscador; favoritos marcables con ícono de corazón (quedan anclados arriba); botón **"Crear nueva entidad"** al pie del listado (modal pide Nombre, Código, País; no admite códigos repetidos).
- **Campana de Notificaciones** (superior derecha): notifica eventos como Simulaciones procesadas y Ráfagas activadas; despliega últimas 4 notificaciones; permite eliminar individualmente o "Eliminar todas"; botón "Ver más" lleva a pantalla de Notificaciones (filtro por palabra clave o rango de fechas desde/hasta).
- **Select de Idioma**: Español, Inglés.

**Menú principal** (lateral izquierdo, se oculta/muestra presionando el logo):
1. Dashboard de Monitoreo
2. Transferencias y Pagos
3. Alertas
4. Whitelist y Blacklist
5. Reporte Operativo
6. Gestión de reglas interentidades
7. Reporte de Auditoría
8. Parametrías
9. Akurtech GPT (chatbot de IA para consultas sobre el uso de Akurtech)
10. Cerrar Sesión (al pie del menú)

## 3. Parametrías Generales

Pantalla accesible desde la card "Parametrías Generales"; ajustes comunes a todas las entidades.

| # | Parámetro | Detalle / campos |
|---|---|---|
| 3.1.1 | **Tiempo de respuesta máximo esperado** | Tiempo en milisegundos máximo tolerable para el impacto de transferencias. Si se supera, se marca en rojo el tiempo más alto registrado (footer de pantalla Transferencias, junto al promedio en verde) |
| 3.1.2 | **Período de duración histórico de login fallido** | Cantidad de días; pasado el período se borran los históricos de login fallido de la BBDD. Botón "Guardar" |
| 3.1.3 | **Período de duración histórico de login satisfactorio** | Cantidad de días que el sistema mantiene el inicio de sesión abierto (ahorra tiempo); pasado el período se borran los registros |
| 3.1.4 | **ABM Monedas** | Agregar/editar/eliminar monedas por entidad. Modal "Agregar Moneda": campos Divisa, Abreviación, Símbolo. Columna Acciones permite Editar/Eliminar |
| 3.1.5 | **Compartir lista negra por ráfagas entre entidades** | Switch "Ráfagas de transferencias a un mismo destinatario" |
| 3.1.6 | **Canales de Rabbit** | Mensajería/cola para comunicación entre módulos. Campos: Servidor, Anfitrión virtual, Puerto, Usuario (admite cambio de contraseña), Nombre de cola de Transferencias, Nombre de cola de Pagos, Nombre de cola de Login. Botón "Guardar" |
| 3.1.7 | **Historificación** | Traslada datos (alertas, reportes de auditoría) a BBDD secundaria. Campos: Activar/desactivar historificación de Transferencias, Pagos y Alertas; Cantidad de meses en línea; Cantidad máxima de registros; Cuándo correr el servicio (fecha/hora); Cada cuántos meses corre el servicio |
| 3.1.8 | **Tarjetas** | Configuración de uso de tarjetas y respuestas del procesador. Campos: Cantidad de intentos de datos erróneos; Cantidad de intentos de pagos con motivos sospechosos; Tiempo para validación de tarjeta; Control de coincidencia de DNI (switch) |
| 3.1.8 (cont.) | **Respuestas del Procesador** | Configuración de respuestas del procesador de pago usadas en API NotRealized, categorizadas en: **Activa tarjeta** (transacción→rechazada status 2, tarjeta→validada estado 1, blanquea contador de motivos sospechosos), **Bloquea tarjeta** (transacción→rechazada, tarjeta→bloqueada estado 2), **Tarjeta inválida** (transacción→rechazada, tarjeta→inválida estado 6), **Respuesta sospechosa** (transacción→rechazada; si tarjeta en estado inicial 0→pendiente de validación estado 4; incrementa contador de motivos sospechosos). Otros motivos no categorizados: transacción→rechazada, tarjeta inicial(0)→pendiente(4), reversión de contadores si ya había sido procesada |
| 3.1.9.0 | **Tarjetas – Contracargo** | Parametriza contracargo de datos marcados como "Fraude" para: Tarjeta, Identificación, Dispositivo, Correo, Comercio. Campos: Añadir a Blacklist (switch); Alerta (switch); Cantidad de pagos; Cantidad de Tiempo (en días) |
| 3.1.10 | **Pagos** | ABM de: Canales de pago (ej. Presencial/POS, En línea, Móvil, Teléfono), Tipo de pago (tarjeta crédito/débito, transferencia bancaria, efectivo, e-wallets), Tipos de tarjeta, Grupos de comercio, Grupos de BIN (agrupan tarjetas por marca, tipo, producto — primeros 6-8 dígitos) |
| 3.1.11 | **Servicio de simulaciones propuestas** | Motor de decisiones que propone versiones optimizadas de reglas basándose en feedback de usuarios y tasas de falsos positivos/negativos. Campos: "Cuándo corre el servicio" (hora, ej. 12:30); "Cantidad máxima de intentos del servicio" (ej. 100) |
| 3.1.12 | **Conectores Externos (Worldsys)** | Verifica personas/gestiona riesgos (PEP, Sujeto Obligado, Terroristas), actualiza blacklists automáticamente. Campos: Usuario y Contraseña; URL; Fecha de escaneo general (día del mes); Fecha de escaneo de novedades (día del mes); Timeout (ms); Analizar transferencias externas (activado/desactivado). Por categoría de riesgo (PEP/Sujeto Obligado/Terrorista): Añadir a Blacklist (switch), Alerta (switch). Parametrías de Akurtech: Activar (switch), Horario de corrida, Frecuencia de corrida (en horas) |
| 3.1.13 | **Compartir modo de creación, segmentación y producto** | Crea modos de creación, tipos de producto, cliente, persona y banca compartibles entre entidades. **Dato:** una vez activado el switch NO se puede desactivar. Sub-secciones: Modo de creación (Agregar nuevo/Editar/Eliminar), Segmentación (tipos de persona), Producto (tipos de producto y subproducto) |
| 3.1.14 | **Licencia** | Gestión de licencia de uso. Muestra: fecha de expiración, días restantes, alerta en rojo si está por vencer/vencida. Carga: botón "Seleccionar Documento" (archivo .lic) + botón "Enviar" |
| 3.1.15 | **Comentario obligatorio en Blacklist y Whitelist** | Switch que obliga a añadir comentario al agregar datos a las listas |
| 3.1.16 | **Rubros** | Parametriza "Ticket promedio anual" y "Devolución promedio anual" por rubro; buscador; edición inline (ícono editar → input, con "X" para descartar y "Check" para guardar) |

## 4. Parametrías de Entidad

Acceso vía botón "Acceder" en card "Parametrías de la entidad" → pantalla **Entidades**.

**Crear nueva entidad** (modal de 3 pasos):

| Paso | Nombre | Campos |
|---|---|---|
| 1 | Datos de entidad | Nombre; Código (único, máx. 10 caracteres numéricos); Selección de país (zona horaria) |
| 2 | Segmentación de la Entidad | Formato de segmentación: *Tipo de Persona/Banca/Cliente*, *Tipo de Cliente*, *Tipo de Banca/Cliente*, *Tipo de persona/Cliente*. **Restricción: una vez creado un registro bajo una segmentación, no puede modificarse** |
| 3 | Ámbitos | Activar/desactivar scopes de transferencias; cambiar nombre; agregar ámbitos |

**Categorías de segmentación** (jerárquicas, ej. Tipo de Persona → Tipo de Banca → Tipo de Cliente):
- **Tipo de Persona**: identifica persona física/jurídica.
- **Tipo de Banca**: clasifica según servicio bancario (ej. Banca Comercial, Preferencial).
- **Tipo de Cliente**: categoriza según relación/transacciones (ej. Regular, Premium, Empresarial).

Cada categoría tiene un **ID único** usado por APIs externas — ver [apis_externas.md](apis_externas.md) (módulos `/PersonType`, `/BankTypes`, `/ClientType`). Acciones permitidas: Agregar Nuevo, Agregar Existente, Modificar, Eliminar (solo si no está asociado a cliente activo).

**Detalle de la entidad** (al seleccionar una entidad del listado) — datos mostrados: nombre, código, tiempo de depuración de alertas, zona horaria, modo de creación de cuenta, aprobar transferencias de clientes no existentes, activar scoring en reglas estándar, correo electrónico, Telegram.

| Switch/campo | Función |
|---|---|
| **Aprobar transferencias de clientes no existentes** | Encendido: permite transferencias sin que el cliente exista en la entidad. Apagado: solo con clientes dados de alta |
| **Activar Scoring en reglas estándar** | Define si reglas de pagos/transferencias/login usan sistema de puntuación en lugar de acciones fijas. Ver [scoring.md](scoring.md) para el detalle completo. Al activar sin reglas previas: no se crean acciones por defecto. Al activar con reglas existentes: se generan acciones por defecto (Alerta: 0, 2FA: 10, Rechazo: 100, Bloqueo cliente: 1000). Al desactivar: modal obligatorio para seleccionar una acción por tipo de regla (transfer, pagos, login); campo scoring vuelve a null |
| **Correo electrónico / Telegram** | Editables/eliminables vía columna Acciones (botones Editar/Eliminar con modal de confirmación) |
| **Transferencias y Pagos** | Configuración de niveles de inferencia (categorización de riesgo y respuestas automáticas). En Transferencias: activar/desactivar scopes/ámbitos. En Pagos: Grupos de comercio (ej. Retail, Alimentos y bebidas, Entretenimiento, Turismo, Servicios) |
| **Aplicaciones** | Editables vía columna Acciones. Base para crear **Reglas Comportamentales** (analizan comportamiento de usuarios en apps móvil/web) |
| **ABM de categoría de clientes** | Igual mecánica que segmentación de entidad (ver arriba) |
| **Parametría de la Aplicación** | Botón "Parametría de App" → pantalla para crear/editar/eliminar **Acciones** (campos: Nombre, ID de Acción) usadas en Reglas Comportamentales |
| **Grupos de comercio** | Botón "Agregar nuevo" (campos: nombre, código). Por grupo: ícono "Consulta" muestra comercios asignados; "Agregar nuevo" comercio pide Razón social, CUIT/CUIL, switch "exceptuar el comercio de los controles de reglas estándar de comercio"; tabla de cuentas asignadas al comercio (editar/eliminar) |

**Listado de entidades** — columnas: Nombre, Código, Habilitado (switch), Acciones (Editar, Agregar App, Clonar Entidad, Configuración de notificaciones).

| Acción | Detalle |
|---|---|
| **Editar** | Modifica nombre, código, zona horaria; modo de creación de cuenta (mover elementos entre columnas "NO" y "SÍ") |
| **Agregar App** | Modal: Nombre, ID de la aplicación, URL. Sirve para crear Reglas Comportamentales |
| **Clonar Entidad** | Modal: Nombre de entidad, código + checkboxes: Lista blanca/lista negra, Segmentación, Reglas IA, Reglas de Machine Learning, Reglas Reputacionales |
| **Configuración de notificaciones** | Campos: Nombre del servidor o IP; Puerto del servidor; Tiempo de espera SMTP (ms); Usar credenciales (switch); Usuario; Contraseña; Activar TLS (switch); Correo; Cantidad de reintentos máximos; Token de Telegram |

## 5. Gestión de Usuarios y Perfiles

**Listado de usuarios** — columnas: Nombre, Usuario, Dominio, Perfil, Correo, Descripción, switch **2FA** (si se deshabilita, solo se reactiva cuando el usuario ingresa el código de la App Authenticator), switch **Habilitar** (usuario deshabilitado no puede ejecutar nada), columna **Acciones** (Editar, Restablecer 2FA, Eliminar).

**Crear usuario** (modal de 3 pasos: "Datos del usuario", "Asignar Entidades", "Perfil"):

| Paso | Detalle |
|---|---|
| Datos del usuario | Elegir "Usuario AD" o "Usuario Local". **AD**: formato `[dominio]\[usuario]`, botón "Buscar usuario"; se desbloquean campos Correo electrónico y Descripción. **Local**: Nombre, Apellido, Nombre de usuario, Correo electrónico, Contraseña (según requisitos de Parametrías de seguridad) |
| Asignar Entidades | Transfer list (izquierda: disponibles: derecha: asignadas) con 4 botones de transferencia (masiva izq→der, individual izq→der, individual der→izq, masiva der→izq). Se requiere al menos una entidad para avanzar |
| Perfil | Select de perfiles existentes + opción "Crear nuevo perfil" (campos: Nombre, Descripción, Permisos por módulo — botones para activar toda una fila de permisos o elegir individualmente) |

**Reglas de negocio de usuarios:**
- Un usuario no puede eliminarse a sí mismo.
- Solo administradores o usuarios con permiso correspondiente pueden eliminar usuarios.
- Solo contraseñas de usuarios LOCALES pueden cambiarse.
- **Detalle de usuario** (solo lectura): Último ingreso, Última actualización, Fecha de alta, Nombre, Apellido, Usuario, Perfil, Email, Descripción, Entidades asignadas.
- **Filtros disponibles**: Nombre, Usuario, Dominio, Perfil, 2FA (Habilitado/Deshabilitado), Habilitar (Habilitado/Deshabilitado). Botón "Reestablecer valores de búsqueda".
- **Descarga .csv** del listado (completo o filtrado).

**Gestión de Perfiles:**
- Listado: Nombre, Descripción, Acciones (Editar, Eliminar). Perfil asignado a algún usuario **no puede eliminarse**.
- **Crear nuevo perfil**: modal con Nombre y Descripción.
- **Detalle/Permisos**: se tildan casilleros de permisos por módulo, luego botón "Actualizar cambios".
- **Descarga .csv** de perfiles ("Descargar Adjunto").
- **Buscador** por nombre de perfil.

**Tipos de permiso configurables por módulo:**

| Permiso | Función |
|---|---|
| Agregar | Crear nuevos registros/elementos |
| Editar | Modificar elementos/configuraciones existentes |
| Eliminar | Borrar registros/elementos |
| Exportar | Descargar/generar informes .csv |
| Analizar | Realizar acciones dentro de registros específicos |
| Consultar | Visualizar información |
| Habilitar | Activar/desactivar funcionalidades, registros o estados |
| Convertir | Transformar un registro/elemento a otro estado |
| Marcar | Señalar/etiquetar elementos con estado específico |
| Asignar | Vincular registros/elementos a entidades específicas |
| Desasignar | Desvincular registros/elementos de entidades específicas |
| Cambiar contraseña | Modificar contraseñas |
| Modificaciones pendientes | Gestionar/visualizar cambios aún no confirmados |
| Documento adjunto | Agregar archivos adjuntos |
| Reporte programado | Crear/configurar reportes programados |

## 6. Parametrías de Seguridad

| Parámetro | Detalle |
|---|---|
| **Timeout de sesión de usuario** | Tiempo máximo en minutos de inactividad antes de cierre de sesión forzada |
| **Solicitud de Challenge (2FA)** | Activable/desactivable para todos los usuarios del sistema; se activa en escenarios de riesgo bajo/moderado |
| **Deshabilitar usuario por inactividad** | Cantidad de días tras los cuales se deshabilita un usuario inactivo (rehabilitable desde Gestión de Usuarios) |
| **Dominio por defecto Active Directory** | Dominio que aparece por defecto al crear usuarios AD |
| **Parametrización de cuentas locales** | Cantidad de intentos fallidos hasta bloqueo de usuario; Tiempo para desbloqueo de usuario (días); Longitud mínima de contraseña; Longitud máxima de contraseña; Caducidad de contraseña (días); Historial de contraseña a controlar (cantidad); Requisitos de contraseña (checkboxes: Minúsculas, Mayúsculas, Caracteres especiales) |

## 7. Dashboard de Monitoreo (dashboards personalizados)

Cada usuario puede crear dashboards dinámicos y personalizados (múltiples, con nombre, editables, eliminables, seleccionables).

**Crear nuevo dashboard**: botón "Nuevo Dashboard" → cards disponibles organizadas por módulo: Transferencias, Reglas de Transferencias, Simulación de Transferencias, Pagos, Reglas de Pago, Login, Reglas de Login. Se arrastran al área central (drag & drop). Obligatorio: nombre + al menos una card.

**Rangos de tiempo configurables por card**: 30 minutos, 1 hora, 2 horas, 6 horas, 12 horas, 24 horas, 48 horas, 72 horas, 15 días, 30 días, 90 días, 365 días, Histórico (default: 24 horas si no se configura).

**Cards SIN rango de tiempo configurable:**
- Transferencias: Reglas de Transferencias, Reglas IA, Reglas reputacionales, Reglas machine learning, Reglas comportamentales.
- Pagos: Reglas de pagos, Reglas reputacionales de pagos, Reglas IA de pagos, Reglas machine learning de pagos, Reglas comportamentales de pagos.
- Login: Reglas de Login, Reglas reputacionales de Login, Reglas comportamentales de Login.

Edición: ícono "Lápiz" permite mover, borrar o agregar cards, y editar campos (Rango de Tiempo o Estado) de cada card. Eliminación de dashboard vía botón dedicado + modal de confirmación.

---
*Ver también: [modulo_login.md](modulo_login.md), [scoring.md](scoring.md), [modulo_transferencias.md](modulo_transferencias.md), [modulo_pagos.md](modulo_pagos.md).*
