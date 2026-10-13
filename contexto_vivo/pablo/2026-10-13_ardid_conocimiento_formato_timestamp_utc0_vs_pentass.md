---
id: 2026-10-13_ardid_conocimiento_formato_timestamp_utc0_vs_pentass
pm: pablo
fecha_captura: 2026-10-13
fuente: "/sync_mails — hilo 'Re: Inconveniente con Ráfagas en ambiente Staging (Coto)' (threadId 19dd915df61a1f03), Lorena Macedo (Pentass) / Pablo Gomes, 2026-10-09"
producto: ardid
tema: Formato real del timestamp que Bind envía a Ardid (Pentass) en Transaction vs. Transfer — corrige una afirmación previa de Pablo de abril 2026 sobre conversión a UTC-3
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "mensaje de Pablo Gomes del 2026-04-29 en este mismo hilo ('hacemos la transformación a UTC-3 antes de enviarlas a Ardid') y la primera respuesta de Pablo en este mismo intercambio del 09/10 ('estamos enviando tanto Transfer como Transaction ya convertidos en UTC-3') — ambas quedan corregidas por la aclaración final del mismo día."
confianza: alta
estado: en_cola
merge_commit:
---

**Contexto:** Pentass (proveedor de Ardid — motor de reglas/ráfagas antifraude) está terminando el desarrollo de una feature de manejo de UTC y le pide a Bind confirmar en qué formato horario viene enviando las transferencias y pagos de todas las entidades, para dejarlo configurado de su lado sin que Bind tenga que tocar la integración al recibir el paquete.

**Primera respuesta de Pablo (09/10 09:50), luego corregida:** "Estamos enviando tanto Transfer como Transaction ya convertidos en UTC-3." Pentass responde con un formato de ejemplo (`2026-10-08 19:31:28.661` para transferencias, `2026-10-08T14:33:32.042Z` para pagos) que no cuadra con una conversión a UTC-3.

**Corrección final de Pablo (mismo día, 09/10 13:56) — el dato correcto:** Bind envía en **Producción en UTC0**, no UTC-3, y el formato **no es uniforme entre los dos tipos de mensaje**:
- **Transaction:** incluye el offset explícito `+00:00` al final del timestamp.
- **Transfer:** NO incluye el offset — el timestamp queda en UTC0 pero sin el sufijo.

Ejemplos reales de request enviados a Ardid el 09/10/2026 (adjuntados por Pablo en el mail):

```
Transaction:
{"TransactionId":"6435673","CommerceId":2375,"TxIdCommerce":null,
"TimeTxStart":"2026-10-09T13:41:19.871269+00:00","PayCode":null,
"Bin":null,"PanLast4":null,"PlasticName":null,"Dni":...}

Transfer:
{ EntityCode: "WA24", DeviceId: "", IpOrigen: "", TransferTransactionId:
"3c38fded-0739-44ff-984d-467d2517aa71", TransferType: 2, Scope: 2,
TrnDateCreate: 10/09/2026 13:49:18, TrnDateUpdate: 10/09/2026 13:49:18,
CuitCuilOrigin: "****0100", CbuCvuOrigin: "****6385", CoinType: 1,
Amount: 100000, CuitCuilReceiver: "****0100", CbuCvuReceiver: "****7986",
AccountTypeReceiver: 1, Processor: 1, TxProcessorId: "", Email: "****@HOTMAIL.COM" }
```

**Por qué importa:** este mismo hilo documenta desde abril 2026 el incidente original de Coto — las ráfagas (controles antifraude en tiempo real) no se activaban en staging porque el servidor SQL de Ardid toma su propia hora de referencia y había un desfase de zona horaria entre esa hora y la hora local de los registros que llegan desde Bind. En ese momento (abril) Pablo había afirmado que la conversión era a UTC-3; el intercambio de hoy deja documentado que en Producción es UTC0, con la inconsistencia adicional del offset explícito solo en Transaction. Pentass está dejando esto "hardcodeado" de su lado para no requerir cambios de integración — si el dato que le confirmamos no es exactamente el real, el desarrollo de Pentass puede quedar mal calibrado y reabrir el mismo tipo de problema de ráfagas que no se activan.

> Fuente: hilo "Re: Inconveniente con Ráfagas en ambiente Staging (Coto)" (threadId `19dd915df61a1f03`), Lorena Macedo (Pentass) / Pablo Gomes, mensajes del 09/10/2026 (reabre un hilo abierto originalmente el 2026-04-29).
