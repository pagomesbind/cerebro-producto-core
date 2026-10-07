---
id: 2026-10-06_adquirencia_conocimiento_percepciones_iibb_en_progreso
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-10-06 10:59, compartida evignoles), minuta Gemini"
producto: adquirencia
tema: Fix del cálculo de percepciones de Ingresos Brutos en liquidación por lote — trabajo retomado con Ari Profiti, versión 19.0 de AD en Staging
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/impuestos_iibb_liquidacion_lote.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

En "Repaso Semanal líderes" (2026-10-06), Matías Alzogaray solicitó colaboración al equipo para avanzar con el fix del cálculo de percepciones de Ingresos Brutos en la liquidación por lote — el mismo bug de performance/NULL ya documentado en `impuestos_iibb_liquidacion_lote.md` (reportado por Fintexa, hasta ahora "sin confirmación de fix"). Esta reunión confirma que el trabajo está efectivamente en curso: coordinado previamente por correo con Ari Profiti (sin más detalle de rol en la minuta).

En paralelo, Daniel Zalazar (Fintexa) confirmó que la versión 19.0 de Adquirencia (AD) se desplegó en Staging y el equipo de QA comenzó las pruebas — sin indicar en la minuta si el fix de percepciones de IIBB forma parte del alcance de esa versión 19.0 o es un desarrollo separado todavía sin versión asignada. Las pruebas de AD 19.0 coinciden en el tiempo con el despliegue de Wallet v73 de este jueves (08/10); Matías Alzogaray estima que las pruebas plenas de AD 19.0 finalizarán hacia el viernes 09/10.

> Fuente: reunión "Repaso Semanal líderes" (2026-10-06), minuta Gemini.
