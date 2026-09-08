---
id: 2026-09-07_sync_metrics_reporte_202636
pm: pablo
fecha_captura: 2026-09-07
fuente: "/sync_metrics — análisis de palancas y hallazgos (pipeline.py analyze + render_email.py)"
producto: transversal
tema: Reporte semanal de NSM y hallazgos (semana 202636)
tipo: conocimiento
destino_propuesto: 3_recursos/datos/log_metricas_semanales.md
tipo_destino: actualizar
contradice: no
confianza: alta
estado: ingestado
merge_commit: d783db8
---

## Semana 202636 (2026-08-31 → 2026-09-07) — Hallazgos de Negocio

### Resumen ejecutivo
NSM#1 registró recuperación fuerte (+86.6% WoW a $387.389 M) pero la tendencia de 4 semanas móviles sigue ligeramente hacia abajo (-1.6%). NSM#2 creció +50.7% WoW a $12.197 M pero con señales de calidad degradada. Hallazgo crítico: concentración extrema en NSM#1 (BSF 67.5% del volumen) expone el negocio a riesgo de dependencia cliente.

### Hallazgos priorizados

**[ALTA] Tarjeta Prepaga en NSM#2: pico extraordinario de volumen con tasa de rechazo elevada**
- Tarjeta Prepaga registró $68,4 M esta semana (+483.8% WoW, z=+6.38) — es una palanca chica que de pronto capturó volumen inusual. Simultáneamente, su tasa de rechazo saltó a 41.6% vs. la media de 8 semanas (24.9%). 
- Lectura: El volumen extra viene de un tipo de transacción o cliente específico con problemas de autorización, probablemente un cliente puntual que probó algo nuevo o un batch de reintentos. 
- Acción: Verificar con Adquirencia si es un patrón técnico conocido o si requiere investigación puntual.

**[ALTA] Bind PSP liquidaciones cta 2: caída del 86.5% en transferencias del Agente de Cobros**
- El collector 'Bind PSP liquidaciones cta 2' registró solo $2.165 M esta semana, cayendo desde $16.093 M (promedio de las 4 semanas previas). Es una caída operativa importante en una cuenta interna de liquidación. 
- Lectura: Podría indicar un cambio conocido en la forma de operar (cambio de cuenta, redistribución de flows a otra cuenta, o un problema técnico temporal). 
- Acción: Validar con Operaciones si es un cambio conocido o si requiere investigación. Otros collectors internos (cta 14, cta 39) muestran movimiento normal, así que el volumen probablemente migró a otra cuenta.

**[ALTA] Concentración extrema en NSM#1: BSF representa el 67.5% del volumen de API BANK**
- Bind PSP depende masivamente de BSF en NSM#1 (volumen operado por API BANK): una sola organización concentra dos tercios del volumen. Si sumamos Cencosud, el top-2 ya sube a ~80%. 
- Lectura: Este nivel de concentración expone el negocio a riesgo de churn cliente. Una salida o reducción de volumen de BSF impactaría directamente el avance hacia el objetivo estratégico de top 2 en volumen API BANK. 
- Acción: Requiere atención estratégica en retención y diversificación de base. Vale revisar qué está detrás del crecimiento de BSF esta semana (+134.1% WoW) para confirmar que es momentum sostenible y no un movimiento puntual.

**[MEDIA] NSM#1 recuperó fuerte: +86.6% WoW, regresando a niveles cercanos al máximo histórico**
- El volumen de API BANK saltó a $387.389 M esta semana. Es la segunda semana consecutiva de recuperación fuerte (semana anterior fue +15.4% WoW) y está apenas 7.7% por debajo del máximo histórico ($419.802 M en semana 202610). 
- Lectura: El rebote es fuerte visto WoW. Sin embargo, observando la tendencia de 4 semanas móviles (el indicador protagonista de este reporte): últimas 4 semanas acumulan $1.059.574 M vs. las 4 previas $1.076.874 M (caída del 1.6%). La tendencia mediano-plazo aún está ligeramente hacia abajo. 
- Implicación: La semana fuerte de 202636 es positiva pero no revierte la desaceleración de fondo que vemos en las últimas 4 semanas. Habrá que monitorear si la semana siguiente (202637) sostiene este nivel o si vuelve a caer.

**[MEDIA] Altas de comercios en Adquirencia: 192 nuevos en la semana, 81.8% concentrados en La Virginia**
- Se registraron 192 altas de comercios de Adquirencia esta semana, un 51.2% por encima de la mediana de las últimas 8 semanas. Es un buen indicador leading de crecimiento futuro en NSM#2 (las altas anteceden al volumen). 
- Lectura: Positivo en cantidad, pero la dependencia es notable: el 81.8% de esas altas provino de un solo cliente (La Virginia). Replca el patrón de concentración que vemos en NSM#1. 
- Implicación: Es positivo tener momentum de altas, pero la dependencia de un solo onboarding hace que el número sea menos representativo de crecimiento genuino de base. Si La Virginia no convierte sus comercios a volumen en las semanas siguientes, el impacto será menor al que sugiere el número de altas.

### Métrica de salud
- Rechazo NSM#1: 0.2% (media 8 semanas: 0.9%) — muy bajo, histórico positivo.
- Rechazo NSM#2: 21.0% promedio (media 8 semanas: 20.8%) — estable. Pero Tarjeta Prepaga + Tarjeta de Crédito muestran rechazos elevados (41.6% y 35.7% respectivamente).
- Devoluciones NSM#1: 0.0% (sin novedad).
- Leading indicators: Cuentas Wallet +13.5% WoW (28.658), Comercios Adquirencia +26.3% WoW (192).

### Serie histórica resumida
- NSM#1 semanas 202633→202636: $284.837M → $179.788M → $207.559M → $387.389M (última semana fuerte, prior caída estructural)
- NSM#2 semanas 202633→202636: $11.783M → $7.659M → $8.094M → $12.197M (último crecimiento sostenido desde semana 202635)

### Notas metodológicas
- "Tendencia" = ventana móvil de últimas 4 semanas cerradas vs. las 4 previas (NO es acumulado de mes calendario).
- WoW = semana anterior directa (202635).
- z-score y desviación estándar = contra los últimos 8 semanas cerradas.
- Baseline 13 semanas = promedio móvil de 13 semanas.
- Máximo histórico = desde el inicio de registros (semana 202536).
