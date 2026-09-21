---
id: 2026-09-10_arquitectura_banco_industrial_split_falla_homo
pm: pablo
fecha_captura: 2026-09-10
fuente: "Mail Re: Bind PSP - próximos pasos (2026-09-09, 19:47), Gonzalo Damian Rivera"
producto: transversal
tema: Banco Industrial — funcionalidad SPLIT no funciona en homologación para PSP 531/532 (caso MDA-297905), bloqueante para el track C
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

# 🔴 Banco Industrial — SPLIT falla en homologación

**Fecha:** 2026-09-09  
**Remitente:** Gonzalo Damian RIVERA (grivera@bind.com.ar)  
**Fuente:** Mail RE: Bind PSP - próximos pasos

## Problema

Pruebas de SPLIT en ambiente de homologación (HOMO):
- **No funciona para PSPS 531** (donde funcionaba antes)
- **No funciona para PSPS 532**

Caso abierto: **MDA-297905**

## Contexto

Esto es el **Punto C** de los 3 tracks de Banco Industrial (reunión 02/09):
- A: Migración a desacoplado (Hernán Clarich + Pablo Gomes)
- B: Migración CBU link a Coelsa (PRIT-309, en proceso)
- **C: Funcionalidad SPLIT en PSP 184 (BLOQUEANTE)**

Pablo Gomes estaba a cargo de pruebas y validaciones en homo para confirmar si SPLIT funciona. Resultado: **NO funciona ni en 531 ni en 532.**

## Impacto

- Bloquea la validación funcional para el cliente BI
- PSP 531/532 son los PSPs de prueba de BI
- Sin SPLIT, no se puede avanzar en la homologación cruzada

## Relacionado

- PRD-239 (Alias visible en checkout) — depende de validación SPLIT en banco
- PRD-200 (Validar CVU/CBU) — validaciones de cuenta en alta
- Migración Banco Industrial — dos tracks más en dependencia (desacoplado, CBU link)

> Fuente: Mail "Re: Bind PSP - próximos pasos" (2026-09-09, 19:47)
