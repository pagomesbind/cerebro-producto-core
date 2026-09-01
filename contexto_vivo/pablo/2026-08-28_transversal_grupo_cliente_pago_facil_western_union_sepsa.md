---
id: 2026-08-28_transversal_grupo_cliente_pago_facil_western_union_sepsa
pm: pablo
fecha_captura: 2026-08-28
fuente: "/idea_start — discovery de alias_cvu_checkout/, aclaración del PM en sesión de trabajo"
producto: transversal
tema: Pago Fácil, Western Union y SEPSA son el mismo grupo cliente para Bind
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

## Pago Fácil, Western Union y SEPSA son, comercialmente, el mismo grupo cliente

Ninguno de los tres tiene ficha propia en `log_clientes.md` (no están en el log maestro de 200 clientes sincronizado de Notion — se gestionan como "entes" de producto, no como clientes CRM estándar). Durante el discovery de `alias_cvu_checkout/` (2026-08-28) apareció una posible confusión: dos pedidos casi idénticos (mostrar/usar un alias en vez del CVU numérico crudo) llegaron por canales separados — uno de "Pago Fácil" (comercial Adriana, sobre el checkout de Servicios/Botón Simple 2.0) y otro de "Western Union/SEPSA" (Guillermo Paolucci, sobre la pasarela Bind-SEPSA, `tareas.md` T-038). El PM aclaró explícitamente: **es un mismo grupo de varias empresas, no dos clientes independientes** — Bind los trata como una sola relación comercial repartida en distintos productos/interlocutores.

**Por qué importa:** al evaluar demanda/generalización de un pedido de este grupo, dos menciones separadas (por producto o por interlocutor comercial) no son dos señales independientes — son la misma relación pidiendo lo mismo dos veces. Vale la pena, además, coordinar entre los equipos que atienden cada frente (Servicios/BS2.0 y la pasarela SEPSA) antes de responderle por separado al mismo grupo.

> Fuente: aclaración del PM en la sesión de `/idea_start` de `alias_cvu_checkout/`, 2026-08-28. Ver `1_proyectos/alias_cvu_checkout/proyecto.md §7` y `1_proyectos/tareas.md` T-038.
