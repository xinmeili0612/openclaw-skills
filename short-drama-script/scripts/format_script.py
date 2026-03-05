#!/usr/bin/env python3
"""
短剧剧本格式化脚本
将大纲转换为标准文学剧本格式
"""

import argparse
import re
from datetime import datetime
from typing import List, Dict, Any

class ScriptFormatter:
    """剧本格式化器"""
    
    def __init__(self):
        self.scene_types = ["内景", "外景", "日", "夜", "晨", "黄昏"]
        self.shot_types = ["全景", "中景", "近景", "特写", "大特写", "俯拍", "仰拍"]
        self.character_emotions = ["冷静", "激动", "愤怒", "悲伤", "喜悦", "紧张", "疑惑", "坚定"]
    
    def format_script(self, outline: Dict[str, Any], episode: int = 1) -> str:
        """将大纲转换为标准剧本格式"""
        
        script_lines = []
        
        # 剧本头部信息
        script_lines.append(f"《{outline.get('title', '短剧剧本')}》")
        script_lines.append(f"第{episode}集")
        script_lines.append(f"编剧：{outline.get('author', 'AI编剧')}")
        script_lines.append(f"日期：{datetime.now().strftime('%Y年%m月%d日')}")
        script_lines.append("=" * 50)
        script_lines.append("")
        
        # 获取本集信息
        episode_info = self._get_episode_info(outline, episode)
        
        # 场景1：开场
        script_lines.extend(self._create_scene(
            scene_number=1,
            scene_type="内景",
            location=episode_info.get('location', '主角家中/办公室'),
            time="日",
            description=episode_info.get('opening', '主角日常生活的场景')
        ))
        
        script_lines.append("")
        
        # 场景2：冲突引入
        script_lines.extend(self._create_scene(
            scene_number=2,
            scene_type="外景" if episode <= 5 else "内景",
            location=episode_info.get('conflict_location', '公司/街道/重要场所'),
            time="日",
            description=episode_info.get('conflict', '主要冲突发生的场景')
        ))
        
        script_lines.append("")
        
        # 场景3：情感发展
        if episode > 3:  # 从第4集开始加入情感线
            script_lines.extend(self._create_scene(
                scene_number=3,
                scene_type="内景",
                location=episode_info.get('emotional_location', '咖啡厅/公园/家中'),
                time="夜" if episode % 2 == 0 else "日",
                description=episode_info.get('emotional', '情感交流或关系发展的场景')
            ))
            script_lines.append("")
        
        # 场景4：高潮或转折
        script_lines.extend(self._create_scene(
            scene_number=4 if episode <= 3 else 5,
            scene_type="内景" if episode % 2 == 0 else "外景",
            location=episode_info.get('climax_location', '关键场所'),
            time="夜" if episode >= 10 else "日",
            description=episode_info.get('climax', '本集高潮或重要转折点')
        ))
        
        script_lines.append("")
        
        # 场景5：结尾悬念
        script_lines.extend(self._create_scene(
            scene_number=5 if episode <= 3 else 6,
            scene_type="内景",
            location=episode_info.get('ending_location', '主角私人空间'),
            time="夜",
            description=episode_info.get('ending', '留下悬念，为下集铺垫')
        ))
        
        script_lines.append("")
        script_lines.append("【本集完】")
        script_lines.append("")
        script_lines.append("下集预告：")
        script_lines.append(episode_info.get('preview', '冲突升级，新角色出现，关系面临考验'))
        
        return "\n".join(script_lines)
    
    def _get_episode_info(self, outline: Dict[str, Any], episode: int) -> Dict[str, str]:
        """获取本集的具体信息"""
        
        # 从大纲中获取本集信息
        episode_outlines = outline.get('episode_outlines', [])
        if episode_outlines and episode <= len(episode_outlines):
            ep_info = episode_outlines[episode - 1]
        else:
            ep_info = {}
        
        # 获取角色信息
        characters = outline.get('characters', [])
        main_char = next((c for c in characters if c['role'] == '女主角'), characters[0] if characters else {})
        male_char = next((c for c in characters if c['role'] == '男主角'), {})
        villain_char = next((c for c in characters if c['role'] == '反派女配'), {})
        
        # 根据集数生成不同的内容
        if episode == 1:
            return {
                'opening': f"{main_char.get('name', '主角')}的日常生活，展示{main_char.get('personality', '性格特点')}",
                'conflict': f"意外事件发生，{main_char.get('name', '主角')}面临{ep_info.get('title', '挑战')}",
                'climax': f"{main_char.get('name', '主角')}做出重要决定，命运开始改变",
                'ending': f"{main_char.get('name', '主角')}思考未来，悬念：接下来会发生什么？",
                'preview': f"{main_char.get('name', '主角')}将如何应对新的挑战？{villain_char.get('name', '反派')}的阴谋逐渐浮现"
            }
        elif episode <= 5:
            return {
                'opening': f"{main_char.get('name', '主角')}适应新环境，展示{main_char.get('personality', '能力')}",
                'conflict': f"{main_char.get('name', '主角')}与{villain_char.get('name', '反派')}首次交锋",
                'emotional': f"{main_char.get('name', '主角')}与{male_char.get('name', '男主角')}关系开始发展" if male_char else "主角获得支持者",
                'climax': f"{main_char.get('name', '主角')}取得小胜利，获得认可",
                'ending': f"新的挑战出现，{main_char.get('name', '主角')}需要更多准备",
                'preview': f"更大的危机即将来临，{main_char.get('name', '主角')}能否应对？"
            }
        elif episode <= 10:
            return {
                'opening': f"{main_char.get('name', '主角')}面临更复杂的局面",
                'conflict': f"{villain_char.get('name', '反派')}的阴谋升级，{main_char.get('name', '主角')}陷入危机",
                'emotional': f"{main_char.get('name', '主角')}与{male_char.get('name', '男主角')}感情加深" if male_char else "主角获得重要盟友",
                'climax': f"关键转折点，{main_char.get('name', '主角')}发现重要真相",
                'ending': f"{main_char.get('name', '主角')}制定新计划，准备反击",
                'preview': f"最终对决即将开始，各方势力汇聚"
            }
        else:
            return {
                'opening': f"{main_char.get('name', '主角')}为最终挑战做准备",
                'conflict': f"最终冲突爆发，{main_char.get('name', '主角')}面对最大敌人",
                'emotional': f"情感高潮，{main_char.get('name', '主角')}与重要人物的关系面临考验",
                'climax': f"真相大白，所有谜题解开",
                'ending': f"{main_char.get('name', '主角')}的结局，留下续集可能性",
                'preview': f"新的故事即将开始，角色们将走向何方？"
            }
    
    def _create_scene(self, scene_number: int, scene_type: str, location: str, time: str, description: str) -> List[str]:
        """创建一个完整的场景"""
        
        scene_lines = []
        
        # 场景头
        scene_lines.append(f"场景{scene_number}：{scene_type} {location} {time}")
        
        # 开场描述（全景）
        scene_lines.append(f"【全景】{description}")
        
        # 角色出场
        if scene_number == 1:
            scene_lines.append("【近景】主角出现在画面中，表情反映当前心境")
        elif scene_number == 2:
            scene_lines.append("【中景】冲突双方对峙，气氛紧张")
        elif scene_number in [3, 5]:
            scene_lines.append("【特写】关键物品或表情特写，增强情感冲击")
        
        # 对话示例
        if scene_number == 1:
            scene_lines.append("主角（内心独白）：这就是我的生活，平静但总觉得缺少什么...")
        elif scene_number == 2:
            scene_lines.append("反派（冷笑）：你以为你能赢过我吗？")
            scene_lines.append("主角（坚定）：我会证明给你看！")
        elif scene_number == 3:
            scene_lines.append("男主角（温柔）：无论发生什么，我都会在你身边。")
            scene_lines.append("主角（感动）：谢谢你...")
        
        # 动作指示
        if scene_number == 2:
            scene_lines.append("【动作】主角握紧拳头，眼神坚定")
        elif scene_number == 4:
            scene_lines.append("【动作】关键物品掉落，发出清脆声响")
        
        # 音乐提示
        if scene_number == 1:
            scene_lines.append("【音乐】轻松日常的背景音乐")
        elif scene_number == 2:
            scene_lines.append("【音乐】紧张激烈的冲突音乐")
        elif scene_number == 3:
            scene_lines.append("【音乐】温暖抒情的情感音乐")
        elif scene_number >= 4:
            scene_lines.append("【音乐】高潮部分的激昂音乐")
        
        # 转场提示（如果不是最后一个场景）
        if scene_number < 6:
            scene_lines.append("【转场】淡出/切至下一场景")
        
        return scene_lines
    
    def format_to_standard(self, raw_text: str) -> str:
        """将原始文本转换为标准剧本格式"""
        
        lines = raw_text.strip().split('\n')
        formatted_lines = []
        
        current_scene = 0
        in_dialogue = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检测场景开始
            if any(marker in line for marker in ["场景", "SCENE", "scene"]):
                current_scene += 1
                formatted_lines.append(f"场景{current_scene}：{self._extract_scene_info(line)}")
                in_dialogue = False
            
            # 检测角色对话
            elif "：" in line or ":" in line:
                parts = line.split("：") if "：" in line else line.split(":")
                if len(parts) >= 2:
                    character = parts[0].strip()
                    dialogue = "：".join(parts[1:]) if "：" in line else ":".join(parts[1:])
                    
                    # 添加情感指示
                    emotion = self._suggest_emotion(dialogue)
                    formatted_lines.append(f"{character}（{emotion}）：{dialogue}")
                    in_dialogue = True
            
            # 检测动作描述
            elif line.startswith("【") or line.startswith("["):
                formatted_lines.append(line)
                in_dialogue = False
            
            # 检测音乐提示
            elif any(marker in line.lower() for marker in ["音乐", "音效", "music", "sound"]):
                formatted_lines.append(f"【音乐】{line}")
                in_dialogue = False
            
            # 普通描述文本
            else:
                if in_dialogue:
                    # 如果是对话的延续
                    formatted_lines.append(f"    {line}")
                else:
                    # 如果是场景描述
                    if not formatted_lines or not formatted_lines[-1].startswith("【"):
                        formatted_lines.append(f"【全景】{line}")
                    else:
                        formatted_lines.append(f"【中景】{line}")
        
        return "\n".join(formatted_lines)
    
    def _extract_scene_info(self, line: str) -> str:
        """从文本中提取场景信息"""
        
        # 尝试匹配常见模式
        patterns = [
            r'内景.*日', r'外景.*夜', r'内景.*夜', r'外景.*日',
            r'室内.*日', r'室外.*夜', r'室内.*夜', r'室外.*日'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                return match.group(0)
        
        # 如果没有匹配到，使用默认值
        return "内景 未知地点 日"
    
    def _suggest_emotion(self, dialogue: str) -> str:
        """根据对话内容建议情感"""
        
        dialogue_lower = dialogue.lower()
        
        if any(word in dialogue_lower for word in ["爱", "喜欢", "感动", "温暖", "幸福"]):
            return "喜悦"
        elif any(word in dialogue_lower for word in ["恨", "讨厌", "愤怒", "生气", "怒火"]):
            return "愤怒"
        elif any(word in dialogue_lower for word in ["悲伤", "难过", "哭泣", "痛苦", "伤心"]):
            return "悲伤"
        elif any(word in dialogue_lower for word in ["害怕", "恐惧", "紧张", "担心", "焦虑"]):
            return "紧张"
        elif any(word in dialogue_lower for word in ["疑问", "为什么", "怎么", "难道", "疑惑"]):
            return "疑惑"
        elif any(word in dialogue_lower for word in ["坚定", "一定", "必须", "决心", "肯定"]):
            return "坚定"
        else:
            return "平静"

def main():
    parser = argparse.ArgumentParser(description="短剧剧本格式化工具")
    parser.add_argument("--input", required=True, help="输入文件路径（JSON大纲或文本）")
    parser.add_argument("--output", default="formatted_script.txt", help="输出文件路径")
    parser.add_argument("--episode", type=int, default=1, help="要格式化的集数")
    parser.add_argument("--mode", choices=["from_outline", "format_text"], default="from_outline", 
                       help="模式：from_outline从大纲生成，format_text格式化现有文本")
    parser.add_argument("--show", action="store_true", help="直接显示完整剧本，不保存到文件")
    
    args = parser.parse_args()
    
    formatter = ScriptFormatter()
    
    try:
        if args.mode == "from_outline":
            # 从JSON大纲生成
            import json
            with open(args.input, 'r', encoding='utf-8') as f:
                outline = json.load(f)
            
            script = formatter.format_script(outline, args.episode)
        
        else:  # format_text
            # 格式化现有文本
            with open(args.input, 'r', encoding='utf-8') as f:
                raw_text = f.read()
            
            script = formatter.format_to_standard(raw_text)
        
        if args.show:
            # 直接显示完整剧本
            print("=" * 60)
            print(f"🎬 短剧剧本 - 第{args.episode}集")
            print("=" * 60)
            print(script)
            print("=" * 60)
            print(f"📊 剧本信息：{len(script.splitlines())}行，约{len(script)//500 + 1}分钟")
            return
        
        # 保存结果
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(script)
        
        print(f"✅ 剧本已生成并保存到 {args.output}")
        print(f"📊 总行数：{len(script.splitlines())}行")
        
        # 显示完整剧本预览
        print("\n📖 剧本预览：")
        print("-" * 50)
        print(script)
        print("-" * 50)
    
    except Exception as e:
        print(f"❌ 错误：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()