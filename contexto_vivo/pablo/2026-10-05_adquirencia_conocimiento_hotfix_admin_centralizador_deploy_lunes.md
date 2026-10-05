---
id: 2026-10-05_adquirencia_conocimiento_hotfix_admin_centralizador_deploy_lunes
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_mails — mail \"RE: Informe Semanal Adquirencia\" (threadId `19f716b9523ce741`, mensaje `1a0fe4998606d688`), Melisa Belpassi (Fintexa), 2026-10-02"
producto: adquirencia
tema: Avance del hotfix DAD-3428 (falla de control de acceso del Admin Centralizador) — en QA externo, deploy confirmado lunes 05/10
tipo: conocimiento
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "2_areas/riesgos.md §\"Falla de control de acceso preexistente en el Admin Centralizador\" — actualiza el estado de la corrección: la fecha estimada ahí era \"a mediados de la semana del 28/09\"; el informe semanal de Adquirencia del 02/10 confirma que el hotfix (DAD-3428, corrección del incidente DAD-3412/AD-1821) recién estaba en QA externo (Pentass probando del lado de Bind) a esa fecha, con salida confirmada en el pasaje intermedio del lunes 05/10/2026 (junto con DAD-3512)."
confianza: alta
estado: en_cola
merge_commit:
---

El informe semanal de Adquirencia (Fintexa, Melisa Belpassi, informe al 02/10/2026) confirma que el hotfix de seguridad DAD-3428 — corrección de la falla de control de acceso preexistente del Admin Centralizador (incidente DAD-3412/AD-1821, CVSS 8.7, ya documentada en `2_areas/riesgos.md`) — se desarrolló y entregó a QA externo, con Pentass realizando las pruebas del lado de Bind. Confirmado para salir en el **pasaje intermedio del lunes 5 de octubre**, junto con el ticket DAD-3512 ("[Botón 2.0] Permitir devolver transferencias mayores a 30 días", que ya estaba en staging en fase de pruebas).

Esto corrige/precisa la estimación previa registrada en `riesgos.md` ("a mediados de la semana que viene" desde el 25/09, es decir semana del 28/09) — el hotfix terminó corriéndose casi una semana más tarde de lo estimado originalmente.

> Fuente: mail "RE: Informe Semanal Adquirencia", Melisa Belpassi (Fintexa), informe al 02/10/2026.
