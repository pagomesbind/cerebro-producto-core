# Overview de la Empresa — Bind PSP

> Fuente: `raw/Overview de la empresa.docx` (ingesta Fase 1, 2026-07-02). Ver [equipo.md](overview_equipo.md) para equipos y [producto/index.md](../overview_productos/index.md) para líneas de negocio.

## Qué es Bind PSP

Bind PSP es una fintech que pertenece al **Grupo BIND**, creada en **2021**. Nació con foco en soluciones de adquirencia y emisión, aprovechando el alcance del ecosistema BIND y su base de clientes existente.

- **Modelo de negocio:** marca blanca B2B2C — soluciones de métodos de pago diseñadas y personalizadas según las necesidades de cada negocio, administradas y operadas desde el ecosistema BIND.
- **Licencia:** obtuvo la licencia de **PSP (Proveedor de Servicios de Pago)** ante el BCRA, y desde entonces enfoca su explotación en **Wallet as a Service** y **PSP as a Service**.
- **Foco estratégico:** APIs y funcionalidades apificadas — finanzas embebidas para clientes. Cuenta con alguna plataforma con front para usuario final, pero **no es la prioridad** de producto.
- **Filosofía:** agilidad y velocidad de respuesta ante necesidades del negocio, buen go-to-market sin sacrificar atención al cliente, y aprovechamiento de sinergias/alianzas con otras empresas del Grupo BIND.

## Grupo BIND — el ecosistema

Grupo BIND es un ecosistema integral de servicios financieros y bancarios (digital y humano) para empresas, fintechs y personas. Su estructura está compuesta por:

- BIND Banco
- BIND Garantías
- BIND Inversiones
- BIND Seguros
- BIND Leasing
- BIND Broker
- **BIND PSP** (este negocio)
- bindX

Esto permite una experiencia financiera 360°, modular y escalable.

### Escala e infraestructura

- SLA del **99,8%**.
- Más de **340 millones de transacciones mensuales**.
- Lidera la red **Coelsa** como banco N°1 en volumen de transacciones.
- Procesa operaciones para **más del 70% de las billeteras digitales** de Argentina, incluyendo **Mercado Pago, Personal Pay y Prex**.

### Rol regulatorio de BIND Banco frente a los PSP

De acuerdo con la regulación del BCRA, la participación de **BIND Banco** en esquemas que involucran PSP se limita a su rol de entidad financiera: **apertura y mantenimiento de cuentas bancarias**. Los fondos de los usuarios de estos servicios deben mantenerse dentro del sistema financiero formal.

> Nota de arquitectura: esto explica por qué las cuentas recaudadoras y CBU/CVU de Bind PSP están físicamente alojadas en **Banco Industrial** (ver [wallet_overview.md](../overview_productos/overview_wallet.md) y [adquirencia_overview.md](../overview_productos/overview_adquirencia.md)).

### Banking-as-a-Service (BaaS)

Grupo BIND fue el primer banco del sistema financiero argentino en disponibilizar APIs abiertas (BaaS), permitiendo que billeteras digitales, fintechs, telcos, retailers y plataformas tecnológicas integren servicios financieros directamente en su experiencia de usuario. Marcas que corren sobre esta infraestructura: **Mercado Pago, Aerolíneas Argentinas, Cencosud, Natura, Personal Pay**.

### Visión hacia 2026

Expansión de la arquitectura API-first, incorporación de inteligencia artificial en procesos clave, y desarrollo de nuevas soluciones financieras digitales.

## Contexto actual (2026)

> Fuente: `raw/Actualidad.docx` (ingesta 2026-07-07).

El 2025 fue un año de fuertes ganancias para Bind PSP, impulsado por la performance de **Astropay** en Wallet — su mejor cliente. Sin embargo, el panorama cambió de forma significativa a comienzos de 2026:

- **Salida de Astropay:** dejó de ser cliente de Bind PSP en **marzo de 2026**, por decisión del Grupo BIND por motivos de compliance, políticos y económicos. Astropay era un cliente conflictivo en materia de compliance por su rubro (muy relacionado al juego de apuestas digital).
- **Incidente de fraude:** en simultáneo, en marzo de 2026 Bind PSP sufrió un incidente crítico de fraude — un bug técnico en Transferencias Pull explotado por usuarios externos, que resultó en un robo de aproximadamente **$11.500 millones** a las organizaciones. Bind PSP debió hacerse cargo de ese dinero. Ver el postmortem completo en [postmortem_transferencias_pull_marzo_2026.md](../../4_archivos/postmortem_transferencias_pull_marzo_2026.md).
- **Respuesta de Grupo BIND:** tras el golpe (con mucha incertidumbre sobre el futuro del negocio en el medio), el Grupo BIND decidió sostener la operación de Bind PSP, pero con muchos más controles: comités internos de decisión con participación de personas ajenas a Bind PSP, auditorías internas más fuertes, exigencia de regularizar riesgos abiertos y de mejorar procesos.
- **Impacto en los objetivos del año:** los objetivos de volumen que el CEO había fijado a fines de 2025 para el cierre de 2026 se habían considerado inalcanzables el 2026-07-07 — el foco pasó a remediar compliance y auditoría. **Actualización 2026-07-17:** el CEO reafirmó estos mismos objetivos como las dos North Star Metrics vigentes de la empresa. Ver el detalle de esos objetivos, las palancas de negocio identificadas (oportunity trees) y el estado vigente en [north_star.md](../direccion/north_star.md).
- **Pipeline comercial:** pese al contexto, hay negociaciones avanzadas con clientes grandes — **COTO, Arcos Dorados, Hipódromo de Palermo** — algunos ya en etapa de integración técnica, que la empresa espera poner operativos este año para empezar a captar su volumen.

