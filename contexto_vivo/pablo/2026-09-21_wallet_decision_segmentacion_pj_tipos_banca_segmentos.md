---
id: 2026-09-21_wallet_decision_segmentacion_pj_tipos_banca_segmentos
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reuniones \"Daily producto\" (09:30), \"Ardid - Persona Jurídica\" (10:01, con Rocío Revelli/Nicolás Colón/Matías Alzogaray) y \"Producto\" (14:01, con Emma Vignoles), todas del 2026-09-21"
producto: wallet
tema: Arquitectura de segmentación por tipo de banca para personas jurídicas en Wallet, con tope operativo hasta aprobación de Cumplimiento
tipo: decision
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Contexto:** el disparador fue la urgencia de prevenir fraude en altas de personas jurídicas (PJ) — hoy todas las cuentas nuevas (físicas y jurídicas) se dan de alta con el mismo tipo de banca ("todos"/"cliente empresa"), sin distinción, y las reglas de Ardid no pueden segmentar por PJ de forma independiente. El disparador inmediato: no se puede frenar a una PJ en el onboarding porque los documentos no se revisan a tiempo, y ya hubo varios casos de fraude con PJ.

**Decisión de arquitectura (acordada en las 3 reuniones del día, con Rocío Revelli de Ardid, Nicolás Colón de Wallet y Emma Vignoles/Pablo Gomes de Producto):**

- Cada organización de Wallet va a tener **tres tipos de banca fijos**: física mayor, física menor y jurídica (hoy solo existe un tipo genérico, sin distinción).
- Cada uno de esos tres tipos de banca va a tener **dos segmentos**: estándar y restringido (por ejemplo "restringido por onboarding" o "restringido por incorporación").
- **Las cuentas de personas jurídicas nacen por defecto en el segmento restringido**, con un **tope operativo de $1.000** hasta que se apruebe la documentación de cumplimiento (PLD) — el mismo criterio que ya se usa para el segmento restringido de menores. El objetivo explícito es forzar una revisión de Cumplimiento antes de que una PJ pueda operar con montos relevantes.
- Se descartó la alternativa de crear un segmento nuevo aparte (en vez de un tipo de banca "jurídica" dedicado) porque duplicaría el trabajo de segmentación para cualquier regla que ya aplique a "todos": con el tipo de banca dedicado, una regla configurada sobre "tipo de banca = jurídica" alcanza a todas las organizaciones sin tener que tocar cada segmentación existente.
- **Cambio de segmento (de restringido a estándar) es manual, no automático:** una vez que Cumplimiento aprueba la documentación (vía ticket Jira + Drive compartido, proceso todavía sin cerrar del todo — ver gap abajo), alguien de Soporte tiene que hacer el cambio a mano, hoy vía Swagger directo sobre la cuenta Wallet. Nicolás Colón queda en definir con Juani (Wallet) la forma más prolija de guardar/exponer esta especificación (hoy son parámetros sueltos; la idea es que una interacción pueda pedir "alta persona jurídica, valor restringido/estándar" sin tener que manejar IDs).
- **Reglas existentes con "todos" deben revisarse una por una:** Rocío Revelli (Ardid) tiene que auditar y actualizar todas las reglas ya creadas que hoy incluyen "todos" los tipos de cliente, para que la regla más restrictiva (jurídica restringida) se aplique antes que las genéricas — Nicolás Colón confirmó que el motor aplica primero la regla más restrictiva, así que no rompe nada mientras se actualicen las reglas viejas, pero el trabajo de revisión es manual y no tiene fecha.
- **Volumen bajo:** Pablo Gomes mostró datos reales de altas de PJ por mes (7, 18, 39, 37, con picos de hasta 108) — Consorcio Abierto concentra la mayoría, seguido de Terra Blockchain y La Virginia. El PM usó este dato explícitamente para justificar que la automatización completa no es prioritaria todavía ("no son 100 por día") — la rutina manual alcanza por ahora.
- **Rutina temporal de soporte (definida en la reunión "Producto" del mismo día, 14:01):** hasta que exista automatización, personal de Soporte (mencionados Luciana o Franco) va a revisar diariamente las nuevas altas de CVU de personas jurídicas y actualizar el segmento vía API a mano.
- **Proceso para entidades sin onboarding propio (reunión "Producto", 14:01):** para las organizaciones que no usan el onboarding de Bind, Cumplimiento recibe el legajo completo en un Drive administrado por Cumplimiento junto con una planilla de control; mientras se aprueba, se aplica un **tope temporal de $1.000.000** (distinto del tope de $1.000 mencionado en la reunión de la mañana para el alta automática por defecto — no está confirmado si son dos topes de escenarios distintos o una inconsistencia entre reuniones, ver gap). Una vez aprobado, Soporte hace el cambio de segmento con autorización registrada en Jira.
- **Precedente de tope físico:** ya hubo un reclamo de Octagon (cartera con PJ) porque el tope de personas físicas ($25M) le resultaba insuficiente para sus cuentas jurídicas — se le subió a $300M ad hoc, sin haber avisado antes al cliente del criterio. Esto refuerza por qué se decidió tratar "jurídica" como tipo de banca aparte con su propio criterio de tope, en vez de heredar el de personas físicas.

**Gap relacionado:** el tope de $1.000 (alta automática, mañana) vs. $1.000.000 (proceso manual sin onboarding propio, tarde) no quedó reconciliado entre reuniones — ver item `2026-09-21_wallet_gap_tope_operativo_pj_1000_vs_1millon` en `contexto_vivo/`.

**Impacto:** esto es arquitectura de Wallet (tipos de banca/segmentos), no un proyecto con IDEA propia en Jira todavía — Nicolás Colón (Wallet) queda de implementarlo, sin ticket ni fecha mencionados en ninguna de las 3 reuniones.
