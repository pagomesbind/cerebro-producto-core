---
id: 2026-09-18_cobro_regla_devolucion_r_por_t_fuera_de_plazo
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones' (2026-09-14), minuta Gemini"
producto: adquirencia
tema: la devolución de transferencias (R por T) no se puede hacer pasado un mes, por diseño — pero clientes institucionales lo exigen igual
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/index.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Regla de producto vigente

Gonzalo Rivera reportó un caso donde no se puede devolver desde el portal una transferencia de una CBU corta porque ya pasó un mes desde la operación. Nicolás Colón explicó que esto es una definición de producto original, no un bug: las devoluciones de **R por T** (recibo por transferencia) se diseñaron para replicar el comportamiento que impone Coelsa para los códigos QR (que también tienen una ventana de devolución acotada), y cambiar ese límite requiere desarrollo — no es solo un parámetro.

## Presión de clientes que rompe la regla

Gonzalo Rivera advirtió que esta limitación ya generó conflicto real con clientes institucionales: un **ministerio** reclamó devolver una transacción con más de un mes de antigüedad y, ante la negativa por regla de negocio, contestó explícitamente que no le importaba la regla y que había que devolverla igual. **Rifsa** planteó el mismo reclamo antes. Pablo Gomes instruyó a Nicolás Colón a "levantar" el pedido (registrarlo como candidato a desarrollo) pero remarcó que antes hay que evaluar el costo de implementarlo y si vale la pena, en vez de comprometerse directo. El caso puntual que originó la discusión (Ciencias Económicas) resultó ser una transferencia por QR, no R por T, así que no aplica de todos modos — pero la tensión de fondo (clientes grandes que exigen devolución sin importar el plazo) queda abierta como pedido a evaluar.
