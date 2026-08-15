# Agrupador Mayorista

> Estado: en producción.

> Modelo de negocio de Adquirencia para entidades que agrupan a muchos comercios bajo una única relación comercial con Bind PSP. Ingesta de 5 Epics históricas de Notion (lote A5): Alta de entidades, ABM de canales de cobro, ABM de roles y usuarios, Mejora modelo agrupador, Parche agrupador mayorista.

## 0. El concepto de "Agrupador mayorista"

Una **entidad agrupadora mayorista** es una entidad que agrupa muchos comercios bajo su paraguas, pero cuyas cobranzas **no se liquidan comercio por comercio**: todo se liquida a un único CBU/CVU de la propia entidad mayorista, quien luego se encarga de liquidar (repartir) por su cuenta a sus comercios reales, típicamente por fuera de Bind PSP (efectivo, transferencia manual, etc.).

Esto genera dos necesidades estructurales que atraviesan todo este documento:
1. **La entidad necesita ver consolidado** lo que hoy solo existe por comercio (liquidaciones, transacciones).
2. **Los comercios de la entidad no deben ver información sensible de la liquidación con Bind** (comisiones, retenciones, importe neto) — porque esa liquidación es en realidad contra la entidad mayorista, no contra ellos.

### Caso real de referencia: BENAJAL S.A. (JONI)

Cliente real usado como caso de diseño (Discovery, no necesariamente 1:1 con lo implementado en el core genérico). BENAJAL tiene una red de comercios que no son propios (redes de ferias/mercados tipo Once, Flores, La Salada) a los que da la solución de cobro (POS/QR/RxT vía Portal Web), y una red de agencias propias de recaudación de impuestos y servicios.

Se plantearon dos variantes de modelo:
- **V1 (más restrictivo):** todos los comercios operan bajo el CUIT único de BENAJAL. Cada comercio tiene su propia CVU (todas a nombre de BENAJAL), pero **el comercio no puede operar esa CVU** — solo consultar transacciones/liquidaciones y ver el saldo como una "cuenta corriente". BENAJAL es quien opera todas las CVUs desde el Admin, y liquida a sus comercios por fuera (comprobante de débito en la CVU del comercio + comprobante de crédito en una CVU propia de BENAJAL).
- **V2 (modelo mayorista V2, more flexible):** todas las cobranzas se acreditan en una única CVU recaudadora de BENAJAL; BENAJAL transfiere internamente a la CVU asignada a cada comercio, y **el comercio sí puede operar su CVU** una vez fondeada (con roles y límites).

**Roles del modelo propuesto (jerarquía fija por comercio):**
| Rol | Puede | No puede |
|---|---|---|
| Administrador | Operar todos los canales de cobro, ver transacciones/liquidaciones, ver y operar la CVU (según permisos y topes), crear usuarios Supervisor/Operador | — |
| Supervisor | Operar canales de cobro de su sucursal, ver transacciones/liquidaciones de su sucursal, crear usuarios Operador | Ver/operar la CVU del comercio |
| Operador | Operar canales de cobro de su caja, ver historial de sus propias ventas | Ver liquidaciones, CVU, ni datos de otros usuarios |

Riesgo identificado y no resuelto del todo: **la responsabilidad regulatoria de una transferencia entre CVUs de distinta titularidad recae siempre en el PSP dueño de las cuentas** — dar acceso a un comercio real a una CVU titularidad de la entidad mayorista es un otorgamiento de acceso a un tercero no apoderado. Mitigante parcial (no elimina el riesgo): reglas de ARDID limitando montos/cantidad de transferencias salientes por día en esas CVUs, o exigiendo 2FA adicional.

---

## 1. Alta de entidades (mecánica general, reutilizada por todo el modelo agrupador)

La creación de una entidad agrupadora usa el mismo flujo genérico de alta de entidades de Adquirencia (ver [configuracion_entidades_y_comercios.md](index.md)), con estas piezas específicas desarrolladas para soportar el volumen de agrupadores:

