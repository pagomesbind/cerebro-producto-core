# Base de proveedor (Fintexa/Soluciones Andinas) — Onboarding Jurídico y de Persona Física

> Estado: en producción.

> ⚠️ **Nota de vigencia y alcance:** este documento resume el material de base que **Fintexa/Soluciones Andinas** (mismo proveedor, ver §0.1) entrega para OB PF y OB PJ. **Ambos productos los consume Bind PSP actualmente en producción** — no es una propuesta nunca adoptada. Bind PSP hizo (y sigue haciendo) cambios, pedidos y ajustes propios sobre esta base, pero la base funcional/de proceso descripta acá es la que entrega el proveedor. Los diagramas Bizagi concretos, sin embargo, están modelados para *otros* clientes del proveedor ("Banco Julio"/"Banco Coinag", ver §3) — son la plantilla genérica, no necesariamente el detalle exacto configurado para Bind PSP. Para el detalle de cómo corre hoy en Bind PSP (bugs, incidentes, particularidades), ver [onboarding_personas_juridicas.md](onboarding_personas_juridicas.md) y el resto del índice del módulo.

## 0. Origen

- **Fecha de recepción:** 2026-07-23.
- **Remitente:** Franco Bertoldi, Socio Gerente de **Soluciones Andinas SRL** (Godoy Cruz, Mendoza — `solucionesandinas.com.ar`), para Pablo Gomes.
- **Adjuntos:**
  - `Onboarding Jurídico - Documento Comercial.pdf` — presentación funcional de la solución (17 láminas).
  - `Proceso negocio OB PF.bpm` — diagrama de proceso (Bizagi Modeler) del Onboarding de Persona Física.
  - `Proceso negocio OB PJ.bpm` — diagrama de proceso (Bizagi Modeler) del Onboarding de Persona Jurídica.
- **Contexto del usuario:** actualmente OB PF y OB PJ son **dos aplicaciones separadas**, ambas consumidas por Bind PSP en producción sobre la base de este proveedor.

### 0.1 Fintexa = Soluciones Andinas (aclarado por el usuario, 2026-07-23)

**Fintexa es un spin-off de Soluciones Andinas — a fines prácticos, la misma empresa.** El nombre anterior de Fintexa es **"Tecnología Financiera" / "Tecfin"**: cuando esos nombres aparezcan en fuentes futuras (mails, reuniones, documentos), refieren a este mismo proveedor. Esto resuelve el gap que este mismo ingest había abierto (el mail llegó firmado por Soluciones Andinas, sin mención literal a "Fintexa") — ver resolución en `gaps_resueltos.md`. La arquitectura de infraestructura ya documentada en [arquitectura_sistema/index.md](../../arquitectura_sistema/index.md) es, por lo tanto, del mismo proveedor que entrega esta base de Onboarding.

## 1. La propuesta funcional (PDF comercial)

Título: *"Transformando el Onboarding Jurídico — Una experiencia digital, inteligente y segura para sus clientes corporativos."*

### 1.1 Problema planteado
El onboarding corporativo tradicional es lento/manual, fragmentado (múltiples sistemas, correos, sin visibilidad), inseguro (fraude, suplantación, errores de carga) y costoso (cumplimiento KYC/KYB).

### 1.2 Propuesta: "Ecosistema End-to-End" con 3 pilares
- **Inteligencia:** automatización de extracción/validación de datos vía IA y OCR.
- **Seguridad:** verificaciones en tiempo real contra fuentes externas, validación biométrica de representantes, matriz de riesgo configurable.
- **Experiencia:** flujo 100% digital, sin fricciones, comunicación transparente en cada etapa.

### 1.3 Las 4 etapas del proceso propuesto
1. **Inicio:** captura de datos inicial (Razón Social, CUIT, Email, Teléfono, Tipo de Sociedad), 100% digital desde web o móvil, aceptación de T&C. El sistema consulta automáticamente en un **"Legajo Digital"** la documentación requerida según el tipo de sociedad.
2. **Validación:** verificación automatizada y análisis de riesgo — cruces en tiempo real contra **AFIP**, **BCRA** (Central de Deudores), **Nosis** y **WorldSys**; matriz de riesgo configurable (aprobar/rechazar/escalar); cruce contra listas restrictivas (PEP, terroristas, sujetos obligados — UIF, WorldSys).
3. **Verificación (OB PF):** por cada Representante Legal/Firmante/Director-Socio identificado en la documentación societaria, se dispara automáticamente un Onboarding de Persona Física independiente (notificación → validación biométrica → sincronización centralizada).
4. **Alta y Otorgamiento:** generación automática de contratos pre-poblados (módulo "Formulario Dinámico"), recolección de firmas (firma digital/electrónica con validez legal), alta final en el sistema core de la entidad + email de bienvenida.

