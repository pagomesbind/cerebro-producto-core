---
id: 2026-10-09_cumplimiento_conocimiento_cpf_consulta_general_estructura_respuesta
pm: pablo
fecha_captura: 2026-10-09
fuente: "/idea_start — API Reference CPF de Coelsa (PDF, 72 págs., documentacion.coelsa.com.ar/CPF) aportado por el PM, págs. 1-30 y 44-52 leídas; discovery PRD-278 \"CPF en onboarding\""
producto: transversal
tema: CPF de Coelsa — la consulta por CUIT/CBU/CVU es general y devuelve una lista de casos (no un score ni un booleano); estados, tipificaciones y plazos
tipo: conocimiento
destino_propuesto: wiki/3_recursos/cumplimiento_normativo/coelsa_cpf_central_prevencion_fraude.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Complementa el archivo ya existente sobre la CPF con lo que el documento oficial dice sobre **cómo responde la consulta**, que es lo relevante para usarla en el onboarding. Cambia la sección "Relevancia y siguiente paso sugerido": ya no es una pregunta abierta si Bind debe consumirla (la Com. "B" 13117 lo exige; ver item `2026-10-09_cumplimiento_conocimiento_com_b_13117_cpf_obligatoriedad`).

## La consulta es general

`GET /api/v1/operaciones/GetOperacionesByCuitCbuCvu/{valor}/{estado}` recibe un CBU, CVU o CUIT/CUIL y un estado (`Todos`, `CASO_VERIFICAR`, `CASO_VERIFICADO`, `OPERACION_GENUINA`, `VERIFICACION_AUTOMATICA`, `SOSPECHOSO_NO_VERIFICADO`) y devuelve los casos reportados por **cualquier** entidad del ecosistema contra esa cuenta o CUIT, no solo los que reportó la entidad que consulta. La documentación describe la CPF como una base "centralizada en COELSA y disponible para todos los participantes". El campo `Importe` solo lo ven la entidad reportante y la receptora de esa operación, "no el resto de las entidades que consultan" — está pensada para consulta cruzada.

## Estructura de la respuesta

No hay score ni indicador booleano. Devuelve `Listado_Operaciones` y un bloque `Respuesta` con `codigo` y `descripcion`. **Cuando no hay casos, la documentación no dice si devuelve una lista vacía o un código de respuesta:** el catálogo define 2003 "el dato no posee operaciones registradas", 2004 "la CVU no posee operaciones registradas" y 2005 "la CBU no posee operaciones registradas" (sin confirmar cuál se usa en la consulta; pendiente de una prueba en el ambiente de Coelsa). Cada operación trae: `Id_Operacion`, `Denominacion_Receptor`, `CBU_receptor`, `CVU_receptor`, `CUIT_receptor`, `CUIT_receptor_entidad`, `CUIT_iniciador`, `CUIT_Reportante`, `Codigo_Estado`, `Fecha_ocurrencia`, `ID_Moneda`, `Importe` (restringido), `Codigo_Canal`, `Metodologia`, `Sub_Metodologia`, `Observaciones`, `Codigo_Tipificacion_Cuentas`, `Usuario_Alta`, `Caso_Verificado`, `Id_caso_verificado`, `Fecha_registro`, `Usuario_modificacion`, `Fecha_modificacion`, `CUIT_Usuario`. Un segundo endpoint (`GetOperacionesByCuit`) consulta por CUIT de entidad receptora/reportante.

## Estados y plazos

| Estado | Significado |
|---|---|
| `CASO_VERIFICAR` | La operación sospechosa ingresó al repositorio; la entidad receptora todavía no la trató |
| `CASO_VERIFICADO` | La receptora confirmó que fue fraude; habilita registrar nuevos casos relacionados |
| `OPERACION_GENUINA` | La receptora comprobó que no fue fraude |
| `VERIFICACION_AUTOMATICA` | Intermedio: pasaron 5 días hábiles sin actualizar el estado |
| `SOSPECHOSO_NO_VERIFICADO` | Pasaron 5 días hábiles más (10 en total) sin actualizar; alerta al ecosistema |

`CASO_VERIFICADO` y `OPERACION_GENUINA` son estados finales. Solo una denuncia sin tratar (`CASO_VERIFICAR`) puede borrarla la entidad reportante.

## Tipificación de la cuenta y metodología

`Tipificacion_Ctas`: `CTA_MULA` (cuenta mula), `CTA_COMPL` (cómplice), `CTA_MUL_VICT` (mula víctima), `SIN_INDICIO`. Canales: `TRANSF_CBU_CVU`, `TRANSF_CVU_CBU`, `TRANSF_CBU_CBU`, `TRANSF_CVU_CVU`, `DEBIN`, `PAGOS_TRANSFERENCIA`, `OTROS`. Metodologías: `RDDO` robo de dispositivo, `ISCC`/`ISSC` ingeniería social con/sin compromiso de credenciales, `VNFT` vendedor fraudulento, `MLWR` malware, `RDID` robo de identidad, `OFIC` oficio, `SMSW` SIM swapping, `FRTI` fraude tecnológico (brute force / credential stuffing), `OTRS` otros. Submetodologías: `PHS`, `RDS`, `TEL`, `PRM`, `EML`, `TVW`, `PRS`, `SKT`, `OTR`.

## Límites de lo que informa

La base contiene solo operaciones sospechosas **reportadas** por las entidades. Detecta cuentas receptoras de fondos de fraude (mulas, cómplices) y CUIT con casos verificados; **no detecta** identidades falsas que todavía no movieron dinero ni fraudes que nadie reportó. Una consulta limpia no prueba que el titular sea confiable. Decidir qué estados y tipificaciones bloquean es una política de Bind (en definición con Compliance, PRD-278), no algo que Coelsa resuelva.

## Códigos de respuesta generales

200 operación exitosa, 400 error en la petición, 401 token inválido, 403 sin autorización, 422 error en el formulario; eliminación: 202 solo puede eliminar la entidad reportante, 203 inexistente o no está en `CASO_VERIFICAR`, 204 eliminada; autenticación 3001-3013; 1999 error genérico; 1001-1004 errores de formato de ID/CBU/CVU/CUIT. Formato: 1001-1052 (1019-1022 restringen a qué tipo de entidad pertenece un CUIT; 1045 consulta fuera del horario preestablecido para las descargas), 2001-2013 reglas de operación (2003/2004/2005 = sin operaciones registradas), 4000 error de consulta a la base y 4001 error al actualizar. Mensajería RabbitMQ (producto `CPFNEWS`): suscripción por única vez, una cola por entidad, mensajes JSON de alta y de modificación. (Págs. 31-43 y 63-72 del PDF no leídas.)

> Fuente: API Reference CPF de Coelsa (PDF aportado por el PM el 2026-10-09; páginas 2-3, 9-11, 17-20, 44-52).
