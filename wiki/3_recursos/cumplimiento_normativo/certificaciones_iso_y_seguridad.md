# Certificaciones ISO y de Seguridad en curso

> Estado: discovery/preparación — primer registro en el canon, confianza media (un solo informe lo menciona, sin antecedente en informes previos del mismo emisor).
>
> Fuente: informe mensual del Comité de Arquitectura COE de septiembre 2026 (Fintexa, Alejandro Sfrede), 2026-10-01, threadId `19fdd426c2490389`.

## Qué se sabe

El informe mensual del Comité de Arquitectura COE de septiembre 2026 menciona por primera vez, a nivel de reporte ejecutivo, que Bind PSP tiene **tres certificaciones en curso, en etapa de preparación**:

1. **ISO 9001** (gestión de calidad) — fecha de auditoría ya confirmada (no se detalla la fecha exacta en el informe). El mismo informe lista "Certificación ISO 9001" en el detalle por estado como "🔵 Listo para iniciar desarrollo" — inconsistente con "fecha de auditoría ya confirmada" del resumen ejecutivo, posible desalineación entre resumen y detalle del mismo informe, no aclarada por la fuente.
2. **ISO 27001** (gestión de seguridad de la información) — en preparación, sin fecha de auditoría confirmada todavía. Ver también `3_recursos/arquitectura_sistema/modelo_de_seguridad.md §1.1`, que ya registraba ISO 27001 como "proceso de certificación en curso (no certificado aún)" desde antes.
3. **El programa de seguridad exigido por el socio de procesamiento** — no se nombra el procesador ni el programa específico en el mail; probablemente se trate del programa de seguridad de Mastercard/Visa o de un requisito de Coelsa/Worldsys, pero esto no está confirmado por la fuente.

## Nota de confianza

Este es el primer informe COE que menciona estas tres certificaciones de forma explícita — no hay antecedente en los informes de julio/agosto ya capturados en `arquitectura_sistema/relacion_con_fintexa.md §2`. No se sabe si son iniciativas nuevas de ese mes o si ya venían preparándose sin haber sido reportadas antes al PM.

## Ver también

- [pci_dss_recertificacion.md](pci_dss_recertificacion.md) — recertificación PCI DSS propia de Bind PSP, certificación distinta pero del mismo dominio.
- [`3_recursos/arquitectura_sistema/modelo_de_seguridad.md §1.1`](../arquitectura_sistema/modelo_de_seguridad.md) — ISO 27001 ya mencionado ahí como "en curso" desde el documento de arquitectura del proveedor.

---
*Creado: 2026-10-01 — `/context_merge`, desde informe mensual COE de septiembre 2026 (Pablo Gomes).*
