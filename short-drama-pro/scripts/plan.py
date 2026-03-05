#!/usr/bin/env python3
"""
第2步：创作方案生成脚本
生成完整的故事骨架、节奏设计、商业化分析
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

class PlanGenerator:
    """创作方案生成器"""
    
    def __init__(self, config_file=None, project_dir=None):
        self.config_file = config_file
        self.project_dir = project_dir or Path.cwd()
        self.config = {}
        self.plan_content = ""
        
    def load_config(self):
        """加载配置文件"""
        if not self.config_file:
            # 在项目目录中查找config.json
            config_files = list(self.project_dir.glob("**/config.json"))
            if not config_files:
                print("❌ 未找到配置文件，请先运行第1步：short-drama-pro start")
                return False
            
            self.config_file = config_files[0]
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"✅ 配置文件加载成功：{self.config_file}")
            return True
        except Exception as e:
            print(f"❌ 配置文件加载失败：{e}")
            return False
    
    def generate_plan(self):
        """生成创作方案"""
        if not self.config:
            if not self.load_config():
                return False
        
        project = self.config.get('project', {})
        theme = project.get('theme', '未知题材')
        episodes = project.get('episodes', 60)
        overseas = project.get('overseas', False)
        
        print(f"🎬 生成《{theme}》创作方案...")
        
        # 构建方案内容
        self.plan_content = self._build_plan_content(theme, episodes, overseas)
        
        return True
    
    def _build_plan_content(self, theme, episodes, overseas):
        """构建方案内容"""
        date_str = datetime.now().strftime('%Y年%m月%d日 %H:%M')
        mode = "出海模式（英文）" if overseas else "国内模式（中文）"
        
        content = f"""# 《{theme}》创作方案

## 📋 项目信息
- **题材类型**：{theme}
- **集数规模**：{episodes}集
- **创作模式**：{mode}
- **生成时间**：{date_str}

## 🎯 故事核心概念

### 一句话梗概
【{self._generate_one_line_summary(theme)}】

### 核心冲突
1. **主要冲突**：{self._generate_main_conflict(theme)}
2. **次要冲突**：{self._generate_secondary_conflict(theme)}
3. **内在冲突**：{self._generate_internal_conflict(theme)}

### 世界观设定
{self._generate_world_setting(theme)}

## 📊 节奏设计

### 整体节奏
{self._generate_rhythm_overview(episodes)}

### 付费卡点策略
{self._generate_payment_strategy(episodes)}

### 爽点分布
{self._generate_excitement_distribution()}

## 🎬 开篇黄金法则

### 前5秒抓人
{self._generate_opening_hook(theme)}

### 第1集结构
{self._generate_episode1_structure()}

## 💰 商业化分析

### 市场定位
{self._generate_market_positioning(theme)}

### 变现潜力
{self._generate_monetization_potential(theme, episodes)}

### 平台偏好
{self._generate_platform_preference(theme)}

## 📝 创作要点

### 内容要求
{self._generate_content_requirements()}

### 技术要点
{self._generate_technical_points()}

## 🔄 工作流程

### 下一步：角色开发
{self._generate_next_steps()}

### 时间安排
{self._generate_timeline(episodes)}

## ⚠️ 注意事项

### 合规要求
{self._generate_compliance_requirements()}

### 商业风险
{self._generate_business_risks()}

