# Cartera de Iniciativas — vista cross-PM

> Compartido entre los tres PM/PO — **solo lo escribe `/context_merge`**. Una fila por iniciativa **en curso** de cualquiera de los tres, con lo que Jira no tiene: por qué se frenó, qué se decidió, qué se aprendió, qué bloquea. No espeja estado ni Story Points de Jira — para eso, Jira. Cada PM aporta la novedad de su propia iniciativa (o de la de otro, si la detecta) como item `tipo: iniciativa` en `contexto_vivo/`, con `proyecto` (PRD/slug) y opcionalmente `pm_destino` si la novedad es para otro PM. El merge hace upsert de la fila por esa clave y antepone la novedad fechada.
>
> Distinto de:
> - `wiki/1_proyectos/index.md` §2 de cada PM — el registro personal y completo de sus propias IDEAs (ese no cambia, lo sigue manteniendo cada uno).
> - `wiki/3_recursos/datos/log_iniciativas_producto.md` — histórico de calibración (SP estimado vs. real) de IDEAs **cerradas**, no de las que siguen en curso.
>
> **Ruteo cross-PM:** las novedades con `pm_destino` se listan aparte en el manifiesto de cada merge, y `/context_pull` se las reporta al PM destinatario como "tenés N novedades dirigidas a vos". El merge no escribe en la carpeta de proyecto del otro PM — el PM destinatario decide si la incorpora a su propio `proyecto.md`.

| Proyecto | PM dueño | Problema que ataca | Foco estratégico | Última novedad |
|---|---|---|---|---|
