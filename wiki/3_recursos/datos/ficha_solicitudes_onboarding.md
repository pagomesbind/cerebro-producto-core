# Ficha de dataset — Solicitudes de Onboarding

> **Ubicación local (git-ignored, NUNCA subir a GitHub):** `datasets_locales/solicitudes desde mayo.csv`
> **Origen:** export directo de la base de Onboarding, provisto por el usuario (2026-07-16).
> **Rango:** desde 2026-05-01 inclusive hasta la fecha de extracción.
> **Volumen:** 38.152 filas, ~123 columnas, delimitador `;`, encoding con BOM UTF-8.

## Sensibilidad

- Campos de identidad **cifrados en origen** (sufijo `Encrypted`): Apellidos, Calle, Ciudad, CodigoPostal, Cuil, Departamento, Documento, DocumentoTramite, FechaNacimiento, Genero, Localidad, Municipalidad, Nombres, Email, Telefono, NombreFantasia, Cbu, NumeroCuenta, CuentaUID.
- Campos en **texto plano** a tratar con cuidado igual: `Ip`, `Dispositivo`, `IdOrganizacion`, `EntidadId`, `ExternalRefid`, `IdOperacion`, `CuilCalculado` (frecuentemente NULL), `LegajoDigitalTramiteId`.
- Nunca reproducir filas completas ni valores de estos campos en documentos de la wiki — solo agregados (conteos, distribuciones, porcentajes).

## Columnas de mayor interés analítico

- `Estado` (numérico, legend confirmado por el usuario 2026-07-16): `1`=Pendiente, `2`=Aprobada, `3`=Rechazada, `4`=Validación Manual, `5`=Pendiente credenciales, `6`=Error alta, `7`=Aprobado a Revisar, `8`=Aprobado sin notificar. El valor `9` aparece 3 veces en la extracción de mayo-2026 sin corresponder a ningún código del legend — anomalía menor, no bloqueante.
- `MotivoRechazo` (numérico, legend confirmado por el usuario 2026-07-16, 33 códigos — ver tabla completa y distribución real en [`hallazgos_2026-07-16_onboarding_vs_wallet.md`](hallazgos_2026-07-16_onboarding_vs_wallet.md) §0). Los códigos `36`, `37`, `38` y `43` aparecen en los datos reales pero **no están en el legend provisto** (que llega hasta `33`) — anomalía a confirmar con desarrollo, no se infiere su significado.
- `TipoSolicitud` (valores observados: `Tin`, `W`, `WC`, `WalletComercioEmail`, `WebPagos`, `Basic`, `update-productos-banco`, más una cola larga de valores tipo GUID — **no mapea 1:1 con los "7 tipos de consumo" del PRD-202 sin confirmación de backoffice/desarrollo**; 23% de filas tiene este campo en `NULL`)
- `IdOrganizacion` (61.8% de las filas está en `NULL` — limita fuertemente cualquier análisis por organización desde este dataset)
- `ExternalRefid` (poblado en ~27.9% de las filas — el campo ya existe y se usa parcialmente hoy, no es un campo nuevo)
- `AddaliaPruebaVida`, `AddaliaValidacionFacial`, `UrlEnrollment`, `IntentosEnrollment` (prueba de vida — ver nota de nomenclatura en el hallazgo del 2026-07-16: el campo real dice "Addalia", no "Socialnet")
- `Step`, `IdAutenticacion`, `UrlAutenticacion` (trazas del flujo paso a paso)
- Flags de altas ejecutadas: `AltaClienteBantotalCompleto`, `AltaCredencialesCompleto`, `AltaComercioCompleto`, `AltaProductoCompleto`, `AltaWalletCompleto`, `AltaCuentaBancaria`, `AltaCuentaComitente`, `AltaCuentaPrincipal`, `AltaCuentaInvestment`, `AltaTDCompleto`

## Cómo volver a analizar este dataset

Delimitador `;`, con BOM al inicio del archivo. Usar `awk -F';'` o herramienta equivalente; evitar cargarlo completo en memoria de un LLM (37MB, ~38k filas) — preferir agregaciones vía línea de comandos (`awk`/`cut`/`sort`/`uniq -c`) y nunca imprimir filas individuales.
