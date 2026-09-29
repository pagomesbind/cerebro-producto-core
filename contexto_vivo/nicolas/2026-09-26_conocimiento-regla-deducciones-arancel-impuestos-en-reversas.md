---
id: 2026-09-26_conocimiento-regla-deducciones-arancel-impuestos-en-reversas
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Mail 'Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes' — pregunta 3.2 de melisa.belpassi@fintexa.tech y respuesta de pagomes@bind.com.ar (Pablo Gomes), 2026-09-25"
producto: adquirencia
tema: Regla de devolución de arancel, IVA e impuestos en reversas (devoluciones/desconocimientos) de Botón/Cobro — solo se devuelven en reversas totales del mismo día del cobro
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no — llena un vacío: la regla nunca estuvo en los tickets de liquidaciones (AD-1361/AD-1398). Ojo: hoy el comprobante de liquidación devuelve arancel e IVA en CADA reversa, y eso no coincide con la regla confirmada."
confianza: media
estado: ingestado
---

**Regla confirmada por Pablo Gomes (2026-09-25) para las deducciones en reversas de liquidaciones de Cobro/Botón:**

- **Los impuestos y aranceles se devuelven solo si la reversa es total y del mismo día del cobro.**
- En **todas las reversas parciales**, y en las **reversas totales de otro día**, **no se devuelve nada** (ni arancel ni impuestos).

**Contexto:** Fintexa preguntó cuál era la regla vigente "validada con Impuestos", porque circulaban dos versiones: (1) "los aranceles no se devuelven nunca" y (2) la regla de arriba. La regla nunca se definió en los tickets de liquidaciones y **afecta a todas las liquidaciones con reversas**. **Hoy el comprobante devuelve arancel e IVA en cada reversa**, o sea que el comportamiento actual no respeta la regla confirmada. Fintexa propuso corregirlo en un **ticket aparte**, que tiene que crear Bind. La misma regla define el criterio de la observación AD-1835 / DAD-3418 (arancel completo repetido en cada línea de devoluciones parciales).

**Riesgo aceptado explícitamente:** en las **devoluciones parciales del mismo día del cobro**, al usuario no se le devuelven el arancel ni los impuestos proporcionales al monto parcial. Se acepta "como hacemos desde siempre" por dos motivos: el **bajo volumen** de estos casos, y que devolverlos obligaría a **eliminar todo el impuesto en SISCRI y mandar a recalcularlo** por el importe parcial acumulado, algo complejo de gestionar en el sistema.

**Por qué la confianza es media:** Pablo respondió "Aceptable" sin mencionar una validación formal con Impuestos/Recaudaciones, que era lo que pedía Fintexa (ver `1_proyectos/tareas.md` T-072, que tenía esa validación pendiente).

> Fuente: Mail "Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes" — Melisa Belpassi (Fintexa) y Pablo Gomes (Bind), 2026-09-25.
