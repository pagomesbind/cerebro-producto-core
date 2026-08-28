# Configuración de Entidades — Alta, Portal Comercio, CUITs Duplicados

> Estado: en producción. Fuente: `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/` (ingesta Notion). Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` en la reestructuración PARA en cascada (2026-08-12).

## 1. Crear entidad en cobro — PSP = 184

**Objetivo:** dejar operativa una nueva entidad en el centralizador de cobro que luego pueda crear comercios, si el PSP es 184.

**Precondición:** crear la Organización en wallet primero, solo si la entidad estará conectada con wallet o usará QR con acreditación en línea en wallet.

**1. Datos de la entidad** (desde Nueva entidad del Admin Centralizador): Nombre, CUIT, Código ("AXXX", último+1), Identificador PSP (STG=532, PRD=184), Dominio adquiriente (STG=com.TESTbind, PRD=com.bind), ID/Nombre/CUIT del Administrador interoperable Coelsa (1 / Coelsa / 30692264785).

**2. Especificaciones:** Id de cuenta (STG=1, PRD=61, sacado del swagger de consulta cuentas Coelsa por PSP), Banco (322), Creación Access Management (TRUE si usa portal comercio), Roles por defecto ("Administrador" por defecto), Genera Notificaciones Internas (TRUE salvo caso raro tipo PMC), Control de fraude mediante Ardid (TRUE por defecto), Admite Comercios con CUIT Duplicados (según caso de uso), Es entidad wallet + Id Organización wallet (⚠️ obligatorio si usará QR con acreditación en wallet en línea).

**3. Convenios:** no cargar nada y siguiente.

**4. Reglas de pago:** STG — Botón simple "Decidir - Boton Simple", POS "Grupo BRONCE". PRD — Botón simple "Decidir - Prepagas"/"Decidir Crédito"/"Decidir Débito", POS "GP Procesamiento".

**5. Impuestos:** agente de retención = Bind PSP si PSP=184.

**Pasos adicionales (solo PROD):** crear grupo de convenio (código = código entidad, descripción "CódigoEntidad - Nombre"); cargar convenios al grupo (**NO modificar convenios existentes**, crear uno nuevo si falta); asignar el grupo a la entidad (STG: grupo "botonsimpl", PRD: el recién creado); configurar canales de cobro por defecto si es agrupadora; configurar portal comercio si aplica (§3); crear comercio inicial; si tiene CBU individual, agregarla como vendedora en Coelsa.

**Validaciones:** semáforos en Admin > Entidades > Datos de la entidad; reglas de pago cargadas; QR funcionando.

## 2. Crear entidad en cobro — PSP ≠ 184

Mismo flujo que §1, con diferencias: Identificador PSP = ID PSP STAGING/PRODUCCIÓN en Coelsa de la entidad; Dominio adquiriente y Id de cuenta según homologación propia (si cobra con QR); agente de retención = "Otro" (⚠️ consultar si será su propio agente; si no es Bind PSP ni el Banco, solicitar soporte a Administración).

⚠️ **Si una entidad ≠ 184/164 quiere cobrar con QR: pedir meet con Emma o especialistas de negocio antes de continuar.** Verificar: ¿homologó aceptador? ¿usan nuestro QR o el suyo?

## 3. Crear nueva entidad vía Swagger (body completo)

Swagger de la API de Comercio: Producción `http://10.22.0.17/swagger/index.html`, STG `http://10.210.1.6/swagger/index.html`. Endpoint **Crear Nueva Entidad**. Cuentas recaudadoras disponibles: consultar Excel de control interno (pedir link vigente a Integraciones).

