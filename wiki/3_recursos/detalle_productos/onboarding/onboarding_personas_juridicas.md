# Onboarding de Personas Jurídicas (OB PJ MVP)

> Estado: en producción.

> Contenido destilado de la Epic de Notion "OB Personas Jurídicas MVP" (91 tickets — la Epic con más tickets de todo el grupo Onboarding). Triage no exhaustivo por volumen: la gran mayoría son bugs puntuales de UX/validación de un mismo formulario, agrupados temáticamente en vez de listados uno por uno.

## 1. Qué es y cómo funciona

Flujo de alta de cuenta para personas jurídicas (sociedades) sobre la base del onboarding de personas físicas ya existente: cada representante legal/apoderado de la sociedad debe completar primero su propio OB de Persona Física (PF), y solo cuando al menos uno de esos OB de PF es aprobado, la solicitud de Persona Jurídica (PJ) puede avanzar. Esta dependencia PJ↔PF fue fuente de varios bugs de sincronización de estado (ver §4).

- **Documentación requerida variable por tipo de sociedad**: SA, SRL, SAS, S.C.A. (Sociedad en Comandita por Acciones), S.H. (Sociedad de Hecho), ASOC (Asociación) y FUND (Fundación) tienen combinaciones distintas de documentos obligatorios (estatuto/contrato social, actas de designación de autoridades, poderes generales amplios para apoderados, etc.) — la lista completa se relevó incorrecta varias veces durante el desarrollo (documentos faltantes para SAS, para SA/SRL/SCA, duplicados para ASOC/FUND).
- **Flujos de cumplimiento normativo**: control de listas de Terrorista/PEP/Sujeto Obligado (SO) para PJ y PF, carga de **Beneficiarios Finales** (personas físicas dueñas/controlantes de la sociedad) y **Propietarios Directos**, con validaciones específicas para cada paso.
- **Backoffice (BO) de Persona Jurídica**: permite contactar a cualquiera de los representantes legales/apoderados (no solo a quien inició la solicitud) para pedir documentación faltante, identificar en el listado quién es Representante Legal vs. Apoderado, y agregar/eliminar representantes directamente desde BO.
- **Regla de reintento de alta**: originalmente, si un CUIT/CUIL ya tenía un alta exitosa, no se permitía reintentar el alta durante 365 días. A pedido del cliente se evaluó reducir esa ventana a 1 día — con el riesgo explícito de que muchas sociedades reintenten el alta sin necesidad, y la mitigación propuesta de que un validador manual (equipo "La Virginia") revise si el reintento es genuino.
- **Notificación a oficiales de sucursal** (cliente La Virginia): al cambiar de estado una solicitud de onboarding de comercio, se dispara un email al oficial de sucursal correspondiente — el vínculo solicitud↔sucursal↔oficial se resuelve por **ID Cliente SAP**, con la casilla de cada oficial parametrizada en una tabla de configuración (sin notificación cruzada entre sucursales). Estados cubiertos: Pendiente, Pendiente Revisión Oficial de Negocio, Pendiente Representante Legal, Aprobada, Rechazada, Error en alta, Validación manual.

## 2. Cluster de bugs de validación de campos

La mayoría del backlog son bugs de validación de formulario, agrupables en:
- **Falta de validación de formato/longitud**: "Documento del representante" no valida cantidad de caracteres ni duplicados, teléfono no valida formato, Código Postal acepta caracteres no numéricos, Razón Social sin límites de longitud (mínimo 5 / máximo 41), "Número de documento" no acepta letras aunque el tipo "Pasaporte" las requiere.
- **Dropdowns con datos incorrectos**: "Ciudad de Buenos Aires" aparece duplicada en Provincia (una de las dos sin listado de localidades), listado de tipos de sociedad incompleto, listado de códigos postales/localidades/provincias sin validar contra un catálogo real.
- **Mensajes de error genéricos o incorrectos**: al presionar "Siguiente" sin completar datos, al no leer bien un DNI, al eliminar un documento — en varios casos el mensaje no orientaba al usuario sobre qué corregir.

