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

### 8.1 Detalle funcional real de la consola de referencia — "AVA Compliance" (2026-09-18)

> Fuente: sesión `/idea_solution` sobre `revision_pj_cumplimiento` — exploración en vivo del ambiente de staging del proveedor externo (caso real de prueba, producto internamente llamado "AVA Compliance"/"AVA Onboarding", accedido en `avaonboarding.adfcloudia.com/compliance`) + revisión completa de la grabación de la demo del 2026-08-19 ya citada en §8.

**Estructura de la consola (pantalla de detalle de un caso):** 5 pestañas — Resumen, Documentos, KYC, Verificaciones, Auditoría — más un header con acciones Aprobar/Observar/Rechazar y una sección de "Asignación del caso" (a quién está asignado, con historial de reasignaciones).

- **Pestaña Resumen:** tarjeta "Score de Compliance" (puntaje 0-100, nivel Crítico/Alto/Medio/Bajo por rango, banda de texto tipo "Riesgo medio - Requiere revisión antes de aprobar", "Nivel de diligencia aplicable" con cuenta regresiva a la próxima actualización de matriz, y detalle de qué factor resta puntos); "Matriz de riesgo" (heatmap 5×5 Probabilidad×Impacto con desglose expandible, nota aclaratoria "no modifica la fórmula del score"); "Estructura societaria" agrupada por rol (Beneficiarios Finales, Firmantes, Autoridades) con avatar, DNI enmascarado, % de participación o cargo, y badge de screening inline por persona; "Alertas Consolidadas" — hallazgos reales (no pendientes), cada uno con título corto tipo código (ej. `INCONSISTENCIA_CUIT_ESTRUCTURA`), descripción específica y fuente citada.
- **Pestaña Documentos:** contador de progreso ("8/8 documentos revisados · 8 aprobados · 0 rechazados · 0 pendientes") con píldora "Listo para decisión final" cuando está completo, botón "Solicitar Documento". Cada fila expandible muestra los campos extraídos del documento (ej. Constancia de CUIT: CUIT, Razón Social, Domicilio fiscal, Actividad Principal, Fecha alta) sin abrir el archivo, más botón "Ver documento" con nota de permisos ("Solo administradores pueden descargar"), % de confianza de extracción/OCR y estado "Aprobado por oficial".
- **Pestaña KYC:** preguntas de la entrevista al cliente en formato pregunta-respuesta con badge "Respondida".
- **Pestaña Verificaciones:** "Screening de sanciones" contra **OFAC, ONU, UIF, REPET, PEP** (nombres reales confirmados en pantalla), con badge de resultado y botón "Re-verificar"; "Verificación de personas (identidad y listas)" — resumen de conteos y tabla por persona (columnas Persona | Rol | Identidad | Cruce DNI | PEP | Sanciones) — el screening y la verificación de identidad corren **por persona**, no solo a nivel solicitud completa.
- **Pestaña Auditoría ("Trazabilidad"):** log de eventos granular — cada entrada con tipo categorizado (`VERIF`, `SISTEMA`, `DECISIÓN`, `DOC`), texto descriptivo, actor y timestamp.

**Uso de este conocimiento:** sirvió para decidir qué adoptar en el rediseño de `revision_pj_cumplimiento` (PRD-256) — alertas específicas + contador de progreso, ambos ya implementados en el mockup — y qué descartar por requerir capacidad que Bind no tiene hoy (score/matriz de riesgo, verificación por persona, auditoría granular, confirmado explícitamente por el PM que estas tres no existen en la plataforma actual). Queda como referencia general de producto para cualquier futuro proyecto de Onboarding que evalúe sumar alguna de estas capacidades.

### 8.2 Gap de PLD — datos y DDJJ mínimos faltantes en el ambiente de pruebas del onboarding de desarrollo propio para Octagon (2026-09-22)

