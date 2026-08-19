---
id: 2026-08-15_wallet_totalizadores_bff_onboarding_w71
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15), ticket WS-1277"
producto: wallet
tema: Totalizadores Coelsa expuestos también en el BFF de Onboarding
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Nota para agregar al final de §4 "Documentación — Consulta totalizadores CBU/CVU": el endpoint `GET /walletentidad-cuenta/v1/api/v1.201/GetTotalizadoresCoelsa?cuit={cuit}&formaConsulta={formaConsulta}` (documentado ahí) ahora también se expone en el **BFF que consume el onboarding** (WS-1277, W 71), autenticando con el header `x-entidad` = Id de organización — permite que el flujo de onboarding consulte totalizadores sin pasar por el BFF de Wallet estándar.