## 3. Cluster de bugs de documentación adjunta

- No se indicaba qué documentos eran obligatorios vs. opcionales, ni el formato/peso de archivo esperado.
- Un documento marcado "en caso de corresponder" (aparentando opcional) era en realidad siempre obligatorio, en más de un caso (Acta de designación de autoridades, Poder general amplio).
- Al haber documentos opcionales en el set, el sistema exigía la carga de *todos* ellos en vez de solo los obligatorios.
- Los documentos cargados no se visualizaban por nombre en el Backoffice, y el nombre de sección no coincidía con lo pedido en la historia de usuario (ej. debía decir "Beneficiario Final", no otra cosa).

## 4. Cluster de bugs de sincronización PJ↔PF y flujos de cumplimiento

- Si algún OB de PF de un representante quedaba rechazado, la solicitud de PJ quedaba bloqueada en estado "Pendiente Representante Legal" sin salida.
- La solicitud de PJ no pasaba a "Aprobada" aun cuando al menos un representante legal/apoderado ya estaba aprobado (la regla de negocio pedía "al menos uno", la implementación exigía todos).
- El listado de representantes legales de una solicitud PJ no se mostraba hasta que completaran su OB de PF.
- No se validaba que el DNI ingresado en el flujo jurídico coincidiera con el DNI real del OB de PF del representante.
- Bugs específicos de los flujos de Beneficiario Final y Propietario Directo: el usuario podía continuar sin marcar ninguna casilla de Beneficiario Final, el campo "Razón Social" estaba mal definido en ambos pasos, y el comportamiento general del flujo de Propietarios Directos no coincidía con lo especificado.
- No se le notificaba al oficial de negocio cuando un usuario respondía con la documentación pedida vía BO; y no llegaba el email al representante legal/apoderado para hacer su OB de PF en algunos casos.

## 5. Otros aprendizajes

- **Firma conjunta de contrato**: evaluada, finalmente cancelada.
- **Envío de contrato firmado**: deshabilitado del flujo (dejó de requerirse).
- **QR en el email al representante legal**: para poder completar el OB de PF desde el celular sin re-tipear la URL.
- **Encriptación de datos personales**: tratada como US propia dentro del grupo Onboarding, coherente con el estándar de cumplimiento del resto de los onboardings de Bind PSP (ver también [onboarding_bind_sucursal.md](onboarding_bind_sucursal.md)).

## 6. Incidentes en producción y versiones de publicación (vía `/sync_releases`)

> Fuente: Jira `bindpsp.atlassian.net`, espacio OB, versiones **OB Jurídico V1.7** (2026-02-20) a **OB PJ 1.7.2** (2026-06-17). Backfill vía export XML, 2026-07-13. La mayoría son incidentes SOPORTE del cliente **La Virginia** (y uno de **Octagon**) que confirman en producción los clusters conceptuales de §2-§4.

