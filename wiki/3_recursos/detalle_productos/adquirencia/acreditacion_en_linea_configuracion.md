# Crear y Configurar Entidad como Acreditación en Línea (Modelo Coto)

> Estado: en producción. Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` en la reestructuración PARA en cascada (2026-08-12). Ver [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) para el contexto conceptual del modelo de acreditación en línea/wallet.

## 1. Agregar especificaciones a la entidad

Usando el endpoint **Crear una especificación** del swagger de comercios (`http://10.22.0.17/swagger/index.html`):

- `EspecificacionTipoId = 2281`, valor = id de la organización wallet (ej. `37` para COTO) — asocia la entidad de cobro a la organización de wallet.
- `EspecificacionTipoId = 2350`, valor = `12` — al dar de alta un comercio, admite setear el CVU externo indicado al crear (incluye admitir comercios con CUIT duplicados).
- `EspecificacionTipoId = 2061`, valor = `11` — al habilitar QR en un comercio, indica que no debe crear el CVU sino sacarlo del CBU.
- `EspecificacionTipoId = 3487`, valor = `1` — indica que por cada cobro QR debe avisar a wallet creando los comprobantes.
- `EspecificacionTipoId = 3505`, valor = `1` — indica que admite comercios con CUIT repetidos.

**Configuración de referencia — STG (ejemplo Eco Cerrado):**

| keyEspecificacionTipo | valorEspecificacionTipo | valor | grupo |
|---|---|---|---|
| AltaComercio | 2350 | 17 | FLUJOS |
| HabilitacionComercio | 2061 | 18 | FLUJOS |
| UpdateComercio | 2395 | 15 | FLUJOS |
| AvisoTransaccionWallet | 2510 | 1 | WALLET |
| WALLET_ORGANIZACION | 2147 | IDOrganizacion | WALLET |

Body de ejemplo: `{"descripcionGrupo":"FLUJOS","especificaciones":[{"keyEspecificacionTipo":"AltaComercio","valorEspecificacionTipo":"2350","valorDefault":"0","valor":"17"}]}`

## 2. Crear Cuenta y CVU

(Paso mencionado sin detalle adicional en la fuente — ver [detalle_productos/wallet/comercio_qr_acreditacion_wallet.md](../wallet/comercio_qr_acreditacion_wallet.md).)

## 3. Adherir como vendedor a cuenta recaudadora

(Paso mencionado sin detalle adicional en la fuente — ver "Adhesión de vendedor" en [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md).)

## 4. Crear comercios

Crear comercios todos con la Cuenta y CVU pre-creada. En `datosWallet`: `WALLET_CUENTA` (id cuenta wallet), `WALLET_ORGANIZACION` (id organización wallet), `WALLET_CVU` (CVU); `Cbu`/`Cvu` a nivel raíz con el mismo CVU; enviar `miembroUsuario`/`miembroContrasenia` con el valor deseado.

Request real usado para el primer comercio (COTO CICSA, sucursal Paysandú):
```json
{
  "nombre": "COTO CICSA", "calle": "Paysandu 1842", "codigoPostal": "1416",
  "codigoProvincia": 1, "codigoLocalidad": 230, "email": "tarjetasdecredito@coto.com.ar",
  "telefono": "1145852244", "cuit": "30548083156",
  "Cbu": "0000184305330026339729", "Cvu": "0000184305330026339729",
  "descripcion": "COTO CICSA", "mcc": "5411", "actividadEconomicaAfip": "471120",
  "categoriaIva": "RI", "rubroRg461419": "01", "tipoCuenta": "13", "condicionibb": "3",
  "sicore": "00", "tipoPersona": "J", "conSplit": false,
  "sucursal": [{
      "calle": "Paysandu 1842", "nombre": "Casa Central", "codigoProvincia": 1, "codigoLocalidad": 230,
      "email": "tarjetasdecredito@coto.com.ar", "telefono": "1145852244", "codigoPostal": "1416",
      "caja": [{ "nombre": "Casa Central", "soloOrden": true, "tipoCajaId": 1 }]
  }],
  "datosWallet": { "WALLET_CUENTA": "2633972", "WALLET_ORGANIZACION": "37", "WALLET_CVU": "0000184305330026339729" },
  "esPep": false, "nacionalidad": "AR"
}
```

Para sucursales adicionales (ej. SUCURSAL 2 del mismo comercio) se agregan además `miembroNombre`, `miembroApellido`, `miembroUsuario`, `miembroContrasenia` con el valor deseado para el usuario que se crea junto a la sucursal.

## Ver también
- [configuracion_de_entidades.md](configuracion_de_entidades.md) — flujo general de creación de entidad, del que este es un caso especializado.
- [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) — mecánica conceptual de acreditación en línea/wallet.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
