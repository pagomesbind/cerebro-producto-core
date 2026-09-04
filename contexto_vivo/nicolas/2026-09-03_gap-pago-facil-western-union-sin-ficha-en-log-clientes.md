---
id: 2026-09-03_gap-pago-facil-western-union-sin-ficha-en-log-clientes
pm: nicolas
fecha_captura: 2026-09-03
fuente: "Reunión \"Análisis COBRO\" (2026-09-03)"
producto: transversal
tema: Pago Fácil/Western Union (Guillermo Paolucci) aparece como cliente activo en tareas.md (Proyecto Servicios, SER-66) y en conversaciones comerciales nuevas, pero no tiene fila propia en 2_areas/clientes/log_clientes.md
tipo: gap
destino_propuesto: 2_areas/clientes/log_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Análisis COBRO" (2026-09-03), Pablo Antonio Gomes mencionó conversaciones comerciales en curso para integrar cobro de facturas y extracción de efectivo mediante QR en sucursales de **Pago Fácil**, con advertencia sobre requerimientos regulatorios de PLD (separar operaciones de extracción de efectivo de los pagos estándar, límites transaccionales por operación y acumulados mensuales por pagador).

Este mismo cliente (bajo el nombre "Western Union/Pago Fácil", contacto Guillermo Paolucci) ya aparece como relación activa en `wiki/1_proyectos/tareas.md` (T-013, T-015) ligado al ticket [SER-66](https://bindpsp.atlassian.net/browse/SER-66) del Proyecto Servicios — pero no se encontró ninguna fila para "Pago Fácil" ni "Western Union" en `2_areas/clientes/log_clientes.md` (verificado por búsqueda de texto sobre las 200 filas del log). Puede ser que el legajo de Notion use otro nombre canónico no evidente, o que sea un cliente todavía no cargado en el barrido de `/sync_customers`. Se deja para que esa skill lo confirme en su próximo barrido de Notion — mientras tanto no corresponde proponer ficha nueva en `casos_de_uso_clientes.md` sin confirmar el cliente en el log maestro.

> Fuente: Reunión "Análisis COBRO" (2026-09-03), minuta Gemini + cruce con `wiki/1_proyectos/tareas.md` T-013/T-015.
