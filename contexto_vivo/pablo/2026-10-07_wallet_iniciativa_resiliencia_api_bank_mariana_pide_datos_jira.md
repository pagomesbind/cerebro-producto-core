---
id: 2026-10-07_wallet_iniciativa_resiliencia_api_bank_mariana_pide_datos_jira
pm: pablo
fecha_captura: 2026-10-07
fuente: "/sync_mails — mail 'Re: Bind PSP - próximos pasos' (threadId 1a0635a69f9a9a2a) y mail 'Re: Modelo desacoplado — resultado del análisis' (threadId 1a0d007a7b7c2a22), Mariana Nadalin, 2026-10-06/07"
producto: wallet
tema: PRD-12 — Mariana Nadalin responde el consolidado de pendientes y pide a Bind qué datos necesita el banco para el Jira de alta de Sociedad Militar
tipo: iniciativa
proyecto: PRD-12
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Novedad puntual para la fila de PRD-12 en `iniciativas.md`:**

El 2026-10-06 (20:55hs), Mariana Nadalin (COO) respondió punto por punto el mail consolidado de estado que Pablo Gomes había enviado horas antes sobre la migración al modelo desacoplado (`resiliencia_api_bank/`):

- **Pendiente 1 (fijar fecha de migración de Sociedad Militar en producción):** aclara que depende de cuándo el banco configure el modelo desacoplado en la cuenta productiva.
- **Pendiente 2 (solicitar al banco que configure la cuenta de Sociedad Militar):** confirma "OK lo pido" — lo gestiona ella directamente con Banco Industrial.
- **Pendiente 3 (aviso a clientes con esquema desacoplado activo):** propone un primer borrador de texto de comunicación genérica (anuncia una mejora de infraestructura operacional, aclara que el cambio es transparente, que servicios/interfaces/SLA no cambian y que no se requiere acción del cliente) a validar con el equipo antes de usarlo como estándar para las próximas migraciones.
- **Pendiente 4 (adaptar el Conciliador):** confirma que el requerimiento ya está cargado con desarrollo, solo falta que se confirme la fecha.

Al día siguiente (2026-10-07, 12:23hs), Mariana escribe en paralelo directo al hilo con Banco Industrial ("Bind PSP - próximos pasos") reafirmando que Bind está en condiciones de avanzar con Sociedad Militar como primera empresa del desacoplado, y pregunta explícitamente **qué datos necesita el banco para que Bind suba el ticket de Jira correspondiente** — pregunta sin responder todavía del lado de Bind/el banco.

Impacto: el proyecto sigue avanzando con buen ritmo (staging validado 05/10, primera cuenta de producción confirmada), pero queda un bloqueante puntual nuevo — nadie respondió todavía qué información hace falta para poder cargar el ticket de Jira que dispare la configuración bancaria de Sociedad Militar. Nueva tarea personal T-189 (🔴) para cerrarlo.