- **OB Jurídico V1.7** (2026-02-20): [OB-71](https://bindpsp.atlassian.net/browse/OB-71) — errores varios en el backoffice de onboarding PJ para La Virginia.
- **OB Jurídico V1.7 1 HF** (2026-04-06): [OB-111](https://bindpsp.atlassian.net/browse/OB-111) — error en alta de OB PJ para el cliente Octagon.
- **OB Jurídico V1.7.1** (2026-05-21, 11 tickets — la tanda más grande de incidentes de producción): [OB-145](https://bindpsp.atlassian.net/browse/OB-145) (solicitud queda en estado "a revisar"), [OB-142](https://bindpsp.atlassian.net/browse/OB-142) (no se puede restablecer la clave del portal), [OB-132](https://bindpsp.atlassian.net/browse/OB-132)/[OB-130](https://bindpsp.atlassian.net/browse/OB-130) (error de alta de representante legal por caracteres numéricos en el trámite), [OB-127](https://bindpsp.atlassian.net/browse/OB-127) (superposición de "Ninguna de las anteriores" en la declaración de PF — cluster §2), [OB-123](https://bindpsp.atlassian.net/browse/OB-123) (no permite subir más de 1 documento por beneficiario final — cluster §3), [OB-122](https://bindpsp.atlassian.net/browse/OB-122) (error al cargar DNI manual en flujo PF), [OB-102](https://bindpsp.atlassian.net/browse/OB-102) (domicilio comercial con "S/N" en Número rompe el alta — cluster §2), [OB-100](https://bindpsp.atlassian.net/browse/OB-100) (Razón Social obligatoria — cluster §4), [OB-98](https://bindpsp.atlassian.net/browse/OB-98) (error al final del proceso de OB PJ), [OB-83](https://bindpsp.atlassian.net/browse/OB-83) (error en campo telefónico de OB Persona Física — cluster §2).
- **OB PJ 1.7.2** (2026-06-17, 10 tickets — mejoras post-estabilización, ya no solo bugs de La Virginia): sugerencia de Gmail en campo email (OB-156), alerta sobre Representante Legal en pantalla de BO (OB-154), renombrar validación en Entidad (OB-153), agregar CUIT de empresa relacionada al RL (OB-152), cambiar estado de solicitudes vencidas a "Vencida" (OB-150), flujo de RL/Apoderado sin modal en iPhone (OB-139/138), teclado alfanumérico habilitado para OTP (OB-137), ícono de cámara mal posicionado en Selfie (OB-136), error de datos al clickear otra opción — La Virginia (OB-144).

## 7. Flujo AS-IS paso a paso (Front + BO), documentación operativa La Virginia

> Fuente: página Notion "Onboarding Jurídico" (`Docs`, Tipo "Capacitación interna", última edición 2026-07-02) — manual con capturas de pantalla del flujo tal como corre hoy en Staging para La Virginia. Motivado por el rediseño de flujo del [proyecto La Virginia — OB PJ](../../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md) (2026-08-06): necesario documentar el AS-IS exacto antes de decidir qué mínimo hay que tocar.
>
> **Nota:** los pasos son reordenables — Backoffice permite a cada entidad configurar el orden del paso a paso de su propia solicitud (mismo mecanismo de "flujo por entidad" ya documentado en [`arquitectura_solicitud_y_flujos.md §2`](arquitectura_solicitud_y_flujos.md#2-configuración-por-flujoentidad)). Lo que sigue es el orden configurado hoy para La Virginia.

### 7.1 Registro de la Persona Jurídica (Front, autogestionado hoy por el cliente final)

| Paso | Contenido |
|---|---|
| 1 | Aceptación de Términos y Condiciones — único contenido del paso, inicia el flujo. |
| 2 | Datos básicos: Razón Social, Email, Confirmar Email, CUIT, tipo de sociedad (lista predefinida, selección única). El tipo de sociedad elegido determina qué documentación respaldatoria se pide después. |
| 3 | Carga de documentación respaldatoria según tipo de sociedad — mezcla de obligatoria y opcional; un mensaje en pantalla indica tipo y tamaño de archivo aceptado. |
| 4 | DDJJ de Propietarios Directos — checkbox: si se marca "no tiene", no pide más datos; si se marca "sí tiene", exige cargar todos los propietarios directos (tantos como sean necesarios) pero solo permite **1 documento respaldatorio para todos los propietarios cargados en conjunto**. |
| 5 | DDJJ de Beneficiarios Finales — misma mecánica de checkbox que el paso 4, pero acá si permite **1 documento por cada beneficiario final** (no uno solo para todos). |
| 6 | Domicilio fiscal — carga manual; Provincia actualiza el listado de Localidades: elegir Localidad autocompleta Código Postal. |
| 7 | Domicilio comercial — carga manual, con checkbox para autocompletar con los datos del domicilio fiscal si coinciden. |
| 8 | Verificación de teléfono de contacto — OTP por SMS; solo acepta dígitos con la longitud esperada; reenvío habilitado a los 120 segundos; se puede volver atrás para cambiar el número. |
| 9 | Alta de Representantes Legales/Apoderados — DNI y email de cada uno, **no editables una vez cargados**; ahí se dispara luego el link de OB de Persona Física de cada uno. Se pueden cargar tantos RL/Apoderados como se necesiten. |
| 10 | Declaración final (PEP/OCDE/FATCA/Sujeto Obligado) — "Sujeto Obligado" exige documentación respaldatoria; OCDE y FATCA no; "Ninguna de las anteriores" bloquea las demás opciones. |
| 11 | Fin del registro de Persona Jurídica. |

### 7.2 Estados de la solicitud PJ en Backoffice y transiciones

| Estado | Significado / disparador |
|---|---|
| **Pendiente** | Recién iniciado el registro. Si el cliente abandona a mitad de camino, **no se puede retomar** — debe reiniciar desde cero. No se pueden eliminar solicitudes en este estado. |
| **Pendiente Revisión Oficial de Negocio** | El registro de PJ se completó; el oficial de negocio del cliente debe revisar la documentación y aprobar o rechazar. |
| **Pendiente Representante Legal** | La solicitud de PJ fue aprobada por el oficial de negocio → dispara los emails de OB de Persona Física a cada RL/Apoderado. Cuando uno de esos OB de PF se aprueba, la PJ pasa a Aprobada. |
| **Aprobado a Revisar** | La PJ fue aprobada (wallet + comercio ya dados de alta) pero falló el envío del webhook final al cliente. |
| **Aprobada** | Se da por aprobada cuando se completa el OB de PF de un Representante Legal — dispara alta de wallet y comercio, habilitando a la PJ para operar. |
| **Error de Alta** | Falló el alta de wallet o comercio — revisar la respuesta de los servicios involucrados para el motivo; el alta es reintentable. |
| **Vencida** | Se cumplió el plazo configurado por la entidad sin terminar el alta — hay que reiniciar todo el proceso. |
| **Rechazada** | El oficial de negocio rechaza por falta de documentación o datos incorrectos — hay que reiniciar todo el proceso. |

Desde Backoffice se puede **contactar al cliente** (email solicitando documentación faltante/complementaria) y, de forma independiente, **contactar al RL/Apoderado** una vez que su propio OB de PF ya se inició (estado distinto de "No Iniciado").

### 7.3 Relación con el OB de Persona Física del representante

Cada Representante Legal/Apoderado cargado en el paso 9 completa su propio flujo estándar de OB de Persona Física (mismo flujo genérico documentado en `manuales_operativos.md §1`, no un flujo distinto para PJ) a partir del link recibido por email. Solo cuando al menos uno de esos OB de PF se aprueba, la solicitud de PJ pasa a Aprobada (ver §7.2, y el cluster de bugs históricos de esta dependencia en §4 más arriba).

### 7.4 Modelo del webhook final — solicitud PF de representante aprobada

Confirma la mecánica ya documentada en `manuales_operativos.md §1` (misma forma de solicitud que el ejemplo de PF individual) — el payload trae el **CUIT/razón social de la persona jurídica** (`nombres`, `cuil`) junto con los datos de cuenta creados (`Cuenta.IdCuenta`, `Cuenta.Cvu`), no los datos personales del representante que completó el OB — el representante es quien dispara la aprobación, pero la cuenta que se crea es la de la PJ.

## 8. Demo end-to-end a un cliente: consola del oficial de cumplimiento y potencial de marca blanca

> Fuente: reunión "Demo ON BOARDING propio - Octagon" (2026-08-19) — demo completa del flujo a Octagon (cliente en producción/integración evolutiva) y al equipo de Compliance de Banco Industrial (banco vinculado a la operatoria de Octagon).

**Flujo de alta demostrado (front, persona jurídica):**
1. Registro con CUIT/CUIL, validado automáticamente contra los servicios web de ARCA (inscripto y activo).
2. Carga de documentación societaria (estatutos, DNI del representante legal, acta de designación de autoridades) — la plataforma usa IA para extraer automáticamente los datos de estos archivos; el cliente puede revisar y reemplazar un documento si la carga fue incorrecta.
3. Alta de beneficiarios finales, con documento de identidad vía IA y validación de que la suma de porcentajes de participación cierre en 100%.
4. Verificación biométrica de los firmantes: escaneo de DNI (frente/dorso) + prueba de vida (liveness), con tecnología de **Neurotecnology**, validando identidad contra Renaper.

**Consola del oficial de cumplimiento (admin), demostrada en esta sesión:**
- Cola de casos con resumen de la estructura societaria.
- Barrido automático inicial contra listas de sanciones: **OFAC, ONU, UIF, Repet, PEP**.
- Revisión documento por documento, con aprobación/rechazo individual y posibilidad de pedir aclaraciones/documentación adicional al cliente (ida y vuelta con notificación).
- KYC completado por el oficial con tipo de cliente, volúmenes anuales y origen de fondos — el sistema calcula una matriz de riesgo/alertas en base a reglas de negocio configuradas, ajustable según la operación.
- Configuración de políticas internas por entidad: reglas de negocio parametrizables (ej. prohibir industrias específicas o estructuras societarias complejas) que aprueban, rechazan o alertan automáticamente según los criterios definidos.
- Trazabilidad/auditoría completa desde el inicio de la solicitud hasta el veredicto final (todo cambio, aprobación, rechazo u observación queda registrado).

**Pedido de acceso de Compliance de Banco Industrial:** el equipo de Compliance de Banco Industrial pidió acceso directo a la plataforma para auditar el legajo digital sin tener que solicitar documentos manualmente — Bind acordó otorgarlo.

**Integración técnica pendiente de definir:** se acordó definir un "paquete de datos" para automatizar, una vez aprobada la solicitud de onboarding, la creación de la CBU y el alta del comercio en los sistemas de Bind (hoy manual). Aunque hoy pueden usarse los endpoints actuales para el alta directa, en los próximos meses habrá que migrar a nuevos endpoints por requerimientos normativos internos — descrito como un cambio administrativo, no traumático para el cliente (sin mayor detalle técnico todavía).

**Potencial como producto externo (marca blanca):** se discutió explícitamente que el núcleo de esta solución de onboarding es modular y podría configurarse como producto adaptable para clientes externos, no solo para uso interno de Bind — ver oportunidad OP-009 en [`2_areas/direccion/oportunidades.md`](../../../2_areas/direccion/oportunidades.md). Consistente con la propuesta ya documentada del proveedor Fintexa/Soluciones Andinas en [`propuesta_fintexa_onboarding_juridico.md`](propuesta_fintexa_onboarding_juridico.md) (plantilla genérica ya nombrada para otros clientes, ej. "Banco Julio"/"Banco Coinag").

---
*Última actualización: 2026-08-19 — nueva §8 (demo end-to-end a Octagon/Banco Industrial: consola de cumplimiento y potencial de marca blanca).*
*Última actualización anterior: 2026-08-06 — nueva §7 (flujo AS-IS paso a paso Front+BO, desde la página Notion "Onboarding Jurídico") a pedido del proyecto [La Virginia — OB PJ](../../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md).*
*Última actualización anterior: Fuente: Notion histórico, Epic "OB Personas Jurídicas MVP" (91 tickets) — ingesta 2026-07-06. §6: backfill `/sync_releases` vía export XML, 2026-07-13.*
