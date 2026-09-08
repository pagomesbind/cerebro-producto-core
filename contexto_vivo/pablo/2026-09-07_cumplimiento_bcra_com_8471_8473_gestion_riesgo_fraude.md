---
id: 2026-09-07_cumplimiento_bcra_com_8471_8473_gestion_riesgo_fraude
pm: pablo
fecha_captura: 2026-09-07
fuente: "Mail de la Cámara Argentina Fintech (Mariano Giraffa, 2026-09-03) + PDF Comunicación 'A' 8473 (BCRA, 03/09/2026) + reunión CAF 'Encuentro informativo Socios - Com. A 8471' (2026-09-04, screenshots + transcripción) + documento de análisis legal de la Cámara sobre la 8471 (agosto 2026) — todo procesado en el discovery de 1_proyectos/gestion_riesgo_fraude/"
producto: transversal
tema: Dos comunicaciones BCRA de prevención de fraude que alcanzan a Bind PSP como PSPCP
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/gestion_riesgo_fraude_bcra.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d783db8
---

## Qué son las dos normas

El BCRA publicó dos comunicaciones complementarias de prevención de fraude, del mismo paquete regulatorio:

- **Com. "A" 8471** (27/08/2026) — incorpora la gestión del riesgo de fraude como un "ambiente de control autónomo" (antes era parte del riesgo operacional general) y extiende **toda la Sección 6 "Gestión del riesgo operacional"** del Texto Ordenado de Lineamientos (hoy exigida solo a entidades financieras) a los **PSPCP** (Proveedores de Servicios de Pago que ofrecen Cuentas de Pago), en igualdad de condiciones. Para los PSP que no ofrecen cuentas de pago, la exigencia es un subconjunto acotado de 4 obligaciones (función específica, autoevaluación, plan de mitigación, tecnología/seguridad), vigente desde el 01/01/2027 sin implementación por etapas.
- **Com. "A" 8473** (03/09/2026) — establece que el BCRA suministra mensualmente información de personas humanas al administrador del esquema de transferencias inmediatas (la Cámara no confirmó el nombre en la reunión, pero Coelsa es la hipótesis de mayor peso), quien elabora un **score de riesgo de fraude por CUIL/CUIT** y lo distribuye sin costo a entidades financieras y PSPCP (archivo mensual + API). Es obligatorio **usar** el score (no decidir automáticamente en base a él) en 3 procesos: altas de nuevos clientes, monitoreo transaccional (ordenante y receptor), y revisión periódica del padrón de titulares para recategorizar riesgo.

## A quién alcanza y con qué régimen

Bind PSP es **PSPCP** (tiene licencia de PSP del BCRA y ofrece cuentas de pago — CVU — vía Wallet) y también **PSPCP como Servicio** — ambas categorías comparten el mismo cronograma y el mismo régimen pleno de la Sección 6, equivalente al de las entidades financieras. Un socio de la Cámara preguntó en la reunión si, siendo PSPCP y PSP a la vez, aplica el calendario más corto del régimen acotado — la respuesta confirmada en la reunión es que **no**: el régimen de PSPCP es el techo regulatorio, cumplirlo satisface cualquier obligación menor de otros roles (aceptador/agregador), sin necesidad de duplicar estructura — basta con que la matriz de riesgo de PSPCP incorpore los riesgos de esas otras actividades.

## Cronograma para Bind (PSPCP) — Com. "A" 8471

| Etapa | Ventana | Contenido |
|---|---|---|
| (A) | 01/09/2026 – 31/12/2026 | Marco, estructura, roles, apetito de riesgo, designación de responsable, riesgos preliminares |
| (B) | 01/01/2027 – 31/05/2027 | Documentación de procesos para identificar/evaluar/controlar/mitigar riesgos en procesos críticos |
| (C) | 01/06/2027 – 31/08/2027 | Autoevaluación + informe final (con auditoría externa) |
| (D) | desde 01/09/2027 | Vigencia plena |

Reportes de avance a la SEFYC en las dos primeras etapas; informe final suscripto por la máxima autoridad + informe de auditor externo al cierre de la tercera.