## Gobierno corporativo (Grupo BIND)

> Fuente: comunicado oficial `directorio@bind.com.ar` — "MODELO DE GOBIERNO CORPORATIVO" (2026-08-05).

- **CEO de Grupo BIND: Marcela Fernie** — primera vez que la wiki registra el nombre; hasta esta comunicación las referencias al "CEO" en [north_star.md](../direccion/north_star.md) y en la sección de contexto arriba quedaban sin nombrar.
- **Directorio actual:** Ariel Sigal, Carlota Chippy Meta, Andrés Meta y Juan Carlos Altmann.
- **Nuevos advisors del Directorio (desde agosto 2026)**, sumados para evolucionar el modelo de gobierno corporativo acompañando el crecimiento del Grupo:
  - **Sebastián Habif** — conocimiento de BIND y del ecosistema emprendedor, para impulsar el desarrollo de negocios a nivel de todo el Grupo.
  - **Gabriel Szpigiel** — ex portfolio manager en mercados emergentes, asesora en mercado de capitales y alternativas de financiamiento.
  - **Tomás Bein** — visión y expertise en estrategia.
  - **Andrés Schneider** — asesora sobre tendencias macroeconómicas y de la industria financiera.
- **Salida del Directorio: Facundo Vázquez** — deja el Directorio de Grupo BIND tras varios años; continúa como Presidente de **Poincenot** y sigue vinculado a proyectos conjuntos con el Grupo.

## Venta del negocio de banca minorista a Banco Patagonia (2026-08-27)

> Fuente: comunicado interno oficial "Novedad importante sobre Banca Minorista" (`directorio@bind.com.ar`, firmado por Andrés Prida, Presidente de Banco Industrial S.A., 2026-08-27).

Grupo BIND alcanzó un acuerdo con **Banco Patagonia** para la **transferencia parcial del negocio de banca minorista y fondo de comercio** de Banco Industrial (la entidad bancaria del Grupo). No afecta directamente a Bind PSP ni a ningún producto de pagos — el comunicado es sobre el negocio de banca minorista tradicional del banco, sin mención explícita de impacto en la operatoria de Bind PSP.

**Motivación declarada:** la estrategia de Grupo BIND viene focalizándose hace varios años en el negocio de empresas (PyMEs, Medianas y Corporativo) y la banca digital como habilitador financiero — el negocio de banca minorista tradicional "requiere de una capilaridad y una economía de escala que hoy se distancian de nuestro foco estratégico".

**Alcance:** se transfieren 28 sucursales de la red del banco. **Excepción:** la Casa Central (Av. Santa Fe 880, CABA) no se transfiere. **Excluidos del acuerdo:** la Banca Privada Zafiro y ciertos clientes, que continúan siendo parte del negocio de Grupo BIND.

**Sobre Banco Patagonia (contraparte):** uno de los principales bancos privados de Argentina, entre los 6 primeros del país en volumen de préstamos y depósitos. Accionista controlante: Banco do Brasil. Más de 1 millón de clientes individuos, ~2.800 empleados, red de más de 200 puntos de atención a nivel nacional.

**Continuidad laboral:** transferencia al Banco Patagonia de los colaboradores alcanzados, con continuidad de la relación laboral (Arts. 225 y 229 de la LCT — transferencia de establecimiento), reconociendo antigüedad y derechos adquiridos.

**Timeline:** proceso de transición durante los próximos meses. Closing sujeto a condiciones precedentes y aprobaciones regulatorias — estimado efectivo a **inicios de 2027**. Comité de Transición integrado por ambos bancos (por Grupo BIND: Ariel Salituri, Marcela Alboher, Inti Benites, coordinado por Gastón Eckelhart).

---
*Última actualización: 2026-08-31 — `/context_merge`: nueva sección "Venta del negocio de banca minorista a Banco Patagonia" (comunicado interno oficial, 2026-08-27).*
*Última actualización anterior: 2026-08-05 — Nueva sección "Gobierno corporativo (Grupo BIND)": nombra por primera vez a la CEO (Marcela Fernie), Directorio actual, incorporación de 4 advisors y salida de Facundo Vázquez.*
*Última actualización anterior: 2026-07-17 — Nota de actualización sobre reafirmación de las North Star Metrics por el CEO (ver [north_star.md](../direccion/north_star.md)).*
*Última actualización anterior: 2026-07-07 — Agregado "Contexto actual (2026)": salida de Astropay, incidente de fraude de Transferencias Pull y respuesta de Grupo BIND.*