> Fuente: mail "Re: Integración On Boarding" — Ana Laura Irrazabal (Analista de PLA/FT, Gerencia de Prevención de LA/FT/FP y Cumplimiento de BIND), 2026-09-22.

Al revisar el ambiente de pruebas del "sistema de onboarding de desarrollo propio" al que se integraría Octagon (insumo directo para la tarea T-057, análisis del paquete de datos propuesto por Octagon), Cumplimiento/PLD detectó que el sistema **omite datos mínimos exigidos por normativa** para identificar a las personas humanas vinculadas (integrantes del órgano de administración, representantes legales, apoderados y Beneficiarios Finales):
- Número de teléfono, dirección de correo electrónico, estado civil, actividad principal.
- Declaraciones Juradas (DDJJ) de **PEP, FATCA, OFAC y Sujeto Obligado**.

**Pedido de PLD:** incorporar los datos y DDJJ faltantes para asegurar un proceso de debida diligencia alineado a la normativa vigente de PLA/FT.

**Sugerencias adicionales de UX/gestión documental sobre las actas de designación:** visualizar claramente identidad/cargos/duración de autoridades; mostrar la lista completa de autoridades y representantes autorizados para operar la cuenta; habilitar descarga del legajo completo en PDF.

**Preguntas abiertas de PLD, sin responder (candidatas a reunión):**
1. Si el motor de búsqueda no encuentra actividad económica asociada, ¿permite continuar con el alta y el análisis?
2. ¿Qué información contendrá el formulario KYC/KYB final que debe firmar el cliente potencial?
3. La matriz de riesgo cliente: ¿es única e inicial, o hay una secundaria según la transaccionalidad? ¿Cómo se pondera?

**Relevancia:** el gap de datos detectado por PLD debería incorporarse a la especificación antes de cerrar el diseño de la integración con Octagon (T-057, Pablo Gomes).

## 9. Estructura real hoy de la pantalla de solicitud en el backoffice (2026-09-18)

> Fuente: sesión `/idea_solution` sobre `revision_pj_cumplimiento` (PRD-256) — el PM navegó en vivo dos solicitudes reales en staging (una en "Pendiente Revisión Oficial De Negocio"/Nivel 1, otra en "Pendiente Revisión Cumplimiento"/Nivel 2). Confirma el detalle real de la pantalla de solicitud, más allá del flujo de pasos ya documentado en §7.

**Estructura (una sola vista larga, sin pestañas):**
1. **Datos de la Solicitud** — identificador, fecha/hora, trámite (Legajo Digital), informado, IP, dispositivo, razón social, CUIT. Los botones **Aprobar/Rechazar** viven dentro de esta misma tarjeta (no en un header fijo).
   > ⚠️ **Corrección (2026-09-21) — el botón "Observar" sí existe, pero solo para el rol Cumplimiento (Nivel 2).** Lo de arriba ("no existe un botón Observar, la función equivalente la cumple Contactar Cliente") describe correctamente el Nivel 1 (Oficial De Negocio) — la sesión original que lo relevó solo navegó ese nivel y generalizó incorrectamente la ausencia a toda la pantalla. En Nivel 2 (solicitud en "Pendiente Revisión Cumplimiento", usuario con rol Cumplimiento), la cabecera muestra **tres** botones — Aprobar, Rechazar y **Observar** — que abren el mismo modal "Cambiar estado" (Estado pre-cargado + Comentario + Actualizar), con Estado = "Observado" para el tercero. "Observar" no reemplaza a "Contactar Cliente" (punto 8, sigue disponible sin cambios): "Contactar Cliente" pide algo puntual sin tocar el estado de la solicitud; "Observar" cambia el estado a "Observado", devolviendo el trámite sin rechazarlo definitivamente. Esto también confirma que el backoffice real ya tiene el mismo patrón "Aprobar/Observar/Rechazar" de la consola de referencia AVA Compliance (§8.1), al menos para Cumplimiento — no es una funcionalidad exclusiva de esa consola que haya que construir desde cero. **Además, las acciones están gateadas por rol específico por nivel, no por "ser administrador"**: con el usuario "Administrador" logueado sin el rol Cumplimiento asignado, la misma solicitud no mostraba ningún botón de acción; al asignarle el rol "Cumplimiento" (configurable en `/nivelAprobacion`, junto con "Oficial De Negocio"), los tres botones aparecieron sin volver a loguearse. **Implicancia metodológica para cualquier relevamiento futuro de este backoffice:** no alcanza con loguearse como un usuario con acceso — hace falta tener asignado el rol/nivel específico que se quiere observar.
