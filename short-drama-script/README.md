# 短剧剧本生成技能

基于微信公众号文章《短剧动态漫创作，最重要的就是剧本！剧本创作Skill 发布！》开发的短剧剧本生成工具。

## 📦 安装

### 自动安装
```bash
# 如果使用OpenClaw技能系统
openclaw skill install short-drama-script
```

### 手动安装
```bash
# 复制技能文件夹到技能目录
cp -r short-drama-script ~/.openclaw/workspace/skills/
```

## 🚀 快速开始

### 1. 生成剧本大纲
```bash
python scripts/generate_outline.py --genre "爱情" --episodes 60 --theme "霸道总裁爱上我"
```

### 2. 格式化剧本
```bash
python scripts/format_script.py --input outline.json --output script_ep1.txt --episode 1
```

### 3. 市场分析
```bash
python scripts/market_analysis.py --action market --genre "爱情" --platform "抖音"
```

## 📁 文件结构

```
short-drama-script/
├── SKILL.md                    # 技能主文档
├── _meta.json                  # 技能元数据
├── README.md                   # 本文件
└── scripts/                    # 脚本文件
    ├── generate_outline.py     # 大纲生成脚本
    ├── format_script.py        # 剧本格式化脚本
    └── market_analysis.py      # 市场分析脚本
```

## 🔧 脚本说明

### generate_outline.py
生成完整的短剧剧本大纲。

**参数：**
- `--genre`：剧本类型（爱情、穿越、重生、玄幻、都市）
- `--episodes`：集数（默认60）
- `--theme`：主题（可选）
- `--output`：输出文件（默认outline.json）
- `--format`：输出格式（json/text/markdown）

**示例：**
```bash
# 生成爱情短剧大纲
python scripts/generate_outline.py --genre "爱情" --episodes 60 --output "love_drama_outline.json"

# 生成Markdown格式大纲
python scripts/generate_outline.py --genre "穿越" --format markdown --output "穿越短剧大纲.md"
```

### format_script.py
将大纲转换为标准文学剧本格式。

**参数：**
- `--input`：输入文件（JSON大纲或文本）
- `--output`：输出文件（默认formatted_script.txt）
- `--episode`：要格式化的集数（默认1）
- `--mode`：模式（from_outline从大纲生成，format_text格式化现有文本）

**示例：**
```bash
# 从大纲生成第1集剧本
python scripts/format_script.py --input outline.json --episode 1 --output "episode_1.txt"

# 格式化现有文本
python scripts/format_script.py --input raw_script.txt --mode format_text --output "formatted.txt"
```

### market_analysis.py
分析短剧市场趋势和商业机会。

**参数：**
- `--action`：分析类型（market市场分析、competition竞争分析、business_plan商业计划）
- `--genre`：剧本类型
- `--platform`：平台
- `--top`：竞争对手数量（默认10）
- `--budget`：商业计划预算（默认50000）
- `--output`：输出文件（默认market_analysis.json）

**示例：**
```bash
# 市场分析
python scripts/market_analysis.py --action market --genre "爱情" --platform "抖音"

# 竞争分析
python scripts/market_analysis.py --action competition --genre "穿越" --top 5

# 商业计划
python scripts/market_analysis.py --action business_plan --genre "玄幻" --platform "B站" --budget 100000
```

## 💰 收入参考

### 新人作者
- **剧本价格**：2万/60集
- **完成时间**：15-20天
- **月收入**：2-6万元
- **投稿要求**：原创内容，格式正确，完整大纲

### 资深作者
- **月收入**：5-10万元
- **分成收入**：10-30万元
- **年收入**：可达100万元
- **IP价值**：可开发游戏、影视、衍生品

## 🌍 出海机会

### 目标市场
- **东南亚**：文化相近，接受度高
- **欧美**：对东方题材感兴趣
- **中东**：保守但市场潜力大

### 本地化要点
- 调整敏感内容
- 符合当地价值观
- 调整角色形象和场景
- 根据市场调整剧情节奏

## ⚠️ 注意事项

### 创作要点
1. **原创为王**：各平台严厉打击抄袭
2. **格式正确**：格式错误直接拒稿
3. **爽点密集**：短剧需要高频爽点
4. **情感共鸣**：引发观众情感共鸣
5. **商业化**：考虑商业变现可能性

### 行业门槛
1. **经验要求**：新人需要学习期
2. **投稿竞争**：优质稿件竞争激烈
3. **平台规则**：各平台规则不同
4. **版权意识**：保护自己的知识产权

## 🔮 技术集成

### 与AI工具集成
- **Seedance 2.0**：剧本转视频指令
- **ComfyUI/N8N**：工作流自动化
- **AI生图工具**：场景视觉化

### 未来发展
1. **Seedance API**：实现剧本到视频的自动化
2. **AI生图集成**：自动生成场景概念图
3. **语音合成**：自动生成角色配音
4. **多语言翻译**：一键出海翻译

## 📞 支持与反馈

如有问题或建议，请参考：
- 原文公众号：钱来有道
- 作者：冰河好帅
- 技能版本：1.0.0
- 更新日期：2026年3月3日

## 📄 许可证

本技能基于微信公众号文章《短剧动态漫创作，最重要的就是剧本！剧本创作Skill 发布！》开发，仅供学习和参考使用。

---
*使用本技能生成的剧本建议进行人工审核和修改，确保质量和原创性。*