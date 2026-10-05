---
id: 2026-10-05_onboarding_conocimiento_flujos_pf_pj_manual_enrolamiento_res200
pm: pablo
fecha_captura: 2026-10-05
fuente: "sesión de trabajo del proyecto bcra_anexo_b — 4 PDF de `raw/` aportados por Luciana Rudaz (los había preparado para responder un pedido de información anterior del BCRA): Manual de enrolamiento de usuarios, Flujo de Onboarding Persona Humana, Flujo de Onboarding Persona Jurídica, Requisitos de alta de cuentas conforme la Resolución Uniforme 200/24"
producto: onboarding
tema: Documentación oficial de Bind PSP sobre el flujo de onboarding PF/PJ, el manual de enrolamiento y los requisitos de la Res. Uniforme UIF 200/24 por tipo de persona y sociedad
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/flujos_onboarding_pf_pj_documentados.md
tipo_destino: crear
contradice: "3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md §1bis — el diagrama PF muestra que, tras agotar reintentos en la consulta a fuentes externas, la solicitud se rechaza (código 99), mientras la wiki dice que en esa etapa la solicitud queda en validación manual; y la numeración de estados del diagrama (3 rechazada, 5 requiere validación manual) difiere del enum de la API pública (4 = Validación Manual, 5 = Pendiente credenciales). Ver 'Puntos a reconciliar'."
confianza: media
estado: ingestado
merge_commit: c0d6964
---

Documentos que Bind PSP ya tenía armados (los preparó Luciana Rudaz para responder un pedido anterior del BCRA). Son la base descriptiva del proceso de onboarding propio y se usan como referencia del proyecto `1_proyectos/bcra_anexo_b/` (copias en su carpeta `referencias/`). Todavía no son canon.

## 1. Manual de enrolamiento de usuarios (rotulado "14) Manual de enrolamiento de los usuarios")

- **Objetivo:** asegurar la identificación, validación y autenticación fehaciente de personas humanas y jurídicas que solicitan una cuenta de pago, con criterios de seguridad, trazabilidad, integridad y protección de la información.
- **Registro y términos:** la persona completa un formulario con datos personales válidos y acepta los Términos y Condiciones Generales. La información tiene carácter de declaración jurada y la persona se compromete a mantenerla actualizada. Bind PSP se reserva el derecho de pedir comprobantes o documentación adicional y de rechazar o suspender cuentas ante incongruencias, inconsistencias o indicios de actividad sospechosa, sin derecho a indemnización.
- **Mecanismo:** cumple con los requisitos de identificación no presencial según normativa BCRA, con mecanismos trazables, auditables y no manipulables.
- **Validaciones para personas humanas (según Res. Uniforme 200/24):** nombre y apellido, tipo y número de documento, nacionalidad, fecha de nacimiento, estado civil, CUIL/CUIT/CDI, domicilio real, domicilio electrónico, actividad u ocupación principal, declaración PEP y cumplimiento FATCA/OCDE, DNI frente y dorso, selfie y prueba de vida; validación en RENAPER Datos (ejemplar vigente, domicilio, nacionalidad) y RENAPER Rostro; validación de correo y teléfono con OTP (SMS o e-mail); validación de listas y servicios externos (ARCA, Nosis y otras fuentes oficiales); bases de sujetos no admitidos y listas internas (negras/blancas).
- **Validaciones adicionales para personas jurídicas:** estatuto o contrato social con certificación notarial e inscripción registral; actas de designación de autoridades vigentes con certificación notarial; identificación de propietarios directos y beneficiarios finales y verificación de su identidad según normativa UIF; declaraciones FATCA, OCDE, PEP y de beneficiarios finales; validación del correo institucional por OTP; validación de identidad (onboarding de persona física) de al menos una persona humana autorizada a operar en representación (apoderado o representante legal). La documentación varía según el tipo societario.
- **Servicios y fuentes:** RENAPER Datos y Rostro (validación documental y biométrica); servicios de prueba de vida (SocialNet), con detección de suplantación mediante video en tiempo real; servicios de verificación de contacto; listas externas e internas (ARCA, Nosis, UIF, listas propias).

