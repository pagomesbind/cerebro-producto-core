---
id: 2026-09-01_agente_cobros_y_pagos_oportunidad_consulta_cbu_cvu_alias
pm: pablo
fecha_captura: 2026-09-01
fuente: "Análisis comparativo entre wiki/3_recursos/detalle_productos/wallet/apis_expuestas/cvu/ y wiki/3_recursos/detalle_productos/agente_cobros_y_pagos/apis_expuestas/, en el marco del relevamiento de API BANK (Banco Industrial)"
producto: agente_cobros_y_pagos
tema: Agente de Cobros y Pagos no expone GET por CBU/CVU/alias a sus entidades — oportunidad de paridad de funcionalidad con Wallet
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: ee14a4b68342c2020cd4dfbc817cd6bc347de70d
---

## Hallazgo

Tanto **Wallet** como **Agente de Cobros y Pagos** de Bind PSP consumen internamente la misma funcionalidad de base de API BANK (Banco Industrial): el endpoint `GET /accounts/cbu/:cbu_cvu` (y su equivalente por alias, `GET /accounts/alias/:alias`) del grupo `Cuenta` de API BANK, que permite consultar los datos de titularidad de una cuenta a partir de su CBU, CVU o alias (ver `2026-09-01_arquitectura_api_bank_cuenta`, endpoints `ConsultaCuentaCBU` / `ConsultaCuentaAlias`).

**Wallet expone esta funcionalidad hacia sus propias organizaciones/clientes**, documentada públicamente en `wiki/3_recursos/detalle_productos/wallet/apis_expuestas/cvu/endpoint_get_consultar_por_cbu_cvu_alias.md` (`GET .../CuentaCVUByCbuCvuOrAlias?cbuOrCvu=&alias=`) — cualquier organización de Wallet puede consultar los datos de titularidad de una cuenta CBU/CVU externa antes de operar contra ella (por ejemplo, para validar el destinatario de una transferencia antes de enviarla).

**Agente de Cobros y Pagos no tiene un endpoint público equivalente.** Se revisó el índice completo de APIs públicas de Agente de Cobros y Pagos (`wiki/3_recursos/detalle_productos/agente_cobros_y_pagos/apis_expuestas/`, subcarpetas `transferencias_cvu/`, `transferencias_entrantes_cvu/` y `operar_cbu/`) y no existe ningún endpoint de tipo "consultar cuenta/titular por CBU, CVU o alias" — los endpoints disponibles son operativos (crear CVU, asignar alias, crear/consultar/eliminar transferencias, consultar saldo, conciliar transferencia) pero ninguno permite a un collector validar de antemano los datos de titularidad de una cuenta destino antes de transferir.

## Por qué importa

Un collector de Agente de Cobros y Pagos que quiera pagarle a un proveedor o hacer una devolución por CBU/CVU/alias no tiene forma, hoy, de confirmar desde la propia API de Bind a nombre de quién está esa cuenta antes de ejecutar la transferencia — a diferencia de una organización de Wallet, que sí puede hacer esa validación previa. Esto es una asimetría de funcionalidad entre dos productos que consumen la misma capacidad de base (API BANK), no una limitación técnica del banco.

## Propuesta

Evaluar exponer en Agente de Cobros y Pagos un endpoint equivalente a `consultar-cbu-cvu-por-cbu-cvu-o-alias` de Wallet, reutilizando la misma integración interna contra API BANK (`ConsultaCuentaCBU`/`ConsultaCuentaAlias`) que ya usa Wallet — sería una funcionalidad nueva ofrecida a los collectors de Agente de Cobros y Pagos, con esfuerzo de desarrollo relativamente acotado dado que la integración de base ya existe y está probada en Wallet.

## Fuente y alcance de la verificación

Verificación hecha revisando el contenido completo de `wiki/3_recursos/detalle_productos/agente_cobros_y_pagos/` (incluyendo `apis_expuestas/index.md` y las 3 subcarpetas de endpoints documentados) — no se encontró el endpoint buscado. Esto confirma la sospecha inicial del PM que originó este relevamiento.
