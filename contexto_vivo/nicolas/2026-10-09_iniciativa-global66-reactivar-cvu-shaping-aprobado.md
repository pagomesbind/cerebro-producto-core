---
id: 2026-10-09_iniciativa-global66-reactivar-cvu-shaping-aprobado
pm: nicolas
fecha_captura: 2026-10-09
fuente: "Sesión /idea_start con Nicolás Colón (2026-10-09)"
producto: wallet
tema: Proyecto nuevo PRD-279 — reactivar una CVU migrada genera una CVU nueva (Global 66 y orgs migradas), shaping aprobado
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: global66_reactivar_cvu
---

**PRD-279 (Nicolás Colón) — proyecto nuevo, shaping cerrado (2026-10-09).** En las organizaciones con CVUs migradas desde otro PSP (Global 66; antes Astropay), rehabilitar por API una CVU deshabilitada crea una CVU nueva y la original queda inoperable, porque el `clientId` de API Bank se arma con el `IdCuenta` de Wallet. Aprobado (BAU, S–M, 2 SP preliminares): corregir la rehabilitación derivando el identificador de la CVU ya guardada en Wallet, para todas las orgs migradas, + reproceso de los casos ya afectados; la reactivación manual queda como puente. IDEA en DISCOVERY vinculada a la historia WS-1861 (Gonzalo Rivera). Abierto: si se le cobra a Global 66 (a definir con Mauro Suppan; se cotiza igual) y validar con Fintexa la derivación del identificador. Próximo paso: análisis funcional-técnico.
