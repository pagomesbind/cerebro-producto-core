---
id: 2026-09-03_adquirencia_id_coelsa_comprobante
pm: pablo
fecha_captura: 2026-09-03
fuente: "Reunión Análisis COBRO (2026-09-03 12:04), minuta Gemini"
producto: adquirencia
tema: ID Coelsa en campo ID externo de comprobantes de acreditación wallet
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_webhook_cobro.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

# ID Coelsa en comprobantes de acreditación wallet

## Decisión acordada (2026-09-03)
Se acordó insertar el **ID Coelsa** en el campo **ID externo** de los comprobantes de acreditación en wallet (Cobro QR con acreditación). Este identificador facilita la conciliación bancaria que realiza el equipo de administración.

**Motivo:** Actualmente el campo de referencia contiene el ID de transacción interno. Insertar el ID Coelsa en ID externo estandariza el proceso de conciliación con otros tipos de comprobantes (impuestos, etc.) y evita duplicación manual de trabajo.

**Impacto:** Mejora operativa: automatiza parte del flujo de conciliación bancaria en administración de Wallet.

## Detalles técnicos
- **Campo:** ID externo de comprobante de acreditación Wallet (Cobro QR)
- **Contenido:** ID Coelsa (en lugar de derivarlo de otra fuente)
- **Beneficiarios:** Equipo de administración (conciliación), clientes (comprobantes)
- **Asociado:** Cambios en configuración de canales QR Tarjeta (ver Gono)

## Próximos pasos
[Nicolás COLÓN] Implementar inserción del ID Coelsa en campo ID externo de comprobantes

> Fuente: Reunión "Análisis COBRO" (2026-09-03 12:04), minuta Gemini
