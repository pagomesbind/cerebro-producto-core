---
id: 2026-10-09_onboarding_iniciativa_prd147_armador_unico_entregado_por
pm: pablo
fecha_captura: 2026-10-09
fuente: "/idea_solution PRD-147 — sesión con el PM, 2026-10-09"
producto: onboarding
tema: PRD-147 — componente Worldsys como armador único, con dos entregadores y marca "entregado por"
tipo: iniciativa
proyecto: PRD-147
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

PRD-147 (legajo en Worldsys): el análisis técnico-funcional pasó a v3.1 (Propuesta, pendiente de aprobación del PM). Novedades: (1) arquitectura según la última reunión con Arquitectura y Seguridad: KYC solo orquesta y un **componente Worldsys con lógica y base de datos propia** (propuesta de Alejandro Sfrede) da de alta la persona, arma y carga el ZIP, monitorea y reintenta, de forma asincrónica y desacoplada del alta; lo entrega **Onboarding** (altas nuevas) o **la organización directamente** (stock, a construir en PRD-214), y Pablo Vargas plantea que solo Onboarding entregue archivos (discusión abierta); T-028 valida con negocio y compliance; (2) cada legajo lleva la marca `entregadoPor` con dos valores, `ONBOARDING` (si Onboarding entrega los archivos, siempre) o `CLIENTE`, también en el nombre del ZIP, para distinguir ante una auditoría quién armó el legajo; (3) Worldsys entregó (mail del 2026-09-09) el cuerpo de la importación "Clientes", que reemplaza a `POST /profile/customers` como vía de alta de persona (endpoint por confirmar); (4) el ambiente de pruebas prometido para el 2026-09-11 sigue sin entregarse.
