# Servicio de validación "Lista Negra BIND" (incluye la lista 15 de PLD)

> Estado: en producción (uso actual en Onboarding PF de BIND 24; no llamado todavía desde el flujo de alta de CVU — ver PRD-116).

> Fuente: documentación de middleware aportada por el PM (contrato SOAP del servicio Listas Negras) + conversación del PM con Juan M. Rodríguez Acquarone (sistemas de Banco Industrial, confirma que la lista 15 es la lista "CUIT RECHAZADOS PLD BIND" dentro de este mismo servicio) + captura de un flujo de onboarding legado del banco donde el paso ya corre en Etapa 1 tras Renaper.

## Qué es

Bind PSP ya tiene integrado (y en uso en producción, en el onboarding de personas físicas de **BIND 24**) un servicio SOAP de **Listas Negras** contra el middleware Poincenot/Depasse del Banco Industrial (Bantotal). El servicio permite validar si una persona (física o jurídica) pertenece a alguna lista negra gestionada por el banco — entre ellas, la **lista 15**, que PLD del grupo BIND exige agregar como control obligatorio en las altas de cuentas de la PSP (ver [`1_proyectos/proyecto-onboarding-estrategico/prd-116_validar_lista15_banco/`](../../../1_proyectos/proyecto-onboarding-estrategico/prd-116_validar_lista15_banco/proyecto.md)). Juan M. Rodríguez Acquarone (sistemas del banco) confirmó que el hit de la lista 15 aparece con `Descripcion: "CUIT RECHAZADOS PLD BIND"` — el servicio no expone el código "15" explícito en la respuesta, solo ese texto.

En la herramienta interna "Respuestas Servicios" (usada para depurar respuestas de servicios externos consultados en onboarding), esta consulta aparece como pestaña **"Lista Negra BIND"**, junto a PDF417, Renaper, Nosis, Morfología, Existe Persona, Validar/Cancelar Enrollamiento, etc.

## Contrato del servicio (`ConsultarListaNegra`)

**Request** (SOAP, `GrupoRequerimiento: Personas`, `IdRequerimiento: ConsultarListaNegra`) — datos relevantes:

| Campo | Descripción |
|---|---|
| `CodigoPais` | Código de país (BT) |
| `CodigoTipoDoc` | Tipo de documento (BT) |
| `NroDocumento` | Número de documento/CUIT (BT) |
| `PrimerNombre` / `SegundoNombre` | Nombre de la persona |
| `PrimerApellido` / `SegundoApellido` | Apellido de la persona |
| `NombreEmpresa` | Para personas jurídicas: razón social (se envía en los campos de nombre/apellido, no acá según el ejemplo de la docu) |

**Response — persona SÍ está en lista negra:**

```
<ListasInhabilitados>
  <ListaInhabilitados>
    <Descripcion>La persona se encuentra en la lista de Inhabilitados: ...</Descripcion>
    <Codigo>0</Codigo>
    <Bloqueante>N</Bloqueante>
  </ListaInhabilitados>
</ListasInhabilitados>
<ExisteEnLista>S</ExisteEnLista>
```

Puede traer más de una `ListaInhabilitados` si la persona figura en varias listas simultáneamente. Cada una trae su propio `Bloqueante` (S/N) — es decir, el servicio ya distingue qué hits son bloqueantes y cuáles no, aunque el ejemplo de la lista 15 (PLD BIND) trae `Bloqueante: N` en la doc de referencia; a confirmar con el banco si ese flag es siempre así para la lista 15 o varía.

**Response — persona NO está en lista negra:** `ExisteEnLista: N`, `ListasInhabilitados` vacío.

**Errores posibles:** `30001` (falta código de país), `30002` (falta tipo de doc), `30003` (falta nro. de documento), `30004` (falta primer nombre), `30005` (falta primer apellido).

## Dónde se ubica en el flujo (patrón legado a replicar)

En un flujo de onboarding viejo del banco (captura aportada por el PM), este paso corre en **Etapa 1, inmediatamente después de Renaper** — antes de los pasos más costosos del resto del flujo. Tiene lógica de corte temprano/bloqueante: si la persona figura en una lista inhabilitante, se frena ahí y se evita ejecutar el resto de las validaciones. Este es el patrón que PRD-116 busca replicar para las altas de CVU (hoy ese flujo no llama a este servicio) — ver decisión registrada en [`decisiones.md`](../../../1_proyectos/proyecto-onboarding-estrategico/prd-116_validar_lista15_banco/decisiones.md) de esa IDEA y la novedad en [`direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) (fila PRD-116): el servicio ya existe, no requiere integración nueva — reduce significativamente el esfuerzo estimado.

## Relación con otros documentos

- Modelo de 3 etapas de una solicitud de onboarding: [`arquitectura_solicitud_y_flujos.md`](arquitectura_solicitud_y_flujos.md) (mismo módulo).
- Este servicio (middleware Poincenot/Depasse, Banco Industrial/Bantotal) todavía no figura en `3_recursos/arquitectura_sistema/integraciones_externas.md` — pendiente de sumarlo la próxima vez que se toque esa tabla.

---
*Creado: 2026-09-03 — `/context_merge`: nuevo archivo, contrato del servicio "Lista Negra BIND" (incluye lista 15 de PLD), a partir de documentación de middleware aportada por el PM y conversación con sistemas de Banco Industrial. Insumo directo de PRD-116.*
