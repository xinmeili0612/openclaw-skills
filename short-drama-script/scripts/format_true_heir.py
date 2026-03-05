#!/usr/bin/env python3
"""
《真千金是学霸》剧本格式化脚本
专门针对真千金学霸题材的剧本生成
"""

import json
from datetime import datetime

def generate_true_heir_script(outline_path, episode=1):
    """生成《真千金是学霸》剧本"""
    
    with open(outline_path, 'r', encoding='utf-8') as f:
        outline = json.load(f)
    
    # 获取本集信息
    episode_info = None
    if 'episode_outlines' in outline:
        for ep in outline['episode_outlines']:
            if ep['episode'] == episode:
                episode_info = ep
                break
    
    if not episode_info:
        episode_info = {
            'title': f'第{episode}集',
            'key_events': ['剧情发展', '冲突升级', '情感推进'],
            'commercial_elements': ['爽点', '情感', '悬念']
        }
    
    # 获取角色信息
    characters = {}
    for char in outline.get('characters', []):
        characters[char['role']] = char
    
    # 生成剧本
    script_lines = []
    
    # 剧本头部
    script_lines.append(f"《{outline.get('title', '真千金是学霸')}》")
    script_lines.append(f"第{episode}集：{episode_info.get('title', '')}")
    script_lines.append(f"编剧：{outline.get('author', 'AI编剧')}")
    script_lines.append(f"日期：{datetime.now().strftime('%Y年%m月%d日')}")
    script_lines.append("=" * 50)
    script_lines.append("")
    
    # 根据集数生成不同内容
    if episode == 1:
        script_lines.extend(_generate_episode_1(outline, characters))
    elif episode == 2:
        script_lines.extend(_generate_episode_2(outline, characters))
    elif episode == 3:
        script_lines.extend(_generate_episode_3(outline, characters))
    elif episode == 4:
        script_lines.extend(_generate_episode_4(outline, characters))
    elif episode == 5:
        script_lines.extend(_generate_episode_5(outline, characters))
    else:
        script_lines.extend(_generate_general_episode(outline, characters, episode))
    
    script_lines.append("")
    script_lines.append("【本集完】")
    script_lines.append("")
    
    # 下集预告
    next_preview = _generate_preview(outline, episode)
    if next_preview:
        script_lines.append("下集预告：")
        script_lines.append(next_preview)
    
    return "\n".join(script_lines)

def _generate_episode_1(outline, characters):
    """生成第1集：贫民窟的学霸"""
    lines = []
    
    heroine = characters.get('女主角，真千金学霸', {})
    mother = characters.get('母亲，矛盾角色', {})
    
    lines.append("场景1：外景 贫民窟街道 晨")
    lines.append("【全景】破旧的街道，低矮的房屋，清晨的阳光勉强穿透雾气")
    lines.append("【中景】苏清月（18岁，清秀但衣着朴素）背着旧书包走出家门")
    lines.append("【特写】她手中拿着一本破旧的数学竞赛题集，边走边看")
    lines.append("")
    
    lines.append("场景2：内景 苏清月家 日")
    lines.append("【全景】狭小但整洁的房间，墙上贴满各种奖状和证书")
    lines.append("【近景】苏清月照顾生病的母亲喝药")
    lines.append(f"苏清月（温柔）：妈，药喝了，我考完试就回来。")
    lines.append(f"苏母（虚弱但欣慰）：月月，别太辛苦...")
    lines.append("【特写】苏清月看着母亲，眼神坚定")
    lines.append("")
    
    lines.append("场景3：内景 学校教室 日")
    lines.append("【全景】普通中学教室，苏清月坐在最后一排")
    lines.append("【中景】数学老师在黑板上写下一道奥数难题")
    lines.append("老师：这道题是去年全国竞赛的压轴题，有同学会解吗？")
    lines.append("【特写】全班沉默，苏清月举手")
    lines.append("苏清月（平静）：老师，我可以试试。")
    lines.append("【动作】她走上讲台，流畅地写下解题步骤")
    lines.append("【音乐】励志向上的背景音乐")
    lines.append("")
    
    lines.append("场景4：外景 学校门口 傍晚")
    lines.append("【全景】苏清月走出校门，手里拿着奖学金通知书")
    lines.append("【中景】她看着通知书，露出淡淡的微笑")
    lines.append("苏清月（内心独白）：有了这笔奖学金，妈的药费就有着落了...")
    lines.append("【特写】通知书上写着：'贵族学校特招录取'")
    lines.append("")
    
    lines.append("场景5：外景 贫民窟街道 傍晚")
    lines.append("【全景】苏清月回到家门口，看到一辆黑色豪车停在那里")
    lines.append("【中景】车上走下一位穿着西装的中年男人")
    lines.append("男人（严肃）：请问是苏清月小姐吗？")
    lines.append("苏清月（疑惑）：我是，请问您是？")
    lines.append("男人：我是苏氏集团的律师，有些事情需要和您谈谈。")
    lines.append("【特写】苏清月惊讶的表情")
    lines.append("【音乐】悬念紧张的音乐起")
    lines.append("【转场】淡出")
    
    return lines