Body (Producción, ejemplo real MARKAB):
```json
{
  "datosEntidad": {
    "nombre": "MARKAB", "cuit": "20200495331", "codigo": "A121", "pspId": "184",
    "dominioAdquirente": "com.bind", "administradorId": 1, "administradorNombre": "COELSA",
    "administradorCuit": "30692264785",
    "especificaciones": [
      {"keyEspecificacionTipo": "CUENTAID", "valorEspecificacionTipo": "1", "valorDefault": "1", "valor": "93"},
      {"keyEspecificacionTipo": "CUENTARECAUDADORA", "valorEspecificacionTipo": "1002583642", "valorDefault": "30685029959", "valor": "30685029959"},
      {"keyEspecificacionTipo": "USABACKOFFICE", "valorEspecificacionTipo": "1", "valorDefault": "1", "valor": "1"},
      {"keyEspecificacionTipo": "PLANTILLAEMAILENTIDAD", "valorEspecificacionTipo": "", "valorDefault": "Shared.AccessManagement.Application.Resources.Templates.EmailNewMiembroDefault.html", "valor": "Shared.AccessManagement.Application.Resources.Templates.EmailNewMiembroDefault.html"},
      {"keyEspecificacionTipo": "NOTIFICACION_INTERNA", "valor": "true", "valorDefault": "", "valorEspecificacionTipo": ""},
      {"keyEspecificacionTipo": "PAGO", "valorEspecificacionTipo": "1", "valorDefault": "1", "valor": "1"},
      {"keyEspecificacionTipo": "CONTRACARGO", "valorEspecificacionTipo": "1", "valorDefault": "1", "valor": "1"},
      {"keyEspecificacionTipo": "HabilitacionComercio", "valorEspecificacionTipo": "1", "valorDefault": "1", "valor": "5"},
      {"keyEspecificacionTipo": "AltaComercio", "valorEspecificacionTipo": "2", "valorDefault": "7", "valor": "7"}
    ]
  },
  "datosImpuestos": {
    "razonSocial": "HERLEIN RAMON JAVIER", "idCategoria_IVA": 1, "tipo_Identificacion": 80, "cuit": "30-71744907-6",
    "rG4622_Liq": "S", "iVA3130_Liq": "N", "tipoIIBB": "RS", "numeroIIBB": "1624175-04",
    "iIBB_SIRTAC_Liq": "S", "iIGG_COD_COMP_RET": "05", "iIGG_COD_IMP": "217", "iIGG_COD_COND": "01",
    "iIGG_COD_OP": "1", "iIGG_TIPO_REG": "G", "iIGG_COD_COMP_DEV": "03", "iVA_COD_IMP": "767",
    "iVA_COD_COND_RI": "01", "iVA_COD_COND_OT": "02", "rG4622_REC_HAB_SNC": 200000,
    "calle_Dir": "Maipú", "numero_Dir": "1210", "codigoPostal_Dir": "1006", "localidad_Dir": "CABA", "idProvincia_Dir": 1
  }
}
```

**Cómo obtener el `CUENTAID`:** consultar el endpoint de Coelsa con el CUIT correspondiente, copiar el CBU, buscarlo con Ctrl+F en la respuesta, y usar el `id` devuelto.

Body STG: mismo esquema, cambiando `nombre`/`cuit`/`codigo`/`pspId` ("531")/`dominioAdquirente` ("com.TESTbind") y con `CUENTAID`/`CUENTARECAUDADORA` de prueba.

## 4. Roles por defecto y herencia de convenios (comercios nuevos)

> Fuente: Reunión "Análisis COBRO" (2026-07-27), minuta Gemini — configuración en vivo de la entidad Demo PCP (ver [1_proyectos/proyecto-coca-cola-andina/proyecto.md](../../../1_proyectos/proyecto-coca-cola-andina/proyecto.md)).

**Roles por defecto de un comercio nuevo:** salvo especificación explícita en contra, todo comercio nuevo nace con tres roles: administrador de aceptador, administrador de wallet y administrador de botón simple.

**Herencia de convenios entidad → comercio (diseño en discusión, 2026-08-11):** un comercio muestra hoy, a la vez, los convenios heredados de su entidad y sus convenios propios, sin filtro — genera visualizaciones redundantes. Consenso del equipo (2026-07-27): falta un filtro por **canal + forma de pago** que priorice el convenio específico del comercio sobre el heredado. Abre además el problema de actualizaciones masivas de convenios a nivel entidad con necesidad de excepciones configurables (ej. comercios tipo bingo que no aceptan ciertas tarjetas). Nicolás Colón se lleva el análisis — ver [2_areas/tareas.md](../../../2_areas/tareas.md) T-067.

> Fuente: Reunión "Mejoras en convenios" (2026-08-11), minuta Gemini (Pablo Gomes, Mariana Nadalin, Gonzalo Rivera, Nicolás Colón). **Requiere más debate** (decisión no cerrada) — hallazgos de esta sesión:

