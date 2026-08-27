---
id: 2026-08-20_adquirencia_reglas_dinamicas_prisma_gp
pm: pablo
fecha_captura: 2026-08-20
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-08-20 12:05, docId 1Q3PZO-WuwDNq5HOyW-eoww1KEVJBvwL7-NP9nT3WMkE)"
producto: adquirencia
tema: Deuda técnica de reglas de procesadores Prisma/GP — decisión de pasar a parámetros de canal dinámicos
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/pos_multiadquirencia.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Deuda técnica confirmada:** el sistema convive con dos procesadores de pago (Prisma y GP) usando grupos de reglas de procesador mal estructurados para la coexistencia — genera problemas operativos al intentar operar con ambos simultáneamente (Daniela Collia, Fintexa). Este hallazgo complementa lo ya documentado en `pos_multiadquirencia.md` sobre el modelo de 2 etapas (Etapa 1: GP por defecto conviviendo obligatoriamente con PRISMA, deuda técnica reconocida) — ahora se define **cómo** resolver esa deuda.

**Decisión acordada (2026-08-20):** en vez de mantener grupos de reglas rígidos por procesador, el proceso pasará a tomar los valores de los **parámetros del canal** directamente — evita ciclos repetitivos de modificación de reglas cada vez que cambia algo. Alcance del ajuste aceptado: adaptar el proceso de lectura de parámetros, no rediseñar la estructura de reglas de cero.

**Acciones de seguimiento (no asignadas a Producto):** Daniela Collia (Fintexa) va a compartir el detalle de la deuda técnica de reglas con Nicolás Colón para que la cargue como ticket formal en el sistema de Bind PSP.

**Además, en la misma reunión — despliegue de un ticket de Prisma sin completar su configuración en el admin:** se decidió proceder con el despliegue pese a que la funcionalidad de configuración desde el panel administrativo (que permitiría seleccionar Prisma como procesador único, hoy el sistema habilita GP por defecto) no está terminada — Cristian Medina y Daniela Collia (Fintexa) confirman que el backend está preparado pero la interfaz de administración no permite esa configuración flexible. El ticket no cumple todos los requisitos de Definition of Done, pero se aprueba el despliegue para no atrasar el cronograma, dejando la limitación de la interfaz administrativa para abordar por separado. Esto es consistente con la limitación ya documentada en `pos_multiadquirencia.md` de que Prisma no puede configurarse hoy como primer procesador (GP hardcodeado como paso previo obligatorio).

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini. Invitados: Luciana Rudaz, Pablo Gomes, Nicolás Colón, Matías Alzogaray, Daniela Collia, Melisa Belpassi, Flavia Salmerón, Marcos Sánchez, Cristian Medina, Julieta Giménez (Fintexa).
