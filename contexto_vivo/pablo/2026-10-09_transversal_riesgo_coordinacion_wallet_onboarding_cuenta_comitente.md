---
id: 2026-10-09_transversal_riesgo_coordinacion_wallet_onboarding_cuenta_comitente
pm: pablo
fecha_captura: 2026-10-09
fuente: "/sync_mails — mail 'Informe Estado Proyectos Emisión al 08/10/2026' (threadId 1a11cec7ef70f307), Nicolás Pomponio (Fintexa PM), 2026-10-08, con respuesta de Emma Vignoles"
producto: transversal
tema: Gap de coordinación entre los equipos de Wallet y Onboarding en desarrollos conjuntos (cuenta comitente) — requerimiento de datos no quedó claro, tickets bloqueados y riesgo detectado a 1 día del pase a producción
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Del informe semanal de estado de proyectos de Wallet (Nicolás Pomponio, PM de Fintexa) al 08/10/2026, con comentario crítico de Emma Vignoles sobre la gestión del punto.

**El problema:** en los desarrollos que se hacen en conjunto entre Wallet y Onboarding — como crear comitente desde Onboarding — surgió una diferencia de criterio sobre qué datos debe enviar Onboarding, porque el requerimiento no quedó del todo claro entre ambos equipos. Por este motivo, los tickets de "cuenta comitente" quedaron bloqueados durante la versión W73.

**Cómo se evidenció:** a un día del pasaje a producción de la W73 (miércoles 07/10, el pasaje fue el jueves 08/10) todavía fue necesario convocar una reunión de urgencia para alinear dependencias del flujo que no estaban resueltas — Fintexa lo marca explícitamente como "oportunidad de mejora en la coordinación previa entre ambos proyectos". Emma Vignoles (Producto) calificó esto como "flojo desde la gestión": "¿Entre todos, no poder coordinar la interdependencia entre OB y Cta Cte... a 1 día del pase a PROD?".

**Propuesta de Fintexa para prevenirlo a futuro:** incorporar con mayor frecuencia al equipo de Onboarding en las reuniones de refinamiento de Wallet, para anticipar estas dependencias antes de que impacten en las fechas de entrega. Próximo accionable concreto: reunión funcional dedicada para alinear qué datos exactamente debe enviar Onboarding para la creación de cuenta comitente.

**Contexto de la versión (para referencia, no es el foco del riesgo):** la W73 pasó a producción el 08/10/2026 con 2 historias con defecto, 1 bloqueada (la de cuenta comitente) y 6 en QA Externo; demoró 2:30hs con la regresión incluida. Desde el pase, toda la operatoria de Wallet pasa por Ardid (dato ya conocido de un item previo del Cerebro). La fecha límite de pase a producción de la W74 quedó fijada en jueves 29/10 — las historias que no cierren refinamiento a tiempo quedan afuera de esa versión.

**No se identificó un proyecto propio de Pablo en `1_proyectos/` para este punto** — es una dependencia cruzada Wallet↔Onboarding gestionada por Fintexa/Emma Vignoles, no un proyecto trackeado individualmente. Se captura como riesgo de proceso transversal (recurrencia de coordinación tardía entre equipos a días del pase a producción).

> Fuente: mail "Informe Estado Proyectos Emisión al 08/10/2026" (threadId `1a11cec7ef70f307`), Nicolás Pomponio (Fintexa) / Emma Vignoles, 2026-10-08.

**Actualización 2026-10-09 (mismo hilo, respuesta de Pablo Serra — Delivery Manager de Fintexa):**
- Sobre el reclamo de Emma: Pablo Serra se compromete a hablarlo con Matías Alzogaray para definir cómo coordinar mejor los 3 equipos (Wallet, Onboarding, Producto) — cómo identificar las interdependencias, cómo gestionarlas y cómo asegurar la presencia de los referentes en las reuniones clave. Sin resolución concreta todavía, solo compromiso de abordarlo.
- Sobre si "desde el pase de la W73 toda la operatoria de Wallet pasa por Ardid" está bien: Pablo Serra aclara que no puede confirmarlo porque no fue una definición del equipo de Desarrollo — punto que queda sin cerrar.
- **Precisión de fecha:** la fecha límite de refinamiento de historias para la W74 es el **miércoles 14/10** (no confundir con el jueves 29/10, que es la fecha límite de pase a producción de la versión completa).
