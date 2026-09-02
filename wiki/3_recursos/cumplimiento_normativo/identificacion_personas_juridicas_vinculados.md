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

## Relevancia para los proyectos de Onboarding de Bind PSP

No es contenido nuevo para el proyecto de PJ ya en curso, sino confirmación con base normativa citada: `1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md` ya registró (2026-08-20) que "beneficiarios finales confirmado cubierto por una US existente" y ya construye alta de representantes legales/apoderados con su propia validación de identidad (US-2/US-3/US-7). Esta matriz sirve como checklist de referencia si se quiere verificar formalmente ese diseño campo a campo (no hecho en la sesión que originó este documento — el contrato de datos detallado de ese proyecto no se comparó línea por línea, a diferencia de PRD-202/PF). Relevante también para **PRD-210** (Fase 3 — cuenta PJ del proyecto Onboarding Estratégico, hoy en horizonte "Más tarde", sin discovery de campos todavía) cuando se retome.

## Reglas transversales

Ver [`identificacion_personas_fisicas_cvu.md` §3](identificacion_personas_fisicas_cvu.md) para la excepción de tipping-off, las alertas de coherencia edad/capacidad (Art. 23) y la prohibición de anonimato — aplican de igual forma a la identificación de vinculados/beneficiarios finales de personas jurídicas.

## Ver también

- [identificacion_personas_fisicas_cvu.md](identificacion_personas_fisicas_cvu.md) — mismo research, requisitos para personas físicas.

---
*Creado: 2026-09-02 — `/context_merge`, desde research de Gemini deep research del PM (2026-09-01).*
