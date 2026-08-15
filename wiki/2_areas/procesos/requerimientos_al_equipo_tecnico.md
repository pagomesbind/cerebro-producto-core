# Proceso para Hacer Requerimientos al Equipo Técnico

> Contenido completo transcrito desde `wiki/3_recursos/conocimiento_interno/proceso/proceso_para_hacer_requerimientos_al_equipo_tecnico.md` (ingesta original), reubicado desde `detalle_productos/transversal/procesos_internos.md §2` en la reestructuración PARA en cascada (2026-08-12).

# Objetivo
El objetivo de este nuevo proceso es mejorar la atención a pedidos al equipo técnico de Bind PSP, ya sea para desarrollos nuevos como para solicitudes de soporte técnico.
La idea principal es que cualquier pedido sea siempre cargado el backlog sin discriminar y que luego el analista haga el relevamiento y el filtro necesario para priorizarlo y asignarlo al equipo de desarrollo de forma ordenada. Luego, será responsabilidad del project manager del equipo técnico que se complete la entrega del mismo.

# ¿De qué se trata el nuevo proceso?
Se trata de que cada equipo que tenga un requerimiento pueda autogestionar su creación en el backlog de desarrollo mediante un formulario de Jira.
Esta forma de creación permite clasificarlos y priorizarlos de forma de que el analista pueda atenderlos de forma ordenada.
Luego, el equipo técnico tendrá más orden y herramientas para priorizar y decidir de qué manera desarrollar y publicar el pedido.

# ¿Quiénes son los responsables en este proceso?
- Bind PSP
	- Analista: Analizar cada nuevo ticket asignado en el backlog, definir funcionalmente, clasificar en la Epic correspondiente, indicar la prioridad correspondiente y pasar a estado Asignado.
	- Project manager: Seguir el ticket asignado para que complete su ciclo de desarrollo correspondiente cumpliendo la prioridad indicada por el equipo de análisis.
	- Equipo interno: Crear requerimientos de nuevos desarrollo o solicitar soporte técnico mediante el formulario correspondiente.
	- Arquitectura y tecnología: Crear requerimientos de iniciativas y mejoras técnicas mediante el formulario correspondiente.
- FINTEXA:
	- Soporte: Crear requerimientos de desarrollos de fixes relacionados a incidencias productivas mediante el formulario correspondiente.

# ¿Cómo deben realizarse los requerimientos?
Dependerá del tipo de pedido y también de quién origina el pedido.

## Equipo interno de Bind PSP - Nuevo desarrollo
Cuando cualquier miembro del equipo de Bind PSP (Soporte, Integraciones, Comercial, Administración) requiera un nuevo desarrollo, deberá solicitarlo por medio de los siguientes formularios dependiendo del producto correspondiente:
- Nuevo requerimiento de desarrollo WALLET: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/229a1da1-35e8-4519-9e65-dc6eb6d7a0be?atlOrigin=eyJpIjoiYzc0NGM3YmY1ODYxNDcxYWI3Njc1MjQ1OTU4ZTc0YTYiLCJwIjoiaiJ9)
- Nuevo requerimiento de desarrollo COBRO: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/a989cdff-8654-41a0-b402-578657976be5?atlOrigin=eyJpIjoiOTFhMjIzODE0NWJkNDYyNmEyODI1ZDNkOWZmNzJhNWYiLCJwIjoiaiJ9)
- Nuevo requerimiento de desarrollo ONBOARDING: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/d4680235-7f63-40df-95c8-e415c868049c?atlOrigin=eyJpIjoiYzJmMDYxN2NiOTE4NGMzYWJmN2RlYmJiOGFhYzY3MDkiLCJwIjoiaiJ9)

