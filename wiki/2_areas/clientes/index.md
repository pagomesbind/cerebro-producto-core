# 🛒 Clientes Bind PSP — Índice del módulo

> **Fuente:** base Notion "Brochure Clientes Bind PSP" → data source "Legajos de clientes" (`collection://4a001976-ca20-4ab1-ad6b-6cf2e0559c01`).
> **Mantenimiento:** carga inicial manual (julio 2026) + sincronización incremental semanal vía skill `/sync_customers`.
> **Propósito:** contexto de producto — entender qué productos integra cada cliente, cómo los opera según su caso de negocio, y qué versatilidad demuestran nuestros productos en distintos rubros. **No** es un legajo comercial/legal: acá no se guardan CUIT, CBU, contactos ni documentación legal.

## Archivos del módulo

| Archivo | Contenido |
|---|---|
| [log_clientes.md](log_clientes.md) | **Log maestro**: una fila por cliente (estado, productos, rubro, tamaño, riesgo, última edición en Notion) + fecha del último barrido de sincronización. |
| [casos_de_uso_clientes.md](casos_de_uso_clientes.md) | Ficha por cliente con contenido sustantivo: modelo de negocio, cómo opera los productos, pricing (esquema + números), volúmenes, particularidades y cronología. |
| [patrones_transversales.md](patrones_transversales.md) | Síntesis viva: versatilidad de cada producto por rubro, patrones de pricing observados, arquetipos de caso de negocio. |

## Tabla de mapeo: "Productos" de Comercial → Productos canónicos

Comercial etiqueta como "Productos" lo que en nuestra taxonomía son **funcionalidades/canales** de un producto. Este mapeo es obligatorio en toda ingesta; la etiqueta comercial original siempre se conserva junto al producto canónico.

| Etiqueta Comercial (Notion) | Producto canónico | Nota |
|---|---|---|
| QRI | Adquirencia | QR interoperable (canal de cobro) |
| Botón de Pago | Adquirencia | Botón Simple |
| Botón de Pago 2.0 | Adquirencia | Botón Simple 2.0 |
| POS | Adquirencia | Terminales |
| RxT | Adquirencia | Recaudación por Transferencia |
| Deuda | Adquirencia | ⚠️ etiqueta ambigua — ver gaps |
| Liquidador | Adquirencia | ⚠️ etiqueta ambigua — ver gaps |
| Monitoreo | Adquirencia | ⚠️ etiqueta ambigua — ver gaps |
| Debin Recurrente | Adquirencia | ⚠️ podría ser funding de Wallet — ver gaps |
| Agente de Cobros y Pagos | Agente de Cobros y Pagos | |
| Agente de Pagos | Agente de Cobros y Pagos | Variante solo-pagos |
| Wallet | Wallet | Wallet as a Service / PSP |
| Dolar CCL | Wallet | Funcionalidad FX |
| recargas | Wallet | ⚠️ etiqueta ambigua — ver gaps |
| Onboarding | Onboarding | |
| "Solución de Cobros" (texto libre) | Adquirencia + Agente de Cobros y Pagos | Nombre histórico conjunto |

Etiquetas nuevas no listadas acá: mapear con mejor criterio, conservar la etiqueta original y registrar la duda en `../gaps_y_preguntas.md`.
