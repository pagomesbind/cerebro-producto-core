---
id: 2026-09-08_gap_aplicabilidad_marco_ti_seguridad_a7724_psp
pm: pablo
fecha_captura: 2026-09-08
fuente: "Texto ordenado BCRA 'Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información' (Comunicación 'A' 7724, RUNOR 1-1785, 10/03/2023) — aportado por el usuario en `raw/A7724.pdf`. Aplicabilidad a Bind PSP confirmada directamente por el PM en sesión de trabajo del 2026-09-08."
producto: transversal
tema: Marco integral de gestión de riesgos de tecnología/ciberseguridad del BCRA (gobierno de TI, gestión de incidentes, continuidad del negocio, ciclo de vida de software, terceras partes, Canales Electrónicos) — Bind PSP se considera alcanzado directamente, sin necesidad de una versión adaptada para PSP
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/gestion_riesgo_tecnologia_seguridad_a7724.md
tipo_destino: crear
contradice: "no — 3_recursos/cumplimiento_normativo/pci_dss_recertificacion.md y gestion_riesgo_fraude_bcra.md cubren dominios adyacentes (seguridad de pagos con tarjeta, antifraude) pero ninguno cubre este marco de gestión de riesgos de TI/ciberseguridad de alcance general; se crea como archivo nuevo dentro de la carpeta ya existente."
confianza: alta
estado: en_cola
merge_commit:
---

## Qué es esta normativa

La Comunicación "A" 7724 del BCRA (10/03/2023) deroga el viejo régimen de "Requisitos mínimos de gestión, implementación y control de los riesgos relacionados con tecnología informática..." y lo reemplaza por un marco mucho más amplio y moderno: **"Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información"**, con 11 secciones que cubren: gobierno de TI/seguridad (roles de Directorio/Alta Gerencia/comité de gobierno), gestión de riesgos de TI, gestión de TI (arquitectura empresarial, IA/machine learning), gestión de seguridad de la información (control de accesos, autenticación multifactor, biometría, criptografía), gestión de continuidad del negocio (BIA, RTO/RPO, planes de continuidad), infraestructura tecnológica (gestión de cambios, copias de respaldo con retención mínima de 6 años para registros contables/auditoría), gestión de ciberincidentes, desarrollo/adquisición/mantenimiento de software (incluye requisitos específicos para el uso de IA/modelos de lenguaje en el ciclo de desarrollo), gestión de terceras partes (subcontrataciones, derechos de auditoría del BCRA), y una Sección 11 completa de "Canales Electrónicos" (ATM, banca móvil/internet, POS, plataformas de pagos móviles) con una matriz de escenarios de riesgo y ~90 requisitos técnico-operativos puntuales.

## Por qué se había marcado como duda de aplicabilidad, y cómo se resolvió

El encabezado de la Comunicación "A" 7724 dirige la norma únicamente a "LAS ENTIDADES FINANCIERAS" — a diferencia de las comunicaciones sobre "Sistema Nacional de Pagos" y "Proveedores de Servicios de Pago" (que sí incluyen expresamente a los PSP/PSPCP entre los destinatarios), esta comunicación no menciona a los PSP en su Sección 1.1 ("Sujetos obligados: 1.1.1. Entidades Financieras"). Se había especulado con la existencia de una versión adaptada para servicios financieros digitales (Comunicación "A" 7783, citada en la tabla de correlaciones de otra norma pero no conseguida).

**Resolución (2026-09-08):** consultado directamente, el PM confirmó la postura de Bind PSP: **"Somos una entidad financiera, una PSP es una entidad financiera."** Por lo tanto, el marco de la Com. "A" 7724 se toma como aplicable directamente a Bind PSP, sin esperar ni buscar una versión recortada específica para PSP. Esta es una posición de negocio/compliance del PM, no una interpretación legal formal verificada con Legales — vale la pena que quede así de explícita en el canon para que cualquier sesión futura sepa que la aplicabilidad ya fue asumida, no que sigue siendo una pregunta abierta.

## Qué falta (no bloqueante, seguimiento normal)

Contrastar la madurez actual de gobierno de TI/seguridad de Bind PSP (gestión de incidentes, continuidad del negocio, ciclo de vida de software, gestión de terceras partes como Fintexa) contra las 11 secciones de esta norma — hoy no hay ningún documento de referencia sobre esto en el Cerebro. Es trabajo de relevamiento futuro, no una definición pendiente.
