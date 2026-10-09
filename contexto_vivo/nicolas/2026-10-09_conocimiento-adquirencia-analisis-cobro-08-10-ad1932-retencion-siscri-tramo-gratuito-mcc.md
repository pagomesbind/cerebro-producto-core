---
id: 2026-10-09_conocimiento-adquirencia-analisis-cobro-08-10-ad1932-retencion-siscri-tramo-gratuito-mcc
pm: nicolas
fecha_captura: 2026-10-09
fuente: "Reunión 'Análisis COBRO' (2026-10-08, ~12:00), solo el resumen del mail de Gemini (mail Gmail 1a11c420118a1a92). Drive desconectado, sin minuta completa"
producto: adquirencia
tema: "Análisis COBRO del 08/10: AD-1932 suma al alcance el aviso de retención a Siscri, el tramo gratuito pasa a un endpoint propio, validación de MCC con comisión 0,05, cambio de razón social (ticket 1035), error de importes en el CSV del admin de transacciones y épica para el admin"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no. Actualiza el item 2026-10-06_conocimiento-ad-v74-tickets-en-evaluacion-dat-2578-dat-3347-ad-1932-3425: AD-1932 ya no está solo 'en evaluación', ahora se cierra con un alcance ampliado"
confianza: media
estado: en_cola
---

**Liquidaciones / AD-1932.** Se cierra el análisis del ticket AD-1932 de liquidaciones. El cambio de lógica de **retención** para avisarle a **Siscri** (la minuta dice "Siscre") se incorpora **dentro del alcance de AD-1932**, sin abrir un ticket nuevo. Así la API de retención queda integrada con Siscri y se evitan retrasos. Daniela Collia (Fintexa) reanaliza y ajusta el alcance; después Producto copia el análisis final a la descripción del ticket. Queda abierto si el **archivo de orden de pago** sigue en uso o si todo sale ya de la tabla de liquidación. Producto lo consulta con Euge, y de eso depende si hay que corregir ese archivo.

**Comercios y comunidades:**
- **Cambio de razón social:** se actualizó la razón social de un comercio en Coelsa (la minuta dice "Alira Coelsa", nombre dudoso). El desarrollo general de cambio de razón social es el **ticket 1035**; Daniela Collia analiza las necesidades de los clientes y las reglas de negocio para definir su alcance.
- **Tramo gratuito:** se acordó crear un **endpoint dedicado** para modificar el tramo gratuito de un comercio, **separado de la modificación general del comercio**, para evitar errores al tocar otros datos. Lo define Producto.
- **Validación de comisiones:** se busca automatizarla. Primer caso: validar el **MCC** al cargar una **comisión de 0,05**. Daniela Collia crea el ticket.
- Se va a crear una **épica para las modificaciones y mejoras generales del panel de administración**. Producto define qué tickets de mejora de los discutidos se crean y cuáles no.

**Admin de transacciones:** se detectó un **error en los importes de los CSV** que se descargan desde el admin de transacciones. Flavia Salmerón y Producto buscan la causa raíz.

**Cuentas de usuario / ticket 1713:** se avanza con las cuentas de usuario cargadas, a partir de los arreglos de "Vini" del ticket 1713.

> Fuente: Reunión "Análisis COBRO" (2026-10-08), resumen del mail de Gemini.
