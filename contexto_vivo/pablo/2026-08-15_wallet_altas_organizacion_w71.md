---
id: 2026-08-15_wallet_altas_organizacion_w71
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, tickets WS-1432+WS-1431/W71.3 FIX, WS-1470/W71.7 FIX, WS-1429/W71.4 FIX, WS-1444/W71.6 FIX"
producto: wallet
tema: Altas de organización y pasaje a PROD de AuthExternal V2 — tramo W71
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: capturado
merge_commit:
---

Nueva sección "7. Historial de altas de organización y migraciones — tramo W71" (continúa el patrón de §1-2 con casos reales):

- **HAPSA (org 62, WS-1432, W 71.3 FIX):** configuración de app setting `x-entidad` para que el onboarding exitoso de HAPSA cree CVU directamente en la organización 62.
- **App Android de demo en PROD (org 64, WS-1431, W 71.3 FIX):** se crea una app "DEMO" en producción para que Bind PSP haga demos/pruebas productivas — apunta a una organización creada solo para ese fin, nunca se publica en las app stores. Alcance funcional: todo excepto viaje QR e ingresar dinero con TIN en puestos físicos; sí incluye lo más nuevo (DEBIN recurrente, ingresar dinero con tarjetas).
- **Organización 66 — PAFX (WS-1470, W 71.7 FIX):** alta de app setting del WalletBFF en PRODUCCIÓN para la organización PAFX (`AltaUsuarioWallet: false`, `UsuarioMail: false`, versiones `APIPAFX`/`APKPAFX`/`IPAPAFX`) — nueva organización habilitada en prod, sin más contexto de negocio en el ticket.
- **Pasaje a PROD de AuthExternal V2, por etapas (WS-1429 relevamiento/soporte técnico W 71.4 FIX; WS-1444 etapa 2/3 W 71.6 FIX):** migración de autenticación externa en curso, por microservicios. La etapa cubierta en esta ingesta migra **Wallet.BIND** y **SharedDebin**. Sin detalle de qué etapas ya pasaron ni cuántas faltan — gap de visibilidad del roadmap completo de esta migración.