def _generate_episode_2(outline, characters):
    """生成第2集：豪门认亲"""
    lines = []
    
    heroine = characters.get('女主角，真千金学霸', {})
    father = characters.get('父亲，理性角色', {})
    mother = characters.get('母亲，矛盾角色', {})
    fake_heir = characters.get('反派女配，假千金', {})
    
    lines.append("场景1：外景 苏家豪宅大门 日")
    lines.append("【全景】气派的欧式别墅，豪华花园，与贫民窟形成鲜明对比")
    lines.append("【中景】苏清月从律师车上下来，看着眼前的豪宅")
    lines.append("苏清月（内心独白）：这里...就是我的亲生父母家？")
    lines.append("【特写】她握紧手中的旧书包，眼神复杂")
    lines.append("")
    
    lines.append("场景2：内景 苏家客厅 日")
    lines.append("【全景】豪华的客厅，水晶吊灯，真皮沙发")
    lines.append("【中景】苏父（50岁，威严）和苏母（45岁，优雅但冷淡）坐在沙发上")
    lines.append("苏父（审视地看着苏清月）：坐吧。")
    lines.append("苏清月（礼貌但疏离）：谢谢。")
    lines.append("【特写】苏母看着苏清月朴素的衣着，微微皱眉")
    lines.append("")
    
    lines.append("场景3：内景 苏家客厅 日")
    lines.append("【中景】林婉儿（18岁，打扮精致）从楼梯上走下来")
    lines.append(f"林婉儿（甜美微笑）：这就是清月妹妹吧？欢迎回家。")
    lines.append("【特写】林婉儿眼中一闪而过的嫉妒")
    lines.append("苏清月（平静）：你好。")
    lines.append("苏母（对林婉儿温柔）：婉儿，来妈妈这边坐。")
    lines.append("【对比镜头】苏母对两个女儿的不同态度")
    lines.append("")
    
    lines.append("场景4：内景 苏清月房间 夜")
    lines.append("【全景】别墅里最小最偏僻的房间，虽然干净但简陋")
    lines.append("【中景】苏清月整理着从贫民窟带来的少量物品")
    lines.append("苏清月（内心独白）：这里很大，很豪华，但...很冷。")
    lines.append("【特写】她拿出和养母的合影，轻轻抚摸")
    lines.append("【闪回】贫民窟小屋里，养母温柔的笑容")
    lines.append("")
    
    lines.append("场景5：内景 林婉儿房间 夜")
    lines.append("【全景】豪华公主房，粉色系装修，满柜名牌")
    lines.append("【特写】林婉儿撕碎苏清月的照片")
    lines.append(f"林婉儿（阴冷）：苏清月...你为什么要回来？")
    lines.append("【动作】她拿起手机，拨通电话")
    lines.append("林婉儿：王姨，明天学校那边...你知道该怎么做。")
    lines.append("【音乐】阴谋诡计的背景音乐")
    lines.append("【转场】淡出")
    
    return lines

