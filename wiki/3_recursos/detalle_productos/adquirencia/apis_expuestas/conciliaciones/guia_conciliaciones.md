# Guía: Conciliaciones (CORE) — Adquirencia

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-conciliarcobro
> Producto: Adquirencia / Soluciones de Cobro

---

## Descripción

El sistema ofrece mecanismos de conciliación y control. Las organizaciones pueden realizar monitoreo en tiempo real mediante consultas de listado de transacciones vía API. Los archivos batch diarios que contienen toda la actividad operacional están disponibles en días hábiles y pueden recuperarse mediante API, permitiendo revisión de operaciones aprobadas, pagos programados y devoluciones procesadas ese día.

La organización es responsable de asegurar la alineación entre sus sistemas internos y la plataforma de Bind PSP.

## Flujo — Conciliación de cobros

```
OPCIÓN 1 — Control en línea (en cualquier momento):
  GET /consultar-transacciones (filtros: comercio, caja, fecha, estado, canal)
  → Devuelve listado de transacciones en tiempo real

OPCIÓN 2 — Archivos batch diarios (conciliación administrativa):

  Cada día hábil Bind PSP genera 3 archivos:
  ┌─────────────────────┬────────────────────────────────────────────┐
  │ Archivo             │ Contenido                                  │
  ├─────────────────────┼────────────────────────────────────────────┤
  │ Rendición           │ Todas las operaciones aprobadas del día    │
  │ Liquidación         │ Cronograma de pagos a acreditar ese día    │
  │ Devoluciones        │ Todas las devoluciones procesadas ese día  │
  └─────────────────────┴────────────────────────────────────────────┘

  Descarga:
  GET /consultar-archivos-cobro?fecha=DDMMAA → listar archivos disponibles
  GET /descargar-archivo/{id}               → descargar archivo específico
```

## Recursos Disponibles

### Controles Online
Consultas en tiempo real de listados de transacciones vía API.

### Conciliación Administrativa
Archivos batch diarios (días hábiles) que contienen:
- Todas las operaciones aprobadas
- Cronogramas de liquidación
- Registros de devoluciones

## Endpoints Disponibles (Slugs Reales del Portal)

| Slug Real | Método | Operación |
|-----------|--------|-----------|
| `./batch-consultararchivos` | GET | Consultar archivos Cobro |
| `./batch-descargararchivo` | GET | Descargar archivo Cobro |
| `./guia-archivobatchcobrorendicion` | GUÍA | Diseño de archivo de rendición |
| `./guia-archivobatchcobroliquidacion` | GUÍA | Diseño de archivo de liquidación |
| `./guia-archivobatchcobrodevoluciones` | GUÍA | Diseño de archivo de devoluciones |
