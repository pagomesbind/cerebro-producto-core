---
id: 2026-09-11_iniciativa-visibilidad-error-alta-cotizacion-fintexa
pm: nicolas
fecha_captura: 2026-09-11
fuente: "Charla directa con el PM — cotización comunicada por Fintexa"
producto: onboarding
tema: Cotización real de Fintexa para visibilidad_error_alta (OB-247) — 24 horas, ~1 SP
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: cb58cfd53c7f3d391017622178663faa33c1c2b8
proyecto: visibilidad_error_alta
---

Novedad sobre [`1_proyectos/visibilidad_error_alta/`](../visibilidad_error_alta/proyecto.md) (OB-247, cliente Inter — motivo de error de broker en grilla de alta de cuenta comitente).

Fintexa cotizó el cambio (columna de motivo de error + export CSV en la grilla de "Error en Alta") en **24 horas de desarrollo, equivalente a ~1 SP y poco más** — por debajo del piso "S=1 SP" de la escala de conversión del equipo. Se pidió la cotización por separado de la de [OB-246](https://bindpsp.atlassian.net/browse/OB-246)/`cola_verificacion_manual` (mismo cliente y portal, discovery cerrado el mismo día que este proyecto), no conjunta.

El costo confirma la hipótesis del Gate 3 del discovery: el dato ya existe (visible en el detalle de la solicitud) y no requiere integración nueva con el broker IVSA — por eso el esfuerzo es tan bajo. Con este costo, el ítem prácticamente no compite contra la Restricción de capacidad del equipo (~1 IDEA entregada cada 3 meses).

**Próximo paso (sin decidir todavía):** el PM va a llevar esta estimación a Emma Vignoles (COO) para decidir si se prioriza contra la capacidad ya comprometida en KR1 de Onboarding (foco de Pablo Gomes) — la decisión de construir sigue pendiente.
