import cairosvg
from pathlib import Path

OUT = Path("output")
SRC = Path("icon.svg")

SIZES = [16, 32, 48, 64, 96, 128, 256, 512]


def main():
    svg = SRC.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)

    (OUT / "icon.svg").write_text(svg, encoding="utf-8")

    for s in SIZES:
        cairosvg.svg2png(
            bytestring=svg.encode("utf-8"),
            output_width=s,
            output_height=s,
            write_to=str(OUT / f"icon-{s}.png"),
        )

    print(f"SVG + PNGs exported to {OUT}/: " + ", ".join(f"icon-{s}.png" for s in SIZES))


if __name__ == "__main__":
    main()
