---
id: 2026-10-06_iniciativa-bajar-tiempos-qr-coelsa-habilita-consulta-qr-trabados
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Fwd: Nueva respuesta en tu ticket #495865 - Consulta de operación por qr_id_trx PRODUCCION' — Gonzalo Rivera, 2026-10-05 (respuesta de Coelsa del 2026-09-15)"
producto: adquirencia
tema: PRD-199 — Coelsa confirma cómo consultar en producción una operación QRDebin por qr_id_trx (id_psp = 0 en rol billetera), una vía para los pagos QR trabados en estado 4/5
tipo: iniciativa
proyecto: bajar-tiempos-pagos-qr
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

**Novedad de PRD-199 (Bajar tiempos de pagos QR):** Gonzalo Rivera reenvió a los 3 PM la respuesta de Coelsa al ticket #495865 como el frente de "demora de los pagos QR cuando quedan con estado 4 o 5". Coelsa confirma que una operación QRDebin se consulta con `GET /apiDebinV1/QR/QRDebin/{qr_id_trx}/{id_psp}` y que, cuando Bind es la billetera y no hay PSP vendedor, `id_psp` va en `0`.

Esto destraba, al menos en lo documental, el problema que quedó abierto en la reunión del 31/08. Hasta ahora no había una forma estándar de reconsultar en Coelsa los QR que quedan en estado indeterminado, y eso explica los reclamos de BSF y Global66. Falta que Fintexa/Keep IT Simple confirmen que funciona con los casos reales y decidir si se automatiza (State Monitor) o queda como herramienta de Soporte. Ver `2026-10-06_conocimiento-coelsa-consulta-qrdebin-por-qr-id-trx-id-psp-0-billetera`.
