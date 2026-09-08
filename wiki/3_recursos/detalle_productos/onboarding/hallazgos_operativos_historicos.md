# Hallazgos Operativos Históricos — Onboarding

> Estado: mezcla de en producción (ya corregidos) y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde `detalle_productos/transversal/dolores_soporte_y_administracion.md`, que mezclaba estos hallazgos con los de otros productos.

## Bugs de datos incompletos

- No se validaban correctamente DNI/Ocupación/Estado Civil en el alta con cuenta comitente (luego sí se permitió enviarlos).
- Onboarding no valida el vencimiento del DNI.

## Idempotencia

**Bug de idempotencia real**: un alta de cuenta Wallet dio timeout, la operación en realidad había respondido bien, y el sistema terminó duplicando la cuenta. Ver [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) para la lectura transversal completa de este patrón.

## Operación

- No se pueden aprobar varias solicitudes de Onboarding juntas (solo de a una).

## Gaps de control antifraude (Pendientes, sin desarrollar)

- Automatizar el envío de mails de fraude.
- No permitir hacer onboardings con el mismo email dos veces.

## Endpoints de domicilio

- Pedir domicilio/nacionalidad/UIF/PEP/FATCA al alta, y no volver a pedir como obligatorios campos que ya existen al actualizar una cuenta.

## Hotfixes de Onboarding de Persona Física

> Fusionado desde `detalle_productos/onboarding/manuales_operativos.md §3` en la reestructuración PARA en cascada (2026-08-12). Fuente: Jira `bindpsp.atlassian.net`, espacio OB. Backfill vía export XML, 2026-07-13.

- **OB 1 HF** (2026-01-28): [OB-62](https://bindpsp.atlassian.net/browse/OB-62) — error en el alta de onboarding para el cliente Inter.
- **OB 2 HF** (2026-02-02): [OB-54](https://bindpsp.atlassian.net/browse/OB-54) — error en la integración con **Worldsys** (proveedor de listas Terrorista/PEP consultado durante el onboarding).

## Decisión de producto — no priorizar mejoras de lectura de QR/código de barra (2026-09-07)

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-07), minuta Gemini.

El sistema de Onboarding es estricto leyendo códigos QR/de barra en el proceso de incorporación — rechaza con facilidad fotos de calidad media, afectando a clientes como **Coppel** (transcripto "Copel" en la minuta). Pablo Gomes fijó una posición de producto explícita: **no se van a priorizar mejoras en la lectura de imagen de QR/código de barra en Onboarding**, porque no es un producto que Bind PSP monetice ni sea foco — el foco actual es legajos, validaciones y cumplimiento PLD. Recomendación para clientes con onboarding propio: integrar por API enviando los datos ya leídos de su lado (como ya hace **INTER**) o intentar su propia lectura con mejor tecnología y usar Bind solo como fallback (caso **Arcos Dorados**). Se plantea evaluar a futuro una mejora de UX de captura (lectura QR en vivo mientras se mueve la cámara, en vez de una sola foto estática) sin compromiso de fecha ni prioridad.

## Riesgos operativos y novedades de compliance

> Fusionado desde `detalle_productos/onboarding/manuales_operativos.md §4` en la reestructuración PARA en cascada (2026-08-12). Fuente: Reunión "Join Soporte Clientes" (2026-07-15), minuta Gemini.

- **Apertura de cuentas comitentes por lotes semanales:** para optimizar la carga operativa, pasa de gestionarse diariamente a **lotes semanales** — el proveedor debe crear un único ticket por semana con la cantidad de cuentas a procesar. Pendiente validar el flujo de aceptación de términos y condiciones.
- **Nuevo DNI — errores de validación por formato PDF417/QR:** el equipo está en contacto con Fintexa para resolver errores de validación de DNI surgidos por la falta de formato PDF417 y la presencia de códigos QR en el nuevo diseño de documento — sin fecha estimada. Distinto de OB-181 (bug ya corregido de flujo bloqueado post-lectura de PDF417, ver [1_proyectos/.../prd-108_legajo_altas_cuenta/proyecto.md](../../../1_proyectos/proyecto-onboarding-estrategico/prd-108_legajo_altas_cuenta/proyecto.md)); acá el problema es la validación del propio documento del nuevo DNI.
- **Legajos de onboarding digital deben alojarse en la herramienta SOS (exigencia de Compliance):** punto de bloqueo reconocido para destrabar nuevas propuestas de negocio, pendiente de resolución entre áreas.
- **Política de bloqueo de transferencias entrantes en cuentas:** no existe exigencia normativa que obligue a bloquear el ingreso de fondos a una cuenta — el criterio de Compliance es que la solución debe enfocarse en el **monitoreo de transacciones**, no en restringir los ingresos.

---
*Fuente: Epic Notion "Dolores de Soporte y administración" (~93 tickets, muestra relevante) — ingesta 2026-07-06.*
*Última actualización: 2026-08-12 — Fusionadas secciones §3 y §4 de `detalle_productos/onboarding/manuales_operativos.md` (reestructuración PARA en cascada). Contenido base creado consolidando la sección de Onboarding de `detalle_productos/transversal/dolores_soporte_y_administracion.md`.*
