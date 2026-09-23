---
id: 2026-09-23_conocimiento-bpg-uat-timeout-networking-western-union
pm: nicolas
fecha_captura: 2026-09-23
fuente: "Mail \"BPG <> Bind PSP | TIME OUT | Staging\" — Adriana Endzeliz (Comercial Bind PSP) con Nicolás Gut y Alejandro Piaggio (Western Union), 2026-09-22"
producto: servicios
tema: BPG UAT (Western Union/Pago Fácil) — endpoint supplier-item/lookup, set de headers y caída de networking del lado de WU resuelta en el día
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
---

**Qué pasó.** El 2026-09-22 el equipo de Bind PSP no pudo llegar al ambiente UAT de BPG (plataforma de Western Union / Pago Fácil) desde staging: el `POST` al endpoint de consulta de items de proveedor devolvía `connect ETIMEDOUT` (timeout de conexión, no una respuesta de error de la aplicación). Adriana Endzeliz (Comercial) escaló a Western Union con el detalle del request.

**Diagnóstico y resolución.** Nicolás Gut (WU) dijo que a él le funcionaba y sumó a Alejandro Piaggio (networking WU), que confirmó que **del lado de Western Union "estuvieron todo el día con problemas"** en BPG UAT. Se normalizó ese mismo día (Adriana confirmó "Ya funciona OK" a las 17:32 ART). La causa fue una caída de networking de WU, no un error de configuración de Bind.

**Dato técnico útil para la integración (homologación BPG):**
- Endpoint UAT usado: `POST http://192.168.176.23:8105/v2/supplier-item/lookup` (IP privada — se accede por vínculo de red con WU, no por internet pública). Body de prueba: `{"ExcludeScandata": false}`.
- Headers que exige BPG: `x-retail-store-id` (ej. `8144000`), `x-workstation-id` (ej. `L44000`), `x-operator` (`BINDPS`), `x-trace-id`, `x-customer-id`, `x-datetime` (ISO con offset `-03:00`) y `appkey` (credencial — **no se transcribe acá**, vive en la configuración del equipo técnico).

**Lección operativa.** Un `ETIMEDOUT` contra BPG UAT apunta primero a la conectividad (vínculo de red / networking de WU), no al contrato de la API: el primer paso es pedirle a WU que verifique networking (contacto usado: Alejandro Piaggio), antes de revisar headers o payload.

> Fuente: Mail "BPG <> Bind PSP | TIME OUT | Staging" — Adriana Endzeliz / Nicolás Gut / Alejandro Piaggio (2026-09-22)
