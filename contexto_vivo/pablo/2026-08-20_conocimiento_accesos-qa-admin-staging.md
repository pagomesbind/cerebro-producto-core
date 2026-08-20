---
id: 2026-08-20_conocimiento_accesos-qa-admin-staging
pm: pablo
fecha_captura: 2026-08-20
fuente: "Pablo Gomes, directo en chat (sesión /idea_start sobre convenios de entidades/comercios), 2026-08-20"
producto: portal_admin
tema: Credenciales de acceso de prueba al Admin en ambiente STAGING, para inspección visual en futuros QA
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/portal_admin/accesos_qa_staging.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Acceso de prueba al Admin (Centralizador de Cobro) en STAGING**, aportado por el PM para que futuras sesiones de QA/discovery puedan navegar el portal e inspeccionar pantallas sin depender de que el usuario esté presente.

- **URL:** https://admin-staging.epays.services/
- **Usuario:** `Admin@Test`
- **Contraseña:** `AdminTest1234`

**⚠️ Restricción de uso, explícita del PM (no negociable):** este acceso es **solo para navegar e inspeccionar** — nunca para modificar datos. Queda **prohibido clickear cualquier accionable** (guardar, crear, editar, eliminar, habilitar/deshabilitar, etc.) en cualquier sesión que use estas credenciales, sin excepción. Cualquier sesión que las use debe releer y respetar esta restricción antes de interactuar con el portal.

**Nota de riesgo (advertida al PM antes de guardar esto, aceptada expresamente):** este Cerebro corre en un repo git (`CEREBRO BIND PSP`) con push automático diario a un remoto — guardar una contraseña en texto plano en la wiki la deja en el historial de git de ese repo. El PM decidió aceptar el riesgo (ambiente de staging, no productivo) en vez de omitir la contraseña o dejarla fuera del repo.
