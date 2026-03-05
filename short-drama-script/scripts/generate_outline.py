#!/usr/bin/env python3
"""
短剧剧本大纲生成脚本
基于微信公众号文章《短剧动态漫创作，最重要的就是剧本！剧本创作Skill 发布！》
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Dict, List, Any

class ShortDramaOutlineGenerator:
    """短剧大纲生成器"""
    
    def __init__(self):
        self.genres = {
            "爱情": ["霸道总裁", "穿越爱情", "校园纯爱", "职场恋情", "古风言情"],
            "穿越": ["现代穿古代", "古代穿现代", "未来穿现在", "异世界穿越"],
            "重生": ["复仇重生", "逆袭重生", "知识重生", "商业重生"],
            "玄幻": ["修仙", "武侠", "异能", "系统流"],
            "都市": ["职场", "商战", "家庭", "社会现实"]
        }
        
        self.commercial_elements = {
            "爽点": ["打脸反派", "逆袭成功", "获得认可", "爱情圆满"],
            "情感": ["亲情", "友情", "爱情", "家国情怀"],
            "冲突": ["身份对立", "利益冲突", "价值观冲突", "情感纠葛"],
            "悬念": ["身份秘密", "前世今生", "隐藏能力", "未解之谜"]
        }
    
    def generate_outline(self, genre: str, episodes: int = 60, theme: str = None) -> Dict[str, Any]:
        """生成剧本大纲"""
        
        if genre not in self.genres:
            available = ", ".join(self.genres.keys())
            raise ValueError(f"类型 '{genre}' 不支持。可用类型: {available}")
        
        # 确定主题
        if not theme:
            theme = self.genres[genre][0]
        
        # 生成三幕结构
        three_act_structure = self._generate_three_act_structure(episodes)
        
        # 生成角色设定
        characters = self._generate_characters(genre, theme)
        
        # 生成分集大纲
        episode_outlines = self._generate_episode_outlines(episodes, genre, theme)
        
        outline = {
            "title": f"{theme}短剧剧本大纲",
            "genre": genre,
            "theme": theme,
            "episodes": episodes,
            "target_audience": "女性18-35岁" if genre == "爱情" else "大众观众",
            "commercial_value": self._assess_commercial_value(genre),
            "three_act_structure": three_act_structure,
            "characters": characters,
            "episode_outlines": episode_outlines,
            "revenue_reference": {
                "beginner": "20,000 RMB / 60集，15-20天完成",
                "experienced": "月收入50,000-100,000 RMB，年收入可达1,000,000 RMB",
                "requirements": "原创内容，格式正确，完整大纲"
            },
            "generated_at": datetime.now().isoformat(),
            "version": "1.0.0"
        }
        
        return outline
    
    def _generate_three_act_structure(self, episodes: int) -> Dict[str, Any]:
        """生成三幕结构"""
        act1_end = episodes // 4
        act2_end = episodes * 3 // 4
        
        return {
            "第一幕：开端": {
                "范围": f"第1-{act1_end}集",
                "目标": "建立主角困境，引发观众共鸣",
                "关键事件": ["主角出场", "建立初始冲突", "展示主角特质", "设置主要悬念"]
            },
            "第二幕：发展": {
                "范围": f"第{act1_end+1}-{act2_end}集",
                "目标": "冲突升级，情节发展",
                "关键事件": ["小高潮不断", "关系发展", "新冲突出现", "主角成长"]
            },
            "第三幕：高潮与结局": {
                "范围": f"第{act2_end+1}-{episodes}集",
                "目标": "最终冲突解决，情感升华",
                "关键事件": ["最终冲突爆发", "真相揭示", "情感高潮", "结局收尾", "续集悬念"]
            }
        }
    
    def _generate_characters(self, genre: str, theme: str) -> List[Dict[str, Any]]:
        """生成角色设定"""
        characters = []
        
        # 主角
        if genre == "爱情":
            characters.append({
                "name": "林婉儿",
                "role": "女主角",
                "age": "25",
                "personality": "聪明独立、善良坚韧、外柔内刚",
                "background": "现代职场女性/古代大家闺秀",
                "motivation": "追求真爱/实现自我价值",
                "arc": "从被动接受到主动争取，最终获得幸福"
            })
            
            characters.append({
                "name": "顾北辰",
                "role": "男主角",
                "age": "28",
                "personality": "外表冷漠、内心温暖、能力强",
                "background": "集团总裁/王爷将军",
                "motivation": "保护所爱之人/完成使命",
                "arc": "从封闭内心到学会爱与被爱"
            })
        
        elif genre == "穿越":
            characters.append({
                "name": "苏晴",
                "role": "女主角",
                "age": "27",
                "personality": "现代思维、医术高超、适应力强",
                "background": "现代外科医生穿越到古代",
                "motivation": "在古代生存并运用现代知识改变命运",
                "arc": "从迷茫适应到成为时代变革者"
            })
        
        # 反派
        characters.append({
            "name": "慕容雪",
            "role": "反派女配",
            "age": "22",
            "personality": "嫉妒心强、工于心计、表面温柔",
            "background": "贵族千金/职场竞争对手",
            "motivation": "争夺爱情/地位/利益",
            "arc": "从优势到失败，最终可能悔改或受到惩罚"
        })
        
        # 配角
        characters.append({
            "name": "小桃",
            "role": "闺蜜/丫鬟",
            "age": "20",
            "personality": "活泼开朗、忠诚可靠",
            "background": "主角的忠实伙伴",
            "motivation": "帮助主角，保护主角",
            "arc": "陪伴主角成长，可能有自己的感情线"
        })
        
        return characters
    
    def _generate_episode_outlines(self, episodes: int, genre: str, theme: str) -> List[Dict[str, Any]]:
        """生成分集大纲"""
        outlines = []
        
        for i in range(1, min(episodes, 11) + 1):  # 只生成前10集示例
            if i == 1:
                outline = {
                    "episode": i,
                    "title": "命运的相遇",
                    "key_events": [
                        "主角出场，展示日常生活",
                        "意外事件发生（穿越/相遇/冲突）",
                        "建立主要矛盾",
                        "留下悬念，吸引观众继续观看"
                    ],
                    "commercial_elements": ["主角魅力展示", "冲突建立", "悬念设置"],
                    "duration": "2-3分钟"
                }
            elif i <= 5:
                outline = {
                    "episode": i,
                    "title": f"挑战与适应",
                    "key_events": [
                        "主角面对新环境的挑战",
                        "展示主角的智慧和能力",
                        "与反派初次交锋",
                        "建立支持者关系"
                    ],
                    "commercial_elements": ["爽点：小成功", "情感：建立联系", "冲突：初次对抗"],
                    "duration": "2-3分钟"
                }
            else:
                outline = {
                    "episode": i,
                    "title": f"转折点",
                    "key_events": [
                        "情节重要转折",
                        "主角获得关键信息或能力",
                        "关系发展或冲突升级",
                        "为后续高潮铺垫"
                    ],
                    "commercial_elements": ["情节推进", "关系发展", "悬念加深"],
                    "duration": "2-3分钟"
                }
            
            outlines.append(outline)
        
        return outlines
    
    def _assess_commercial_value(self, genre: str) -> Dict[str, Any]:
        """评估商业价值"""
        value_map = {
            "爱情": {"demand": "高", "competition": "高", "revenue_potential": "高", "platform_preference": "抖音、快手"},
            "穿越": {"demand": "中高", "competition": "中", "revenue_potential": "中高", "platform_preference": "B站、腾讯视频"},
            "重生": {"demand": "中", "competition": "中", "revenue_potential": "中", "platform_preference": "起点、晋江"},
            "玄幻": {"demand": "中高", "competition": "高", "revenue_potential": "高", "platform_preference": "腾讯动漫、快看"},
            "都市": {"demand": "中", "competition": "中", "revenue_potential": "中", "platform_preference": "爱奇艺、优酷"}
        }
        
        return value_map.get(genre, {
            "demand": "中",
            "competition": "中",
            "revenue_potential": "中",
            "platform_preference": "多平台"
        })

def main():
    parser = argparse.ArgumentParser(description="短剧剧本大纲生成器")
    parser.add_argument("--genre", required=True, help="剧本类型：爱情、穿越、重生、玄幻、都市")
    parser.add_argument("--episodes", type=int, default=60, help="集数，默认60集")
    parser.add_argument("--theme", help="主题，如'霸道总裁爱上我'")
    parser.add_argument("--output", default="outline.json", help="输出文件路径")
    parser.add_argument("--format", choices=["json", "text", "markdown"], default="json", help="输出格式")
    parser.add_argument("--show", action="store_true", help="直接显示内容，不保存到文件")
    
    args = parser.parse_args()
    
    try:
        generator = ShortDramaOutlineGenerator()
        outline = generator.generate_outline(args.genre, args.episodes, args.theme)
        
        if args.show:
            # 直接显示内容
            print("=" * 60)
            print(f"📖 短剧剧本大纲：《{outline['title']}》")
            print("=" * 60)
            print(f"📝 类型：{outline['genre']}")
            print(f"🎯 主题：{outline['theme']}")
            print(f"📊 集数：{outline['episodes']}集")
            print(f"👥 目标受众：{outline['target_audience']}")
            print(f"💰 商业价值：需求{outline['commercial_value']['demand']}，竞争{outline['commercial_value']['competition']}")
            print()
            
            print("🎬 三幕结构：")
            for act, details in outline['three_act_structure'].items():
                print(f"  {act}：{details['范围']}")
                print(f"    目标：{details['目标']}")
                print(f"    关键事件：{', '.join(details['关键事件'])}")
                print()
            
            print("👤 主要角色：")
            for char in outline['characters']:
                print(f"  {char['name']}（{char['role']}，{char['age']}岁）")
                print(f"    性格：{char['personality']}")
                print(f"    背景：{char['background']}")
                print(f"    动机：{char['motivation']}")
                print()
            
            print("💰 收入参考：")
            for level, info in outline['revenue_reference'].items():
                print(f"  {level}：{info}")
            
            print("=" * 60)
            return
        
        if args.format == "json":
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(outline, f, ensure_ascii=False, indent=2)
            print(f"✅ 大纲已生成并保存到 {args.output}")
        
        elif args.format == "text":
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(f"《{outline['title']}》\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"类型：{outline['genre']}\n")
                f.write(f"主题：{outline['theme']}\n")
                f.write(f"集数：{outline['episodes']}集\n")
                f.write(f"目标受众：{outline['target_audience']}\n\n")
                
                f.write("三幕结构：\n")
                for act, details in outline['three_act_structure'].items():
                    f.write(f"  {act}：{details['范围']}\n")
                    f.write(f"    目标：{details['目标']}\n")
                    f.write(f"    关键事件：{', '.join(details['关键事件'])}\n\n")
                
                f.write("主要角色：\n")
                for char in outline['characters']:
                    f.write(f"  {char['name']}（{char['role']}）\n")
                    f.write(f"    性格：{char['personality']}\n")
                    f.write(f"    背景：{char['background']}\n")
                    f.write(f"    动机：{char['motivation']}\n\n")
            
            print(f"✅ 文本大纲已生成并保存到 {args.output}")
        
        elif args.format == "markdown":
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(f"# {outline['title']}\n\n")
                f.write(f"**类型**：{outline['genre']}  \n")
                f.write(f"**主题**：{outline['theme']}  \n")
                f.write(f"**集数**：{outline['episodes']}集  \n")
                f.write(f"**目标受众**：{outline['target_audience']}  \n\n")
                
                f.write("## 三幕结构\n\n")
                for act, details in outline['three_act_structure'].items():
                    f.write(f"### {act}\n")
                    f.write(f"- **范围**：{details['范围']}\n")
                    f.write(f"- **目标**：{details['目标']}\n")
                    f.write(f"- **关键事件**：\n")
                    for event in details['关键事件']:
                        f.write(f"  - {event}\n")
                    f.write("\n")
                
                f.write("## 主要角色\n\n")
                for char in outline['characters']:
                    f.write(f"### {char['name']}（{char['role']}）\n")
                    f.write(f"- **年龄**：{char['age']}\n")
                    f.write(f"- **性格**：{char['personality']}\n")
                    f.write(f"- **背景**：{char['background']}\n")
                    f.write(f"- **动机**：{char['motivation']}\n")
                    f.write(f"- **成长弧**：{char['arc']}\n\n")
            
            print(f"✅ Markdown大纲已生成并保存到 {args.output}")
    
    except Exception as e:
        print(f"❌ 错误：{e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()