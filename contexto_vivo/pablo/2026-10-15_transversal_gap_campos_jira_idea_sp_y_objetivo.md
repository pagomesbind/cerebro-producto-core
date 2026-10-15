---
id: 2026-10-15_transversal_gap_campos_jira_idea_sp_y_objetivo
pm: pablo
fecha_captura: 2026-10-15
fuente: "Sesión de trabajo con Pablo Gomes (Claude Code) — lectura de PRD-202 en Jira con expand=names, 2026-10-14"
producto: transversal
tema: Ids de campos de la IDEA en Jira PRD documentados de forma contradictoria
tipo: gap
destino_propuesto: wiki/2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/datos/log_iniciativas_producto.md y .claude/skills/idea_finish/SKILL.md — nombran customfield_10107 como SP de la IDEA; .claude/skills/idea_jira/references/campos_jira.md usa customfield_10389"
confianza: alta
estado: en_cola
merge_commit:
---

**Fecha:** 2026-10-14 · **Severidad:** Media

**Contradicción.** La documentación del Cerebro no coincide sobre qué campo de la IDEA guarda el SP estimado:
- `log_iniciativas_producto.md` y la skill `idea_finish` usan `customfield_10107`.
- `idea_jira/references/campos_jira.md` usa `customfield_10389`.

**Lo que dice Jira hoy** (PRD-202 leída con `expand=names`):
- `customfield_10107` = **"Impacto"** (en PRD-202 vale 5).
- `customfield_10389` = **"SP estimado"** (54).
- `customfield_10101` = **"Objetivo del proyecto"**: rango `{start,end}`, que se usa como mes de salida.
- `customfield_10100` = "Inicio del proyecto".
- `customfield_10096` = "Hoja de ruta" (ej. "Ahora").

**Observaciones.**
- `customfield_10101` no se puede filtrar por JQL: `is not EMPTY` devuelve 0 resultados aunque haya valores cargados.
- Si `idea_finish` lee `10107`, la calibración SP estimado vs. real estaría comparando el campo "Impacto".

**Pendiente.** Confirmar y corregir los archivos y la skill que usan `10107`.
