---
id: 2026-09-07_conocimiento-coelsa-conciliacion-cashout-cas-y-cuadraturas-fci
pm: nicolas
fecha_captura: 2026-09-07
fuente: "Reunión \"Daily producto\" (2026-09-07) + reunión \"Weekly - Producto / Operaciones\" (2026-09-07)"
producto: wallet
tema: Ajustes de conciliación Coelsa (inclusión de cashout/CAS) y corrección de cuadraturas de wallet por fondos comunes de inversión
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Dos ajustes de conciliación/cuadratura de Wallet acordados/detectados el mismo día, en reuniones distintas pero sobre el mismo dominio:

**1. Conciliación Coelsa — inclusión de transferencias cashout y CAS (reunión "Daily producto"):** se acordó modificar la conciliación de Coelsa para que contemple, además de las transferencias inmediatas entrantes, las transferencias de tipo **cashout** y **CAS**. Matías Alzogaray indicó que esta corrección, junto con un mecanismo de reintento automático para la asignación de alias (**nota: este reintento de alias parece coincidir con el fix ya documentado en `validaciones_y_alias_cvu.md` vía tickets WS-1556/DEM-1828, mergeado el 2026-09-03** — a confirmar en el merge si es la misma mejora reafirmada o una extensión nueva, para no duplicar), debería reducir los problemas que un cliente (mencionado como "Pago Nube" en la minuta) presenta con CBU Collect. Ver gap sobre identidad de este cliente en `contexto_vivo/2026-09-07_gap-tienda-nube-pago-nube-sin-ficha-en-log-clientes.md`.

**2. Cuadraturas de billetera por fondos comunes de inversión (reunión "Weekly - Producto / Operaciones"):** María Eugenia Vila detectó que las cuadraturas actuales de billeteras muestran diferencias incorrectas porque solo consideran los saldos de cuentas principales y **no incluyen los saldos retenidos en fondos comunes de inversión (FCI)** para entidades como **La Virginia** y **Copel** — nota: "Copel" en la minuta probablemente corresponde al cliente **COPPEL** (Wallet, Onboarding — ver `log_clientes.md`), dado el patrón de errores de transcripción de Gemini ya observado con otros nombres de cliente. Se determinó que el diseño de cuadraturas debe modificarse para sumar estos saldos y reflejar el balance real.

Adicionalmente (mismo bloque de la reunión "Weekly"), se propuso — sin decisión firme, "Requiere más debate" — programar un **proceso automático de conciliación horaria de transferencias entrantes de billeteras para todas las organizaciones** (hoy no hay ese automatismo); pendiente de validar capacidad técnica. Ver tarea T-033 en `tareas.md` y decisión pendiente en `1_proyectos/tareas.md`.

> Fuente: Reunión "Daily producto" (2026-09-07, minuta Gemini) + reunión "Weekly - Producto / Operaciones" (2026-09-07, minuta Gemini).
