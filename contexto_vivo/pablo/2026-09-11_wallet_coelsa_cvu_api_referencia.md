---
id: 2026-09-11_wallet_coelsa_cvu_api_referencia
pm: pablo
fecha_captura: 2026-09-11
fuente: "Ingesta manual de documentación pública de Coelsa (VPN habilitada) — https://documentacion.coelsa.com.ar/cvu/#introduccion — lectura completa del sitio. Consultado 2026-09-11."
producto: wallet
tema: Referencia técnica de la API CVU de Coelsa — PSP, Cuentas Recaudadoras, alta/baja/modificación de CVU, Comercios CVU, Actividad Comercial, acciones masivas SFTP y reportes
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/wallet/coelsa_cvu_api_referencia.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Por qué este documento

`wallet/apis_expuestas/cvu/guia_cvu.md` documenta la **API pública que Bind expone** a sus clientes (`POST /cvu`, `PATCH /alias`, etc. — dominio exclusivo de `/sync_web`, no tocar). Este item documenta la capa de abajo: **la API real de Coelsa** que el backend de Bind consume para que esa API pública funcione (alta/baja de PSP, cuentas recaudadoras, CVU en sí, comercios). Es contenido nuevo, no estaba capturado.

## 1. Autenticación y ambientes

Mismo esquema OAuth2 password grant que DEBIN (ver `wallet/coelsa_debin_api_referencia.md`), contra un endpoint de auth **v2** propio de CVU. Tres ambientes:

| Ambiente | Autenticación | CVU | Admin |
|---|---|---|---|
| Prueba | `testauth.coelsa.com.ar` (sin VPN) | `test-cvu.coelsa.com.ar` | `testauth.coelsa.com.ar/CoelsaAdmin` |
| Homologación | `homoalias.coelsa.com.ar/auth` (VPN + cert. cliente) | `homocvu.coelsa.com.ar` | `homoalias.coelsa.com.ar/CoelsaAdmin/` |
| Producción | `servalias-02.coelsa.com.ar/auth` (VPN + cert. cliente) | `cvu.coelsa.com.ar` (IP 138.121.76.28) | `servalias-02.coelsa.com.ar/CoelsaAdmin/` |

Componentes: WEB de Seguridad/CoelsaAdmin (igual que DEBIN), API Autenticación v2, **API CVU** (`/apiCVU/...`).

## 2. Jerarquía de entidades: PSP → Cuenta Recaudadora → CVU

Es importante entender el orden de dependencia, porque cada nivel valida al anterior:

1. **PSP** (`/apiCVU/PSP/...`): el Proveedor de Servicios de Pago habilitado por BCRA. `POST AltaPSP` (el primer banco que lo da de alta fija CUIT/Razón Social/Tipo/Nombre de Fantasía — el resto de las entidades solo pueden reutilizarlo, no modificar esos campos; sí pueden cambiar `url_psp`, propia de cada entidad). Requiere gestionar luego con Soporte Coelsa la parametrización del **tipo de PSP** según definición regulatoria BCRA. `PUT ModificacionPSP/{cuit}`, `GET ConsultaPSP/{idPsp}/{cuit}` (0 = comodín), `GET ConsultaPSP` (paginado, por banco), `GET AllPSP` (paginado, todos los PSP del ecosistema).
2. **Cuenta Recaudadora** (`/apiCVU/Cuentas/...`): la cuenta real (CBU, en ARS) donde efectivamente vive la plata de todos los CVU del PSP. `POST AltaCuenta` (requiere PSP ya activo, CBU del banco del token, CBU existente en la base de CBU de Coelsa para ese CUIT de PSP, moneda ARS). `DELETE BajaCuenta/{idPSP}/{id}`, `PUT ModificarCuenta/{idPsp}/{id}`, `GET ConsultaCuentaCbu/{idPsp}/{cbu}`, `GET ConsultaCuenta/{idPsp}/{id}`, `POST ConsultaListaCuenta/{idPsp}/{codBanco}` (por PSP, por banco o ambos — 0 como comodín).
3. **CVU** (`/apiCVU/CVU/...`): la clave virtual en sí, asociada a un PSP + cuenta recaudadora + CUIT titular.

## 3. Alta/baja/modificación de CVU — con o sin *screening*

Existen **dos métodos** de alta y de modificación:

- **`POST AltaCVU`** (y `PUT ModifCVU/{cvu}/{cuit}`) — Coelsa aplica directo, queda en estado **3200 – CVU ACTIVO**. No se envían avisos por HTTP.
- **`POST AltaCVUscr`** (y `PUT ModifCVUscr/{cvu}/{cuit}`) — variante con *screening*: Coelsa deja el CVU en **3201 – CVU EN SCREENING** y dispara `AvisoOperacionCVU` (HTTP) al endpoint del **banco débito** configurado para el PSP (dar de alta el endpoint antes, vía `POST /apiCVU/Banco/EndPoint`). El banco debe responder OK(200) indicando `3300 – CVU MODIFICADO CORRECTAMENTE` o `3400 – CVU ELIMINADO/INACTIVO`; según eso Coelsa deja el CVU Activo o lo da de baja. Al resolverse (3200 o 3400), Coelsa avisa finalmente al **PSP** con otro `AvisoOperacionCVU`. Para simular la respuesta del banco en pruebas: `POST /apiCVU/Banco/AvisoOperacionCVU`.

