---
id: 2026-09-02_decision-criterios-build-vs-bau
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Daily producto\" (2026-09-02)"
producto: transversal
tema: Criterio de clasificación de proyectos como Build (crecimiento/nuevas capacidades) vs. Bau (estabilidad/mantenimiento/cumplimiento) para reportar el uso de recursos del equipo
tipo: decision
destino_propuesto: 2_areas/procesos/criterios_build_bau.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Daily producto" (2026-09-02, con Luciana Rudaz, Pablo Gomes, Matias Alzogaray, Nicolás Colón) se acordó un criterio explícito para clasificar el trabajo del equipo entre **Build** y **Bau**, ante la necesidad de reflejar con precisión ante la gerencia el uso real de recursos (la clasificación venía siendo subjetiva).

**Definición acordada:**
- **Build:** foco en crecimiento, innovación e impacto directo en métricas clave (nuevas funcionalidades o productos).
- **Bau (Business as Usual):** foco en mantener la estabilidad, resolver errores, gestionar deuda técnica y garantizar la operatividad diaria — reconocido explícitamente como fundamental para la continuidad del negocio y, a menudo, la mayor parte de la carga operativa real del equipo.

**Aplicación práctica discutida en la reunión:**
- Tareas exigidas por normativa o necesarias para evitar fallas operativas (ejemplo citado: deshabilitación automática de cuentas bloqueadas en Ardid, reportes normativos) → **Bau**.
- Proyectos orientados a nuevas capacidades para retener clientes (ejemplo citado: alta de cuenta comitente pedida por clientes específicos) → a evaluar caso a caso bajo el mismo criterio (si su omisión impediría la operatoria, tira a Bau; si no, tira a Build).

**Punto abierto, no resuelto en la reunión:** la clasificación del flujo de **Onboarding** completo generó debate extenso y no se cerró — algunos lo ven Bau (mejora de flujos existentes + cumplimiento normativo), otros Build (al ser una reconstrucción integral). El equipo reconoció que esta clasificación específica impacta directamente en el reporte de esfuerzo a la dirección y quedó pendiente aplicar el criterio de forma consistente en futuras asignaciones — no se llegó a una definición cerrada para este caso puntual.

Contexto adicional que motivó la discusión: aclaración sobre diferencias entre **adquirente** (habilita procesamiento directo con el procesador, ideal para comercios de gran volumen — ej. Payway) y **agrupador** (subadquirente para comercios más pequeños, gestiona relación comercial y cumplimiento) — relevante porque el Banco Central y organismos supervisores como la CFI imponen obligaciones de cumplimiento y riesgo distintas según el rol. Este conocimiento conceptual puede ser relevante también para `2_areas/overview_productos/` si no está ya cubierto ahí — a evaluar en el merge.

> Fuente: Reunión "Daily producto" (2026-09-02), minuta Gemini.
