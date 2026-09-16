---
id: 2026-09-15_iniciativa-titularidad-tarjeta-prd-formalizado
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Skill /idea_prd sobre titularidad_tarjeta (PRD-25)"
producto: Adquirencia (Botón Simple)
tema: PRD v1.0 de titularidad_tarjeta formalizado
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
proyecto: titularidad_tarjeta
---

Se formalizó el PRD v1.0 del proyecto de validación de titularidad de tarjeta (PRD-25 en Jira): valida con la API VaTa de MODO después de que el motor antifraude interno analice la transacción, solo si este no la rechaza por motivos propios. El diseño de manejo de respuestas se simplificó el mismo día — todo código 409 de MODO rechaza la transacción, sin distinguir el motivo específico (corregido tras una charla del PM con Pablo Gomes, reemplaza el criterio más granular que se había acordado antes). El componente de integración se diseña como servicio reutilizable, no exclusivo del checkout de pago con tarjeta, pensando en un futuro consumidor en el canal de cobro presencial (POS) — esa extensión queda fuera de este proyecto, registrada por separado como oportunidad candidata.

El checklist de 7 áreas quedó completo, con la mayoría de las filas en estado Pendiente: Fraude no validó formalmente el diseño de secuencia/resiliencia (aunque sigue el mismo criterio ya vigente para el motor antifraude propio), Legales tiene que revisar y firmar el contrato con el proveedor externo (incluye datos personales), Soporte necesita capacitación sobre el nuevo motivo de rechazo, Comercial no definió si el control se comunica/factura a los comercios, e IT necesita confirmar si el proveedor ofrece ambiente de pruebas. Ninguna de estas quedó registrada como tarea de Producto — quedan documentadas en el propio PRD para que las levante el proceso de preparación de lanzamiento cuando llegue el momento.
