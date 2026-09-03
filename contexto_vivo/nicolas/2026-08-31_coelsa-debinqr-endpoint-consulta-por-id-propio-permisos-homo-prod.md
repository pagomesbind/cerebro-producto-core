---
id: 2026-08-31_coelsa-debinqr-endpoint-consulta-por-id-propio-permisos-homo-prod
pm: nicolas
fecha_captura: 2026-09-01
fuente: "Mail \"Permisos COELSA debin HOMO y PROD\" — Agustín Grau (Fintexa, CTO) a grivera@bind.com.ar y ncolon@bind.com.ar, cc security@tecfinanciera.com (2026-08-31)"
producto: wallet
tema: Endpoint de Coelsa para consultar el estado de una operación DEBIN (incluye DEBINQR) por ID propio, y usuarios Coelsa habilitados por ambiente
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/debin_y_fondeo.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Fintexa (Agustín Grau, CTO) pidió habilitar permisos en Coelsa para poder probar y validar la consulta de una operación DEBIN por ID propio (`ori_trx_id`) — el caso de uso mencionado explícitamente es **DEBINQR**. El endpoint de Coelsa a habilitar:

```
GET /apiDebinV1/Debin/Debin3/{ori_trx_id}/{tipo_operacion}/{idPsp}
```

Usuarios de Coelsa para API Debin que se mencionan en el pedido:
- **HOMO:** `qrihomoandinas`
- **PROD:** `qriandinas`

**Contexto:** este endpoint parece ser la vía de consulta de estado por ID propio para DEBIN/DEBINQR — complementario al endpoint ya documentado en `debin_y_fondeo.md` (`GET .../debins/{id}/psp/{idPsp}`, usado en el flujo de contracargos para traer la operación DEBIN original) y a la reactivación de Transferencias Pull en curso con Coelsa (ticket #456632, ver T-011 en `tareas.md` y `contexto_vivo/2026-08-31_coelsa-psp-url-modificacion-no-impacta-en-consulta.md`) — no está confirmado si son el mismo frente de trabajo o dos pedidos de acceso independientes a la misma familia de APIs de Coelsa.

**Sin acción de Producto identificada en el mail:** el pedido está dirigido al equipo técnico (Gonzalo Rivera) con el PM en copia directa ("to"), sin pedido explícito de definición o aprobación de Producto — se captura como conocimiento técnico, no se abrió tarea.

**Actualización (2026-09-02) — resuelto, y confirmado que es un frente independiente:** Gonzalo Rivera cargó el pedido como ticket interno propio (**MDA-295641** en `bindtm.atlassian.net`, no en el espacio PRD ni ligado al ticket Coelsa #456632) el 2026-09-01, y confirmó "Listo!" (con captura de pantalla) el 2026-09-02. Con esto se despeja la duda que había quedado abierta: este pedido de permisos DEBINQR es un **frente de acceso independiente** al de la reactivación de Transferencias Pull en Homologación (ticket Coelsa #456632, ver `contexto_vivo/2026-08-31_coelsa-psp-url-modificacion-no-impacta-en-consulta.md` y T-011 en `tareas.md`) — ambos tocan la misma familia de APIs de Coelsa pero son solicitudes de acceso separadas.

> Fuente: Mail "Permisos COELSA debin HOMO y PROD" — agustin.grau@fintexa.tech (2026-08-31), con respuestas de grivera@bind.com.ar (2026-09-01 y 2026-09-02).
