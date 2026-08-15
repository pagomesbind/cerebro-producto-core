# Onboardings para el BIND (canal sucursal / banco)

> Estado: en producción.

> Contenido destilado de la Epic de Notion "Onboardings para el BIND" (24 tickets). A diferencia de las demás Epics de este módulo (onboarding digital self-service vía Wallet/API), esta Epic cubre las variantes de onboarding ligadas directamente a **BIND como banco** (sucursales, canales propios) — triage con menor profundidad porque la mayoría de los tickets son textos/wording sin descripción adicional más allá del título.

## 1. Variantes de flujo identificadas

La Epic agrupa al menos 3 flujos/marcas de onboarding distintos para clientes que se dan de alta a través de un canal ligado a la sucursal bancaria de BIND, no del onboarding digital B2B2C:

- **"Zafiro"**: flujo de referencia (`Flujo zafiro`), tomado como base para otras variantes (ver "BANCO Mercado abierto" — documentado como "ídem zafiro" con términos y condiciones distintos y el nombre de fantasía **"BIND PH SUC"**).
- **"OB Bind Mercado abierto"**: variante propia para un caso de negocio no detallado, con su propio flujo (`Sucursal del banco`, `Cambio wording flujo Banco SUC`, `Cambio de dominio para flujos del banco`).
- **"Socialnet"**: integración/autenticación contra un sistema o base de usuarios ya enrolados llamado Socialnet — incluye autenticar a los usuarios ya enrolados en Socialnet, ajustes varios, y una pantalla de carga con problema visual ("pantalla carga socialnet blanco").

Todos los flujos comparten piezas de infraestructura: envío de solicitudes a **Legajo Digital**, actualización de datos de contacto en **Bantotal** para comercios, y encriptación de datos personales de los onboardings (mismo estándar transversal que en [onboarding_personas_juridicas.md §5](onboarding_personas_juridicas.md)).

## 2. Reempadronamiento ("Júbilo")

Flujo separado de **reempadronamiento** (re-registro de clientes ya existentes), con nombre de proyecto interno "Júbilo Parte 1" — sugiere una migración o depuración de base de clientes que requirió pedirles vía este flujo web que se re-registren. Ajustes menores de copy/UX relevados en el backlog: texto de bienvenida (general y en el paso de ingresar celular), botón "Continuar sin…", título de la página web, pantalla de error "solicitud existente" y de "error desconocido", deshabilitar visualmente el botón de inicio una vez usado, y Términos y Condiciones agregados a la bienvenida.

## 3. Reglas de negocio y operación

- **Timeout de solicitudes pendientes**: las solicitudes en estado pendiente por más de 30 minutos pasan automáticamente a rechazadas.
- **Encriptación de datos personales**: aplicada a los onboardings de este canal como estándar de cumplimiento (ticket propio, sin más detalle en el backlog).

---
*Fuente: Notion histórico, Epic "Onboardings para el BIND" — ingesta 2026-07-06. La mayoría de los 24 tickets son ajustes de texto/UI sin descripción adicional en Notion más allá del título — triage no exhaustivo por falta de contenido, no por volumen.*
