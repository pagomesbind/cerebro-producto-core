# Guía Técnica de Configuración de Entidades — Flujos y Wallet (Eco Cerrado)

> Estado: en producción. Reubicado desde `detalle_productos/wallet/otros_manuales.md §7` en la reestructuración PARA en cascada (2026-08-12). Guía técnica para configuración de entidades en Homologación y Producción, específicamente para el circuito de **eco cerrado** (comercio + wallet en la misma organización) — ver [cuentas_menores_y_eco_cerrado.md](cuentas_menores_y_eco_cerrado.md) para la descripción funcional del circuito. Documenta procedimientos de bajo nivel sobre tablas `Especificacion`, `EspecificacionTipo`, `EspecificacionGrupo`, asignación de canales y vinculación con cuentas BIND.
>
> Fuente original con adjunto PDF: "Guía Técnica de Configuración de Entidades, Flujos y Wallet.pdf".

## 1. Verificación previa de la entidad (SQL)

Antes de actualizar vía API, auditar el estado actual para evitar colisiones de configuración y duplicidad de registros:

```sql
SELECT
    eg.Descripcion AS 'Grupo',
    et.[Key] AS 'EspecificacionTipo',
    e.Valor
FROM Especificacion E
INNER JOIN EspecificacionTipo ET ON ET.ID = E.EspecificacionTipoId
INNER JOIN EspecificacionGrupo eg ON eg.Id = et.EspecificacionGrupoId
WHERE E.EntidadId IN (617,645,423,333) AND eg.Descripcion IN ('FLUJOS','WALLET');
```

## 2. Configuración en Homologación (IP: `10.210.1.6`)

Entidad Flujos: **617**. Entidad Wallet Organización: **342**. ⚠️ Respetar `valorEspecificacionTipo` para mantener integridad referencial.

- **Habilitación de Comercio** (grupo `FLUJOS`, key `HabilitacionComercio`, tipo `1`, valor `11`).
- **Alta de Comercio** (grupo `FLUJOS`, key `AltaComercio`, tipo `2`, valor `12`).
- **Update de Comercio** (grupo `FLUJOS`, key `UpdateComercio`, tipo `3`, valor `8`).
- **Aviso Transacción Wallet** (grupo `WALLET`, key `AvisoTransaccionWallet`, tipo `1`, valor `1`).
- **Wallet Organización** (Entidad 342, grupo `WALLET`, key `WALLET_ORGANIZACION`, tipo `1`, valor `62`).

Cada una se aplica con `POST http://10.210.1.6/api/v1/entidades/{entidadId}/especificaciones`, body:
```json
{
  "descripcionGrupo": "FLUJOS",
  "especificaciones": [{
      "keyEspecificacionTipo": "HabilitacionComercio",
      "valorEspecificacionTipo": "1",
      "valorDefault": "11",
      "valor": "11"
  }]
}
```

## 3. Configuración en Producción (IP: `10.22.0.17`)

> ⚠️ ADVERTENCIA CRÍTICA: verificar exhaustivamente los IDs productivos comparándolos con entidades reales (ej: La Virginia, Coto) antes de ejecutar scripts.

Ejemplo configuración organización: `{"nombre":"TF03","codigo":402,"billeteraId":184,"urlRedirectEnrolamiento":null,"codigoEntidad":"7","pspId":1}`

- **Habilitación Comercio** (Entidad 333, grupo `FLUJOS`, key `HabilitacionComercio`, tipo `1`, valor `18`) — vía `POST http://10.22.0.17/api/v1/entidades/333/especificaciones`.
- **Wallet Organización** (Entidad 333, grupo `WALLET`, key `WALLET_ORGANIZACION`, tipo `1`, valor `3`).

## 4. Configuración de canales

`idCanal: 2` → canal requerido para este flujo. `POST /api/v1/canalesEntidad/{codigo}` (Homologación código `A084` en `10.210.1.6`; Producción código `7` en `10.22.0.17`), body:
```json
[{ "idCanal": 2, "asignar": true, "datosCanal": { "conSplit": false } }]
```

## 5. Migración de comercio — Wallet

Ejemplo real: Comercio `C07943`, contexto `x-entidad: 9`. Se setean `WALLET_CUENTA` (valor `275205`) y `WALLET_CVU` (valor `0000532609360002752055`) vía `POST /api/v1/comercios/{comercio}/especificaciones` (grupo `WALLET`) con header `x-entidad`.

## 6. Tabla resumen de configuración

| Especificación | Homologación | Producción |
|---|---|---|
| HabilitacionComercio | 11 | 18 |
| AltaComercio | 12 | 17 |
| UpdateComercio | 8 | 15 |
| AvisoTransaccionWallet | 1 | 1 |
| Wallet Organización | 62 | 30 (Ent 423) / 3 (Ent 333) |

## 7. Verificación cuenta vendedor (BIND)

Para habilitar flujo DEBIN: `PUT {{apibank.url}}/v1/banks/322/accounts/{{account_id}}/transaction-requests` (ej. `account_id: 20-1-735135-30-5`). Se espera `200 OK` con `adhered: true`. Si el flujo automatizado falla, coordinar inserción manual con el equipo interno correspondiente.

## Ver también
- [cuentas_menores_y_eco_cerrado.md](cuentas_menores_y_eco_cerrado.md) — descripción funcional del circuito Eco Cerrado.
- [comercio_qr_acreditacion_wallet.md](comercio_qr_acreditacion_wallet.md) — circuito hermano de acreditación QR en wallet (sin eco cerrado).

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/wallet/otros_manuales.md §7` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
