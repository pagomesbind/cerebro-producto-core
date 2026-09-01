---
id: 2026-08-31_wallet_restricciones_alias_cbu_cvu_coelsa
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_meetings — reuniones \"Daily producto\" (docId 1FmdGdYQNIjTh6eu1nvntVCEmxVJA8-P5TGAXRwLzX9E) y \"Web de developers\" (docId 1_spgwib2p1_-J9Znh7ZENtBsUo4wj8c8sDAopcA0WRE), ambas 2026-08-28"
producto: wallet
tema: Restricciones de Coelsa/BCRA para modificar el alias de un CBU/CVU corto
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/apis_expuestas/cvu/guia_cvu.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

## Restricción de cantidad/formato para modificar el alias de un CBU/CVU corto

`guia_cvu.md` (según lo que ya documenta el proyecto `alias_cvu_checkout/`, ver su §"Contexto leído del Cerebro") registra la ventana de 24hs entre modificaciones de alias y que Coelsa asigna un alias arbitrario si Bind no lo hace dentro de los 5 segundos de creado el CBU/CVU — pero **no documenta un tope anual de modificaciones ni el formato válido del alias**. Dos reuniones independientes del mismo día (2026-08-28) citan ambos datos, de forma consistente entre sí:

- **Reunión "Daily producto"** (Pablo Gomes explicando las restricciones conocidas a Nicolás Colón, mientras trabajaban el discovery de `alias_cvu_checkout/`): *"tenemos restricciones de cuelsa que no permite asignar/modificar un alias existente vinculado a un CBU en un plazo menor a 24 horas desde la última vez y [con un límite de] tres [o diez] veces por año"* — el número exacto quedó ambiguo en la minuta (dictado "tres o diez"), sin poder distinguir cuál de los dos es el correcto solo con esta fuente.
- **Reunión "Web de developers"** (Franco Gimenez, documentando la funcionalidad para el portal público de developers, citando explícitamente la normativa del BCRA): el alias de CBU corto **puede modificarse un máximo de diez (10) veces al año** y **debe contener entre 6 y 20 caracteres**.

**Lectura combinada:** el número correcto parece ser **10 modificaciones/año** (coincide entre ambas fuentes, y la de "Web de developers" es más precisa por citar la normativa BCRA de origen) — la mención de "tres" en "Daily producto" probablemente fue un lapsus o confusión del orador con otro límite no identificado. El dato de **6-20 caracteres** es aporte nuevo, no mencionado en ninguna fuente anterior del Cerebro. Esto cierra el gap explícito que dejó abierto el discovery de `alias_cvu_checkout/proyecto.md` (2026-08-28): *"guia_cvu.md ... No documenta el límite de 10 modificaciones/año que citó el PM — dato nuevo, no está en el Cerebro."*

> Fuente: reuniones "Daily producto" (2026-08-28, 15:10) y "Web de developers" (2026-08-28, 16:03), minutas Gemini.
