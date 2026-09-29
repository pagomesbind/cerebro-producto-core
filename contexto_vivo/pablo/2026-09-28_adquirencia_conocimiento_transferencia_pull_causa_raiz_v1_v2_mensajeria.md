---
id: 2026-09-28_adquirencia_conocimiento_transferencia_pull_causa_raiz_v1_v2_mensajeria
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_mails — mails 'Nueva respuesta en tu ticket 456632...', icm@coelsa.com.ar → Nicolás Colón, 2026-09-25 13:48 y 20:34 (threadId 19f055a718dd930f)"
producto: adquirencia
tema: causa raíz confirmada y resuelta del ticket Coelsa #456632 (Transferencia Pull en Homologación) — versión de mensajería V1 vs. V2
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/transferencias_pull_debin_coelsa.md
tipo_destino: actualizar
contradice: "no — completa el item ya mergeado el 2026-09-24 (`2026-09-24_adquirencia_conocimiento_transferencia_pull_formato_request_coelsa`), que había identificado la discrepancia de formato del request sin que Coelsa aportara una explicación. Este item aporta la causa raíz que Coelsa confirmó después."
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

## Causa raíz confirmada

Coelsa (Niurka Yamarte) confirmó el 2026-09-25 que el PSP **5071** (el usado en Homologación para este ticket) tenía configurada la **versión V1** de la mensajería de Transferencias Pull/DEBIN. Esto explica exactamente la discrepancia de formato que Bind había detectado el 22/09 (ver item previo, ya mergeado): en la versión V1, el request **no debería** traer el objeto `cuenta_virtual` (CVU) — pero el request real capturado sí lo traía, lo cual generó la comparación fallida contra el ejemplo de referencia documentado por Coelsa.

Para que el objeto `cuenta_virtual` se envíe y reciba correctamente entre comprador y vendedor (tal como se ve en el request esperado del evento `AvisoDebinPendienteCVU`) hace falta la **versión V2** de la mensajería.

## Resolución

- 2026-09-25 13:48 — Coelsa eleva el hallazgo como bug interno y pide a Bind confirmar si corresponde migrar el PSP 5071 a V2.
- 2026-09-25 20:34 — Coelsa confirma: "Ya habilitamos la versión 2 de la mensajería. Puedes volver a intentar procesar los debines."

## Por qué importa

Cierra (al menos del lado de la causa técnica) casi 3 meses de ticket abierto sin resolución. No era un problema de red/conectividad (como sugerían los mensajes previos sobre telnet/URL) ni de documentación desactualizada de Coelsa — era una configuración de versión de mensajería específica del PSP de Homologación, no alineada con lo que el flujo de DEBIN con CVU requiere. Queda pendiente que Bind confirme en un reintento real que el flujo ahora funciona de punta a punta (no confirmado todavía en la fuente de este item).

> Fuente: mails "Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación", icm@coelsa.com.ar → ncolon@bind.com.ar, 2026-09-25 13:48 y 20:34 (threadId `19f055a718dd930f`).
