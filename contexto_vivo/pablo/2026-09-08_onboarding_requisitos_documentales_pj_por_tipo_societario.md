---
id: 2026-09-08_onboarding_requisitos_documentales_pj_por_tipo_societario
pm: pablo
fecha_captura: 2026-09-08
fuente: "Documento interno de Bind PSP (`raw/req segun UIF 200-24.pdf`, sin autor visible en el PDF, aportado por el usuario) titulado 'Requisitos alta de cuentas conforme la Resolución Uniforme 200/24' — checklist operativo de datos y documentación por tipo de persona/sociedad. Contrastado contra el texto oficial de la Resolución UIF 200/2024 (confirmado vía Boletín Oficial, aviso 318446 del 19/12/2024: RESOL-2024-200-APN-UIF#MJ) y contra el estado actual del Cerebro sobre Onboarding de personas jurídicas."
producto: onboarding
tema: Checklist interno de Bind PSP de documentación exigida para alta de personas jurídicas, desagregado por tipo societario (SA, SRL, SAS, SH, Capítulo I Sección IV, Asociaciones/Fundaciones, Cooperativas, SCS, SCA)
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/identificacion_personas_juridicas_vinculados.md
tipo_destino: actualizar
contradice: "no — complementa identificacion_personas_juridicas_vinculados.md (2026-09-01), que ya cubre el marco general UIF de personas jurídicas/vinculados/beneficiario final pero sin desagregar por tipo societario. También complementa (sin contradecir) el hallazgo del sub-agente de exploración de esta misma sesión: ya existe un sistema de Onboarding PJ en producción (`3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md`) que cubre SA/SRL/SAS/S.C.A./S.H./Asociación/Fundación con 'documentación requerida variable por tipo de sociedad' — este item aporta el detalle documental exacto por tipo que ese archivo de producto no desagrega, y agrega 2 tipos societarios que no aparecían mencionados en ningún archivo relevado (Sociedad Capítulo I Sección IV, Sociedades en Comandita Simple)."
confianza: media
estado: en_cola
merge_commit:
---

## Contexto — por qué se captura

El usuario pidió auditar si el proyecto `proyecto-onboarding-estrategico` cumple con la normativa de apertura de cuentas CVU, aportando dos documentos de `raw/`: el texto ordenado BCRA "Sistema Nacional de Pagos – Servicios de Pago" y este checklist interno de Bind PSP sobre la Resolución UIF 200/2024. El checklist interno es más granular que la investigación regulatoria ya en canon (`identificacion_personas_juridicas_vinculados.md`, de una sesión anterior con Gemini deep research): desagrega la documentación societaria exigida **por tipo de sociedad**, algo que ningún archivo de este Cerebro tenía hasta ahora en un solo lugar.

Relevancia directa: dentro de `proyecto-onboarding-estrategico`, **PRD-210** ("Fase 3 — cuenta PJ") es hoy un placeholder puro sin campos definidos (confirmado por exploración de esta sesión — no tiene `gaps.md` ni `decisiones.md`, horizonte "Más tarde", ~0,1% del volumen). Existe además, **fuera** de ese proyecto, un sistema de Onboarding PJ ya en producción y un proyecto de cliente puntual (`1_proyectos/proyecto-la-virginia-ob-pj/`) que ya resuelven buena parte de esto — este item no reemplaza ese trabajo, lo complementa como checklist de referencia para cuando PRD-210 se retome o para verificar el diseño ya existente campo a campo (verificación que, según el propio Cerebro, **todavía no se hizo** línea por línea).

## Personas físicas — sin novedad de fondo

El checklist interno confirma, para personas físicas, el mismo set ya extensamente trabajado en `identificacion_personas_fisicas_cvu.md` y en el contrato de PRD-202 (nombre/apellido, tipo y N° de documento, nacionalidad/fecha de nacimiento, estado civil, CUIL/CUIT/CDI, domicilio real, domicilio electrónico —art. 75 CCyC—, actividad laboral, PEP) más la documentación operativa (DNI frente/dorso, selfie, prueba de vida, Renaper datos, Renaper rostro, mail/teléfono con OTP, DDJJ PEP, aceptación T&C, validación de listas/Nosis/ARCA) — todo esto ya tiene mecanismo de captura confirmado en PRD-202 (ver `prd-202_onboarding_consolidado/artefactos/2026-09-01_matriz_cumplimiento_normativo_pf.md`). **Única novedad real para PF, ya registrada como gap separado en `prd-202_onboarding_consolidado/gaps.md` (2026-09-08):** el checklist agrega explícitamente **"DDJJ FATCA" y "DDJJ OCDE"** como dos declaraciones distintas — el contrato de PRD-202 solo tiene `esFacta`/`esUif`/`esPep`, sin campo de OCDE/CRS.

## Personas jurídicas — datos generales exigidos (Art. 20 aprox., checklist interno)

- Denominación o razón social.
- Fecha y número de inscripción registral.
- CUIT, CDI o Clave de Inversores del Exterior (CIE), o la que en el futuro cree ARCA (equivalente para extranjeros).
- Domicilio legal (calle, número, localidad, provincia, país, código postal).
- Domicilio comercial (mismo desagregado).
- Domicilio electrónico (art. 75 CCyC).
- Actividad principal realizada.
- Identificación de los integrantes del órgano de administración u órgano equivalente, representantes legales y/o apoderados — con las mismas reglas de identificación que persona humana.
- Identificación de propietarios directos y/o beneficiarios finales, con verificación de identidad — **excepción documentada:** si la titularidad del capital social presenta alto nivel de atomización, se tiene por cumplido identificando a los integrantes del órgano de administración/equivalente y/o a quienes ejerzan el control efectivo, sin necesidad de identificar a cada accionista disperso.
- Cumplimiento de la normativa UIF de PEP (extendida a beneficiarios finales) y de prevención de financiamiento del terrorismo.

