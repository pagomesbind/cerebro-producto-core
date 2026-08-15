# Riesgos del Contexto Fijo — Bind PSP

> Riesgos que afectan a la plataforma o al negocio en general, no a un proyecto puntual — esos viven en la sección de riesgos de su propio `proyecto.md`. Compartido entre los tres PM/PO: **solo lo escribe `/context_merge`**. Cada PM aporta un riesgo de este alcance como item `tipo: riesgo` en `contexto_vivo/`.

## Capacidad del proveedor de infraestructura (Fintexa)

Dos reducciones de dotación consecutivas en el equipo de Fintexa asignado a Bind PSP (julio y agosto 2026 — Soporte, QA, SRE, Dev Wallet/Adquirencia/Mobile POS). Ver detalle en [3_recursos/arquitectura_sistema/relacion_con_fintexa.md](../3_recursos/arquitectura_sistema/relacion_con_fintexa.md).

## Seguridad — Ardid no aísla datos entre clientes (multi-tenencia)

Fintexa confirmó que Ardid no aísla datos entre organizaciones — clientes como Coto y BIN podrían ver operaciones ajenas entre sí. Sin fecha de resolución confirmada, del lado de Pentass. Ver [3_recursos/arquitectura_sistema/incidentes_de_plataforma.md §4](../3_recursos/arquitectura_sistema/incidentes_de_plataforma.md).

## Compliance — integridad de `LAVADOOPERACIONES` sin resolver

Conflicto de diseño abierto hace ~2 meses (a la fecha del hallazgo) sobre si la fuente de verdad del reporte antilavado a Worldsys/BCRA debe ser la tabla de comprobantes o de movimientos, y cómo tratar reversas. Bloquea desarrollo de Nicolás Colón. Ver [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md §2](../3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md).

## PCI DSS del proveedor Fintexa — certificación sin confirmar en el texto narrativo del documento de arquitectura

La única mención de PCI DSS v4.0 Level 1 en el documento de arquitectura del proveedor es un diagrama; el texto narrativo y el resumen ejecutivo no lo listan entre los estándares de compliance. Ver [3_recursos/arquitectura_sistema/modelo_de_seguridad.md](../3_recursos/arquitectura_sistema/modelo_de_seguridad.md) y [gaps_y_preguntas.md](gaps_y_preguntas.md).

## Ver también
- [gaps_y_preguntas.md](gaps_y_preguntas.md) — vacíos de información del contexto fijo, distinto de riesgos ya identificados.
- [tareas.md](tareas.md) — backlog operativo, no riesgos.

---
*Última actualización: 2026-08-12 — Creación del archivo en la reestructuración PARA en cascada, consolidando 4 riesgos ya documentados en la wiki pero sin un lugar propio.*
