---
id: 2026-09-30_conocimiento-siscri-wallet-impuestos-100-transaccional-sin-acumulado-mensual
pm: nicolas
fecha_captura: 2026-09-30
fuente: "Mail 'Retenciones SIRTAC COTO' — Sabrina Capdevila (BIND) y respuesta de Alan Martínez (Área Técnica Bind PSP), 2026-09-29"
producto: siscri
tema: El motor de impuestos de Wallet es 100% transaccional — no puede acumular retenciones para descontarlas una vez a fin de mes
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/siscri/integracion_wallet.md
tipo_destino: actualizar
contradice: "no — agrega una limitación explícita al modelo de §1 (asíncrono, no bloqueante, con recycle)"
confianza: alta
estado: en_cola
---

**Limitación confirmada por el Área Técnica (Alan Martínez, 29/09/2026):** el motor de impuestos de Wallet funciona de forma **100% transaccional**. Calcula y descuenta los impuestos en el momento en que se crea cada comprobante. Si en ese momento la cuenta no tiene fondos, manda el débito a **recycle**, que es el mecanismo ya documentado en §1.

**Lo que no soporta hoy:** acumular los montos del período para hacer **un solo descuento el último día del mes**. No existe una modalidad de liquidación mensual acumulada por entidad o por impuesto.

**Contexto del hallazgo:** Sabrina Capdevila (BIND, área de Impuestos) pidió que a **COTO CICSA, "entidad A102"**, se le calculen y descuenten las retenciones de **SIRTAC** el último día de cada mes. Pidió hacerlo como un cambio de configuración. Alan Martínez respondió que el pedido choca con esta limitación técnica. No es un parámetro: sería un desarrollo. El código "A102" se copia tal cual del mail. En el canon, COTO figura en Wallet como entidad 184, así que "A102" podría ser un código de SISCRI o de Impuestos, sin confirmar.

**Relación con lo ya documentado:** en Adquirencia, `calculo_impuesto_online_qr.md` describe el paso a lotes parametrizables. Ese cambio tampoco es una liquidación acumulada mensual: sigue siendo cálculo por transacción, solo que agrupado en el tiempo.

> Fuente: Mail "Retenciones SIRTAC COTO" — Sabrina Capdevila (2026-09-29 10:42 ART) y Alan Martínez (2026-09-29 10:59 ART).
