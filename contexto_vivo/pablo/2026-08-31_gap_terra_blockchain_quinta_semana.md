---
id: 2026-08-31_gap_terra_blockchain_quinta_semana
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_metrics — análisis semanal, semana 202635"
producto: wallet
tema: Terra Blockchain — caída sostenida de 5 semanas RESUELTA: cliente dado de baja por Compliance
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Cierre del gap abierto **"[2026-08-04] — /sync_metrics: caídas de cliente sin explicación en la wiki —
Terra Blockchain (Wallet, -75,7%) y Sucredito (NSM#2, -70,9%)"** en `2_areas/gaps_y_preguntas.md`
(actualizado semana a semana desde entonces: 2026-08-11/18/26).

**Resuelto (2026-08-31, confirmado por el usuario).** La caída sostenida de Terra Blockchain, medida
durante cinco semanas consecutivas (−75,7% → −79,5% → −87,9% → −83,6% → −73,0% vs. promedio de 4 semanas;
tendencia 4×4 semanas confirmando −89,8%), **no es un problema de negocio ni un caso de posible churn** —
el cliente fue **dado de baja por Compliance**. La caída medida en las métricas es exactamente el efecto
esperable de esa baja, no una señal de alerta.

**Por qué el patrón se parecía al de un churn real (Octagon):** una baja de Compliance produce la misma
firma estadística que una salida comercial no planificada — caída progresiva a medida que las operaciones
en curso del cliente se liquidan y no se generan nuevas. Sin el contexto de la baja, el detector (y la
lectura de negocio) no podían distinguir un caso del otro.

**Acción tomada:** se retiró la tarea T-036 de `1_proyectos/tareas.md` — el usuario confirmó que los
hallazgos de `/sync_metrics` son informativos y no deben generar tareas de seguimiento por sí solos.

**Estado:** ✅ Resuelto (2026-08-31) — no requiere ninguna acción de Soporte/Comercial. Se cierra este gap;
si Terra Blockchain vuelve a aparecer en futuros hallazgos de "caída de cliente" por algún motivo (ej. un
error de baja mal registrada), tratarlo como caso nuevo, no reabrir este.
