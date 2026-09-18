---
id: 2026-09-18_adquirencia_webhook_qr_desfase_horario_gmt3
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-09-17), minuta Gemini, con Fintexa (Melisa Belpassi)"
producto: adquirencia
tema: bug de zona horaria en el webhook de pagos QR — falta el desfase GMT-3 desde el 31/08
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/index.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Hallazgo

Un ticket de soporte detectó que el webhook de pagos QR envía la hora de pago **sin el desfase de GMT-3**, generando confusión en los clientes que lo consumen: en vez de recibir la hora real (ej. `18:58`), reciben el valor crudo con el offset pegado pero sin restar (ej. `21:58 -3`), como si fueran las 21:58 horas. Melisa Belpassi (Fintexa) identificó que el cambio se introdujo en el ticket `1448` (identificado internamente como `494`), implementado el **31 de agosto de 2026**, y asumió la responsabilidad del error — el análisis de riesgo y las respuestas del PRD de ese ticket no alertaron lo suficiente sobre el impacto de fecha/hora antes de desplegarlo.

## Decisión pendiente

El caso se derivó a Mariana Nadalin para discutirlo con Gonzalo Rivera, evaluando dos caminos: **revertir el cambio** (aunque eso implica volver al estado incorrecto anterior) o **exigir a los clientes que integren considerando correctamente el GMT-3** tal como se envía hoy. Pablo Gomes quedó a cargo de comunicarle a Gonzalo Rivera la situación para que tome la decisión — sin resolver todavía en la reunión del 17/09.

> Nota: este bug viene arrastrándose desde el 31/08 (18 días antes de esta captura) sin que constara en la wiki — vale la pena confirmar con Gonzalo Rivera si ya se decidió algo antes de la próxima corrida.
