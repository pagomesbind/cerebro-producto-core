---
id: 2026-08-25_wallet_coelsa_alias_arbitrario_bloqueo_24hs
pm: pablo
fecha_captura: 2026-08-25
fuente: "/idea_start + /idea_solution — discovery y análisis técnico de `asignacion_alias_cvu` (ticket MDA-292391, Banco Industrial), 2026-08-25"
producto: wallet
tema: "Mecánica real de Coelsa ante alias no asignado a tiempo tras crear un CVU: asignación arbitraria + bloqueo de 24hs, y comportamiento actual del sistema ante esa falla"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

## Mecánica de Coelsa cuando el alias no se asigna a tiempo tras crear un CVU

**Actualizado (2026-08-25, `/idea_solution`) — la ventana de 5 segundos está oficialmente documentada, no es solo conocimiento empírico.** El endpoint público de creación de CVU y su guía documentan explícitamente: *"al momento de crear un CVU, Coelsa le asignará un alias aleatorio a menos que la entidad le asigne un alias válido dentro de los 5 segundos desde la creación"* — y que esto aplica **igual** tanto si Bind asigna el alias automáticamente como si la organización lo gestiona ella misma vía API (mismo plazo de 5 segundos en ambos casos, sin delay adicional para ninguno de los dos). También documentado: solo se puede asignar/modificar un alias una vez cada 24hs, y esa restricción incluye el alias que haya asignado Coelsa automáticamente.

- Cuando el alias por defecto no queda asignado dentro de esos 5 segundos desde la creación del CVU, **Coelsa le asigna al CVU un alias arbitrario por su propia cuenta**.
- A partir de ese momento, **Coelsa bloquea cualquier reasignación de alias durante 24 horas** — ni la plataforma ni la organización pueden corregirlo antes de que pase ese plazo, sea por reintento automático o por acción manual de Soporte.

**Mecanismo de la falla original (caso MDA-292391):** el flujo de asignación automática de alias de Wallet, tras crear el CVU, llama a un endpoint interno de asignación de alias contra el banco emisor (producto "apibank" de Banco Industrial). **Corrección de atribución** (confirmada por el propio proveedor bancario en conversación directa): quien hace la consulta previa contra Coelsa antes de proceder es **el banco emisor internamente**, no Wallet — Wallet solo ve un único llamado (la asignación de alias) que el banco responde con error si su consulta previa a Coelsa indica que el CVU todavía no propagó a la réplica que usa para resolver esa consulta (separada del flujo transaccional real, según explicó el proveedor por analogía con su API de débito recurrente). El código de error observado en producción es `422` con detalle `VW006 | El CVU no existe`.

**Comportamiento actual del sistema ante esta falla (aclarado por el PM en `/idea_solution`, no documentado antes):**
- Cuando la falla ocurre **dentro del flujo automático de creación de CVU** (parámetro `aliasAutomatico=true`, el valor por defecto): el endpoint público de creación responde igual `201` (éxito), pero con el campo `alias` **vacío** — sin ningún error explícito hacia quien integró. Es un fallo silencioso desde la perspectiva de la organización integradora.
- Cuando la falla ocurre en una llamada **directa** al endpoint público de asignación de alias (`aliasAutomatico=false`, o una reasignación posterior): ese endpoint **sí devuelve el error real del banco** (`422`, "no existe el id de CVU" en la documentación pública) — a diferencia del camino anterior, acá la organización sí se entera de que algo falló.

> Fuente: discovery `/idea_start` de `1_proyectos/asignacion_alias_cvu/` (2026-08-25) — ticket MDA-292391 (Banco Industrial/apibank) + conversación técnica del PM con el proveedor bancario (Google Hangouts, 2026-08-24); actualizado por `/idea_solution` (2026-08-25) contra la documentación pública oficial de los endpoints de CVU/alias y aclaraciones del PM sobre el comportamiento actual del sistema. Ver `1_proyectos/asignacion_alias_cvu/artefactos/asignacion_alias_cvu-solution.md` para el análisis técnico completo (contrato, diagramas, máquina de estados) y la solución adoptada (reintento de 700ms, cubriendo ambos caminos de invocación).
