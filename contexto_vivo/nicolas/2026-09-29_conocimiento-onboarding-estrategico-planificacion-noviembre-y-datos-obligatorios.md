---
id: 2026-09-29_conocimiento-onboarding-estrategico-planificacion-noviembre-y-datos-obligatorios
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Reunión 'Producto' (2026-09-28) — resumen del mail de Gemini (Drive no disponible, sin minuta detallada)"
producto: onboarding
tema: Onboarding estratégico — fecha objetivo noviembre 2026, domicilio legal y género pasan a ser datos obligatorios a comunicar a clientes, alcance de la lista 15 a definir, baja de inversiones/cuentas comitentes manual mientras no haya endpoints, corrección de vulnerabilidades en validación de identidad
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

La reunión "Producto" del 28/09 ordenó los desarrollos en curso de **Onboarding estratégico**, con **fecha objetivo en noviembre de 2026**. Lo que se habló:

- **Planificación oficial a clientes:** el equipo va a mandar a los clientes la planificación de los cambios que requiere el onboarding estratégico, con la fecha objetivo de noviembre.
- **Datos obligatorios nuevos:** hay que comunicarles a los clientes que es **obligatorio** enviar datos como **domicilio legal** y **género**. La minuta dice "datos como", así que la lista podría ser más larga.
- **Lista 15 (CUIT rechazados PLD BIND):** falta definir si la validación contra la lista 15 se integra en los flujos de onboarding existentes o en el alta de cuenta comitente y totalizadores. Ver `validacion_lista_negra_bind.md`. Queda a cargo de Nicolás Colón.
- **Screening de compliance:** hay que confirmar qué listas de screening son obligatorias en el onboarding. La minuta menciona terrorismo y residencia en Estados Unidos (probable FATCA). Queda a cargo de Nicolás Colón.
- **Baja manual:** mientras no existan endpoints automáticos, se arma un procedimiento manual para la baja de inversiones, el rescate total y la eliminación de cuentas comitentes.
- **Seguridad:** se revisó la corrección de vulnerabilidades en la validación de identidad. Es probable que tenga relación con la vulnerabilidad de Renaper/DNI ya documentada en §1ter, pero no está confirmado. Pablo Gomes va a escribir un documento explicativo sobre la lectura de documentos de identidad (DNI) y un manual de configuración de parámetros de totalizadores. También va a iniciar la revisión del scoring de usuarios.
- **Rechazos por longitud:** hay que investigar por qué se rechazan cuentas con una cantidad alta de caracteres. No se aclara en qué campo.

> Fuente: Reunión "Producto" (2026-09-28), resumen del mail de Gemini.
