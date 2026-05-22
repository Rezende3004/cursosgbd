#!/usr/bin/env python3
"""Padroniza comentários de autoria em arquivos SQL do repositório."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
AUTHOR_LINE = "-- Desenvolvido/Adaptado por João Pedro da Costa Rezende"

AUTHOR_PATTERNS = [
    re.compile(r"^\s*--\s*(autor|author)\s*:.*$", re.IGNORECASE),
    re.compile(r"^\s*--\s*(desenvolvido|developed|criado|created|feito)\s+por\s+.*$", re.IGNORECASE),
    re.compile(r"^\s*--\s*(adaptado|adapted)\s+por\s+.*$", re.IGNORECASE),
]


def replace_author_headers(path: Path) -> bool:
    original = path.read_text(encoding="utf-8-sig")
    lines = original.splitlines(keepends=True)
    changed = False
    updated_lines: list[str] = []

    for line in lines:
        newline = "\n" if line.endswith("\n") else ""
        content = line[:-1] if newline else line

        if any(pattern.match(content) for pattern in AUTHOR_PATTERNS):
            updated_lines.append(f"{AUTHOR_LINE}{newline}")
            changed = True
        else:
            updated_lines.append(line)

    updated = "".join(updated_lines)
    if changed and updated != original:
        path.write_text(updated, encoding="utf-8")
        return True

    return False


def main() -> None:
    changed_files = []

    for sql_file in sorted(ROOT.rglob("*.sql")):
        if ".git" in sql_file.parts:
            continue

        if replace_author_headers(sql_file):
            changed_files.append(sql_file.relative_to(ROOT))

    if not changed_files:
        print("Nenhum cabeçalho de autoria encontrado para substituição.")
        return

    print("Cabeçalhos atualizados:")
    for file_path in changed_files:
        print(f"- {file_path}")


if __name__ == "__main__":
    main()
