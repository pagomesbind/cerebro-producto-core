---
id: 2026-10-08_cumplimiento_conocimiento_bcra_anexo_b_estado_directorio
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reuniones 'Anexo-B y GAP' (2026-10-07, 18:00) y 'BIND PSP Anexo B a presentar al BCRA' (2026-10-08, 10:27, con Directorio Bind/Banco Industrial)"
producto: transversal
tema: Estado de cumplimiento del Anexo B BCRA al 08/10 — porcentajes, brechas por área, presupuesto DRP y gobernanza
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/anexo_b_bcra.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto

Dos reuniones consecutivas (07/10 con el equipo de Compliance/Tecnología — Hernán Clarich, Mariana Nadalin, Emma Vignoles, Pablo Gomes — y 08/10 con Directorio de Bind/Banco Industrial) repasaron el estado real de cumplimiento del Anexo B antes de la presentación formal del martes 13/10. Complementa (no contradice) lo ya capturado el 2026-10-13 sobre el calendario de inspección del BCRA (26/10-27/11/2026).

## Estado de cumplimiento (08/10, reportado por Hernán Clarich a Directorio)

- **Cumplimiento global del Anexo B: 44%, subiendo a ~50%** al momento de la reunión del 08/10 (venía de un análisis con LLM cargando normativa + documentación existente, reportado el 07/10).
- Sobre **66 puntos normativos analizados** (normas 7724 y 7783/"777" según transcripción): **15 de incumplimiento total, 29 de cumplimiento parcial, 16 brechas documentales**.
- **Gobierno corporativo es el área más débil: 22% de cumplimiento** — falta independencia formal del CISO, comité de gobierno de tecnología y seguridad, plan estratégico, presupuesto dedicado y matriz de responsabilidades con terceros.
- Otras áreas evaluadas prioritariamente por el regulador: **ciberseguridad** y **terceras partes** (incluye fraude y billetera como servicio — "Billetera como Servicio"/BaaS).
- El **25% de las respuestas del Anexo B serán auditadas** por el inspector del BCRA con evidencia verificable — gran parte ya cubierta por la documentación de certificación PCI DSS (Bind está cerrando su 4ª recertificación).
- **Criterio acordado con Directorio:** reportar porcentajes de cumplimiento **conservadores** (ej. 12,5% o 20% en vez de inflar la cifra), siempre respaldados por un plan de acción detallado paso a paso en Excel (hitos y plazos) — no documentos formales vacíos de ejecución real. El foco debe estar en procesos operativos reales del día a día.

## Documentación a crear/modificar

- **17 documentos de política existentes a modificar + 6 políticas nuevas a crear** (cifra repetida en ambas reuniones; en el detalle del 07/10 Hernán habla de "11 a modificar + 6 nuevas" para la línea específica de políticas de seguridad — hay una pequeña discrepancia de conteo entre las dos reuniones, probablemente por cómo se agrupan, sin resolver explícitamente cuál es la cifra final).
- Políticas nuevas cubren: gestión de riesgos, terceras partes, canales digitales — algunas (ej. ciberresiliencia) ya tienen borradores adaptados del banco.

## Costos de infraestructura (DRP/réplicas)

- Para cumplir el requisito de resiliencia (RTO) y la auditoría de pagos (PCI), Bind debe implementar una réplica de base de datos que reduzca el RTO catastrófico de **30 minutos a 15 minutos o menos**.
- Costo adicional estimado: **~USD 3.800/mes** (incluye billeteras, operaciones y botones de pago) → **~USD 46.000/año**. Se decidió dar visibilidad al Directorio sobre este consumo adicional como inevitable, sin alternativas viables de reducción de otro lado.

## Terceros críticos identificados

Fintexa (desarrollo y conciliación), Ardid/Akurtech (Pentass), Worldsys/Wersis, Asure, Tango — contratos en revisión/firma para estandarizar roles, responsabilidades y facultades de auditoría. Comentario adicional: **Senco** (otro cliente/entidad, contexto no explicitado) también debe presentar el Anexo B completo, con auditoría el 26/10.

## Gobernanza y CISO

- Se definió conformar el **comité de gobierno y seguridad retroactivamente en agosto** (coincidiendo con la entrada en vigencia de la normativa), con acta a redactar sin incluir nombres de personas específicas (delegación de funciones).
- **Lucas Paus será designado CISO** formalmente, con revisión y aprobación final de las políticas de seguridad a su cargo.
- Pendiente: resolver observaciones de auditoría interna de años anteriores, reevaluando/reduciendo el nivel de riesgo de las que ya no son significativas.

## Retención de registros

Requisito regulatorio de retener ciertos registros **12 meses en formato inalterable (solo lectura)** — hoy Bind retiene 90-120 días. Ampliar a 12 meses con almacenamiento no reescribible implica un costo adicional menor. **Conecta con el gap `2026-10-06_transversal_gap_depuracion_registros_wallet_retencion`** (todavía `en_cola`): la depuración de bases de Wallet programada sin participación de Compliance/PLD podría entrar en tensión directa con este requisito de 12 meses — revisar ambos juntos al mergear.

## Onboarding/legajos y auditoría a clientes/subcontratistas

- Discusión sobre la falta de control del 100% de los legajos cuando la organización cliente hace la mayor parte de las altas (Pablo Gomes planteó esto explícitamente) — Mariana Nadalin insistió en que es indispensable recopilar y respaldar todo el stock de legajos para las auditorías.
- El regulador extiende sus exigencias hasta los subcontratistas de los clientes (caso Fintexa mencionado explícitamente).
- Acordado: documentar formalmente el proceso de monitoreo transaccional/revisión de legajos (hoy reactivo, basado en umbrales/solicitudes puntuales, sin procedimiento escrito) — tarea para hacer junto a Diego.

## Ciberincidente de abril

Se confirmó la presentación formal, en el registro oficial de ciberincidentes del BCRA, del episodio ocurrido en abril (mismo procedimiento ya usado para otro caso similar). Requerimientos recientes de información del BCRA también tocan antecedentes de la entidad Inter y de "Azul Finanzas".

> Fuente: reuniones "Anexo-B y GAP" (07/10/2026, 18:00hs, con Hernán Clarich/Mariana Nadalin/Emma Vignoles) y "BIND PSP Anexo B a presentar al BCRA" (08/10/2026, 10:27hs, con Directorio Bind/Banco Industrial completo).
