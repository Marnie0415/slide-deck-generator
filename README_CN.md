# Slide Deck Generator - 幻灯片生成器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Version](https://img.shields.io/badge/Version-1.1.0-blue)]()

> 把笔记、文本、代码变成可编辑的 PowerPoint 演示文稿。

## 功能

从 Markdown 笔记、技术大纲或代码生成完整的幻灯片，支持导出为真实 .pptx 文件。

## 安装

### 步骤 1：克隆仓库

```bash
git clone https://github.com/Marnie0415/slide-deck-generator.git
```

### 步骤 2：复制到 skills 目录

**macOS / Linux：**

```bash
cp -r slide-deck-generator ~/.claude/skills/
```

**Windows (PowerShell)：**

```powershell
Copy-Item -Path "slide-deck-generator" -Destination "$env:USERPROFILE\.claude\skills\slide-deck-generator" -Recurse
```

### 步骤 3：安装依赖（可选，用于生成 PPTX）

```bash
pip install python-pptx
```

## 使用方法

```text
用我的笔记生成幻灯片
```

## 包含工具

### PPTX 生成器 (`scripts/generate_pptx.py`)

从 JSON 生成真实 PowerPoint 文件：

```bash
python scripts/generate_pptx.py slides.json output.pptx
```

## 故障排除

详见 [故障排除指南](docs/troubleshooting.md)
