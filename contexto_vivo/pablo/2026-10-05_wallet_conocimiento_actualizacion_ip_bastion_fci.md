---
id: 2026-10-05_wallet_conocimiento_actualizacion_ip_bastion_fci
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_mails — mails \"Confirmación de baja de servidor anterior SOPORTE PRD - ex Bastion PRD 10.45.2.10\" (threadId `1a0fd4180e3c6868`) y \"...SOPORTE STG - ex Bastion STG\" (threadId `1a0fd280ec8fabdb`), Emiliano Gonzalez Cortiñas (Fintexa Infraestructura), 2026-10-02"
producto: wallet
tema: Cambio de dirección del bastión PRD/STG usado como workaround del procedimiento de rescate masivo de FCI (API Broker Poincenot)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md — el procedimiento operativo de rescate masivo de FCI vía API Broker Poincenot (ingerido 2026-10-02, item `wallet_conocimiento_procedimiento_rescate_masivo_fci_poincenot`) documenta un workaround vía Postman/bastión; la IP de ese bastión cambia a partir del 09/10/2026, ver detalle abajo"
confianza: alta
estado: en_cola
merge_commit:
---

Infraestructura (Fintexa, Emiliano Gonzalez Cortiñas) confirmó la baja definitiva de los bastiones viejos de soporte, efectiva el **09/10/2026 a las 18hs**:

- **Bastion PRD:** `10.45.2.10` → nueva dirección operativa `10.45.2.20`.
- **Bastion STG:** `10.55.2.10` → nueva dirección operativa `10.210.255.6`.

A partir de la baja, los servidores anteriores dejan de estar disponibles (sin acceso a la información que tuvieran almacenada). El acceso a los nuevos servidores ya está operativo desde antes y debe usarse para todas las tareas habituales (mismo usuario/contraseña).

**Por qué importa:** el procedimiento de rescate masivo de FCI vía API Broker Poincenot (ya ingerido al canon el 2026-10-02) documenta un workaround operativo vía Postman/bastión para sortear la limitación de Swagger con JSONs extensos — ese procedimiento debería actualizarse con la nueva dirección del bastión antes del 09/10, para no quedar con una referencia a una IP dada de baja.

> Fuentes: mails "Confirmación de baja de servidor anterior SOPORTE PRD/STG", Emiliano Gonzalez Cortiñas (Fintexa), 2026-10-02.
