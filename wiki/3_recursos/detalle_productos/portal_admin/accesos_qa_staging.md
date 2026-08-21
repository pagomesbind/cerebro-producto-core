# Accesos de QA — Ambiente STAGING (Admin / Centralizador de Cobro)

> Estado: en producción (ambiente de staging, acceso vigente). Aportado por el PM directo en sesión de trabajo, 2026-08-20, para que futuras sesiones de QA/discovery puedan navegar el portal e inspeccionar pantallas sin depender de que el usuario esté presente.

## Acceso de prueba al Admin (Centralizador de Cobro) en STAGING

- **URL:** https://admin-staging.epays.services/
- **Usuario:** `Admin@Test`
- **Contraseña:** `AdminTest1234`

## ⚠️ Restricción de uso (no negociable)

Este acceso es **solo para navegar e inspeccionar** — nunca para modificar datos. Queda **prohibido clickear cualquier accionable** (guardar, crear, editar, eliminar, habilitar/deshabilitar, etc.) en cualquier sesión que use estas credenciales, sin excepción. Cualquier sesión que las use debe releer y respetar esta restricción antes de interactuar con el portal.

## Nota de riesgo (aceptada expresamente por el PM)

Este Cerebro corre en repos git con push automático — guardar una contraseña en texto plano la deja en el historial de git de esos repos. El PM decidió aceptar el riesgo (ambiente de staging, no productivo) en vez de omitir la contraseña o dejarla fuera del repo.

---
*Fuente: Pablo Gomes, directo en chat (sesión `/idea_start` sobre convenios de entidades/comercios), 2026-08-20.*
