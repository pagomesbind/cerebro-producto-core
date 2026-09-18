---
id: 2026-09-18_onboarding_conocimiento_consola_referencia_octagon_ava
pm: pablo
fecha_captura: 2026-09-18
fuente: "/idea_solution sobre revision_pj_cumplimiento — exploración en vivo del ambiente de staging del proveedor externo (caso real de prueba) + grabación de la demo del 2026-08-19 (ya citada parcialmente en onboarding_personas_juridicas.md §8)"
producto: onboarding
tema: detalle funcional de la consola de Cumplimiento del proveedor externo (producto "AVA Compliance") usado como referencia de diseño
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f460705
---

Ampliación de `onboarding_personas_juridicas.md §8` (que ya documenta la demo del 2026-08-19 a alto nivel) con el detalle funcional real, obtenido navegando en vivo un caso de prueba en el ambiente de staging del proveedor (producto internamente llamado "AVA Compliance" / "AVA Onboarding", accedido en `avaonboarding.adfcloudia.com/compliance`) y revisando la grabación completa de la demo.

**Estructura de la consola (pantalla de detalle de un caso):** 5 pestañas — Resumen, Documentos, KYC, Verificaciones, Auditoría — más un header con acciones Aprobar/Observar/Rechazar y una sección de "Asignación del caso" (a quién está asignado, con historial de reasignaciones).

**Pestaña Resumen:**
- Tarjeta "Score de Compliance": puntaje 0-100, nivel (Crítico/Alto/Medio/Bajo por rango), banda de texto ("Riesgo medio - Requiere revisión antes de aprobar"), "Nivel de diligencia aplicable" (ej. "Debida Diligencia Estándar") con cuenta regresiva a la próxima actualización de matriz (ej. "2 años"), y el detalle de qué factor resta puntos (ej. "Volumen Anual Operado: > $50.000.000 → -30 pts").
- "Matriz de riesgo": heatmap 5×5 (Probabilidad × Impacto), con la celda del caso marcada y un desglose expandible ("Ver desglose") que muestra Score, Nivel, Probabilidad, Impacto, Celda (P/I) y una nota aclaratoria: "La matriz representa la distribución del riesgo acumulado del Score Compliance entre Probabilidad e Impacto. No modifica la fórmula del score."
- "Estructura societaria": agrupada por rol — Beneficiarios Finales, Firmantes, Autoridades — cada persona con avatar, DNI enmascarado (con ícono de ojo para revelar), % de participación (beneficiarios) o cargo (Director Titular/Suplente, Apoderado, Presidente), y un badge de screening inline por persona ("Sin coincidencias").
- "Alertas Consolidadas": lista de hallazgos reales (no de pendientes), cada uno con título corto (a veces en formato código, ej. `INCONSISTENCIA_CUIT_ESTRUCTURA`), descripción específica (ej. "Porcentaje de participación total es 96%, debe ser 100%") y fuente citada (ej. "Fuente: Análisis de Fraude", "Fuente: Análisis KYC"). Dos estilos de severidad visual (rojo/crítico vs. amarillo/advertencia).

**Pestaña Documentos:** contador de progreso arriba del listado ("8/8 documentos revisados · 8 aprobados · 0 rechazados · 0 pendientes") con una píldora "Listo para decisión final" cuando está completo, y botón "Solicitar Documento". Cada fila de documento es expandible (acordeón) y muestra los campos extraídos del documento (ej. para una Constancia de CUIT: CUIT, Razón Social, Domicilio fiscal, Actividad Principal, Fecha alta) sin necesidad de abrir el archivo — más un botón "Ver documento" con nota de permisos ("Solo administradores pueden descargar"). Cada documento tiene además un % (aparenta ser confianza de extracción/OCR) y estado "Aprobado por oficial".

**Pestaña KYC:** preguntas de la entrevista al cliente, en formato pregunta-respuesta con badge "Respondida" (ej. Actividad principal, Tipo de clientes, Locales comerciales, Medios de pago).

**Pestaña Verificaciones:** "Screening de sanciones" contra las listas **OFAC, ONU, UIF, REPET, PEP** (nombres reales confirmados en pantalla), con badge de resultado ("Screening limpio") y botón "Re-verificar". Debajo, "Verificación de personas (identidad y listas)": un resumen de conteos (autoridades/firmantes/beneficiarios/verificados/PEP/en listas) y una tabla por persona con columnas Persona | Rol | Identidad | Cruce DNI | PEP | Sanciones — es decir, el screening y la verificación de identidad corren **por persona**, no solo a nivel solicitud completa.

**Pestaña Auditoría ("Trazabilidad"):** log de eventos mucho más granular que un simple historial de estados — cada entrada tiene un tipo categorizado (`VERIF`, `SISTEMA`, `DECISIÓN`, `DOC`), texto descriptivo (ej. "Consulta al padrón ARCA en vivo", "Documento adicional 'CONTRATOS_COMERCIALES' validado", "Usuario confirmó explícitamente el documento DOC-xxx"), actor y timestamp.

**Uso de este conocimiento:** sirvió para decidir qué adoptar en el rediseño de `revision_pj_cumplimiento` (alertas específicas + contador de progreso, ambos ya implementados) y qué descartar por requerir capacidad que Bind no tiene hoy (score/matriz de riesgo, verificación por persona, auditoría granular — confirmado explícitamente por el PM que estas tres no existen en la plataforma actual). Queda como referencia general de producto para cualquier futuro proyecto de Onboarding que evalúe sumar alguna de estas capacidades.
