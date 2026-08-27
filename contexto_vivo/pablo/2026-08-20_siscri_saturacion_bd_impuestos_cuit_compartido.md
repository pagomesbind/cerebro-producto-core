---
id: 2026-08-20_siscri_saturacion_bd_impuestos_cuit_compartido
pm: pablo
fecha_captura: 2026-08-20
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-08-20 12:05, docId 1Q3PZO-WuwDNq5HOyW-eoww1KEVJBvwL7-NP9nT3WMkE)"
producto: siscri
tema: Saturación de la base de impuestos por CUIT compartido entre entidades comerciales + regla de liquidación same-day para transacciones online
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/siscri/calculo_impuesto_online_qr.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Problema reportado (Julieta Giménez, Fintexa):** saturación en la base de datos de impuestos (SISCRI) — múltiples entidades comerciales comparten el mismo CUIT, lo que hace que las consultas sean ineficientes (no pueden discriminar por CUIT solo).

**Decisión acordada:** aplicar un **filtro por código de comercio** (en vez de CUIT) para optimizar las consultas.

**Bug de lógica de negocio identificado en la misma discusión:** las transacciones en línea no procesadas en el día quedan en una **cola de espera incorrecta** en vez de resolverse. **Regla de negocio acordada:** las transacciones en línea deben **liquidarse en el mismo día**; si no es posible procesarlas, se **descartan** (no quedan pendientes indefinidamente). Ajuste a coordinar con Sergio (sin apellido registrado en la minuta).

**Relación con conocimiento ya documentado:** `calculo_impuesto_online_qr.md` ya diagnosticó (2026-07-06) el flujo Transaccion→ServiceProcess→LIQ_IMP para QR con alta varianza de latencia (mediana ~1,71h, máximo 5,38h) y evidencia de ráfagas de backlog — este hallazgo de saturación por CUIT compartido es una causa raíz adicional/complementaria de ese mismo backlog, no necesariamente el mismo caso PedidosYa ya resuelto en §7 de ese archivo.

**Confianza media:** no se pudo confirmar en la wiki actual si "Sergio" corresponde a un contacto ya conocido de Fintexa/Bind, ni el nombre exacto del ticket a crear para el escalado de recursos de BD (ver también el ítem de riesgo de escalado de BD, mismo tema, capturado por separado si aplica).

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini.