### 1.4 Automatización inteligente de documentos (OCR/IA)
Documentos de entrada: Estatuto Social (PDF), Balance General (JPG), Inscripción AFIP, Poderes → motor IA/OCR → datos estructurados y validados: **Datos Societarios** (Razón Social, CUIT, Fecha de constitución), **Datos Financieros** (Facturación anual, Mes de cierre del ejercicio), **Participantes** (Nombre, DNI, Cargo, % de participación), **Datos Impositivos** (Condición ante IVA, Ganancias). El sistema valida consistencia del CUIT entre documentos y permite edición manual de cualquier dato extraído.

### 1.5 Backoffice ("Control Total")
- **Gestión de Solicitudes:** búsqueda/filtro/visualización de cada solicitud en tiempo real.
- **Visor de Datos Consolidados:** secciones organizadas (Datos de la Sociedad, Participantes, Datos Impositivos, Domicilios).
- **Timeline de Solicitud:** historial cronológico auditable de cada acción/validación/cambio de estado.
- **Comunicación Integrada:** contacto al cliente por email directamente desde la solicitud.
- **Continuidad Omnicanal:** un ejecutivo en sucursal puede retomar y finalizar junto al cliente una solicitud online incompleta.

### 1.6 Cumplimiento y aprobaciones configurables
- **Matriz de Riesgo Configurable:** activar/desactivar validaciones externas (Nosis, AFIP, etc.), definir umbrales de score y condiciones de rechazo automático (ej. situación 3/4/5 en BCRA).
- **Niveles de Aprobación Múltiples:** flujos secuenciales configurables (ej. Ejecutivo → Supervisor → Gerente), con perfiles de usuario asociados a cada nivel y estrategias de notificación flexibles.
- **Trazabilidad Completa:** cada acción/aprobación/cambio de estado queda en un timeline de auditoría visible para el ejecutivo.

### 1.7 Gestión automatizada de dependencias PJ↔PF (regla de negocio propuesta)
La plataforma monitorea el progreso del OB PF de cada representante legal y decide automáticamente según 3 escenarios (con un parámetro configurable de "mínimo de aprobados"):
- **Escenario 1 — Representante único rechazado:** la solicitud de la empresa se **rechaza** automáticamente, notificando al contacto inicial.
- **Escenario 2 — Múltiples representantes, mínimo no alcanzado:** ej. 3 RL con parámetro "mínimo 2 aprobados" — si solo 1 de 3 aprueba, la solicitud se **rechaza**.
- **Escenario 3 — Mínimo alcanzado:** ej. 2 de 3 RL aprobados (mínimo 2) → la solicitud **avanza** al siguiente nivel de aprobación.

### 1.8 Arquitectura técnica propuesta
- **Patrón:** orquestador central ("Orquestador Onboarding Jurídico", con API-Orquestador + BackOffice) integrado nativamente con: Frontend-Onboarding (Web & Móvil), Legajo Digital (repositorio de documentos), Formulario Dinámico (generación de contratos), Servicios de Verificación (Nosis/AFIP/BCRA/WorldSys), y el Sistema Core del cliente (para el alta final).
- **Stack:** arquitectura de microservicios, **.NET Core 8** y **React**.
- **Despliegue:** cloud-ready (Azure, AWS con Kubernetes) u on-premise (servidores Windows/IIS).
- **Seguridad:** validación de usuarios y gestión de perfiles de acceso detallados; auditoría completa de eventos técnicos y funcionales (usuario, fecha, acción).

## 2. Integraciones ya realizadas (según el mail, no el PDF)

Listado tal como lo detalló el proveedor — estas son integraciones que la aplicación **ya tiene construidas**, no parte de la propuesta a futuro:

- Consultar morfología y leer PDF417 (DNI).
- Consultar lista de no admitidos propias por documento / número de teléfono / email.
- Consultar lista de no admitidos que **Banco Julio** disponga.
- **RENAPER** — consulta.
- **AFIP** — consulta Padrón A5.
- **UIF** — consulta Sujeto Obligado.
- **NOSIS** — consulta.
- **VERAZ** — consulta.
- **WordSys** — consulta.
- Validar propiedad del email mediante envío de OTP.
- Consultar scoring email.
- Validar propiedad de la línea celular mediante envío de OTP.
- Consultar scoring teléfono.
- Verificación de identidad por desafíos de preguntas y respuestas (Veraz / Nosis).
- **BCRA** — consulta Central de Deudores.

## 3. Diagramas de proceso (Bizagi) — lectura de los `.bpm`

Los archivos `.bpm` son proyectos Bizagi Modeler (contenedor ZIP); se extrajo el diagrama de proceso (`Diagram.xml`) de cada uno. **Ambos procesos están nombrados y modelados para bancos que no son Bind PSP** ("OnBoarding **Banco Julio**" y "OnBoarding Persona Jurídica **Banco Coinag**"), consistente con la aclaración del mail de que son una propuesta base reutilizada de otros clientes del proveedor, no el proceso de Bind PSP.

