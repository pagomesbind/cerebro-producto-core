#!/usr/bin/env python
"""
/audit_wiki — auditoria estructural de wiki/ para el Segundo Cerebro Bind PSP.

No arregla nada solo: reporta desvios para que el Bibliotecario (o el usuario)
decida como resolverlos. Pensado para correr en ~30 segundos y dar una foto
completa de salud estructural, no un analisis semantico del contenido.

Chequeos:
  1. Carpetas sin index.md / proyecto.md (excluyendo las 3 excepciones de CLAUDE.md).
  2. Links relativos rotos (formato [texto](ruta/relativa.md#ancla)).
  3. Archivos .md huerfanos: no referenciados por el index.md de su propia carpeta.
  4. Archivos de detalle_productos/ por encima del umbral de fision (~300 lineas)
     o sin "Estado:" declarado en el cuerpo.
  5. Nombres de la lista negra anti-cajon (carpetas o archivos).

Uso: python audit.py [--json]
"""
import os
import re
import sys
import json

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
WIKI = os.path.join(REPO, "wiki")

# Carpetas que no requieren index.md propio (unidades no navegables / hojas autodescriptivas)
INDEX_EXCEPTIONS_NAMES = {"artefactos"}
def is_under_artefactos(path):
    parts = path.replace("\\", "/").split("/")
    return "artefactos" in parts

def is_apis_expuestas_leaf(path):
    parts = path.replace("\\", "/").split("/")
    return "apis_expuestas" in parts and parts[-1] != "apis_expuestas" and parts.index("apis_expuestas") == len(parts) - 2

def is_historial_raw_lote_or_child(path):
    parts = path.replace("\\", "/").split("/")
    if "historial_raw" in parts:
        idx = parts.index("historial_raw")
        return len(parts) > idx + 1  # cualquier cosa dentro de un lote
    return False

BLACKLIST_DIRS = {"transversal", "otros", "varios", "misc", "general"}
BLACKLIST_FILES = {"otros_manuales.md", "manuales_operativos.md"}

FISSION_THRESHOLD = 300
DETALLE_PRODUCTOS = os.path.join(WIKI, "3_recursos", "detalle_productos")

LINK_RE = re.compile(r'\[[^\]]*\]\((?!https?://|mailto:)([^)#\s]+)(#[^)]*)?\)')


def all_dirs():
    out = []
    for root, dirs, files in os.walk(WIKI):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        out.append((root, dirs, files))
    return out


def check_missing_index():
    missing = []
    for root, dirs, files in all_dirs():
        rel = os.path.relpath(root, REPO).replace("\\", "/")
        lower = {f.lower() for f in files}
        if "index.md" in lower or "proyecto.md" in lower:
            continue
        base = os.path.basename(root)
        if base in INDEX_EXCEPTIONS_NAMES or is_under_artefactos(rel):
            continue
        if is_apis_expuestas_leaf(rel):
            continue
        if is_historial_raw_lote_or_child(rel):
            continue
        missing.append(rel)
    return sorted(missing)


def check_broken_links():
    broken = []
    for root, dirs, files in all_dirs():
        for f in files:
            if not f.lower().endswith(".md"):
                continue
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            except Exception as e:
                broken.append({"file": os.path.relpath(fpath, REPO), "link": None, "error": str(e)})
                continue
            for m in LINK_RE.finditer(text):
                target = m.group(1)
                if target.startswith("#"):
                    continue
                resolved = os.path.normpath(os.path.join(root, target))
                if not os.path.exists(resolved):
                    broken.append({
                        "file": os.path.relpath(fpath, REPO).replace("\\", "/"),
                        "link": target,
                    })
    return broken


def check_orphans():
    orphans = []
    for root, dirs, files in all_dirs():
        lower_files = [f for f in files if f.lower().endswith(".md")]
        index_path = None
        for f in files:
            if f.lower() == "index.md":
                index_path = os.path.join(root, f)
                break
        if index_path is None:
            continue
        try:
            with open(index_path, "r", encoding="utf-8") as fh:
                index_text = fh.read()
        except Exception:
            continue
        for f in lower_files:
            if f.lower() in ("index.md",):
                continue
            if f not in index_text:
                orphans.append(os.path.relpath(os.path.join(root, f), REPO).replace("\\", "/"))
    return sorted(orphans)


def check_fission_and_estado():
    flagged = []
    if not os.path.isdir(DETALLE_PRODUCTOS):
        return flagged
    for root, dirs, files in os.walk(DETALLE_PRODUCTOS):
        if "apis_expuestas" in root.replace("\\", "/").split("/"):
            continue  # las apis expuestas tienen su propio estandar, no aplica esta regla
        for f in files:
            if not f.lower().endswith(".md") or f.lower() == "index.md":
                continue
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8") as fh:
                    lines = fh.readlines()
            except Exception:
                continue
            n = len(lines)
            text = "".join(lines)
            has_estado = "Estado:" in text or "Estado :" in text
            issues = []
            if n > FISSION_THRESHOLD:
                issues.append(f"{n} lineas (umbral {FISSION_THRESHOLD})")
            if not has_estado:
                issues.append("sin 'Estado:' declarado")
            if issues:
                flagged.append({"file": os.path.relpath(fpath, REPO).replace("\\", "/"), "issues": issues})
    return flagged


def check_blacklist():
    hits = []
    for root, dirs, files in all_dirs():
        for d in dirs:
            if d.lower() in BLACKLIST_DIRS:
                hits.append(os.path.relpath(os.path.join(root, d), REPO).replace("\\", "/"))
        for f in files:
            if f.lower() in BLACKLIST_FILES:
                hits.append(os.path.relpath(os.path.join(root, f), REPO).replace("\\", "/"))
    return sorted(hits)


def main():
    report = {
        "carpetas_sin_index": check_missing_index(),
        "links_rotos": check_broken_links(),
        "archivos_huerfanos": check_orphans(),
        "fision_o_sin_estado": check_fission_and_estado(),
        "nombres_lista_negra": check_blacklist(),
    }
    if "--json" in sys.argv:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return
    total = sum(len(v) for v in report.values())
    print(f"=== /audit_wiki — {total} desvios detectados ===\n")
    print(f"1. Carpetas sin index.md/proyecto.md: {len(report['carpetas_sin_index'])}")
    for x in report["carpetas_sin_index"][:50]:
        print(f"   - {x}")
    print(f"\n2. Links rotos: {len(report['links_rotos'])}")
    for x in report["links_rotos"][:50]:
        print(f"   - {x['file']} -> {x.get('link')}")
    print(f"\n3. Archivos huerfanos (no referenciados por el index.md de su carpeta): {len(report['archivos_huerfanos'])}")
    for x in report["archivos_huerfanos"][:50]:
        print(f"   - {x}")
    print(f"\n4. detalle_productos/ por encima del umbral de fision o sin Estado declarado: {len(report['fision_o_sin_estado'])}")
    for x in report["fision_o_sin_estado"][:50]:
        print(f"   - {x['file']}: {', '.join(x['issues'])}")
    print(f"\n5. Nombres de la lista negra anti-cajon: {len(report['nombres_lista_negra'])}")
    for x in report["nombres_lista_negra"][:50]:
        print(f"   - {x}")


if __name__ == "__main__":
    main()