2. **Contacto** — email y teléfono, cada uno con Editar, badge Verificado/Sin verificar, botón "Enviar código" y campo "Código OTP" + botón Verificar (flujo manual completo).
3. **Domicilio Fiscal** y **Domicilio Comercial** — dos bloques separados, mismos campos (País, Provincia, Ciudad, Calle, Numeración, Piso, Barrio, Código Postal, Departamento, CPA, Localidad, Manzana, Municipalidad).
4. **Beneficiario Final** — tabla (Apellido y Nombre, Nro. de Documento, botón "Ver Detalles Beneficiario") que abre un modal con Razón Social, Tipo/Número de Documento, Domicilio Real, Nacionalidad, Fecha de Nacimiento, Profesión, Estado Civil, Votos en la Sociedad, PEP.
   > ⚠️ **Corrección (2026-09-21) — "Propietario Directo" sí es una sección separada, convive con Beneficiario Final.** Los dos casos revisados originalmente no tenían propietario directo cargado, lo que se interpretó erróneamente como ausencia del concepto. Una solicitud con ambas secciones cargadas (FIAT CHRYSLER RIMACO ARGENTINA S.A.) muestra **Propietario Directo** como tabla independiente (Razón Social / Nro de Identificador / "Ver Detalles Propietario"), con modal propio: Domicilio Legal, Lugar de Registración, Tipo de identificador fiscal, Propiedad y/o Votos de la Sociedad (%), Flotación (%) — en el caso observado el propietario directo era otra persona jurídica (Banco de Galicia S.A.), no una persona física. Ambas secciones (Propietario Directo y Beneficiario Final) conviven en la misma pantalla, una debajo de la otra.
5. **Datos Bancarios** (CBU, Número de cuenta) y **Datos Comerciales** (Nombre de Fantasía, ID del comercio, Código de Caja, Código Sucursal) — vacíos hasta la aprobación, igual que ya estaba documentado.
6. **Historial** — tabla resumida de cambios de estado relevantes (Fecha, Hora, Estado, Usuario, Comentario), 2-3 filas típicamente.
7. **Representantes Legales** — tabla (Fecha y Hora, Estado, Representante/CUIL-DNI, Carácter, Email) con acción para ver/gestionar.
8. **Contactar Cliente** — formulario (Método de Contacto, Documentación, Enviar correo a, Comentario con contador 0/500, botones Cancelar/Enviar).
9. **Validaciones Servicios Externos** (Deudor-Arca, Arca-Actividad, Documento-Lista Negra, Mba-System, Nosis-Jurídico, Situación-BCRA) y **Validaciones Declaración Jurada** (FATCA, OCDE, PEP, UIF) — **son dos paneles separados**; el segundo es información que el propio cliente declaró (siempre Sí/No), no una consulta a un servicio externo.
10. **Archivos** — **una sola lista plana de documentos agrupados por categoría** ("Documentación societaria", "Otros archivos"), no agrupados por persona/entidad. Cada documento tiene menú de acciones vía ícono de tres puntos.
    > ⚠️ **Corrección (2026-09-21) — el menú de acciones NO es uniforme, depende del estado del documento.** Documento en estado **"Falta"** (naranja, `priority_high`): el menú tiene una única opción, **"Cargar"** — abre el selector de archivo para que el propio operador lo suba en el momento (alternativa a pedírselo al cliente vía "Contactar Cliente"). Documento en estado **"Pendiente"** (ya cargado, con nombre de archivo y fecha): el menú tiene 4 opciones — **Descargar, Visualizar, Marcar Verificado, Reemplazar**. No existe una opción "Marcar Pendiente" en ningún estado observado — el nombre correcto de la acción de aprobación es **"Marcar Verificado"**, y el de corrección es **"Reemplazar"** (no un "marcar pendiente" que regrese a un estado anterior); un oficial que reemplaza un documento mal cargado usa "Reemplazar" — el rechazo es solo a nivel de toda la solicitud, no de un documento puntual. Este es el punto que el PM señaló como **la causa concreta de que a un oficial le resulte incómodo validar** — no hay forma de ver de un vistazo qué documentos corresponden a qué persona.
