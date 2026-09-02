# Identificación de Personas Físicas — Marco Regulatorio para Altas de Cuenta CVU

> ⚠️ **Estado: orientación de diseño, no validado como ground truth de auditoría.** Contenido de una investigación hecha por el PM con Gemini (deep research, 2 rondas), citando fuentes públicas concretas (BCRA, Boletín Oficial/UIF, AFIP/ARCA) pero **no verificado línea por línea contra el texto vigente de cada Comunicación/Resolución por Compliance/PLD de Bind PSP**. Antes de tratarlo como ground truth para auditoría o para cerrar un gap de cumplimiento formal, corresponde una validación con Compliance/PLD (ver `1_proyectos/tareas.md` T-053). Se documenta igual porque, aun con esa reserva, es información de calidad suficiente para orientar el diseño de producto y detectar posibles brechas a confirmar.
>
> Fuente: research de Pablo Gomes con Gemini — "Normativa CVU PSP Argentina.md" (2026-09-01, panorama general BCRA/UIF/ARCA/AAIP) + "Mapeo Exhaustivo de Requisitos Regulatorios y Datos Obligatorios para CVU en Argentina.md" (2026-09-01, ronda más profunda, matriz de datos DDC de UIF y distinción legajo vs. reporte RSM) — ambas archivadas en `4_archivos/historial_raw/2026-09_normativa_cvu_pf_argentina/`.

## 1. Cuatro entes regulan la captura de datos en el alta de una cuenta CVU de persona física

La apertura de una cuenta de pago con CVU por parte de un PSPCP en Argentina no es una decisión libre de UX — está mandada por cuatro reguladores, cada uno con su propio foco:

- **BCRA** (Texto Ordenado de PSP + Comunicaciones "A" 6885, 6859, 7328, 7495, 8432): identificación unívoca previa a la apertura, vínculo biunívoco CVU↔CUIT/CUIL/CDI, y en materia de fraude (Com. "A" 7328) exige captura en tiempo real de DNI (frente y dorso) + prueba de vida biométrica, validados contra RENAPER. También exige aceptación explícita y registrada de las advertencias regulatorias (el PSP no es una entidad financiera, los fondos no tienen garantía de depósito bancario).
- **UIF** (Ley 25.246 + reforma Ley 27.739, Resolución UIF 200/2024 — reglamento específico del sector): exige un legajo digital único por titular con Debida Diligencia del Cliente (DDC) proporcional al riesgo (EBR — Bajo/Medio/Alto), datos identificatorios completos (ver matriz abajo), 3 declaraciones juradas obligatorias, y conservación de todo el legajo por **10 años** desde el cierre/desvinculación de la cuenta. Actualización periódica según riesgo: alto = anual, medio = cada 3 años, bajo = cada 5 años. Para riesgo medio/alto exige documentación de respaldo de ingresos/patrimonio (recibo de sueldo, Monotributo, certificación contable) — pero la **Resolución UIF 78/2025 prohíbe explícitamente exigir DDJJ impositivas** (Ganancias, Bienes Personales) para ese perfil, limitando la evaluación a documentación financiera/bancaria/comercial.
- **ARCA/AFIP** (RG 4614/2019): régimen informativo mensual obligatorio (nómina de titulares, saldos, ingresos/egresos). Exige validar el CUIT/CUIL/CDI contra el padrón público de ARCA y catalogar la condición fiscal (Consumidor Final/Monotributista/Responsable Inscripto/Exento) y jurisdicción, para aplicar correctamente regímenes de retención/percepción (ej. Sircreb).
- **AAIP** (Ley 25.326 de Protección de Datos Personales): la biometría facial es dato sensible — exige consentimiento libre/expreso/informado, base de datos inscripta en el Registro Nacional de Bases de Datos, y mecanismos de ejercicio de derechos ARCO — con la salvedad de que el derecho de supresión queda supeditado a los 10 años de conservación obligatoria de BCRA/UIF.

