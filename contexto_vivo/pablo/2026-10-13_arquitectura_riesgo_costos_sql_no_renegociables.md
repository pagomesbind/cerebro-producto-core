---
id: 2026-10-13_arquitectura_riesgo_costos_sql_no_renegociables
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-10-13, 11:01)"
producto: transversal
tema: Costos de SQL representan el 39% de la infraestructura, sin posibilidad de renegociar reservas hasta enero de 2027
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## Riesgo

Daniel Zalazar (Fintexa) informó que los **costos de SQL representan el 39% del gasto total de infraestructura**, y que las reservas contratadas **no pueden renegociarse hasta enero de 2027** sin incurrir en penalizaciones severas. Emma Vignoles expresó frustración por este costo elevado combinado con la falta de depuración de bases de datos (la depuración programada para esa mañana no se había ejecutado por sobrecarga del equipo con pases y staging).

## Por qué es un riesgo

- El costo de infraestructura sigue creciendo mientras la depuración de bases (que reduciría el volumen y potencialmente el costo) se posterga reiteradamente por falta de ventana operativa.
- No hay margen de negociación comercial hasta enero de 2027, es decir, cualquier optimización de costo en el corto plazo depende exclusivamente de medidas técnicas internas (depuración, escalado automático/Zero Downtime en curso), no de renegociar el contrato.
- Conecta con el gap ya abierto `2026-10-06_transversal_gap_depuracion_registros_wallet_retencion` (todavía `en_cola`): la depuración de Wallet se ejecutó finalmente sin participación confirmada de Compliance/PLD (ver `tareas.md` T-216) — revisar si el mismo patrón de "depuración urgente por costo, sin gobernanza regulatoria" se repite acá.

## Mitigación en curso (sin resolver el riesgo de fondo)

Daniel Zalazar se comprometió a enviar los cálculos detallados y revisar el asunto con Hernán Clarich. El escalado automático de bases de datos ("Zero Downtime") ya es un proyecto arquitectónico independiente (ver decisión `2026-10-06_arquitectura_decision_escalado_bd_proyecto_independiente`, ya `en_cola`).

> Fuente: reunión "Repaso Semanal líderes", 2026-10-13 11:01hs.
