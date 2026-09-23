---
id: 2026-09-21_onboarding_menu_documentos_falta_vs_pendiente_y_propietario_directo
pm: pablo
fecha_captura: 2026-09-21
fuente: "sesión libre — navegación en vivo del backoffice STG de Onboarding Jurídico (app-onboarding-juridico-bo-stg-001), solicitud real 'FIAT CHRYSLER RIMACO ARGENTINA S.A. (Test)' en estado Pendiente Revisión Oficial De Negocio, para armar un manual de uso del Paso 2 (operador de la organización)"
producto: onboarding
tema: estructura real de la pantalla de solicitud PJ en backoffice — corrección de §9 (menú de Archivos) y confirmación de sección Propietario Directo
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md §9, puntos 4 y 10 (mergeados 2026-09-18) — punto 10 dice que el menú de cada documento en 'Archivos' es uniformemente 'Descargar, Visualizar, Marcar Pendiente'; punto 4 deja sin confirmar si existe una sección 'Propietarios' separada de Beneficiario Final"
confianza: alta
estado: ingestado
merge_commit:
---

Navegación en vivo (no simulada) del backoffice STG sobre una solicitud jurídica real pendiente de revisión Nivel 1, para relevar el detalle del Paso 2 del flujo (operador de la organización / rol "Oficial De Negocio"). Dos correcciones/ampliaciones puntuales sobre lo ya mergeado en §9 de `onboarding_personas_juridicas.md`:

**1. El menú de acciones de "Archivos" NO es uniforme — depende del estado del documento (corrige punto 10).**

Lo documentado dice "Descargar, Visualizar, Marcar Pendiente" para "cada documento". En la práctica el menú (ícono de tres puntos) cambia según si el documento ya fue cargado:

- Documento en estado **"Falta"** (naranja, priority_high): el menú tiene una única opción, **"Cargar"** — abre el selector de archivo para que el propio operador lo suba en el momento (alternativa a pedírselo al cliente vía "Contactar Cliente").
- Documento en estado **"Pendiente"** (ya cargado, con nombre de archivo y fecha de carga): el menú tiene 4 opciones — **Descargar, Visualizar, Marcar Verificado, Reemplazar**. No existe una opción "Marcar Pendiente" en ningún estado observado; el nombre correcto de la acción de aprobación de documento es **"Marcar Verificado"**, y la de corrección es **"Reemplazar"** (no un "marcar pendiente" que lo regrese a un estado anterior).

Esto importa para el manual operativo: un oficial que reemplaza un documento mal cargado usa "Reemplazar", no busca (inexistente) una opción para "rechazar" el documento puntual — el rechazo es solo a nivel de toda la solicitud.

**2. "Propietario Directo" SÍ es una sección separada de "Beneficiario Final" (resuelve la duda abierta en punto 4).**

La solicitud observada (FIAT CHRYSLER RIMACO ARGENTINA S.A.) tenía ambas secciones cargadas y visibles simultáneamente, cada una con su propia tabla y su propio modal "Ver Detalles":

- **Propietario Directo**: tabla con Razón Social / Nro de Identificador / "Ver Detalles Propietario". El modal muestra: Domicilio Legal, Lugar de Registración, Tipo de identificador fiscal, Propiedad y/o Votos de la Sociedad (%), Flotación — si cotiza en bolsa (%). En el caso observado el propietario directo era otra persona jurídica (Banco de Galicia S.A.), no una persona física.
- **Beneficiario Final**: tabla con Apellido y Nombre / Nro de Documento / "Ver Detalles Beneficiario". El modal (ya documentado en punto 4) muestra Razón Social, Tipo/Número de Documento, Domicilio Real, Nacionalidad, Fecha de Nacimiento, Profesión, Estado Civil, Votos en la Sociedad, PEP.

Es decir: el caso anterior (sin sección Propietarios) era porque esa solicitud puntual no tenía propietario directo cargado — no porque el concepto no exista separado de Beneficiario Final. Ambas secciones conviven en la misma pantalla, una debajo de la otra.

**Dato adicional no contradictorio, útil para el manual: el modal de "Cambiar estado" (Aprobar/Rechazar).**

Los botones "Aprobar" y "Rechazar" de la cabecera de la solicitud abren el mismo modal, "Cambiar estado", con el campo "Estado" pre-cargado según qué botón se tocó ("Aprobado" o "Rechazado") y un campo "Comentario" (contador 0/500) antes de "Actualizar". No se registró si el comentario es estrictamente obligatorio en ambos casos o solo se sugiere — no se llegó a intentar un "Actualizar" en vacío sobre la solicitud real para no alterarla.

Fuente: manual de uso construido en la misma sesión — ver [`2026-09-21_manual_onboarding_pj_operador.html`](../proyecto-la-virginia-ob-pj/artefactos/2026-09-21_manual_onboarding_pj_operador.html), que documenta el Paso 2 completo del flujo de 4 actores (carga → operador Nivel 1 → cumplimiento Nivel 2 → conformidad del representante legal) con capturas de pantalla reales.
