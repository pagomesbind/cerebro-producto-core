---
id: 2026-08-25_coelsa-reactivacion-transferencias-pull-homologacion
pm: nicolas
fecha_captura: 2026-08-25
fuente: "Mail \"Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación\" — icm@coelsa.com.ar (hilo 2026-06-26 → 2026-08-24)"
producto: wallet
tema: Coelsa — pasos para reactivar Transferencias Pull en homologación + endpoint de registro de URL del PSP
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/transferencias_pull.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

El ticket Coelsa #456632 ("Reactivación de Transferencias Pull - Homologación") documenta el circuito completo para reactivar transferencias pull en el ambiente de homologación de Coelsa, tras un ajuste técnico de Coelsa en la configuración del entorno que invalidó el PSP anterior:

1. Coelsa exige crear un **nuevo PSP en HOMO** asociado a la cuenta recaudadora, porque el banco sponsor no permite crear un PSP nuevo con el mismo CUIT que uno ya existente — la solución acordada con Coelsa fue usar un **CUIT ficticio válido** para el nuevo PSP.
2. Además del PSP, hay que crear una **CVU asociada a ese CUIT** (en este caso, Coelsa pidió puntualmente el CUIT `23244825664` para la CVU).
3. Una vez creado el PSP, Coelsa requiere los datos: **CBU de la cuenta recaudadora, CVU asociada, y los datos del PSP** (código, CUIT, razón social, URL, estado) para continuar las pruebas.
4. Paso final (novedad del 2026-08-24, la que motiva esta captura): **hay que registrar la URL del PSP en Coelsa antes de poder arrancar las pruebas de estado**. El método indicado por Coelsa es `PUT /apiCVU/PSP/ModificacionPSP/{cuit}`.

Sin este último paso (registrar la URL vía ese PUT) Coelsa no permite continuar con las pruebas de estado del ambiente de homologación — ver tarea T-009 en `1_proyectos/tareas.md`.

> Fuente: hilo de mail "Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación", icm@coelsa.com.ar / Niurka Yamarte (COELSA), mensajes del 2026-06-26 al 2026-08-24; respuesta de Nicolás Colón del 2026-08-21 con los datos del PSP creado (CBU `3220001805007699600017`, CVU `0005071502070018043201`, PSP código `5071`, razón social "KEEP IT SIMPLE SRL").
