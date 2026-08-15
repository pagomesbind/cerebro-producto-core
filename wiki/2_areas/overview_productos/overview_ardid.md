# Ardid — Overview de Producto

> Fuente: `raw/Product Overview_Ardid.docx` (ingesta Fase 1, 2026-07-02). Área de negocio: [Fraude](../overview_empresa/overview_equipo.md) (responsable: Rocío Revelli). Provisto por: Pentass.

## Qué es

Software de **monitoreo transaccional** adquirido a un desarrollador tercerizado (**Pentass**) como producto de paquete cerrado, aunque hosteado en la nube propia de Bind PSP.

> ⚠️ **Nota de nomenclatura (2026-07-02):** el proveedor rebrandeó el software de **"Ardid" a "Akurtech"** a partir de la versión 1.18 (mayo 2026) — es el mismo producto y el mismo proveedor bajo dos nombres comerciales en distintos momentos, confirmado por el usuario y corroborado técnicamente (el token de autenticación de las APIs sigue usando `"aud": "Ardid"` como audiencia interna). El manual técnico completo, catálogo de APIs y taxonomía de reglas quedaron documentados en [3_recursos/detalle_productos/ardid/](../../3_recursos/detalle_productos/ardid/index.md).

- Expone **APIs** para integración y consumo por terceros: permite analizar transferencias y transacciones, respondiendo en línea el resultado del monitoreo según reglas y restricciones configurables por el usuario.
- Cuenta con una **aplicación web** para gestionar esas configuraciones.
- **Soporta multi-entidad.**
- Requiere que, previamente, se creen entidad, clientes, cuentas, productos, etc., para poder analizar transferencias sobre ellos.

## Uso interno y externo

- **Interno**: hace sinergia con **Adquirencia** y **Wallet**, que están integrados a Ardid para analizar transacciones de tarjeta y operaciones de wallet respectivamente. Ver [adquirencia_overview.md](overview_adquirencia.md) y [wallet_overview.md](overview_wallet.md).
- **Externo**: Bind PSP también ofrece Ardid como producto a entidades externas, que se integran directamente y lo consumen alojadas en el mismo tenant que las entidades propias de Bind PSP, con credenciales de API especiales.

---
*Última actualización: 2026-07-02 — Agregada nota de rebranding Ardid→Akurtech y enlace al manual técnico completo en `wiki/3_recursos/ardid_manual_tecnico/`.*
