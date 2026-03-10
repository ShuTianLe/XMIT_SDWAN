#!/usr/bin/env python3
"""
Copy the starter prototype kit into a destination directory and stamp it with a project name.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

TEXT_EXTENSIONS = {".html", ".css", ".js", ".md", ".txt", ".json"}


def slugify(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized.strip("-") or "prototype"


def copy_template(template_dir: Path, output_dir: Path) -> None:
    for source in template_dir.rglob("*"):
        relative = source.relative_to(template_dir)
        target = output_dir / relative
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def replace_tokens(root: Path, tokens: dict[str, str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        text = path.read_text()
        for token, value in tokens.items():
            text = text.replace(token, value)
        path.write_text(text)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a static HTML prototype starter from the product-html-prototype skill.",
    )
    parser.add_argument("--name", required=True, help="Project or prototype name")
    parser.add_argument("--output", required=True, help="Destination directory")
    parser.add_argument(
        "--tagline",
        default="先把产品逻辑立住，再谈实现细节。",
        help="Short hero line for the starter template",
    )
    parser.add_argument(
        "--accent",
        default="#bf4f2f",
        help="Primary accent color for the starter template",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing destination directory",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "assets" / "prototype-starter"
    output_dir = Path(args.output).expanduser().resolve()

    if not template_dir.exists():
        print(f"[ERROR] Starter template not found: {template_dir}")
        return 1

    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        print(
            "[ERROR] Output directory already exists and is not empty. "
            "Use --force to overwrite.",
        )
        return 1

    if output_dir.exists() and args.force:
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    copy_template(template_dir, output_dir)

    tokens = {
        "__PROJECT_NAME__": args.name,
        "__PROJECT_TAGLINE__": args.tagline,
        "__PROJECT_SLUG__": slugify(args.name),
        "__PRIMARY_ACCENT__": args.accent,
    }
    replace_tokens(output_dir, tokens)

    print(f"[OK] Prototype starter created at {output_dir}")
    print("Files:")
    for path in sorted(output_dir.rglob("*")):
        if path.is_file():
            print(f"  - {path.relative_to(output_dir)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