11. **Línea de Tiempo** — a diferencia del "Historial" resumido (punto 6), es un **log técnico crudo y muy granular**: decenas de eventos por solicitud (ej. "Update Documentación" repetido muchas veces, "Create Otp Sms", "Update Padron A5"), cada uno con timestamp exacto e ID interno (GUID), pensado para depuración técnica, no para que un analista de negocio lo lea.
12. **Respuestas Servicios** — pestañas con el JSON crudo de cada respuesta de servicio externo (Afip PadronA5, Legajo Digital, Beneficiario Final, Declaración Jurada, Matriz de Riesgo Jurídica, etc.), colapsable, pensado para debugging técnico. Acá aparece suelto el dato de actividad económica de ARCA (ej. `idActividad: "829900"`) que hoy no se le muestra al oficial en ninguna pantalla legible.

**Dato adicional:** en el Historial de una de las solicitudes aparece el comentario "A revisar por matriz de riesgo" al pasar a Nivel 1 — sugiere algún mecanismo interno de matriz/scoring que dispara ese estado, aunque no hay ninguna tarjeta de score visible para el oficial (consistente con lo confirmado en §8.1: no existe una funcionalidad de "Score de Compliance" como la de la consola de referencia externa). No investigado más a fondo — posible gap a explorar en un futuro discovery si se retoma matriz de riesgo.

## 10. Manual operativo de punta a punta — los 4 pasos del flujo con capturas reales (2026-09-21/22)

> Fuente: manual de uso construido en sesión libre por el PM (`2026-09-21_manual_onboarding_pj_operador.html`, en `1_proyectos/proyecto-la-virginia-ob-pj/artefactos/`), con navegación en vivo del backoffice STG sobre solicitudes reales (FIAT CHRYSLER RIMACO ARGENTINA S.A., CLARO S.A.) y una carga real end-to-end del formulario público de La Virginia ("Mundo Virginia"). Complementa el flujo AS-IS de alto nivel de §7 con el detalle real de UI de cada paso.

### 10.1 Paso 1 — Formulario público de alta (front, Mundo Virginia)

Wizard con barra de progreso, un sub-paso a la vez ("Anterior"/"Siguiente" o "Iniciar"/"Siguiente"):

