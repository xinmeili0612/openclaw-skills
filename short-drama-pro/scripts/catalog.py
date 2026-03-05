#!/usr/bin/env python3
"""
第4步：目录生成脚本
生成50-100集完整目录，标记付费卡点
"""

import json
import sys
from datetime import datetime
from pathlib import Path

class CatalogGenerator:
    """目录生成器"""
    
    def __init__(self, project_dir=None):
        self.project_dir = project_dir or Path.cwd()
        self.config = {}
        self.catalog_content = ""
    
    def load_config(self):
        """加载配置"""
        config_file = self.project_dir / "config.json"
        if not config_file.exists():
            print("❌ 未找到配置文件")
            return False
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            return True
        except:
            return False
    
    def generate_catalog(self):
        """生成目录"""
        project = self.config.get('project', {})
        theme = project.get('theme', '未知题材')
        episodes = project.get('episodes', 60)
        
        print(f"📚 生成《{theme}》{episodes}集目录...")
        
        self.catalog_content = self._build_catalog_content(theme, episodes)
        return True
    
    def _build_catalog_content(self, theme, episodes):
        """构建目录内容"""
        date_str = datetime.now().strftime('%Y年%m月%d日 %H:%M')
        
        content = f"""# 《{theme}》剧集目录

## 📋 目录总览
- **总集数**：{episodes}集
- **每集时长**：2-3分钟
- **总时长**：{episodes*2}-{episodes*3}分钟（约{episodes*2//60}-{episodes*3//60}小时）
- **生成时间**：{date_str}

## 🎬 分集目录

"""
        
        # 生成每集目录
        for i in range(1, episodes + 1):
            title, conflict, mark = self._generate_episode_info(theme, i, episodes)
            content += f"{mark} 第{i}集：{title}\n"
            content += f"   - 核心冲突：{conflict}\n"
            
            # 每5集加空行
            if i % 5 == 0:
                content += "\n"
        
        # 添加节奏分析
        content += self._generate_rhythm_analysis(episodes)
        
        # 添加重要提示
        content += self._generate_important_notes()
        
        # 添加下一步建议
        content += self._generate_next_steps()
        
        content += f"\n---\n*目录生成时间：{date_str}*\n"
        
        return content
    
    def _generate_episode_info(self, theme, episode_num, total_episodes):
        """生成单集信息"""
        # 根据集数位置确定阶段
        if episode_num <= total_episodes // 4:
            # 第一幕：开端
            phase = "开端"
            mark = "🎯"
        elif episode_num <= total_episodes * 3 // 4:
            # 第二幕：发展
            phase = "发展"
            mark = "⚡"
        else:
            # 第三幕：高潮与结局
            phase = "高潮"
            mark = "🎉"
        
        # 付费卡点标记
        payment_points = self._get_payment_points(total_episodes)
        if episode_num in payment_points:
            mark = "💰"
        
        # 重要集标记
        important_points = [1, total_episodes//2, total_episodes-5, total_episodes]
        if episode_num in important_points:
            mark = "🔥"
        
        # 根据题材和集数生成标题和冲突
        if theme == "霸道总裁":
            title, conflict = self._generate_boss_episode(episode_num, total_episodes, phase)
        elif theme == "真千金是学霸":
            title, conflict = self._generate_true_heir_episode(episode_num, total_episodes, phase)
        else:
            title, conflict = self._generate_general_episode(episode_num, total_episodes, phase, theme)
        
        return title, conflict, mark
    
    def _get_payment_points(self, total_episodes):
        """获取付费卡点位置"""
        if total_episodes < 50:
            return [10, 25, 40]
        elif total_episodes < 80:
            return [10, 25, 40, 55]
        else:
            return [10, 20, 30, 40, 50, 60, 70]
    
    def _generate_boss_episode(self, episode_num, total_episodes, phase):
        """生成霸道总裁单集"""
        templates = {
            "开端": [
                ("意外相遇", "男女主角第一次见面，发生冲突"),
                ("职场初遇", "女主角成为男主角助理，被刁难"),
                ("深夜加班", "两人独处，关系微妙变化"),
                ("商业危机", "公司遇到问题，女主角帮忙"),
                ("家族压力", "男主角被逼婚，女主角伤心")
            ],
            "发展": [
                ("感情升温", "两人经历危机，感情加深"),
                ("情敌出现", "反派女配正式登场"),
                ("商业竞争", "公司面临重大挑战"),
                ("误会产生", "因误会而分开"),
                ("真相大白", "误会解除，感情更深")
            ],
            "高潮": [
                ("最终危机", "最大商业危机爆发"),
                ("感情抉择", "男主角在事业和爱情间选择"),
                ("反派阴谋", "反派最后挣扎，阴谋暴露"),
                ("真情告白", "男主角正式表白"),
                ("圆满结局", "有情人终成眷属")
            ]
        }
        
        phase_templates = templates.get(phase, templates["开端"])
        template_idx = (episode_num - 1) % len(phase_templates)
        return phase_templates[template_idx]
    
    def _generate_true_heir_episode(self, episode_num, total_episodes, phase):
        """生成真千金是学霸单集"""
        templates = {
            "开端": [
                ("命运转折", "贫民窟学霸被豪门认回"),
                ("豪门初入", "第一次进入豪门，面对冷漠"),
                ("假千金挑衅", "假千金表面欢迎实际刁难"),
                ("学校风云", "转学贵族学校，被同学嘲笑"),
                ("实力证明", "用学霸实力打脸看不起她的人")
            ],
            "发展": [
                ("竞赛开始", "参加全国数学竞赛"),
                ("阴谋初现", "假千金开始设计陷害"),
                ("感情萌芽", "与男主角关系发展"),
                ("亲情考验", "亲生父母的冷漠与挣扎"),
                ("真相逼近", "调换婴儿的线索出现")
            ],
            "高潮": [
                ("竞赛决赛", "全国竞赛最终对决"),
                ("阴谋败露", "假千金阴谋被揭穿"),
                ("亲情回归", "亲生父母忏悔和接纳"),
                ("爱情圆满", "与男主角确定关系"),
                ("人生新篇", "开启全新人生")
            ]
        }
        
        phase_templates = templates.get(phase, templates["开端"])
        template_idx = (episode_num - 1) % len(phase_templates)
        return phase_templates[template_idx]
    
    def _generate_general_episode(self, episode_num, total_episodes, phase, theme):
        """通用单集生成"""
        templates = {
            "开端": [
                ("故事开始", "主角出场，建立基础设定"),
                ("冲突初现", "主要矛盾开始出现"),
                ("命运转折", "意外事件改变主角命运"),
                ("新环境", "主角进入新环境，面临挑战"),
                ("首次考验", "主角面临第一次重大考验")
            ],
            "发展": [
                ("关系发展", "主角与其他角色关系加深"),
                ("冲突升级", "主要矛盾更加激烈"),
                ("新挑战", "新的问题和挑战出现"),
                ("成长时刻", "主角获得重要成长"),
                ("转折点", "故事发生重要转折")
            ],
            "高潮": [
                ("最终冲突", "故事的主要冲突达到高潮"),
                ("真相揭示", "重要真相被揭露"),
                ("情感高潮", "情感线达到最高点"),
                ("问题解决", "主要问题得到解决"),
                ("新的开始", "故事结束，新生活开始")
            ]
        }
        
        phase_templates = templates.get(phase, templates["开端"])
        template_idx = (episode_num - 1) % len(phase_templates)
        title, conflict = phase_templates[template_idx]
        
        # 根据题材调整
        if "重生" in theme:
            conflict = f"利用前世记忆{conflict}"
        elif "战神" in theme:
            conflict = f"展现战神实力{conflict}"
        elif "甜宠" in theme:
            conflict = f"甜蜜互动，{conflict}"
        
        return title, conflict
    
    def _generate_rhythm_analysis(self, episodes):
        """生成节奏分析"""
        act1_end = episodes // 4
        act2_end = episodes * 3 // 4
        act3_end = episodes
        
        payment_points = self._get_payment_points(episodes)
        payment_str = "、".join([f"第{p}集" for p in payment_points])
        
        return f"""
## 📊 节奏分析

### 三幕结构
1. **第一幕：开端（1-{act1_end}集）** - 建立主角困境，引发观众共鸣
2. **第二幕：发展（{act1_end+1}-{act2_end}集）** - 冲突升级，情节发展，关系建立
3. **第三幕：高潮与结局（{act2_end+1}-{episodes}集）** - 最终解决，情感升华，留续集悬念

### 付费卡点分布
{payment_str}

### 爽点密度
- **每集至少1个核心爽点**：身份反转、实力打脸、情感共鸣
- **每3集1个中等爽点**：小高潮、关系突破、阴谋揭露
- **每10集1个大爽点**：重大反转、真相大白、情感高潮
- **付费卡点集必须有高强度爽点**：确保观众愿意付费

### 情感节奏
- **1-{act1_end}集**：建立情感连接，引发观众同情
- **{act1_end+1}-{act2_end}集**：情感发展，关系深化
- **{act2_end+1}-{episodes}集**：情感高潮，圆满结局

"""
    
    def _generate_important_notes(self):
        """生成重要提示"""
        return """
## ⚠️ 重要提示

**请务必预览完整目录后再开始写分集剧本！**

确保：
1. 整体节奏合理，冲突设置恰当
2. 付费卡点位置科学，能有效引导付费
3. 爽点分布均匀，避免观众疲劳
4. 情感发展自然，能引发观众共鸣

如果发现目录有问题，可以：
1. 调整某些集数的冲突设置
2. 重新分配付费卡点位置
3. 优化整体节奏安排

"""
    
    def _generate_next_steps(self):
        """生成下一步建议"""
        return """
## 🚀 下一步

目录确认无误后，可以开始分集剧本创作：

1. **使用命令**：`short-drama-pro episode 1` 生成第1集剧本
2. **按顺序完成**：建议按集数顺序创作，确保剧情连贯
3. **定期自检**：每完成5集运行一次自检：`short-drama-pro check 1-5`
4. **批量生成**：支持批量生成多集剧本

### 创作建议
- 严格按照目录的冲突设置进行创作
- 注意每集的时长控制（2-3分钟）
- 确保每集结尾有钩子，吸引继续观看
- 付费卡点集要特别精心设计

"""
    
    def save_catalog(self):
        """保存目录"""
        if not self.catalog_content:
            return False
        
        catalog_file = self.project_dir / "剧集目录.md"
        
        try:
            with open(catalog_file, 'w', encoding='utf-8') as f:
                f.write(self.catalog_content)
            
            # 更新工作流状态
            self._update_workflow_status()
            
            print(f"✅ 剧集目录已保存：{catalog_file}")
            return True
        except Exception as e:
            print(f"❌ 保存失败：{e}")
            return False
    
    def _update_workflow_status(self):
        """更新工作流状态"""
        config_file = self.project_dir / "config.json"
        if not config_file.exists():
            return
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            config['workflow']['step4_completed'] = True
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            
            print("✅ 工作流状态已更新：第4步完成")
        except:
            pass
    
    def run(self):
        """运行目录生成"""
        print("="*60)
        print("📚 第4步：生成剧集目录")
        print("="*60)
        
        if not self.load_config():
            return False
        
        if self.generate_catalog():
            if self.save_catalog():
                print("\n" + "="*60)
                print("✅ 剧集目录生成完成！")
                print("="*60)
                print("\n📋 目录包含：")
                print(f"  • {self.config.get('project', {}).get('episodes', 60)}集完整规划")
                print("  • 每集标题和核心冲突")
                print("  • 付费卡点标记（💰）和重要集标记（🔥）")
                print("  • 节奏分析和创作建议")
                print("\n🚀 下一步：")
                print("  short-drama-pro episode 1    # 生成第1集剧本")
                print("="*60)
                return True
        
        return False

def main():
    """主函数"""
    generator = CatalogGenerator()
    generator.run()

if __name__ == "__main__":
    main()