- **Backend:** alta de entidad con todas sus configuraciones propias (datos básicos, impuestos, especificaciones: Siscri/Notificaciones/Access Management/CUIT duplicado/Ardid/organización wallet), más edición de Notificaciones/Flujo CUIT duplicado/Ardid.
- **Frontend:** grilla de visualización del detalle de especificaciones de la entidad y de sus comercios.
- **Sección Convenios y Reglas:** asignación de grupo de convenios y reglas de procesamiento con los que nacerán por herencia todos los comercios de la entidad (obligatorio elegir al menos un grupo de cada uno).
- Motivación explícita del PRD: el volumen de altas de comercios se disparó justamente por los **nuevos modelos agrupadores** que estaban iniciando servicios — de ahí la necesidad de una gestión de canales y roles más sólida (§2 y §3).

**Cluster de bugs detectado en el pase a Staging** (todos sobre el flujo de alta de entidad, encontrados en la Regresión épica de esta Epic):
- Al crear una entidad nueva, en Especificaciones desaparecieron las opciones de "Roles por defecto" (solo quedaba "Administrador mayorista" visible).
- Error al crear una entidad QR sin split: el campo "ID cuenta" solo dejaba seleccionar un valor fijo, y el selector de "Rol por defecto" se resetéaba solo a "AdministradorMayorista" después de un cartel de error.
- Al crear una entidad, a veces tira error en pantalla pero la entidad **igual se crea** (inconsistencia entre respuesta de API y estado real).

---

## 2. ABM de canales de cobro

### 2.1 Motivación y modelo de datos

PRD explícito: el equipo de integraciones/operaciones necesitaba poder habilitar, deshabilitar y cambiar condiciones del canal de cobro de un comercio **sin intervención manual de soporte**, justamente para escalar el alta de comercios que traen los modelos agrupadores.

Modelo de cascada de dos niveles:
- **`canal_entidad`**: configuración de canales por defecto a nivel Entidad (qué canales trae un comercio nuevo al crearse: QR con/sin split, POS con/sin arancel reducido y con qué merchant/site_id, Botón Simple con qué site_id, RxT).
- **`canal_comercio`**: la instancia real por comercio, que nace clonando lo que trae `canal_entidad` (salvo error, que queda registrado con motivo).

**Estados de un canal en un comercio:**
| Estado | Significado |
|---|---|
| Configurado | Canal habilitado y operativo |
| Pre-Configurado | Trae datos por defecto de la Entidad, pero requiere habilitación (a veces con datos extra particulares del comercio, ej. Botón Simple) |
| No Configurado | Sin datos ni habilitación |
| Configurado con Error | Falló la habilitación tras reintentos — requiere soporte para corregir datos y reintentar |

### 2.2 Habilitación de canales (por procesador)

- **QR**: determina con/sin split. Si PSP=184, siempre split=false (ignora lo que mande el Front). Si PSP≠184, respeta lo que venga. Al habilitar con split, se da de alta el CVU 164 correspondiente.
- **POS**: recibe opcionalmente `merchant_id` (GP) o `site_id` (Decidir); si no vienen, usa el valor por defecto de la Entidad (o error si tampoco lo tiene). Solo puede haber una habilitación de POS activa por comercio. Flujo real con GP: 1) alta de submerchant vía API Comercio, 2) crear sub-comercio, 3) guardar especificación tipo 32 en CardBusinessRules con el JSON de error si lo hay, 4) persistir en `dbo.CanalComercio`.
- **Botón Simple**: recibe opcionalmente `site_id` (Decidir), personalización de checkout (colores/logo) y caja de imputación de cobros (si no la manda, crea sucursal+caja "Boton simple" por defecto — son obligatorias para poder facturar la transacción, no es capricho de diseño).
- **RxT**: sin configuraciones adicionales más allá del `collector_id`.

### 2.3 Refactor mayor: desacoplar "habilitado" de la creación automática de QR

Bug de arquitectura de fondo, resuelto como US propia de alto riesgo: la sola creación/habilitación general de un comercio (`Comercios.Habilitado=1`) **no debe disparar nada relacionado a QR** (alta en Coelsa, CVU, suscripción DEBIN recurrente, split) si la Entidad no tiene QR configurado como canal por defecto. La creación automática de canales debe depender exclusivamente de `canal_entidad`, y las habilitaciones quedar registradas en `canal_comercio` (con campo de error para reintento si falla alguno).

