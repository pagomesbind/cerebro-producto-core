# Pagos FX — Portal Web, alta de beneficiarios (Mastercard)

> Estado: en producción.

> Fuente: Reunión "Seguimiento Portal - Pagos Fx" (minuta Gemini, 2026-07-23) — sesión de diseño técnico entre Bind PSP (Luciana Rudaz, foco Pagos FX) y Fintexa/proveedores externos (Keep It Simple, Tecfinanciera). Complementa el contexto de negocio ya documentado en [`psp_as_a_service_normativa_8432.md`](psp_as_a_service_normativa_8432.md) y el resumen de Epic/tickets de PRD-184 (proyecto de Luciana Rudaz — desde 2026-08-13 vive en su propio Cerebro, ya no en `1_proyectos/` de esta instancia). El "PCP" que aparece en la minuta original es "PSP" (Bind PSP) — error recurrente de ASR de Gemini.

## 1. Concepto de "corredor" y validación dinámica

El servicio de Mastercard **no persiste los datos de los beneficiarios** — Bind PSP necesita lógica propia de alta. Un **corredor** se define por la combinación de: país de destino + moneda de destino + tipo de pago + instrumento de pago (siempre bancario). El sistema consume un endpoint que devuelve las especificaciones requeridas y su versión vigente para cada corredor; el front-end debe renderizar dinámicamente los campos obligatorios que ese endpoint devuelve (con menús desplegables para valores soportados, nunca texto libre, para asegurar la calidad del dato que viaja a Mastercard).

- **Actualización diaria de especificaciones:** proceso batch (BGS) a las 00:00hs mantiene las especificaciones de cada corredor al día en la base.
- **Versionado:** el pago valida la versión de especificación asociada al beneficiario. Si quedó desactualizada, el sistema devuelve error — no existe today un mecanismo de notificación proactiva al usuario cuando cambia una especificación.
- **Datos del remitente excluidos del formulario:** el backend resuelve el `sender` automáticamente a partir de la cuenta del usuario logueado — no debe pedirse ni mostrarse en el alta de beneficiario.

## 2. Tipo de cuenta y buscador de bancos

La lógica de cuenta depende del país de destino:
- **IBS** (ASR: "IVS" en otras fuentes) → estándar IBAN.
- **ASB** (ASR: "ASV") → requiere validación adicional vía **buscador de bancos** (`Bank Lookup`): consulta por BIC (+ nombre de banco si está disponible) para traer sucursales; el front muestra el resultado en un desplegable y envía la selección como JSON serializado dentro del alta.
- El tipo de cuenta se deriva automáticamente del país de destino en el front — no se pide al usuario.
- El backend acepta `null` en el JSON bancario cuando el tipo es IBS, pero **todavía no lo valida de forma estricta** — el front debe filtrar esa lógica mientras tanto para evitar errores.

## 3. Alta de beneficiario — request y ciclo de vida

**Campos del alta:** id de cuenta, país destino, moneda destino, tipo de pago, tipo de cuenta, versión de especificación, JSON de información bancaria (si aplica ASB), id externo (opcional). Un único archivo adjunto permitido, convertido a base64, **máximo 8MB**.

**Documentación requerida según tipo de beneficiario:** identificación fiscal (personas físicas) vs. documentación legal de existencia (empresas) — disclaimer específico para la carga de estos documentos (a redactar por Luciana Rudaz).

**Ciclo de estado:** el alta no admite guardado parcial — todos los datos obligatorios deben completarse en una sola sesión. Tras el envío queda `PENDIENTE`; el backend corre validación **asíncrona** contra Mastercard (dirección + cuenta bancaria, usando también los datos del Bank Lookup si es ASB) que toma del orden de horas. El front debe reflejar el cambio a "válido y aprobado" dinámicamente cuando se resuelve. **No existe funcionalidad de edición** de un beneficiario ya dado de alta — ante datos incorrectos hay que volver a cargarlo desde cero; los cambios por actualización de especificación se atienden vía soporte técnico.

## 4. Flujo de pago — ajustes de UX (requerimientos de COMEX/compliance)

