# Changelog de `2_areas/`

> Resumen corto de cada merge que tocó esta capa — qué cambió, sin el detalle (eso está en el archivo). **Solo lo escribe `/context_merge`**, una línea por archivo tocado, agrupadas por fecha de merge. Vive en el core y viaja con el espejo, así que se lee desde el install sin tocar el clon compartido. Rotación anual a `wiki/4_archivos/`.
>
> Distinto del manifiesto de cada merge (`manifiestos/YYYY-MM-DD.md` en el core): el manifiesto es el recibo operativo completo (qué items consumió, qué permisos pidió, qué contradicciones abrió) y lo lee `/context_pull`; esto es el resumen humano.

## 2026

### 2026-08-31 (pablo + nicolas)

- `direccion/decisiones.md` — creada 1 entrada: migración del detector de "caída de cliente" de `/sync_metrics` a metodología de ventana móvil 4×4 semanas (pablo).
- `direccion/oportunidades.md` — creada 1 fila (OP-016): alias de CVU visible en checkout de transferencia de Botón Simple 2.0 (pablo).
- `direccion/iniciativas.md` — creada 1 fila nueva (alias_cvu_checkout) y actualizadas 2 filas (PRD-202: 2 novedades; convenios_configuracion: 2 novedades) (pablo).
- `gaps_y_preguntas.md` — creado 1 gap nuevo (guia_cvu.md sin tope anual de modificaciones de alias, señalizado para `/sync_web`); actualizados 4 gaps existentes (dim_collectors, mapeo confirmado/reconfirmado; La Virginia, sexta semana; Pago Fácil sin ficha, ahora con evidencia de producción); cerrado y rotado a `4_archivos/gaps_resueltos.md` el gap de Terra Blockchain/Sucredito (baja por Compliance) (pablo + nicolas).
- `4_archivos/gaps_resueltos.md` e `index.md` — creados (primera rotación de un gap resuelto en el repo compartido).
- `overview_empresa/overview_empresa_general.md` — actualizado: nueva sección sobre la venta del negocio de banca minorista de Grupo BIND a Banco Patagonia (permiso explícito del usuario, régimen D) (pablo).
- `procesos/comunicacion_de_lanzamientos.md` — actualizado: nueva sección sobre la propuesta (sin decisión formal) de calendario de ventanas de despliegue anticipado (permiso explícito, régimen D) (pablo).
- `clientes/patrones_transversales.md` — actualizado: nueva sección 5 (notas de identidad de cliente) — Pago Fácil/Western Union/SEPSA son el mismo grupo comercial (permiso explícito, régimen D) (pablo).

### 2026-08-27 (pablo + nicolas)

- `direccion/decisiones.md` — creadas 2 entradas: prioridades de Producto de Cobro/Adquirencia para septiembre 2026 (fusión de 2 items del mismo hecho, Pablo Gomes + Nicolás Colón), y alcance inicial de pagos de servicios BPG (solo botón de pago, sin saldo de wallet).
- `direccion/oportunidades.md` — creadas 6 filas (OP-010 a OP-015): funcionalidades POS/Botón pedidas por Andesmar, rediseño de convenios entidad→comercio, pago de servicios con saldo de wallet de terceros, ecosistema financiero para cámara de supermercados mayoristas, fix de resiliencia de alias CVU (apibank/Coelsa), integración con Cobros con Transferencia (CCT) de Coelsa.
- `direccion/iniciativas.md` — actualizada 1 fila (PRD-147, novedad ZIP consolidado Worldsys) y creadas 6 filas nuevas (PRD-66, PRD-216, comercios_mayoristas con 2 novedades, asignacion_alias_cvu con 2 novedades, convenios_configuracion, PRD-223).
- `riesgos.md` — creados 2 riesgos: saturación de BD de impuestos por CUIT compartido (agente_cobros_y_pagos/siscri), y Proyecto Servicios (continuidad de equipo + bloqueo de pruebas con tarjetas prepagas).
- `gaps_y_preguntas.md` — creados 5 gaps: doc vs. real de `GET /CuentaCorriente` (datosOperacion), Red Link 404 sin dueño de producto identificado, contradicción de prioridad de desarrollo Onboarding (PF/PJ/menores), Epic AD-8 no funciona como documenta el canon, contrato real de API de Convenios contradice documentación previa.
- `clientes/casos_de_uso_clientes.md` — actualizadas 4 fichas: CREDICUOTAS (pedido de 2do factor), GRUPO SLOTS - Jugadon (alerta por cambio de categorización de webhook CBU Collect), COTO CICSA (fix de impuestos QR, semáforo amarillo), ARCOS DORADOS (fix de orden de productos al leer QR, con permiso explícito del usuario).
- `procesos/comunicacion_de_lanzamientos.md` — creado (con permiso explícito del usuario): acuerdo de canal estándar de mail interno para anunciar lanzamientos de producto.
- `procesos/index.md` — actualizado, sumada fila del archivo nuevo.

### 2026-08-21 (pablo)

- `direccion/decisiones.md` — creada 1 entrada con contradicción sin resolver (orquestador de configuración de entidades vía API: ¿decisión de roadmap vigente o no? — dos versiones del mismo PM, escaladas).
- `gaps_y_preguntas.md` — creado 1 gap (contradicción del orquestador de API, ver arriba).
- `direccion/oportunidades.md` — creada 1 fila (OP-009, onboarding propio como producto de marca blanca).
- `direccion/iniciativas.md` — creada 1 fila (PRD-214, primer discovery formal — dimensionamiento de stock actualizado y bifurcación de arquitectura SharedKYC vs. integración directa).
- `riesgos.md` — creado 1 riesgo (desalineación entre comisión facturada a la entidad y comisión real cobrada por el procesador).
- `clientes/casos_de_uso_clientes.md` — actualizada ficha de OCTAGON (cronología: demo de onboarding propio a Octagon y Compliance de Banco Industrial, con permiso explícito del usuario).

### 2026-08-19 (pablo)

- `gaps_y_preguntas.md` — creado 3 gaps (MCC4829 VISA, backfill AD Portal 2.0, dim_collectors sin orden de columnas), actualizados 2 (La Virginia, Terra Blockchain — tercera semana consecutiva de cada patrón).
- `direccion/iniciativas.md` — creado, primeras 2 filas (PRD-147, PRD-202); PRD-147 actualizada con la novedad del 2026-08-19 (problem statement v2.0, sin decisiones/gaps nuevos).
- `direccion/decisiones.md` — creada 1 decisión (liderazgo de gestión de proyecto de Onboarding pasa a Soluciones Andinas — item duplicado de 2 fuentes, fusionado en una sola entrada).
- `tareas.md` — creada 1 tarea (T-107, renovación de contrato de Figma).
- `overview_empresa/overview_equipo.md` — actualizado (nueva Gerente de Operaciones Mariana Nadalin + cronograma presencial Fintexa).
- `CLAUDE.md` (raíz del repo, no `2_areas/` pero mismo régimen de permiso) — actualizado: se suma `riesgos.md` como archivo lazy de proyecto/subproyecto en `1_proyectos/`, con el mismo patrón que `gaps.md`/`decisiones.md` (decisión ya aprobada por el usuario en sesión previa 2026-08-18).
