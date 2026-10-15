---
id: 2026-10-13_wallet_conocimiento_fci_rescate_total_withdraw_parametro
pm: pablo
fecha_captura: 2026-10-13
fuente: "/sync_mails — hilos 'Re: Astropay FCI - Rescate masivo de cuentas' (threadId 1a1361e1379d5b03) y 'Re: Comitentes Astropay con saldo' (threadId 1a0e865d6b79a31d), equipo Bind/Fintexa/Keep IT Simple, 2026-10-13"
producto: wallet
tema: Rescate masivo de FCI vía API Broker Poincenot — parámetro "totalWithdraw":true permite rescatar el saldo completo sin calcular montos exactos
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no — complementa el procedimiento de rescate masivo de FCI ya documentado (reporte de posición de Poincenot + JSON armado a mano + ejecución vía Postman por tamaño del body, capturado 2026-10-02)"
confianza: alta
estado: en_cola
merge_commit:
---

Durante la coordinación de un nuevo rescate masivo de FCI para cuentas de Astropay (continuación del procedimiento ya documentado), surge un detalle técnico nuevo sobre el request a Poincenot:

- Gastón Degiovanni (Bind) aclara que **para hacer un rescate total de una cuenta no hace falta conocer ni calcular el monto exacto** ("Monto Valuado en Moneda del Fondo" del reporte de posición de Poincenot). Alcanza con enviar el campo `"totalWithdraw": true` en el body de la solicitud, por ejemplo:

  ```json
  {
    "fund": "2",
    "account": "4652",
    "value": {
      "totalWithdraw": true
    }
  }
  ```

- Esto evita el paso de sacar el reporte de posición del día exacto y calcular el VCP para obtener el monto valuado — simplifica el procedimiento documentado en 2026-10-02 para los casos donde el objetivo es vaciar la cuenta por completo (no un rescate parcial).
- Gastón pide explícitamente que, cuando se envíen las cuentas a rescatar, se use este mecanismo de rescate total ("manda los rescates totales porfa, así no quedan decimales") para evitar remanentes por redondeo.
- El hilo paralelo ("Astropay FCI - Rescate masivo de cuentas") muestra que el procedimiento de coordinación sigue el mismo patrón ya documentado: acordar fecha con el negocio → pedir reporte de posición a Poincenot → armar el JSON → ejecutar (Swagger o Postman por el tamaño del body de ~74 cuentas). Sin novedad adicional sobre ese flujo en esta corrida, más allá del detalle de `totalWithdraw`.

> Fuente: hilo "Re: Comitentes Astropay con saldo" (threadId `1a0e865d6b79a31d`), Gastón Degiovanni (Bind), 13/10/2026 18:09-18:21; hilo "Re: Astropay FCI - Rescate masivo de cuentas" (threadId `1a1361e1379d5b03`), Franco Giménez (Bind), 13/10/2026 17:15.
