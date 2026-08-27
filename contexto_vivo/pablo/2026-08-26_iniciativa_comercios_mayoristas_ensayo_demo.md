---
id: 2026-08-26_iniciativa_comercios_mayoristas_ensayo_demo
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_meetings — reunión 'Previa demo mayoristas' (2026-08-26 09:31), minuta Gemini, docId 1Vc8ksoClbXqLAtRxlw-kBB6R5HS-kkwSd1BF_e8Me_g"
producto: ecosistema_wallet_adquirencia
tema: comercios_mayoristas (MayoristaPay) — ensayo interno de la demo a la cámara, pese al estado Diferido
tipo: iniciativa
proyecto: comercios_mayoristas
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

El proyecto `comercios_mayoristas` (MayoristaPay), cerrado en Gate 2 como 🟡 Diferido el 2026-08-25 (sin desarrollo hasta que cierre el acuerdo comercial con la cámara), tuvo actividad real el 2026-08-26: un ensayo interno ("Previa demo mayoristas") de la demo comprometida a la cámara de supermercados mayoristas (T-031), mostrando capacidades **ya existentes** de Bind (onboarding, portal, POS, wallet, backoffice, reglas Ardid) — consistente con la decisión de no invertir esfuerzo de desarrollo nuevo mientras el contrato no cierre.

Durante el ensayo se acotó el alcance de la demo en vivo (se excluyen archivos por lotes y carga de créditos por riesgo de inestabilidad) y se detectó un bug productivo real de Wallet/Ardid (bloqueo permanente de tarjetas por hash de vencimiento — ver item de conocimiento aparte en `contexto_vivo/`). Queda pendiente de confirmar si la demo real a la cámara ya se dio en la fecha prevista (26/08) o si el cambio de horario mencionado en los próximos pasos ("reprogramar reunión") la desplaza — el PM no tiene visibilidad directa de la coordinación comercial con la cámara. Este es el evento que condiciona la reactivación de todo el discovery, así que se sigue monitoreando de cerca.

Ver `1_proyectos/comercios_mayoristas/proyecto.md §8` y `1_proyectos/tareas.md` T-031.
