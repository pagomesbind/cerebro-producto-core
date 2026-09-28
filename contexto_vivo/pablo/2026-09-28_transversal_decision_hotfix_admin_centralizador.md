---
id: 2026-09-28_transversal_decision_hotfix_admin_centralizador
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_mails — mail 'Hallazgo de Seguridad en Admin Centralizador. URGENTE.', Melisa Belpassi (Fintexa) → Bind PSP, 2026-09-25 (threadId 1a0d9342080b4610)"
producto: transversal
tema: decisión de vía de entrega (hotfix vs. versión V74) para la corrección de la falla de seguridad del Admin Centralizador
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Fintexa reportó una falla de seguridad grave en el Admin Centralizador (ver item `tipo: riesgo` capturado el mismo día, `2026-09-28_transversal_riesgo_vulnerabilidad_control_acceso_admin_centralizador`, para el detalle técnico) y propuso dos alternativas de entrega de la corrección (DAD-3428): un hotfix a producción, independiente del calendario de versiones, o incluir la corrección en la V74.

**Decisión (2026-09-25):** hotfix. Pablo Gomes lo votó primero ("Yo voto hotfix"); Mariana Nadalin (COO) coincidió explícitamente ("es un hotfix porque es una vulnerabilidad grande"); Hernán Clarich (Fintexa) reforzó la urgencia ("dado que es replicable en producción y se comprobó, esto tiene alta prioridad"). Sin objeciones de nadie en el hilo — decisión unánime y rápida (dentro de la misma tarde).

Según el informe semanal de Adquirencia del 25/09, la corrección "se está desarrollando y quedará en producción a mediados de la semana que viene" (semana del 28/09) — sin fecha exacta confirmada al momento de esta captura.

> Fuente: mail "Hallazgo de Seguridad en Admin Centralizador. URGENTE.", Melisa Belpassi (Fintexa) → evignoles/mnadalin/hernan.clarich-ext/security@tecfinanciera.com/malzogaray/pagomes/agustin.grau/sebastian.rios/pablo.serra/pablo.vargas/alejandro.sfrede, 2026-09-25 15:34, con respuestas de Pablo Gomes (15:42), Mariana Nadalin (15:45) y Hernán Clarich (16:01) el mismo día.
