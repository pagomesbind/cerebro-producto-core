---
id: 2026-09-10_conocimiento-ardid-segmentacion-personas-juridicas-por-cuit
pm: nicolas
fecha_captura: 2026-09-10
fuente: "Reunión \"ARDID\" (2026-09-09, 15:30), minuta + transcripción Gemini"
producto: ardid
tema: Falta de identificación automática de cuentas de personas jurídicas en ARDID; propuesta de segmentación por prefijo de CUIT
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En el marco del nuevo límite operativo para cuentas de personas jurídicas (ver gap asociado sobre el monto exacto, `2026-09-10_gap-contradiccion-limite-operativo-personas-juridicas-1000-vs-10000`), surgió en la reunión "ARDID" (2026-09-09) que **el sistema no tiene hoy un método automático para distinguir si una CBU/CVU corresponde a una persona jurídica**: las cuentas de personas jurídicas se registran bajo el mismo segmento ARDID que las personas físicas, pese a tener CUIT (en vez de CUIL).

**Propuesta técnica (Nicolás Colón, 00:05:19):** adaptar el alta de cuentas en Wallet para identificar personas jurídicas cuando el CUIT comienza con el prefijo **"30"**, y usar esa identificación para asignarles un segmento distinto en ARDID. Mariana Nadalin (Ardid/Akurtech) coincidió en que sería la mejor opción, pero aclaró que **hoy esa integración no existe**: Wallet tiene la lógica de identificación de CUIT pero no actúa directamente sobre ARDID (00:06:24).

**Estado de la decisión:** "Requiere más debate" — queda pendiente de validación con el equipo correspondiente.

**Gestión de cuentas existentes vs. nuevas:** para las cuentas de personas jurídicas ya creadas, Mariana Nadalin explicó que se puede migrar manualmente creando un nuevo segmento en ARDID, pero advirtió que gestionar las cuentas **nuevas** de esta forma requeriría consultas diarias manuales a la billetera — calificado como inviable a escala (00:07:36).

**Próximos pasos (Nicolás Colón):** hablar con el equipo de Wallet sobre la identificación automática de personas jurídicas en el alta, y consultar con Pablo Gomes por una alternativa más directa de segmentación (ver tareas T-041/T-042 en `tareas.md`).

**Tema aparte, mismo encuentro:** durante la revisión conjunta de reglas de transferencia salientes/entrantes por tipo de cliente y empresa, Mariana Nadalin advirtió que Matías Alzogaray ("Mati") podría no estar de acuerdo con la modificación de prioridades que esto implica; se acordó igualmente abrir un ticket en PMC siguiendo sus indicaciones (ver tarea T-043).

> Fuente: Reunión "ARDID" (2026-09-09, 15:30), minuta y transcripción Gemini.
