---
id: 2026-09-02_ardid_riesgo_multa_pruebas_bloqueo
pm: pablo
fecha_captura: 2026-09-02
fuente: "/sync_mails — mail \"MINUTA - Repaso Semanal líderes: Mar, 1 de sept de 2026\" (threadId 1a05e97ebeb0061d), Matías Alzogaray (PM, minuta directa — no Gemini), 2026-09-01; monto completado por /sync_meetings desde la minuta de Gemini de la misma reunión (docId 1X8xiv7fdhxrYAfC66viZq3ViKvKQGGdR2dhViPii-V4), 2026-09-02"
producto: ardid
tema: Multa de $75 millones originada por errores en pruebas de bloqueo de transacciones de Ardid
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Fuente:** minuta de "Repaso Semanal líderes" del 2026-09-01 (Matías Alzogaray, PM), mencionada al pasar como parte del diagnóstico de la sobrecarga operativa que motivó la reforma del ciclo de despliegues (ver `2026-09-02_contexto_fijo_reforma_ciclo_despliegues`).

**Hallazgo:** se confirmó una **multa de $75 millones** a Bind PSP originada por errores en las pruebas de bloqueo de transacciones de Ardid (motor antifraude) — transacciones que debían bloquearse no se bloquearon. La minuta oficial (mail a la lista ampliada, con Fintexa/Tecnológica Financiera en copia) redactó el monto ("[DATO REDACTADO]"); el monto se completó cruzando la minuta de Gemini de la misma reunión (enviada solo a invitados de la organización Bind PSP), que lo deja explícito dentro de la sección "Detalles" (análisis de causas por la técnica de los cinco porqués, cita de Emma Vignoles). Sigue sin confirmarse la entidad que aplicó la multa (banco/red de tarjetas/regulador), el ticket/versión de Ardid involucrado, ni si ya está resuelta — ninguna de las dos fuentes lo detalla.

**Nota sobre la discrepancia de fuentes:** no es una contradicción de hechos, sino de nivel de detalle según audiencia — la redacción del monto en la minuta oficial es probablemente deliberada por sensibilidad ante destinatarios externos.

**Confianza media** porque ambas fuentes mencionan el hecho al pasar, dentro de una reunión enfocada en otro tema (reforma de despliegue), sin ticket ni informe de causa raíz propio.

**Riesgo hacia adelante:** el equipo sumó como acción "sumar a un referente del equipo de Ardid a las reuniones de coordinación" (Hernán Clarich, próxima reunión) — señal de que Ardid quedó fuera del loop de coordinación de despliegues hasta ahora, lo que probablemente contribuyó al error de las pruebas de bloqueo.

> Gap abierto: no se conoce la entidad que aplicó la multa, el ticket/versión de Ardid involucrado, ni el detalle técnico del error de bloqueo — si aparece en un mail o reunión futura, actualizar este hallazgo (`tipo_destino: actualizar` sobre el mismo archivo canon una vez mergeado).
