---
id: 2026-09-30_adquirencia_iniciativa_prd251_frente_a_ejecutado_con_mejora_confirmada
pm: pablo
fecha_captura: 2026-09-30
fuente: "actualización de 1_proyectos/index.md §2 por el PM, tras medir impacto real de producción de rechazos_bines_payway (PRD-251)"
producto: adquirencia
tema: PRD-251 — Frente A ejecutado en producción (despliegue v73, 29/09) con mejora confirmada en datos reales del 30/09
tipo: iniciativa
proyecto: PRD-251
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Novedad para la cartera de iniciativas

El Frente A de `rechazos_bines_payway` (PRD-251, carga masiva urgente de BINs en `dbo.IssuerIdentification`, ticket AD-978) salió de "bloqueado en producción" a "ejecutado con mejora confirmada": el despliegue v73 salió el martes 29/09 20:30-23hs (reprogramado desde el 24/09, cancelado esa noche por atraso de QA y defectos de liquidaciones) y aplicó en el mismo despliegue (1) la eliminación de la validación de `payment_methods.json` del frontend y (2) la carga masiva de BINs (AD-978) — el fix que llevaba desde el 21/09 bloqueado exactamente porque cargar los BINs reales sin quitar esa validación rompía pagos válidos.

El PM comparó transacciones reales de tarjeta (formas de pago prepaga/crédito/débito) de la mañana del 30/09 contra la misma ventana horaria del día anterior: +15,2% de volumen procesado y % de rechazo de 18,82% a 17,28%, con 37 BINs de los 89.721 dados de alta/reactivados por el ticket que no registraban ninguna transacción antes de las 20:30hs del 29/09 (hora real del despliegue) y ya suman 105 transacciones desde entonces — evidencia directa de BINs que pasaron de no existir en el sistema a operar con normalidad. Detalle completo en `1_proyectos/rechazos_bines_payway/proyecto.md` §7 (no es objeto de este item — acá solo la novedad puntual para la cartera).

El resto del proyecto (Frente B — precisión variable de BIN, Frente C — automatización semanal vía el conciliador) sigue sin cambios: IDEA PRD-251 en EN APROBACION, 9 historias en Backlog pendientes del comité de aprobación.