## 2. Flujo de Onboarding Persona Humana (diagrama de calles: Front, Backend, Externos, Backoffice/Legajo digital)

Secuencia: nueva solicitud (estado 1) → pantalla de bienvenida y explicación del paso DNI → foto de frente y dorso → backend extrae datos (PDF417) y guarda → valida en RENAPER (con reintentos) → consulta a otros externos (Nosis, Worldsys, ARCA y otro servicio) y guarda resultados y puntaje (con reintentos) → validación final en matriz (parametría por entidad) → si requiere validación manual: revisión manual en backoffice (puede reprocesar; si aprueba continúa, si rechaza termina en estado 3) → explicación del paso selfie → ingreso de foto y validación por comparación con servicio externo, guardando el puntaje → email: envío de OTP, ingreso, validación, con reenvío → celular: ídem → información adicional (estado civil, datos de comercio, etc.), selección de DDJJ y aceptación de T&C; si queda incompleto "no se le permite avanzar" → define estado final según matriz → valida si existe la persona → si no existe, crea cliente → crea CVU → alta de comercio (Bind Pagos) → envía email de bienvenida.

**Códigos de error del diagrama:** 1 `DOCUMENTO_NO_ENCONTRADO`; 2 `PDF417_NO_ENCONTRADO` (continúa solo si los datos del DNI se enviaron aparte; si no, rechazo); 4 `PERSONA_NO_ENCONTRADA`; 5 `PERSONA_FALLECIDA`; 6 `EJEMPLAR_NO_VALIDO`; 7 comparación facial sin puntaje suficiente; 8 rechazo en la matriz final; 10 error de OTP de email al llegar al máximo de intentos; 11 ídem para el teléfono; 15 `OTP_INCORRECTO` (error < máximo, se reintenta); 99 reintentos agotados tras falta de respuesta de un servicio.

**Estados de solicitud que muestra el diagrama:** 1 al iniciar; 3 = rechazada (por no poder extraer datos del DNI, por validaciones en RENAPER, por puntaje de riesgo insuficiente, por validación manual); 5 = requiere validación manual.

## 3. Flujo de Onboarding Persona Jurídica

Nueva solicitud PJ (estado 1) → bienvenida, explicación de validación de identidad y T&C → carga de datos de la PJ → valida datos en servicios externos (Nosis, ARCA/AFIP y otro) → guarda → busca la documentación requerida según el tipo de sociedad → muestra y carga documentación → **validación manual de la documentación en backoffice** (no válida: rechazo, estado 3; en evaluación: estado 4) → carga del email del representante legal o apoderado → envío de un link de onboarding PF al representante → mensaje "solicitud en evaluación" → el representante realiza el onboarding PF (mismo flujo de la sección 2). Resultado final: si el onboarding del representante/apoderado es correcto, alta de cuenta y habilitación de productos exitosa (estado 2); si no, estado 5 ("OB y alta de cuenta PJ exitosa, pendiente alta de productos", según el rótulo del diagrama). La PJ solo se aprueba con al menos una persona humana representante validada.

## 4. Requisitos de alta de cuentas conforme Res. Uniforme 200/24 (documento de Bind PSP)

**Personas físicas:** nombre y apellido completo; tipo y número de documento; nacionalidad y fecha de nacimiento; estado civil; CUIL/CUIT/CDI (o clave equivalente para extranjeros); domicilio real (calle, número, localidad, provincia, país y código postal); domicilio electrónico (art. 75 CCyC); actividad laboral o profesional principal; cumplimiento de la Resolución UIF de PEP. Documentación y validaciones: DNI frente y dorso, selfie, prueba de vida, RENAPER Datos (CUIL, domicilio, nacionalidad, fecha de nacimiento, ejemplar vigente), RENAPER Rostro, mail y/o teléfono de contacto con OTP, DDJJ PEP, FATCA y OCDE, aceptación de T&C, validación de listas y servicios externos (ARCA, Nosis).