- **Creación automática del grupo de convenios de una entidad es inconsistente hoy** — el equipo sospecha que solo dispara si la entidad nace con el canal QR habilitado, sin confirmar la causa exacta. Acuerdo de diseño: toda entidad nueva debería recibir automáticamente su propio grupo de convenios (vacío, código = código de entidad), sin depender del canal.
- **Sin validación de duplicados por forma de pago:** el sistema hoy no impide dos convenios de la misma forma de pago dentro de un mismo canal en un grupo — se queda con el último que se cargó. Propuesta: validar que solo pueda existir un convenio por combinación canal+forma de pago.
- **Diseño propuesto para la retroactividad (la parte que "requiere más debate"):** en vez de reasignar convenios existentes al modificar un grupo, la entidad **crea convenios propios y nuevos** al momento de su alta (no reutiliza los genéricos compartidos entre varias entidades, que hoy generan ~2.694 registros con mucha duplicación por QR). Así, modificar un convenio de esa entidad impacta directo a todos los comercios que lo heredan (misma tabla), sin desasignar/reasignar nada. Para las excepciones puntuales por comercio (ej. sacar tarjeta de crédito a un bingo, caso ya vivido con Sur Finanzas/casinos), Gonzalo Rivera propone un flag `habilitado: 0/1` a nivel comercio en vez de eliminar/reemplazar el convenio heredado — permite que el comercio siga heredando actualizaciones futuras del grupo salvo en el convenio puntual que se inhabilitó. Pablo Gomes lo señala como una solución "sofisticada" que necesita análisis adicional antes de construirse.
- **Convenio asignado manualmente a un comercio debe tener prioridad sobre el heredado** y no debe poder modificarse en el momento de la asignación (Nicolás Colón) — si hace falta otro valor, se crea un convenio nuevo, nunca se pisa el ya existente, para no romper la trazabilidad cuando se actualiza el original.
- **Otros hallazgos de configuración, ya acordados:**
  - Unificar el formato de comisión a **porcentaje siempre** (hoy varía: QR pide 0,6, tarjeta de débito pide 0,06 del mismo valor real — fuente de errores de carga).
  - Vigencia de convenios por defecto pasa de 10 a **100 años** (nunca se revisan, riesgo de vencimientos masivos no contemplados en 4-5 años) — pendiente confirmar si el campo de vigencia siquiera está funcionando hoy.
  - El sistema no deja cargar `0` en tiempo de acreditación (bug menor).
  - Comportamiento de generación automática de convenios QR (sospecha: ligado a reglas de Coelsa o rubro del comercio) sigue sin causa raíz confirmada — Pablo Gomes lo investiga.
  - Falta un campo que indique el **origen del convenio** (heredado vs. asignado manualmente) en el admin — hoy no se distingue, genera confusión operativa.
  - Preconfiguración de canales a nivel entidad solo aplica al momento de creación del comercio — una vez habilitado un canal en un comercio, no es sencillo deshabilitarlo; Pablo Gomes revisa esta lógica.
  - Arancel reducido/comisiones de Coelsa para PSP 184/164 hoy se corrigen manualmente vía Swagger ("hardcodeado") — Coelsa valida por CUIT + actividad comercial, así que una configuración incorrecta en el admin puede alterar masivamente las comisiones de todos los comercios con esos mismos parámetros. Pablo Gomes analiza una solución más robusta.

> ⚠️ **Contradicción registrada (2026-08-24) — ver antes de usar esta sección para diseño nuevo.** La descripción de arriba (§4) es la caracterización informal del mecanismo de herencia de convenios, construida en reuniones de 2026-07-27/2026-08-11 sin conocer el contrato real de la API. El 2026-08-24, un discovery técnico sobre el proyecto `convenios_configuracion` relevó el spec OpenAPI real de la "Api Comercios" (`Shared.Comercio.Api`) y encontró un modelo de datos más preciso (Convenio maestro + ComercioConvenio con override opcional y flag `FromCommerce`) — ver [gestion_convenios_comisiones.md](gestion_convenios_comisiones.md), que **reemplaza** esta sección para efectos de diseño. Se mantiene el texto original de §4 arriba por trazabilidad (fue el consenso del equipo en su momento), pero no debe tomarse como la fuente de verdad del contrato de API. Gap escalado — pendiente de decisión del usuario, ver `gaps_y_preguntas.md`.

**Validación de Access Management por email, no por CUIT:** para Demo PCP se definió validar por email en vez de CUIT, para evitar conflictos con comercios de CUIT duplicado — alternativa al modo estándar (`username`: CUIT vs. `Admin@{codigoComercio}`, ver §6).

