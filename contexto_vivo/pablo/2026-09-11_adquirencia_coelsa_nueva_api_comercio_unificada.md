---
id: 2026-09-11_adquirencia_coelsa_nueva_api_comercio_unificada
pm: pablo
fecha_captura: 2026-09-11
fuente: "Ingesta manual de documentación pública de Coelsa (VPN habilitada) — https://documentacion.coelsa.com.ar/comercio/#introduccion — sitio completo (es corto: Introducción, Objetivo, Alcance, Solicitud de Token, Conectividad, API Comercios, Versionado). Consultado 2026-09-11."
producto: adquirencia
tema: Nueva API 'Comercio' de Coelsa — ABM unificado de comercios que soporta CBU y CVU (reemplazo potencial de la API apiCVU/Comercio solo-CVU)
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/coelsa_nueva_api_comercio_cbu_cvu.md
tipo_destino: crear
contradice: "no — complementa, no contradice, apiCVU/Comercio (ver adquirencia/mecanica_qr_coelsa.md Parte 4); es una API nueva y distinta, no una versión de la misma"
confianza: alta
estado: ingestado
merge_commit: <pendiente>
---

## Hallazgo clave — esta es una API distinta de la ya documentada

`adquirencia/mecanica_qr_coelsa.md` (Parte 4) documenta en detalle `apiCVU/Comercio/Comercio` (base `cvu.coelsa.com.ar`, exige que el comercio tenga **CVU** previo). El sitio de documentación `documentacion.coelsa.com.ar/comercio/` describe una API **distinta y más nueva**, con **su propio dominio** (`homo-comercio.coelsa.com.ar` / análogo en prod) y objetivo explícito declarado por Coelsa:

> "Crear un comercio con un modelo de negocio que permita una operación fluida y flexible... Desarrollar una nueva API para el ABM de Comercios que soporte tanto **CBU como CVU**... Integrar a los nuevos comercios en la nueva API, **sin requerir la validación de una CVU** para el alta del comercio... Mantener el flujo actual para los comercios que sigan operando con CVU. **Los comercios actuales no necesitan darse de alta nuevamente.**"

Es decir: Coelsa ofrece ahora una vía de alta de comercios que **no depende de tener un CVU primero** — puede darse de alta directo con CBU. Esto es relevante para **evaluar** si conviene migrar o adoptar esta vía para casos donde hoy se fuerza la creación de un CVU solo para poder dar de alta el comercio (ver troubleshooting de titularidad de CVU documentado en `mecanica_qr_coelsa.md` Parte 3 — varios de esos incidentes nacen justamente de la dependencia CVU-primero que esta API nueva promete eliminar).

**Relevancia directa para el proyecto abierto `wiki/1_proyectos/convenios_configuracion/`** (ABM de comercios/convenios, que ya trabaja con `entidad-comercio-v1.json`): si ese proyecto está diseñando o rediseñando el flujo de alta de comercios, esta API nueva de Coelsa es la contraparte externa a evaluar — **no se toca el proyecto directamente desde esta ingesta**, se deja la referencia para que el PM del proyecto la revise.

## Endpoints (`POST/GET/PUT/DELETE /api/ComercioPsp`)

Mismo esquema de auth (OAuth2 password grant) y mismas reglas de negocio de fondo que la API CVU (MCC de 4 dígitos según boletín CIMPRA 530, comisión numérica 2 decimales en rango 0,60%–0,80%, Razón Social/Nombre de Fantasía obligatorios, fecha de alta opcional ≤ hoy):

| Método | Endpoint | Función |
|---|---|---|
| POST | `/api/ComercioPsp` | Alta de comercio (CUIT + PSP) |
| POST | `/api/ComercioPsp/Masivo` | Alta masiva, límite 1000 ítems |
| DELETE | `/api/ComercioPsp/{pspId}/{cuitComercio}/{mcc}` | Baja por PSP+CUIT+actividad |
| GET | `/api/ComercioPsp/{pspId}/{cuitComercio}` | Consulta lista de comercios por CUIT/PSP |
| GET | `/api/ComercioPsp/{pspId}/{cuitComercio}/{mcc}` | Consulta puntual por PSP+CUIT+actividad |
| PUT | `/api/ComercioPsp/{pspId}/{cuitComercio}/{mcc}` | Modifica datos del comercio por actividad |
| PUT | `/api/ComercioPsp/{pspId}/{cuitComercio}` | Modifica solo tramo gratuito y categoría |

**Conectividad:** requiere VPN + Túnel IPSEC dedicado hacia `homo-comercio.coelsa.com.ar` (homologación) — distinto del túnel usado para DEBIN/CVU, a coordinar con el equipo de Telecomunicaciones si se decide integrar.

## Consideraciones de negocio (idénticas a las ya conocidas de apiCVU/Comercio)

- El PSP debe estar activo; el PSP/CUIT del comercio debe existir, estar activo y tener cuenta activa en el banco del token.
- La actividad comercial (MCC) debe estar asociada al PSP con su comisión.
- Los datos de categoría y tramo gratuito, al reinformarse, **actualizan** los comercios ya existentes asociados al mismo CUIT/PSP (no crean duplicados).

## Confianza y siguiente paso sugerido

Confianza alta en la lectura de la documentación; **no verificado** si Bind ya integró o evaluó esta API nueva, o si sigue usando exclusivamente `apiCVU/Comercio`. No es un gap (no hay contradicción documental), es una oportunidad a evaluar — queda mejor como pregunta directa al PM que como entrada en el banco de oportunidades, dado que depende de una decisión técnica puntual sobre una integración ya viva, no de una idea de producto nueva.
