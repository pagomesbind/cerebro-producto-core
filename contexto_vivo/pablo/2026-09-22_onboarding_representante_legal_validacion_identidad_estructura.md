---
id: 2026-09-22_onboarding_representante_legal_validacion_identidad_estructura
pm: pablo
fecha_captura: 2026-09-22
fuente: "sesión libre — video real autograbado por el PM completando su propio onboarding personal como representante legal de una solicitud PJ de test (FIAT CHRYSLER RIMACO ARGENTINA S.A.), para armar el Paso 4 de un manual de uso del flujo completo; frames extraídos con ffmpeg del .mp4 provisto en raw/"
producto: onboarding
tema: estructura del sitio de onboarding personal del representante legal (Paso 4) — validación biométrica de identidad, contacto propio y declaración personal
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Primera vez que se releva de punta a punta el Paso 4 del flujo de onboarding de Persona Jurídica: el onboarding **personal** del representante legal, disparado automáticamente cuando el Paso 3 (cumplimiento) aprueba la solicitud. Hasta ahora `onboarding_personas_juridicas.md` solo documentaba el backoffice (Pasos 2 y 3) y el formulario público de carga de la PJ (Paso 1, capturado ayer); este paso corre en un **tercer sitio, completamente distinto**: `ustus-01.azurewebsites.net` — ni el backoffice ni el formulario público de la PJ.

**Disparo:** al aprobarse el Paso 3, se envía un email al representante legal con el email cargado en el Paso 1 (Datos representantes), invitándolo a completar su propio onboarding.

**Estructura del sitio (mismo patrón de barra de progreso que el formulario público):**

1. **Bienvenida / Términos y Condiciones** — muestra un resumen de los datos ya cargados de la empresa (Razón Social, CUIT, domicilio completo, teléfono) y las tres declaraciones de la empresa (Sujeto Obligado UIF / FATCA / OCDE) tal como quedaron en el Paso 1, para que el representante las revise. Dos checkboxes obligatorios: "Acepto los Términos y Condiciones" y "Declaro que los datos y las declaraciones juradas de la empresa son correctos". Botón "Iniciar" solo se habilita con ambos tildados.
2. **Validación de identidad — DNI** — instrucciones (foto del DNI físico vigente RENAPER, frente y dorso, nítida y legible) seguidas de dos capturas de cámara independientes (Galería/Tomar foto/Cambiar cámara para cada lado). Al cargar ambos lados, una pantalla de confirmación muestra las dos miniaturas (Frente/Dorso) antes de dejar avanzar. Después corre un procesamiento con barra de progreso (0%→100%) — validación OCR/MRZ del documento.
3. **Validación de identidad — Selfie (prueba de vida)** — mismo patrón: instrucciones, cámara frontal con óvalo guía, pantalla de confirmación con miniatura de la selfie tomada y botón "Retomar selfie" antes de aceptar, y un segundo procesamiento (facematch selfie-vs-DNI) que termina en "¡Completado!" con un ícono de check verde.
4. **Emails de contacto** — el representante carga **su propio email personal** (no el de la empresa), con validación de formato en vivo ("Formato de email inválido" si no matchea el patrón) y verificación por código numérico de 6 dígitos enviado por correo, con cuenta regresiva para reenvío y opción "Cambiar email".
5. **Teléfono de contacto** — mismo patrón que el email pero con el teléfono propio del representante y verificación por SMS. **Dato relevante:** en el test real, el SMS con el código llegó con varios segundos de demora — el representante ya había avanzado a la pantalla de Declaración cuando la notificación con el código apareció en pantalla. El formulario no bloquea el avance mientras se espera el código, así que hay que tener en cuenta esta asincronía al explicarle el flujo a un representante legal real.
6. **Declaración personal** — cuatro condiciones sobre la persona física (no la empresa): ¿Sos Sujeto Obligado (UIF)? / ¿Sos ciudadano o residente fiscal de otro país (OCDE)? / ¿Sos ciudadano o residente fiscal estadounidense (FATCA)? / ¿Sos una persona políticamente expuesta (PEP)? — o "Ninguna de las anteriores". Al confirmar, procesa (barra de progreso) y cierra el onboarding.
7. **Confirmación final** — mensaje: "Pudimos validar tus datos y te enviaremos un email para contactarte cómo seguir. No olvides revisar tu SPAM."

**No relevado en esta sesión (queda abierto para una futura pasada si hace falta):** qué pasa si la validación biométrica falla de forma definitiva (reintentos agotados, DNI ilegible más de N veces); qué campos adicionales pide la Declaración si se tilda alguna de las cuatro condiciones especiales en vez de "Ninguna de las anteriores" (mismo punto abierto que ya quedó anotado para la Declaración de la empresa en el Paso 1).

Fuente: manual de uso construido en la misma sesión — ver [`2026-09-21_manual_onboarding_pj_operador.html`](../proyecto-la-virginia-ob-pj/artefactos/2026-09-21_manual_onboarding_pj_operador.html), que con este paso queda con los 4 pasos completos del flujo, todos con capturas de pantalla reales (las del Paso 4 extraídas con ffmpeg de un video real autograbado por el PM).
