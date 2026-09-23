---
id: 2026-09-21_onboarding_boton_observar_nivel_cumplimiento_y_permisos_por_rol
pm: pablo
fecha_captura: 2026-09-21
fuente: "sesión libre — navegación en vivo del backoffice STG de Onboarding Jurídico (app-onboarding-juridico-bo-stg-001), misma solicitud 'FIAT CHRYSLER RIMACO ARGENTINA S.A. (Test)' aprobada en vivo de Nivel 1 a Nivel 2 (Cumplimiento) para armar el manual de uso del Paso 3"
producto: onboarding
tema: el botón Observar sí existe, pero solo para el rol Cumplimiento — corrige §9 punto 1; permisos de acción atados a un rol por nivel, no al usuario logueado en general
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md §9 punto 1 (mergeado 2026-09-18) — afirma explícitamente 'no existe un botón Observar, la función equivalente la cumple Contactar Cliente (punto 8)'"
confianza: alta
estado: ingestado
merge_commit:
---

Navegación en vivo (no simulada): se aprobó con un comentario general una solicitud jurídica real en STG desde el rol "Oficial De Negocio" (Nivel 1) — pasó automáticamente a "Pendiente Revisión Cumplimiento" (Nivel 2). Dos hallazgos que corrigen/completan lo documentado en §9 sobre esa misma pantalla:

**1. El botón "Observar" sí existe — pero solo aparece para el rol Cumplimiento (corrige punto 1).**

Lo documentado en §9 punto 1 dice textualmente que "no existe un botón Observar, la función equivalente la cumple Contactar Cliente". Esto es incorrecto para el Nivel 2: en la cabecera de "Datos de la Solicitud", cuando la solicitud está en "Pendiente Revisión Cumplimiento" y el usuario logueado tiene el rol Cumplimiento, aparecen **tres** botones — Aprobar, Rechazar y **Observar** — no dos. Los tres abren el mismo modal "Cambiar estado" ya documentado (Estado pre-cargado + Comentario + Actualizar), con Estado = "Observado" en el caso de Observar. Es decir: la sesión que generó §9 punto 1 solo vio la pantalla en Nivel 1 (Oficial De Negocio) — donde efectivamente solo hay Aprobar/Rechazar — y generalizó incorrectamente esa ausencia a toda la pantalla. El "Observar" de Nivel 2 no reemplaza a "Contactar Cliente" (que también sigue disponible en Nivel 2, sin cambios) — son dos mecanismos distintos: "Contactar Cliente" pide algo puntual al representante legal sin tocar el estado de la solicitud; "Observar" cambia el estado de la solicitud a "Observado" con un comentario, devolviendo el trámite sin rechazarlo definitivamente.

Esto también resuelve una ambigüedad de §8.1: la consola de referencia externa "AVA Compliance" tiene un patrón "Aprobar/Observar/Rechazar" — ahora se confirma que el backoffice real de Bind PSP **ya tiene ese mismo patrón hoy**, al menos para el rol Cumplimiento (Nivel 2), no es una funcionalidad exclusiva de la consola de referencia que haya que construir desde cero.

**2. Las acciones (Aprobar/Rechazar/Observar) están gateadas por un rol específico por nivel, no por si el usuario es "administrador" o tiene acceso general al backoffice.**

Con el mismo usuario "Administrador" logueado, la solicitud en "Pendiente Revisión Cumplimiento" **no mostraba ningún botón de acción** (ni Aprobar, ni Rechazar, ni Observar) — verificado con recarga completa de la página y navegación fresca desde la grilla, no era un problema de caché. Todo el contenido de la pantalla (Contacto, Documentación, Validaciones, Historial, etc.) se veía igual, solo faltaban los botones de acción del header. Al asignarle al mismo usuario el rol "Cumplimiento" (existe como entidad configurable en `/nivelAprobacion`, junto con "Oficial De Negocio" — pantalla de administración con las dos filas, ambas "Habilitado", y un botón "Modificar orden de niveles de aprobación"), los tres botones aparecieron inmediatamente sin volver a loguearse.

Implicancia para cualquier discovery futuro sobre este backoffice (incluido `revision_pj_cumplimiento`/PRD-256): para relevar en vivo qué puede hacer un rol, no alcanza con loguearse como un usuario con acceso al backoffice — hace falta que ese usuario tenga asignado el rol/nivel específico que se quiere observar, o se puede llegar a conclusiones incompletas como la de §9 punto 1.

Fuente: manual de uso construido en la misma sesión — ver [`2026-09-21_manual_onboarding_pj_operador.html`](../proyecto-la-virginia-ob-pj/artefactos/2026-09-21_manual_onboarding_pj_operador.html) §Paso 3, con capturas de los tres botones y del modal de Observar.
