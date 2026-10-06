---
id: 2026-10-05_adquirencia_decision_prohibir_swagger_abm_usar_apim
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones', 2026-10-05 15:01, minuta Gemini (compartida, mnadalin)"
producto: adquirencia
tema: decisión de evitar el uso de Swagger para operaciones ABM y pasar a API Management (APIM) con credenciales individuales — auditoría de ABM queda baja prioridad
tipo: decision
destino_propuesto: 3_recursos/detalle_productos/adquirencia/configuracion_de_entidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Gap de auditoría planteado (Gonzalo Rivera, Luciana Rudaz, reunión "Weekly - Producto / Operaciones", 2026-10-05):** falta trazabilidad de bajas, altas y modificaciones de cuentas, CBU corta o inserciones de saldo realizadas mediante **Swagger** — esto genera observaciones de auditoría interna.

**Decisión (Pablo Gomes):** el uso de Swagger para estas operaciones debe **evitarse**; las operaciones deben hacerse desde la interfaz de **API Management (APIM)** con credenciales individuales por operador (en vez de la vía directa de Swagger, que no deja registro atribuible a una persona). La auditoría de ABM vía log dedicado queda con **baja prioridad** para el equipo — no se la trata como urgente pese al hallazgo de auditoría.

**Nota de contexto:** `configuracion_de_entidades.md` ya documenta el patrón de "crear entidad vía Swagger con body completo" como procedimiento manual existente — este ítem agrega la decisión explícita de discontinuar esa vía para ABM operativo (altas/bajas/modificaciones de cuenta, CBU corta, saldo) en favor de APIM, no necesariamente para toda operación vía Swagger documentada en ese archivo.
