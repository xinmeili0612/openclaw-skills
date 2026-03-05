---
name: google-image-generator
description: 使用Google Image Generation API生成图片，支持中文配字和多种风格。
---

# Google图片生成工具

## 功能特点
- 🎨 支持多种图片风格：科技感、复古、手绘、卡通等
- 📝 支持中文配字，自动添加到图片中
- 📐 支持多种图片比例：16:9（封面）、4:3（文章内）、1:1（正方形）
- ⚡ 快速生成，质量稳定
- 🔑 使用Google API密钥，无需其他平台账号

## 使用方法

### 生成封面图
```bash
openclaw skill google-image-generator generate "AI自动化工作流程图，展示从命令到发布的完整链路，科技感蓝色调，简洁扁平设计，中文标注" --ratio "16:9" --output "cover.png"
```

### 生成文章内图片
```bash
openclaw skill google-image-generator generate "开发者配置API的界面示意图，显示AppID输入框，深色主题UI，中文标注" --ratio "4:3" --output "img1.png"
```

### 生成正方形图片
```bash
openclaw skill google-image-generator generate "微信公众号后台草稿箱界面，显示文章列表，绿色微信品牌色，中文标注" --ratio "1:1" --output "square.png"
```

## 配置说明
- 需要配置GOOGLE_API_KEY环境变量
- 支持自定义图片风格和颜色调性
- 自动处理中文标注，确保图片中的文字清晰可读

## 注意事项
- 生成时间根据图片复杂度和比例而定，通常在10秒到30秒之间
- 图片质量受prompt质量影响，建议使用详细的描述词
- 免费额度有限，超出部分会产生费用