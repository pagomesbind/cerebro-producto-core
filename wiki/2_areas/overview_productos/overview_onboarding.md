# Onboarding — Overview de Producto

> Fuente: `raw/Product overview_Onboarding.docx` (ingesta Fase 1, 2026-07-02). Área de negocio: [equipo.md](../overview_empresa/overview_equipo.md). Provisto por: FINTEXA (producto preexistente, adoptado para este uso — ver [decisiones.md](../direccion/decisiones.md)).

## Qué es

Producto que automatiza el alta de comercios en **Adquirencia** (y otras altas) permitiendo que el propio titular complete el flujo sin intervención manual. Cada **Entidad** = un flujo de onboarding, con front web marca blanca customizable (colores, logos) por entidad.

## Las 3 fases

### Fase 1 — Obtención de datos y validación

Se solicita información al usuario y se consulta a servicios externos (Renaper, ARCA, Nosis, Worldsys, etc.). Algunas validaciones son bloqueantes en línea (marcadas con \* abajo); otras solo levantan información para usarse en la Fase 2.

| Paso | Bloqueante | Descripción |
|---|---|---|
| Lectura PDF417 del DNI | ✅ | Extrae datos del DNI vía código PDF417 para invocar Renaper Datos. |
| Lectura OCR del DNI | — | Contingencia opcional si el PDF417 no se puede interpretar. |
| Análisis de morfología de fotos del DNI | — | Analiza la imagen para intentar detectar que se trata de un DNI real y no una foto o una imagen editada. |
| Renaper Datos | ✅ | Valida edad límite, vigencia del ejemplar y si la persona está fallecida. |
| Selfie + Renaper Rostro | ✅ | Valida match entre selfie y rostro registrado en Renaper. |
| Nosis | — | Información general; de acá se obtiene el CUIT si el usuario no lo ingresó. |
| Padrón ARCA A5 | — | Información impositiva / actividad en ARCA. |
| UIF | — | Determina si la persona es sujeto obligado ante la UIF. |
| Worldsys PEP y terrorista | — | Listas de PEP / terrorismo. |
| Prueba de vida (Socialnet) | ✅ | Video en vivo vía URL provista por Socialnet. |
| Listas negras del BIND | — | Contra listas negras de Banco Industrial. |
| Listas negras/blancas propias de CUIT | — | Cargadas en el backoffice de Onboarding. |
| Listas negras de email / teléfono | — | Cargadas en el backoffice de Onboarding. |
| Scoring de teléfono / email (Seon) | — | Servicio externo Seon. |
| OTP a email | ✅ | Valida propiedad del email. |
| OTP a celular | ✅ | Valida propiedad del celular. |
| Aceptación de declaraciones juradas y T&C | — | — |

### Fase 2 — Matriz de validación

Última instancia en la que la solicitud puede rechazarse. Se construye un **puntaje de ponderación** configurable por entidad (ejemplo real de la fuente: sin actividad en AFIP = 100 puntos). Se configuran dos umbrales de puntos:
- Por encima de un umbral → **VALIDACIÓN MANUAL**.
- Por encima de otro umbral → **RECHAZADA**.

Si algún servicio externo usado en esta fase (Worldsys, ARCA/AFIP, UIF) estuvo caído al momento de la consulta, la solicitud pasa automáticamente a **VALIDACIÓN MANUAL**, permitiendo reprocesar la consulta fallida desde el backoffice.

En estado VALIDACIÓN MANUAL, un usuario del backoffice puede reprocesar el servicio fallido, o aprobar/rechazar manualmente indicando motivo. Si se aprueba, continúa a Fase 3.

### Fase 3 — Altas

Acá el usuario ya pasó exitosamente las validaciones de la Fase 2. Entonces el sistema procede a concretar las altas en los sistemas externos o internos que tenga configuradas como acciones del flujo (por ejemplo, alta de cuenta en Wallet, alta de cuenta bancaria, etc.), en **orden secuencial** (no en paralelo). Si una falla, las siguientes no se ejecutan y la solicitud pasa a estado **ERROR EN ALTA**.

