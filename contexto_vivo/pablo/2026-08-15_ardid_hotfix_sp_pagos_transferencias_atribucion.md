---
id: 2026-08-15_ardid_hotfix_sp_pagos_transferencias_atribucion
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión ARDID V 1.18.2.1 HF (publicada 2026-07-22), ticket ARD-32"
producto: ardid
tema: Atribución de versión Jira al hotfix de reintentos de SP ya documentado (§11)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Solo atribución — sin contenido nuevo.** ARD-32 ("Solicitamos aplicar fix de Ardid para resolver problemas de ejecución de los Stored Procedures en PROD... base de datos de SQL correspondiente a los servicios de Pagos y Transferencias") es el ticket Jira del **mismo hotfix ya documentado en `integracion_con_productos_bind.md` §11** ("Incidente de reinicio de límites diarios (2-3 julio) y hotfix de reintentos de Pentass"): coincide la fecha de despliegue (releaseDate de la versión Jira **ARDID V 1.18.2.1 HF** = 2026-07-22, exactamente el miércoles 7:30am mencionado en la minuta de la reunión del 2026-07-17) y el objeto del fix (reintentos automáticos en los SP de Pagos y Transferencias, sin modificar tablas/columnas/SPs existentes).

Ticket sin detalle técnico adicional en Jira más allá de la descripción de la solicitud — el único comentario es una imagen (adjunto PDF `Informe_Incidencia_BindPSP_PROD.pdf` referenciado, no accesible por API/no se intentó Chrome MCP dado que el contenido ya está cubierto en la minuta). Sin Epic Link, sin SP cargados.

**Acción propuesta para el merge:** agregar la fila de esta versión al §10 (línea de tiempo de versiones Jira) y sumar la referencia cruzada `ARD-32 → §11` en el propio §11, para que quede trazable desde ambos lados sin duplicar la narrativa.
