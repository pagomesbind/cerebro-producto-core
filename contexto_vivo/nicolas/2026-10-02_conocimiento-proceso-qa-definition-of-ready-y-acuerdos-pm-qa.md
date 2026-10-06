---
id: 2026-10-02_conocimiento-proceso-qa-definition-of-ready-y-acuerdos-pm-qa
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Mail 'Re: Updated invitation: PM + QA @ Fri Sep 18, 2026' — resumen de Andrea Orsini (Líder de Calidad) del 2026-09-18, reenviado con FYI el 2026-10-02; y mail 'Re: Gestión de Aceptadores QR' — Pablo Gomes, 2026-10-02"
producto: transversal
tema: Acuerdos de la reunión PM + QA (18/09) — Definition of Ready para tickets que van a QA externo de Bind PSP, versiones más acotadas, menos temas por ventana, ordenar los pasajes de OB; más el pedido de Pablo Gomes de documentación estándar por proyecto cerrado
tipo: conocimiento
destino_propuesto: 2_areas/procesos/requerimientos_al_equipo_tecnico.md
tipo_destino: actualizar
contradice: "no — formaliza como acuerdo la propuesta 2 ('tickets a QA con documentación completa') que el item 2026-09-29_conocimiento-proceso-ad73-cancelacion-comite-cambios-hotfix-y-tickets-a-qa dejó en stand-by. Ese acuerdo es del 18/09, o sea anterior a la minuta del 24/09; conviene que el merge los fusione"
confianza: alta
estado: en_cola
---

**Acuerdos de la reunión "PM + QA" (18/09/2026).** Los resumió Andrea Orsini (Líder de Calidad de Bind PSP). Participantes: Hernán Clarich (organizador), Fintexa (Nicolás Pico, Melisa Belpassi, Mariela Marin, Nicolás Pomponio, Pablo Serra) y, en copia, Analía Dobrodzejunas (PM de OB, que empieza a sumarse a estas reuniones), Matías Alzogaray, Pablo Gomes, Nicolás Colón y Luciana Rudaz. Orsini lo reenvió con FYI el 02/10.

Acciones para reducir el cuello de botella de QA:
1. **Versiones más acotadas.** El objetivo es terminar las pruebas y dejar toda la publicación lista **1 o 2 días antes** de la fecha del pasaje.
2. **Menos temas por ventana.** Tiene que ser un compromiso del negocio: **Comercial y Producto**. Orsini propone sumar a estas reuniones a los responsables de Comercial y Operaciones, que no conocen este punto.
3. **Definition of Ready (DoR) para US y OBS.** Si un ticket enviado a QA externo (de Bind PSP) no cumple el DoR, **vuelve al estado "En curso"** hasta que cumpla. El DoR exige:
   - Un resumen de las definiciones finales acordadas entre Producto y Análisis Funcional, claro y conciso, con todo lo necesario para probar.
   - Si se actualiza o agrega un endpoint, el endpoint en el documento con indicaciones claras de cuál usar.
   - Si hacen falta credenciales, incluidas en la documentación.
   - Si el endpoint lo pueden consumir los clientes, **ya publicado en APIM** y con el detalle de cómo encontrarlo en la plataforma.
   - Un resumen de las pruebas principales que hizo QA de Fintexa/SA, con los pasos para reproducirlas.
   - Si se necesitan pruebas de estrés o performance, la evidencia de que QA de Fintexa las hizo.
   - Documentación complementaria si hace falta.
4. **Proyecto OB.** Trabajarlo igual que Wallet y AD: pasajes ordenados, coordinados en tiempo y forma, y más acotados. Los desarrollos de OB tienen que venir **con testing hecho** por QA, SA o Fintexa. Hernán Clarich lo lleva a hablar con Emma Vignoles, Sebas y Franco.

**Estándar de documentación por proyecto cerrado (Pablo Gomes, 02/10).** Al recibir de Keep IT Simple la documentación de negocio de "Gestión de Aceptadores QR" (todos los endpoints, con su lógica y sus códigos de respuesta), Pablo Gomes pidió que **esa misma estructura se entregue con cada proyecto cerrado** de ahora en más, o "cerrado estructuralmente", sin esperar al último bug. También quiere los **códigos de error existentes en todas las APIs expuestas**. Esa documentación se va a pasar a los equipos de Soporte cuando se avise que el proyecto quedó en producción. Por ahora es un pedido al proveedor, no un proceso formalizado.

**Dato al margen:** Keep IT Simple (Mariano Panella) mencionó que generó el documento funcional de QA de Aceptadores "con el comando BIND". Parece una herramienta o plantilla propia del proveedor para generar documentación, sin más detalle.

> Fuentes: Mail "Re: Updated invitation: PM + QA @ Fri Sep 18, 2026 2:30pm - 3:30pm (GMT-3)" — Andrea Orsini (resumen del 2026-09-18, reenviado el 2026-10-02); Mail "Re: Gestión de Aceptadores QR" — Pablo Gomes (2026-10-02); Mail "Documento funcional QA: Gestion de Aceptadores" — Mariano Panella (2026-10-02).