## Equipo interno de Bind PSP - Pedido de soporte de análisis
Cuando cualquier miembro del equipo de Bind PSP (Soporte, Integraciones, Comercial, Administración) requiera resolver una duda técnica, la creación de documentación, la ejecución de una prueba u otra tarea de análisis, deberá solicitarlo por medio de los siguientes formularios dependiendo del producto correspondiente:
- Nuevo pedido de soporte de análisis WALLET: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/ac1eb781-0d88-475c-beb4-36fad024585f?atlOrigin=eyJpIjoiNmFiMjZjYjdhYzFmNDkxMTg1M2JkNDU2Yzk2YWNmZTMiLCJwIjoiaiJ9)
- Nuevo pedido de soporte de análisis COBRO: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/44efe632-96b0-4d6f-86ea-aca73ead315d?atlOrigin=eyJpIjoiMjRjYmRiOGIyNThlNDU3ZmIwZDVlMjU3NjU2ZDAzNDkiLCJwIjoiaiJ9)
- Nuevo pedido de soporte de análisis ONBOARDING: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/d4680235-7f63-40df-95c8-e415c868049c?atlOrigin=eyJpIjoiNTgyNzE3YmFiN2NhNGRkZGE2YTc0MDc2NjYyYjcxODQiLCJwIjoiaiJ9)

## Equipo de soporte de FINTEXA
Cuando a partir de un ticket de soporte de Fintexa se identifica y define un desarrollo necesario para arreglar un incidente o para evitar que algo vuelva a pasar, deberá solicitarlo por medio de los siguientes formularios dependiendo del producto correspondiente:
- Fix por error en producción WALLET: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/cb136c86-3ab9-46fa-94e2-f7f40596367e?atlOrigin=eyJpIjoiZjJmYjk2ZDBkNjYyNDI2NzhiZmYwNmI4ZjFjMmU1NTkiLCJwIjoiaiJ9)
- Fix por error en producción COBRO: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/5317635c-d8ed-4532-8409-68f961e8ee18?atlOrigin=eyJpIjoiZGE2ZTExMzUyYjZlNGJkMWEzMTM3MmI1YWVmOTA3MjAiLCJwIjoiaiJ9)
- Fix por error en producción ONBOARDING: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/602f9a81-79b5-4db1-9be0-8c1f18d0087f?atlOrigin=eyJpIjoiNTFiZGUzMmU4OTliNDMzNmJmZmQxZmJmOTcxZTcxNDAiLCJwIjoiaiJ9)

## Equipo técnico de FINTEXA
Cuando el equipo técnico de Fintexa descubre un cambio que considera necesario o favorable hacer, deberá solicitarlo por medio de los siguientes formularios dependiendo del producto correspondiente:
- Iniciativa técnica de desarrollo WALLET: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/b98ff3ee-5cc0-44dd-aead-22ebf4eec9c2?atlOrigin=eyJpIjoiYWVjYTkxYTQ1ZDliNDZmYzg2MmFjMjQ5ZDk0MTJlODAiLCJwIjoiaiJ9)
- Iniciativa técnica de desarrollo COBRO: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/3a6bc3b9-fa3a-4039-8f52-be8b358074db?atlOrigin=eyJpIjoiYzc3NDU5ZTI2MThiNDZlMzhkNzgyNzhhYjY5OTA2ODciLCJwIjoiaiJ9)

## Equipo de arquitectura
Cuando se apruebe la viabilidad de una iniciativa técnica proveniente del comité de arquitectura y se decida desarrollarla, deberá solicitarlo por medio de los siguientes formularios dependiendo del producto correspondiente:
- Iniciativa del COE WALLET: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/cc269eaf-0f22-41e1-91d1-76579856f96d?atlOrigin=eyJpIjoiZDRkYmRhYjlhZDQxNGFlYmIzMDU3Y2M5MGY1ZDZhMTQiLCJwIjoiaiJ9)
- Iniciativa del COE COBRO: [Jira](https://bindpsp.atlassian.net/jira/software/c/form/eed9bd9f-6d3e-4dca-9008-9ffe10a38839?atlOrigin=eyJpIjoiZjE1MDg3OWZhMGU4NDc1YmFkMTk3ZDEwNThjOGQ1NjkiLCJwIjoiaiJ9)

## Ver también
- [publicaciones_mensuales.md](publicaciones_mensuales.md) — ciclo mensual sobre el que se planifica lo cargado por este proceso.
- [gestion_jira.md](gestion_jira.md) — espacios y tipos de ticket que resultan de este proceso.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/procesos_internos.md §2` (reestructuración PARA en cascada). Contenido sin cambios.*
