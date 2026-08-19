---
id: 2026-08-19_wallet_ccl_deploy_pese_a_regresiones
pm: pablo
fecha_captura: 2026-08-19
fuente: "/sync_mails — mail 'Re: MINUTA: Análisis de riesgo Emisión V 72' (malzogaray@bind.com.ar, 2026-08-18, minuta de la reunión de PRE-Despliegue V72 del mismo día)"
producto: wallet
tema: Dólar CCL — despliegue V72 aprobado pese a regresiones sin cerrar (bloqueo en Apibank homologación)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En la reunión de PRE-Despliegue de Emisión V72 (18/08/2026, 14:30) se aprobó avanzar con el despliegue de los cambios de **Dólar CCL** pese a no poder finalizar las pruebas de regresión en ambiente de homologación, por errores persistentes originados en **Apibank** (ambiente de homologación, no productivo). Se confirmó que el impacto de este bloqueo es mínimo — afecta solo a un ticket de compra de dólar fallida detectado desde visión interna. Para no desenfocar al equipo de QA (Ana), se dispuso centralizar toda la comunicación técnica sobre este tema exclusivamente a través de Andrea Orsini.

Queda en Stand-by/Parking Lot la corrección definitiva de los errores de Apibank (reportados vía Poison) que bloquean hoy las pruebas end-to-end de CCL en ambientes no productivos — no resuelto para el despliegue del 19/08.

> Fuente: Mail "Re: MINUTA: Análisis de riesgo Emisión V 72: Mié, 12 de ago de 2026 a las 11:30am – 12:00pm (GMT-03)" — malzogaray@bind.com.ar (2026-08-18), minuta de la reunión de PRE-Despliegue V72 del 18/08 a las 14:30.
