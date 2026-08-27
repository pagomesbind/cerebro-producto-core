---
id: 2026-08-26_wallet_ccl_comision_cero_devolucion_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), ticket WS-1351"
producto: wallet
tema: Dólar CCL — identifica y cierra el ticket que §3.6bis dejaba sin nombrar (compra fallida con ComisionInterna=0 no se devolvía)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/dolar_ccl.md §3.6bis — el mail del 2026-08-18 dice 'el impacto de este bloqueo es mínimo, afecta solo a un ticket de compra de dólar fallida detectado desde visión interna' sin nombrarlo. Es WS-1351."
confianza: alta
estado: en_cola
merge_commit:
---

§3.6bis documenta que el despliegue de Emisión V72 se aprobó pese a no poder cerrar las pruebas de regresión en homologación (bloqueadas por errores de Apibank en ese ambiente), señalando que el impacto real era acotado a "un ticket de compra de dólar fallida detectado desde visión interna" — sin identificarlo. Ese ticket es **[WS-1351](https://bindpsp.atlassian.net/browse/WS-1351)**, W 72, 3 SP, Epic WS-79, y quedó publicado (Finalizada) en la misma versión.

**El bug:** en una compra de dólar CCL, si `ComisionInterna` es $0 y la operación es rechazada por Poincenot en la pata 1, el intento de devolución fallaba — el `MS Comprobantes` rechazaba crear un comprobante de cargo por un monto de $0, y el flujo de devolución completo se cortaba ahí (el cliente no recibía su dinero de vuelta).

**Fix:** cuando la comisión a aplicar es $0, directamente no se genera comprobante de cargo — el flujo de devolución continúa sin ese paso. Aplica tanto a compra como a venta de dólar CCL. Validado por Nicolás Colón el 2026-08-04.

**Al mergear:** en §3.6bis, agregar una nota de cierre identificando el ticket ("el ticket referido en el mail es WS-1351, publicado y corregido en W 72") y considerar mover el detalle técnico a §3.6 (lista de "Bugs y aprendizajes reales") como una entrada más, ya que deja de ser un riesgo abierto.
