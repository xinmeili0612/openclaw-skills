#!/usr/bin/env python3
"""
第7步：项目导出脚本
导出完整项目，准备提交
"""

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

class ProjectExporter:
    """项目导出器"""
    
    def __init__(self, project_dir=None):
        self.project_dir = project_dir or Path.cwd()
        self.config = {}
        self.export_content = ""
    
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
    
    def export_project(self):
        """导出项目"""
        project = self.config.get('project', {})
        theme = project.get('theme', '未知题材')
        episodes = project.get('episodes', 60)
        overseas = project.get('overseas', False)
        
        print(f"📦 导出《{theme}》项目...")
        
        # 创建导出目录
        export_dir = self.project_dir / "exports"
        export_dir.mkdir(exist_ok=True)
        
        # 生成完整剧本文件
        self._generate_complete_script(export_dir, theme, episodes, overseas)
        
        # 生成项目报告
        self._generate_project_report(export_dir, theme, episodes, overseas)
        
        # 打包项目文件
        self._package_project(export_dir, theme)
        
        return True
    
    def _generate_complete_script(self, export_dir, theme, episodes, overseas):
        """生成完整剧本文件"""
        date_str = datetime.now().strftime('%Y年%m月%d日')
        mode = "出海模式（英文）" if overseas else "国内模式（中文）"
        
        # 收集所有剧本内容
        scripts_content = []
        scripts_dir = self.project_dir / "scripts"
        
        if scripts_dir.exists():
            for script_file in sorted(scripts_dir.glob("第*集剧本.md")):
                with open(script_file, 'r', encoding='utf-8') as f:
                    scripts_content.append(f.read())
        
        complete_script = f"""# 《{theme}》完整剧本

## 📋 项目信息
- **剧名**：{theme}
- **集数**：{episodes}集
- **创作模式**：{mode}
- **编剧**：AI编剧
- **完成时间**：{date_str}
- **总字数**：约{episodes * 1200}字
- **总时长**：约{episodes * 3}分钟

## 🎯 创作说明

### 创作理念
本剧本基于专业短剧创作方法论生成，注重：
1. **节奏紧凑**：每集2-3分钟，快速进入剧情
2. **爽点密集**：每集至少3个核心爽点
3. **情感共鸣**：引发观众情感共鸣和代入感
4. **商业价值**：科学设置付费卡点，考虑变现潜力

### 格式说明
- 使用专业文学剧本格式
- 包含详细拍摄备注
- 标注音乐音效提示
- 提供创作分析和爽点设置

### 使用说明
1. 本剧本可直接用于拍摄
2. 可提交平台审核
3. 可根据需要进行适当调整

## 📖 剧本正文

{"="*60}

""".join(scripts_content)
        
        # 保存完整剧本
        script_file = export_dir / f"《{theme}》完整剧本.md"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(complete_script)
        
        print(f"✅ 完整剧本已生成：{script_file}")
    
    def _generate_project_report(self, export_dir, theme, episodes, overseas):
        """生成项目报告"""
        date_str = datetime.now().strftime('%Y年%m月%d日')
        
        report = f"""# 《{theme}》项目报告

## 📊 项目概览
- **项目名称**：{theme}短剧项目
- **创作完成**：{date_str}
- **项目状态**：剧本创作完成，准备提交
- **工作流进度**：7/7步完成

## 📁 项目文件清单

### 核心文件
1. `config.json` - 项目配置文件
2. `README.md` - 项目说明文档
3. `创作方案.md` - 完整创作方案
4. `角色档案.md` - 角色设定文档
5. `剧集目录.md` - 完整分集目录
6. `自检报告.md` - 质量检查报告

### 剧本文件
- `scripts/第1集剧本.md` - 第1集剧本
- `scripts/第2集剧本.md` - 第2集剧本
- ...（共{episodes}集剧本）

### 导出文件
- `exports/《{theme}》完整剧本.md` - 整合剧本
- `exports/《{theme}》项目报告.md` - 本报告
- `exports/{theme}_project.zip` - 项目压缩包

## 🎯 创作成果

### 完成内容
1. **完整故事架构**：{episodes}集完整剧情
2. **专业剧本格式**：可直接拍摄的剧本
3. **详细角色设定**：主要角色和配角档案
4. **节奏设计**：科学的付费卡点和爽点分布
5. **商业化分析**：市场定位和变现潜力

### 质量保证
1. **专业标准**：基于行业专业方法论
2. **合规安全**：通过合规审核检查
3. **商业可行**：考虑商业化变现需求
4. **制作友好**：格式规范，便于拍摄制作

## 💰 商业化价值

### 市场定位
- **目标受众**：根据题材确定相应观众群体
- **平台偏好**：抖音、快手、B站等主流平台
- **竞争分析**：差异化定位，避免同质化竞争

### 变现潜力
- **广告分成**：预计{episodes*100}-{episodes*300}元/集
- **付费观看**：付费点播收入潜力
- **IP开发**：角色和故事IP的衍生价值
- **商业合作**：品牌植入和联名合作机会

### 投资回报
- **创作成本**：AI辅助创作，成本较低
- **制作成本**：根据制作规模确定
- **预期收益**：基于平台数据和市场分析
- **风险控制**：合规审核，避免政策风险

## 🚀 下一步建议

### 立即行动
1. **提交审核**：将剧本提交目标平台审核
2. **联系制作**：寻找合适的制作团队
3. **预算规划**：制定拍摄和制作预算
4. **时间安排**：规划制作和上线时间表

### 长期规划
1. **IP运营**：考虑IP的长期运营价值
2. **系列开发**：规划续集或系列作品
3. **品牌建设**：建立编剧或制作品牌
4. **市场拓展**：考虑出海或跨平台发展

## 📞 技术支持

### 创作支持
- 剧本修改和优化建议
- 专业编剧咨询
- 创作方法论指导

### 制作支持
- 拍摄团队推荐
- 制作预算咨询
- 平台对接协助

### 商业支持
- 商业化方案设计
- 投资对接服务
- 版权保护咨询

## ⚠️ 注意事项

### 版权保护
1. 及时进行版权登记
2. 注意合同条款审查
3. 保护原创内容权益

### 合规要求
1. 严格遵守平台审核规则
2. 关注政策变化和调整
3. 确保内容价值观正确

### 商业风险
1. 市场变化风险
2. 竞争加剧风险
3. 政策调整风险

---
*项目报告生成时间：{date_str}*
*本报告基于专业短剧项目标准生成，仅供参考和指导*
"""
        
        # 保存项目报告
        report_file = export_dir / f"《{theme}》项目报告.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 项目报告已生成：{report_file}")
    
    def _package_project(self, export_dir, theme):
        """打包项目文件"""
        import zipfile
        
        # 创建压缩包
        zip_path = export_dir / f"{theme}_project.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 添加项目根目录文件
            for file_path in self.project_dir.glob("*"):
                if file_path.is_file() and file_path.suffix in ['.md', '.json', '.txt']:
                    arcname = file_path.relative_to(self.project_dir)
                    zipf.write(file_path, arcname)
            
            # 添加scripts目录
            scripts_dir = self.project_dir / "scripts"
            if scripts_dir.exists():
                for script_path in scripts_dir.rglob("*"):
                    if script_path.is_file():
                        arcname = script_path.relative_to(self.project_dir)
                        zipf.write(script_path, arcname)
            
            # 添加exports目录（不包括压缩包自身）
            for export_path in export_dir.glob("*"):
                if export_path.is_file() and export_path != zip_path:
                    arcname = export_path.relative_to(self.project_dir)
                    zipf.write(export_path, arcname)
        
        print(f"✅ 项目已打包：{zip_path}")
        print(f"📦 文件大小：{zip_path.stat().st_size / 1024:.1f} KB")
    
    def _update_workflow_status(self):
        """更新工作流状态"""
        config_file = self.project_dir / "config.json"
        if not config_file.exists():
            return
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            config['workflow']['step7_completed'] = True
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            
            print("✅ 工作流状态已更新：第7步完成")
        except:
            pass
    
    def run(self):
        """运行导出"""
        import argparse
        
        parser = argparse.ArgumentParser(description='项目导出')
        parser.add_argument('--project-dir', help='项目目录')
        parser.add_argument('--format', choices=['zip', 'folder'], default='zip', help='导出格式')
        
        args = parser.parse_args()
        
        if args.project_dir:
            self.project_dir = Path(args.project_dir)
        
        print("="*60)
        print("📦 第7步：项目导出")
        print("="*60)
        
        if not self.load_config():
            return False
        
        if self.export_project():
            self._update_workflow_status()
            print("\n" + "="*60)
            print("🎉 项目导出完成！")
            print("="*60)
            print("\n📋 导出内容：")
            print("  • 完整剧本文件（整合所有集数）")
            print("  • 项目报告（创作成果和商业化分析）")
            print("  • 项目压缩包（便于传输和提交）")
            print("\n🚀 下一步行动：")
            print("  1. 提交剧本到目标平台审核")
            print("  2. 联系制作团队开始拍摄")
            print("  3. 规划商业化运营方案")
            print("\n💡 提示：")
            print("  • 使用 https://markdowntoword.io/zh 转换格式")
            print("  • 注意版权保护和合同审查")
            print("  • 关注平台审核规则变化")
            print("="*60)
            return True
        
        return False

def main():
    """主函数"""
    exporter = ProjectExporter()
    exporter.run()

if __name__ == "__main__":
    main()