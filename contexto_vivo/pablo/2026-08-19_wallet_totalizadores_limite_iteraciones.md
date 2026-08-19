---
id: 2026-08-19_wallet_totalizadores_limite_iteraciones
pm: pablo
fecha_captura: 2026-08-19
fuente: "/sync_mails — mail 'Re: MINUTA: Análisis de riesgo Emisión V 72' (malzogaray@bind.com.ar, 2026-08-18, minuta de la reunión de PRE-Despliegue V72 del mismo día)"
producto: wallet
tema: Validación de Totalizadores CBU/CVU — límite de 30 iteraciones en producción (V72)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En la reunión de PRE-Despliegue de Emisión V72 (18/08/2026, 14:30), dentro de "Configuraciones Técnicas y Endpoints", se definió: **la validación de Totalizadores (CBU, CVU larga y CVU corta) se habilita en producción con un límite estricto de 30 iteraciones** como parte del despliegue de la V72 (desplegado 19/08/2026 06:30-07:30 según la minuta previa del 12/08 del mismo hilo).

En la misma sección se registró una decisión relacionada: **se descartó incorporar CUITs a la lista blanca (whitelist)** de esta validación — la regla aplica exclusivamente a personas físicas, no a personas jurídicas.

> Fuente: Mail "Re: MINUTA: Análisis de riesgo Emisión V 72: Mié, 12 de ago de 2026 a las 11:30am – 12:00pm (GMT-03)" — malzogaray@bind.com.ar (2026-08-18), minuta de la reunión de PRE-Despliegue V72 del 18/08 a las 14:30.
