---
id: 2026-09-10_gap-contradiccion-limite-operativo-personas-juridicas-1000-vs-10000
pm: nicolas
fecha_captura: 2026-09-10
fuente: "Reuniones \"ARDID\" y \"Join Soporte Clientes\" (2026-09-09), minutas Gemini"
producto: onboarding
tema: Contradicción en el monto del límite operativo para cuentas de personas jurídicas — $1.000 (decisión ya en canon) vs $10.000 (dos reuniones independientes del 09/09)
tipo: gap
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "wiki/2_areas/direccion/decisiones.md (mergeado 2026-09-09 desde contexto_vivo, item 2026-09-08_decision-limite-1000-cuentas-personas-juridicas-sin-documentacion): \"se permite la creación de cuentas de personas jurídicas aplicando un límite operativo máximo de $1.000 hasta que el cliente presente la documentación de respaldo requerida por cumplimiento\" (reunión \"Producto\", 2026-09-08)."
confianza: alta
estado: ingestado
merge_commit: 201b3e0
---

El monto del límite operativo para cuentas CVU de personas jurídicas sin documentación de respaldo aparece con **dos valores distintos** según la fuente, ambos posteriores a la decisión ya mergeada en el canon:

- **Canon actual ($1.000):** decisión "Acordada" del 2026-09-08 (reunión "Producto"), ya en `direccion/decisiones.md`.
- **Reunión "ARDID" (2026-09-09, 15:30):** Mariana Nadalin (Ardid/Akurtech) expone que "todas las cuentas bancarias (CBU) dadas de alta para personas jurídicas deben contar con un límite máximo de **10.000 pesos**", por pedido del directorio, con plazo obligatorio para el **1 de octubre de 2026** (00:03:59 de la transcripción).
- **Reunión "Join Soporte Clientes" (2026-09-09, 10:03):** sección "Decisiones" (estado "Acordada") registra: "se aprobó que las cuentas CVU de personas jurídicas que no utilicen el flujo de onboarding estándar nazcan con un límite operativo de **10.000 pesos** hasta que compliance valide su documentación de respaldo" — mismo criterio conceptual que la decisión de $1.000 del canon, pero con el monto multiplicado por 10. Nota: el párrafo de "Resumen" del mismo documento dice en cambio "1.000 pesos", inconsistente con su propia sección de Decisiones — no se pudo resolver la ambigüedad interna de esa minuta contra la transcripción (no se abrió).

Dos fuentes independientes (distintos asistentes, distintas reuniones, mismo día) coinciden en $10.000, lo que sugiere que el monto real vigente pasó a ser $10.000 y que la cifra de $1.000 documentada en el canon (2026-09-08) quedó desactualizada — pero no hay confirmación explícita de que sea un cambio deliberado vs. un error de transcripción que se arrastra. Compliance/Pablo Gomes (dueño de la iniciativa Onboarding Shared KYC/Worsis, `pm_destino: pablo`) debería confirmar el monto vigente antes de que el merge actualice `direccion/decisiones.md`.

> Fuente: Reunión "ARDID" (2026-09-09, 15:30, minuta+transcripción Gemini) y reunión "Join Soporte Clientes" (2026-09-09, 10:03, minuta Gemini).