`DELETE BajaCVU/{cvu}/{cuit}` y `GET ConsultaCVU/{cvu}` completan el CRUD.

Body de alta típico:
```json
{
  "cvu": {
    "psp_id": 4, "cta_id": 1, "cvu": "0000004800000000001263",
    "tipo": "1", "cuit": "20333048494", "titular": "...",
    "moneda": "032", "persona_tipo": "F"
  }
}
```

## 4. Crédito en Línea (Aviso CVU en la API Bancos)

Mensaje `POST [endpoint]/AvisoCVU` a implementar en la **API Bancos** (la misma superficie documentada en `wallet/coelsa_debin_api_referencia.md §4`) — es el punto de integración entre la plataforma de Créditos en Línea de Coelsa y el banco/PSP. Se complementa con los mismos endpoints de gestión de endpoint (`PostEndPoint`/`GetEndPoint2`) y de consulta/crédito de DEBIN ya documentados en la referencia de DEBIN — **no son endpoints nuevos**, es la misma API reutilizada desde el contexto CVU.

**Adecuaciones requeridas para operar CVU** (documentadas explícitamente por Coelsa, independientemente de si la entidad opera o no con PSP propio): permitir CBU/CVU que comiencen con `"000"`, y adecuar la recepción del archivo de conciliación al **formato V3**.

## 5. Comercios CVU y Actividad Comercial

**Actividad Comercial** (`/apiCVU/Actividad`): cada actividad (rubro, código MCC de 4 dígitos según boletín CIMPRA 530) tiene, a nivel PSP, un rango mínimo/máximo de comisión. `POST Actividad` (alta), `GET Actividad/{idPsp}/{actividad_comercial}` y `GET Actividad/{idPsp}` (consulta con mín/máx), `GET Actividad` (lista), `POST Actividad/{idPsp}/{actividad_comercial}` (modificar comisión — trunca a 2 decimales, rango permitido 0.60%–0.80%).

**Comercios CVU** (`/apiCVU/Comercio/...`): réplica casi exacta de la API "Comercio" standalone (ver item separado sobre la nueva API unificada CBU+CVU) pero acotada a comercios con CVU: `POST Comercio` (alta — requiere CVU ya registrado para el CUIT, PSP activo, MCC válido con comisión dentro de rango, tramo gratuito y fecha de alta opcionales), `POST Masivo` (alta hasta 1000 ítems), `DELETE Comercio/{idpsp}/{cuit}/{actividad_comercial}`, `GET ListaComercio/{idpsp}/{cuit}`, `GET Comercio/{idpsp}/{cuit}/{actividad_comercial}`, `PUT Comercio/{idpsp}/{cuit}/{actividad_comercial}` (modificar por actividad), `PUT Comercio/{idpsp}/{cuit}` (modificar solo tramo gratuito/categoría). Catálogo de códigos de error de alta incluye, entre otros: `5000` alta OK, `5001` no dado de alta, `5002` CUIT mal formulado, `5003` categoría mal formulada, `5004` actividad mal formulada, `5005` ID PSP erróneo, `5007` comercio ya existente, `5008` PSP no registrado en la entidad, `5009` comisión mal formulada.

## 6. Acciones masivas (SFTP) y Reportes

- **Masivo CVU** (SFTP): hasta 10.000 CVU por archivo (alta/baja/modificación). Procedimiento: la entidad sube el archivo `AAAAMMDDHHMMSS.xxx` (xxx = número de entidad BCRA) a la carpeta "entrada"; sube un segundo archivo vacío `.ok` para disparar el procesamiento; Coelsa deja la respuesta (totalizadores + errores) en la carpeta "salida". Requiere que la entidad solicite un usuario SFTP dedicado a Seguridad Informática de Coelsa.
- **Masivo Comercio** (mismo canal SFTP, carpeta `BATCH_COMERCIO`, hasta 10.000 comercios por archivo, mismo patrón de `.ok` y archivo de respuesta `AAAAMMDDHHMMSSRTA.xxxx`).
- **Reporte de Tramo Gratuito**: generado mensualmente (1er día del mes) por entidad/PSP, lista los comercios con tramo gratuito activo tras 90 días desde el alta — vía SFTP o agente, carpeta sugerida `CVU/BANCOS/XXX/REPORTES/TRAMOGRATUITOVTO`.

## Anexo — payloads reales (request/response literales de la documentación)

### PSP

