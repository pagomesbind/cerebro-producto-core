---
id: 2026-09-30_clientes_fast_transfer_sin_ficha_pago_configuracion
pm: pablo
fecha_captura: 2026-09-30
fuente: "/sync_meetings — reunión 'Join Soporte Clientes' (2026-09-30 10:04, minuta Gemini, docId 1qAhV4ttix0uoPPHzuh2PsZNKgy1wUo2us4pgt4lRD9s), compartida por Emma Vignoles. Invitados: Mauro Suppan, Luciana Rudaz, Emma Vignoles, Diego Weledniger, Adriana Endzeliz, Gustavo Lazzaro, Gonzalo Rivera, Alberto Murad, Matias Alzogaray, Nicolás Colón, Pablo Gomes"
producto: transversal
tema: Cliente "Fast Transfer" sin ficha en log_clientes.md — pagó el pago de configuración tras demoras previas
tipo: gap
destino_propuesto: wiki/2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

<!--
Cuerpo: conocimiento TRABAJADO y COMPLETO, no la transcripción cruda.
No resumir — el detalle completo es lo que hace que "no omitir" sea sostenible.
Citar la fuente donde corresponda (quién lo dijo, en qué reunión/mail/sesión).
-->

**Hallazgo:** en la reunión "Join Soporte Clientes" del 2026-09-30, Diego Weledniger le comunicó a Adriana Endzeliz que **"Fast Transfer"** acababa de abonar el "pago de configuración" (onboarding/alta técnica) tras demoras previas en el proceso de facturación. Diego aclaró que este dato se incluyó en "el folleto" (ficha/propuesta comercial) pese a no ser información que se coloca habitualmente, justamente por las demoras que hubo.

**Verificado — "Fast Transfer" no aparece en absoluto** en `wiki/2_areas/clientes/log_clientes.md` ni en `casos_de_uso_clientes.md` (grep case-insensitive sobre ambos archivos, sin resultados), a diferencia de otros clientes sin ficha ya documentados como excepción aceptada (TPay, Pago Fácil/Western Union, PedidosYa, Cros Online/Pago Nube — ver precedente en `4_archivos/contexto_ingestado/` del merge del 2026-09-14). No hay forma de saber desde esta minuta si "Fast Transfer" es un cliente nuevo recién dado de alta, un cliente ya existente bajo otro nombre comercial, o un prospecto que recién ahora formalizó el pago inicial.

**Por qué se registra como gap y no como ficha nueva (regla de la skill, 3a-bis):** la skill `/sync_meetings` nunca toca `log_clientes.md` ni crea fichas — eso es dominio exclusivo de `/sync_customers` sobre su fuente de Notion. Este item solo señala que `/sync_customers` debería verificar si "Fast Transfer" existe en Notion y, si corresponde, darlo de alta en el próximo barrido.

**Confianza media:** el nombre puede estar mal transcrito por Gemini (ninguna otra fuente lo confirma); si no aparece tampoco en Notion al momento del próximo `/sync_customers`, vale la pena cruzarlo contra clientes de "Servicios"/Impuestos y Agrupadores existentes antes de asumir que es 100% nuevo.
