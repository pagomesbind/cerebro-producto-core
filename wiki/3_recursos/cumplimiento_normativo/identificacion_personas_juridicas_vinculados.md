# Identificación de Personas Jurídicas, Vehículos Colectivos y Sujetos Vinculados

> ⚠️ **Estado: orientación de diseño, no validado como ground truth de auditoría.** Misma reserva que [`identificacion_personas_fisicas_cvu.md`](identificacion_personas_fisicas_cvu.md): investigación de IA (Gemini deep research) con citas públicas, no validada línea por línea por Compliance/Legales de Bind PSP todavía. Tratar como orientación de diseño hasta esa validación (ver `1_proyectos/tareas.md` T-053).
>
> Fuente: research de Pablo Gomes con Gemini (deep research) — "Mapeo Exhaustivo de Requisitos Regulatorios y Datos Obligatorios para CVU en Argentina.md", 2026-09-01, archivado en `4_archivos/historial_raw/2026-09_normativa_cvu_pf_argentina/`.

## Resumen — la UIF exige desagregar "quién es el cliente" de "quién controla/representa al cliente"

Para personas jurídicas, Fondos Comunes de Inversión (FCI) y Fideicomisos, la Resolución UIF 78/2023 (Reportes Sistemáticos Mensuales de Cuentas Comitentes y FCI) exige no solo los datos propios de la entidad, sino la identificación de un conjunto de personas humanas vinculadas — el ordenamiento regulatorio argentino proscribe el anonimato indirecto mediante estas obligaciones. Igual que para personas físicas, hay distinción entre lo exigible en el **Legajo de Cliente (DDC)** y lo exigible en el **layout técnico del RSM** — el legajo es siempre la exigencia de máxima; el RSM puede marcar campos como opcionales por eficiencia de ingesta masiva sin relajar la obligación de tenerlos en el legajo.

## Matriz de datos obligatorios — persona jurídica

| Campo | Legajo (DDC) | Reporte (RSM, Res. 78/2023) | Nota |
|---|---|---|---|
| Tipo de persona | Obligatorio Absoluto | Obligatorio Absoluto | Selección taxativa "Persona Jurídica" |
| Denominación social | Obligatorio Absoluto | Obligatorio Absoluto | Razón social o nombre del vehículo colectivo |
| CUIT/CUIL/CDI/CIE | Obligatorio Absoluto | No obligatorio técnicamente | Formato numérico corrido, sin guiones, si se informa en el RSM |
| Fecha de constitución | Obligatorio Absoluto | No obligatorio técnicamente | Fecha del instrumento de constitución legal |
| Riesgo asignado al cliente | Obligatorio Absoluto | No obligatorio técnicamente | Escala de 5 niveles (Bajo/Medio bajo/Medio/Medio alto/Alto), Res. 21/2018 |
| Domicilio (sede/legal) | Obligatorio Absoluto | Obligatorio Absoluto | Calle, número, localidad, provincia |
| Piso y departamento | Condicional | Condicional | Solo si la propiedad tiene esa subdivisión |

**La asimetría es deliberada, no un error de diseño de reporte:** que el CUIT, la fecha de constitución o el riesgo asignado sean opcionales en el layout RSM no los vuelve opcionales en el legajo — la ausencia de esos datos en el legajo físico/digital del Sujeto Obligado es infracción directa a las reglas de identificación y verificación, aunque el envío mensual a la UIF no se bloquee por faltarlos.

## Sujetos vinculados de carga obligatoria (Res. 78/2023 — cuentas comitentes, FCI, Fideicomisos)

Personas humanas que deben quedar identificadas indefectiblemente, más allá de la propia entidad:

- **Participantes de constitución/organización:** al menos una Persona Humana (o Persona Humana Extranjera) como participante en la constitución/organización del FCI o Fideicomiso.
- **Órganos de administración/fiduciarios:** al menos una Persona Humana como Fiduciario o Administrador.
- **Condóminos de cuentas comitentes:** identificación de la totalidad de personas humanas que sean condóminas de la cuenta.
- **Representantes/garantías:** identificación completa de todo Apoderado, Tutor, Curador, Representante Legal o Garante del titular o de los condóminos.

