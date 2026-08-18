---
name: idea_golive
description: Genera un checklist de pre-lanzamiento cross-funcional (ingeniería, diseño, soporte, legal, cumplimiento, operaciones) con responsables, fechas y criterios de go/no-go. Se activa con /idea_golive.
when_to_use: Se activa cuando el usuario ejecuta /idea_golive, típicamente 1-2 semanas antes de un lanzamiento significativo o cross-funcional. No usar para un cambio chico de un solo equipo — ahí el checklist agrega ceremonia sin valor.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del lanzamiento]"
---

<!-- Adaptado de product-on-purpose/pm-skills (deliver-launch-checklist), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# 🚀 CHECKLIST DE LANZAMIENTO: /idea_golive

## Por qué existe esta skill

Un lanzamiento significativo toca a más equipos de los que un PM tiene en la cabeza al mismo tiempo: ingeniería, QA, soporte, legal/cumplimiento, operaciones, comunicación. Sin un checklist compartido, las sorpresas aparecen el día del lanzamiento. Esta skill coordina esas áreas, saca a la luz bloqueadores temprano, y define criterios claros de go/no-go — no para agregar burocracia, sino para no descubrir un problema regulatorio o de soporte a último momento.

## Cuándo NO usarla

- El cambio es chico y de un solo equipo, sin superficie cross-funcional real → un checklist de lanzamiento agrega ceremonia sin valor; trackealo directo en el sprint.
- El lanzamiento ya pasó y lo que hace falta es una retro o análisis de resultados, no un checklist previo.

## ⚖️ Reglas duras

1. **Todo item lleva responsable y fecha.** Sin dueño, el item no genera accountability real.
2. **Distinguí bloqueadores de nice-to-haves** explícitamente — mezclar ambos diluye la señal de qué realmente frena el lanzamiento.
3. **El plan de rollback no es opcional.** Todo lanzamiento tiene que poder revertirse si algo sale mal.
4. **Áreas regulatorias (BCRA/UIF/PCI DSS) se relevan siempre**, aunque el lanzamiento parezca puramente técnico — un cambio en un flujo de pagos o KYC casi nunca es "solo" ingeniería.
5. **El checklist es siempre autocontenido.** Es la previa a un documento que se comparte con stakeholders de varias áreas, algunos sin acceso a este sistema — sin links a la wiki, sin nombres de archivo o de skill, sin jerga de proceso interno. Todo lo que el checklist da por sabido (qué se lanza, por qué) se explica en el propio "Overview del lanzamiento", no se linkea al PRD o a `proyecto.md`.
6. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto del lanzamiento

1. Resolvé la ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2. Leé `proyecto.md` y el PRD asociado en `artefactos/` si existen — el checklist parte de lo que ya se especificó, no lo redefine. Si es miembro de un proyecto general, leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre.
2. Si el lanzamiento involucra un proveedor externo (Fintexa u otro), revisá `wiki/3_recursos/arquitectura_sistema/` por dependencias conocidas.
3. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-golive.md`** de una corrida anterior, leelo completo — esta corrida lo actualiza in place (ver Paso 8), no genera un documento nuevo en paralelo.

### Paso 1 — Definir el contexto del lanzamiento

Documentá qué se lanza, cuándo, y quiénes son los stakeholders clave. Establecé el tier del lanzamiento (release mayor, feature menor, experimento) — esto define el alcance del checklist.

### Paso 2 — Relevar requisitos por función

Para cada función (ingeniería, QA, soporte, legal/cumplimiento, operaciones, comunicación), identificá qué tiene que estar completo, verificado o listo antes del lanzamiento. Distinguí bloqueadores de nice-to-haves.

### Paso 3 — Asignar responsables y fechas

Todo item del checklist necesita un responsable y una fecha objetivo.

### Paso 4 — Identificar dependencias y bloqueadores

Marcá items que bloquean otro trabajo o que están bloqueados por factores externos. Sacalos a la luz temprano para poder desbloquearlos a tiempo.

### Paso 5 — Definir criterios de go/no-go

¿Qué condiciones tienen que cumplirse para lanzar? ¿Quién toma la decisión final?

### Paso 6 — Documentar el plan de rollback

¿Cómo se revierte si aparecen problemas críticos después del lanzamiento?

### Paso 7 — Programar la cadencia de check-ins

¿Cuándo se revisa el avance del checklist? (dailies, revisión a T-2 días, sync del día del lanzamiento).

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Un checklist completo llena: Overview del lanzamiento; Ingeniería; QA y testing; Diseño/UX; Comunicación; Soporte; Legal y cumplimiento; Operaciones e infraestructura; Analítica y monitoreo; Criterios de go/no-go; Plan de rollback; Cronograma de check-ins; Issues abiertos.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo.

## ✅ Checklist de calidad

- [ ] Todas las áreas funcionales relevantes están representadas
- [ ] Todo item tiene responsable y fecha objetivo
- [ ] Los bloqueadores están claramente diferenciados de los nice-to-haves
- [ ] Los criterios de go/no-go son específicos y medibles
- [ ] El plan de rollback está documentado
- [ ] La cadencia de check-ins está programada
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin jerga de proceso interno

## Paso 8 — Cierre estándar

1. **Persistir el entregable** en `artefactos/{{nombre_corto_proyecto}}-golive.md` — `{{nombre_corto_proyecto}}` es el nombre corto del proyecto: la carpeta misma si nació de `/idea_start` (sin prefijo `prd-XXX`), o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre del archivo — versión en el frontmatter + historial de revisiones al pie) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md` (sección de entrega y seguimiento PM). **Si el archivo ya existía**, esta corrida lo actualiza: reescribí limpio el estado vigente y sumá una entrada al historial de revisiones — no crear un archivo nuevo en paralelo.
2. **Riesgos/bloqueadores detectados** que no tienen dueño claro → `gaps.md` de la IDEA/proyecto; item `tipo: gap` en `contexto_vivo/` solo si son de contexto fijo, no del proyecto.
3. **Acciones del checklist con responsable de Producto** → `wiki/1_proyectos/tareas.md` (personal, directo, dedupe primero). Si alguna es de interés de todo el equipo, sumá además un item `tipo: tarea_equipo` en `contexto_vivo/`.
4. **Índices:** `wiki/1_proyectos/index.md`.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.