---
id: 2026-09-28_onboarding_riesgo_vulnerabilidad_facematch_dni_selfie
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_meetings — reunión \"Producto\" (2026-09-28 14:12, compartida por evignoles), minuta Gemini"
producto: onboarding
tema: Vulnerabilidad de seguridad en la validación de identidad — la foto del DNI no se compara efectivamente contra la selfie del usuario
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md — el canon documenta (desde 2026-09-08) que la normativa exige DOS validaciones biométricas distintas y separadas: prueba de vida (liveness, sin score) y concordancia facial/face match (score de similitud entre selfie y foto de DNI). Este hallazgo de auditoría de seguridad indica que, en la práctica, la comparación de face match no está bloqueando correctamente — permite usar una foto ajena junto con un número de trámite de DNI correcto. No se aclaró en la reunión si el control no está implementado, está mal configurado, o es bypasseable en algún camino de contingencia (posible punto de contacto con la vulnerabilidad ya trackeada en PRD-247, 'DNI frente/dorso sin cruzar', que también involucra el camino de contingencia — sin confirmar si es el mismo mecanismo)."
confianza: media
estado: ingestado
merge_commit: 3492d04
---

Pablo Gomes mencionó en la reunión "Producto" un hallazgo de auditorías de seguridad: actualmente el proceso de onboarding **no compara adecuadamente la fotografía del DNI con la selfie del usuario**, lo que permite completar el onboarding usando una foto de otra persona junto con un número de trámite de DNI correcto (es decir, datos documentales válidos pero biometría no verificada contra la identidad real del solicitante).

Esto es una brecha de seguridad con implicancia directa de fraude/PLD — un actor malicioso con acceso al número de trámite de un DNI ajeno podría completar el onboarding sin que el sistema detecte la discordancia facial.

**Próximo paso (Pablo Gomes):** el hallazgo quedó anotado para ser abordado en el desarrollo de los sistemas de puntuación (scoring) y las validaciones de API (ver T-147 en `tareas.md`, marcada 🔴 por la naturaleza del hallazgo).

**Nota de severidad:** no se registró en la minuta el volumen de casos afectados, si el proveedor de biometría (Socialnet/FaceTec, ver `prd-147_legajo_worldsys/artefactos/legajo_worldsys-propuesta_documentos_zip_evidencia.md`) es el mismo que presenta la falla, ni desde cuándo está expuesta esta brecha — sugerido confirmar esto como parte de T-147 antes de escalar a Cumplimiento/Fraude formalmente.

> Fuente: reunión "Producto", 2026-09-28 (`/sync_meetings`).
