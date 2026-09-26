import json
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parent
PROJECTS = ROOT / "projects"
OUT = ROOT / "output"

SIZES = [16, 32, 48, 64, 96, 128, 256, 512]


def build_project(proj: Path) -> dict:
    out_dir = OUT / proj.name
    out_dir.mkdir(parents=True, exist_ok=True)

    assets = {}
    for svg_path in sorted(proj.glob("*.svg")):
        stem = svg_path.stem
        svg = svg_path.read_text(encoding="utf-8")
        (out_dir / f"{stem}.svg").write_text(svg, encoding="utf-8")

        pngs = []
        for s in SIZES:
            cairosvg.svg2png(
                bytestring=svg.encode("utf-8"),
                output_width=s,
                write_to=str(out_dir / f"{stem}-{s}.png"),
            )
            pngs.append(f"{stem}-{s}.png")

        assets[stem] = {
            "svg": f"{stem}.svg",
            "png": pngs,
        }
        print(f"  {proj.name}/{stem}: {len(pngs)} PNGs")

    return assets


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"projects": {}}

    for proj in sorted(p for p in PROJECTS.iterdir() if p.is_dir()):
        print(f"[{proj.name}]")
        manifest["projects"][proj.name] = {
            "assets": build_project(proj),
        }

    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"\nExported {len(manifest['projects'])} project(s) to {OUT}/")


if __name__ == "__main__":
    main()