**Bloqueo de desarrollo de Access Manager v2:** detenido — el sistema no soporta la convivencia de v1 y v2 (el cambio de versión rompe la conexión a base de datos), bloqueando el pase de v2 a Staging. Fintexa evalúa un proyecto futuro de reestructuración del Admin/Centralizador — ver oportunidad OP-005 en [2_areas/direccion/oportunidades.md](../../../2_areas/direccion/index.md).

## 5. Configurar Portal Comercio

Prerrequisito: la entidad debe estar previamente creada. Pasos: Admin > Entidades > ver detalle de la entidad (ícono ojo) > menú "..." > **"Configuración Portal"** > **Guardar** sin modificar ningún parámetro — habilita el portal con configuración por defecto. ⚠️ Puede demorar hasta una hora en impactar.

## 6. Permitir CUITs duplicados a la entidad

Requiere asignar una especificación vía `POST` a `Comercio → Especificaciones` (Swagger STG `http://10.210.1.6/swagger/index.html`), header `X-ENTIDAD` = ID de la entidad:
```json
{"descripcionGrupo":"FLUJOS","especificaciones":[{"keyEspecificacionTipo":"AltaComercio","valorEspecificacionTipo":"2","valorDefault":"13","valor":"13"}]}
```
En Producción, `valorDefault`/`valor` = `"7"` en vez de `"13"`.

## 7. Hotfix de localidades/código postal — alcance acotado (ticket 789, continuación 2026-08-20)

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini. Continúa el hallazgo de validación de código postal único en localidades ya documentado en [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) (cliente Coto, ticket 789, 2026-08-13).

**Problema tratado en esta sesión:** inconsistencias en las validaciones de localidad y código postal durante la creación y edición de comercios/entidades, presentadas por Daniela Collia (Fintexa).

**Decisión acordada (2026-08-20):**
- El **endpoint de localidades se modifica** para retornar una lista de localidades en vez de una sola — esta tarea se separa en un ticket de menor prioridad (no forma parte del hotfix inmediato).
- El **alcance del hotfix se mantiene limitado** a corregir las validaciones actuales de código postal/localidad — se posterga la reestructuración de la respuesta de la API a un ticket futuro, al no considerarse una urgencia funcional para los usuarios actuales.
- Nicolás Colón queda a cargo de crear el ticket para el ajuste de la lista de localidades y códigos postales, una vez documentado el alcance (Daniela Collia debe indicar explícitamente en el ticket 789 que el cambio de respuesta de localidades queda fuera de alcance de este hotfix).

## Ver también
- [acreditacion_en_linea_configuracion.md](acreditacion_en_linea_configuracion.md) — configuración de entidad para el modelo de acreditación en línea/wallet (Modelo Coto).
- [herramientas_operativas_boton_simple.md](herramientas_operativas_boton_simple.md) — configuración de estilo, canales y alta masiva de CVU para Botón Simple.
- [mejoras_admin_backoffice_prd88.md](mejoras_admin_backoffice_prd88.md) — mejoras recientes al flujo de alta de entidad (IDEA PRD-88).
- [gestion_convenios_comisiones.md](gestion_convenios_comisiones.md) — contrato real de la API de Convenios (2026-08-24) que reemplaza la descripción informal de §4 para efectos de diseño nuevo — ver nota de contradicción en §4.

---
*Última actualización: 2026-08-27 — `/context_merge`: §4 suma nota de contradicción (contrato real de API de convenios releva el mecanismo de herencia, ver `gestion_convenios_comisiones.md`); nueva §7 (hotfix de localidades/código postal, ticket 789, continuación 2026-08-20).*
*Última actualización anterior: 2026-08-14 — `/sync_meetings`: §4 suma el diseño en discusión de herencia/retroactividad de convenios (convenios propios por entidad + flag `habilitado` a nivel comercio) y hallazgos de configuración (formato de comisión, vigencia 100 años, origen del convenio no visible, arancel Coelsa "hardcodeado"). Ver reunión "Mejoras en convenios" (2026-08-11) en `wiki/2_areas/control/log_reuniones.md`.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` (reestructuración PARA en cascada). Contenido sin cambios de fondo; algunos JSON de ejemplo condensados (campos redundantes/vacíos omitidos).*
