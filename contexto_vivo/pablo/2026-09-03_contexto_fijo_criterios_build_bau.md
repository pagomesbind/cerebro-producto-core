---
id: 2026-09-03_contexto_fijo_criterios_build_bau
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Daily producto' 2026-09-02 09:49 (docId 1oKS7XkT8jYGkdObwgKENcrWO-HAprbfGXlDeNMs_rVw), minuta Gemini"
producto: transversal
tema: Criterio de clasificación Build vs. Bau para reportar trabajo de Producto
tipo: decision
destino_propuesto: 2_areas/procesos/criterios_de_priorizacion.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Decisión acordada:** el equipo de Producto estandarizó el criterio para clasificar cualquier iniciativa/proyecto como **Build** o **Bau**, a los fines de reportar con precisión al equipo directivo el uso de recursos y qué se está trabajando realmente:

- **Build:** foco en crecimiento, innovación e impacto en métricas clave (nuevas funcionalidades o productos).
- **Bau** (Business as Usual): foco en mantener estabilidad, resolver errores, gestionar deuda técnica y garantizar la operatividad diaria — reconocido explícitamente como la mayor parte de la carga operativa real del equipo, aunque menos visible.

La discusión surgió porque la clasificación puede ser subjetiva caso por caso (ejemplo debatido en la propia reunión: el rediseño integral del flujo de Onboarding — ¿es Bau porque mejora un flujo existente y atiende cumplimiento normativo, o Build por ser una reconstrucción integral?), y el equipo remarcó la necesidad de aplicar el mismo criterio de forma consistente hacia adelante, no ad-hoc por proyecto.

**Ejemplos de aplicación acordados en la misma reunión:**
- **Bau:** tareas exigidas por normativa o necesarias para evitar fallos operativos — ej. la deshabilitación automática de cuentas bloqueadas en Ardid, reportes normativos.
- **Build (candidato, sin cerrar):** proyectos orientados a nuevas capacidades para retener clientes — ej. el "alta de cuenta comitente" pedido por clientes específicos (ver PRD-208) — el criterio de corte discutido fue si su omisión impediría la operatoria (Bau) o si abre una capacidad nueva de negocio (Build).
- **Sin resolver en la reunión:** la refactorización de segmentos en Wallet (dar a clientes como Credicuotas autonomía sobre sus segmentos, hoy dependientes de una API del calculador de costos sin integración directa en Wallet) quedó pendiente de definición más profunda — ver item de oportunidad `2026-09-03_wallet_oportunidad_segmentos_autonomos` en `contexto_vivo/`.

> Fuente: reunión "Daily producto" (2026-09-02 09:49), minuta Gemini. Participantes: Luciana Rudaz, Pablo Gomes, Matías Alzogaray, Nicolás Colón.
