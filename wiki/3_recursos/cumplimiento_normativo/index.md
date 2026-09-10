# Cumplimiento Normativo

> Obligaciones normativas que Bind PSP debe cumplir independientemente del producto (Wallet o Adquirencia): reportería antilavado al banco/BCRA, certificación PCI DSS, y límites operativos de gestión de riesgo UIF/ROS. Nace en la reestructuración PARA en cascada (2026-08-12) al desarmar `detalle_productos/transversal/cumplimiento_normativo.md`, que mezclaba estos 3 temas normativos en un solo archivo.

## Documentos de este módulo

| Archivo | Contenido |
|---|---|
| [reporteria_worldsys_bcra.md](reporteria_worldsys_bcra.md) | Los 5 tipos de archivo diario que Bind PSP informa al banco/BCRA vía Worldsys (Wallet + Adquirencia), enriquecimiento de datos para Matriz de Riesgo, y el conflicto de diseño sin resolver sobre comprobantes vs. movimientos. |
| [pci_dss_recertificacion.md](pci_dss_recertificacion.md) | Mantenimiento de la certificación PCI DSS propia de Bind PSP: alta disponibilidad de pago presente, reducción de alcance PCI (TTL en Bóveda). |
| [limites_operativos_uif_ros.md](limites_operativos_uif_ros.md) | Topes operativos mensuales por segmento de cliente para decidir cuándo pedir documentación adicional, evitando ROS innecesarios ante la UIF. |
| [identificacion_personas_fisicas_cvu.md](identificacion_personas_fisicas_cvu.md) | ⚠️ Mayormente orientación de diseño, no validada por Compliance — con excepción de los puntos 1.3/4.13.1.1, confirmados contra texto primario BCRA. Marco regulatorio (BCRA/UIF/ARCA/AAIP) de identificación y resguardo de datos para altas de cuenta CVU de personas humanas — matriz de datos DDC, distinción legajo vs. reporte RSM, **4ta DDJJ obligatoria de cooperación tributaria internacional (OCDE/CRS + FATCA)**. |
| [identificacion_personas_juridicas_vinculados.md](identificacion_personas_juridicas_vinculados.md) | ⚠️ Orientación de diseño, no validada por Compliance. Requisitos UIF de identificación para personas jurídicas, FCI/Fideicomisos y sujetos vinculados/beneficiario final. |
| [gestion_riesgo_fraude_bcra.md](gestion_riesgo_fraude_bcra.md) | Comunicaciones "A" 8471 y 8473 del BCRA — programa de gestión de riesgo de fraude (Sección 6 extendida a PSPCP) y score de riesgo de fraude por CUIL/CUIT de uso obligatorio. Cronograma de 4 etapas desde 2026-09-01, discovery en curso en `1_proyectos/gestion_riesgo_fraude/`. |
| [gestion_riesgo_tecnologia_seguridad_a7724.md](gestion_riesgo_tecnologia_seguridad_a7724.md) | Comunicación "A" 7724 BCRA — marco integral de gestión de riesgos de TI/ciberseguridad (gobierno, continuidad del negocio, ciclo de vida de software, terceras partes, Canales Electrónicos). Aplicabilidad a Bind PSP asumida como posición de negocio, sin relevamiento de madurez todavía. |

## Ver también

- [3_recursos/arquitectura_sistema/index.md](../arquitectura_sistema/index.md) — infraestructura y seguridad que sostiene estas obligaciones (mTLS, PCI a nivel de red).
- [3_recursos/detalle_productos/index.md](../detalle_productos/index.md) — mecánica de producto de Wallet/Adquirencia sobre la que corren estos reportes.
- [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) — gap abierto sobre PCI DSS del proveedor Fintexa (distinto de la recertificación propia documentada acá).

---
*Última actualización: 2026-09-10 — `/context_merge`: `identificacion_personas_fisicas_cvu.md` actualizado con la 4ta DDJJ obligatoria (cooperación tributaria internacional OCDE/CRS + FATCA, fuente primaria BCRA) y confianza subida para los puntos 1.3/4.13.1.1.*
*Última actualización anterior: 2026-09-08 — `/context_merge`: 1 archivo nuevo (gestión de riesgos de TI/ciberseguridad, Com. "A" 7724 BCRA), desde auditoría de cumplimiento normativo del PM.*
*Última actualización anterior: 2026-09-07 — `/context_merge`: 1 archivo nuevo (gestión de riesgo de fraude, Com. "A" 8471/8473 BCRA), desde discovery de `gestion_riesgo_fraude/` (Pablo Gomes).*
*Última actualización anterior: 2026-09-02 — `/context_merge`: 2 archivos nuevos (identificación de personas físicas y jurídicas/vinculados para CVU), desde research de Gemini deep research del PM.*
*Última actualización anterior: 2026-08-12 — Creación del módulo en la reestructuración PARA en cascada, desarmando `detalle_productos/transversal/cumplimiento_normativo.md` en 3 archivos temáticos.*