1. **Bienvenida** — pantalla de marca, advierte que hace falta tener actividad económica dada de alta en ARCA para continuar.
2. **Datos cliente** — Razón Social, Email, Confirmar Email, CUIT, Tipo de Sociedad (dropdown). Cada campo valida en vivo con un tilde verde.
3. **Documentación** — grilla de documentos societarios obligatorios (asterisco = obligatorio), cada uno con su propio botón de carga individual (solo PDF, máx. 6MB). Los nombres de documento coinciden con lo que el backoffice ve luego como "Falta"/"Pendiente" en Archivos → Documentación societaria (§9 punto 10) — es la misma lista, acá se sube y en el backoffice se revisa.
4. **Propietario Directo (socio o accionista)** — dos checkboxes de partida (solo personas humanas / tiene socios persona jurídica). Tildando la segunda, formulario por socio: Razón Social, Lugar de Registro, Tipo+N° de identificador fiscal, Domicilio Legal, % de Propiedad/Votos, % de Flotación, con opción de eliminar el bloque.
5. **Beneficiario Final** — mismo patrón de checkboxes de partida (umbral 10%+ de participación). Tildando la segunda, formulario completo: Razón Social, Nombre, Apellido, Tipo+Número de documento, Nacionalidad, Tipo+N° de identificador fiscal, Estado civil, Domicilio real, Profesión, Fecha de nacimiento, % de propiedad/votos, ¿Es PEP?, más adjunto del documento de identidad (frente/dorso).
6. **Domicilio Fiscal** — Calle, Número, Piso, Departamento, Provincia (dropdown), Localidad (combobox con autocompletado) y Código Postal.
7. **Domicilio Comercial** — mismo formulario que Domicilio Fiscal, para la dirección operativa.
8. **Teléfono** — código de país + número. Mismo dato que el backoffice muestra en "Contacto" como "Sin verificar" hasta confirmar con OTP.
9. **Datos representantes** — Carácter del representante (dropdown, ej. "Representante Legal"), Documento, Email. Mismo email que el backoffice ve en "Representantes Legales" con estado "No iniciada", y al que en el Paso 4 le llega la invitación de onboarding personal.
10. **Declaración** — tres checkboxes de condición especial (Sujeto Obligado / OCDE / FATCA) o "Ninguna de las anteriores". No se relevó qué campos adicionales pide si se tilda alguna de las tres primeras (pendiente para una futura sesión).
11. **Proceso Completado** — confirma que se enviará email a cada representante/firmante para completar su validación de identidad (dispara el Paso 4/Nivel 2), y que la solicitud será evaluada por un ejecutivo. A partir de acá la solicitud es visible en el backoffice como "Pendiente Revisión"/Nivel "Oficial De Negocio".

Confirma desde el lado de carga que "Propietario Directo" y "Beneficiario Final" son dos sub-formularios independientes (consistente con la corrección de §9 punto 4).

### 10.2 Paso 4 — Onboarding personal del representante legal

Corre en un **tercer sitio, distinto del backoffice y del formulario público**: `ustus-01.azurewebsites.net`. Se dispara con un email al representante legal (email cargado en el Paso 1 / §10.1 punto 9) cuando el Paso 3 (Cumplimiento) aprueba la solicitud.

1. **Bienvenida / Términos y Condiciones** — resumen de los datos ya cargados de la empresa (Razón Social, CUIT, domicilio, teléfono) y las tres declaraciones (Sujeto Obligado UIF/FATCA/OCDE) del Paso 1, para que el representante las revise. Dos checkboxes obligatorios (Términos y Condiciones + confirmación de que los datos/DDJJ de la empresa son correctos) habilitan "Iniciar".
2. **Validación de identidad — DNI** — foto de frente y dorso del DNI físico (RENAPER), cada una con su propia captura de cámara, pantalla de confirmación con miniaturas, y procesamiento (OCR/MRZ) con barra de progreso.
3. **Validación de identidad — Selfie (prueba de vida)** — cámara frontal con óvalo guía, confirmación con miniatura y opción "Retomar selfie", procesamiento de facematch selfie-vs-DNI.
4. **Emails de contacto** — el representante carga **su propio email personal** (no el de la empresa), con verificación por código numérico de 6 dígitos.
5. **Teléfono de contacto** — mismo patrón con el teléfono propio y verificación por SMS. **Dato relevante:** en una prueba real el SMS llegó con varios segundos de demora, después de que el representante ya había avanzado a la pantalla de Declaración — el formulario no bloquea el avance mientras se espera el código, asincronía a tener en cuenta al explicarle el flujo a un representante real.
6. **Declaración personal** — cuatro condiciones sobre la persona física (Sujeto Obligado UIF / residente fiscal de otro país OCDE / residente fiscal EEUU FATCA / PEP) o "Ninguna de las anteriores".
7. **Confirmación final** — avisa que se enviará un email para indicar cómo seguir.

