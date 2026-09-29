---
id: 2026-09-26_conocimiento-coelsa-pull-homologacion-causa-mensajeria-v1-habilitada-v2
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Mail 'Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación' — icm@coelsa.com.ar (Niurka Yamarte), mensajes del 2026-09-25 10:48 y 17:34 (ART)"
producto: wallet
tema: Transferencias Pull en Homologación (ticket Coelsa #456632) — causa raíz confirmada por Coelsa: el PSP 5071 tenía configurada la versión V1 de la mensajería; Coelsa habilitó la V2 el 25/09 y Bind debe volver a probar
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/transferencias_pull.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/transferencias_pull.md §6 — 'Observación del Cerebro (no confirmada por Coelsa)' (merge 2026-09-25): hipótesis de que el formato 'esperado' por Bind salía de otra especificación de 2023 y que Coelsa mandaba un aviso DEBIN estándar donde Bind espera el de transferencia pull. Coelsa confirma que la diferencia es de VERSIÓN de mensajería (V1 vs. V2) configurada por PSP, no de una especificación distinta."
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

Continuación de §6 de `transferencias_pull.md` (reactivación de Transferencias Pull en Homologación, ticket Coelsa #456632). **Cierra el diagnóstico que había quedado abierto en la entrada del 2026-09-23/24 (merge 2026-09-25).**

**2026-09-25 10:48 (ART) — Coelsa (Niurka Yamarte):** validaron los IDs de prueba que Bind envió el 24/09 y confirmaron que **el PSP 5071 (KEEP IT SIMPLE SRL, el PSP de homologación creado para estas pruebas) tiene configurada la versión V1 de la mensajería**. Para que el objeto **`CUENTA VIRTUAL`** (`cuenta_virtual`) viaje bien, tanto del lado Comprador como del Vendedor, hace falta la **versión V2 de la mensajería**. Es la que corresponde al request esperado para el evento `AvisoDebinPendienteCVU` con los datos de CVU asociados a **TRXPL**. Coelsa además **elevó internamente un bug** que detectó en la revisión. Según su redacción, en la versión V1 "no debería recibirse" el objeto `CUENTA VIRTUAL`; no explicaron más detalle del bug. Pidieron a Bind confirmar si correspondía pasar a V2.

**2026-09-25 17:34 (ART) — Coelsa:** avisa que **ya habilitó la versión 2 de la mensajería** para el PSP y que Bind puede volver a intentar procesar los DEBIN. En el hilo de mail no figura una confirmación explícita de Bind entre los dos mensajes; pudo haberse dado por COELSA Home o por otro canal.

**Qué cambia respecto de lo documentado:**
- Las diferencias de payload que ya documenta §6 (falta de `operacion.objeto.tipo: "TRXPL"`, de `operacion.vendedor.cuenta_virtual` y de `EntityID`, `esTitular` entero, etc.) se explican porque **Coelsa versiona la mensajería por PSP (V1/V2)** y el PSP nuevo de homologación quedó dado de alta en V1. La implementación de Bind (2023) está construida sobre el contrato V2. No hace falta adaptar el parser de Bind: el ajuste fue de configuración del lado de Coelsa.
- **Aprendizaje operativo (para cualquier alta futura de PSP en Coelsa, en homologación o en producción):** al crear o reactivar un PSP, **confirmar con Coelsa qué versión de mensajería queda configurada**. Tiene que ser V2 si se opera con CVU o transferencias pull. Es un parámetro por PSP, no global, y un PSP nuevo puede nacer en V1.

**Estado a la fecha de captura:** V2 habilitada. Falta que Bind vuelva a correr las pruebas de DEBIN/transferencia pull en homologación y confirme que los avisos se interpretan bien (ver `1_proyectos/tareas.md` T-011).

> Fuente: Mail "Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación" — icm@coelsa.com.ar, Niurka Yamarte (2026-09-25, dos mensajes).
