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

## Ver también

- [pci_dss_recertificacion.md](pci_dss_recertificacion.md) — seguridad de pagos con tarjeta, dominio adyacente pero distinto (PCI DSS es específico de datos de tarjeta; esta norma es de alcance general de TI/ciberseguridad).
- [gestion_riesgo_fraude_bcra.md](gestion_riesgo_fraude_bcra.md) — antifraude (Com. "A" 8471/8473), dominio adyacente pero distinto.

---
*Creado: 2026-09-08 — `/context_merge`, desde auditoría de cumplimiento normativo del PM (2026-09-08).*
