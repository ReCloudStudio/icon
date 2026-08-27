# ReCloud Icon

ReCloud 品牌图标的源文件与多尺寸导出。

## 目录结构

- `icon.png`：原始位图（1254×1254 RGBA，透明背景）
- `icon.svg`：优化后的矢量图标（蓝渐变，userSpaceOnUse 渐变）
- `main.py`：读取 `icon.svg` 导出多尺寸 PNG
- `output/`：导出的 `icon-{16,32,48,64,96,128,256,512}.png` 与副本 `icon.svg`
- `flake.nix` / `pyproject.toml`：Nix + uv 开发环境

## 环境

```bash
nix develop        # 提供 uv / cairo / librsvg / potrace / imagemagick
```

或直接使用已有的 `uv` 虚拟环境（含 `cairosvg`）。

## 生成多尺寸 PNG

```bash
uv run main.py     # 读取 icon.svg，写入 output/icon-{尺寸}.png
```

## 重新生成 SVG

矢量轮廓由 `potrace` 从位图提取，再替换为蓝渐变填充：

```bash
magick icon.png -alpha extract -threshold 30% -negate shape.pbm
potrace shape.pbm -s --opaque --alphamax 1 --turdsize 2   # 得干净轮廓，替换 fill 为渐变
```