def _generate_episode_3(outline, characters):
    """生成第3集：假千金的挑衅"""
    lines = []
    
    heroine = characters.get('女主角，真千金学霸', {})
    fake_heir = characters.get('反派女配，假千金', {})
    
    lines.append("场景1：外景 贵族学校门口 晨")
    lines.append("【全景】气派的学校大门，各种豪车接送学生")
    lines.append("【中景】林婉儿"热情"地拉着苏清月介绍学校")
    lines.append(f"林婉儿（大声）：清月妹妹，这就是我们学校，和你们乡下学校很不一样吧？")
    lines.append("【特写】周围同学投来异样的目光")
    lines.append("苏清月（平静）：学校就是学习的地方，没什么不同。")
    lines.append("")
    
    lines.append("场景2：内景 教室 日")
    lines.append("【全景】豪华教室，每个学生都有独立桌椅")
    lines.append("【中景】林婉儿"好心"给苏清月安排座位")
    lines.append(f"林婉儿：清月妹妹，你就坐这里吧，虽然位置偏了点...")
    lines.append("【特写】角落里的破旧桌椅，与其他座位形成对比")
    lines.append("苏清月（淡然）：谢谢，这里很好。")
    lines.append("")
    
    lines.append("场景3：内景 数学课堂 日")
    lines.append("【全景】数学老师走进教室，神情严肃")
    lines.append("老师：今天我们来个随堂测试，检验一下新同学的水平。")
    lines.append("【中景】林婉儿和几个女生交换眼神，露出得意的笑")
    lines.append("老师（在黑板上写题）：这道题，请新同学苏清月上来解答。")
    lines.append("【特写】黑板上是一道极其复杂的微积分题")
    lines.append("")
    
    lines.append("场景4：内景 数学课堂 日")
    lines.append("【全景】全班同学等着看笑话")
    lines.append("【中景】苏清月平静地走上讲台")
    lines.append("【特写】她拿起粉笔，几乎没有思考就开始解题")
    lines.append("苏清月（边写边解释）：这道题可以用拉格朗日中值定理...")
    lines.append("【动作】粉笔在黑板上流畅书写，步骤清晰严谨")
    lines.append("【音乐】从紧张到震撼的转变")
    lines.append("")
    
    lines.append("场景5：内景 数学课堂 日")
    lines.append("【全景】全班鸦雀无声")
    lines.append("【特写】老师震惊的表情")
    lines.append("老师（激动）：完...完美！三种解法都正确！")
    lines.append("【中景】林婉儿脸色铁青")
    lines.append("【特写】苏清月放下粉笔，平静地回到座位")
    lines.append("苏清月（内心独白）：学习，是我唯一能掌控的东西。")
    lines.append("【转场】淡出")
    
    return lines

