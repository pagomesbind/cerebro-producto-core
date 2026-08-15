# Crear Collector en Agente de Cobros y Pagos

> Estado: en producción. Contenido completo transcrito desde `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/`. Reubicado desde `detalle_productos/cobros/configuracion_y_operacion.md §1-2` en la reestructuración PARA en cascada (2026-08-12).

## 1. Crear collector — PSP = 184

# Precondiciones
Ninguna.
# Configuraciones
- [ ] Reservar un código del proxy en el excel de control de Fintexa (pedir link vigente al equipo de Integraciones — el histórico apuntaba a un SharePoint de Fintexa).
- [ ] Crear nueva entidad en cobro. Ver instructivo interno de Notion (pedir link vigente si no se tiene acceso).
- [ ] Crear nuevo collector en `MiddlewareAggregatorDB > Collectors.dbo` usando el endpoint `POST /api/v1/Organizacion` del swagger de MiddlewareAggregator (STG/PRD — pedir URL vigente a Infraestructura) con el body:
	```json
{
  "collectAccountId": "20-1-735135-8-5",//account_id de la recaudadora, en STG usamos siempre 20-1-735135-8-5
  "codigo": 892,//código reservado en el excel
  "bankId": 322,//siempre 322
  "name": "Nombre cliente",//nombre del collector
  "cuit": "CUIT cliente", //cuit del collector
  "psp": "532", //en STG=532 en PRD=184
  "cbu": "3220001805007351350083",//cbu de la recaudadora
  "urlWebHook": "https://webhook.site/6995788f-6fbf-42e0-ae75-6acb53b6a733", //url en la que el collector quiere recibir los webhooks.
  "idCaja": "A114$$C15904$$B00003478600",//de la caja creada antes = CodEntidad$$CodComercio$$CodCaja
  "createdAt": "2025-10-08T14:16:02.872Z", //dia de hoy
  "cancellationDate": null //siempre null
  }
	```
- [ ] Pedir consumer para Agente de Cobros y Pagos indicando: AMBIENTE (STG/PRD), Producto: CVUCollect, x-entidad: IdCollector, email.
- [ ] Pedir consumer para Cobro indicando: AMBIENTE (STG/PRD), Producto: Cobro, x-entidad: Código de entidad, e-mail.
- [ ] Crear el registro para setear una especificación que conecte la entidad al collector en `SharedComercioDB > Especificaciones.dbo` usando el endpoint `POST /api/v1/entidades/{id}/especificaciones` con el header `x-entidad = CodigoEntidad` y con el body:
	```json
{
"descripcionGrupo": "CVU_TRANSFERENCIA",
"especificaciones": [
   {
    "keyEspecificacionTipo": "COLLECTOR_ID",
    "valorEspecificacionTipo": "",
    "valorDefault": "XX", // ID de collector creado
    "valor": "XX" // ID de collector creado
   }
]
}
	```
- [ ] Configurar convenios de canal CVUCollect y forma de pago transfer.
# Validaciones
- [ ] En staging: Ejecutar regresión automática (ver instructivo interno de Notion).

## 2. Crear collector — PSP != 184

Mismos pasos que §1, con dos diferencias:
- En el body de creación del collector, el campo `"psp"` lleva el id del PSP correspondiente en el ambiente (no `532`/`184`).
- Paso adicional: **solicitar mediante Jira a FINTEXA** que configuren lo necesario para que este `idCollector` consuma API Bank por el producto CVUCollect con otras credenciales especiales. Indicar `idCollector`, ambiente y asunto por donde se enviaron las credenciales por mail. Pasar las credenciales de API Bank por email a `security@fintexa.tech`.

## Ver también

- [webhook_transferencia_entrante_cbu.md](webhook_transferencia_entrante_cbu.md) — cómo se notifica una transferencia entrante al collector creado acá.
- [transferencia_saliente_mecanica.md](transferencia_saliente_mecanica.md) — cómo funciona una transferencia saliente del collector.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/cobros/configuracion_y_operacion.md §1-2` (reestructuración PARA en cascada); URLs internas con IP hardcodeada y link de SharePoint reemplazados por referencia a quién los provee, dado que quedaron obsoletos o son de acceso restringido a personal interno.*
*Última actualización anterior: 2026-07-03 — Creación del módulo `detalle_productos/cobros/` a partir de documentos de `wiki/3_recursos/conocimiento_interno/`.*
