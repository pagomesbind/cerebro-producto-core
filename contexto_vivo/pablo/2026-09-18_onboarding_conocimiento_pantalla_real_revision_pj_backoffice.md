---
id: 2026-09-18_onboarding_conocimiento_pantalla_real_revision_pj_backoffice
pm: pablo
fecha_captura: 2026-09-18
fuente: "/idea_solution sobre revision_pj_cumplimiento — repaso en vivo del PM sobre dos solicitudes reales del backoffice de Onboarding jurídico en staging (Nivel 1 y Nivel 2)"
producto: onboarding
tema: estructura real actual de la pantalla de solicitud de PJ en el backoffice (no la referencia externa)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md §7 (flujo AS-IS) — no documenta el detalle real de la pantalla de solicitud, solo el flujo de pasos"
confianza: alta
estado: en_cola
merge_commit:
---

Durante `/idea_solution` sobre `revision_pj_cumplimiento` (PRD-256), el PM navegó en vivo dos solicitudes reales en el ambiente de staging del backoffice de Onboarding jurídico (una en estado "Pendiente Revisión Oficial De Negocio" / Nivel 1, otra en "Pendiente Revisión Cumplimiento" / Nivel 2). Esto confirma el detalle real de la pantalla de solicitud, más allá del flujo de pasos ya documentado en `onboarding_personas_juridicas.md §7`:

**Estructura de la pantalla hoy (una sola vista larga, sin pestañas):**
1. **Datos de la Solicitud** — identificador, fecha/hora, trámite (Legajo Digital), informado, IP, dispositivo, razón social, CUIT. Los botones **Aprobar/Rechazar** viven adentro de esta misma tarjeta (no en un header fijo) — **no existe un botón "Observar"**, la función equivalente la cumple la sección "Contactar Cliente" más abajo.
2. **Contacto** — email y teléfono, cada uno con Editar, badge Verificado/Sin verificar, botón "Enviar código" y un campo de texto "Código OTP" + botón Verificar (flujo manual completo, no solo el botón de envío).
3. **Domicilio Fiscal** y **Domicilio Comercial** — dos bloques separados, mismos campos (País, Provincia, Ciudad, Calle, Numeración, Piso, Barrio, Código Postal, Departamento, CPA, Localidad, Manzana, Municipalidad).
4. **Beneficiario Final** — tabla (Apellido y Nombre, Nro. de Documento, botón "Ver Detalles Beneficiario") que abre un modal con: Razón Social, Tipo de Documento, Número de Documento, Domicilio Real, Nacionalidad, Fecha de Nacimiento, Profesión, Estado Civil, Votos en la Sociedad, PEP. **No se vio ninguna sección "Propietarios" separada** en los dos casos de prueba revisados — no se pudo confirmar si es porque esos casos puntuales no tenían propietarios cargados o si el concepto no existe separado de Beneficiario Final.
5. **Datos Bancarios** (CBU, Número de cuenta) y **Datos Comerciales** (Nombre de Fantasía, ID del comercio, Código de Caja, Código Sucursal) — vacíos hasta la aprobación, igual que ya estaba documentado.
6. **Historial** — tabla resumida de cambios de estado relevantes (Fecha, Hora, Estado, Usuario, Comentario) — 2-3 filas típicamente.
7. **Representantes Legales** — tabla (Fecha y Hora, Estado, Representante/CUIL-DNI, Carácter, Email) con acción para ver/gestionar.
8. **Contactar Cliente** — formulario (Método de Contacto, Documentación, Enviar correo a, Comentario con contador de caracteres 0/500, botones Cancelar/Enviar).
9. **Validaciones Servicios Externos** (Deudor-Arca, Arca-Actividad, Documento-Lista Negra, Mba-System, Nosis-Jurídico, Situación-BCRA) y **Validaciones Declaración Jurada** (FATCA, OCDE, PEP, UIF) — **son dos paneles separados**, no uno solo; el segundo es información que el propio cliente declaró (siempre Sí/No), no una consulta a un servicio externo.
10. **Archivos** — **una sola lista plana de documentos agrupados por categoría** ("Documentación societaria", "Otros archivos"), no agrupados por persona/entidad. Cada documento tiene menú de acciones (Descargar, Visualizar, Marcar Pendiente) vía ícono de tres puntos. Este es el punto que el PM señaló como **la causa concreta de que a un oficial le resulte incómodo validar** — no hay forma de ver de un vistazo qué documentos corresponden a qué persona.
11. **Línea de Tiempo** — a diferencia del "Historial" resumido (punto 6), esta es un **log técnico crudo y muy granular**: decenas de eventos por solicitud (ej. "Update Documentación" repetido muchas veces, "Create Otp Sms", "Update Padron A5"), cada uno con timestamp exacto y un ID interno (GUID), pensado para depuración técnica, no para que un analista de negocio lo lea.
12. **Respuestas Servicios** — pestañas con el JSON crudo de cada respuesta de servicio externo (Afip PadronA5, Legajo Digital, Beneficiario Final, Declaración Jurada, Matriz de Riesgo Jurídica, etc.), colapsable, claramente pensado para debugging técnico. Acá aparece suelto el dato de actividad económica de ARCA (ej. `idActividad: "829900"`) que hoy no se le muestra al oficial en ninguna pantalla legible.

**Dato adicional:** en el Historial de una de las solicitudes revisadas aparece el comentario "A revisar por matriz de riesgo" al pasar a Nivel 1 — sugiere que existe algún mecanismo interno de matriz/scoring que dispara ese estado, aunque no hay ninguna tarjeta de score visible para el oficial (consistente con lo ya confirmado: no existe una funcionalidad de "Score de Compliance" como la de la consola de referencia externa). No se investigó más a fondo — posible gap a explorar en un futuro discovery si se retoma el tema de matriz de riesgo.
