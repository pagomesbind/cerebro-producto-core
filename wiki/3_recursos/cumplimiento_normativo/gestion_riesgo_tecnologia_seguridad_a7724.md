# Gestión de Riesgos de Tecnología y Seguridad de la Información — Comunicación "A" 7724 BCRA

> Estado: aplicabilidad a Bind PSP asumida como posición de negocio/compliance del PM (no interpretación legal formal verificada con Legales). Sin relevamiento de madurez actual todavía.
>
> Fuente: Texto ordenado BCRA "Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información" (Comunicación "A" 7724, RUNOR 1-1785, 10/03/2023), aportado por el usuario en `raw/A7724.pdf`. Aplicabilidad a Bind PSP confirmada directamente por el PM en sesión de trabajo del 2026-09-08.

## Qué es esta normativa

La Comunicación "A" 7724 del BCRA (10/03/2023) deroga el viejo régimen de "Requisitos mínimos de gestión, implementación y control de los riesgos relacionados con tecnología informática..." y lo reemplaza por un marco mucho más amplio y moderno: **"Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información"**, con 11 secciones:

1. Gobierno de TI/seguridad (roles de Directorio/Alta Gerencia/comité de gobierno).
2. Gestión de riesgos de TI.
3. Gestión de TI (arquitectura empresarial, IA/machine learning).
4. Gestión de seguridad de la información (control de accesos, autenticación multifactor, biometría, criptografía).
5. Gestión de continuidad del negocio (BIA, RTO/RPO, planes de continuidad).
6. Infraestructura tecnológica (gestión de cambios, copias de respaldo con retención mínima de 6 años para registros contables/auditoría).
7. Gestión de ciberincidentes.
8. Desarrollo/adquisición/mantenimiento de software (incluye requisitos específicos para el uso de IA/modelos de lenguaje en el ciclo de desarrollo).
9. Gestión de terceras partes (subcontrataciones, derechos de auditoría del BCRA).
10. (Correlativa a las anteriores en el texto ordenado.)
11. **Canales Electrónicos** (ATM, banca móvil/internet, POS, plataformas de pagos móviles) — matriz de escenarios de riesgo y ~90 requisitos técnico-operativos puntuales.

## Por qué se había marcado como duda de aplicabilidad, y cómo se resolvió

El encabezado de la Comunicación "A" 7724 dirige la norma únicamente a "LAS ENTIDADES FINANCIERAS" — a diferencia de las comunicaciones sobre "Sistema Nacional de Pagos" y "Proveedores de Servicios de Pago" (que sí incluyen expresamente a los PSP/PSPCP entre los destinatarios), esta comunicación no menciona a los PSP en su Sección 1.1 ("Sujetos obligados: 1.1.1. Entidades Financieras"). Se había especulado con la existencia de una versión adaptada para servicios financieros digitales (Comunicación "A" 7783, citada en la tabla de correlaciones de otra norma pero no conseguida).

**Resolución (2026-09-08):** consultado directamente, el PM confirmó la postura de Bind PSP: **"Somos una entidad financiera, una PSP es una entidad financiera."** Por lo tanto, el marco de la Com. "A" 7724 se toma como aplicable directamente a Bind PSP, sin esperar ni buscar una versión recortada específica para PSP. Es una posición de negocio/compliance del PM, no una interpretación legal formal verificada con Legales — se deja explícita en el canon para que cualquier sesión futura sepa que la aplicabilidad ya fue asumida, no que sigue siendo una pregunta abierta.

## Qué falta (no bloqueante, seguimiento normal)

Contrastar la madurez actual de gobierno de TI/seguridad de Bind PSP (gestión de incidentes, continuidad del negocio, ciclo de vida de software, gestión de terceras partes como Fintexa) contra las 11 secciones de esta norma — no hay todavía ningún documento de referencia sobre esto en el Cerebro. Es trabajo de relevamiento futuro, no una definición pendiente.

## Anexo B — Comités de Tecnología/Seguridad de la Información y de Riesgos Tecnológicos/Continuidad del Negocio (2026-09-30/10-01)

