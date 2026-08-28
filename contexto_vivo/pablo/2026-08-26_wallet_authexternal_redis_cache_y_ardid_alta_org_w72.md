---
id: 2026-08-26_wallet_authexternal_redis_cache_y_ardid_alta_org_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), tickets WS-1461, WS-1447"
producto: wallet
tema: AuthExternal V2 — bug de cache Redis nunca funcional; alta de organización — path incorrecto hacia Ardid Product
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

Dos hallazgos del tramo W72 que amplían §7 ("Historial de altas de organización y migraciones") con la misma lógica de casos reales ya usada ahí.

**1. AuthExternal V2 — la cache Redis de credenciales de servicio nunca funcionó ([WS-1461](https://bindpsp.atlassian.net/browse/WS-1461), Epic WS-564, detectado 2026-08-06 analizando logs de PROD tras el pasaje de etapa 2):**

- Síntoma: en cada `gettoken`, error `JsonReaderException` al leer de Redis (`Error accessing cache for {CacheKey}, falling back to database`). **No era un incidente** — la excepción se capturaba y el flujo caía a base de datos, el token se seguía emitiendo bien, sin impacto funcional. Pero la cache estaba al **0% de efectividad**: nunca funcionó desde que existe.
- Causa raíz: `ServiceAuthentication.Parameters` es una interfaz (`IServiceAuthenticationParameters`, `private set`) que se serializa a Redis como objeto, pero el único constructor público de la clase recibe un `string? parameters` — al releer, Newtonsoft intenta matchear un objeto contra un string y tira la excepción. De las 45 credenciales de PROD, 33 tenían `parameters` poblado (cache siempre rota) y 12 lo tenían vacío (no fallaban, pero sufrían corrupción silenciosa del Id).
- El defecto afectaba **todos los ambientes**, no solo PROD (el registro de cache no es condicional por entorno).
- Fix: se cachea un DTO plano con `Parameters` como string JSON (misma forma que la columna `NVARCHAR(MAX)`), reusando el serializador de `ServiceAuthParametersValueConverter`; la rehidratación va por discriminador interno, no por el enum del ctor. Se prohibió explícitamente usar `TypeNameHandling` (CWE-502/RCE sobre un Redis compartido).
- **Segundo defecto encontrado al validar el fix contra Redis real:** el TTL de la cache estaba corrido por zona horaria (restaba el componente UTC de un `DateTimeOffset` contra `DateTime.Now` local) — en UTC-3 los 10 minutos configurados se convertían en ~3h10m (∼19x). Era inocuo mientras la cache estaba rota; el fix de arriba lo activaba, así que se corrigió en el mismo commit.
- Deuda técnica reconocida (no introducida por este fix, preexistente): los tests de integración no corren contra la implementación real de `ICacheService` (usan `NonMemoryCache`), por lo que esta familia de bugs de round-trip contra Redis es ciega a CI — recomendación de cerrar con Testcontainers + Redis real, evaluada por el Lead Técnico y descartada por ahora (queda como prueba local documentada).
- Verificado en STAGING el 2026-08-11, validado en PROD por Andrea Orsini el 2026-08-14 (regresión de los flujos Poincenot/Lirium/PIX/Debin/Wallet.Bind/Totalizadores/Mastercard).

**2. Alta de organización — Ardid Product respondía 404 por prefijo de path incorrecto ([WS-1447](https://bindpsp.atlassian.net/browse/WS-1447), Epic WS-54, W 72):**

- Al dar de alta una organización, los pasos internos de alta de `ProductType`/`ProductCategory`/`Product` en Ardid devolvían 404 porque `Wallet.Cuenta.Api/appsettings.Production.json` tenía el prefijo `/apiproduct/` en vez de `/apiproductmanagement/` (el gateway real en `api.bindpagos.com.ar` solo expone el segundo). Alineado con el patrón `/api{dominio}management/` que ya usaban los endpoints de client en el mismo bloque `MsArdid`.
- Solo config de PRODUCCIÓN — los demás 5 ambientes (STG/FintexaSTG/etc.) usan otro gateway (`/ardid-product/`) y no estaban afectados; por eso no era reproducible fuera de prod.
- Validado por Andrea Orsini el 2026-08-14: regresión de alta de organización, alta de cuenta con CUIT existente/inexistente en Ardid, todas OK.

**Al mergear:** agregar ambos como nuevas viñetas de §7, mismo formato que las entradas W71 ya existentes (HAPSA, PAFX, etc.) — no reemplazan nada, son hallazgos nuevos del mismo tramo de infraestructura/altas.
