# 故障排除

## 常见问题

### 1. 生成 PPTX 报错 "No module named 'pptx'"

安装 python-pptx：

```bash
pip install python-pptx
```

### 2. PPTX 打开后是空白

检查 slides.json 格式是否正确。每个幻灯片必须包含 `type` 和 `title` 字段。

### 3. 中文字符显示为方块

python-pptx 默认使用 Calibri 字体，可能不支持中文。在 PowerPoint 中手动更换字体即可。

### 4. 想要更多幻灯片类型

编辑 `scripts/generate_pptx.py`，在 `generate_pptx` 函数中添加新的类型处理。

### 5. JSON 格式错误

使用 JSON 验证器检查格式：

```bash
python -m json.tool slides.json
```

## 性能基准

- 10 张幻灯片：< 2 秒
- 30 张幻灯片：< 5 秒
- 100 张幻灯片：< 15 秒
