# Recursos — El Detalle Técnico

> Tercer salto del PARA en cascada: si el contexto fijo de `2_areas/` no alcanza, acá vive el detalle específico de un producto o de la infraestructura. **Canon compartido entre los tres PM/PO, vivido en el repo `CEREBRO_CORE`: nadie escribe acá directo, ni siquiera una sesión de sync** — todo aporte nace como item en `wiki/1_proyectos/contexto_vivo/` y solo `/context_merge` lo ingiere (escritura libre sobre `3_recursos/`; crear una carpeta nueva sigue requiriendo permiso). Excepción de mecánica, no de regla: los items `tipo: dato` de `datos/` se aplican por copia byte a byte, sin criterio editorial — ver `datos/index.md`.

## Subcarpetas

| Carpeta | Contenido |
|---|---|
| [detalle_productos/](detalle_productos/index.md) | Cómo funciona cada producto hoy — mecánica interna, manuales de configuración, hacks operativos, y su API pública expuesta (`<producto>/apis_expuestas/`, dominio exclusivo de `/sync_web`). |
| [arquitectura_sistema/](arquitectura_sistema/index.md) | Sistemas/IT duro no ligado a un producto: infraestructura cloud, seguridad de plataforma, NFR/performance, evolución de la plataforma, relación técnica con el proveedor Fintexa. |
| [cumplimiento_normativo/](cumplimiento_normativo/index.md) | Obligaciones regulatorias de Bind PSP: reportería PLD/BCRA, PCI DSS, límites UIF/ROS. |
| [datos/](datos/index.md) | Stores de datos acumulados y fichas de datasets ad-hoc — antes repartidos entre `2_areas/control/` y `2_areas/datasets/`. Consulta puntual, no contexto de overview. |

## Archivos sueltos

| Archivo | Contenido |
|---|---|
| [changelog.md](changelog.md) | Resumen corto de cada merge que tocó esta capa, solo lo escribe `/context_merge`. |

## Ver también
- [2_areas/index.md](../index.md) — el contexto fijo, consultado antes que este módulo.
- [1_proyectos/index.md](../1_proyectos/index.md) — lo dinámico, en lo que trabaja el PM día a día. Incluye `contexto_vivo/`, el buzón de todo aporte a esta capa.

---
*Última actualización: 2026-08-15 — Pipeline de sincronización multi-PM: nueva carpeta `datos/` (fusiona `2_areas/control/` + `2_areas/datasets/`) y `changelog.md`. Escritura exclusiva de `/context_merge` sobre el repo `CEREBRO_CORE`.*
*Última actualización anterior: 2026-08-12 — Creación del índice raíz de `3_recursos/` en la reestructuración PARA en cascada (no existía).*
