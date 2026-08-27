# ReCloud 图标源仓库

本仓库存放 ReCloud Studio 品牌图标的源文件与生成脚本，是 `icon-showcase` 展示站的同步上游。展示站通过 GitHub raw 拉取本仓库的 `output/` 资产，因此本仓库的变更需推送后才对展示站可见。

## 关键文件

- `icon.svg`：主图标，potrace 提取轮廓 + 手动垂直蓝渐变（`linearGradient id=g`，顶浅底深）。仓库核心资产。
- `icon.png`：1254×1254 原始栅格源（透明背景）。
- `main.py`：用 cairosvg 从 `icon.svg` 导出 `output/icon-{16,32,48,64,96,128,256,512}.png`。
- `main_text.py`：合成横排字标（`icon-text.svg`/`icon-text-studio.svg` 及对应多尺寸 PNG），ImageMagick + DejaVuSans-Bold。
- `icon-text.svg` / `icon-text-studio.svg`：带文字图标源。
- `output/`：生成的位图与 SVG（25 个文件），被展示站 `scripts/sync.mjs` 拉取。

## 环境

- Nix：`nix develop`（flake 提供 uv/cairo/librsvg/potrace/imagemagick），或 `direnv allow`。
- Python 依赖：cairosvg（`uv sync` 生成 `.venv`）。
- cairosvg 依赖 libcairo，运行前需 `export LD_LIBRARY_PATH=/nix/store/...cairo.../lib`；直接使用 `uv run main.py` 时 flake shellHook 已设置。

## 常用命令

- `uv run main.py`：重新导出主图标 PNG 到 `output/`。
- `uv run main_text.py`：重新导出带文字字标。
- `bun run sync`（在 icon-showcase 仓库）：从本仓库拉取最新资产。

## 约定

- 提交需 GPG 签名（`git commit -S`）。
- 修改渐变/形状后须重新导出 `output/` 并推送，否则展示站同步到的仍是旧资产。
- 渐变方向保持垂直单调（顶 `#C8E0FD` → 底 `#3069C9`），不要引入环形或对角线分段。
