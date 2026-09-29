---
id: 2026-09-28_transversal_riesgo_vulnerabilidad_control_acceso_admin_centralizador
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_mails — mail 'Hallazgo de Seguridad en Admin Centralizador. URGENTE.', Melisa Belpassi (Fintexa) → Bind PSP, 2026-09-25 (threadId 1a0d9342080b4610)"
producto: transversal
tema: falla de control de acceso preexistente en el Admin Centralizador — expone datos y operaciones entre organizaciones/entidades distintas
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

## Origen

El 23/09, durante las pruebas de la V73 de Adquirencia, Bind reportó DAD-3412 (AD-1821): un usuario Administrador Nivel 1 de la entidad BS20 visualizaba la entidad RXT en el módulo Entidades del Admin Centralizador. El análisis de Fintexa identificó dos problemas distintos.

## Qué se encontró

- **Caso reportado (severidad baja):** se debe a un filtro que el navegador conserva de una sesión anterior de un usuario interno de Nivel 0. Solo ocurre en equipos donde antes ingresó personal de Soporte, QA o Desarrollo con ese nivel — no lo puede generar un usuario de cliente final.
- **Falla de control de acceso preexistente (severidad alta — CVSS 4.0: 8.7):** el backend no valida que la entidad consultada pertenezca a la organización del usuario, ni que el rol tenga permiso para la operación. **No es un error introducido en la V73: existe desde el origen de la plataforma y está presente en todos los ambientes, incluido producción.**

## Alcance de la explotación

Verificado en producción el 24/09 de forma controlada: con un usuario de prueba con rol "Operador solo lectura" de una entidad, fue posible consultar transacciones y comercios de **otra** entidad. Las pruebas se limitaron a lectura. La falla es explotable por un usuario de cliente final, sin conocimientos avanzados — el análisis de código muestra que, además de lectura, expone operaciones de **modificación y baja**, incluida la configuración de canales y los datos de la cuenta de recaudación.

## ¿Fue explotada por terceros?

Resultado "no verificable" (investigación DAD-3427): no se puede confirmar ni descartar. Se revisaron los registros de acceso de los últimos 7 y luego 30 días sin detectar actividad anómala, pero por la naturaleza de la falla un acceso indebido es indistinguible de uno legítimo en los logs (mismo código de entidad existente, respuesta técnicamente idéntica a una consulta válida). Solo sería detectable un intento con código de entidad inexistente (respuesta de error anómala) — no se encontró ninguno en la ventana revisada. **Conclusión de Fintexa: no hay casos reportados ni evidencia de intentos de explotación en los últimos 30 días, pero no puede garantizarse que la falla no haya sido aprovechada con éxito.**

## Corrección y mitigación

Corrección (DAD-3428) en desarrollo: validar en el backend, en cada operación, que la entidad solicitada corresponda a la organización y nivel del usuario. Pruebas iniciales con resultados favorables. Vía de entrega: **hotfix** (ver item `tipo: decision` del mismo día, `2026-09-28_transversal_decision_hotfix_admin_centralizador`) — según el informe semanal de Adquirencia del 25/09, se espera en producción "a mediados de la semana que viene" (semana del 28/09), sin fecha exacta confirmada.

**Estado:** Abierto — corrección en desarrollo, sin fecha de entrega confirmada al momento de esta captura.

> Fuente: mail "Hallazgo de Seguridad en Admin Centralizador. URGENTE.", Melisa Belpassi (Fintexa), 2026-09-25 15:34 (threadId `1a0d9342080b4610`); confirmación de vía de entrega (hotfix) en el mismo hilo; fecha estimada de resolución vía informe semanal Adquirencia, mail "RE: Informe Semanal Adquirencia", 2026-09-25.