### 2.4 Manejo de errores y reintentos

Patrón repetido para QR y POS: al fallar una habilitación, distinguir **error técnico interno** (reintentar automático, mostrar mensaje traducido con el dato causante) de **error externo/procesador** (reintentar hasta 3 veces, mensaje genérico de falla de servicio externo). Nuevo campo `[MensajeAmigable]` en `dbo.CanalComercio` y endpoint de reintento manual desde el Admin (botón "Reintentar" por canal).

### 2.5 Bugs de integración conocidos

- **Editar canal Botón Simple no actualiza `CardBusinessRulesDB.dbo.Especificacion`**: al cambiar el Id Procesador desde el Admin, el front tira error pero el cambio se aplica solo en `SharedComercioDB.dbo.CanalComercio`, dejando desincronizada la tabla de reglas de negocio que realmente usa el motor de pago — la transacción sigue cursando con el ID viejo.
- **Errores de alta en GP no se registran** (`AltaGP`/Merchant): la tabla de especificaciones queda con registros de otros comercios y errores genéricos ("Value cannot be null (Parameter 'source')") en vez del motivo real, salvo el caso de "Código Postal Inexistente" que sí se informa bien.
- **Comercio no sigue la regla de canal de la Entidad**: al configurar una Entidad con POS/QR/BS/RxT habilitados y crear un comercio nuevo, no queda ningún canal configurado en base — la tabla de especificaciones se llena con 5 registros de otros comercios con errores no relacionados al alta real.
- **Canal Botón Simple no se genera**: falla con "El campo CashCode es obligatorio" al intentar habilitarlo desde el Admin para un comercio.
- Validación floja: el campo Nombre/Apellido del responsable de Botón Simple admite solo números.
- Ticket de limpieza confirmado (Possumus, en desarrollo): el campo MerchantID en los formularios de configuración de canal POS ya no se usa (se selecciona automático según arancel reducido/no reducido) — se recomendó ocultarlo para evitar confusión de los operadores.

---

## 3. ABM de roles y usuarios — AccessManagement 2.0

### 3.1 Motivación

Con el modelo agrupador escalando, el modelo viejo de permisos (una fila de `Rol` por cada Organización, con permisos hardcodeados 1:1) se volvió insostenible: no había forma de estandarizar ni reutilizar roles entre entidades sin duplicar filas por cada una, y el ABM de usuarios/roles por comercio era manual (pedidos a soporte).

### 3.2 Modelo nuevo (AccessManagement 2.0)

Se separa **plantilla** (`RolTemplate` + `PermisoTemplate`, reutilizable) de **instancia** (`Rol`, uno por Entidad/aplicación, con flag `IsDefault`). Esquema relacional resultante:

```
Miembro (1:N) MiembroRol (N:1) Rol (N:1) Organizacion (Nivel 0 = Entidad)
Miembro (1:N) MiembroOrganizacion (N:1) Organizacion (Nivel 1/2/3 = Comercio/Sucursal/Caja)
```

Esto separa "a qué Organización pertenece el miembro" (`MiembroOrganizacion`, por nivel) de "qué Rol tiene" (`MiembroRol`, ligado a la Entidad/Nivel 0) — antes ambas cosas colapsaban en una sola fila de `Rol` por organización, generando repetición masiva.

**Piezas nuevas:**
- ABM de Roles por Entidad (sección "Gestión de Roles" en el Admin, solo visible para usuarios SUPERADMIN de Bind, nunca para entidades): crear/editar roles y sus permisos por Aplicación y Nivel jerárquico; **no permite eliminar** un rol, solo editar sus permisos.
- Roles **permitidos** vs. roles **por defecto** por Entidad: un rol por defecto es siempre uno permitido, pero no todo permitido es por defecto. Reemplaza la lógica vieja que guardaba el rol por defecto como una `EspecificacionTipo` bajo el grupo `ROLES_DEFECTO` en Comercio.
- ABM completo de usuarios (Miembros) por comercio desde el Admin: alta/edición/bloqueo/reseteo de contraseña, con recursividad para encontrar usuarios de sucursales y cajas.
- Spike + desarrollo "Aplicación por Defecto": AccessManagement soportaba una única aplicación hardcodeada (BFF); se generalizó para poder crear nuevas aplicaciones (ej. BFF2) con sus propios RolTemplate, de forma que el mismo motor de permisos sirva a Admin Centralizador, Portal Comercios, TIN/WICO y MPOS sin duplicar lógica.
- Migración completa "AccessManagement 2.0": migrar tablas Aplicacion/AplicacionConfiguracion/Miembro/Organizacion/Rol/MiembroRol/MiembroOrganizacion del modelo viejo al nuevo, incluyendo recursividad de Organización por Nivel y remapeo de Roles reutilizando plantillas donde un mismo Rol se repetía idéntico en todas las organizaciones hijas de un mismo Nivel/Aplicación.