Altas posibles:
- Cuenta en Wallet
- Cuenta + CVU en Wallet
- Cuenta + CVU + cuenta comitente en Wallet
- Comercio en Adquirencia
- Cuenta en Banco Industrial
- Producto (CBU) en Banco Industrial
- Usuario en homebanking de Banco Industrial
- Tarjeta (débito/crédito) en Banco Industrial
- Legajo digital (nuevo trámite con la documentación de la solicitud)
- Notificación a la entidad (webhook — solo si la solicitud fue aprobada)

Cada paso de Fase 1 y cada acción de Fase 3 es configurable y parametrizable por flujo/entidad; no todas ocurren necesariamente ni en el mismo orden.

## Modalidades de integración

1. **Onboarding con front marca blanca**: FINTEXA provee el front, con URL fija por entidad. El primer paso suele ser cargar fotos del DNI. Todas las solicitudes se ven y gestionan desde el backoffice.
2. **Onboarding por API por partes**: para entidades con front propio, que consumen las APIs de **OrquestadorBind** (API Manager) paso a paso.
3. **Onboarding por API con registro único**: para clientes que solo necesitan validaciones puntuales (ej. Renaper Datos, contratable solo por entidades importantes o bancarias). La entidad envía toda la info conocida de su cliente en un único endpoint; el onboarding ejecuta todas las validaciones y altas de forma secuencial y responde al final con el resultado y las cuentas creadas.

La documentación técnica de APIs y guías de integración se publica en la web de developers de Bind PSP.

## Integraciones con otros productos

- **Wallet**: altas de cuenta/CVU/cuenta comitente. Ver [wallet_overview.md](overview_wallet.md).
- **Adquirencia**: alta de comercio. Ver [adquirencia_overview.md](overview_adquirencia.md).
- **Banco Industrial**: altas de cuenta, producto CBU, usuario homebanking, tarjeta.

## Modelo de datos: Onboarding no tiene base de clientes

> Aclarado por Cristian Bonafede (Fintexa) en reunión técnica del 2026-07-17 (ver [PRD-202](../../1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md) §8).

La base de Onboarding guarda **solicitudes** (de validación/alta), no clientes ni cuentas — los datos de una solicitud se encriptan mientras se valida, pero la finalidad no es persistirlos como fuente de verdad a largo plazo. Cuando la validación finaliza, Onboarding se da vuelta y llama al producto correspondiente (Wallet, Adquirencia) para crear el recurso — a partir de ahí, **ese producto pasa a ser la fuente confiable de los datos del cliente** (si el cliente actualiza su email o su foto de DNI después, eso lo maneja Wallet/Comercio, no Onboarding). Implicancia práctica: **Onboarding no debería usarse como fuente de datos a futuro** para recuperar información de un cliente ya dado de alta (ej. "traer la última foto del DNI") — para eso está Legajo Digital (documentos) y el producto dueño del recurso (datos vivos).

**Nota de arquitectura en discusión (sin decisión cerrada, 2026-07-17):** el rol de Onboarding como orquestador de **todo** el flujo de alta (validar + crear la cuenta/comercio) está siendo cuestionado por el equipo de Fintexa a raíz de un bloqueo de seguridad sobre PRD-202 (la entidad no puede cambiar de consumer de Wallet a Onboarding para dar de alta una cuenta). Está en evaluación un modelo donde Onboarding se limita a **validar**, y cada producto (Wallet, Cobro) es quien efectivamente crea su propio recurso — revertiría el modelo actual descripto en "Fase 3 — Altas" arriba, donde es Onboarding quien concreta las altas en los sistemas externos/internos. Ver gap abierto en `../gaps_y_preguntas.md` (2026-07-17) y seguimiento en `0_direccion/estrategia/foco_onboarding.md` §5.

---
*Última actualización: 2026-07-17 — Nueva sección sobre el modelo de datos de Onboarding (no tiene base de clientes, solo solicitudes) y nota sobre la discusión arquitectónica en curso (Onboarding ¿orquesta todo, o solo valida?) — aportado por el usuario a pedido explícito, tras una reunión técnica con Fintexa.*
*Última actualización anterior: 2026-07-02 — Ingesta Fase 1; completadas por el usuario las 2 oraciones que habían quedado incompletas en la fuente original (paso "Análisis de morfología" y apertura de Fase 3).*
