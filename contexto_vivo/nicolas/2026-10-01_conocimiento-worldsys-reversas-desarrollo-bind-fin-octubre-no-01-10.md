---
id: 2026-10-01_conocimiento-worldsys-reversas-desarrollo-bind-fin-octubre-no-01-10
pm: nicolas
fecha_captura: 2026-10-01
fuente: "Mail 'Re: Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas.' — Nicolás Colón (Bind PSP) 2026-09-30 10:05 ART y respuesta de Leandro Competiello (Worldsys) 2026-09-30 10:08 ART"
producto: transversal
tema: Reversas/comprobantes en LAVADOOPERACIONES — el desarrollo del lado de Bind PSP termina a fines de octubre 2026, no entra el 01/10; Worldsys ajusta su plan y sigue pidiendo los códigos de tipos de operación
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md
tipo_destino: actualizar
contradice: "sí — corrige el item en_cola 2026-09-30_conocimiento-worldsys-reversas-confirma-01-10-pide-codigos-tipos-operacion (decía que la captura arrancaba el 01/10/2026 y que no había respuesta de Bind en el hilo) y el 2026-09-16_conocimiento-worldsys-reversas-comprobantes-resuelto-octubre (entrada en vigor con el procesamiento del 01/10)"
confianza: alta
estado: en_cola
---

**Corrección sobre §2 de `reporteria_worldsys_bcra.md`.** Sigue a los items del 2026-09-29 y 2026-09-30 (ambos `en_cola`). El barrido del 30/09 no vio los dos últimos mensajes del hilo. Por eso decía que Bind no había respondido y que el esquema arrancaba el 01/10. Las dos cosas quedan corregidas abajo.

11. **Bind PSP respondió el 30/09 (Nicolás Colón, 10:05).** El desarrollo de los cambios en el archivo de Bind PSP **sigue en curso**. La fecha estimada de **finalización y puesta en producción es a fines de octubre de 2026**. Los cambios son tres: `IdComprobante` en `NUMEROOPERACION`, la interfaz `TiposComprobantes` en lugar de la lista fija de `TIPOOPERACION`, y los registros de devolución con monto negativo. Mientras tanto, Bind ofrece ir mandando el listado de tipos de comprobante.
12. **Worldsys ajusta el plan (Leandro Competiello, 10:08).** Worldsys había entendido, por lo hablado con María Victoria Simonetti (PLA/FT/FP), que el cambio tenía que estar listo a fines de septiembre para capturar en producción desde octubre. Acepta la nueva fecha sin objeciones ("nos ocupamos de ajustar"). Igual **pide que Bind le mande ya los tipos de operación** para parametrizarlos.
13. **Implicancia.** El esquema de reversas con monto negativo **no aplica al procesamiento de alertas del 01/10/2026**. Lo más pronto que puede entrar es el procesamiento de noviembre, siempre que el desarrollo salga a fines de octubre. Hasta entonces sigue el riesgo que marcó Diego Scaldaferri (Gerente de Cumplimiento PLA/FT/FP, 10/09): las reversas suman en los acumuladores de alertas. Con eso aparecen falsos positivos y queda un "potencial riesgo no visualizado". El prerequisito que sigue abierto es el envío del listado de tipos de comprobante, que ya no depende de la fecha del desarrollo.

Sigue sin confirmarse en el hilo si llegó y se aprobó el documento de alcance y horas que Worldsys prometió el 15/09. Tampoco se sabe si Compliance (Simonetti/Scaldaferri) estaba al tanto de la fecha de fines de octubre. Worldsys dice que entendió otra cosa hablando con Simonetti.

> Fuente: Mail "Re: Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas." — Nicolás Colón (2026-09-30 10:05 ART) y Leandro Competiello, Worldsys (2026-09-30 10:08 ART).