- **Confirmación de pago:** se invierte la jerarquía visual (moneda destino pasa a ser el dato principal, ARS queda secundario) y se agregan los datos de cuenta del beneficiario (IBAN/SWIFT-BIC) al resumen.
- **Botón de alta de beneficiario:** se pide mejorar su visibilidad e incluirlo también dentro del flujo de pago (no solo en la pantalla de gestión de beneficiarios).
- **Reorganización del flujo de declaración jurada/documentación:** eliminar el recuadro gris de "estructura del pago", mover la carga de archivos al paso de selección de conceptos, y deshabilitar los botones de navegación hasta que se cumplan las validaciones obligatorias.
- **Conceptos de pago:** se redujo la lista de valores permitidos; cada concepto debe llevar un disclaimer relacionando el concepto con la documentación adjunta requerida, con el botón de continuar deshabilitado hasta cumplirlo.
- **Navegación:** falta un botón de "volver atrás" durante la revisión del pago — hoy las únicas opciones son continuar, aceptar y pagar, o cancelar (cancelar saca al usuario al panel general).
- **Guardado de pagos pendientes:** evaluado y **descartado explícitamente** — no se implementa en esta instancia.
- **Comprobante de pago:** debe poder exportarse/descargarse en PDF (confirmación de envío exitoso + desde el módulo de "mis operaciones", con el estado final de la transacción). Requisito legal de pie de página: leyenda de "servicios de Bind PSP en alianza con Mastercard" **sin usar el logo de Mastercard** (restricción legal), manteniendo el texto "Powered by PSP".
- **Filtro de beneficiarios:** la tabla de gestión de beneficiarios no filtra hoy por estado ni por campo "habilitado" — se pidió ticket independiente para no impactar otras áreas del sistema.

## 5. Estado de la integración (a la fecha de la reunión)

Se compartieron archivos Excel con el resumen de especificaciones y corredores soportados. Credenciales de producción esperadas la semana siguiente para pruebas con datos reales.

## 6. Alta operativa de una organización nueva de Pagos FX/crossborder (posible caso PeYa) — 2026-08-05

> Fuente: reunión "eco cerrado peya" (2026-08-05), minuta Gemini. **Nota de confianza:** el título de la reunión sugiere el caso PeYa (ver gap `[2026-07-15]` en `../../../2_areas/gaps_y_preguntas.md`, PedidoYa pidiendo credenciales de producción), pero el contenido de la minuta no menciona a PeYa explícitamente — se documenta igual por ser conocimiento técnico reutilizable de la mecánica de alta de organizaciones de Pagos FX.

**Flujo de alta de una organización nueva** distingue dos partes independientes que deben gestionarse por separado: la **billetera (wallet)** — creación de organización + asignación de cuenta recaudadora — y la **adquirencia** — creación de entidad + portal 2.0. Al momento de la reunión solo se había completado el lado wallet.

**Configuración vía scripts/API, no acceso directo a producción:** Fintexa (Martín Hovanyecz) provee 7 scripts que cubren la configuración completa de una organización (reemplazando una variable de organización en cada uno), pero el equipo de Bind PSP **no tiene permiso de ejecutarlos directamente en producción** (no hay Swagger habilitado ahí) — la ejecución queda del lado de Fintexa. Cuando es posible, el equipo prefiere gestionar specs y cargos vía **API expuesta** en vez de scripts, y reserva los tickets a Fintexa solo para lo que no puede autogestionar.

**Corredores (Pagos FX crossborder):** se usa una tabla general de corredores para la organización "BM PCP" — un corredor es un destino (ej. Brasil, Canadá, China) habilitado por organización. Bloqueado temporalmente por falta de acceso a la base de datos de "wallet cross border" (ticket ya generado para permisos).

**Gap de notificación:** falta en producción el evento de notificación **"pago exterior resultado"** (sí existe "notificación pago FX") — pendiente de confirmar si el script de creación del tipo de evento se omitió; es necesario para el MVP.

**Entidades de transición:** mientras se esperan las credenciales de producción definitivas de la nueva entidad **"Move"** (apunta a una nueva cuenta comitente + entidad de API Broker, ver también `tareas_producto.md` T-068), el equipo sigue usando la entidad **"Coin"** en producción para pruebas de pago limitadas.

## Ver también

- [`psp_as_a_service_normativa_8432.md`](psp_as_a_service_normativa_8432.md) — contexto normativo/impositivo de Pagos FX (Norma 8432 BCRA), caso PeYa.
- PRD-184 (Pagos FX SEGUNDO MVP - Portal Web) — tickets de Jira de este mismo frente (AD-1318 alta de beneficiario, AD-1379 confirmación de pago, AD-1378 disclaimer, AD-1380 botón de alta): esta reunión aporta el detalle técnico de diseño detrás de esos tickets. Proyecto de Luciana Rudaz, vive en su propio Cerebro desde 2026-08-13.
- PRD-183 (Pagos FX SEGUNDO MVP - APIs) — frente de APIs del mismo segundo MVP. Ídem, Cerebro de Luciana Rudaz.

---
*Última actualización: 2026-08-05 — `/sync_meetings`: nueva §6 (alta operativa de organización nueva de Pagos FX/crossborder — corredores, scripts vs. API, gap de notificación, entidades de transición "Move"/"Coin"). Ver reunión "eco cerrado peya" del 2026-08-05 en `wiki/5_control/log_reuniones.md`.*
*Última actualización anterior: 2026-07-23 — Creación del archivo (`/sync_meetings`), a partir de la reunión "Seguimiento Portal - Pagos Fx" del 2026-07-23.*
