---
id: 2026-10-02_wallet_conocimiento_procedimiento_rescate_masivo_fci_poincenot
pm: pablo
fecha_captura: 2026-10-02
fuente: "/sync_mails — hilos \"Comitentes Astropay con saldo\" (threadId 1a0e865d6b79a31d) y \"RV: Astropay FCI - Rescate masivo de cuentas\" (threadId 1a0f88f4086736e6), 2026-09-28/2026-10-02"
producto: wallet
tema: Procedimiento operativo de rescate masivo de FCI vía API Broker Poincenot — limitación de Swagger para JSON extensos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/api_broker_poincenot.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

BIND Inversiones (Gastón Degiovanni) pidió instruir el rescate total de **74 comitentes con saldo en Astropay** (cuentas remanentes del producto, en proceso de salida/discontinuación). Pablo Gomes derivó el pedido al equipo de soporte (Gonzalo Rivera, Mariana Nadalin), que coordinó la ejecución técnica con Fintexa/Keep IT Simple. Guillermo Bonino (Keep IT Simple) documentó el **procedimiento operativo real para un rescate masivo de FCI** contra la API Broker (Poincenot/IVSA):

1. Convenir con el negocio (BIND Inversiones) la **fecha exacta** de ejecución.
2. El negocio solicita a Poincenot el **reporte de posición de cada cuenta** actualizado a esa fecha, en Excel. La columna relevante es **"Monto Valuado en Moneda del Fondo"** — el reporte debe sacarse el mismo día convenido, porque el cálculo depende del **VCP (valor cuotaparte)** vigente ese día.
3. Con ese Excel, Keep IT Simple arma el **JSON de la solicitud de rescate masivo** a enviar a Poincenot.
4. Ejecución del endpoint correspondiente desde el **swagger del wrapper de Poincenot**.

**Limitación técnica real detectada:** para una tanda de 74 cuentas, el JSON generado es lo bastante extenso como para que **Swagger UI no permita ejecutar la llamada desde su propia interfaz** (body demasiado grande). En ese caso, la solicitud debe ejecutarse **vía Postman desde el bastión de producción** — requiere tener a mano un acceso al bastión con Postman configurado de antemano.

Se adjuntó un JSON de ejemplo (`paquete-rescates-poincenot.json`) generado a partir del Excel de referencia, para validar formato.

> Fuente: hilos de mail "Comitentes Astropay con saldo" (Gastón Degiovanni, BIND Inversiones, 2026-09-28/2026-10-01) y "RV: Astropay FCI - Rescate masivo de cuentas" (Guillermo Bonino vía Nicolás Pomponio, Fintexa, 2026-10-01), threadIds `1a0e865d6b79a31d` y `1a0f88f4086736e6`.