---
*本方案基于专业短剧创作方法论生成，仅供参考和指导。实际创作中请根据具体情况进行调整。*
"""
        
        return content
    
    def _generate_one_line_summary(self, theme):
        """生成一句话梗概"""
        summaries = {
            "霸道总裁": "普通女孩意外成为总裁助理，从误会到相爱，最终收获事业与爱情",
            "真千金是学霸": "贫民窟学霸被豪门认回，用知识逆袭人生，打脸假千金",
            "重生穿越": "女主重生回到十年前，利用前世记忆逆袭人生，惩治渣男贱女",
            "战神归来": "战神隐姓埋名回归都市，保护家人，惩治恶势力",
            "甜宠": "甜蜜爱情故事，从相识到相守，全程高甜无虐",
            "都市情感": "现代都市中的爱情故事，探讨情感与事业的平衡",
            "古装宫廷": "古代宫廷中的权谋与爱情，妃嫔争宠，皇子夺嫡",
            "励志逆袭": "底层人物通过努力逆袭成功，实现人生价值",
            "家庭伦理": "家庭关系中的矛盾与和解，亲情与责任的冲突",
            "萌宝": "萌娃助攻父母爱情，温馨治愈的家庭故事",
            "悬疑探案": "侦探破解谜案，揭露真相，维护正义",
            "软科幻": "近未来科技背景下的情感故事，科技与人性交织",
            "末日重生": "末日危机中的生存与爱情，人性考验与希望",
            "喜剧": "轻松搞笑的故事，幽默中蕴含人生哲理"
        }
        
        return summaries.get(theme, f"{theme}题材的精彩故事，充满冲突与反转")
    
    def _generate_main_conflict(self, theme):
        """生成主要冲突"""
        conflicts = {
            "霸道总裁": "阶级差异与真爱的冲突，商业竞争与个人情感的矛盾",
            "真千金是学霸": "真假千金的身份对立，贫富阶级的价值冲突",
            "重生穿越": "前世今生的命运对抗，复仇与救赎的情感挣扎",
            "战神归来": "隐藏身份与保护家人的矛盾，正义与邪恶的终极对决"
        }
        
        return conflicts.get(theme, "身份、阶级、情感的多重矛盾交织")
    
    def _generate_secondary_conflict(self, theme):
        """生成次要冲突"""
        return "人际关系复杂纠葛，事业发展面临挑战，友情与爱情的抉择"
    
    def _generate_internal_conflict(self, theme):
        """生成内在冲突"""
        return "主角的内心挣扎与成长，价值观的碰撞与重塑，自我认同的追寻"
    
    def _generate_world_setting(self, theme):
        """生成世界观设定"""
        settings = {
            "霸道总裁": """
- **时代背景**：现代都市，商业社会
- **社会结构**：明显的阶级分层，豪门与普通人的巨大差距
- **特殊设定**：商业帝国、豪门恩怨、职场竞争""",
            
            "真千金是学霸": """
- **时代背景**：现代中国，教育竞争激烈的社会
- **社会结构**：贫富差距明显，教育资源分配不均
- **特殊设定**：豪门家族、真假千金、学霸逆袭""",
            
            "重生穿越": """
- **时代背景**：现代与过去的时空交错
- **社会结构**：不同时代的社会规则和价值观念
- **特殊设定**：重生记忆、时空穿越、命运改变"""
        }
        
        return settings.get(theme, """
- **时代背景**：根据题材设定相应时代
- **社会结构**：阶级分布、权力关系、社会规则
- **特殊设定**：根据题材的特殊元素进行设定""")
    
    def _generate_rhythm_overview(self, episodes):
        """生成节奏概述"""
        act1_end = episodes // 4
        act2_end = episodes * 3 // 4
        act3_end = episodes
        
        return f"""
- **第一幕：开端（1-{act1_end}集）** - 建立主角困境，引发观众共鸣
- **第二幕：发展（{act1_end+1}-{act2_end}集）** - 冲突升级，情节发展，关系建立
- **第三幕：高潮（{act2_end+1}-{act3_end-5}集）** - 最终冲突爆发，真相揭示
- **第四幕：结局（{act3_end-4}-{episodes}集）** - 冲突解决，情感升华，留续集悬念"""
    
    def _generate_payment_strategy(self, episodes):
        """生成付费卡点策略"""
        if episodes < 50:
            payment_points = [10, 25, 40]
        elif episodes < 80:
            payment_points = [10, 25, 40, 55]
        else:
            payment_points = [10, 20, 30, 40, 50, 60, 70]
        
        strategy = ""
        for i, point in enumerate(payment_points):
            if point <= episodes:
                desc = [
                    "第一个付费卡点（小高潮，建立核心冲突）",
                    "第二个付费卡点（关系突破，情感发展）",
                    "第三个付费卡点（重大转折，真相逼近）",
                    "第四个付费卡点（最终对决前）",
                    "第五个付费卡点（新冲突出现）",
                    "第六个付费卡点（情感高潮）",
                    "第七个付费卡点（大结局前）"
                ][i] if i < 7 else "付费卡点"
                strategy += f"- **第{point}集**：{desc}\n"
        
        return strategy
    
    def _generate_excitement_distribution(self):
        """生成爽点分布"""
        return """