> Fuente: hilo de mail "REGLAMENTO - ANEXO B" — Mariana Nadalin (COO BIND PSP) y Eugenia Blanco (Auditoría, Banco Industrial), 2026-09-30 a 2026-10-01, threadId `1a0f287dad25c235`.

Uno de los requerimientos del Anexo B del BCRA le pide a Bind PSP **"proveer los reglamentos de cada uno de los Comités existentes (Tecnología y Seguridad de la Información, Riesgos Tecnológicos y/o Continuidad del Negocio), junto con las actas correspondientes a las reuniones celebradas durante el último semestre"** (carpeta "A1a"). Mariana Nadalin (COO de Bind PSP) consultó el 2026-09-30 a Eugenia Blanco (Auditoría, Banco Industrial) porque **la estructura de la PSP no tiene estos Comités conformados**.

**Respuesta y criterio de la auditora del banco (Eugenia Blanco, 2026-09-30):**
- Mientras los Comités no estén conformados, **no corresponde enviar reglamentos** — lo correcto es declarar en las planillas del Anexo B (`Planillas\XXXXX - 5 – A1c.xlsx`) un porcentaje de cumplimiento parcial: **25%** si hay acciones iniciales de implementación, o **50%** si el requisito está parcialmente implementado.
- La información presentada al BCRA tiene carácter de **declaración jurada (DDJJ)** — una inconsistencia entre lo informado y la evidencia real, detectada en una eventual inspección de la GAES, es el peor escenario posible.
- La base para contestar el Anexo B debe ser el **GAP Analysis y los Planes de Adecuación**, con tareas/tiempos/fechas estimadas para todo punto que no esté en full compliance.
- El Anexo B se presenta **semestralmente** — el BCRA ve la evolución recién en la siguiente entrega.
- **Pasos recomendados del Plan de Adecuación** para conformar un Comité: (1) conformación por Acta de Directorio (composición ideal: 2 directores + máximo responsable del área), (2) redacción del Reglamento (periodicidad de reuniones, formato de Actas, toma de decisiones, etc.), (3) primera reunión del Comité + redacción del Acta.
- Se organiza una reunión con Virginia Eggs (Auditoría) y Claudio Mendizábal (Compliance IT del banco) para revisar este punto y otras dudas del Anexo B.

**Avance de Bind PSP (Mariana Nadalin, 2026-10-01):**
- Ya está definida la nómina de quienes conformarán el Comité de la PSP.
- Se pidió al banco el **reglamento modelo** que usan internamente, para adaptarlo específicamente a la PSP y formalizarlo rápido.
- Objetivo: tener el borrador adaptado para la **primera reunión constitutiva entre martes y miércoles de la semana siguiente** (semana del 06-07/10/2026).
- El banco (Virginia Eggs, Líder de Auditoría de Sistemas) envió el 2026-10-01 dos reglamentos modelo como adjunto: `REG-SI-01 Reglamento Comité de Seguridad de la Información.pdf` y `REG-TYS-01 Reglamento Comité Sistemas y Tecnología.pdf` (contenido de los PDF no leído automáticamente — quedan como referencia de modelo, no se transcribe su contenido).

En copia en todo el hilo: Emma Vignoles, Hernán Clarich, Pablo Gomes.

## Cronograma de auditoría del BCRA sobre el ciclo de vida completo del software (2026-10-02)

> Fuente: reunión "Revisión Pruebas QA" (Bind PSP + Fintexa, 2026-10-02).

Hernán Clarich (Fintexa, gobierno de tecnología/sistemas) confirmó que, a partir de ahora, el **BCRA audita el ciclo de vida completo del software hasta la puesta en producción**, incluyendo segregación de ambientes y trazabilidad de punta a punta — esto es parte del marco de Anexo B ya referenciado arriba (conformación de Comités de TI/Seguridad), no un requisito nuevo separado.

**Cronograma de 2 etapas:**
1. **Este año (2026):** el BCRA pide una "foto" del estado actual — qué procesos existen hoy, cuáles están en curso, y cuál es el gap de todo lo que falta regularizar. No es todavía una auditoría formal, es el primer relevamiento de scope.
2. **El año que viene (2027, sin fecha exacta):** inspección formal.