La Com. "A" 8473 no tiene fecha límite dura confirmada para Bind todavía: el plazo (60 días para altas/revisión de padrón, 90 días para monitoreo transaccional) corre desde que el administrador del esquema entregue documentación técnica, y ese administrador tiene hasta el 2027-01-01 para hacerlo.

## Contenido mínimo exigido del programa antifraude (8471)

Programa documentado (prevención/detección/respuesta/resolución/aprendizaje); función específica con responsable designado; procedimientos de detección/monitoreo tecnológico; canales de denuncia + plan de respuesta; capacitación de personal y concientización de clientes; **reporte trimestral al Directorio**; base de datos única de casos con trazabilidad; mecanismos de reporte/consulta a la Central de Prevención de Fraude (CPF); comunicación a la SEFYC de nuevas modalidades detectadas; revisión anual con intervención de auditoría interna.

## Implicancias de diseño relevantes para cualquier producto que use el score o reglas de fraude

- El score **no es determinístico** — es obligatorio recibirlo/considerarlo, no aprobar/rechazar automáticamente en base a él. El riesgo legal está en los dos extremos: ignorarlo si después hay un fraude que señalaba, o aplicarlo ciego y asumir la responsabilidad si se equivocó (el BCRA se desliga: "es solo una herramienta").
- **Riesgo de falsos positivos por asociación** (documento de la Cámara, §5.3): compartir domicilio/dispositivo/beneficiario con una cuenta involucrada en fraude es indicio, no prueba, de participación de todos los vinculados. Cualquier motor de reglas debe diferenciar señal de alerta vs. atribución definitiva, prever revisión humana para decisiones de mayor impacto, permitir actualizar/rectificar datos, y evitar resultados discriminatorios o desproporcionados — especialmente cuando el perfil determina bloqueo/restricción/cierre de cuenta.
- **Base centralizada de denuncias/casos** — exige categorías claras (alertas técnicas, reclamos de usuarios, incidentes confirmados operativamente, fraudes presuntos, fraudes confirmados por investigación interna, denuncias penales, imputaciones/condenas) para no funcionar como una "lista negra" interna de facto; debe registrar fuente/fecha, confiabilidad, estado de revisión, quién accedió/modificó, plazos de conservación y reglas para terceros vinculados sin haber participado.
- **Exposición legal real:** los reportes trimestrales al Directorio generan trazabilidad de "qué se sabía y qué se aceptó" — si se detecta una modalidad de fraude, se documenta, y no se logra frenarla a tiempo, esa misma documentación puede convertirse en evidencia de responsabilidad civil, comercial o penal (dolo eventual). Aplica directo al patrón del incidente de fraude de Bind de marzo 2026 (Transferencias Pull, ~$11.500M, personas físicas — mismo universo que cubre el score de la 8473).
- **Principio de proporcionalidad explícito en la norma** — las disposiciones deben aplicarse de forma proporcional a la dimensión y complejidad operativa de cada empresa; Bind no tiene por qué construir el mismo programa que un banco grande.
- **Alcance más amplio que fraude a clientes** — la Sección 6 cubre también fraude interno (empleados) y ataques externos (seguridad de la información), no solo fraude transaccional/de clientes.

## Por qué importa para Ardid / monitoreo transaccional

El acápite de monitoreo transaccional de la 8473, y buena parte de los "procedimientos de detección/monitoreo tecnológico" que exige la 8471, encajan naturalmente en **Ardid** (el motor de antifraude/monitoreo transaccional ya en producción, con su propio scoring) — no en Onboarding. Cualquier trabajo de Ardid que toque reglas de bloqueo/restricción de cuenta debería considerar el requisito de revisión humana y anti-discriminación de la 8471 §5.3 desde el diseño.

## Fuente completa del discovery

Ver `1_proyectos/gestion_riesgo_fraude/proyecto.md` (§2 y el anexo de discovery) y `referencias/` (R1: PDF de la 8473, R2: transcripción de la reunión CAF, R3: documento de análisis de la Cámara sobre la 8471) para el detalle completo, con citas.
