---
id: 2026-10-09_cumplimiento_conocimiento_com_b_13117_cpf_obligatoriedad
pm: pablo
fecha_captura: 2026-10-09
fuente: "/idea_start — PDF de la Comunicación \"B\" 13117 del BCRA (10/02/2026) aportado por el PM, discovery PRD-278 \"CPF en onboarding\""
producto: transversal
tema: Com. "B" 13117 BCRA — obligación de reportar y de consultar y usar la Central de Prevención de Fraude (CPF), incluido el onboarding
tipo: conocimiento
destino_propuesto: wiki/3_recursos/cumplimiento_normativo/com_b_13117_cpf_obligatoriedad.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué es

La Comunicación "B" 13117 del BCRA (10/02/2026) está dirigida a entidades financieras, cámaras electrónicas de compensación, **proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP)**, redes de transferencias electrónicas y administradores de esquemas de pago de transferencias electrónicas. Referencia: *Sistema Nacional de Pagos – Transferencias – Normas Complementarias. Central de Prevención de Fraude. Comunicación A 8298. Aclaraciones.* Firman las Gerencias Principales de Seguridad de la Información y de Sistemas de Pago y Cuentas Corrientes.

Es un recordatorio: lo indicado en el **punto 2.6 del texto ordenado "Sistema Nacional de Pagos – Transferencias – Normas Complementarias" es de cumplimiento obligatorio** para entidades financieras, PSPCP y administradores de esquemas de transferencias inmediatas. Bind PSP es PSPCP, así que está alcanzada.

## Qué implica para la CPF (texto de la norma)

- **a) Reportar.** Todas las entidades financieras y PSPCP deben reportar a la CPF la información de **todos los eventos de fraude de sus clientes**, según las reglas acordadas en el marco de la CIMPRA y la documentación que pone a disposición Coelsa.
- **b) Consultar y utilizar.** Todas las entidades financieras, PSPCP y administradores de esquemas de transferencias inmediatas deben **consultar y utilizar la información registrada en la CPF para prevenir eventos de fraude** en los procesos relacionados con sus clientes. La norma da ejemplos: transferencias inmediatas push o pull, pagos con transferencia, y **el onboarding de nuevos clientes**, "entre otros".

## Totalizadores en el alta

Recuerda además que se deben usar los dos mecanismos del punto 2.3 del Anexo de la Com. "A" 8298, en el marco del punto 3 de ese anexo, e incluye **consultar en el proceso de altas de clientes la interfaz de programación automatizada del punto 2.3.2** (es la API de totalizadores de CBU/CVU por CUIT/CUIL; ver `wallet/conciliacion_y_totalizadores.md`). Esa consulta ya está resuelta en el onboarding de Bind (PRD-118/PRD-200) — no es lo mismo que consultar la CPF.

## Sanciones

"Los sujetos obligados y quienes resulten responsables son pasibles de la aplicación de sanciones conforme a los arts. 41 y 42 de la Ley de Entidades Financieras y disposiciones concordantes" por los incumplimientos que la **SEFYC** constate en su fiscalización.

## Relación con otros documentos del Cerebro

- La planilla **B1e** del Anexo B del BCRA ya citaba "cumplimiento Com. B 13117/CPF" (`gestion_riesgo_tecnologia_seguridad_a7724.md`).
- La Com. "A" 8471 (punto 8 del contenido mínimo del programa antifraude) exige también "mecanismos para reportar y consultar la CPF" (`gestion_riesgo_fraude_bcra.md`).
- Estado de cumplimiento de Bind (a 2026-10-09, según el PM): **no se consulta la CPF en ningún proceso** y los casos de fraude se reportan solo **manualmente**. Proyecto de remediación: PRD-278 "CPF en onboarding" (consulta en el alta). El reporte (inciso a), el screening del stock y el monitoreo transaccional quedan para Ardid / PRD-238.

> Fuente: Com. "B" 13117 BCRA, 10/02/2026 (PDF en `1_proyectos/fraude_en_altas/referencias/fraude_en_altas-bcra_com_b_13117.pdf`); estado de cumplimiento declarado por Pablo Gomes en sesión `/idea_start`, 2026-10-09.
