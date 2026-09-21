# Desconocimientos de tarjeta (Botón Simple) — contracargo total de uso interno

> Estado: en producción (mecánica base y código `004` en archivo de liquidación) — separación de conceptos en el PDF de comercio confirmada para AD V73 (24/09/2026).
>
> Extraído de [devoluciones_y_contracargos.md §0](devoluciones_y_contracargos.md) por umbral de tamaño (2026-09-21) — no confundir con las devoluciones/contracargos estándar documentados ahí: un "desconocimiento" es el caso donde el titular de la tarjeta niega haber hecho la compra.
>
> Fuente: Notion histórico, Epic **"Desconocimientos de tarjeta"** (Dolor); Mail "Análisis COBRO: Lun, 10 de ago de 2026" (malzogaray@bind.com.ar); Reunión "Análisis COBRO" (2026-09-07); sesión de trabajo directa con el PM (2026-09-17); Reunión "Análisis de riesgo: AD V 73" (2026-09-17), minuta Gemini.

## Mecánica base

- **Endpoint de uso exclusivamente interno** (Operaciones Bind PSP, vía Swagger o luego desde el Admin) — nunca expuesto a las entidades/comercios. Marca una transacción de Botón Simple como desconocimiento por transacción.
- Efecto: crea un **contracargo de tipo "desconocimiento"** (total, no parcial — distinto de los contracargos tipo "devolución" ya soportados), pasa la transacción a estado `DEVUELTA`, y registra el timestamp del desconocimiento.
- **Se liquida exactamente igual que una devolución** (mismo criterio de impuestos, archivos y PDF de comercio) — resta en la liquidación al comercio en el siguiente día hábil a la fecha de desconocimiento. Es decir: técnicamente reutiliza todo el motor de devoluciones existente, solo cambia el tipo de contracargo y quién puede dispararlo.

## Implementación PRD-146/AD-1360 (agosto 2026)

> Fuente: Mail "Análisis COBRO: Lun, 10 de ago de 2026" — malzogaray@bind.com.ar, 2026-08-10.

- **Código `004`** identifica el desconocimiento como tipo de contracargo diferenciado de la devolución en el archivo/registro de liquidación — resuelve un bug de importes en cero que ocurría al no distinguirlos.
- El PDF de liquidación suma un apartado propio "Detalle de desconocimientos" + columna nueva en el resumen, sin alterar el total liquidado.
- **No existe el concepto de "desconocimiento parcial"**: cualquier desconocimiento se aplica sobre el remanente total de la transacción.
- **Estrategia de emisión tolerante a fallos:** el PDF de liquidación se emite siempre, incluso con inconsistencias de datos — se prioriza la disponibilidad del comprobante sobre la consistencia (correcciones reactivas post-emisión).
- Detalle completo del seguimiento de este desarrollo en PRD-146 (Tratamiento de contracargos de tarjeta) — proyecto de Nicolás Colón, vive en su propio Cerebro desde 2026-08-13.
- **Ratificación de prioridad (2026-09-07, "Análisis COBRO"):** el tablero de incidentes ratificó el estatus de **máxima prioridad** para PRD-146, ya iniciado bajo múltiples tickets de Fintexa: [DAD-2209](https://fintexa.atlassian.net/browse/DAD-2209), [DAD-2257](https://fintexa.atlassian.net/browse/DAD-2257). Acción de seguimiento acordada: revisar el avance de estos tickets una vez compartidos (owner: Daniela Collia, Fintexa), sin fecha límite definida. Detalle operativo completo en el Cerebro de Nicolás Colón.

## Contrato técnico del endpoint (2026-09-17, confianza Verbal — no Confirmado)

Transcripto directamente por el PM en sesión de trabajo, sin Swagger ni documento formal citado.

```
POST https://10.22.0.35/api/v1/Transactions/refund
```

Body:
```json
{
  "commerceCode": "${codigoComercio}",
  "identifyOrder": "${identificadorOrden}",
  "partial": false,
  "amountGross": "${monto}",
  "description": "${motivo}",
  "entityIdentifier": "${entidadIdentificador}",
  "channel": "BotonSimple",
  "tipoContracargo": "desconocimiento",
  "deudaId": "${deudaId}",
  "transaccionId": "${transaccionId}"
}
```

Es el mismo endpoint genérico de "refund"/contracargo — el campo `tipoContracargo` (`"desconocimiento"` vs. el valor usado para "devolución" estándar) es lo que lo diferencia, consistente con la mecánica base ("se reutiliza todo el motor de devoluciones existente, solo cambia el tipo de contracargo"). No se confirmó en esta sesión de qué ambiente es la URL (la IP interna no indica Staging o Producción), ni el contrato de response/códigos de error/idempotencia. El webhook de contracargo documentado en [devoluciones_y_contracargos.md §1](devoluciones_y_contracargos.md) sí trae un par clave-valor `Tipo: Desconocimiento` — es decir, ya distingue este caso, aunque el proyecto `ardid_desconocimientos` (ver [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md)) decidió no usarlo como disparador de su automatización, por simplicidad y no por limitación técnica del webhook — en cambio se engancha directo al final de este endpoint.

## Separación de desconocimientos y devoluciones en PDF y liquidación — confirmada para AD V73 (2026-09-17)

> Fuente: Reunión "Análisis de riesgo: AD V 73" (2026-09-17), minuta Gemini.

Matias Alzogaray, Maria Eugenia Vila y Maximiliano Ambrosini confirmaron, para la versión **AD V73** (despliegue 24/09/2026), la separación de **desconocimientos (contracargos) y devoluciones** tanto en los archivos de liquidación como en los reportes en formato PDF. Maximiliano Ambrosini detalló que el PDF mostrará ambos conceptos por separado, con distintos códigos (el código `004` ya identifica el desconocimiento en el archivo de liquidación desde PRD-146/AD-1360 — ver arriba; esta novedad extiende la misma separación también al **PDF** de cara al comercio). Como decisión, Gonzalo Damian Rivera indicó que se debe avisar previamente a los clientes y modificar el portal de desarrolladores con el nuevo formato de archivos; post-implementación se validará la correcta emisión.

**Resuelve un pendiente ya documentado:** esto es la confirmación, para AD V73, del ticket 361 (vinculado al 2209) que en la reunión "Análisis COBRO" del 2026-09-03 había quedado "pendiente de más debate" sobre si entraba en la v73 o la v74 — corrección del PDF de liquidaciones para el cliente **Coto**, diferenciando "desconocimiento" de "devolución" (ver [webhooks_y_notificaciones.md](webhooks_y_notificaciones.md), última sección). La novedad extiende/ratifica esa separación con códigos distintos también en el PDF, con aviso previo a clientes y actualización del portal de desarrolladores antes del despliegue.

## Ver también

- [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) — mecánica general de contracargos/devoluciones estándar (no desconocimientos).
- [webhooks_y_notificaciones.md](webhooks_y_notificaciones.md) — webhook de arancel neto y otras notificaciones de cobro.

---
*Última actualización: 2026-09-21 — `/context_merge`: archivo nuevo, extraído de `devoluciones_y_contracargos.md §0` por umbral de tamaño; nueva sección "Separación de desconocimientos y devoluciones en PDF y liquidación" (reunión "Análisis de riesgo: AD V 73", 2026-09-17).*