**Alta PSP** — `POST /apiCVU/PSP/AltaPSP`:
```json
{
  "psp": {
    "cuit": "",
    "razon_social": "PRUEBA1PSP",
    "tipo": "1",
    "nombre_fantasia": "Prueba2 AltaPSP",
    "url_psp": "https://httpstat.us/300"
  }
}
```

**Modificar PSP** — `PUT /apiCVU/PSP/ModificacionPSP/{cuit}` (solo puede cambiar `nombre_fantasia`/`url_psp` — CUIT/Razón Social/Tipo quedan fijos desde el primer alta):
```json
{
  "psp": {
    "nombre_fantasia": "MERCADO LIBRE SRL",
    "url_psp": "https://api.mercadopago.com/providers/beta/notify/coelsa/"
  }
}
```

### Cuenta Recaudadora

**Alta** — `POST /apiCVU/Cuentas/AltaCuenta`:
```json
{ "cuenta": { "psp_id": 15, "descripcion": "CUENTA EMPRESA 14", "cbu": "9993658300000000036827" } }
```

**Modificar** — `PUT /apiCVU/Cuentas/ModificarCuenta/{idPsp}/{id}`:
```json
{ "cuenta": { "descripcion": "PRUEBA  ModificarCuenta", "cbu": "9993658300000000036827" } }
```

### CVU

**Alta (sin screening)** — `POST /apiCVU/CVU/AltaCVU`:
```json
{
  "cvu": {
    "psp_id": 4, "cta_id": 1, "cvu": "0000004800000000001263",
    "tipo": "1", "cuit": "20333048494", "titular": "PRUEBA AltaCVU",
    "moneda": "032", "persona_tipo": "F"
  }
}
```
Resultado inmediato: estado `3200 – CVU ACTIVO`, sin avisos HTTP.

**Alta con screening** — `POST /apiCVU/CVU/AltaCVUscr` (mismo body, distinto endpoint). Resultado inmediato: `3201 – CVU EN SCREENING`, y Coelsa dispara `AvisoOperacionCVU` al banco débito configurado — el banco debe responder `3300 – CVU MODIFICADO CORRECTAMENTE` o `3400 – CVU ELIMINADO/INACTIVO` para que Coelsa resuelva el estado final.

**Modificar (sin screening)** — `PUT /apiCVU/CVU/ModifCVU/{cvu}/{cuit}`:
```json
{ "cvu": { "cta_id": 1, "tipo": "1", "titular": "PRUEBA ModifCVU", "moneda": "032", "persona_tipo": "F" } }
```
`ModifCVUscr/{cvu}/{cuit}` es la variante con screening, mismo body, mismo mecanismo de aviso que el alta.

**Baja** — `DELETE /apiCVU/CVU/BajaCVU/{cvu}/{cuit}` (sin body, parámetros en la URL).

**Consulta** — `GET /apiCVU/CVU/ConsultaCVU/{cvu}` (sin body).

### Secuencia completa — Alta de CVU con screening (flujo paso a paso)

1. PSP: `POST /apiCVU/CVU/AltaCVUscr` con el body de arriba → Coelsa deja el CVU en `3201 – CVU EN SCREENING`.
2. Coelsa → Banco Débito (endpoint dado de alta previamente vía `POST /apiCVU/Banco/EndPoint`): `POST [endpoint]/AvisoOperacionCVU` — el banco valida y responde con `3300` (correcto) o `3400` (eliminado/inactivo).
3. Coelsa aplica el resultado: si `3300` → CVU queda `3200 – ACTIVO`; si `3400` → CVU queda `3400 – ELIMINADO/INACTIVO`.
4. Coelsa → PSP: nuevo `AvisoOperacionCVU` informando el estado final (`3200` o `3400`).
5. Para pruebas en homologación, el endpoint `POST /apiCVU/Banco/AvisoOperacionCVU` permite simular manualmente la respuesta del banco del paso 2.

## Relevancia para proyectos/áreas vigentes

- Complementa directamente `wallet/validaciones_y_alias_cvu.md` y `wallet/apis_expuestas/cvu/` (API pública de Bind) — esta es la capa de implementación por debajo.
- El límite de comisión (0.60%–0.80%) y el mecanismo de tramo gratuito coinciden exactamente con lo ya documentado en `adquirencia/mecanica_qr_coelsa.md` (Parte 3) para QR — confirma que es la **misma API de Comercios** subyacente a ambos flujos (QR de adquirencia y CVU de wallet), tal como esa nota ya advertía ("infraestructura compartida con Wallet").
- El alta masiva por SFTP (10.000 CVU o comercios por archivo) no estaba documentada en ningún lugar de la wiki — puede ser relevante para iniciativas de altas masivas (cross-ref: `wiki/1_proyectos/prd-66_provincianet_creacion_masiva_qr/` trabajó un problema de volumen de altas de QR; vale la pena que el PM de ese proyecto revise si el canal SFTP masivo de Coelsa es una alternativa a lo que se investigó ahí).

## Confianza

Alta — documentación oficial completa. Sin contradicciones detectadas contra contenido ya existente.