### 3.1 `Proceso negocio OB PF.bpm` — "OnBoarding Banco Julio"

Carriles (lanes): **Front-End**, **API-Orquestadora**, **API Varios**, **RENAPER**, **API Notificaciones**, **Legajo digital**, **Back Office**, **Sistema cliente**.

12 fases del proceso principal:
1. Valida documentación (verifica morfología de imágenes, aplica OCR, obtiene datos PDF417/QR, solicita fotos frente/dorso DNI).
2. Validaciones (consulta cache Renaper — si existe y está vigente, si no, consulta Renaper en vivo; valida que la persona exista, el ejemplar sea válido y no haya fallecido).
3. Valida bases no admitidos (por DNI — ¿es admitido?).
4. Prueba de vida (desafío de prueba de vida, ¿obtuvo los datos?, ¿está vivo?).
5. Validación facial (comparación facial, ¿superó el umbral de aceptación?).
6. Valida Email (verifica existencia, solicita email, scoring email).
7. Valida Número celular (verifica existencia, solicita OTP, scoring teléfono, reintentos si no válido).
8. Validación matriz riesgo (checklist del dueño del cliente, ¿superó validaciones de checklist?).
9. Detalle alta persona (crea la persona, crea trámite, guarda datos).
10. Notifica alta solicitud (envía datos para el alta, verifica solicitudes anteriores).
11. Guardar legajo digital (almacena imágenes/datos PDF417-QR, TyC, checklist en PDF).
12. Mensaje fin (muestra mensaje de éxito y bienvenida, o de error).

Fallback explícito: si no se supera una validación automática (ej. matriz de riesgo), el proceso deriva a **"Verificación manual"** (¿superó verificación?) antes de resolver Validado / A revisar / No superó.

### 3.2 `Proceso negocio OB PJ.bpm` — "OnBoarding Persona Jurídica Banco Coinag"

Carriles (lanes): **Front-End**, **API-Orquestador**, **API-Varias**, **BackOffice**, **Sistema Cliente**. Sistemas externos nombrados en el diagrama: **BCRA**, **Nosis**, **AFIP**, **ARCA**, **MBA System**.

4 fases del proceso principal:
1. **Inicio:** ingreso de datos básicos, ¿la empresa existe? (si no, crea la empresa), carga de documentación (estatuto, poderes, accionistas, etc.), propone y verifica Domicilio Fiscal, carga de Domicilio Comercial, carga de Teléfono de contacto + OTP.
2. **Validación:** procesa contenido de documentos, ingresa datos de contacto de Beneficiarios Finales, confirma DDJJ, **envía enlaces para OB de Representantes Legales y Firmantes** (dispara los OB PF individuales), busca documentos/trámite.
3. **Aprobación Solicitud Jurídica:** ¿cumple? → ejecutivo evalúa la solicitud según su nivel; ¿aprobado? → si no, notifica rechazo al cliente y cambia estado a "rechazada".
4. **Alta de productos/Clientes:** solicita alta en sistema de clientes, alta cliente, envío de bienvenida, mensaje de éxito.

## 4. Relación con el conocimiento ya existente

- Este es el material de **base del proveedor** sobre el que corre el OB PJ de Bind PSP ya documentado en [onboarding_personas_juridicas.md](onboarding_personas_juridicas.md) (OB PJ MVP, con su propio historial de bugs e incidentes en Producción). No lo reemplaza: ese documento describe cómo quedó configurado/customizado y cómo se comporta en producción para Bind PSP; este documento describe la base funcional/de proceso genérica que entrega el proveedor.
- La dependencia PJ↔PF que describe el proveedor (mínimo N de M representantes aprobados, configurable) es la **base de la que parte** la regla de negocio ya documentada para el OB PJ interno ("al menos uno debe estar aprobado") — Bind PSP la ajustó a su propia configuración (mínimo 1) a partir de este mecanismo genérico del proveedor.
- Los diagramas Bizagi concretos (§3) nombran a otros clientes del proveedor (Banco Julio, Banco Coinag) porque son la plantilla base reutilizada entre clientes — no implica que el detalle paso a paso sea idéntico a la configuración real de Bind PSP, aunque la estructura general (etapas, validaciones externas, verificación de representantes, alta final) sí es la misma familia de proceso.

---
*Fuente: mail de Franco Bertoldi (Soluciones Andinas SRL) a Pablo Gomes, 2026-07-23. Adjuntos: `Onboarding Jurídico - Documento Comercial.pdf` (17 láminas, leídas como imágenes por falta de texto extraíble), `Proceso negocio OB PF.bpm` y `Proceso negocio OB PJ.bpm` (proyectos Bizagi Modeler, diagramas leídos desde `Diagram.xml`). Originales resguardados en [`4_archivos/historial_raw/2026-07-23_ingesta_fintexa_onboarding_juridico/`](../../../4_archivos/historial_raw/2026-07-23_ingesta_fintexa_onboarding_juridico/).*
