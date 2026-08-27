---
id: 2026-08-24_onboarding_requisitos_evidencia_legajo_delegado
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Consulta documento evidencia para legajo' (docId 1Iws6wjmWkCcukdwWJTFHPd9EDuOgTu4Ujb-6GCq_1YE), 2026-08-24, con María Victoria Simonetti (PLD, Banco Industrial)"
producto: onboarding
tema: Requisitos de evidencia documental cuando el onboarding es delegado a un tercero (revalidación interna, PEP/FATCA, control de listas)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/integracion_worldsys_complianceone.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Requisitos de evidencia documental para legajo cuando el onboarding fue delegado a un tercero

**Contexto:** el PM (Pablo Gomes) se reunió con María Victoria Simonetti, referente de PLD (Prevención de Lavado de Dinero) de Banco Industrial, para alinear qué documentos/evidencia debe conservar Bind PSP en el legajo (destino final: Worldsys/ComplianceOne, ver PRD-147) cuando la validación de identidad del cliente fue delegada a un tercero — el caso concreto discutido es BCF actuando por cuenta de un comercio (ej. Carrefour), que a su vez usa proveedores externos de prueba de vida como Socialnet o FaceTech.

**Documentación obligatoria del legajo, en cualquier escenario:**
- DNI frente y DNI dorso: siempre como **imágenes JPG separadas**, nunca unificadas en un solo archivo/PDF.
- Foto selfie.
- Evidencia de las declaraciones de **PEP** (Persona Expuesta Políticamente), **FATCA** y **sujeto obligado**.
- Evidencia de la **aceptación de términos y condiciones** por parte del cliente (Simonetti tomó como referencia un ejemplo real de otro sistema de monitoreo, "Vin Uruguay", donde el contrato completo con la aceptación queda embebido en el legajo).
- Evidencia del **control de listas**: puede entregarse como archivo de texto (TXT) o imagen (JPG), y debe detallar horario del control, contra qué lista se corrió, y resultado (positivo/negativo).

**Distinción normativa entre tipos de control de listas:**
- El **control de listas contraterroristas** es un requisito normativo obligatorio a nivel regulatorio — evalúa porcentaje de similitud por nombre y apellido, no contra el número de documento.
- La **"lista 15"** (mencionada en otros proyectos internos, ver PRD-116) es una política interna del banco para alinear criterios entre equipos — no es un mandato normativo.

**Riesgo de auditoría al delegar onboarding sin revalidación propia:** Simonetti advirtió que si Bind PSP delega el onboarding en un tercero (ej. BCF) y no ejecuta ninguna validación propia sobre lo que ese tercero le pasa, queda expuesto a observaciones de auditoría — el argumento que un auditor puede usar es que la entidad "no hace ningún control cuando pasa directo". La mitigación esperada es que Bind PSP ejecute una **revalidación interna** sobre lo que el tercero envía: por ejemplo, verificar que el porcentaje de similitud de la prueba de vida dio un valor razonable, que el DNI frente/dorso son legibles, que el domicilio y los datos identificativos están completos, y volver a correr un chequeo de listas propio. El argumento de defensa ante auditoría pasa a ser: "la entidad tiene su propio onboarding, y además hacemos una convalidación adicional con nuestro propio logueo" — no delegación ciega.

**Estructura de almacenamiento para evitar duplicidad (evitar saturación en Worldsys):**
- El paquete original del tercero (DNI, selfie, prueba de vida) **no se duplica** — se sube una sola vez.
- La revalidación/relogueo que hace Bind PSP internamente (qué controles corrió, con qué resultado) se sube como **un archivo separado (TXT/log)**, distinto del paquete original — nunca repitiendo el mismo documento dos veces.
- Este criterio de "un documento resumen de validación propia + el paquete original sin duplicar" es preferido por Simonetti para no generar una cantidad excesiva de archivos por legajo (mencionó el riesgo de Worldsys rechazando por volumen: "no me mandes 40 archivos por una persona").

**Caso específico de proveedores de prueba de vida sin evidencia rica (Socialnet, FaceTech):** cuando el proveedor de prueba de vida usado por el tercero delegado (ej. Socialnet, usado por Bind PSP mismo con algunos clientes; o FaceTech, usado por Carrefour) no entrega video ni resumen completo — solo un ID/código de consulta que permite ir a consultar el resultado en la plataforma del proveedor — la evidencia mínima aceptable es un documento que demuestre que el proveedor ejecutó la prueba, en qué horario, y qué resultado dio (aunque no incluya el video).

**Verificación de Renaper y listas antiterroristas cuando el tercero valida vigencia de DNI:** si el tercero delegado (ej. BCF) ya valida contra Renaper que el DNI está vigente, Bind PSP igual debe solicitar y conservar esa evidencia — el respaldo documental demuestra que la entidad tiene un control adicional y no procesa altas de forma directa sin revisión.

**Aplicación práctica pendiente (PRD-147):** este criterio es el insumo de fondo para T-014 (definir qué documentos exigir por entidad antes de pedirle a Worldsys que parametrice su catálogo de `document-types`) — ver `1_proyectos/proyecto-onboarding-estrategico/prd-147_legajo_worldsys/decisiones.md` (2026-08-24) y `tareas.md` (T-030). La propuesta de documentos por solicitud de persona física está en preparación por el PM, a validar con Diego y Simonetti; la persona jurídica queda para un segundo pase por mayor complejidad de legajo.

> Fuente: Reunión "Consulta documento evidencia para legajo" (2026-08-24), minuta Gemini, con María Victoria Simonetti (PLD, Banco Industrial) y Pablo Gomes.