def _generate_episode_4(outline, characters):
    """生成第4集：第一次交锋"""
    lines = []
    
    heroine = characters.get('女主角，真千金学霸', {})
    fake_heir = characters.get('反派女配，假千金', {})
    hero = characters.get('男主角，豪门继承人', {})
    
    lines.append("场景1：内景 学校餐厅 日")
    lines.append("【全景】豪华的学生餐厅，林婉儿和她的"闺蜜团"坐在一起")
    lines.append("【中景】苏清月独自坐在角落吃饭")
    lines.append(f"女生A（故意大声）：婉儿，听说你那个妹妹昨天在数学课出风头了？")
    lines.append(f"林婉儿（假装无奈）：清月妹妹可能想快点融入吧，毕竟...环境差异大。")
    lines.append("【特写】苏清月仿佛没听见，专注地看着手中的书")
    lines.append("")
    
    lines.append("场景2：内景 图书馆 日")
    lines.append("【全景】安静的图书馆，苏清月在角落学习")
    lines.append("【中景】顾北辰（22岁，帅气高冷）走进图书馆")
    lines.append("【特写】顾北辰注意到专注学习的苏清月")
    lines.append("顾北辰（内心独白）：那个女孩...有点意思。）")
    lines.append("【动作】他在不远处坐下，假装看书，实际在观察苏清月")
    lines.append("")
    
    lines.append("场景3：内景 学校公告栏 日")
    lines.append("【全景】学生们围在公告栏前")
    lines.append("【中景】公告：全国高中生数学竞赛选拔开始")
    lines.append(f"林婉儿（自信地）：这次竞赛，我一定要拿冠军！")
    lines.append("女生B：婉儿肯定没问题，你可是我们学校的数学天才！")
    lines.append("【特写】林婉儿看到走过来的苏清月，故意提高音量")
    lines.append(f"林婉儿：清月妹妹，你要参加吗？这种竞赛和普通考试可不一样哦。")
    lines.append("")
    
    lines.append("场景4：内景 图书馆 傍晚")
    lines.append("【全景】苏清月在报名表上签字")
    lines.append("【特写】报名表上工整的字迹：苏清月")
    lines.append("苏清月（内心独白）：竞赛...是证明自己的机会。）")
    lines.append("【中景】顾北辰走过来，看到报名表")
    lines.append("顾北辰（淡淡）：你也参加数学竞赛？")
    lines.append("苏清月（抬头）：是的。")
    lines.append("顾北辰：我是这次竞赛的赞助商代表，期待你的表现。")
    lines.append("【特写】两人对视，空气中微妙的气氛")
    lines.append("")
    
    lines.append("场景5：内景 苏家客厅 夜")
    lines.append("【全景】苏清月告诉家人要参加竞赛")
    lines.append("苏母（皱眉）：清月，你刚转学，不要好高骛远。")
    lines.append(f"林婉儿（假装关心）：妈，清月妹妹可能想证明自己吧，虽然...有点难。")
    lines.append("苏父（看了苏清月一眼）：参加可以，别给苏家丢脸。")
    lines.append("【特写】苏清月握紧拳头，眼神坚定")
    lines.append("苏清月：我会努力的。")
    lines.append("【音乐】励志奋斗的音乐")
    lines.append("【转场】淡出")
    
    return lines

def _generate_episode_5(outline, characters):
    """生成第5集：竞赛开始"""
    lines = []
    
    heroine = characters.get('女主角，真千金学霸', {})
    fake_heir = characters.get('反派女配，假千金', {})
    hero = characters.get('男主角，豪门继承人', {})
    
    lines.append("场景1：外景 竞赛场地 日")
    lines.append("【全景】豪华的会议中心，各校精英汇聚")
    lines.append("【中景】苏清月穿着校服，在一群打扮精致的学生中显得朴素")
    lines.append(f"林婉儿（带着闺蜜团走过来）：清月妹妹，紧张吗？第一次参加这种场合吧？")
    lines.append("苏清月（平静）：还好。")
    lines.append("女生C（小声嘲笑）：穿成这样来比赛，真是丢人。")
    lines.append("")
    
    lines.append("场景2：内景 竞赛大厅 日")
    lines.append("【全景】庄严的竞赛现场，评委席上坐着各界精英")
    lines.append("【特写】顾北辰坐在评委席，目光扫过参赛者")
    lines.append("【中景】主持人宣布比赛规则")
    lines.append("主持人：第一轮，笔试，90分钟，现在开始！")
    lines.append("【动作】所有参赛者开始答题")
    lines.append("")
    
    lines.append("场景3：内景 竞赛大厅 日")
    lines.append("【特写】苏清月专注答题，笔尖飞快")
    lines.append("【对比镜头】林婉儿皱眉思考，有些题目让她卡住")
    lines.append("【中景】时间过去60分钟，苏清月已经答完")
    lines.append("【动作】她举手示意交卷")
    lines.append("监考老师（惊讶）：同学，你确定要提前交卷？")
    lines.append("苏清月：确定。")
    lines.append("")
    
    lines.append("场景4：内景 休息区 日")
    lines.append("【全景】提前交卷的苏清月在休息区看书")
    lines.append("【中景】顾北辰走过来")
    lines.append("顾北辰：这么快就交卷，很有自信？")
    lines.append("苏清月（抬头）：题目不难。")
    lines.append("顾北辰（挑眉）：哦？最后一题可是去年的国际奥赛题。")
    lines.append("苏清月：用柯西不等式和均值不等式可以简化。")
    lines.append("【特写】顾北辰眼中闪过欣赏")
    lines.append("")
    
    lines.append("场景5：内景 竞赛大厅 日")
    lines.append("【全景】笔试结束，学生们陆续走出考场")
    lines.append("【