**Personas jurídicas:** denominación o razón social; fecha y número de inscripción registral; CUIT/CDI/CIE; domicilio legal y comercial; domicilio electrónico; actividad principal; identificación de integrantes del órgano de administración, representantes legales o apoderados (con las reglas de personas humanas); propietarios directos o beneficiarios finales y verificación de su identidad (en titularidades muy atomizadas basta identificar al consejo de administración o a quienes ejerzan el control efectivo); cumplimiento de la Resolución UIF de PEP en relación con los beneficiarios finales y de la de financiamiento del terrorismo.

**Documentación por tipo de sociedad** (R = requerido, O = opcional): 
- S.A., S.R.L., S.A.S., S.C.S. y S.C.A.: estatuto o contrato social con certificación notarial (R); constancia de inscripción registral (R); acta de designación de autoridades vigentes (R); certificación notarial y/o inscripción registral del acta de designación (R); modificaciones al estatuto con constancia de inscripción (O); poderes generales amplios de apoderados (R).
- Sociedad de hecho: contrato social o nota con el régimen de firmas certificado ante escribano (R); constancia de AFIP (R); poderes generales amplios (R).
- Sociedad Capítulo I Sección IV: contrato social con firmas certificadas ante escribano (R); modificaciones posteriores con certificación notarial (O); poderes generales amplios (R).
- Asociaciones y fundaciones: instrumento constitutivo o estatuto con certificación notarial (R); constancia de otorgamiento de la personería jurídica (R); acta de designación de autoridades vigentes (R); certificación notarial y/o inscripción del acta (R); modificaciones (O); poderes generales amplios (R).
- Cooperativas: instrumento constitutivo o estatuto con certificación notarial (R); constancia de inscripción ante el INAES y autorización para funcionar (R); acta de designación de autoridades (R); certificación notarial y/o inscripción del acta (R); modificaciones con constancia de inscripción (O); poderes generales amplios (R).
- Para todas las personas jurídicas además: mail de contacto, OTP de validación del domicilio electrónico de la sociedad, DDJJ SO, FATCA y OCDE, DDJJ de propietarios directos y/o beneficiarios finales, identificación de la identidad de esos propietarios o beneficiarios, aceptación de T&C, validación de listas y servicios externos (ARCA, Nosis) y onboarding de persona física de al menos una persona humana que opere en representación.

## Puntos a reconciliar con el canon actual (para el merge)

1. **Fallo de consultas externas (resuelto 2026-10-05):** el diagrama PF rechaza (código 99) al agotar los reintentos en la consulta a otros externos; el PM confirmó que en realidad la solicitud queda en revisión manual y que se puede "Reprocesar" (ver item `2026-10-05_onboarding_conocimiento_pf_comportamiento_confirmado_encriptacion_config_flujos`). El diagrama quedó desactualizado en ese punto.
2. **Numeración de estados:** el diagrama usa 5 = requiere validación manual y 3 = rechazada; la API pública (Registro Único) documenta 4 = Validación Manual y 5 = Pendiente credenciales. Probablemente son vistas distintas (interna vs. pública); no confirmado.
3. **Alta de comercio (Bind Pagos):** el diagrama PF cierra con el alta de comercio; `hallazgos_operativos_historicos.md` registra la desactivación del flujo de OB de pequeños comercios el 2026-10-01. Confirmar si el paso sigue vigente.
4. **Prueba de vida y comparación facial:** los documentos describen la prueba de vida con SocialNet y la validación facial con RENAPER Rostro; el canon (§6.1) documenta que ambos proveedores relevados entregan una captura 2D y no el video completo. Los documentos no hablan de evidencia de video.
