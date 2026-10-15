---
id: 2026-10-15_conocimiento-ardid-roadmap-akurtech-120-coelsa-cuit-121-modulo-360-prevent-marzo
pm: nicolas
fecha_captura: 2026-10-15
fuente: "Reunión \"Ardid+BindPSP: Roadmap\" (2026-10-14), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: ardid
tema: Roadmap de Ardid con el proveedor — 1.20 con integración Coelsa + validación de CUIT (diciembre) y control de transferencias a una misma cuenta; 1.21 con módulo 360; Coelsa Prevent en Ardid para la normativa de marzo; pendientes de desbloqueo por evento y bloqueo masivo de tarjetas por hash
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/historico/historial_versiones.md
tipo_destino: actualizar
contradice: "no — complementa. El canon describe la 1.20 como \"reglas interentidades\" (roadmap Pentass, 2026-09-21). Este item le suma contenido a la 1.20; no dice si las reglas interentidades siguen en esa versión"
confianza: media
estado: en_cola
---

**Roadmap acordado con el proveedor de Ardid (reunión "Ardid+BindPSP: Roadmap", 2026-10-14).** La minuta escribe las versiones como "119", "120" y "121". Se interpretan como 1.19, 1.20 y 1.21, la numeración del canon.

| Versión | Contenido | Fecha |
|---|---|---|
| **1.19** (hoy en pruebas) | Trae **controles de comercio**. Nicolás Colón tiene que evaluar si cubren lo que necesita Bind (T-132). | — |
| **1.20** | **Integración con Coelsa** y **validación de CUIT**. Lorena Macedo suma además un **control de cantidad de transferencias a una misma cuenta**. | Diciembre 2026 |
| **1.21** | **Módulo 360:** consulta centralizada de transferencias y pagos. | Sin fecha |
| Sin versión asignada | **Coelsa Prevent en Ardid**, para cumplir la normativa vigente. | Marzo (2027, se infiere) |

**Temas abiertos para definir entre las dos partes:**
- **Desbloqueo de cuentas por evento.** Revisar un evento web (webhook) que avise cuando una cuenta se desbloquea desde la plataforma de Ardid. Es lo que pide la oportunidad `2026-10-08_oportunidad-sincronizar-desbloqueo-ardid-habilita-cuenta-wallet` (reclamo de COTO). El tema ya está en la agenda con el proveedor.
- **Bloqueo masivo de tarjetas por identificador hash.** Faltan los detalles técnicos. Tiene relación directa con PRD-248 (`ardid_desconocimientos`): hoy Fraude carga los desconocimientos a mano en el front de Ardid.

**Entregables pendientes del proveedor (Lorena Macedo):** prototipos de la integración con Coelsa, hoja de ruta actualizada con sus tickets y documentación funcional de la API de "alcance". El resumen no aclara a qué funcionalidad se refiere "alcance".

**Cruce con el canon y con otros items:**
- El item `2026-10-14_conocimiento-cumplimiento-roadmap-compliance-plazos-cpf-prevent-y-onboarding-saturado` registraba que había plazos para Coelsa Prevent, pero sin fecha. Este item da el primer dato: **marzo**, vía Ardid.
- "Validación de CUIT" e "integración con Coelsa" pueden ser la CPF o Prevent (`3_recursos/cumplimiento_normativo/`). El resumen no lo aclara.

> Fuente: Reunión "Ardid+BindPSP: Roadmap" (2026-10-14), resumen del mail de Gemini.
