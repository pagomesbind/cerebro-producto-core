# Ardid/Akurtech — Blacklist/Whitelist y Ráfagas

> Estado: en producción.

> Fuente: `Akurtech 6 - Blacklist - Ráfagas.pdf` (36 páginas), guía funcional oficial del proveedor. Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general.

## 1. Whitelist y Blacklist — permisos y alcance

Los **Permisos de Lista Negra y Lista Blanca** otorgan a los usuarios la facultad de agregar los siguientes tipos de entidad:

| Tipo de entidad |
|---|
| Identificación |
| Dispositivo |
| Cuenta |
| IP |
| Correo |
| Dominio de Email |
| Geolocalización |
| Tarjeta |
| Comercio |

Quien tenga estos permisos puede: **cargar** datos (a Lista Negra o Lista Blanca), **convertir** un dato de una lista a la opuesta (y viceversa), **editar** y **eliminar**.

Se crean **por entidad** y se pueden aplicar a **Transferencias** y a **Transacciones (Pagos)**. Acceso desde el margen izquierdo de la pantalla.

## 2. Configuración por tipo de dato

| Card | Botón de alta | Dato requerido | Notas |
|---|---|---|---|
| **Identificación** | Agregar Identificación | Número de CUIT + lista (whitelist/blacklist) | CUIT válido = whitelist; inválido/sospechoso = blacklist |
| **Dispositivo** | Agregar dispositivo | "Id del dispositivo" + lista | Confiable = whitelist; sospechoso = blacklist |
| **Cuenta** | Agregar cuenta | "Alias" + CBU o CVU (según cuál esté registrado) | Válida = whitelist; sospechosa = blacklist |
| **IP** | Agregar IP | Número de IP + lista | Conocida = whitelist; sospechosa = blacklist |
| **Correo** | Agregar correo | Correo + lista | Válido = whitelist; sospechoso/inválido/temporal = blacklist. **Permite además cargar patrones** a la blacklist, con parámetros opcionales: longitud mínima, longitud máxima, caracteres especiales |
| **Dominio de correo** | Agregar dominio de correo | Dominio de e-mail + lista | Conocido = whitelist; inválido/sospechoso/temporal = blacklist |
| **Geolocalización** | Agregar geolocalización | País + lista | Válido = whitelist; sospechoso = blacklist |
| **Tarjeta** | Agregar tarjetas | HASH o PAN de la tarjeta + lista | Conocida = whitelist; sospechosa = blacklist |
| **Comercio** | Agregar blacklist/whitelist Comercio | ID del comercio + lista | Conocido = whitelist; sospechoso = blacklist |

Todas las cards permiten **eliminar** o **cambiar de lista** el registro.

## 3. Carga masiva (todas las cards)

Mecanismo idéntico en las nueve cards: permite importar datos vía archivo **CSV** para insertar múltiples registros de una sola vez.

