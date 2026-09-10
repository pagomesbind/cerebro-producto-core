---
id: 2026-09-10_direccion_riesgo_crecimiento_clientes_individuales_qr
pm: pablo
fecha_captura: 2026-09-10
fuente: "Reunión 'BIND / PNET: Performance, recurrencia, etc.' (2026-09-10) — comentario de Facundo Nicolas Collerone (Provincia Net) sobre la proyección de crecimiento de su propia base de clientes. Detalle completo en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8 'Reunión 2026-09-10', punto 2 y 11`."
producto: adquirencia
tema: riesgo de escalamiento de la contención de la cola compartida de generación de QR a medida que crece la base de clientes "de a uno" de Provincia Net
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Riesgo:** Provincia Net (Facundo Collerone) proyectó en la reunión del 2026-09-10 un aumento fuerte, en los próximos meses, de su segmento de clientes de consumo **individual/interactivo** ("de a uno" — hoy sin ningún proceso batch de por medio, van directo contra la API de creación de deuda/QR de Bind). Mencionó nuevos sectores entrando a este segmento: telefonía, transporte, y otros. Este es exactamente el segmento que hoy reporta los timeouts de generación de QR (ej. DEPAY) cuando compite con las ráfagas masivas de Provincia Net contra la **cola única compartida** de generación de QR (mecanismo confirmado por Ingeniería de Bind en la misma reunión — ver `2026-09-10_adquirencia_reunion_pnet_causa_raiz_cola_unica_y_mitigacion`).

**Por qué es un riesgo de contexto fijo y no solo de PRD-66:** el crecimiento proyectado es de clientes de Provincia Net (que a su vez son terceros — municipios, empresas de servicios — no clientes directos de Bind), pero el síntoma (timeouts en la cola compartida) impacta a **cualquier cliente de Bind** que use el canal interactivo de creación de QR, no solo a los de PNET. Si este crecimiento se concreta antes de que la mitigación de largo plazo (cola separada interactiva/batch, ticket AD935) esté implementada, el número de clientes afectados por el mismo problema puede multiplicarse — no es un riesgo exclusivo de la relación con Provincia Net.

**Estado de la mitigación al momento de este registro:** en curso pero sin ETA firme — escalado de recursos (vCores/pods) como paliativo de 1-1,5 mes, y diseño de arquitectura de 2 colas todavía en discusión activa (sin fecha de implementación). Ver `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8` para el detalle completo del plan.

**Sin cuantificación dura:** no hay una fecha ni un número concreto de cuántos clientes/qué volumen se sumaría — es una proyección cualitativa de Provincia Net sobre su propio negocio, no un compromiso ni un dato medido. Confianza media por ese motivo.

## Ver también

- `2026-09-10_adquirencia_reunion_pnet_causa_raiz_cola_unica_y_mitigacion` (contexto vivo) — mecanismo técnico completo y plan de mitigación.
- `3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md` — la investigación de base de este mismo problema.
- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8` — transcripción resumida completa de la reunión.