**Motivo adicional citado:** el BCRA viene mirando este proceso específicamente a raíz de un incidente ya reportado anteriormente (ocurrido en abril, según la minuta) — van a revisar de nuevo procesos de seguridad, gestión de vulnerabilidades y gestión de backlog, buscando "debilidades en la gobernanza y la gestión".

**Qué van a pedir — métricas de gestión:** cantidad y forma de los pasajes/releases, cómo están segregados los ambientes, cómo son las pruebas, el ciclo de vida de punta a punta (incluye evolutivos). Esto alcanza también la relación con terceras partes (Fintexa como proveedor) — el BCRA pone foco especial en el control que Bind PSP ejerce sobre lo que delega a terceros. Matías Alzogaray (PM Bind) se compromete a presentar un primer boceto de métricas estandarizadas el viernes 2026-10-09, en paralelo con sus propias métricas de ciclo de ticket (tiempo desde asignación hasta cierre) y el trabajo ya en curso de equiparar story points entre el Jira de Bind y el de Fintexa.

**Conexión con el semáforo de riesgo de despliegue:** el registro formal de aceptación de riesgo (acordado en la misma serie de reuniones, ver `2_areas/procesos/analisis_de_riesgo_de_despliegue.md`, pendiente de permiso de usuario) alimenta directamente el "apetito de riesgo" que el BCRA va a pedir en esta auditoría.

## Desglose operativo del apartado B del Anexo B en planillas B1a-B1h, con dueños asignados (2026-10-02)

> Fuente: mail "BCRA Anexo B. ver este próximo Lunes" — Hernán Clarich, 2026-10-02.

Hernán Clarich compartió el desglose de trabajo del apartado **B** del Anexo B del BCRA — "Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información asociados a los servicios financieros digitales" — con asignación de dueños por planilla, todas en una carpeta de Drive compartida ("Anexo B"):

- **B1a** (estado de cumplimiento de la planilla general) — Hernán, nivel macro; Pablo/Maru ayudan con las herramientas de monitoreo transaccional.
- **B1b** (servicios financieros digitales + herramientas de monitoreo transaccional) — Pablo, con soporte de evaluación de Hernán.
- **B1c** (detalle de soluciones aplicadas en el proceso de alta digital de clientes/onboarding + su monitoreo transaccional) — Pablo.
- **B1d** (controles aplicados en el proceso de alta digital) — Maru/Rocío.
- **B1e** (monitoreo transaccional para prevención de fraude + cumplimiento Com. B 13117/CPF) — Maru/Rocío.
- **B1f** (estrategia de monitoreo transaccional por modalidad de servicio financiero digital, patrones de comportamiento, factores de autenticación) — Pablo.
- **B1g** (procedimientos de alta digital de clientes y de alta no concretada) — Pablo, solo si existe un nuevo servicio financiero digital en curso de desarrollo o a desarrollarse.
- **B1h** (proyectos en desarrollo/previstos de nuevos productos/servicios financieros digitales, con sus medidas de protección, factores de autenticación, monitoreo y gestión de ciberincidentes) — sin asignado explícito en el mail.

Seguimiento de avance programado para el lunes 2026-10-05.

## Ver también

- [pci_dss_recertificacion.md](pci_dss_recertificacion.md) — seguridad de pagos con tarjeta, dominio adyacente pero distinto (PCI DSS es específico de datos de tarjeta; esta norma es de alcance general de TI/ciberseguridad).
- [gestion_riesgo_fraude_bcra.md](gestion_riesgo_fraude_bcra.md) — antifraude (Com. "A" 8471/8473), dominio adyacente pero distinto.

---
*Última actualización: 2026-10-05 — `/context_merge`: nuevas secciones "Cronograma de auditoría del BCRA sobre el ciclo de vida completo del software" y "Desglose operativo del apartado B del Anexo B en planillas B1a-B1h, con dueños asignados" (Pablo Gomes).*
*Última actualización anterior: 2026-10-01 — `/context_merge`: nueva sección "Anexo B — Comités de Tecnología/Seguridad de la Información y de Riesgos Tecnológicos/Continuidad del Negocio" (Pablo Gomes).*
*Creado: 2026-09-08 — `/context_merge`, desde auditoría de cumplimiento normativo del PM (2026-09-08).*
