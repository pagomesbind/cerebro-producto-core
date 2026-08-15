# Guía — ¿Qué debes tener en cuenta del saldo?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-saldopesos
> Producto: Wallet — Saldo en pesos

## Descripción

Por cada cuenta de wallet se lleva una cuenta corriente de los movimientos en pesos argentinos que resulta en un saldo.

En cualquier momento se puede consultar el saldo actual de una cuenta. Pero también se puede consultar el saldo histórico que tuvo una cuenta un día anterior pero sólo al momento del cierre.

Por cada cuenta corriente se registra de forma cronológica y en línea cada ajuste de saldo de crédito o de débito que tenga. Estos ajustes de saldo se llaman **comprobantes**.

Naturalmente, el sistema se encarga de gestionar los comprobantes por cada operación específica. Por ejemplo: para una operación de transferencia saliente, inmediatamente antes de procesarla, se crea un comprobante de débito para descontar el saldo necesario para cursarla. Si la transferencia es exitosa, queda el saldo descontado, pero si la transferencia falla en el momento de su procesamiento, el sistema crea además un comprobante de crédito para devolver el saldo previamente descontado en concepto de reversa.

Sin embargo, la entidad es libre de crear sus propios comprobantes sobre las cuentas corrientes por más que no estén asociados a operaciones de Bind PSP. Esto puede realizarlo para ajustar sobre el saldo de sus cuentas para realizar operaciones propias de su negocio. Por ejemplo: débito por retiro en efectivo, crédito por una promoción, débito para cobrar un servicio, etc.

Para esto, la entidad debe crear sus propios tipos de comprobante para así justificar cada tipo de movimiento diferente que necesite realizar sobre las cuentas.

Los saldos de las cuentas son virtuales pero el dinero que se utilice para realizar operaciones al exterior es el que se encuentra en la cuenta recaudadora del PSP asociada a la entidad.

El ajuste de saldos de cuentas corrientes mediante comprobantes no necesariamente implica un movimiento financiero. Por eso la entidad debe ser responsable de velar porque al final del día la sumatoria de los saldos de sus cuentas corrientes sea menor o igual que el saldo total en la cuenta recaudadora.

> **Regla clave:** La entidad debe asegurar que al final del día el saldo de la cuenta recaudadora sea mayor o igual que la sumatoria de los saldos de todas las cuentas corrientes.

## Modelo conceptual — Cuentas corrientes y comprobantes

```
Cuenta Wallet
  │
  ├── Saldo actual  ←─ sumatoria neta de todos sus comprobantes
  │
  └── Comprobantes (cuenta corriente cronológica)
        │
        ├── TipoComprobante: "001"=Cobros y pagos / "002"=Retiros efectivo /
        │                     "003"=Depósitos efectivo / "004"=Transferencias
        ├── signo: +1 (crédito) o -1 (débito)
        ├── importe: monto del ajuste
        └── saldo: saldo resultante después del ajuste

Relación con la cuenta recaudadora:
  Σ saldos de todas las cuentas ≤ saldo de la cuenta recaudadora del PSP

Ciclo de vida de un comprobante en una operación (ej. transferencia saliente):
  1. Bind PSP crea comprobante de DÉBITO (anticipa el descuento) → saldo baja
  2a. Éxito: queda el débito, la transferencia sale
  2b. Error: Bind PSP crea comprobante de CRÉDITO (reversa) → saldo vuelve

La entidad puede crear sus propios comprobantes para ajustes internos
(ej. débito por retiro en efectivo, crédito por promoción, cobro de servicio).
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `POST` | Crear comprobante | [endpoint_post_crear_comprobante.md](endpoint_post_crear_comprobante.md) |
| `GET` | Consultar tipos de comprobante | [endpoint_get_consultar_tipos_comprobante.md](endpoint_get_consultar_tipos_comprobante.md) |
| `POST` | Crear tipo de comprobante | [endpoint_post_crear_tipo_comprobante.md](endpoint_post_crear_tipo_comprobante.md) |
| `DEL` | Eliminar tipo de comprobante | [endpoint_delete_eliminar_tipo_comprobante.md](endpoint_delete_eliminar_tipo_comprobante.md) |
| `GET` | Consultar comprobante por ID | [endpoint_get_consultar_comprobante_id.md](endpoint_get_consultar_comprobante_id.md) |
| `GET` | Consultar comprobante por ID ext. | [endpoint_get_consultar_comprobante_id_externo.md](endpoint_get_consultar_comprobante_id_externo.md) |
| `GET` | Consultar saldo actual por ID | [endpoint_get_consultar_saldo_actual_id.md](endpoint_get_consultar_saldo_actual_id.md) |
| `GET` | Consultar saldo actual por CVU | [endpoint_get_consultar_saldo_actual_cvu.md](endpoint_get_consultar_saldo_actual_cvu.md) |
| `GET` | Consultar saldos actuales | [endpoint_get_listar_saldos_actuales.md](endpoint_get_listar_saldos_actuales.md) |
| `GET` | Consultar saldo histórico por ID | [endpoint_get_consultar_saldo_historico_id.md](endpoint_get_consultar_saldo_historico_id.md) |
| `GET` | Consultar saldo histórico por CVU | [endpoint_get_consultar_saldo_historico_cvu.md](endpoint_get_consultar_saldo_historico_cvu.md) |
| `GET` | Consultar saldos históricos | [endpoint_get_listar_saldos_historicos.md](endpoint_get_listar_saldos_historicos.md) |
