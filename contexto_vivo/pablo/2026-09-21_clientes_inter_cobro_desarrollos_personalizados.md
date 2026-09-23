---
id: 2026-09-21_clientes_inter_cobro_desarrollos_personalizados
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Producto\" (14:01, con Emma Vignoles/Nicolás Colón), 2026-09-21"
producto: onboarding
tema: Inter — decisión de empezar a cobrar por desarrollos personalizados; 180 solicitudes en cola de verificación manual (cotizadas 70h); propuesta de cuenta comitente en dólares en evaluación
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 25b8e37
---

**Cliente ya con ficha:** Inter (`log_clientes.md`, productos Wallet/Dólar CCL, alta 2025-12-02).

**Decisión acordada en la reunión:** Bind PSP empieza a **cobrar a Inter por cotizaciones y desarrollos de funcionalidades personalizadas** que pide fuera del alcance estándar — antes esto no estaba formalizado. Mauro queda en redactar el proceso de cobranza para Inter.

**Pedido 1 — reprocesamiento masivo de verificaciones manuales:** Inter reportó **180 solicitudes acumuladas en verificación manual de onboarding**, imposibles de procesar una por una. Nicolás Colón (tras consultar con Cristian Bonafede, Fintexa) confirmó que se puede agregar funcionalidad de reprocesamiento masivo al frontend de onboarding — estimación inicial de 3 días de trabajo, ajustada en la reunión a una **cotización final de 70 horas**, a cobrar a Inter.

**Pedido 2 — columna de motivo de error:** segundo pedido de Inter (frontend de onboarding): agregar una columna con el detalle del motivo de error en el alta de cuentas en el broker — originalmente tasado en menos de un punto de historia, pero al sumar visualización + exportación a Excel la estimación sube a **40 horas**. Alan (comercial) había indicado inicialmente que Inter no pensaba pagarlo — se ratificó en la reunión que si no acepta el pago, no se hace el desarrollo.

**Pedido 3 — cuenta comitente en dólares:** Inter propuso, para una próxima reunión de producto, la posibilidad de **comprar y transferir dólares para retenerlos en una cuenta comitente**. Se marcó preocupación por la complejidad de integrar esto con IPSA — requiere evaluar el alcance con el equipo técnico y comercial; falta asignar a alguien de Producto para gestionar la relación con Inter en este frente. Sin alcance ni estimación todavía.

**Pedido 4 — integración de legajos vía API:** Inter exige compartir el 100% de los legajos de sus ~10.000 cuentas de clientes existentes. Como Cumplimiento no autoriza legajos incompletos, Bind PSP está construyendo una API para que Inter envíe la documentación y validaciones completas del onboarding directamente — a revisar con Cumplimiento.

**Reunión semanal:** Nicolás Colón y Alan tienen reunión semanal con Inter para tratar los temas pendientes de producto — sin fecha puntual mencionada en esta minuta.