## 2. La distinción clave: Legajo (DDC) vs. Reporte (RSM)

Un campo puede ser condicional u opcional en el layout técnico del Reporte Sistemático Mensual (RSM) que se envía a la UIF, y aun así ser **"Obligatorio Absoluto" en el Legajo de Cliente** que el Sujeto Obligado debe mantener. La norma sustantiva de DDC es la exigencia de máxima — el RSM solo optimiza qué campos viajan en la ingesta masiva, no relaja qué hay que tener guardado.

### Matriz de domicilio real de persona humana

| Campo | Fuente | Legajo (DDC) | Reporte (RSM) |
|---|---|---|---|
| Calle y número | Art. 13 inc. e; Res. 200/2024 | Obligatorio Absoluto | Obligatorio Absoluto |
| Barrio | Res. 99/2023 art. 2 inc. ñ | Obligatorio Sectorial (según actividad) | Condicional |
| Localidad, provincia, país | Art. 13 inc. e; Res. 99/2023 | Obligatorio Absoluto | Obligatorio Absoluto |
| Código postal | Art. 13 inc. e; Res. 78/2023 | Obligatorio Absoluto | No obligatorio técnicamente |
| Teléfono y correo electrónico | Art. 13 inc. f | Obligatorio Absoluto | Condicional |
| Actividad laboral/profesional | Art. 13 inc. g | Obligatorio Absoluto | Condicional |
| Condición de PEP | Art. 13 inc. h; Res. 200/2024 | Obligatorio Absoluto | Obligatorio Absoluto |

**No se menciona explícitamente "piso"/"departamento" para persona humana** en ninguna de las 2 rondas de investigación (sí aparece como campo "Condicional" en la matriz de persona jurídica, ver [`identificacion_personas_juridicas_vinculados.md`](identificacion_personas_juridicas_vinculados.md) — condicionado a que la propiedad tenga esa subdivisión). Punto a confirmar con Compliance si aplica igual al domicilio real de una persona física.

**Ejemplo directamente relevante para el diseño de producto:** el teléfono y correo electrónico son "Obligatorio Absoluto" en el legajo (Art. 13 inc. f) y solo "Condicional" en el RSM — relevante para el gap ya abierto en `1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/gaps.md` sobre contacto condicionado a una palanca de OTP: la norma no lo condiciona.

## 3. Reglas transversales de DDC (condicionan el diseño de monitoreo/onboarding, no son campos de captura)

- **Excepción de tipping-off:** si el Sujeto Obligado sospecha LA/FT/FP y entiende que completar la DDC (pedir documentación adicional, contactar al cliente) alertaría al sospechoso, puede abstenerse de completar el proceso de DDC — siempre que formule de inmediato el ROS correspondiente ante la UIF.
- **Alertas de incoherencia edad/capacidad (Art. 23 DDC):** exige configurar alertas automáticas cuando el volumen/patrón de operación no es coherente con la edad o capacidad del cliente — casos explícitos: menores de edad con volúmenes no justificables por patrimonio heredado/cedido, personas con dificultad para comprender actos jurídicos o de edad avanzada con movimientos atípicos, y terceros operando cuentas de personas vulnerables sin respaldo documental de tutela/curatela/mandato. **Relevante directo para PRD-211** (Fase 2 — cuenta PF menor de edad, hoy en horizonte "Más tarde"): la norma exige tanto el vínculo formal con el tutor/representante como el monitoreo continuo de coherencia edad-volumen, no solo la validación de identidad en el alta.
- **Prohibición de anonimato:** bajo ningún concepto se admite dar de alta clientes con nombres falsos o anónimos.

## 4. Las 3 declaraciones juradas obligatorias en el onboarding

1. **PEP** (Persona Expuesta Políticamente) — Resolución UIF 35/2023 — checkbox que, ante respuesta afirmativa, abre un formulario de detalle.
2. **Sujeto Obligado ante la UIF** — art. 20 Ley 25.246 — checkbox con confirmación explícita.
3. **Origen y licitud de los fondos** — aceptación de cláusula legal integrada al flujo.

