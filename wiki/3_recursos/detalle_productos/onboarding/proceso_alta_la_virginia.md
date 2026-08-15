# Proceso de Alta de Cuentas — Caso La Virginia (Puente Manual y Rediseño PJ)

> Estado: en curso (proceso puente manual vigente hasta que la automatización esté lista; rediseño PJ en desarrollo, MVP a 1 mes). Reubicado desde `detalle_productos/onboarding/manuales_operativos.md §5-6` en la reestructuración PARA en cascada (2026-08-12).

## 1. Proceso manual puente de alta de cuentas comitentes

> Fuente: Reunión "La Virginia | Proceso Batch Alta Cta Comitente" (2026-07-24), minuta Gemini.

La automatización batch de altas de cuenta comitente para La Virginia no va a estar lista hasta fines de septiembre de 2026. Mientras tanto, el equipo habilita las cuentas **manualmente** a partir de los IDs de cuenta que entrega el cliente (volumen actual ~100, potencial total ~1.400, en tandas graduales) — motivo: La Virginia no tiene la documentación del cliente propia, esa información vive en el sistema de Onboarding.

**Flujo técnico definido:**
1. Usar el `idCuenta` para identificar la solicitud correspondiente en la base de datos de Onboarding.
2. Recuperar los datos del cliente y descargar los archivos (frente y dorso de DNI) en base64 — reutiliza los endpoints de [consultar_solicitud_y_archivos.md](consultar_solicitud_y_archivos.md) (`GET /solicitudes/{id}`, `GET /archivos/{id}`).
3. Relacionar automáticamente `idCuenta`↔`idSolicitud` vía consultas SQL directas a la base de Onboarding, para evitar búsqueda manual.

Se construyó una herramienta/script de soporte para sostener el proceso hasta que la automatización esté lista, con despliegue en entornos accesibles para Soporte (ej. CUA). Validación planificada primero en Staging, con paso a Producción recién después de un checkpoint de revisión.

**Checkpoint 2026-07-29 — primera cuenta creada con éxito (en Producción, no en Staging):**
- Staging resultó **inutilizable para validar el proceso**: solicitudes marcadas como completas traían campos obligatorios (código postal, localidad) en `null`, y el `idCuenta` de Wallet asociado frecuentemente no existía en la base de Staging. Ante esto, el equipo probó directamente en producción.
- El sistema exige un campo de **"verificación de identidad"** en el alta (motivo no del todo claro) que acepta cualquier valor no vacío — workaround: enviar el DNI del titular.
- La búsqueda de una solicitud debe hacerse por **`idSolicitud`**, no por `idCuenta` (no existe endpoint de búsqueda por `idCuenta`).
- La primera alta en producción devolvió un código de error **2011** en la interfaz pese a haberse creado correctamente — la cuenta quedó verificada como activa consultando la base directamente. Falsa señal de error pendiente de corregir.
- **Pendiente de desarrollo (no bloqueante):** alternar entre Stage y producción desde el panel; mapear el DNI en la verificación de identidad; corregir la visualización del error 2011; endpoint dedicado para verificar el alta de una cuenta comitente; instalar el script en la VM de producción; definir el método de vinculación `idCuenta`↔`idSolicitud` (CSV o búsqueda por CUIT).
- Ver seguimiento en [2_areas/tareas.md](../../../2_areas/tareas.md) T-061.

## 2. Rediseño del flujo de onboarding PJ para clientes con integración propia

> Fuente: Reunión "OB PJ" (2026-08-05), minuta Gemini — con Cristian Bonafede (Tecfinanciera/Fintexa) y Franco Bertoldi (Soluciones Andinas).

**Problema:** de ~120-250 intentos de alta de personas jurídicas de La Virginia, solo el **5% (12) resultó exitoso**. Causa raíz: el cliente final carga mal los datos (apoderados, beneficiarios finales) y el flujo no permite retomar/corregir una carga previa — el onboarding "sale limpio" en demo controlada, pero no funciona en la operación real con 2.000 personas jurídicas por dar de alta. La Virginia no se anima a salir a producción con el producto en su estado actual.

**Decisión de flujo nuevo** (ver [2_areas/direccion/decisiones.md](../../../2_areas/direccion/index.md) 2026-08-05): en vez de que el cliente final autogestione su propia carga, un **oficial de negocio de La Virginia** (whitelist de 15 personas) inicia el onboarding, recolecta y carga la documentación previamente validada. Solo al final se dispara la validación de personas humanas (apoderados/firmantes) vía el link ya existente.

**Mecánica de datos confirmada (Legajo Digital vs. plataforma de Onboarding):**
- La plataforma de Onboarding **no es el repositorio definitivo** — guarda temporalmente (hoy en S3, sin organización, riesgo de pérdida de links) y un proceso asíncrono transfiere los archivos a **Legajo Digital**, que sí conoce el ciclo de vida de un cliente.
- Legajo Digital define, de forma dinámica y por tipo de sociedad, **qué documentación pedir** (vía "código de trámite") — el onboarding solo renderiza lo que Legajo Digital le indica.
- El onboarding maneja **solicitudes**, no clientes — una misma persona jurídica puede generar múltiples solicitudes (alta básica, aprobación de operación, alta de cuenta comitente) que hoy no se pueden relacionar entre sí dentro de la plataforma (solo indirectamente, por número de documento, con datos encriptados).
- Bind PSP guarda además en **SOS** (obligación del BIN, herramienta de Compliance) — la doble guarda en SOS + Legajo Digital está en discusión estratégica sobre si se justifica mantenerla.

**Otras definiciones de la sesión:**
- Se **rechaza** la propuesta de un tercero (Daxia) de sumar un formulario web externo no integrado — se prioriza mantener el control del proceso en la plataforma propia.
- La aceptación de términos y condiciones se traslada al onboarding de la persona humana (hoy la haría el oficial de negocio, lo cual no corresponde).
- Validación de OTP de email/teléfono: se evalúa moverla al backoffice en vez de bloquear la carga inicial en el frontend.
- Edición desde backoffice: mientras la solicitud no esté en estado aprobado/final, debe poder editarse sin reiniciar todo el proceso.
- **MVP con plazo de 1 mes** — no se busca cubrir todas las validaciones complejas de entrada, solo lo mínimo para que La Virginia pueda operar; el resto queda para fases evolutivas.
- Relacionado (mismo debate, contexto Onboarding PF): evaluación de integrar **FaceTech** (US$0,09) en vez de Socialnet (US$0,30) para prueba de vida — no prioridad de este mes, se cotiza en paralelo.
- Se reconoce déficit de herramientas/conocimiento de producto en soporte N1/N2 — genera volumen alto de tickets escalados directo a desarrollo; pendiente resolver vía producto, no vía parches operativos.

Ver seguimiento en [2_areas/tareas.md](../../../2_areas/tareas.md) T-086.

## Ver también
- [consultar_solicitud_y_archivos.md](consultar_solicitud_y_archivos.md) — endpoints reutilizados en el proceso manual puente.
- [1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md](../../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md) — proyecto vivo asociado a este cliente.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/onboarding/manuales_operativos.md §5-6` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
