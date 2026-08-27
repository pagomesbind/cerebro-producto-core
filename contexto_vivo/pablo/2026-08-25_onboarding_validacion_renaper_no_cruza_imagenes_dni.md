---
id: 2026-08-25_onboarding_validacion_renaper_no_cruza_imagenes_dni
pm: pablo
fecha_captura: 2026-08-25
fuente: "Reunión 'RE: BIND PSP - REI - Onboarding Digital' (minuta Gemini, 2026-08-25) — sesión de pruebas de validación de identidad en ambiente productivo con Victoria Farías (LLYASOC, auditoría externa por cuenta de Banco Industrial/REI), Emma Vignoles, Mariana Nadalin, Pilar Erviti, Adriana Endzeliz"
producto: onboarding
tema: "Mecánica real de la validación de identidad contra Renaper (no cruza imágenes de DNI frente/dorso) y vulnerabilidad detectada: el sistema permitió crear una cuenta combinando el frente del DNI de una persona con el dorso de otra"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Mecánica de la validación de identidad: Renaper no compara imágenes, la biometría es un paso aparte

Durante una sesión de pruebas de onboarding en ambiente **productivo** (test conjunto entre Bind PSP y una auditora externa contratada por Banco Industrial — ver contexto de la tarea `T-014`/`T-024` en `1_proyectos/tareas.md`, ticket de fondo: falla del proveedor de prueba de vida en STG que obligó a mover las pruebas a producción), el equipo probó deliberadamente combinaciones de documentos para entender los límites de la validación:

- **Prueba realizada:** se inició un registro cargando el **frente del DNI de una persona** y el **dorso del DNI de otra persona distinta**, seguido de una selfie/prueba de vida. Se repitieron combinaciones (frentes, dorsos, personas distintas, incluyendo a una tercera persona) para mapear qué bloquea el sistema y qué no.
- **Hallazgo (aclarado por Emma Vignoles, Bind PSP):** el sistema **no valida la imagen del DNI contra Renaper** — consulta la API de datos de Renaper usando **CUIL + género + número de trámite** (campos de texto extraídos/ingresados, no la foto del documento). La validación biométrica (que la persona frente a cámara coincide con la foto del DNI) corre **por un camino completamente aparte**, vía el proveedor Socialnet/Facetech.
- **Consecuencia — vulnerabilidad identificada:** como consecuencia de ese diseño, el sistema permite en ciertas configuraciones **crear una cuenta combinando el frente y el dorso de DNIs de dos personas distintas**, porque nada en el flujo cruza la imagen del frente contra la del dorso, ni contra el resultado de Renaper más allá de los 3 campos de texto. Victoria Farías (la auditora) señaló explícitamente que esto es una debilidad a incluir en el informe de auditoría.
- **Mitigación probada en la misma sesión:** ante los bloqueos repetidos por intentos fallidos, Pablo Gomes ajustó en caliente el parámetro de intentos fallidos permitidos a 4 — dato operativo (el límite de intentos es configurable), no una corrección del hallazgo de fondo.
- **Pruebas pendientes (quedaron para el día siguiente, 2026-08-26 9:30, por caché/latencia del sistema en actualizar los intentos permitidos):** validar el rechazo ante número de trámite/género inconsistentes, y validar el comportamiento si se presenta una fotografía impresa en vez de una selfie en vivo.

> Fuente: minuta Gemini de la reunión "RE: BIND PSP - REI - Onboarding Digital" (2026-08-25, 15:31 GMT-03:00), compartida por Emma Vignoles. Contexto de negocio (por qué se estaba haciendo esta prueba, en qué ambiente, quién es la auditora) documentado en `1_proyectos/tareas.md` T-024.
