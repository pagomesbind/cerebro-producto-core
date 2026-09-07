---
id: 2026-09-01_arquitectura_api_bank_gap_catalogo_codigos_psi_externo
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta-PSICrearCuenta y https://sandbox.bind.com.ar/apidoc/api_data.json"
producto: transversal
tema: API BANK (Banco Industrial) — catálogo de códigos PSI/STI no accesible desde el portal público
tipo: gap
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/alta_de_cuenta.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## Descripción del gap

Al relevar el grupo `Alta_De_Cuenta` de API BANK (endpoints `PSICrearCuenta` y `STICrearCuenta`, ver item de conocimiento `2026-09-01_arquitectura_api_bank_alta_de_cuenta`), varios campos obligatorios del body remiten a un catálogo de códigos externo al portal, referenciado en la descripción del endpoint como:

> "En el documento adjunto se definen los valores posibles para: `civil_status`, `sex`, `occupation`/`occupation_description`, `laboral_activity`/`laboral_activity_description`, `nationality`, `province_code`/`province`, `country` — Archivo de Códigos-Descripciones (`@@URL_PSI_CODE_DESC`)"

El placeholder `@@URL_PSI_CODE_DESC` no está resuelto en el JSON fuente (`api_data.json`) — es una variable de template de apidoc.js que normalmente se sustituye en tiempo de build o requiere navegar el portal con JS para resolverse a una URL real. No se pudo acceder al contenido de ese archivo desde este relevamiento (basado en fetch directo del JSON del portal, sin ejecución de JS de la página).

## Impacto

Los endpoints `PSICrearCuenta`, `STICrearCuenta` y `STICrearCuentaPJ` (grupo `Alta_De_Cuenta`) quedan documentados con la forma de sus parámetros pero **sin los valores concretos permitidos** para varios campos obligatorios (estado civil, género, ocupación, actividad laboral, nacionalidad, provincia, país). Esto limita el valor de la documentación como referencia de implementación si en algún momento Bind necesitara integrar directamente contra estos endpoints de onboarding de API BANK (hoy no se usan — Bind opera contra API BANK principalmente para Cuenta/Billetera/Transferencias, no para onboarding de cuentas nuevas vía PSI/STI).

## Cómo resolverlo

- Navegar el portal `https://sandbox.bind.com.ar/apidoc/` con un navegador real (ejecutando JS) para ver si el link se resuelve a una URL visible en la UI, o
- Consultar directamente a Banco Industrial/Fintexa por el "Archivo de Códigos-Descripciones" de la integración PSI/STI, si en algún momento se evalúa este flujo de onboarding como alternativa.

No es urgente resolverlo mientras Bind no tenga un proyecto activo de onboarding vía PSI/STI de API BANK — se documenta como gap para que quede explícito que la documentación de `Alta_De_Cuenta` está incompleta en ese punto, y no como una omisión no declarada.
