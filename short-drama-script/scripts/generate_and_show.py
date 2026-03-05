#!/usr/bin/env python3
"""
短剧剧本生成与显示脚本
一键生成并直接显示剧本内容
"""

import argparse
import json
import sys
from datetime import datetime

class QuickScriptGenerator:
    """快速剧本生成器"""
    
    def __init__(self):
        self.templates = {
            "真千金是学霸": self._generate_true_heir_script,
            "霸道总裁爱上我": self._generate_boss_love_script,
            "重生之逆袭人生": self._generate_rebirth_script,
            "校园纯爱日记": self._generate_campus_love_script
        }
    
    def generate_script(self, theme, episode=1):
        """生成剧本"""
        if theme in self.templates:
            return self.templates[theme](episode)
        else:
            return self._generate_general_script(theme, episode)
    
    def _generate_true_heir_script(self, episode=1):
        """生成《真千金是学霸》剧本"""
        if episode == 1:
            return self._true_heir_episode_1()
        elif episode == 2:
            return self._true_heir_episode_2()
        elif episode == 3:
            return self._true_heir_episode_3()
        else:
            return self._true_heir_general_episode(episode)
    
    def _true_heir_episode_1(self):
        """第1集：贫民窟的学霸"""
        script = """《真千金是学霸》
第1集：贫民窟的学霸
编剧：AI编剧
日期：{date}
==================================================

场景1：外景 贫民窟街道 晨
【全景】破旧的街道，低矮的房屋，清晨的阳光勉强穿透雾气
【中景】苏清月（18岁，清秀但衣着朴素）背着旧书包走出家门
【特写】她手中拿着一本破旧的数学竞赛题集，边走边看
苏清月（内心独白）：还有三天就是全国数学竞赛了，这道题还需要优化解法...

场景2：内景 苏清月家 日
【全景】狭小但整洁的房间，墙上贴满各种奖状
【近景】苏清月照顾生病的母亲喝药
苏清月（温柔）：妈，药喝了，我中午回来给您热饭。
苏母（虚弱但欣慰）：月月，别光顾着学习，注意身体...
【特写】苏清月看着母亲苍白的脸，眼神坚定
苏清月：妈，等我拿到这次竞赛的奖金，就带您去大医院看病。

场景3：内景 学校教室 日
【全景】普通中学教室，同学们都在嬉闹
【中景】数学老师走进教室，神情严肃
老师：今天模拟考试，最后一道题是去年国际奥赛的压轴题。
【特写】试卷发下来，同学们一片哀嚎
男生A：这什么题啊，看都看不懂！
女生B：又是苏清月的表演时间了...

场景4：内景 学校教室 日
【全景】考试进行中，苏清月快速答题
【特写】她的笔尖在试卷上流畅书写
【闪回】深夜，苏清月在昏暗灯光下自学
苏清月（内心独白）：知识，是改变命运的唯一途径。

场景5：外景 学校门口 傍晚
【全景】苏清月走出校门，手里拿着奖学金
【特写】钱包里是医院缴费单和药费清单
突然，一辆黑色劳斯莱斯停在她面前

场景6：外景 学校门口 傍晚
【全景】车上走下一位中年男人和一位女士
女士（眼眶微红）：孩子，我是...你的亲生母亲。
【特写】苏清月震惊的表情，手中的书包掉落
【音乐】震撼转折的背景音乐起
【画面定格】苏清月难以置信的脸
【字幕】命运的齿轮，开始转动...

【本集完】

下集预告：
豪门认亲！真假千金首次交锋！
假千金林婉儿的温柔陷阱！
苏清月将如何应对全新的豪门生活？""".format(date=datetime.now().strftime('%Y年%m月%d日'))
        
        return script
    
    def _true_heir_episode_2(self):
        """第2集：豪门认亲"""
        script = """《真千金是学霸》
第2集：豪门认亲
编剧：AI编剧
日期：{date}
==================================================

场景1：外景 苏家豪宅大门 日
【全景】气派的欧式别墅，豪华花园
【中景】苏清月从劳斯莱斯上下来
苏清月（内心独白）：这里...就是我的亲生父母家？

场景2：内景 苏家客厅 日
【全景】豪华的客厅，水晶吊灯，真皮沙发
【中景】苏父（威严）和苏母（优雅但冷淡）坐在沙发上
苏父（审视地）：坐吧。
苏清月（礼貌但疏离）：谢谢。

场景3：内景 苏家客厅 日
【中景】林婉儿（打扮精致）从楼梯上走下来
林婉儿（甜美微笑）：这就是清月妹妹吧？欢迎回家！
【特写】林婉儿眼中一闪而过的嫉妒
苏母（对林婉儿温柔）：婉儿，来妈妈这边坐。
【对比镜头】苏母对两个女儿的不同态度

场景4：内景 苏清月房间 夜
【全景】别墅里最小最偏僻的房间
【中景】苏清月整理着从贫民窟带来的物品
苏清月（内心独白）：这里很大，很豪华，但...很冷。

场景5：内景 林婉儿房间 夜
【全景】豪华公主房，满柜名牌
【特写】林婉儿撕碎苏清月的照片
林婉儿（阴冷）：苏清月...你为什么要回来？
【动作】她拿起手机拨通电话
林婉儿：王姨，明天学校那边...你知道该怎么做。
【音乐】阴谋诡计的背景音乐
【转场】淡出

【本集完】

下集预告：
贵族学校的第一天！
假千金的"贴心"照顾！
数学课上的惊人反转！
全校震惊：贫民窟女孩竟是天才学霸！""".format(date=datetime.now().strftime('%Y年%m月%d日'))
        
        return script
    
    def _true_heir_episode_3(self):
        """第3集：假千金的挑衅"""
        script = """《真千金是学霸》
第3集：假千金的挑衅
编剧：AI编剧
日期：{date}
==================================================

场景1：外景 圣英学院门口 晨
【全景】气派的贵族学校，各种豪车
【中景】林婉儿"热情"地拉着苏清月
林婉儿（大声）：清月妹妹，这就是圣英学院，和你们乡下学校很不一样吧？
【特写】周围同学投来异样的目光

场景2：内景 教室 日
【全景】豪华教室，智能黑板
【中景】林婉儿"好心"给苏清月安排座位
林婉儿：清月妹妹，你就坐这里吧，虽然位置偏了点...
【特写】角落里的破旧桌椅

场景3：内景 数学课堂 日
【全景】数学老师走进教室
老师：今天校长要求检验新同学的水平，随堂测试。
【中景】林婉儿和几个女生交换眼神，露出得意的笑
老师（在黑板上写题）：这道题，请新同学苏清月上来解答。
【特写】黑板上是一道极其复杂的微积分题

场景4：内景 数学课堂 日
【全景】全班同学等着看笑话
【中景】苏清月平静地走上讲台
【特写】她拿起粉笔，几乎没有思考就开始解题
苏清月（边写边解释）：这道题可以用拉格朗日中值定理...
【动作】粉笔在黑板上流畅书写

场景5：内景 数学课堂 日
【全景】全班鸦雀无声
【特写】老师震惊的表情
老师（激动）：完...完美！三种解法都正确！
【中景】林婉儿脸色铁青
【特写】苏清月放下粉笔，平静地回到座位
苏清月（内心独白）：学习，是我唯一能掌控的东西。
【转场】淡出

【本集完】

下集预告：
全国数学竞赛报名开始！
假千金的暗中阻挠！
神秘评委顾北辰登场！
苏清月能否突破重围，获得参赛资格？""".format(date=datetime.now().strftime('%Y年%m月%d日'))
        
        return script
    
    def _true_heir_general_episode(self, episode):
        """通用集数生成"""
        script = """《真千金是学霸》
第{episode}集
编剧：AI编剧
日期：{date}
==================================================

【本集剧情概要】
苏清月在豪门生活中逐渐适应，学霸实力不断展现。
假千金林婉儿的阴谋升级，但每次都被苏清月巧妙化解。
顾北辰对苏清月的关注越来越多，两人关系微妙发展。
苏清月参加全国数学竞赛，一路过关斩将。
家族内部对苏清月的态度开始转变。

【关键场景】
1. 竞赛准备：苏清月深夜备战
2. 冲突升级：林婉儿的新阴谋
3. 情感发展：顾北辰的暗中相助
4. 实力证明：竞赛中的精彩表现
5. 家族认可：苏父开始重视这个女儿

【商业元素】
- 爽点：学霸实力碾压对手
- 情感：主角的坚韧和善良
- 冲突：真假千金的明争暗斗
- 悬念：竞赛结果和感情发展

【时长】约3分钟

【本集完】

下集预告：
竞赛结果揭晓！
假千金真面目即将暴露！
顾北辰的表白时刻！
苏清月的命运将迎来重大转折！""".format(
    episode=episode,
    date=datetime.now().strftime('%Y年%m月%d日')
)
        
        return script
    
    def _generate_boss_love_script(self, episode=1):
        """生成《霸道总裁爱上我》剧本"""
        script = """《霸道总裁爱上我》
第{episode}集
编剧：AI编剧
日期：{date}
==================================================

【剧情概要】
普通女孩林小雨意外成为总裁陆霆骁的助理。
两人从误会到相知，从冲突到相爱。
商战阴谋，家族阻挠，感情考验。
最终有情人终成眷属。

【本集完】""".format(
    episode=episode,
    date=datetime.now().strftime('%Y年%m月%d日')
)
        
        return script
    
    def _generate_rebirth_script(self, episode=1):
        """生成《重生之逆袭人生》剧本"""
        script = """《重生之逆袭人生》
第{episode}集
编剧：AI编剧
日期：{date}
==================================================

【剧情概要】
女主重生回到十年前，利用前世记忆逆袭人生。
惩治渣男贱女，保护家人，发展事业。
从被欺负到成为人生赢家。

【本集完】""".format(
    episode=episode,
    date=datetime.now().strftime('%Y年%m月%d日')
)
        
        return script
    
    def _generate_campus_love_script(self, episode=1):
        """生成《校园纯爱日记》剧本"""
        script = """《校园纯爱日记》
第{episode}集
编剧：AI编剧
日期：{date}
==================================================

【剧情概要】
青涩的校园爱情，从相识到相知。
学业与爱情的平衡，友情与爱情的抉择。
纯真美好的青春故事。

【本集完】""".format(
    episode=episode,
    date=datetime.now().strftime('%Y年%m月%d日')
)
        
        return script
    
    def _generate_general_script(self, theme, episode=1):
        """生成通用剧本"""
        script = """《{theme}》
第{episode}集
编剧：AI编剧
日期：{date}
==================================================

【剧情概要】
这是一个关于{theme}的故事。
主角在逆境中成长，用智慧和勇气战胜困难。
经历爱情、友情、亲情的考验。
最终实现自我价值，收获幸福。

【本集重点】
1. 主角面临新挑战
2. 展现主角特质
3. 冲突升级
4. 情感发展
5. 留下悬念

【时长】约3分钟

【本集完】

下集预告：
新的危机即将来临！
主角将如何应对？
感情线会有新发展吗？
敬请期待下一集！""".format(
    theme=theme,
    episode=episode,
    date=datetime.now().strftime('%Y年%m月%d日')
)
        
        return script

def main():
    parser = argparse.ArgumentParser(description="短剧剧本快速生成与显示工具")
    parser.add_argument("--theme", required=True, help="剧本主题，如'真千金是学霸'")
    parser.add_argument("--episode", type=int, default=1, help="集数，默认第1集")
    parser.add_argument("--list", action="store_true", help="列出可用主题")
    
    args = parser.parse_args()
    
    generator = QuickScriptGenerator()
    
    if args.list:
        print("📚 可用剧本主题：")
        print("-" * 40)
        for theme in generator.templates.keys():
            print(f"  • {theme}")
        print("-" * 40)
        print("💡 提示：也可以使用自定义主题")
        return
    
    try:
        script = generator.generate_script(args.theme, args.episode)
        
        print("=" * 60)
        print(f"🎬 短剧剧本生成完成")
        print("=" * 60)
        print(script)
        print("=" * 60)
        print(f"📊 剧本信息：第{args.episode}集，{len(script.splitlines())}行")
        print(f"💡 提示：使用 --episode 参数生成其他集数")
        print("=" * 60)
    
    except Exception as e:
        print(f"❌ 错误：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()