## Documentación por tipo societario — la parte no cubierta hasta ahora en ningún archivo de este Cerebro

Todos los tipos, salvo donde se indica lo contrario, exigen: instrumento constitutivo/estatuto/contrato social con certificación notarial (Requerido); constancia de inscripción registral correspondiente (Requerido); acta de designación de autoridades vigentes (Requerido); certificación notarial y/o inscripción registral de esa acta (Requerido); modificaciones al estatuto con constancia de inscripción registral (Opcional); poderes generales amplios de apoderados (Requerido).

| Tipo societario | Particularidad respecto del patrón general |
|---|---|
| Sociedad Anónima (S.A.) | Patrón general, sin variantes. |
| Sociedad de Responsabilidad Limitada (S.R.L.) | Patrón general, sin variantes. |
| Sociedad por Acciones Simplificada (S.A.S.) | Patrón general, sin variantes. |
| Sociedad de Hecho (S.H.) | **No pide estatuto formal** — en su lugar: "Contrato Social o Nota donde indiquen cómo es el Régimen de firmas de la sociedad", certificado ante Escribano Público (Requerido) + constancia de AFIP (Requerido) + poderes (Requerido). Es el tipo con menos formalidad documental de todos. |
| Sociedad Capítulo I Sección IV (sociedades no constituidas regularmente, LGS) | Contrato social con firmas certificadas ante Escribano Público (Requerido, sin exigir inscripción registral como los tipos formales) + modificaciones posteriores con certificación notarial (Opcional) + poderes (Requerido). **Tipo societario no mencionado en ningún otro archivo relevado de este Cerebro** (ni en `identificacion_personas_juridicas_vinculados.md` ni en `onboarding_personas_juridicas.md`). |
| Asociaciones y Fundaciones | Constancia de otorgamiento de la **personería jurídica** (en vez de inscripción registral mercantil) — resto igual al patrón general. |
| Cooperativas | Constancia de inscripción ante el **INAES** y autorización para funcionar (en vez de Registro Público) — resto igual al patrón general. **Tipo societario no mencionado en ningún otro archivo relevado de este Cerebro.** |
| Sociedades en Comandita Simple (S.C.S.) | Patrón general, sin variantes. **Tipo societario no mencionado en ningún otro archivo relevado de este Cerebro.** |
| Sociedades en Comandita por Acciones (S.C.A.) | Patrón general, sin variantes. |

## Documentación y validaciones transversales a toda persona jurídica (checklist interno, sección final)

- Mail de contacto + OTP de validación (sobre el domicilio electrónico de la sociedad).
- DDJJ Sujeto Obligado (SO).
- DDJJ FATCA.
- **DDJJ OCDE** — mismo campo ausente que en persona física, ver gap en `prd-202_onboarding_consolidado/gaps.md`.
- DDJJ de declaración de Propietarios Directos y/o Beneficiarios Finales.
- Identificación de identidad de Propietarios Directos y/o Beneficiarios Finales, si existieran.
- Aceptación de términos y condiciones.
- Validación de listas y consulta a servicios externos (ARCA, Nosis).
- **Validación de identidad (Onboarding de Persona Física) de al menos UNA persona humana que opere en representación de la sociedad** (Representante Legal y/o Apoderados) — coincide con la regla de negocio ya confirmada por el sub-agente de exploración para el sistema PJ en producción ("la PJ se aprueba con al menos uno aprobado, no todos los representantes").

## Addendum (2026-09-08, 2ª ronda) — umbral de beneficiario final, con reserva de confianza

El usuario aportó un segundo documento (`raw/Informe_Requisitos_CVU_Argentina.pdf`, "Informe Técnico y Regulatorio", sin membrete oficial ni número de comunicación verificable — a diferencia de los PDF de BCRA escaneados con formato oficial ya procesados esta sesión, este tiene todas las características de un informe de síntesis de terceros o generado por IA, no un texto normativo primario). Se marca **confianza baja** para todo su contenido, y se detectaron 2 inconsistencias concretas contra fuentes primarias ya confirmadas esta sesión: cita "Resolución UIF 76/2019" como la norma vigente de DDC para PSP, cuando el Boletín Oficial (aviso 318446) confirma que la vigente es la **Resolución UIF 200/2024** (76/2019 podría ser una resolución anterior derogada, o directamente un dato inventado); y describe la conformación técnica de la CVU citando "Com. 'A' 6588", que no coincide con el origen real de esa sección según la tabla de correlaciones del texto ordenado BCRA ya leído directamente esta sesión (Sección 2.3 proviene de Com. "A" 6510/7533, no 6588). Ninguna de las dos afirmaciones se incorpora al canon.

Lo único potencialmente útil y no visto hasta ahora en ninguna fuente primaria de este Cerebro: el informe menciona que la Declaración Jurada de Beneficiarios Finales para personas jurídicas aplica a "personas físicas que posean el **10% o más del capital social o derechos de voto**". Es un dato verosímil (el umbral típico usado en normativa PLAFT de la región suele rondar ese valor), pero **no confirmado contra una fuente primaria de UIF/BCRA** — se deja anotado acá como pista a verificar formalmente antes de usarlo en el diseño de PRD-210, no como dato ya validado.

## Qué queda pendiente, explícitamente fuera de esta captura

No se comparó este checklist campo a campo contra el diseño ya en producción de `onboarding_personas_juridicas.md` ni contra `proyecto-la-virginia-ob-pj` (mismo criterio de cautela que dejó `identificacion_personas_juridicas_vinculados.md` el 2026-09-01) — sería el paso siguiente natural si se decide invertir en verificar formalmente esa cobertura, o si se retoma PRD-210.
