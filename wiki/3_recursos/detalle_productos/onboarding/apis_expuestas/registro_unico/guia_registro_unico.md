# Guía — Onboarding Registro Único

> Extraído el: 2026-07-01
> Fuente: https://psp.bind.com.ar/developers/apis/guia-onboarding-registro-unico
> Producto: Onboarding

## ¿Cómo validar un onboarding propio?

Esta solución permite validar en Bind PSP a un usuario analizándolo según los criterios indicados para el caso de uso y así aprobar el mismo para resultar en el alta de una cuenta, CVU, cuenta comitente, etc.

Esta funcionalidad está pensada en resolver un último paso en un onboarding construido por la Entidad, pero que le hagan falta validaciones necesarias para ciertos casos.

Entonces, al finalizar el onboarding en la aplicación y ser la persona aprobada por la entidad, recién invoca esta funcionalidad para determinar si finalmente la persona es aprobada por Bind PSP y, si lo es, al mismo tiempo se resuelven las altas correspondientes.

Se puede configurar para que el onboarding finalice incluyendo en el proceso mismo:

- Con alta de cuenta y CVU
- Con alta de cuenta, CVU y cuenta comitente
- Con alta de cuenta, CVU y cuenta cripto

Esta configuración será según el caso de uso y funcionalidades que luego la entidad utilizará dentro del ecosistema de Bind PSP.

## Flujo — Onboarding como registro único aprobado

```
1. La Entidad completa su propio onboarding (fuera de Bind PSP)
2. La persona es aprobada por la Entidad → recién entonces invoca Bind PSP

3. POST /orquestador/api/v1/onboarding  (o /onboarding-cuenta-comitente)
   → Body: frente + dorso (DNI Base64) + selfie + email + telefono
           + maritalState + occupation
           + DDJJ: isOcde/isFatca/isPEP/isUIF/isTyc + timestamps respectivos
   
4. Bind PSP ejecuta en secuencia (internamente):
   a. Lectura del PDF417 del DNI
      [Si falla: HTTP 422 PDF417_NO_ENCONTRADO → reenviar con documento/tramite/genero manual]
   b. Renaper Datos → verifica existencia, vigencia, fallecido, menor de edad
   c. Renaper Rostro → comparación facial selfie vs DNI
   d. Nosis → antecedentes comerciales
   e. Worldsys → listas PEP y terrorismo
   f. UIF → sujeto obligado
   g. Matriz de riesgo → puntajeRiesgo

5a. Si APROBADO (HTTP 201):
    → Crea cuenta Wallet + CVU (+ cuenta comitente si /onboarding-cuenta-comitente)
    → EVENT webhook a URL configurada en backoffice (aviso onboarding aprobado)

5b. Si RECHAZADO (HTTP 422):
    → Error específico: ya existe solicitud aprobada / Renaper no reconoce /
      fallecido / DNI no vigente / menor de edad

6. GET /solicitudes/{id} → consultar estado + archivos legajo + historial + JSONs auditores
```

**Configuraciones posibles (parametriza Bind PSP):**
- Alta de cuenta + CVU
- Alta de cuenta + CVU + cuenta comitente (`/onboarding-cuenta-comitente`)
- Alta de cuenta + CVU + cuenta cripto

## API Reference

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | [Registro único CVU](endpoint_post_crear_solicitud.md) | Crea solicitud con alta de cuenta y CVU |
| POST | [Registro único CVU+comitente](endpoint_post_crear_solicitud_cvu_comitente.md) | Crea solicitud con alta de cuenta, CVU y cuenta comitente |
| GET | [Consultar solicitud por ID](endpoint_get_consultar_solicitud_id.md) | Consulta una solicitud por su ID |
| GET | [Consultar solicitud por ID externo](endpoint_get_consultar_solicitud_id_externo.md) | Consulta una solicitud por ID externo |
| EVENT | [Aviso de onboarding aprobado](endpoint_event_aviso_onboarding_aprobado.md) | Webhook cuando el onboarding es aprobado |
