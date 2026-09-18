---
id: 2026-09-17_conocimiento-endpoint-refund-tipo-contracargo-desconocimiento
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Sesión /idea_solution sobre ardid_desconocimientos, transcripción directa del PM (2026-09-17), sin documento formal cruzado"
producto: adquirencia
tema: Contrato técnico (Verbal) del endpoint interno que marca un contracargo como "desconocimiento"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

El endpoint interno de uso exclusivo de Operaciones que hoy usa Administración para marcar una transacción de Botón Simple como "desconocimiento" (ya documentado funcionalmente en §0 de este archivo — "Desconocimientos de tarjeta") tiene el siguiente contrato técnico, según lo transcribió el PM directamente en el chat (sin Swagger ni documento formal citado — **nivel de confianza Verbal, no Confirmado**):

**`POST https://10.22.0.35/api/v1/Transactions/refund`**

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

Es el mismo endpoint genérico de "refund"/contracargo — el campo `tipoContracargo` (`"desconocimiento"` vs. lo que sea que use para "devolución" estándar) es lo que lo diferencia, consistente con la mecánica ya documentada ("se reutiliza todo el motor de devoluciones existente, solo cambia el tipo de contracargo"). No se confirmó en esta sesión la URL de qué ambiente es (la IP interna no indica si es Staging o Producción), ni el contrato de response/códigos de error/idempotencia.

Dato adicional relevante: existe un webhook de contracargo ya construido (documentado en este mismo archivo, sección de "Documentación: devoluciones parciales") que sí trae un par clave-valor `Tipo: Desconocimiento` — es decir, el webhook ya distingue este caso, aunque el proyecto que originó esta captura decidió no usarlo como disparador de su automatización (por simplicidad, no por limitación técnica del webhook).