- **每集至少1个核心爽点**：身份反转、实力打脸、情感共鸣等
- **每3集1个中等爽点**：小高潮、关系突破、阴谋揭露等
- **每10集1个大爽点**：重大反转、真相大白、情感高潮等
- **付费卡点集必须有高强度爽点**：确保观众愿意付费"""
    
    def _generate_opening_hook(self, theme):
        """生成开篇钩子"""
        return """
1. **视觉冲击**：强烈对比画面或意外事件开场
2. **情感共鸣**：立即建立主角困境，引发观众同情
3. **悬念设置**：留下"接下来会发生什么"的强烈疑问
4. **节奏快速**：前30秒必须进入第一个冲突点"""
    
    def _generate_episode1_structure(self):
        """生成第1集结构"""
        return """
1. **开场（0-30秒）**：主角日常生活展示，建立基础人设
2. **转折（30-90秒）**：意外事件发生，命运开始转折
3. **冲突（90-150秒）**：主要矛盾建立，冲突升级
4. **悬念（150-180秒）**：留下强烈钩子，吸引继续观看"""
    
    def _generate_market_positioning(self, theme):
        """生成市场定位"""
        positioning = {
            "霸道总裁": """
- **目标受众**：女性18-35岁，喜欢浪漫爱情、豪门恩怨
- **情感需求**：对完美爱情的向往，对阶级跨越的幻想
- **观看场景**：碎片化时间，寻求情感慰藉和娱乐放松""",
            
            "真千金是学霸": """
- **目标受众**：女性15-30岁，学生和年轻职场女性
- **情感需求**：对逆袭成功的渴望，对公平正义的追求
- **观看场景**：学习工作间隙，寻求励志和情感共鸣""",
            
            "重生穿越": """
- **目标受众**：女性20-40岁，喜欢复仇逆袭、命运改变
- **情感需求**：对人生重来的幻想，对正义伸张的渴望
- **观看场景**：晚间休息时间，寻求爽感和情感释放"""
        }
        
        return positioning.get(theme, """
- **目标受众**：根据题材确定相应年龄和性别的观众
- **情感需求**：满足观众的娱乐、情感、幻想等需求
- **观看场景**：碎片化时间，寻求快速的情感满足""")
    
    def _generate_monetization_potential(self, theme, episodes):
        """生成变现潜力分析"""
        return f"""
- **平台分成**：广告收入预计{episodes*100}-{episodes*300}元/集
- **付费观看**：付费点播预计{episodes*500}-{episodes*2000}元总收入
- **IP开发**：角色IP、故事IP的衍生价值潜力巨大
- **商业合作**：品牌植入、联名合作等商业机会丰富"""
    
    def _generate_platform_preference(self, theme):
        """生成平台偏好"""
        return """
- **抖音**：适合快节奏、强冲突、视觉冲击强的题材
- **快手**：适合接地气、情感真挚、生活化的题材
- **B站**：适合有深度、有创意、年轻化的题材
- **微信视频号**：适合正能量、价值观正确、情感共鸣强的题材"""
    
    def _generate_content_requirements(self):
        """生成内容要求"""
        return """
1. **原创性**：避免抄袭，确保内容原创，有独特创意
2. **专业性**：使用专业剧本格式，符合拍摄要求
3. **合规性**：严格遵守平台审核要求，避免违规内容
4. **商业性**：考虑商业化变现可能，设置付费卡点"""
    
    def _generate_technical_points(self):
        """生成技术要点"""
        return """
