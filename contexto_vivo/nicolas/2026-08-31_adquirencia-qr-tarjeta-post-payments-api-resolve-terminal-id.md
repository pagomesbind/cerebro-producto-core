---
id: 2026-08-31_adquirencia-qr-tarjeta-post-payments-api-resolve-terminal-id
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Análisis COBRO\" (2026-08-31)"
producto: adquirencia
tema: QR Tarjeta — definiciones técnicas de Post-payments, Terminal ID en API Resolve, validación de rubro por canal y webhook con aranceles
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Análisis COBRO" (2026-08-31, Daniela Collia y equipo Fintexa, Pablo Gomes, Nicolás Colón, Luciana Rudaz, Matías Alzogaray) se avanzó sobre el desarrollo de QR Tarjeta (pago con tarjeta desde wallets terceras, cliente MODO — ya documentado en `boton_simple_2_0.md`), continuación de la tarea T-010 (`tareas.md`). Definiciones acordadas:

- **Especificación de Post-payments separada de Botón Simple:** se decidió crear un ticket y especificación técnica nueva para "post payments" en vez de reutilizar la de Botón Simple, porque los requisitos de configuración de canal son distintos.
- **Terminal ID en API Resolve:** se discutió qué dato enviar como "terminal ID" (se había considerado un valor aleatorio). Se acordó mantener el uso del **código de comercio como identificador de terminal**, interpretando que el flujo de alta por comercio representa la caja para este propósito — a validar con Modo.
- **Validación de rubro de comercio vs. site ID del canal:** el rubro del comercio solo se conoce a nivel comercio, no a nivel entidad, lo que complica el filtrado del site ID en el dropdown de configuración de canal. Se acordó que si el site ID no es compatible con el rubro del comercio, el sistema **no bloquea** — muestra una advertencia/error y deja la corrección manual a cargo del usuario, para no comprometer la integridad de datos sin frenar la operación.
- **Requiere más debate (sin cerrar):** restringir la configuración de canales para comercios no habilitados mostrando un mensaje de error directo — Nicolás Colón lo va a analizar, no está confirmado.
- **Mejora de UX en Admin:** mover el botón de "guardar" dentro de cada sección de canal, para que solo aparezca la primera vez que se configura (en vez de un botón único fuera de las secciones).
- **Webhook de Cobro QR exitoso — nuevos campos:** se agregarán al evento el porcentaje y monto del arancel aceptador, y el importe neto del arancel, para que las entidades agregadoras tengan la info impositiva sin tener que hacer una consulta adicional a la transacción. Pendiente de definir si va dentro del objeto de mensaje de pago o como info adicional (para no romper integraciones existentes).
- **Endpoints en desarrollo:** se retomó "get payments" y "get order"; "patch plans" está listo para desarrollo pero bloqueado en stage por un código de billetera que rompe las pruebas generales (requiere intervención técnica); "Paymis Notify" debe rediseñarse desde cero.
- **Performance de generación de archivos (ticket 1144):** la segunda parte de la mejora busca eliminar llamadas repetitivas/bucles innecesarios; sin fallas críticas reportadas hoy, es preventiva.
- **Campo "purpose of payment":** solo se incluye cuando es obligatorio para Mastercard; si llega vacío el arreglo de valores soportados sería un caso de error, aunque poco probable (Flavia Salmeron/Fintexa, Luciana Rudaz).

Próximos pasos a cargo de Nicolás Colón: crear los tickets de post-payments, API Resolve (terminal ID) y herramientas de configuración de pago (dropdown de procesador); implementar la mejora de UI de canal; consultar con Euge sobre errores de performance previos — ver T-010 actualizada en `tareas.md`.
