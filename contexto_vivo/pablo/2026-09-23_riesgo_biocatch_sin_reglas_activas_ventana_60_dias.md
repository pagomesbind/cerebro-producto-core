---
id: 2026-09-23_riesgo_biocatch_sin_reglas_activas_ventana_60_dias
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_meetings — reunión \"GD-6592 - Imple Divorcio\" (01:45 a ~08:00 GMT-3, minuta de Gemini, docId 1Ens77gdB8HPfFagSzwozLQmLKHvCpEXfQFgu95nCPp0), 2026-09-22"
producto: transversal
tema: Biocatch (control biométrico antifraude de la nueva plataforma BIN 24/Bind 24 de Banco Industrial) opera sin reglas de fraude activas durante una ventana de 60 días de recolección de baseline
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**Hallazgo (reunión "GD-6592 - Imple Divorcio", cutover de BIN 24, 22/09/2026):** Gonzalo Pereira (proveedor de Biocatch) explicó que la herramienta de control antifraude biométrico de la nueva plataforma BIN 24 **está recolectando información biométrica del dispositivo (patrón de escritura, movimiento del mouse) durante un período recomendado de 60 días, operando sin reglas de fraude activas en producción**. Como consecuencia directa, las solicitudes a la API de scoring devuelven valores bajos que permiten operar con normalidad — es decir, durante esta ventana **Biocatch no está efectivamente bloqueando ni señalando operaciones sospechosas**, solo recolectando datos para calibrar el modelo.

**Por qué es relevante:** esta ventana de 60 días sin reglas activas coincide temporalmente con el propio go-live de la plataforma decoupled de Banco Industrial — un momento de alta exposición operativa (múltiples regresiones funcionales encontradas la misma noche, ver item de canon `2026-09-23_arquitectura_conocimiento_golive_banco_industrial_desacoplado`) en el que, además, el control antifraude biométrico no está activo. No se menciona en la minuta si existe algún control compensatorio explícito para este período (más allá de las medidas generales de seguridad ya conocidas, como las mencionadas en el mismo repaso semanal de líderes del mismo día — ver `2026-09-23_transversal_riesgo_fraude_inter_seguridad_informatica`).

**Hallazgos técnicos relacionados, mismo módulo Biocatch (menor severidad, contexto):** inicializaciones múltiples ("inits") fuera de contexto por reutilización incorrecta del identificador de sesión del cliente entre dos dominios de login distintos — el equipo decidió convivir temporalmente con este comportamiento hasta un parche definitivo, sin fecha; la app móvil no estaba enviando eventos biométricos al proveedor (solo la versión web), reportado sin resolución al cierre de la reunión; error de certificado de Biocatch resuelto durante la ventana (renovación aplicada correctamente).

**Estado:** sin fecha de fin de la ventana de 60 días mencionada en la minuta (no se aclara si cuenta desde el lanzamiento original o desde este cutover), sin dueño ni ticket de seguimiento explícito para activar las reglas de fraude al cierre del período.
