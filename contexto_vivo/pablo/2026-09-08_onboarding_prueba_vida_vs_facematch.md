---
id: 2026-09-08_onboarding_prueba_vida_vs_facematch
pm: pablo
fecha_captura: 2026-09-08
fuente: "Reunión 'Producto' (2026-09-08, minuta Gemini), Pablo Gomes/Emma Vignoles"
producto: onboarding
tema: prueba de vida vs. concordancia facial — dos validaciones biométricas distintas exigidas por norma
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En la reunión "Producto" (2026-09-08), al repasar los requisitos normativos faltantes para el legajo de onboarding, Pablo Gomes aclaró una distinción que hasta ahora no estaba explicitada en la wiki: **prueba de vida** y **concordancia facial (face match)** son dos validaciones biométricas distintas, y la normativa exige tener **las dos**, no una sola.

- **Prueba de vida ("liveness"):** responde solo "vive o no vive" — no tiene score ni puntaje de coincidencia. Es la validación que confirma que la persona frente a la cámara es una persona real en el momento (no una foto, no un video pregrabado).
- **Concordancia facial (face match):** mide qué tan parecida es la persona a la foto del documento (DNI) que se está validando — sí tiene un score/puntaje de similitud.

Ninguno de los proveedores relevados hoy entrega el video completo como evidencia — lo que sí entregan ambos (Socialnet, FaceTech) es una **captura 2D** (foto) extraída del video de la prueba de vida, que se cruza contra la foto del DNI. **Socialnet** hace ambas validaciones combinadas en un mismo servicio: agarra el video, extrae 3 imágenes, compara una contra la imagen del DNI (face match) y manda la otra a RENAPER (para cruzar contra el rostro registrado ahí). El caso que disparó la aclaración: María Victoria Simonetti (PLD, Banco Industrial) le había pedido a Pablo Gomes que la evidencia de prueba de vida incluya explícitamente el score que dio el proveedor y el motivo por el cual se dejó pasar (o no) la prueba de vida — pedido que technically corresponde al *face match*, no a la prueba de vida en sí (que no tiene score).

**Implicancia para el diseño de evidencia del legajo (PRD-147/PRD-202):** el paquete de evidencia armado por Onboarding para cada solicitud debe distinguir y dejar constancia de las dos validaciones por separado (prueba de vida: vive/no vive: sin score; face match: score de similitud + foto comparada), no tratarlas como una sola pieza de evidencia genérica "biometría".

> Fuente: Reunión "Producto" (2026-09-08), minuta Gemini, ~00:46:08-00:48:27 — Pablo Gomes explicando a Emma Vignoles.
