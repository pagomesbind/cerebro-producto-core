# SUR FINANZAS — Mecánica de Plataforma White-Label Multi-Comercio (Wallet + Adquirencia)

> Estado: en producción. Fuente: Notion histórico, 6 Epics: **"SUR FINANZAS: MVP"** (34 tickets), **"SUR FINANZAS: Requerimientos"** (91 tickets — la Epic con más tickets relevada en todo el proyecto de ingesta), **"SUR FINANZAS: APK Wallet MVP"**, **"SUR FINANZAS: Links de pago en portal comercio"**, **"SUR FINANZAS"** (Dolor) y **"Worldsys etapa 2: separar SUR FIN"**. Reubicado desde `detalle_productos/transversal/sur_finanzas.md` en la reestructuración PARA en cascada (2026-08-12) — la ficha comercial del cliente vive en [`2_areas/clientes/casos_de_uso_clientes.md`](../../../2_areas/clientes/casos_de_uso_clientes.md), este archivo documenta solo la mecánica técnica.
>
> La mayoría de los tickets de estas Epics no tienen contenido más allá del título (son anteriores a que el equipo adoptara PRDs/Definiciones en Notion) — este documento sintetiza la mecánica a partir de los títulos y la escasa documentación disponible.

## 1. Qué es: un "agrupador" multi-comercio con canales configurables por comercio

El patrón que emerge del backlog es el de una plataforma **multi-comercio/multi-cuenta** (similar en espíritu a los "Agrupador mayorista" de Adquirencia) donde cada comercio de SUR FINANZAS puede tener:

- **Cuenta y saldo propios** (vía Wallet) — con movimientos, extracto, exportación a CSV, y una grilla de movimientos con **años de iteraciones de UX** (filtros por fecha, signo, CUIT, id Coelsa, tipo de comprobante, saldo al momento del comprobante, orden, paginado a 100 registros) — el volumen de tickets de "Grilla movimientos" (>15 solo en Requerimientos) refleja que este es el módulo más usado y más pedido por el cliente.
- **Canales de cobro configurables independientemente por comercio**: QR, POS y Botón pueden habilitarse/deshabilitarse por comercio (`Deshabilitar QR para comercio`, `Deshabilitar POS para comercio`, `Flujo habilitar sin split, Aceptador, wallet y pos`), incluyendo variantes de login: "solo wallet", "QR wallet" o "solo QR".
- **Multi-credencial** (ticket XL): un mismo comercio o usuario opera con más de una credencial/cuenta — evolucionó más adelante a **"Usuario multicuenta"** (SF2, "tener más de una cuenta+CVU por usuario/comercio") y a poder tener **más de una cuenta+CVU por comercio** desde el front.
- **Transferencias con costos propios** (ticket XL, prioridad máxima) — SUR FINANZAS cobra sus propios costos de transferencia, con pantalla dedicada de costos y lógica de cálculo por porcentaje.
- **Access Management centralizado** propio, con perfiles diferenciados (ej. "usuario supervisor no debe ver el saldo", "perfil de usuario solo consulta").

## 2. Integración normativa con Worldsys (banco/BCRA)

La Epic **"Worldsys etapa 2: separar SUR FIN"** (y tickets relacionados dentro de Requerimientos) indica que los reportes regulatorios que Bind PSP envía al banco/BCRA vía Worldsys tuvieron que **separarse explícitamente para SUR FINANZAS**: generar históricos de "lavado de operaciones", separar archivos de Wallet por PSP, y regularizar domicilios/actividades — es decir, SUR FINANZAS se reporta como una entidad normativamente distinguible dentro del mismo PSP, no mezclada con el resto de las organizaciones de Wallet. Ver [`3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md`](../../cumplimiento_normativo/index.md).

## 3. Deuda y pendientes normativos/operativos (Epic "Dolor" + cola de Requerimientos)

Varios ítems quedaron en estado `Pendiente` (nunca completados según el histórico, verificar en Jira):
- **Facturación automática contra AFIP.**
- **Automatización de Régimen Informativo (RI) BCRA y AFIP.**
- Acceso a archivos de Coelsa y del banco (aparentemente manual hasta el freeze).
- CPA en onboarding de nuevos clientes (mismo gap normativo de CPA que en Wallet general — ver `detalle_productos/wallet/organizaciones_y_configuracion.md`, reforzando que es un problema transversal, no aislado).
- Guardar información de integrantes por cuenta para Personas Jurídicas.

## 4. Bugs/hallazgos puntuales

- **Comprobante de reversa de transferencia no se veía** (bug confirmado en producción).
- **Token de Wallet vencía en el portal de comercio y no se mostraba el saldo** — clasificado como ticket de Soporte, no bug de desarrollo, sugiriendo que se resolvía operativamente (renovar sesión) en vez de corregir la expiración del token del lado del portal.
- **"SURF: Ocultar funcionalidad pago QR"**: en algún momento se decidió ocultar el pago QR específicamente para SUR FINANZAS — decisión de producto sin motivo documentado en el título, marca a preguntar si es relevante retomarla.
- **Sección Usuarios del Portal vacía** para un administrador real (confirmado en QA — ver también `detalle_productos/portal_admin/`).
- **Grillas de movimientos lentas con volumen**: se intentó adaptar a un endpoint nuevo ("2.0"), aunque 2 tickets de adaptación quedaron "No aplica" (descartados); quedó pendiente optimizar el filtro por ID Coelsa desde la grilla.
- **Bug de segmentación cruzada con TIN**: las cuentas de **TIN** se daban de alta en el calculador de costos con el segmento de **SUR FINANZAS** (mezcla de configuración entre dos clientes white-label distintos).

## Ver también

- [2_areas/clientes/casos_de_uso_clientes.md](../../../2_areas/clientes/casos_de_uso_clientes.md) — ficha comercial de SUR FINANZAS (modelo de negocio, casos de uso).
- `detalle_productos/wallet/organizaciones_y_configuracion.md` — mismo gap de CPA en onboarding, confirmado también en SUR FINANZAS.
- `detalle_productos/adquirencia/agrupador_mayorista.md` — mismo espíritu de multi-comercio con canales configurables, patrón "Agrupador mayorista".

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/sur_finanzas.md` (reestructuración PARA en cascada); ficha comercial del cliente separada a `2_areas/clientes/casos_de_uso_clientes.md` (D9).*
