---
id: 2026-08-31_servicios-restricciones-coelsa-alias-cbu
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Daily producto\" (2026-08-28)"
producto: servicios
tema: Restricciones de Coelsa sobre asignación/modificación de alias de CBU, relevantes para el checkout de Botón Simple 2.0 (Pago Fácil)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Daily producto" (2026-08-28, Pablo Gomes con Nicolás Colón, probando el flujo de las skills `/idea_start` sobre un pedido real) se analizó un requerimiento informal de Adriana (comercial) para el cliente Pago Fácil: mostrar el alias del CBU junto al CBU numérico en la opción de transferencia del checkout de Botón Simple 2.0.

Hallazgos técnicos sobre el mecanismo de Coelsa, aplicables a cualquier CBU de la plataforma (no solo Pago Fácil):

- El sistema hoy genera lotes de CBU asociados a una entidad (en este caso, Pago Fácil) que se reciclan entre **todos los comercios de esa misma entidad** — el reciclaje es a nivel entidad, no comercio. En la creación inicial de esos lotes **no se invoca la asignación de alias**.
- **Coelsa exige obligatoriamente un alias para todo CBU**: si la plataforma no lo asigna en un plazo de 5 segundos, Coelsa le asigna uno arbitrario de forma automática (ejemplo real visto en pruebas: `pies.farol`). Esto cambia el enfoque del problema — no es que falte un alias, es que ya existe uno (aleatorio, generado por Coelsa) que Bind PSP no persiste en base ni muestra en la interfaz.
- **Restricción de modificación**: no se permite asignar o modificar el alias vinculado a un CBU en un plazo menor a 24 horas desde la última modificación, con un límite de 3 a 10 modificaciones por año (la minuta registra ambos números en distintos pasajes — a confirmar el valor exacto).
- Alternativa técnica identificada para evitar consumir el cupo de modificaciones de Coelsa: la API de One Bank (`get cuenta cbu corta y cbu larga`) permite **consultar** (no modificar) el alias ya asignado por Coelsa.

Decisión tomada en la sesión (ver también item de oportunidad relacionado): el alcance de una eventual solución sería general para toda la plataforma (no exclusivo de Pago Fácil), con parametrización por entidad/comercio para habilitar la visibilidad, consultando el alias vía la API existente al asignar el CBU y persistiéndolo — posponiendo cualquier asignación de alias personalizado/custom.
