---
id: 2026-09-22_arquitectura_desacoplado_control_saldo_minimo
pm: pablo
fecha_captura: 2026-09-22
fuente: "Análisis técnico-funcional (/idea_solution) sobre resiliencia_api_bank — confirmación directa del PM, 2026-09-22, citando explicación verbal del banco"
producto: transversal
tema: Mitigación del riesgo de la ventana de sincronización del modelo desacoplado — política de saldo mínimo, no mecanismo técnico
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/modelo_acoplado_vs_desacoplado.md
tipo_destino: actualizar
contradice: "no — completa la sección de riesgo operativo ya existente con la mitigación concreta que la compañía decidió aplicar"
confianza: alta
estado: en_cola
---

## Conocimiento

El archivo ya documenta el riesgo de la ventana de sincronización (2-5 minutos) del modelo desacoplado: el saldo se actualiza contra un valor que todavía no refleja el core bancario, lo que puede permitir operar sobre un saldo "virtual" inexistente en la realidad. Lo que faltaba documentar es **cómo la compañía decidió mitigar ese riesgo**, confirmado por el responsable de producto durante un análisis técnico-funcional (22/09/2026):

> "Esto según nos explicaron solo implica que nosotros debemos asegurar que las organizaciones con las que operamos nunca queden cerca de cero el saldo, porque puede ser que en un momento en que en la realidad no tengan saldo suficiente, saquen plata y puedan porque virtualmente tienen saldo porque aún no ha actualizado el sistema."

**La mitigación no es un mecanismo técnico nuevo** (no hay un caché adicional, ni un bloqueo, ni una validación de saldo distinta a la que ya existe) — es una **política operativa de saldo mínimo**: las cuentas/organizaciones migradas al modelo desacoplado deben mantener siempre un colchón de saldo suficiente para que ningún movimiento pueda dejarlas en descubierto real durante la ventana de actualización asincrónica.

## Confirmación adicional relevante para el archivo

También se confirmó en el mismo análisis, con el mismo responsable de producto, que:
- **No hay ningún flag ni disparador del lado de la compañía** para activar el modelo desacoplado — es 100% configuración interna del banco por cuenta/subcuenta, sin ningún llamado de API ni parámetro de la compañía involucrado.
- El contrato de API de transferencia desde CVU (endpoint de creación y de consulta de estado) **no cambia entre modelo acoplado y desacoplado** — el propio campo `id` de la respuesta ya distingue el circuito con un prefijo (`WP` = interna desacoplada), es decir, el contrato ya contempla el modelo desacoplado como una variante de comportamiento del mismo endpoint, no como una operación distinta.
- El único frente de impacto real y confirmado es la conciliación del equipo de Administración y Recaudaciones (cambio del identificador de movimiento en el archivo de conciliación, pérdida del reporte horario solo para la cuenta migrada) — ajuste interpretativo/manual de ese equipo, no desarrollo de Ingeniería.
