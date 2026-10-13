---
id: 2026-10-13_cumplimiento_conocimiento_a7724_correccion_alcance_y_seccion_11
pm: pablo
fecha_captura: 2026-10-13
fuente: "PDF de la Comunicación 'A' 7724 del BCRA (10/03/2023, texto original de 76 páginas, RUNOR 1-1785) y PDF de la Com. 'A' 7783 (02/06/2023), ambos aportados por el PM en raw/ el 2026-10-13; comparados contra el archivo del canon ingestado el 2026-09-08"
producto: transversal
tema: Corrección del archivo de la A 7724 — Sección 11 (Canales Electrónicos) derogada por la A 7783, alcance a PSP por la A 7783, vigencias y notificaciones a la GAES
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/gestion_riesgo_tecnologia_seguridad_a7724.md
tipo_destino: actualizar
contradice: "3_recursos/cumplimiento_normativo/gestion_riesgo_tecnologia_seguridad_a7724.md — (1) lista 'Canales Electrónicos' como Sección 11 vigente con ~90 requisitos: la Com. A 7783 (02/06/2023) derogó esa Sección 11; (2) dice que A 7783 'fue citada pero no conseguida' y que la aplicabilidad a PSP es solo una posición del PM: la A 7783 está disponible y nombra a los PSP como sujetos obligados (1.1.2); (3) la numeración de las 11 secciones que lista no coincide con el texto ordenado (la Sección 11 actual es el Glosario)."
confianza: alta
estado: en_cola
merge_commit:
---

## Qué hay que corregir en `gestion_riesgo_tecnologia_seguridad_a7724.md`

El archivo del canon se armó el 2026-09-08 desde el texto **original** de la A 7724 (10/03/2023). Ese texto fue modificado tres meses después por la A 7783. Con ambos PDFs a la vista:

1. **La Sección 11 "Canales Electrónicos" ya no existe.** El texto original la traía (ATM, terminales de autoservicio, banca móvil, telefónica, por Internet, POS, plataformas de pagos móviles, con una matriz de escenarios de riesgo). La Com. "A" 7783 la **derogó** y la reemplazó por un texto ordenado propio para servicios financieros digitales (ver el archivo nuevo `servicios_financieros_digitales_a7783.md`). En el texto ordenado vigente (versión 2a, 29/11/2023) la Sección 11 es el "Glosario de términos". La frase del archivo "~90 requisitos técnico-operativos puntuales de Canales Electrónicos" debe eliminarse. Estructura vigente de la A 7724: Sección 1 Disposiciones generales, 2 Gobierno de tecnología y seguridad de la información, 3 Gestión de riesgos, 4 Gestión de la tecnología (incluye gestión de proyectos, presupuesto y gestión de datos), 5 Gestión de la seguridad de la información (5.5 capacitación, 5.7.2 factores de autenticación, 5.8 eventos), 6 Continuidad del negocio, 7 Infraestructura tecnológica y procesamiento, 8 Gestión de ciberincidentes, 9 Desarrollo, adquisición y mantenimiento de software (9.1 registros de auditoría), 10 Gestión de la relación con terceras partes, 11 Glosario.
2. **Sujetos obligados de la A 7724:** 1.1.1 entidades financieras y 1.1.2 infraestructuras del mercado financiero (INTERBANKING, COELSA, LINK y PRISMA), agregadas por la A 7783. **Los PSP no figuran en la A 7724.** Quedan alcanzados por la **A 7783 (1.1.2 PSP)**, cuya Sección 1.2 los obliga a gestionar tecnología, seguridad de la información, infraestructura, software y terceras partes "en concordancia con" la A 7724. Esto cambia el estatus de la aplicabilidad registrada el 2026-09-08: ya no es solo "posición del PM" ("una PSP es una entidad financiera"); hay una referencia normativa expresa. Sigue sin ser un dictamen legal formal.
3. **Vigencias.** La A 7724 entró en vigor a los 180 días corridos de su difusión (≈ septiembre de 2023). La A 7783, a los 180 días de su difusión; los textos ordenados figuran vigentes desde el 29/11/2023. No hay plazos de adecuación futuros: el BCRA audita cumplimiento actual.
4. **El archivo debe dejar de decir que la A 7783 "no fue conseguida".** Ya está en el Cerebro.

## Obligaciones de notificación y reporte a la GAES (no estaban registradas)

La A 7724 obliga a informar a la Gerencia de Auditoría Externa de Sistemas (GAES) de la SEFYC en estos casos:

- **Proyectos de nuevos servicios financieros digitales o cambios en la modalidad de los existentes** cuando traten datos de clientes y de usuarios de servicios financieros, datos contables y/o transaccionales (punto 4.3.1, gestión de proyectos). Sin plazo expreso en este punto; la A 7783 fija **60 días antes de la puesta en producción** para nuevos productos o tipos de servicio (ver el archivo nuevo).
- **Delegación en terceras partes (Sección 10):** antes de iniciar la relación, informar a la GAES las características del proceso, servicio o actividad a delegar. Las delegaciones no transfieren las responsabilidades primarias. Aplica al análisis de proveedores como Fintexa, Worldsys, Socialnet, FaceTec o cualquier proveedor nuevo.
- **10.4 Informes de auditoría:** auditorías internas sobre los procesos delegados en terceros, con revisión del cumplimiento legal y regulatorio; los informes y los de los auditores externos sobre esos servicios se remiten a la GAES, con periodicidad según el riesgo y la criticidad del servicio delegado.
- Capacitación y concientización (5.5): programas revisados al menos una vez al año, con informe a la Alta Gerencia sobre su efectividad.
- **Registros de auditoría de sistemas y aplicaciones (9.1):** cada acción debe quedar registrada con identificación unívoca, tipo de evento o acción, fecha y hora, usuarios intervinientes, dispositivo, aplicación o canal de origen y, ante cambios de parámetros, el valor anterior y posterior. Deben protegerse en integridad, disponibilidad y confidencialidad. La información que da soporte a los registros contables y los registros de auditoría debe conservarse **recuperable por no menos de 6 años** y estar **disponible de inmediato** si la GAES la requiere. Se exige además documentación funcional, técnica y de usuario actualizada de los sistemas. (La A 7783, punto 4.1, remite a este requisito.)

La regla de plazo de 180 días para corregir "errores de encuadramiento" detectados por auditorías (punto 11.3.1.4 del texto original) formaba parte de la Sección 11 derogada y no debe tomarse como vigente.
