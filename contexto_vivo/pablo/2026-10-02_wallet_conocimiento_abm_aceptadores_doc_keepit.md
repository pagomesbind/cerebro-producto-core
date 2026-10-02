---
id: 2026-10-02_wallet_conocimiento_abm_aceptadores_doc_keepit
pm: pablo
fecha_captura: 2026-10-02
fuente: "/sync_mails — hilo \"Gestión de Aceptadores QR\" (threadId 1a0fc5e4f47e7e8a), Martín Hovanyecz (Keep IT Simple), 2026-10-02"
producto: wallet
tema: Documentación funcional del nuevo desarrollo de gestión de aceptadores (ABM) — habilitación automática de QR, endpoints de Consulta/Asignación/Habilitación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ecosistema_wallet_adquirencia/gestion_aceptadores_qr.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

Martín Hovanyecz (Keep IT Simple) envió la documentación funcional del nuevo desarrollo de **gestión de aceptadores (ABM)** — corresponde a la Historia WS-1601 ("Gestión de aceptadores con mecanismo de autenticación configurable") empaquetada en la versión 73 de Wallet junto con el proyecto `getnet_oauth2_resolve/` (PRD-237, despliegue a producción confirmado 08/10/2026, ver `getnet_oauth2_resolve/proyecto.md §8`).

**Alcance descrito en el mail (cuerpo del mensaje, no se leyó el adjunto HTML todavía — queda pendiente de lectura manual, ver nota abajo):**
- Flujos de habilitación automática de QR para aceptadores.
- Endpoints de **Consulta**, **Asignación** y **Habilitación** de QRs.
- Todos los endpoints documentados con su lógica y sus **códigos de respuesta/error**.

**Pendiente de lectura manual:** el detalle técnico completo (contratos de request/response, catálogo de códigos) está en el adjunto `gestion-aceptadores-documentacion-negocio.html`, no descargado automáticamente por esta skill. Cuando se lea, el contenido debe fusionarse en este mismo archivo temático (no crear uno nuevo).

**Reacción de Pablo Gomes (mismo hilo, 2026-10-02):** confirmó que la documentación "está muy clara y completa", destacó puntualmente que incluya los códigos de error existentes, y pidió que este mismo formato (endpoints + códigos de error) se adopte como entregable estándar al cerrar cualquier proyecto a futuro, para extendérselo a los equipos de Soporte en el momento en que el proyecto pasa a producción — ver item de decisión relacionado `2026-10-02_transversal_decision_estandar_documentacion_cierre_proyecto`.

> Fuente: hilo de mail "Gestión de Aceptadores QR" — Martín Hovanyecz (Keep IT Simple) / Pablo Gomes, 2026-10-02, threadId `1a0fc5e4f47e7e8a`.
