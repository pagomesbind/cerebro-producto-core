---
id: 2026-09-01_adquirencia_parametrizacion_tiempos_qr
pm: pablo
fecha_captura: 2026-09-01
fuente: "/sync_meetings — reunión 'Configuración de tiempos de consulta de Pagos QR' (2026-08-31 14:27, minuta Gemini), con Pablo Gomes, Emma Vignoles, Mariana Nadalin, Gonzalo Rivera, Nicolás Colón, Luciana Rudaz, Hernan Clarich + Fintexa (Agustín Grau, Juan Pablo Carubelli)"
producto: adquirencia
tema: Parametrización del tiempo de espera de resolución de pagos QR/transferencias/Debin (State Monitor)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Nicolás Colón presentó un desarrollo que permite **parametrizar el tiempo de espera de resolución de pagos QR** (aplica también a **transferencias salientes y Debin**), reemplazando el timeout fijo que tenía el sistema. Historial del parámetro: 7s → 5s (ajuste previo, ya en producción) → nueva configuración acordada en esta reunión: **primera consulta a 4,5s + segunda consulta a 2s** (la segunda toma como base la respuesta de la primera). La base estadística usada es de Coelsa: tiempo promedio de resolución entre 4,7s y 4,8s.

**Mecánica del doble chequeo (explicada por Juan Pablo Carubelli, Fintexa):** si tras las dos consultas la transacción no se resuelve, queda en **estado 4 (pendiente)**. El **State Monitor** la toma después; si tampoco logra resolverla, pasa a **estado 5 (auditoría)**. Es la primera vez que se documenta el detalle de esta máquina de estados en el Cerebro — no había referencia previa al State Monitor de QR/Debin en `mecanica_qr_coelsa.md`.

**Motivo de negocio:** el cliente **TPay** reclamó por tiempos de resolución largos y transacciones que quedan en estado indeterminado — el ajuste responde directamente a ese reclamo. Nicolás Colón le va a entregar a Gonzalo Rivera el informe técnico de tiempos para que pueda responderle a TPay.

**Riesgo aceptado y su mitigación:** reducir el tiempo de la primera consulta corre el riesgo de dejar operaciones fuera antes de que Coelsa termine de resolverlas — se espera que la segunda consulta (2s adicionales) mitigue ese efecto. Nicolás Colón monitorea la evolución del cambio y reporta resultados.

**Pendiente identificado en la misma reunión:** Gonzalo Rivera va a cargar en Jira un caso con las transacciones antiguas que quedaron bloqueadas en estado 4, para que el equipo técnico las analice; Juan Pablo Carubelli investiga por qué ciertas operaciones antiguas no pasaron automáticamente al estado de auditoría según la lógica esperada.

> Fuente: Reunión "Configuración de tiempos de consulta de Pagos QR" (2026-08-31), minuta Gemini — sección Detalles.

## Nota — cliente TPay sin ficha en el Cerebro

TPay no aparece en `wiki/2_areas/clientes/log_clientes.md` — no se pudo verificar contexto comercial previo (producto contratado, tamaño, riesgo). Capturado también como item `tipo: gap` separado (`2026-09-01_contexto_fijo_cliente_tpay_sin_ficha.md`) para que `/sync_customers` lo levante en su próximo barrido de Notion.