## 5. Matriz de datos a capturar (síntesis)

| Categoría | Campo | Mecanismo esperado | Conservación |
|---|---|---|---|
| Identificación | Nombre/apellido completos, tipo y N° de documento | OCR/PDF417 de DNI, cotejo RENAPER | 10 años posdesvinculación |
| Fiscal | CUIT/CUIL/CDI | Verificación en tiempo real contra padrón ARCA, vínculo biunívoco a CVU | 10 años |
| Demográfico | Fecha de nacimiento, nacionalidad, estado civil | Extracción de DNI + RENAPER (nacimiento/nacionalidad); DDJJ manifestada (estado civil) | 10 años |
| Contacto | Email y celular | Verificación activa por OTP (SMS / link) | 10 años |
| Domicilio real | Calle, número, barrio (sectorial), localidad, provincia, CP, país | Formulario estructurado, cotejo contra DNI/comprobante | 10 años |
| Biometría | Selfie/prueba de vida interactiva | Liveness + RENAPER | 10 años (evidencia) |
| Perfil económico | Ocupación/profesión/actividad | Selección de catálogo estandarizado | 10 años |
| DDJJ | PEP, Sujeto Obligado, Origen y licitud de fondos | Checkboxes + formulario de detalle si PEP=sí | 10 años |
| Respaldo de ingresos | Documentación probatoria (solo riesgo Medio/Alto) | Carga de archivo — nunca DDJJ impositiva | Exigible según matriz de riesgo |
| Consentimiento | T&C, leyenda BCRA (no es entidad financiera, sin garantía de depósito), política de privacidad | Checkbox firmado con log de IP/timestamp | 10 años |

## 6. Trazabilidad y seguridad exigidas (transversal)

Cada interacción del flujo de alta debe generar un audit trail con timestamp UTC, IP pública, user-agent, device ID y las respuestas de las APIs de RENAPER/validación tributaria. Firma digital + sellado de tiempo (Ley 25.506) sobre documentos/DDJJ aceptados. Cifrado AES-256 en reposo y TLS 1.3 en tránsito.

## 7. Nota operativa (confianza baja) — mención suelta de requisitos regulatorios 2024

En la reunión "Weekly - Producto / Operaciones" (2026-08-31) se mencionó, sin más contexto (norma de origen, fecha límite), la obligación de capturar el domicilio real en el alta de cuenta — coincide con lo documentado en §2 arriba — y una necesidad adicional no cubierta acá: **consultar la actividad ante AFIP durante las altas en wallets**. Ver [`wallet/validaciones_y_alias_cvu.md` §3](../detalle_productos/wallet/validaciones_y_alias_cvu.md) para el registro completo de esa mención suelta.

## Por qué se documenta — relevancia directa para Onboarding Estratégico

Este es el mandato que originó [`proyecto-onboarding-estrategico`](../../1_proyectos/proyecto-onboarding-estrategico/proyecto.md) (post-fraude marzo 2026, auditoría del grupo BIND). Al comparar esta matriz contra el contrato de datos ya diseñado de PRD-202 (`POST /cuenta/kyc`), se detectaron brechas puntuales — documentadas como gaps específicos de esa IDEA, no acá: ver `1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/gaps.md`, entrada 2026-09-01.

## Ver también

- [identificacion_personas_juridicas_vinculados.md](identificacion_personas_juridicas_vinculados.md) — mismo research, requisitos para personas jurídicas, FCI/Fideicomisos y sujetos vinculados/beneficiario final.
- [limites_operativos_uif_ros.md](limites_operativos_uif_ros.md) — topes operativos UIF/ROS, tema complementario no contradictorio.
- [reporteria_worldsys_bcra.md](reporteria_worldsys_bcra.md) — informe diario a Worldsys/BCRA, tema complementario.

---
*Creado: 2026-09-02 — `/context_merge`, desde research de Gemini deep research del PM (2026-09-01).*