No relevado: qué pasa si la validación biométrica falla definitivamente (reintentos agotados), ni qué campos adicionales pide la Declaración si se tilda alguna condición especial (mismo punto abierto que en el Paso 1).

### 10.3 Nivel 3 automático — alta de Wallet/comercio tras la conformidad del representante legal

Una vez que el representante legal completa el Paso 4 (§10.2), corre un **Nivel 3 automático, sin intervención de ningún operador**, que termina de aprobar la solicitud y provisiona la cuenta. Progresión de estados observada en "Historial" (mismo trigger — la conformidad del representante legal):

1. `Pendiente Revisión` (Nivel 1 — Oficial De Negocio) → Aprobada
2. `Pendiente Revisión` (Nivel 2 — Cumplimiento) → Aprobada
3. `Pendiente Representante Legal` (Nivel 2 — Cumplimiento) → "Aprobada por niveles - Emails enviados a RL" (dispara el Paso 4)
4. `Aprobado a revisar` (Nivel 3) → comentario "Alta Wallet OK"
5. `Aprobada` (Nivel 3) → comentario "Solicitud completa"

Los pasos 4 y 5 son el Nivel 3 automático — la sección "Documentación" muestra en paralelo `DDJJ`, `Alta Wallet`, `Comercio - Alta` y `Asignar Comercio`, cada una con su propio timestamp, como las tareas internas que ejecuta ese nivel.

**⚠️ Etiqueta incorrecta — "CBU" en realidad muestra el CVU.** En "Datos de la Solicitud" con estado final "Aprobada", el campo que la pantalla etiqueta como **"CBU"** en realidad contiene el **CVU** de la cuenta recién creada — no hay ningún CBU real involucrado en este flujo. Es una etiqueta heredada/incorrecta puntual de esta pantalla del backoffice de Onboarding Jurídico, no un problema de terminología del producto Wallet en general (que sí distingue CBU/CVU correctamente — ver `wallet/validacion_totalizadores_cbu_cvu.md` y `apis_expuestas/cvu/`). "Datos Comerciales" (ID del comercio, Código de caja, Código de sucursal) queda dado de alta y vinculado a la cuenta en el mismo paso.

---
*Última actualización: 2026-09-23 — `/context_merge`: nueva §8.2 (gap de PLD sobre datos/DDJJ faltantes en el ambiente de pruebas del onboarding de desarrollo propio para Octagon, insumo T-057); corrección de §9 punto 1 (botón Observar sí existe para el rol Cumplimiento) y punto 4/10 (Propietario Directo es sección separada; menú de Archivos depende del estado del documento); nueva §10 con el manual operativo de punta a punta de los 4 pasos del flujo (formulario público detallado, onboarding del representante legal, Nivel 3 automático y etiqueta CBU/CVU incorrecta).*
*Última actualización anterior: 2026-09-18 — `/context_merge`: nueva §8.1 (detalle funcional real de la consola de referencia "AVA Compliance") y nueva §9 (estructura real de la pantalla de solicitud en el backoffice) — ambas del discovery de `revision_pj_cumplimiento` (PRD-256).*
*Última actualización anterior: 2026-08-19 — nueva §8 (demo end-to-end a Octagon/Banco Industrial: consola de cumplimiento y potencial de marca blanca).*
*Última actualización anterior: 2026-08-06 — nueva §7 (flujo AS-IS paso a paso Front+BO, desde la página Notion "Onboarding Jurídico") a pedido del proyecto [La Virginia — OB PJ](../../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md).*
*Última actualización anterior: Fuente: Notion histórico, Epic "OB Personas Jurídicas MVP" (91 tickets) — ingesta 2026-07-06. §6: backfill `/sync_releases` vía export XML, 2026-07-13.*
