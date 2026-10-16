---
id: 2026-10-07_clientes_coppel_cuentas_de_menores_discovery
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Coppel | Cuenta menores' (2026-10-07, 11:00, con Open Pass)"
producto: wallet
tema: Coppel (vía integrador Open Pass) arranca discovery comercial/técnico de cuentas para menores de edad, lanzamiento objetivo enero 2027
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto

Coppel (cliente ya fichado en `log_clientes.md` — Wallet+Onboarding, retail, grande) arrancó junto a su integrador **Open Pass** el discovery de un nuevo producto: **cuentas para menores de edad**. Reunión de kickoff comercial/técnico/compliance, expectativa de negocio de Coppel: **lanzamiento al mercado a fines de enero de 2027**.

## Definiciones y puntos abiertos

- **Propuesta comercial y contrato nuevo**: Mauro Suppan (Fintexa) elabora propuesta comercial específica; se requiere **un nuevo contrato** antes de iniciar la integración técnica.
- **Umbral transaccional para menores**: PLD exige un umbral inferior al de cuentas adultas — todavía sin definir el monto exacto (`Requiere más debate`).
- **Bloqueo automático por umbral**: se acuerda desarrollar un mecanismo que bloquee/dé de baja automáticamente la CVU corta del menor al superar el umbral mensual.
- **Flujo de onboarding**: Open Pass propone reutilizar el **flujo de onboarding único** existente, enviando los datos del tutor tras una invitación directa — pendiente validación interna de compliance/producto/PLD (`Requiere más debate`). Un flujo separado específico para menores requeriría rediseñar la experiencia desde cero (limitación de tiempo ya existente en el flujo único actual).
- **Control de egresos**: Open Pass controlará y limitará los egresos de dinero de los menores en su plataforma — los ingresos no se pueden bloquear por restricciones generales del mercado.
- **Estados intermedios y consentimiento**: el sistema de Bind no contempla hoy de forma nativa un estado intermedio para cuentas de menores antes de la activación — Pablo Gomes evalúa si se puede soportar con ajustes mínimos. El consentimiento del tutor debe quedar registrado y validado conforme a cumplimiento.
- **Cuenta remunerada**: **excluida en esta primera etapa** para menores — el proveedor externo de ese servicio no tiene fecha definida para ofrecerlo a este segmento.
- **Validación de parentesco**: Open Pass la resuelve por cuenta propia.
- **Coordinación con el refactor de incorporación en curso**: Pablo Gomes advirtió que el proyecto de rediseño de flujos de incorporación (cierre estimado fin de año) requerirá que las organizaciones migren y entreguen información adicional de legajos (ej. pruebas de vida) por exigencia de cumplimiento — sugiere coordinar este trabajo junto con el de cuentas de menores para evitar desarrollo duplicado.

## Hallazgos operativos no relacionados con menores (misma reunión)

- **Archivos de conciliación desactualizados desde el 5 de octubre** — Open Pass/Bind deben investigar la causa del retraso en la generación automática.
- **Falta de archivo automático de saldos diarios de FCI** por cuenta — Bind está desarrollando un endpoint para entregarlo hacia fines de octubre; mientras tanto se evalúan alternativas manuales temporales.

## Próximos pasos

Open Pass comparte diagrama detallado del flujo de onboarding propuesto y un cronograma general con tareas/dependencias (Gantt). Bind revisa segmentación de transacciones para PLD con Rocío/Maru.

> Fuente: reunión "Coppel | Cuenta menores", 2026-10-07 11:00hs (Pablo Gomes, Adriana Endzeliz, Gonzalo Rivera, Mauro Suppan/Fintexa, equipo Open Pass — Paola Morici, Francesca Calcaterra, Mariana Sigal).
