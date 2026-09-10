---
id: 2026-09-10_onboarding_cooperacion_tributaria_ocde_fatca_fuente_primaria
pm: pablo
fecha_captura: 2026-09-10
fuente: "sesión de chat libre con el PM sobre PRD-202 — texto ordenado BCRA 'Depósitos de Ahorro, Cuenta Sueldo y Especiales' leído completo y citado línea por línea (t-depaho.pdf, archivado en wiki/4_archivos/historial_raw/2026-09_normativa_bcra_ampliacion_auditoria_onboarding/), puntos 1.3 y 4.13.1.1"
producto: onboarding
tema: 4ta DDJJ obligatoria (cooperación tributaria internacional OCDE/CRS + FATCA) — fuente primaria, no Gemini research
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/identificacion_personas_fisicas_cvu.md
tipo_destino: actualizar
contradice: "3_recursos/cumplimiento_normativo/identificacion_personas_fisicas_cvu.md §4 y §5 — la lista de '3 declaraciones juradas obligatorias' queda incompleta (falta la DDJJ de cooperación tributaria internacional) y toda la matriz de ese archivo está basada en investigación de Gemini (confianza declarada como no validada); esta captura aporta el texto primario, ya leído completo, de la norma BCRA que dan origen tanto al punto 1.3 (identificación mínima) que ese archivo sí cubre, como al 4.13.1.1 (cooperación tributaria) que no cubre"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué se agrega al canon

El archivo `3_recursos/cumplimiento_normativo/identificacion_personas_fisicas_cvu.md` (creado 2026-09-02, fuente: research de Gemini del PM, explícitamente marcado "no validado como ground truth") lista en su §4 **3 declaraciones juradas obligatorias**: PEP, Sujeto Obligado ante la UIF, y Origen/licitud de fondos. Falta una **4ta**: la DDJJ de cooperación tributaria internacional (Estándar OCDE/CRS + FATCA), que sí es exigida por una norma leída de punta a punta esta sesión (no por investigación de IA sin validar) — BCRA "Depósitos de Ahorro, Cuenta Sueldo y Especiales" (texto ordenado, última comunicación incorporada "A" 8444, 04/06/26).

### Fuente primaria — punto 4.13.1.1 (texto citado, no parafraseado)

> "4.13. Procedimientos especiales de identificación de clientes en materia de cooperación tributaria internacional.
> 4.13.1. Identificación de clientes.
> En función del Estándar de la Organización para la Cooperación y Desarrollo Económicos (OCDE) para el Intercambio Automático de Información sobre cuentas financieras y de las disposiciones de la Ley de cumplimiento fiscal de cuentas extranjeras (Foreign Account Tax Compliance Act, FATCA) de los Estados Unidos de América, las entidades financieras deberán arbitrar las medidas necesarias para identificar a los titulares de cuentas alcanzados por dicho estándar y disposiciones.
> A tal efecto: 4.13.1.1. Deberán solicitar a sus clientes titulares de cuentas declarables que sean personas declarables... la presentación de una declaración jurada... i. Personas humanas: Apellido/s y nombre/s. Documento de identidad. Lugar y fecha de nacimiento. Domicilio correspondiente al de la jurisdicción de residencia fiscal reportada. Información sobre el país de residencia fiscal (jurisdicción). Número de identificación fiscal en el país o jurisdicción residencia fiscal (NIF). Tipo y número de cuenta."

**Punto clave — FATCA y OCDE/CRS son regímenes legales distintos** (FATCA es ley unilateral de EE.UU.; OCDE/CRS es el estándar multilateral), **pero esta norma argentina los agrupa bajo el mismo procedimiento de identificación y exige el mismo shape de dato para ambos** — no hay calificador de "opcional" ni "si lo tuviera" en ningún ítem de la lista, a diferencia de otras partes del mismo texto ordenado que sí marcan datos como opcionales cuando corresponde. Conclusión operativa: cuando un titular es "persona declarable" (residente fiscal en otra jurisdicción, sea por FATCA o por CRS), hace falta capturar — además del booleano de declaración — país/jurisdicción, NIF y domicilio fiscal de esa jurisdicción. Para FATCA la jurisdicción es siempre EE.UU. (no hace falta preguntarla); para OCDE puede haber más de una jurisdicción declarada (estructura array).

### De paso — el mismo texto ordenado ya respalda el punto 1.3 que el archivo canon sí cubre

El punto 1.3 ("Identificación y situación fiscal del titular", Sección 1 — Caja de ahorros) exige como mínimo: nombres y apellidos completos, **lugar y fecha de nacimiento**, domicilio, ocupación, estado civil y DDJJ de PEP/No PEP — coherente con lo ya documentado en el archivo canon, pero ahora con la cita textual exacta en vez de solo la síntesis de research. No exige domicilio/localidad de nacimiento, solo "lugar" (interpretado como país en el diseño de PRD-202, decisión explícita del PM de no pedir más detalle que el mínimo normativo — ver `1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/gaps.md`).

## Dónde ya se aplicó esto (a nivel proyecto, no canon)

El contrato de datos de PRD-202 (`personaFisica.declaracion.ocde`/`.fatca`, `personaFisica.personal.paisNacimiento`) ya implementa este hallazgo — ver `1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/artefactos/onboarding_consolidado-us.md` v7.2 y `decisiones.md`/`gaps.md` [2026-09-08]. Esta captura es para que el mismo hallazgo normativo quede también en el canon de referencia general (`3_recursos/cumplimiento_normativo/`), disponible para cualquier otro proyecto/PM que trabaje identificación de personas físicas — no solo para quien lea el gap puntual de esta IDEA.

## Qué NO se incluye acá (deliberado)

La estructura de detalle para "Sujeto Obligado ante la UIF" (`inciso`/`numeroInscripcionUIF`) que también se diseñó en PRD-202 **no** se propone para el canon — es una inferencia por analogía, sin una norma primaria leída línea por línea que la confirme (a diferencia de OCDE/FATCA, respaldado arriba con cita textual). Queda como diseño de proyecto (`gaps.md` [2026-09-08] (3)), pendiente de validar con Compliance/PLD antes de proponerlo como conocimiento canon.

## Sugerencia de aplicación en `/context_merge`

En `identificacion_personas_fisicas_cvu.md`: agregar un 4to ítem a la lista de §4 ("Cooperación tributaria internacional — OCDE/CRS + FATCA"), con su propia sub-sección de estructura de datos (mismo nivel de detalle que la matriz de domicilio de §2), citando BCRA "Depósitos de Ahorro...", punto 4.13.1.1 con el texto de arriba. Aprovechar el merge para subir la confianza declarada del archivo en los puntos que este texto primario ya confirma (1.3, 4.13.1.1) — el resto del documento sigue con la reserva de "no validado" que ya tenía.
