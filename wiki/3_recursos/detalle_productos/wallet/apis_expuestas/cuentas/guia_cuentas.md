# Guía — ¿Qué debes saber sobre las cuentas? (Wallet)

> Extraído el: 2026-07-01
> Fuente: https://psp.bind.com.ar/developers/apis/guia-cuentas
> Producto: Wallet — Cuentas

---

La cuenta identifica al titular de cualquiera de los productos de wallet que luego necesites crear. Luego para una cuenta se relacionará un único CVU y/o una única cuenta comitente y/o una única cuenta cripto, etc. Es decir, que no se podrá asociar más de un mismo producto a una cuenta.

Cada cuenta debe identificarse con un CUIT. Pueden crearse más de una cuenta para una misma persona (mismo CUIT).

Pueden crearse cuentas tanto a personas físicas como a personas jurídicas.

Pueden deshabilitarse las cuentas. Si una cuenta está deshabilitada no podrá realizar cash out de ningún tipo. Sin embargo, sí podrá recibir cash in. Esto permite bloquear usuarios para proteger su saldo pero permitir que ingresen más dinero.

Entonces, si la entidad quiere desactivar completamente la operatoria de un titular deberá también eliminar cada uno de los productos asociados a su cuenta. Por ejemplo, para evitar que el titular pueda usar su cuenta virtual para ingresar dinero debe eliminarse su CVU asociado.

Bind PSP puede deshabilitar una cuenta arbitrariamente por diferentes motivos justificados. En este caso, se notificará de este evento a la entidad mediante un webhook.

Si la entidad usa la licencia de PSP de Bind PSP, las cuentas sólo deben crearse si el titular superó las validaciones de KyC o KyB mínimas exigidas por el PSP. La entidad puede demostrar que utiliza medios de validación propios suficientes o si no puede consumir el producto Onboarding de Bind PSP.

## Flujo — Estructura y ciclo de vida de una cuenta

```
ESTRUCTURA (por organización/entidad):

  ORGANIZACIÓN
    ├── CBU RECAUDADORA (única, del PSP)
    └── CUENTAS (N cuentas, una por titular)
          ├── CVU (único por cuenta)
          ├── CUENTA COMITENTE (único por cuenta)
          └── ADDRESS CRIPTO (único por cuenta)

  Regla: 1 cuenta por titular puede tener como máximo 1 de cada producto.
  Excepción permitida: mismo CUIT puede tener más de una cuenta.

CREAR CUENTA:
  1. POST /cuenta (CUIT + datos del titular)
     → Requisito si usa licencia PSP de Bind: titular debe haber pasado KYC/KYB
     → Puede ser persona física o jurídica

HABILITAR / DESHABILITAR:
  PATCH /cuenta/{id} (habilitar=true/false)
  → Deshabilitada: NO puede hacer cash out, SÍ puede recibir cash in
  → Para bloquear también el cash in: eliminar el CVU asociado
  → Bind PSP puede deshabilitar arbitrariamente → EVENT webhook a la entidad

MODIFICAR DATOS:
  PUT /cuenta/{id}
```

## Endpoints disponibles

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Crear cuenta | endpoint_post_crear.md |
| `PATCH` | Habilitar/deshabilitar cuenta | endpoint_patch_habilitar_deshabilitar.md |
| `PUT` | Modificar cuenta | endpoint_put_modificar.md |
| `GET` | Consultar cuenta por ID | endpoint_get_consultar_id.md |
| `GET` | Consultar cuentas por CUIT | endpoint_get_consultar_cuit.md |
| `GET` | Consultar cuentas por email | endpoint_get_consultar_email.md |
| `GET` | Consultar cuentas por celular | endpoint_get_consultar_celular.md |
| `EVENT` | Aviso de cuenta deshabilitada | endpoint_event_cuenta_deshabilitada.md |