1. **格式规范**：使用标准剧本格式，包括场景、对话、动作等
2. **节奏控制**：爽点密集，节奏快速，避免拖沓
3. **情感共鸣**：引发观众情感共鸣，建立情感连接
4. **悬念设置**：每集结尾必须留下钩子，吸引继续观看"""
    
    def _generate_next_steps(self):
        """生成下一步建议"""
        return """
1. **主角设定**：确定主角姓名、年龄、性格、背景、动机
2. **配角设定**：开发反派、朋友、家人等重要配角
3. **人物关系**：绘制人物关系图，明确角色之间的关联
4. **成长弧线**：设计主角的成长变化和心路历程"""
    
    def _generate_timeline(self, episodes):
        """生成时间安排"""
        weeks = max(1, episodes // 15)
        return f"""
- **第1周**：完成1-15集剧本创作和修改
- **第2周**：完成16-30集剧本创作和修改
- **第3周**：完成31-45集剧本创作和修改
- **第4周**：完成46-{episodes}集剧本创作+整体修改
- **总周期**：{weeks}周完成全部{episodes}集剧本"""
    
    def _generate_compliance_requirements(self):
        """生成合规要求"""
        return """
1. **政治敏感**：避免涉及政治敏感内容，不讨论敏感话题
2. **暴力血腥**：控制暴力血腥程度，避免过度描写
3. **色情低俗**：避免色情低俗内容，保持健康积极
4. **价值观**：符合社会主义核心价值观，弘扬正能量"""
    
    def _generate_business_risks(self):
        """生成商业风险"""
        return """
1. **市场变化**：观众口味变化快，需要及时调整内容
2. **政策调整**：监管政策可能变化，需要关注政策动向
3. **竞争加剧**：短剧市场竞争激烈，需要差异化创新
4. **版权纠纷**：确保内容原创，避免版权问题"""
    
    def save_plan(self):
        """保存创作方案"""
        if not self.plan_content:
            print("❌ 未生成方案内容")
            return False
        
        plan_file = self.project_dir / "创作方案.md"
        
        try:
            with open(plan_file, 'w', encoding='utf-8') as f:
                f.write(self.plan_content)
            
            print(f"✅ 创作方案已保存：{plan_file}")
            
            # 更新工作流状态
            self._update_workflow_status()
            
            return True
        except Exception as e:
            print(f"❌ 保存失败：{e}")
            return False
    
    def _update_workflow_status(self):
        """更新工作流状态"""
        config_file = self.config_file
        if not config_file or not os.path.exists(config_file):
            return
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            config['workflow']['step2_completed'] = True
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            
            print("✅ 工作流状态已更新：第2步完成")
        except Exception as e:
            print(f"⚠️ 工作流状态更新失败：{e}")
    
    def run(self, args=None):
        """运行方案生成"""
        import argparse
        
        parser = argparse.ArgumentParser(description='生成创作方案')
        parser.add_argument('--config', help='配置文件路径')
        parser.add_argument('--project-dir', help='项目目录路径')
        
        if args:
            parsed_args = parser.parse_args(args)
        else:
            parsed_args = parser.parse_args()
        
        # 设置参数
        if parsed_args.config:
            self.config_file = parsed_args.config
        if parsed_args.project_dir:
            self.project_dir = Path(parsed_args.project_dir)
        
        print("="*60)
        print("📝 第2步：生成创作方案")
        print("="*60)
        
        # 生成方案
        if self.generate_plan():
            if self.save_plan():
                print("\n" + "="*60)
                print("✅ 创作方案生成完成！")
                print("="*60)
                print("\n📋 下一步建议：")
                print("  short-drama-pro characters    # 第3步：角色开发")
                print("  short-drama-pro catalog       # 第4步：生成目录")
                print("\n💡 创作方案包含：")
                print("  • 故事核心概念和世界观")
                print("  • 节奏设计和付费卡点策略")
                print("  • 商业化分析和市场定位")
                print("  • 创作要点和合规要求")
                print("="*60)
                return True
            else:
                return False
        else:
            return False

def main():
    """主函数"""
    generator = PlanGenerator()
    generator.run()

if __name__ == "__main__":
    main()