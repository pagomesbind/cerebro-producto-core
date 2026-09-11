---
id: 2026-09-10_conocimiento-global66-reactivacion-cvu-manual-swagger
pm: nicolas
fecha_captura: 2026-09-10
fuente: "Reunión \"Daily producto\" (2026-09-09, 09:31), minuta Gemini"
producto: wallet
tema: Global 66 — eliminar y reactivar una Clave Virtual Uniforme genera una CVU nueva en vez de reactivar la anterior, por tratarse de cuentas migradas sin identificador de cuenta original
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 201b3e0
---

**Hallazgo:** en Global 66, al eliminar y volver a dar de alta una Clave Virtual Uniforme (CVU) a través del endpoint de la billetera, el sistema genera una **CVU nueva** en lugar de reactivar la anterior. Causa raíz: esas cuentas provienen de **migraciones previas** y no se crearon originalmente con un identificador de cuenta propio del sistema actual. Luciana Rudaz confirmó que Astropay tuvo exactamente el mismo problema en el pasado, por el mismo motivo de migración de claves.

**Alcance:** afecta únicamente a **3 usuarios/cuentas de Global 66** — no es una situación masiva.

**Solución propuesta (Pablo Gomes):** incorporar un atributo de identificador de cliente y desarrollar una lógica específica para los casos que provienen de migraciones.

**Decisión operativa provisional (estado "Requiere más debate"):** hasta que exista esa solución, la organización de Global 66 puede seguir eliminando CVU libremente, pero debe **solicitar la reactivación de forma manual** — el equipo ejecuta el alta manual vía Swagger en APIBank y actualiza los registros con un script, según el volumen de casos.

> Fuente: Reunión "Daily producto" (2026-09-09, 09:31), minuta Gemini.
