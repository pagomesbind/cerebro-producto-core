---
id: 2026-09-23_conocimiento-ardid-segmentacion-wallet-payload-real-y-cambio-de-segmento
pm: nicolas
fecha_captura: 2026-09-23
fuente: "Confirmaciones del PM (Nicolás Colón) con capturas del uso real del equipo, sesión /idea_solution + /idea_us de ardid_limites_pj, 2026-09-17 al 2026-09-23"
producto: ardid
tema: Cómo crea hoy Wallet la segmentación en Ardid (BankType/ClientBankType reales, distintos del catálogo) y cómo se propaga el cambio de segmento de una cuenta
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/ardid/apis_externas.md §10.a — el catálogo del proveedor documenta /CreateClientBankType con `ClientTypeId` y `BankType` (1 empresa, 2 individuo) en PascalCase; el uso real del equipo no manda `ClientTypeId` y usa `bankType` = id del BankType creado. También 2_areas/direccion/oportunidades.md OP-017 (2026-09-02), que dice que Wallet no puede crear o actualizar segmentos en el Calculador de Costos."
confianza: alta
estado: ingestado
---

**Creación de la segmentación de una Organización en Ardid, tal como la hace hoy Wallet** (confirmado por el PM con capturas del uso real, 2026-09-22):

1. **Primero el tipo de banca (`BankType`), uno propio por Organización/Entidad** — nunca compartido. Se crea con dos query params, sin cuerpo: `Name` y `entityCode`. El catálogo del proveedor lo documenta como `POST /CreateBankType` (API `/BankTypes`), con respuestas `200` y `404` (nombre vacío, entidad no encontrada, entidad no segmentada, `entityCode` vacío). Wallet **guarda el Id que devuelve** y con ese Id crea los niveles ("primero se crea el BankType, se persiste el Id que devuelva, y con ese dato se crea el consecuente ClientBankType. Es uno nuevo cada vez" — PM, 2026-09-17). El catálogo no documenta rechazo por nombre repetido.
2. **Después los niveles (`ClientBankType`)**, con este cuerpo real (camelCase):
   ```json
   {
     "entityCode": "{código de la Entidad}",
     "bankType": {Id del BankType creado en el paso 1},
     "externalClientTypeId": 0,
     "name": "...",
     "description": "...",
     "personTypeId": 1
   }
   ```
   No se envía `ClientTypeId` (que sí figura en el catálogo). `personTypeId` va en `1` para todos los tipos de titular. `description` = `name`. `externalClientTypeId`: `0` persona física adulta y `1` persona física menor (en producción desde PRD-17/WS-53).
3. **Los procesos existentes** (alta de cuenta, job diario de graduación menor→mayor) ubican los niveles por los Ids guardados en las especificaciones de la Organización, **no por nombre** — renombrar un nivel no los rompe (confirmado por el PM, 2026-09-23).

**Nombres vigentes hasta hoy** (Organizaciones existentes): `Standard {Entidad}` (persona física adulta) y `Standard {Entidad} menor` (persona física menor), tanto para el `BankType` como para su `ClientBankType`. El proyecto `ardid_limites_pj` define una convención nueva para Organizaciones nuevas (`Persona Fisica Mayor/Menor {Entidad}`, `Persona Juridica {Entidad}`, con variante `... Restringido {Entidad}`) — se incorporará al canon cuando el proyecto cierre.

**Cambio de segmento de una cuenta** (confirmado por el PM, 2026-09-23): la operación de WalletCuenta `PATCH /api/v1/Cuenta/{id}/ActualizarSegmento` (header `x-entidad`, body `{"segmentoId": N}`, donde el segmento es el del Calculador de Costos) **ya pasa el cambio a Ardid para cualquier cuenta de Wallet**, siempre que el segmento del Calculador de Costos esté enlazado a su `ClientBankType` equivalente (campo `ardidClientBankTypeId` del segmento). No distingue persona física de jurídica. Los segmentos del Calculador de Costos se crean con `{tipo, codigo, descripcion, ardidClientBankTypeId, entidadIdExterno}`, y `tipo` y `codigo` tienen que ser únicos en toda la base, cada uno por separado (columna `nvarchar(MAX)`, probado por el PM).
