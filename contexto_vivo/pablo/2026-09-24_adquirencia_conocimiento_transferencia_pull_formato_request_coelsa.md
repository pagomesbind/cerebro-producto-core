---
id: 2026-09-24_adquirencia_conocimiento_transferencia_pull_formato_request_coelsa
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_mails — mail 'Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación', Nicolás Colón → icm@coelsa.com.ar, 2026-09-23 18:42 (threadId 19f055a718dd930f, mensaje 1a0cf9440b824968)"
producto: adquirencia
tema: primer diagnóstico técnico real del ticket Coelsa #456632 (Transferencia Pull en Homologación) — discrepancia de formato entre el request real que envía Bind y el documentado por Coelsa
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/transferencias_pull_debin_coelsa.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Contexto

El ticket Coelsa #456632 ("Reactivación de Transferencias Pull - Homologación") lleva abierto desde 2026-06-26 sin resolución — sucesivas idas y vueltas puramente administrativas (crear un PSP nuevo en Homologación con CUIT ficticio porque no se podía reutilizar el mismo CUIT, registrar la URL del PSP con `PUT /apiCVU/PSP/ModificacionPSP/{cuit}`, validar telnet a la IP configurada). El mail del 2026-09-23 (Nicolás Colón) es el primer mensaje del hilo que aporta un diagnóstico técnico real en vez de solo demoras administrativas.

## Hallazgo

Coelsa reportaba que el telnet a la IP configurada del PSP no respondía, pero Bind confirmó que **las peticiones sí llegan** — el problema real es que Bind **no las está interpretando** porque el `request` real que envía Coelsa difiere del documentado. Comparación directa (mismo endpoint de aviso de DEBIN pendiente/CVU):

**Request real recibido** (ejemplo capturado el 2026-09-22, operación `ORD6LEN8QOL61LG9M1Y30V`):
```json
{
  "operacion": {
    "comprador": {
      "cuenta": {"banco": "322", "sucursal": "0001", "alias": "DISCO.BUDA.TOMATE", "cbu": "3220001805007699600017", "esTitular": 0, "moneda": "032", "tipo": "20"},
      "codigo": "",
      "titular": "KEEP IT SIMPLE SRL",
      "cuit": "30714979732",
      "cuenta_virtual": {"id_psp": "5071", "cuit_psp": "30714979732", "cvu": "0005071502070018043201", "cuit_cvu": "23244825664", "titular_cvu": "Nicolas Colon"}
    },
    "vendedor": { "...": "mismo shape que comprador, sin cuenta_virtual" },
    "detalle": {"fecha": "...", "fechaExpiracion": "...", "concepto": "VAR", "idUsuario": 1804958, "idComprobante": 1545489, "moneda": "032", "importe": 1.0, "mismoTitular": 0}
  },
  "debin": {
    "id": "ORD6LEN8QOL61LG9M1Y30V",
    "estado": {"codigo": "INICIADO", "descripcion": "PERSISTIDO"},
    "estadoComprador": {"codigo": "01", "descripcion": "NO ADHERIDO"}
  },
  "preautorizado": true,
  "evaluacion": {"puntaje": 65, "reglas": "2a,9,1c"}
}
```

**Request esperado según la documentación de Coelsa** (ejemplo de referencia, operación `5R7ZG0QND73YP5E2EXYPOJ`):
```json
{
  "operacion": {
    "objeto": {"tipo": "TRXPL"},
    "comprador": { "...": "mismo shape, sin id de operación propio" },
    "vendedor": { "...": "..." },
    "detalle": { "...": "..." }
  },
  "debin": {
    "id": "5R7ZG0QND73YP5E2EXYPOJ",
    "estado": {"codigo": "INICIADO", "descripcion": "PERSISTIDO"},
    "estadoComprador": {"codigo": "00", "descripcion": "ADHERIDO"}
  },
  "preautorizado": true,
  "evaluacion": {"puntaje": 0, "reglas": ""},
  "EntityID": 0
}
```

**Diferencias concretas identificadas por Bind:**
- El request real **no trae** el nodo `operacion.objeto.tipo: "TRXPL"` que sí aparece en el ejemplo documentado — posible campo de discriminación de tipo de operación que Bind no está mapeando/esperando.
- El request real **sí trae** `EntityID` ausente (el documentado lo tiene, en `0`) — a confirmar si es opcional u obligatorio.
- Ambos formatos comparten los nodos `preautorizado` y `evaluacion` (puntaje + reglas de scoring), pero con valores de ejemplo muy distintos (65/`"2a,9,1c"` vs. 0/vacío) — sin aclarar si `evaluacion` es siempre parte del contrato o solo aparece bajo ciertas condiciones.

Bind (Nicolás Colón) pidió a Coelsa (Niurka Yamarte) que orienten si el problema es de su lado o si la documentación pública está desactualizada. **Sin respuesta de Coelsa todavía al cierre de esta captura** — el ticket sigue abierto.

## Por qué importa

Es el primer indicio concreto, en casi 3 meses de ticket abierto, de **por qué** las Transferencias Pull nunca terminaron de funcionar en Homologación: no es un problema de red/conectividad (como parecía por los mensajes previos sobre telnet/URL), sino una posible discrepancia de contrato entre lo que Coelsa envía en producción real y lo que su propia documentación pública describe. Si se confirma, afecta a cualquier integración de Transferencia Pull/DEBIN que dependa de esa documentación.
