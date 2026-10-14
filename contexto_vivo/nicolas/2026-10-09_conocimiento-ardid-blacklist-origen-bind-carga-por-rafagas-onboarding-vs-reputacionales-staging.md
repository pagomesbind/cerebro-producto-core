---
id: 2026-10-09_conocimiento-ardid-blacklist-origen-bind-carga-por-rafagas-onboarding-vs-reputacionales-staging
pm: nicolas
fecha_captura: 2026-10-09
fuente: "Mail 'RE: Consultas: integración con Akurtech (Ardid) y circuito de fondeo de wallet' — Samira Aouada (Pentass) 2026-10-08"
producto: ardid
tema: Ardid (Akurtech) — de dónde sale la blacklist, cómo se carga desde la herramienta, blacklists compartidas entre clientes con aprobación, reglas de Onboarding vs. reputacionales, simulaciones y staging
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/blacklist_whitelist_rafagas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

Respuestas de Pentass (proveedor de Ardid/Akurtech) a las consultas de Credicuotas. Aclaran cosas que el archivo canon no explica (ese archivo sale del manual `Akurtech 6 - Blacklist - Ráfagas.pdf`). Confianza media: es la respuesta del proveedor por mail, sin documento.

- **Origen de la blacklist de Akurtech.** Se alimenta con información que manda BIND: casos de transferencias pull, eventos de SPF, denuncias de otras entidades y fraudes con denuncia registrada. La blacklist de Akurtech y las de BIND no son independientes: la primera se nutre de las segundas.
- **Carga desde la herramienta.** Fuera de lo que incorpora BIND, el único mecanismo disponible hoy para sumar registros a la blacklist desde Ardid es una **ráfaga con la acción "Agregar a blacklist"**. No se mencionó carga manual ni por otro tipo de regla.
- **Blacklists compartidas.** Las blacklists del grupo BIND se pueden usar dentro de Akurtech. También se puede incorporar información que viene de **otros clientes** de Akurtech. Los datos nuevos que llegan así aparecen en el dashboard con estado **"Pendiente de aprobación"** y alguien los tiene que validar.
- **Reglas de Onboarding vs. reglas reputacionales.** Las dos consultan blacklists. La diferencia es **cuándo actúan**:
  - Onboarding: solo durante el alta de la cuenta. Contrastan los datos del usuario contra los registros de las blacklists.
  - Reputacionales: durante la operatoria transaccional (por ejemplo, al hacer una transferencia).
  - Controlar contra blacklists las transacciones posteriores depende de qué datos lleguen en cada evento. Habría que analizar qué datos se pueden enviar en cada transacción.
- **Pruebas antes de activar reglas.** Se pueden probar reglas con **simulaciones**, disponibles en la versión que hoy está en **staging**. En staging las reglas no afectan transacciones productivas: sirve para probar configuraciones y aprender la herramienta antes de pasarlas a producción.
- **Movimientos internos entre cuentas.** Según Pentass, las restricciones dependen del **tipo de comprobante** del movimiento: no todos tienen el mismo tratamiento ni las mismas funcionalidades. No dieron montos ni cantidades.

**Sin resolver en el mail:** qué agrega la blacklist de Akurtech frente a consumir directamente la blacklist de BIND (lo valida Rocío Revelli para la próxima reunión), y si el límite diario de transferencias hacia Tapi aplica también a los movimientos internos (Pentass pide más contexto del flujo).

> Fuente: Mail "RE: Consultas: integración con Akurtech (Ardid) y circuito de fondeo de wallet" — Samira Aouada (Pentass), 2026-10-08.
