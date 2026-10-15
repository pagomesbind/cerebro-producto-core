---
id: 2026-10-13_arquitectura_conocimiento_incidente_certificado_intermedio
pm: pablo
fecha_captura: 2026-10-13
fuente: "/sync_mails — mail 'Incidente caída por certificado' (threadId 1a1372dac25f4193), Daniel Zalazar (Fintexa), 2026-10-13"
producto: transversal
tema: Incidente de caída por certificado — cadena incompleta originada en un certificado intermedio, aplicación del certificado nuevo suspendida hasta resolver
tipo: conocimiento
destino_propuesto: wiki/3_recursos/arquitectura_sistema/incidentes_de_plataforma.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

Fintexa (Daniel Zalazar, Infrastructure Leader) reporta un incidente de caída de servicio por certificado, con post-mortem adjunto (PDF `20261013_inicidente_error_certificado.pdf`, **no leído automáticamente por esta skill** — ver nota de adjunto pendiente en el log de mails).

**Lo que se sabe del cuerpo del mail (sin abrir el adjunto):**
- Causa: la cadena de certificados quedó **incompleta**, originada en un **certificado intermedio**.
- Mitigación inmediata: se **suspendió la aplicación del certificado** (nuevo, en reemplazo) al día siguiente del incidente, hasta resolver el problema de la cadena.
- Destinatarios: Hernán Clarich, Emma Vignoles, Gonzalo Rivera, Pablo Serra (Fintexa) y Pablo Gomes; en copia Agustín Grau, Sebastián Ríos, Pablo Vargas, infra@fintexa.tech, Andrea Orsini.
- Seguimiento (14/10, Pablo Serra — Delivery Manager de Fintexa): agrega a Mariana Nadalin al hilo con un simple "Gracias", sin agregar información nueva ni indicar que el incidente siga abierto — sugiere cierre operativo, pendiente de confirmación explícita.

**Pendiente:** el detalle completo (servicio/dominio afectado, duración, impacto en clientes, plan de remediación de la cadena de certificados) está en el PDF adjunto, no procesado. Si se vuelve relevante (por ejemplo si hay un nuevo incidente del mismo origen), conviene pedir que se abra y lea manualmente.

> Fuente: mail "Incidente caída por certificado" (threadId `1a1372dac25f4193`), Daniel Zalazar (Fintexa) 13/10/2026 18:31, con seguimiento de Pablo Serra (Fintexa) 14/10/2026 09:29.