## Beneficiario final

Definido como la persona humana que posee la titularidad o el control efectivo de la entidad/estructura. Sobre todo Beneficiario Final, representante o participante vinculado recae la obligación de aplicar DDC completa — incluida la verificación de su **domicilio real** (calle, número, localidad, provincia, país, CP) y la constatación de su condición de PEP (Res. UIF 200/2024).

## Checklist interno de Bind PSP — documentación exigida por tipo societario (Resolución UIF 200/2024)

> ⚠️ Confianza media. Fuente: documento interno de Bind PSP (`raw/req segun UIF 200-24.pdf`, sin autor visible) titulado "Requisitos alta de cuentas conforme la Resolución Uniforme 200/24", contrastado contra el texto oficial de la Resolución UIF 200/2024 (Boletín Oficial, aviso 318446 del 19/12/2024: RESOL-2024-200-APN-UIF#MJ). Más granular que la matriz de arriba (research de Gemini deep research): desagrega la documentación societaria exigida **por tipo de sociedad**, algo que ningún otro archivo de este Cerebro tenía hasta ahora en un solo lugar. Complementa (sin contradecir) [`detalle_productos/onboarding/onboarding_personas_juridicas.md`](../detalle_productos/onboarding/onboarding_personas_juridicas.md), que ya documenta un sistema de Onboarding PJ en producción con "documentación requerida variable por tipo de sociedad" pero sin ese detalle desagregado.

### Datos generales exigidos (checklist interno)

- Denominación o razón social.
- Fecha y número de inscripción registral.
- CUIT, CDI o Clave de Inversores del Exterior (CIE), o la que en el futuro cree ARCA (equivalente para extranjeros).
- Domicilio legal y domicilio comercial (calle, número, localidad, provincia, país, código postal).
- Domicilio electrónico (art. 75 CCyC).
- Actividad principal realizada.
- Identificación de los integrantes del órgano de administración u órgano equivalente, representantes legales y/o apoderados — con las mismas reglas de identificación que persona humana.
- Identificación de propietarios directos y/o beneficiarios finales, con verificación de identidad — **excepción documentada:** si la titularidad del capital social presenta alto nivel de atomización, se tiene por cumplido identificando a los integrantes del órgano de administración/equivalente y/o a quienes ejerzan el control efectivo, sin necesidad de identificar a cada accionista disperso.

### Documentación por tipo societario

Todos los tipos, salvo donde se indica lo contrario, exigen: instrumento constitutivo/estatuto/contrato social con certificación notarial (Requerido); constancia de inscripción registral correspondiente (Requerido); acta de designación de autoridades vigentes (Requerido); certificación notarial y/o inscripción registral de esa acta (Requerido); modificaciones al estatuto con constancia de inscripción registral (Opcional); poderes generales amplios de apoderados (Requerido).

| Tipo societario | Particularidad respecto del patrón general |
|---|---|
| Sociedad Anónima (S.A.) | Patrón general, sin variantes. |
| Sociedad de Responsabilidad Limitada (S.R.L.) | Patrón general, sin variantes. |
| Sociedad por Acciones Simplificada (S.A.S.) | Patrón general, sin variantes. |
| Sociedad de Hecho (S.H.) | **No pide estatuto formal** — en su lugar: "Contrato Social o Nota donde indiquen cómo es el Régimen de firmas de la sociedad", certificado ante Escribano Público (Requerido) + constancia de AFIP (Requerido) + poderes (Requerido). Es el tipo con menos formalidad documental de todos. |
| Sociedad Capítulo I Sección IV (sociedades no constituidas regularmente, LGS) | Contrato social con firmas certificadas ante Escribano Público (Requerido, sin exigir inscripción registral como los tipos formales) + modificaciones posteriores con certificación notarial (Opcional) + poderes (Requerido). **No mencionado en ningún otro archivo relevado de este Cerebro.** |
| Asociaciones y Fundaciones | Constancia de otorgamiento de la **personería jurídica** (en vez de inscripción registral mercantil) — resto igual al patrón general. |
| Cooperativas | Constancia de inscripción ante el **INAES** y autorización para funcionar (en vez de Registro Público) — resto igual al patrón general. **No mencionado en ningún otro archivo relevado de este Cerebro.** |
| Sociedades en Comandita Simple (S.C.S.) | Patrón general, sin variantes. **No mencionado en ningún otro archivo relevado de este Cerebro.** |
| Sociedades en Comandita por Acciones (S.C.A.) | Patrón general, sin variantes. |

### Documentación y validaciones transversales a toda persona jurídica

- Mail de contacto + OTP de validación (sobre el domicilio electrónico de la sociedad).
- DDJJ Sujeto Obligado (SO).
- DDJJ FATCA y **DDJJ OCDE** (dos declaraciones distintas).
- DDJJ de declaración de Propietarios Directos y/o Beneficiarios Finales.
- Identificación de identidad de Propietarios Directos y/o Beneficiarios Finales, si existieran.
- Aceptación de términos y condiciones.
- Validación de listas y consulta a servicios externos (ARCA, Nosis).
- **Validación de identidad (Onboarding de Persona Física) de al menos UNA persona humana que opere en representación de la sociedad** (Representante Legal y/o Apoderados) — coincide con la regla de negocio ya confirmada para el sistema PJ en producción ("la PJ se aprueba con al menos uno aprobado, no todos los representantes").

### Dato de confianza baja, sin confirmar contra fuente primaria

Un segundo documento aportado (`raw/Informe_Requisitos_CVU_Argentina.pdf`) — sin membrete oficial, con características de síntesis de terceros/IA más que de texto normativo primario — menciona que la Declaración Jurada de Beneficiarios Finales para personas jurídicas aplica a "personas físicas que posean el **10% o más del capital social o derechos de voto**". Es un dato verosímil (umbral típico en normativa PLAFT regional) pero **no confirmado contra una fuente primaria de UIF/BCRA** — queda anotado como pista a verificar formalmente antes de usarlo en diseño, no como dato ya validado. El mismo documento contiene 2 afirmaciones ya descartadas por contradecir fuentes primarias confirmadas (cita "Resolución UIF 76/2019" en vez de la vigente 200/2024; cita "Com. 'A' 6588" para la CVU en vez de 6510/7533) — no incorporadas al canon.

### Qué queda pendiente, explícitamente fuera de esta captura

No se comparó este checklist campo a campo contra el diseño ya en producción de `onboarding_personas_juridicas.md` ni contra `proyecto-la-virginia-ob-pj` — sería el paso siguiente natural si se decide invertir en verificar formalmente esa cobertura, o si se retoma PRD-210.

## Relevancia para los proyectos de Onboarding de Bind PSP

No es contenido nuevo para el proyecto de PJ ya en curso, sino confirmación con base normativa citada: `1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md` ya registró (2026-08-20) que "beneficiarios finales confirmado cubierto por una US existente" y ya construye alta de representantes legales/apoderados con su propia validación de identidad (US-2/US-3/US-7). Esta matriz sirve como checklist de referencia si se quiere verificar formalmente ese diseño campo a campo (no hecho en la sesión que originó este documento — el contrato de datos detallado de ese proyecto no se comparó línea por línea, a diferencia de PRD-202/PF). Relevante también para **PRD-210** (Fase 3 — cuenta PJ del proyecto Onboarding Estratégico, hoy en horizonte "Más tarde", sin discovery de campos todavía) cuando se retome.

## Reglas transversales

Ver [`identificacion_personas_fisicas_cvu.md` §3](identificacion_personas_fisicas_cvu.md) para la excepción de tipping-off, las alertas de coherencia edad/capacidad (Art. 23) y la prohibición de anonimato — aplican de igual forma a la identificación de vinculados/beneficiarios finales de personas jurídicas.

## Ver también

- [identificacion_personas_fisicas_cvu.md](identificacion_personas_fisicas_cvu.md) — mismo research, requisitos para personas físicas.

---
*Última actualización: 2026-09-08 — `/context_merge`: nueva sección de checklist interno de documentación por tipo societario (Res. UIF 200/2024), desde auditoría de cumplimiento normativo del PM.*
*Creado: 2026-09-02 — `/context_merge`, desde research de Gemini deep research del PM (2026-09-01).*
