---
id: 2026-09-11_transversal_conocimiento_estado_ingesta_documentacion_coelsa
pm: pablo
fecha_captura: 2026-09-11
fuente: "Ingesta manual completa de https://documentacion.coelsa.com.ar/ (DEBIN, Comercio, CVU, Prevent, CPF), vía VPN habilitada del usuario. Consultado 2026-09-11."
producto: "transversal"
tema: Registro de la primera ingesta completa de documentación de Coelsa — baseline de changelog para futuras ingestas incrementales
tipo: conocimiento
destino_propuesto: wiki/3_recursos/arquitectura_sistema/integraciones_externas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Propósito de este item

El usuario pidió explícitamente dejar registrado el estado de esta ingesta para que **una futura sesión no tenga que releer toda la documentación de Coelsa de cero** — solo buscar qué cambió desde acá. Este item es ese punto de referencia.

## Alcance cubierto (2026-09-11)

Se leyó de punta a punta la documentación pública de Coelsa para **5 de los 9 productos** que expone el sitio:

| Producto Coelsa | Cubierto | Contexto_vivo generado |
|---|---|---|
| DEBIN (incluye PAGO QR/PCT, Interchange, CVU-Comercios embebido) | ✅ Completo | `2026-09-11_wallet_coelsa_debin_api_referencia.md`, `2026-09-11_adquirencia_coelsa_qr_catalogo_apis_y_codigos_error.md` |
| Comercio (ABM unificado CBU+CVU) | ✅ Completo (sitio corto) | `2026-09-11_adquirencia_coelsa_nueva_api_comercio_unificada.md` |
| CVU | ✅ Completo | `2026-09-11_wallet_coelsa_cvu_api_referencia.md` |
| Prevent | ✅ Completo (sitio corto) | `2026-09-11_cumplimiento_coelsa_prevent_scoring_y_on_hold.md` |
| CPF | ✅ Completo (sitio corto) | `2026-09-11_cumplimiento_coelsa_cpf_central_prevencion_fraude.md` |
| ECHEQ, FCEM, CEDIP, Alias CBU | ❌ Excluidos a pedido explícito del usuario (2026-09-11) — no ingestados, quedan pendientes de una ronda futura si Bind los llega a necesitar. | — |

## Cómo detectar cambios en una futura ingesta (sin releer todo)

- **Solo el sitio DEBIN tiene página de "Novedades"** (`https://documentacion.coelsa.com.ar/debin/#novedades`) — es un changelog cronológico mantenido por Coelsa. **Último ítem conocido a esta ingesta: 2026-Septiembre** (actualización del Manual de Servicio Procesamiento CCT — endpoints de plan de pagos/avisos/cuentas de comisiones/consultas por ID — y agregado del impuesto SIRTAC al Manual de Pagos con Transferencia PCT). Una futura sesión solo necesita abrir esa página y leer las entradas **posteriores** a "2026-Septiembre" para saber qué cambió.
- **Comercio, CVU, Prevent y CPF no tienen página de Novedades propia.** Para esos 4, la única forma de detectar cambios es comparar el contenido completo contra lo ya documentado en los items de contexto_vivo listados arriba (una vez mergeados, contra los archivos finales en `detalle_productos/` y `cumplimiento_normativo/`). Ninguno de los 4 es un sitio grande (entre 20K y 40K caracteres de texto), así que una re-lectura completa puntual no es costosa si se sospecha un cambio.
- Método de extracción usado (útil documentarlo para la próxima vez): estos sitios son SPA tipo Slate/ReadMe de una sola página larga por producto; `document.querySelector('.content')` contiene todo el texto, pero los bloques `<pre>` de ejemplos `curl` incluyen JWT de ejemplo larguísimos que conviene filtrar (regla usada: reemplazar cualquier token sin espacios de más de 80 caracteres) para no gastar contexto en relleno. Los tabs de código por lenguaje (`tab-java`/`tab-javascript`/`tab-csharp`) no aportan al `.innerText` visible — alcanza con la versión `tab-shell` (cURL).

## Confirmaciones cruzadas útiles de esta ingesta

- El reparto de Interchange (25/50/75 según tamaño de comercio) y el mecanismo de tramo gratuito documentados en la especificación técnica interna que ya tenía `adquirencia/mecanica_qr_coelsa.md` (Parte 4) **coinciden exactamente** con lo que expone el sitio público de Coelsa — sin contradicciones.
- Se confirmó que la API `apiCVU/Comercio` (documentada en `mecanica_qr_coelsa.md` Parte 4) y la nueva API standalone `/comercio/` de Coelsa son **dos superficies distintas** (la nueva no exige CVU previo) — ver item dedicado.

## Confianza

Alta. Este item es puramente de proceso/trazabilidad, no de contenido de producto.
