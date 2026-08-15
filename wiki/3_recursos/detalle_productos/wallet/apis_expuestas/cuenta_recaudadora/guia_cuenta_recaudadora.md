# Guía — ¿Cómo operar la cuenta recaudadora?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-cuentarecaudadora
> Producto: Wallet — Cuenta recaudadora

## Descripción

La entidad cuenta con algunas herramientas que le permiten automatizar tareas operativas sobre la conciliación y administración de la cuenta recaudadora.

En todo momento puede consultar el saldo total actual de la cuenta recaudadora asociada y también cuenta con la funcionalidad de debin recurrente para automatizar la realización de debin y fondear la cuenta recaudadora cuando sea necesario.

La entidad debe asegurar que al final del día el saldo de la cuenta recaudadora sea mayor o igual que la sumatoria de los saldos de todas las cuentas corrientes.

## Flujo — Administración de la cuenta recaudadora

```
MONITOREO (en cualquier momento):
  GET /saldo-recaudadora → saldo total disponible en la cuenta recaudadora del PSP

REGLA OPERATIVA DIARIA:
  Al cierre de cada día:
  Σ saldos de todas las cuentas corrientes ≤ saldo de la cuenta recaudadora

FONDEO VÍA DEBIN (cuando el saldo es insuficiente):
  1. POST /fondear-debin
     → Inicia un DEBIN recurrente desde una cuenta externa
     → Requiere suscripción DEBIN activa entre la recaudadora y la cuenta origen
     → Fondos acreditados en la cuenta recaudadora cuando el DEBIN se aprueba

  2. GET /debin-fondeo/{id} → monitorear estado del DEBIN de fondeo
     → Estados: PENDING / IN_PROGRESS / COMPLETED / FAILED
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `GET` | Consultar saldo de la cuenta recaudadora | [endpoint_get_consultar_saldo_recaudadora.md](endpoint_get_consultar_saldo_recaudadora.md) |
| `POST` | Fondear cuenta recaudadora con debin | [endpoint_post_fondear_debin.md](endpoint_post_fondear_debin.md) |
| `GET` | Consultar debin de fondeo de cuenta recaudadora | [endpoint_get_consultar_debin.md](endpoint_get_consultar_debin.md) |
