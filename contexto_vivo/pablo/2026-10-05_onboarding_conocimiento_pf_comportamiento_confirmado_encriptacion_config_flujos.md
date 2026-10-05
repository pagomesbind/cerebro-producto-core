---
id: 2026-10-05_onboarding_conocimiento_pf_comportamiento_confirmado_encriptacion_config_flujos
pm: pablo
fecha_captura: 2026-10-05
fuente: "sesión de trabajo del proyecto bcra_anexo_b — correcciones del PM al borrador de P-01 (Procedimiento de Onboarding Digital de Personas Humanas) y definición de encriptación recibida por el PM"
producto: onboarding
tema: Comportamiento confirmado del onboarding de persona humana (estados, revisión manual y Reprocesar, webhook, política de datos), configuración de flujos y matriz, y datos encriptados en la base de Onboarding
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "2026-10-05_onboarding_conocimiento_flujos_pf_pj_manual_enrolamiento_res200 (item en cola de captura, punto a reconciliar 1) — el diagrama de Luciana rechaza al agotar reintentos en la consulta a fuentes externas; el PM confirma que en ese caso la solicitud queda en revisión manual, coherente con arquitectura_solicitud_y_flujos.md §1bis. El diagrama quedó desactualizado en ese punto."
confianza: alta
estado: en_cola
merge_commit:
---

Definiciones que Pablo Gomes confirmó al revisar el borrador de P-01 (2026-10-05). Reflejan cómo funciona hoy el onboarding de persona humana; ya están en el documento de Drive de P-01.

## Comportamiento confirmado

- **Política de datos:** antes de iniciar la solicitud, la persona debe aceptar la política de uso de datos personales. Sin esa aceptación no se inicia.
- **Información complementaria según el flujo:** la persona completa datos adicionales que dependen del flujo configurado para la entidad, como ocupación y estado civil.
- **Estados:** existe **Pendiente** (la solicitud fue iniciada y todavía resta que el cliente complete pasos). **No existe** un estado "En progreso". Se mantienen, según el enum de la API pública, Rechazada, Aprobada, Validación manual, Vencida y Error de alta.
- **Revisión manual por falla de listas:** cuando un servicio externo de consulta de listas no responde, la solicitud queda en revisión manual, porque no puede determinarse la información que debe evaluar la matriz.
- **Reprocesar:** desde la revisión manual, la opción "Reprocesar" reintenta las consultas que hubieran fallado. Si esta vez resultan satisfactorias, la solicitud retoma el flujo y continúa.
- **Webhook:** se envía un webhook a la entidad con el resultado de la solicitud. Nota para el merge: `arquitectura_solicitud_y_flujos.md` §1bis documenta que hoy el webhook se dispara solo para solicitudes aprobadas y que PRD-202 lo amplía a los 5 desenlaces; P-01 lo describe de forma general ("con el resultado de la solicitud").

## Configuración de flujos y matriz de evaluación

- Cada entidad tiene su propio flujo, configurado en el backoffice. Por entidad/flujo se configuran las etapas encendidas o apagadas, sus parámetros y umbrales (ej. cantidad máxima de intentos, plazo de vigencia de la solicitud pendiente), los datos y documentos requeridos, y la **ponderación de cada validación en la matriz de evaluación** junto con los umbrales de resultado.
- La **matriz** consolida el resultado y el puntaje de cada validación, pondera según el flujo y compara el total contra umbrales: aprobación automática, revisión manual o rechazo. Además puede haber condiciones que derivan directo (ej. PEP según Worldsys: rechazo o revisión manual). Se evalúa cuando terminaron las validaciones iniciales de identidad y las consultas externas.
- Orden de referencia para describir el flujo (el de Onboarding estratégico): validaciones iniciales de identidad (lectura de DNI y Renaper Datos, prueba de vida y comparación facial, OTP de correo y de teléfono), validaciones con matriz (consultas externas, información complementaria y declaraciones, evaluación), y alta y notificación.

## Encriptación de datos en la base de Onboarding

Indicación recibida por el PM: se encriptan los siguientes datos de las solicitudes: nombre y apellido; fecha de nacimiento; número de DNI; número de CUIL; número de trámite del DNI; imagen del frente del DNI; imagen del dorso del DNI; dirección (calle, número, piso, departamento, CPA, ciudad, municipalidad, provincia, país); teléfono; correo electrónico; hash (identificador de dispositivo). Nivel mínimo de encriptación AES-256 y SHA-256 para los hashes.

**Pendiente de verificar:** la indicación original estaba redactada como "se deberían encriptar". P-01 lo afirma en presente por pedido del PM. Confirmar con Ingeniería (Fintexa) que la encriptación está efectivamente implementada en la base de Onboarding y para todos los campos de la lista, antes de que P-01 se firme y se envíe.

## Canales de uso de Onboarding por las entidades (agregado 2026-10-05)

Tres canales, descriptos en P-01 (fuentes: `2_areas/overview_productos/overview_onboarding.md` modalidades de integración, `onboarding_por_api.md` §1-2 y §4):
- **Front de Onboarding de Bind PSP (marca blanca):** URL fija por entidad, personalizable con colores y logos. Bind PSP guía a la persona en todos los pasos (documento, prueba de vida, contacto). Las solicitudes se gestionan desde el backoffice.
- **API por partes:** la entidad tiene front propio y consume las APIs paso a paso (OrquestadorBind). Puede crear la solicitud con `externalId` propio, retomarla más adelante (el caso COTO CICSA pidió dos pasos separados por meses), actualizarla con datos ya validados por la entidad, y cada respuesta trae el estado y el resultado del paso. Autenticación OAuth2.
- **API de registro único (integración completa, caso Inter):** un solo endpoint con toda la información y las imágenes del DNI capturadas por la app de la entidad; Bind PSP interpreta el documento del lado servidor, valida y da de alta en forma secuencial y responde con el resultado y las cuentas. Bind PSP no interactúa con la persona, así que no puede pedir otra foto si la lectura falla.

No incluido en P-01: el canal de sucursal/banco del BIND (`onboarding_bind_sucursal.md`), por no ser onboarding digital B2B2C.

## Persona jurídica: consultas a servicios externos y matriz (agregado 2026-10-05)

El PM aportó una captura del backoffice ("Validaciones Servicios Externos") de una solicitud PJ. El panel lista los servicios consultables y el resultado de cada uno: Deudor - Arca, Arca - Actividad, Documento - Lista Negra, Mba - System, Nosis - Jurídico y Situación - BCRA. En la captura solo "Arca - Actividad" estaba consultada ("La persona está registrada en Arca con una actividad"); los demás figuraban "No se consultó". Decisión del PM: aunque hoy no estén activados en el flujo de PJ, P-02 declara que la solución puede consultarlos (listas y burós) para recabar información que se evalúa en la matriz de riesgo. Cada flujo define qué servicios activa. La configuración por entidad y la matriz son las mismas que en persona humana.

**Por confirmar:** qué es el servicio "Mba - System" (P-02 lo cubre como "otros servicios de información habilitados").