> Fuente Jira (confirmación, IDEA [PRD-88](https://bindpsp.atlassian.net/browse/PRD-88), Epic [AD-7](https://bindpsp.atlassian.net/browse/AD-7)): la migración y el refactor de endpoints se completaron preservando compatibilidad con Portal Comercio, TIN/WICO y MPOS (endpoints con el mismo contrato pese al cambio de lógica interna). Delta nuevo: bug de login que no validaba si un miembro estaba dado de baja — solo validaba si estaba bloqueado por intentos fallidos (`bloqueadoHasta`), permitiendo el ingreso de usuarios ya dados de baja.

### 3.3 Jerarquía de roles del Portal Comercio (5 niveles fijos, propuesta discovery)

Administrador de Comercio → Encargado → Operador → Viewer → Soporte Técnico. Cada uno con visibilidad/acciones crecientes; ajustes de visibilidad configurables **por red de cliente corporativo**, no por usuario individual, para evitar excepciones que escalan mal. Un mismo usuario puede tener jerarquías distintas en comercios distintos, y funcionalidades distintas según el producto en el que esté operando (Portal vs. SmartPOS).

---

## 4. Ocultar información sensible a roles mayoristas

Necesidad puntual y recurrente del modelo agrupador: un usuario con rol "mayorista" (ej. `AdministradorMayorista`) no debe ver la información de **liquidación con Bind** de sus comercios, porque esa liquidación en rigor es contra la entidad mayorista.

**Rol nuevo:** `Admin comercio mayorista` — igual al Administrador de comercio estándar, pero sin acceso a las secciones Liquidaciones y Usuarios del Portal Comercio.

**Enfoque en dos etapas** (repetido varias veces en el histórico, por ejemplo para "Ocultar datos en portal a Roles Mayorista"):
1. **Parche rápido en Frontend**: lógica condicional hardcodeada por nombre de rol (`if rol == "AdministradorMayorista"`) que oculta secciones/campos puntuales (Inicio: "Tus Datos"/"Saldo"; Transacciones: "Total Retenciones", "Comisión", "Fecha Liquidación", "Total Neto"; export CSV: "Comisión", "IVA Comisión", "Retenciones/Percepciones", "Importe Neto") — pedido explícito del equipo técnico como solución de corto plazo.
2. **Backend con permisos reales**: se registran como `Permiso` formales ligados al rol en AccessManagement, y el Frontend se refactoriza para consultar permisos en vez de comparar el nombre del rol — más flexible pero requiere haber migrado a AccessManagement 2.0 (§3). Al menos dos de estas tareas de "etapa 2" quedaron **canceladas** en el histórico (probablemente absorbidas por la migración general de AccessManagement).

Bugs encontrados durante estas restricciones:
- El comprobante de una transacción le mostraba al rol mayorista el **importe neto** en vez del **importe bruto** (mostrar el neto filtra indirectamente cuál fue la comisión/retención, que es justo el dato que se quería ocultar).
- No aparecía el nombre de fantasía del comercio en el inicio del Portal ni en el usuario — feedback directo de demo con el cliente.

---

## 5. Reporte consolidado de liquidaciones a nivel Entidad

Para que la entidad agrupadora no tenga que filtrar liquidación por liquidación comercio por comercio, se construyó una vista consolidada ("ADMIN-Reporte Maestro de Liquidaciones por Comercio"), en 3 partes:

1. **Modificación de `dbo.Liquidacion`** (PaymentAcceptorRendicionDB): se agregaron los campos `CodigoEntidad` y `CuitCuilComercio` (bug de nombramiento detectado en QA: el campo se llamó primero solo `Cuit`, se corrigió a `CuitCuilComercio` para evitar ambigüedad). Se modificaron **todos** los procesos de liquidación existentes (QR, RxT, POS, BS) para completar estos campos, más script de backfill sobre liquidaciones históricas. Marcado como tarea bloqueante de la que dependían las otras dos partes.
2. **Reporte CSV vía Report Manager**: nuevo tipo de reporte filtrable por rango de fecha de liquidación y CUIT/CUIL de comercio (o todos), a nivel Entidad.
3. **Grilla de liquidaciones a nivel Entidad**: nueva sección "Liquidaciones de comercios" en el Admin, con descarga de PDF por liquidación, filtros y paginación — mismo patrón que la liquidación por comercio existente pero agregada por `CodigoEntidad`.

Pedido puntual de un cliente real (Desarrollos del Litoral): que su export CSV de Transacciones no incluya Comisión/IVA Comisión/Retenciones-Percepciones/Importe Neto — resuelto primero con un parche de Frontend condicional por entidad, y luego con un tipo de reporte "Transacciones Restringido" separado en Report Manager que directamente no incluye esos campos (evita que la restricción dependa de lógica de Frontend).

---

## 6. Bug recurrente de fondo: manejo de timezone en fecha de liquidación

Patrón que aparece **dos veces independientes** en el histórico de este modelo (no es un bug puntual, es una fragilidad de diseño): el campo `FechaProceso` de una liquidación a veces queda persistido en `-03:00` (hora Argentina) en vez de UTC, lo que corre mal el cálculo de fecha de liquidación:

- **Liquidaciones de fin de semana se calculan mal**: sábado y domingo deberían liquidar el miércoles (plazo 48hs desde el lunes), pero al tener `FechaProceso` en `-03:00` en vez de UTC, el sistema calculaba mal y las liquidaba el martes.
- **BOTONLIQ con cantidad de transacciones incorrecta**: la cantidad de tx en el archivo de liquidación (`botonliq`) no coincidía con la liquidación real, por la misma causa raíz de manejo de TZ -03:00 — con nota explícita de que "no se arregló como habíamos convenido" (regresión de un fix anterior).

Para cualquier desarrollo futuro que toque `FechaProceso`/fechas de liquidación: verificar explícitamente que se persista y compare siempre en UTC, no en hora local Argentina.

---

## 7. Mejoras operativas y de portal marca blanca (menores, sin aprendizaje técnico adicional)

Bolsa de ~35 tickets pequeños (S/M, mayormente sin ticket de aprendizaje) de mejora incremental del Admin/Portal en el contexto del modelo agrupador — filtros y columnas nuevas en la grilla de Transacciones (fecha, sucursal, caja, comercio, procesador, medio de pago, canal, ID Coelsa, ID Orden Venta QR), personalización de portal marca blanca (logo, "accent color" parametrizable por entidad, footer "Powered by Bind Pagos"), UX/UI de POS marca blanca, generador de templates de mail de usuario de portal, y un onboarding marca blanca dedicado para Sur Finanzas (validaciones AFIP/UIF/Worldsys/Renaper, prueba de vida Addalia, sin alta bancaria — ver también [transversal/sur_finanzas.md](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md)). Detalle completo en Notion si se necesita precedente puntual de alguno.

Dos piezas de mayor porte dentro de este mismo lote:
- **Reglas de pago administrables desde el Admin (Botón Simple)**: antes las reglas de pago (grupos de convenio/comisión) se gestionaban solo por script/soporte; se armó ABM completo (back + front) para crearlas y asignarlas desde el Admin.
- **Perfil "solo lectura" para entidad en el Admin** y **perfiles a nivel sucursal** — extensiones del modelo de roles pedidas puntualmente por clientes agrupadores.

---
*Ver también: [configuracion_entidades_y_comercios.md](index.md) para el flujo genérico de alta de entidad/comercio que este modelo reutiliza, y [liquidaciones_y_devoluciones.md](devoluciones_y_contracargos.md) para la mecánica general de liquidación.*
