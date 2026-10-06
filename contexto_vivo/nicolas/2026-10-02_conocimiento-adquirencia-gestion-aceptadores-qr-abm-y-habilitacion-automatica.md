---
id: 2026-10-02_conocimiento-adquirencia-gestion-aceptadores-qr-abm-y-habilitacion-automatica
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Mail 'Gestión de Aceptadores QR' — Martín Hovanyecz (Keep IT Simple), 2026-10-02; mail 'Documento funcional QA: Gestion de Aceptadores' — Mariano Panella (Keep IT Simple), 2026-10-02"
producto: adquirencia
tema: Nuevo desarrollo de Gestión de Aceptadores QR (ABM) con habilitación automática de QRs y endpoints de Consulta, Asignación y Habilitación de QRs; documentación en adjuntos sin descargar
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
---

**Qué existe.** Keep IT Simple (Martín Hovanyecz, con Juan Pablo Carubelli y Mariano Panella; Nicolás Pomponio de Fintexa y QA de Tec Financiera en copia) terminó un **desarrollo nuevo de Gestión de Aceptadores QR**. Incluye:
- un **ABM de aceptadores**;
- flujos anexos de **habilitación automática de QRs**;
- endpoints nuevos de **Consulta, Asignación y Habilitación de QRs**, documentados con su lógica y sus códigos de respuesta.

La documentación de negocio se mandó el 02/10 a Pablo Gomes y Nicolás Colón (adjunto `gestion-aceptadores-documentacion-negocio.html`). El mismo día se mandó a QA de Bind PSP (Ana Moreno) un documento funcional de pruebas (adjunto `aceptadores-pruebas-qa.html`), que también está cargado en Jira, para entender el alcance y probar.

**Estado.** El desarrollo está en QA. Pablo Gomes lo calificó de "muy claro y completo" y dijo que se va a pasar a Soporte cuando se avise que el proyecto quedó en producción. **Ningún adjunto se descargó en este barrido**, así que este item no trae el detalle de los endpoints ni de la lógica de habilitación. Cuando alguien lea los adjuntos, completar el archivo temático (probablemente nuevo en `adquirencia/`, o una sección de `configuracion_de_entidades.md` / `mecanica_qr_coelsa.md`, según el contenido).

**Producto dueño a confirmar.** Se asignó a Adquirencia porque "aceptador" es el comercio que cobra con QR. Si el desarrollo es de la Billetera (por ejemplo, el circuito interoperable de Getnet), el merge tiene que reubicarlo.

> Fuente: Mail "Gestión de Aceptadores QR" — Martín Hovanyecz (2026-10-02); Mail "Documento funcional QA: Gestion de Aceptadores" — Mariano Panella (2026-10-02).
