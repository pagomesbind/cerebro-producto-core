---
id: 2026-10-07_adquirencia_riesgo_pan_en_claro_auditoria_pos_prisma
pm: pablo
fecha_captura: 2026-10-07
fuente: "sesión directa con el PM (PRD-70, POS con Prisma) — tabla de mapeo de campos de respuesta de Prisma a la transacción, entregada por Fintexa al PM; la fila de `dataAdquirente.Pan` indica `PaymentCard.PAN`, en claro, anotada como CWE-312"
producto: adquirencia
tema: el número de tarjeta (PAN) completo se guardaría sin cifrar en la tabla de Auditoría de los cobros POS por Prisma
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Qué dice la fuente.** En el mapeo que Fintexa le pasó al PM, el campo `dataAdquirente.Pan` de la respuesta de Prisma se guarda "solo en Auditoría", en `PaymentCard.PAN`, **en claro**, con la anotación CWE-312 (almacenamiento de información sensible sin cifrar). No queda claro si esa anotación la puso Fintexa o quien armó la tabla a partir del código.

**Por qué importa.** PCI DSS exige que el PAN esté ilegible dondequiera que se almacene (v4.0, req. 3.5.1) y que, al mostrarse, se enmascare con un máximo de BIN y últimos 4 dígitos (req. 3.4.1) — a validar con el QSA de Bind PSP, que es quien confirma el alcance exacto. Bind PSP mantiene su propia certificación PCI DSS (ver `3_recursos/cumplimiento_normativo/pci_dss_recertificacion.md`) y ya hay un gap abierto sobre la certificación del proveedor Fintexa (`2_areas/gaps_y_preguntas.md`); un PAN completo legible en una tabla de auditoría ampliaría el alcance PCI y el impacto de cualquier acceso indebido a esa tabla.

**Qué no sabemos (confianza media).**
- Si la tabla de Auditoría está cifrada en reposo, o si "en claro" describe solo la columna.
- Quién tiene acceso y con qué retención.
- Si el mismo comportamiento aplica al otro procesador del POS (Global Processing) y a los pagos con tarjeta no presente, o solo a esta integración.

**Siguiente paso propuesto.** Preguntarle a Fintexa por escrito (cifrado en reposo, accesos, retención, alcance) antes de ampliar lo que se guarda de cada transacción. Cruza con la tarea T-192 (mapeo de campos) en `1_proyectos/tareas.md`.
