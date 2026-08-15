# Guía — Diseño de archivo cuadratura

> Fuente: https://psp.bind.com.ar/developers/apis/guia-archivowalletcuadratura
> Producto: Wallet — Consultas y conciliaciones

> **Nota:** Esta guía aún no tiene contenido publicado en el portal (página en blanco al 2026-07-01).

## Flujo — Propósito del archivo cuadratura

```
Propósito: documento diario que permite verificar la integridad del saldo
           de la cuenta recaudadora frente a los saldos de las cuentas corrientes.

Publicación: cada día hábil, junto con los demás archivos batch.
  GET /consultar-archivos-wallet?fecha=DDMMAA → listar archivos del día
  GET /descargar-archivo/{id} → descargar archivo de cuadratura

Uso típico:
  El archivo de cuadratura es el instrumento formal para que la entidad
  verifique que la suma de saldos de todas sus cuentas corrientes
  no excede el saldo de la cuenta recaudadora al cierre del día.

  Si la cuadratura detecta inconsistencia → contactar a soporte de Bind PSP.
```
