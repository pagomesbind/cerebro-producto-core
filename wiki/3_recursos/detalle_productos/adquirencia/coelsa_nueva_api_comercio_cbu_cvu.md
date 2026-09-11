# Coelsa — Nueva API "Comercio" (ABM unificado, soporta CBU y CVU)

> Estado: discovery — no construido. No verificado si Bind PSP ya integró o evaluó esta API; hoy Bind opera exclusivamente con `apiCVU/Comercio` (ver [`mecanica_qr_coelsa.md` Parte 4](mecanica_qr_coelsa.md)). Es documentación de referencia de una vía alternativa que expone Coelsa, no un desarrollo en curso de Bind.

> Fuente: Ingeniería manual de documentación pública de Coelsa (VPN habilitada) — https://documentacion.coelsa.com.ar/comercio/ (Introducción, Objetivo, Alcance, Solicitud de Token, Conectividad, API Comercios, Versionado). Consultado 2026-09-11.

## Por qué es una API distinta, no una versión de la ya documentada

[`mecanica_qr_coelsa.md` Parte 4](mecanica_qr_coelsa.md) documenta en detalle `apiCVU/Comercio/Comercio` (base `cvu.coelsa.com.ar`), que **exige que el comercio tenga un CVU previo** para poder darse de alta. El sitio `documentacion.coelsa.com.ar/comercio/` describe una API **nueva y separada**, con **dominio propio** (`homo-comercio.coelsa.com.ar` en homologación, análogo en producción), cuyo objetivo declarado por Coelsa es:

> "Crear un comercio con un modelo de negocio que permita una operación fluida y flexible... Desarrollar una nueva API para el ABM de Comercios que soporte tanto **CBU como CVU**... Integrar a los nuevos comercios en la nueva API, **sin requerir la validación de una CVU** para el alta del comercio... Mantener el flujo actual para los comercios que sigan operando con CVU. **Los comercios actuales no necesitan darse de alta nuevamente.**"

Es decir: Coelsa ofrece ahora una vía de alta de comercios que **no depende de tener un CVU primero** — puede darse de alta directo con CBU. Esto es relevante para **evaluar** si conviene migrar o adoptar esta vía para casos donde hoy se fuerza la creación de un CVU solo para poder dar de alta el comercio (varios de los incidentes de troubleshooting de titularidad de CVU documentados en `mecanica_qr_coelsa.md` Parte 3 nacen justamente de esa dependencia CVU-primero).

**Relevancia directa para el proyecto abierto `wiki/1_proyectos/convenios_configuracion/`** (ABM de comercios/convenios, ya trabaja con `entidad-comercio-v1.json`): si ese proyecto está diseñando o rediseñando el flujo de alta de comercios, esta API nueva de Coelsa es la contraparte externa a evaluar — no se toca el proyecto directamente desde esta ingesta, queda como referencia para que el PM del proyecto la revise.

## Endpoints — `/api/ComercioPsp`

Mismo esquema de autenticación (OAuth2 password grant) y las mismas reglas de negocio de fondo que la API CVU ya documentada (MCC de 4 dígitos según boletín CIMPRA 530, comisión numérica de 2 decimales en el rango 0,60%–0,80%, Razón Social/Nombre de Fantasía obligatorios, fecha de alta opcional ≤ hoy):

| Método | Endpoint | Función |
|---|---|---|
| POST | `/api/ComercioPsp` | Alta de comercio (CUIT + PSP) |
| POST | `/api/ComercioPsp/Masivo` | Alta masiva, límite 1000 ítems |
| DELETE | `/api/ComercioPsp/{pspId}/{cuitComercio}/{mcc}` | Baja por PSP+CUIT+actividad |
| GET | `/api/ComercioPsp/{pspId}/{cuitComercio}` | Consulta lista de comercios por CUIT/PSP |
| GET | `/api/ComercioPsp/{pspId}/{cuitComercio}/{mcc}` | Consulta puntual por PSP+CUIT+actividad |
| PUT | `/api/ComercioPsp/{pspId}/{cuitComercio}/{mcc}` | Modifica datos del comercio por actividad |
| PUT | `/api/ComercioPsp/{pspId}/{cuitComercio}` | Modifica solo tramo gratuito y categoría |

**Conectividad:** requiere VPN + Túnel IPSEC dedicado hacia `homo-comercio.coelsa.com.ar` (homologación) — **distinto** del túnel usado para DEBIN/CVU, a coordinar con el equipo de Telecomunicaciones si se decide integrar.

## Consideraciones de negocio (idénticas a las ya conocidas de `apiCVU/Comercio`)

- El PSP debe estar activo; el PSP/CUIT del comercio debe existir, estar activo y tener cuenta activa en el banco del token.
- La actividad comercial (MCC) debe estar asociada al PSP con su comisión.
- Los datos de categoría y tramo gratuito, al reinformarse, **actualizan** los comercios ya existentes asociados al mismo CUIT/PSP (no crean duplicados).

## Confianza y siguiente paso sugerido

Confianza alta en la lectura de la documentación pública; **no verificado** si Bind ya integró o evaluó esta API, o si sigue usando exclusivamente `apiCVU/Comercio`. No es un gap (no hay contradicción documental), es una oportunidad a evaluar — queda mejor como pregunta directa al PM que como entrada en el banco de oportunidades, dado que depende de una decisión técnica puntual sobre una integración ya viva, no de una idea de producto nueva.

## Ver también

- [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) Parte 3/Parte 4 — API `apiCVU/Comercio` ya integrada por Bind PSP (alta de comercio, tramo gratuito, comisiones).
- `wiki/1_proyectos/convenios_configuracion/` — proyecto de ABM de comercios/convenios que podría ser el consumidor natural de esta API si se decide adoptarla.

---
*Creado: 2026-09-11 — `/context_merge` desde `contexto_vivo/` (Pablo Gomes): nueva API "Comercio" de Coelsa (ABM unificado CBU/CVU, sin requerir CVU previo), documentación pública, no verificado si Bind la integró.*
