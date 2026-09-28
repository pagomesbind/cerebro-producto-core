---
id: 2026-09-28_wallet_iniciativa_inter_fondeo_usd_discovery_cerrado
pm: pablo
fecha_captura: 2026-09-28
fuente: "/idea_start — sesión de shaping de inter_fondeo_usd/, cierre del discovery"
producto: wallet
tema: cierre del discovery de ingreso y envío de USD al exterior para Inter
tipo: iniciativa
proyecto: PRD-261
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Novedad:** se cerró el discovery de `inter_fondeo_usd/` (PRD-261 — "Ingreso y envío de dólares al exterior para usuarios con billetera integrada"). El proyecto surgió del pedido de Inter (billetera propia sobre Wallet, lanzada 03/09/2026) de poder ingresar USD bancarizados en Argentina y enviarlos a su cuenta en el exterior desde la misma app.

Dirección (Emma Vignoles, Gustavo) decidió tratarlo como apuesta estratégica más amplia que el pedido puntual de Inter: aplicar sobre Dólar 1Click (el producto vigente de compra de USD con bonos, que ya usan Bind e Inter) el patrón de saldo multimoneda que en su momento se había diseñado para el proyecto Dólar FX — con el objetivo de poder ofrecer "saldo en USD" como producto propio (PSP as a Service) a otros integradores, no solo a Inter. Un segundo cliente grande de Wallet (BSF, ~55% del volumen) mostró interés informal en cuenta en dólares, sin pedido formal todavía.

**Condición dura:** el desarrollo se ejecuta solo si Inter paga (Inter ya pidió presupuesto). Si se aprueba, se arma un equipo ad hoc dedicado, para no competir con la capacidad ya comprometida del roadmap.

**Alternativa aprobada:** construir primero una orquestación acotada (ingreso, retiro a cuenta propia en Argentina, conversión para expatriar), consultando el saldo en vivo al proveedor externo de cambio (IVSA/Poincenot) sin que Bind PSP guarde un saldo propio — diseñada desde el inicio para escalar después a un saldo/ledger multimoneda propio, vendible a otros integradores.

**Estado del proyecto:** discovery cerrado (`-start.md` aprobado por el PM, 2026-09-28), IDEA en Jira PRD-261 en DISCOVERY. Próximo paso: análisis funcional-técnico (`/idea_solution`) una vez que el PM incorpore la documentación técnica actualizada del proveedor externo de cambio de moneda.