Flujo: clic en el botón de carga masiva → modal → **"Descargar ayuda de formato"** (CSV con instrucciones) → **"Descargar ejemplo"** (CSV de ejemplo) → subir archivo con formato correcto → botón **Aceptar** → confirmación. Ver también la API equivalente `/Blacklist/UploadBlackList` en [apis_externas.md](apis_externas.md#15e-uploadblacklist-post--post-apiblacklistuploadblacklist).

## 4. Novedades (dashboard de Blacklist/Whitelist)

Sección **Novedades**, visible en el dashboard dentro de blacklist y whitelist. Los datos se cargan directamente desde Akurtech mediante un script, provenientes de bases de datos actualizadas ya comprobadas como fraudulentas — este flujo corresponde al conector **Worldsys** documentado en [configuracion_inicial.md](configuracion_inicial.md#3-parametrías-generales), parámetro 3.1.12.

| Acción | Alcance | Descripción |
|---|---|---|
| **Rechazar** | Individual por blacklist | Botón que rechaza todos los datos insertados en esa lista pendiente |
| **Consulta** | Individual por blacklist | Abre modal con los valores correspondientes a la lista; dentro del modal se puede aprobar/rechazar todas, o individualmente |
| **Aprobar todas** | General, para todos los valores de la lista | Agrega automáticamente todos los valores mostrados en Novedades a la blacklist |
| **Ver todas** | General | Abre modal con la lista completa; permite aprobar todas en general, o individualmente desde la columna Acciones |

## 5. Ráfagas — definición general

> "Son procesos automáticos y configurables diseñados para evaluar grandes volúmenes de datos en tiempo real o en análisis histórico. Estas evaluaciones tienen como objetivo identificar patrones sospechosos de fraude o comportamiento anómalo en las transacciones, actividades de usuarios o eventos que ocurren dentro de un sistema."

Se pueden pensar como **alertas personalizables o triggers automáticos** que el sistema dispara al detectar ciertos eventos o patrones previamente definidos.

**Configuración común a todas las ráfagas:** columna **"Habilitada"** (switch) en el listado lateral izquierdo, para activar/desactivar cada regla de ráfaga; panel derecho con configuración parametrizable al seleccionar una ráfaga; se guarda con el botón **"Guardar"**.

## 6. Ráfagas de Transferencias

### 6.1. Ráfagas de transferencias Entrantes

Monitorean flujos de dinero que llegan a una cuenta desde fuentes externas; indicador potencial de fraude, lavado de dinero, financiamiento ilícito o errores operativos.

| Subtipo | Definición |
|---|---|
| **Ráfagas desde el mismo originante** | Un único remitente realiza múltiples transacciones hacia el mismo destinatario o diferentes cuentas en período corto |
| **Ráfagas desde el mismo originante según el importe** | Detecta transacciones repetitivas/acumulativas de un originante, analizando específicamente los montos |
| **Ráfagas desde el mismo originante al mismo destinatario** | Un originante realiza múltiples transacciones consecutivas hacia la misma cuenta destinataria en período corto |
| **Ráfagas hacia un mismo beneficiario** | Múltiples originantes transfieren a un mismo beneficiario en período corto |
| **Ráfagas de monto acumulado diario** | Monitorea el monto total transaccionado (enviado o recibido) por usuario/cuenta/entidad en 24 horas; se activa si el acumulado excede un umbral predefinido o es anómalo vs. histórico |
| **Ráfagas consecutivas desde el mismo originante con monto acumulado diario** | Un mismo originante realiza transferencias consecutivas (o en período corto) cuyo monto acumulado diario supera un límite o es anómalo |
| **Ráfagas diarias idénticas desde el mismo originante** | Un mismo originante realiza transferencias con características idénticas (monto, destinatario o frecuencia) en un solo día |

### 6.2. Ráfagas de transferencias Salientes

Patrones donde un mismo originante realiza múltiples transferencias salientes (a uno o varios destinatarios) en período corto o dentro de un día.

| Subtipo | Definición |
|---|---|
| **Ráfagas de transferencias a un mismo destinatario** | Un mismo destinatario recibe múltiples transferencias en período corto o en un día, de uno o varios originantes |
| **Ráfagas de transferencias a un mismo IP de origen** | Múltiples transacciones/eventos (transferencias, logins, pagos, solicitudes, etc.) asociados a una misma IP en período corto |
| **Ráfagas de transferencias desde un mismo originante** | Un mismo originante realiza múltiples transferencias en período corto. **Configurable por: segmentación, cantidad de transferencias, tiempo, monto mínimo, y acción a realizar.** Se pueden configurar varias reglas de este tipo |
| **Ráfagas hacia el mismo beneficiario** | Un mismo beneficiario recibe múltiples transferencias en período corto o en un solo día |
| **Ráfagas diarias idénticas al mismo beneficiario** | Un mismo beneficiario recibe múltiples transferencias con el **mismo monto** en período corto o en un solo día |

## 7. Ráfagas de Login

| Subtipo | Definición |
|---|---|
| **Ráfagas de login desde un mismo dispositivo** | Un único dispositivo (identificado por ID de dispositivo, huella digital del navegador, o identificador único) realiza múltiples intentos de login en período corto |

## 8. Ráfagas de Pagos

Patrones donde un mismo originante realiza múltiples pagos consecutivos o en período corto, con características repetitivas (montos similares, destino idéntico, frecuencia anormalmente alta), dirigidos a uno o varios destinatarios.

| Subtipo | Definición |
|---|---|
| **Ráfagas de devolución a un mismo comercio** | Un mismo comercio recibe múltiples devoluciones de dinero en período corto o en un día, de uno o varios usuarios/cuentas |
| **Ráfagas de pagos rechazados a un mismo dispositivo** | Un único dispositivo genera múltiples intentos de pago fallidos/rechazados en período corto |
| **Ráfagas de pagos rechazados a un mismo IP** | Múltiples intentos de pago fallidos/rechazados desde una misma IP en período corto |
| **Ráfagas de pagos rechazados a un mismo email** | Múltiples intentos de pago fallidos/rechazados asociados a un mismo correo electrónico en período corto |
| **Ráfagas de pagos rechazados a un mismo comercio** | Un comercio recibe múltiples intentos de pago fallidos/rechazados en período corto |

## 9. Configuración de umbrales

La fuente documenta explícitamente umbrales/parámetros configurables solo para el subtipo **"Ráfagas de transferencias desde un mismo originante"** (§6.2): **segmentación, cantidad de transferencias, tiempo, monto mínimo, y acción a realizar**.

Para el resto de los subtipos de ráfaga (transferencias entrantes, hacia beneficiario, login, pagos), el texto describe la **definición conceptual** de cada patrón pero no detalla explícitamente los campos/umbrales concretos del formulario de configuración más allá del switch "Habilitada" y el botón "Guardar" genéricos.

## 10. Interacción entre Blacklist, Ráfagas y Reglas de Pagos/Transferencias/Login

- Las **Reglas Reputacionales** y **Reglas Machine Learning** de Pagos/Transferencias/Login **toman sus datos de las Blacklist/Whitelist**: si un dato (tarjeta, IP, dispositivo, identificación, etc.) no está cargado en alguna de las listas, el control reputacional correspondiente no se ejecuta. Esto conecta directamente los nueve tipos de entidad de la sección 2 con el scoring reputacional documentado en [scoring.md](scoring.md).
- Las **Ráfagas** se aplican como triggers automáticos independientes sobre Transferencias, Login y Pagos, evaluando volúmenes y patrones en tiempo real o histórico.
- Tanto blacklist/whitelist como ráfagas se **crean por entidad** y se aplican a Transferencias y Transacciones (Pagos); las ráfagas de login son la única categoría exclusiva de sesión/autenticación, no de movimiento de fondos.
- El texto no detalla explícitamente el mecanismo técnico de cómo el resultado de una ráfaga se combina con el resultado de una regla estándar/reputacional/ML/comportamental de pagos (por ejemplo, si también aplica la lógica de "acción más restrictiva" descrita en [scoring.md](scoring.md)) — la integración puntual entre el módulo de Ráfagas y el módulo de Reglas no se explicita en la fuente; solo se infiere la conexión con Blacklist/Whitelist.

---
*Ver también: [modulo_transferencias.md](modulo_transferencias.md#53-reglas-reputacionales), [modulo_pagos.md](modulo_pagos.md#9-reglas-de-pago--reglas-reputacionales) y [modulo_login.md](modulo_login.md#3-reglas-reputacionales--login) para cómo cada módulo consume estos datos, y [apis_externas.md](apis_externas.md#15-api-blacklist-incluye-submódulo-commerce) para las APIs de gestión de blacklist.*
