---
id: 2026-09-22_onboarding_formulario_publico_pj_estructura_pasos
pm: pablo
fecha_captura: 2026-09-22
fuente: "sesión libre — carga real end-to-end del formulario público de onboarding de Persona Jurídica (Mundo Virginia, ambiente STG) como usuario final/operador, con datos de test, para armar el Paso 1 de un manual de uso del flujo completo"
producto: onboarding
tema: estructura y sub-pasos del formulario público de alta de Persona Jurídica (Mundo Virginia) — lo que carga el usuario final/operador antes de que la solicitud llegue al backoffice
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

Carga real (no simulada) del formulario público de onboarding de Persona Jurídica sobre el ambiente STG de La Virginia ("Mundo Virginia"), como usuario final/operador, con datos de test. Documenta el lado "de entrada" del flujo que `onboarding_personas_juridicas.md` ya cubre desde el backoffice (Pasos 2 y 3) — es decir, qué carga exactamente el usuario final antes de que la solicitud aparezca en la grilla de "Personas Jurídicas" con estado "Pendiente Revisión".

**Estructura del wizard (barra de progreso arriba, un sub-paso a la vez, con "Anterior"/"Siguiente" o "Iniciar"/"Siguiente"):**

1. **Bienvenida** — pantalla de marca ("¡Bienvenido a Mundo Virginia!") con una advertencia: hace falta tener actividad económica dada de alta en ARCA para continuar. Botón "Iniciar".
2. **Datos cliente** — Razón Social, Email, Confirmar Email, CUIT, Tipo de Sociedad (dropdown; en el test se usó "Anónima (SA)"). Cada campo valida en vivo con un tilde verde.
3. **Documentación** — grilla de documentos societarios obligatorios (asterisco = obligatorio), cada uno con su propio botón de carga individual. Advertencia fija: "Solo se permiten archivos PDF y menores a 6MB". Los nombres de documento coinciden con lo que el Paso 2 del backoffice ve como "Falta"/"Pendiente" en la sección Archivos → Documentación societaria (confirma que es la misma lista, solo que acá se sube y en el backoffice se revisa).
4. **Propietario Directo (socio o accionista)** — dos checkboxes de partida, mutuamente relevantes: "Indica si la sociedad pertenece solamente a personas humanas" vs. "Indica si la sociedad tiene socio/s persona/s jurídica/s". Tildando la segunda se abre un formulario por socio societario: Razón Social, Lugar de Registro, Tipo de identificador fiscal (dropdown, ej. CUIL) + N° identificador fiscal, Domicilio Legal, % de Propiedad y/o Votos de la Sociedad, % de Flotación (si cotiza en bolsa), con un ícono de tacho para eliminar el bloque si se cargó de más.
5. **Beneficiario Final** — mismo patrón de dos checkboxes de partida: "NO TIENE personas humanas que posean, directa o indirectamente, el 10% o más..." vs. "TIENE...". Tildando la segunda se abre un formulario completo por beneficiario: Razón Social (del titular persona humana), Nombre, Apellido, Tipo de documento (dropdown DNI/LC/CUIT) + Número de documento, Nacionalidad, Tipo de identificador fiscal (ej. CUIL) + N° de identificación, Estado civil, Domicilio real, Profesión, Fecha de nacimiento, % de propiedad y/o votos, ¿Es PEP? (dropdown SI/NO), más un adjunto de "Tipo de documento adjunto" (DNI/LC/CUIT) para subir el documento de identidad — en el test se adjuntaron frente y dorso de un DNI real de prueba.
6. **Domicilio Fiscal** — Calle, Número, Piso, Departamento, Provincia (dropdown), Localidad (combobox con autocompletado/búsqueda) y Código Postal.
7. **Domicilio Comercial** — mismo formulario exacto que Domicilio Fiscal, para la dirección operativa.
8. **Teléfono** — código de país + número de contacto. Es el mismo dato que el Paso 2 del backoffice muestra en "Contacto" como "Sin verificar" hasta que se confirme con OTP.
9. **Datos representantes** — Carácter del representante (dropdown; en el test "Representante Legal" — no se relevaron las demás opciones del dropdown), Documento del representante, Email del representante. Este es el mismo email que en el Paso 2 aparece bajo "Representantes Legales" con estado "No iniciada", y al que en el Paso 4 le llega la invitación para completar el onboarding personal.
10. **Declaración** — tres checkboxes de condición especial (Sujeto Obligado / domicilio fiscal en el exterior-OCDE / domicilio fiscal en EEUU-FATCA) o "Ninguna de las anteriores". No se relevó qué campos adicionales pide el formulario si se tilda alguna de las tres primeras opciones en vez de la última (queda pendiente para una futura sesión si se necesita).
11. **Proceso Completado** — pantalla final de confirmación: avisa que se enviará un email a cada representante/firmante cargado para completar su validación de identidad (dispara el Paso 4), y que la solicitud será evaluada por un ejecutivo en unos días. A partir de acá la solicitud ya es visible en el backoffice, en estado "Pendiente Revisión" / Nivel "Oficial De Negocio" (arranca el Paso 2).

**Confirma además, desde el lado de carga, dos cosas ya documentadas desde el backoffice:** que "Propietario Directo" y "Beneficiario Final" son dos sub-formularios independientes (no una sola sección, coherente con la corrección ya capturada en [`2026-09-21_onboarding_menu_documentos_falta_vs_pendiente_y_propietario_directo.md`](2026-09-21_onboarding_menu_documentos_falta_vs_pendiente_y_propietario_directo.md)); y que el email del representante cargado acá es el mismo campo editable que el Paso 2 puede corregir desde "Representantes Legales" si llegó mal cargado.

Fuente: manual de uso construido en la misma sesión — ver [`2026-09-21_manual_onboarding_pj_operador.html`](../proyecto-la-virginia-ob-pj/artefactos/2026-09-21_manual_onboarding_pj_operador.html), que ahora documenta el Paso 1 completo (este) más los Pasos 2 y 3, con capturas de pantalla reales de una carga end-to-end.
