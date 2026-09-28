---
id: 2026-09-28_transversal_iniciativa_conciliacion_agente_cobros_pagos_nico_colon
pm: pablo
fecha_captura: 2026-09-28
fuente: "Reunión de revisión de impacto (Gonzalo Rivera, Mariana Nadalin) sobre la migración al modelo desacoplado del proveedor bancario — discovery de resiliencia_api_bank/, grabación cortada, resumen reconstruido por el PM"
producto: agente_cobros_y_pagos
tema: Falta un proyecto de conciliación automática de transferencias entrantes con Coelsa para Agente de Cobros y Pagos — hoy solo está en marcha para Wallet
tipo: iniciativa
proyecto: resiliencia_api_bank (origen del pedido) — nuevo proyecto a levantar del lado de Nicolás Colón, sin slug propio todavía
pm_destino: Nicolás Colón
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

## Novedad

En el proyecto `resiliencia_api_bank/` (Pablo Gomes), al revisar el impacto de migrar cuentas al modelo desacoplado del proveedor bancario, se confirmó con Gonzalo Rivera (Soporte) y Mariana Nadalin (Administración y Recaudaciones) que **el proyecto de conciliación automática de transferencias entrantes con Coelsa (por organización, cada una hora) que reemplaza el reporte horario que se pierde al migrar solo cubre Wallet** — está en desarrollo, estimado noviembre/diciembre de 2026.

**Agente de Cobros y Pagos no tiene ningún proyecto equivalente, ni siquiera levantado.** Cualquier collector de ese producto que hoy tenga conciliación intradiaria activa y se migre al modelo desacoplado quedaría sin ninguna contingencia automática para reemplazar lo que pierde — a diferencia de Wallet, que al menos tiene el proyecto en curso con fecha estimada.

## Por qué es una iniciativa para Nicolás Colón

Agente de Cobros y Pagos es un producto distinto de Wallet, con su propio camino interno (confirmado en el mismo discovery: no comparte el flujo de conciliación de Wallet). Levantar y priorizar este proyecto es una decisión de producto que le corresponde a quien lidera esa área, no a Pablo Gomes. Mientras no exista, ningún collector con conciliación intradiaria activa debería migrarse al modelo desacoplado — los que no la tienen hoy pueden migrar sin este bloqueo.

**Corrección (2026-09-28):** el proyecto equivalente para Wallet (el que reemplaza el reporte horario que se pierde al migrar, estimado noviembre/diciembre de 2026) **también es de Nicolás Colón** — se había registrado por error como de Gonzalo Rivera, el propio PM lo corrigió. Esto refuerza que Nicolás Colón es el dueño natural de este segundo proyecto para Agente de Cobros y Pagos: ya lidera el mismo tipo de desarrollo para Wallet.
