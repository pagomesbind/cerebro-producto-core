---
id: 2026-09-08_iniciativa-onboarding-shared-kyc-worsis-limite-pj-freeze-webhooks
pm: nicolas
fecha_captura: 2026-09-09
fuente: "Reunión \"Producto\" (2026-09-08), minuta Gemini"
producto: onboarding
tema: Arquitectura de alta de personas jurídicas (Shared KYC/Worsis), límite operativo PJ y freeze de webhooks
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: ingestado
proyecto: onboarding_estrategico (Pablo Gomes) — nombre exacto de la carpeta/proyecto en su instancia sin confirmar desde acá
pm_destino: pablo
---

Reunión "Producto" (2026-09-08, 16:00) — invitados: Luciana Rudaz, Pablo Gomes, Emma Vignoles, Matías Alzogaray, Nicolás Colón. Foco: arquitectura y cumplimiento normativo para la integración de sistemas mediante un microservicio **Shared KYC** y su relación con **Worsis** (proveedor externo de legajos digitales), en el marco de cuentas de personas jurídicas ya aprobadas por cumplimiento. Este tema corresponde al foco estratégico de Onboarding de Pablo Gomes, no a un proyecto propio de este Cerebro — se captura como iniciativa para su revisión.

**Decisiones acordadas en la reunión:**
- **Arquitectura de validación y onboarding:** se acordó implementar la arquitectura donde Wallet interactúa con Shared KYC para la validación y el procesamiento de alta de cuentas.
- **Límite operativo para cuentas jurídicas:** se acordó permitir la creación de cuentas de personas jurídicas aplicando un límite operativo máximo de **$1.000** hasta que se presente la documentación de respaldo requerida (ver item de decisión separado, `2026-09-08_decision-limite-1000-cuentas-personas-juridicas-sin-documentacion`, propuesto también para `direccion/decisiones.md` por tratarse de una regla que afecta el alta de cuentas en Wallet, no solo el backlog de Onboarding).
- **Freeze de webhooks:** se acordó detener los cambios propuestos sobre el webhook para no incluir datos adicionales que puedan romper integraciones de clientes actuales (ver item de decisión separado, `2026-09-08_decision-freeze-cambios-webhook-integraciones-clientes`).
- **Auditoría de licencias:** se acordó un mapeo y revisión conjunta de herramientas y licencias (ej. Sira, Notion) para optimizar costos y uso — sin asignación puntual registrada en la minuta.

**Pendientes de más debate (no decididos todavía):**
- Si se mantiene un repositorio interno de legajos digitales o se depende de Worsis — pendiente de costos de infraestructura/almacenamiento.
- Explorar integración alternativa a Mastercard si no se compromete una fecha de entrega — pendiente de validación y análisis de contratos.
- Evaluar a Manteca como proveedor de pagos regionales — se propuso coordinar una reunión con su CEO y estimar costos.

**Próximos pasos relevantes (fuente: minuta completa):**
- [Pablo Gomes] Crear tickets de desarrollo para la arquitectura de alta de cuenta, omitiendo temporalmente la integración con Worsis; investigar costos de Legajo Digital propio vs. Worsis; actualizar documentación de la billetera; definir costos de Worsis.
- [Emma Vignoles] Apoyar el análisis de costos de infraestructura; formalizar el pedido de servicio de FaceTech; reunirse con Coto y BCF para explicar el cambio de normativa y su impacto operativo; coordinar reunión con Manteca (jueves).
- [Luciana Rudaz] Estimar el costo de desarrollo de un webhook completo.

> Nota: los próximos pasos asignados a Nicolás Colón en esta misma reunión (gestión de Compliance con Vicky, coordinación de regresión con Luciana, unificación de temas de cumplimiento con Pablo Gomes, pruebas de regresión en stage con credenciales "mood") se registraron directo en `wiki/1_proyectos/tareas.md` (T-036 a T-039) — no requieren pasar por `contexto_vivo/`.

> Nota para el merge: dado que Onboarding es foco estratégico de Pablo Gomes, este item es principalmente para su conocimiento/registro en su propio `decisiones.md`/`proyecto.md` — el merge puede optar por solo dejar una fila de novedad en `direccion/iniciativas.md` sin duplicar el detalle de las decisiones ya cubiertas en los dos items de decisión asociados.
