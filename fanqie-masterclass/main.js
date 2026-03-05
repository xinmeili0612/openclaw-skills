#!/usr/bin/env node

const process = require('process');

function getChapter(chapterNum) {
    const chapters = {
        '1': `📚 第一章：番茄小说平台分析\n\n1. 用户群体分析：\n   - 番茄小说的用户主要集中在18-35岁\n   - 以女性读者为主，占比超过60%\n   - 读者喜欢轻松、爽文、甜宠等类型\n\n2. 爆款小说特点：\n   - 节奏快，黄金三章必须有钩子\n   - 主角光环强，逆袭打脸情节多\n   - 情感冲突明显，满足读者爽点\n\n3. 题材选择：\n   - 优先选择当前热门题材（如：赘婿、神医、穿越、修仙等）\n   - 结合自身兴趣和擅长领域\n   - 创新题材更容易脱颖而出`,
        '2': `📚 第二章：小说创作基础\n\n1. 人物塑造：\n   - 主角要有明确的目标和驱动力\n   - 配角要具有独特的性格和作用\n   - 反派要足够坏，才能衬托主角的好\n\n2. 情节构建：\n   - 要有清晰的故事主线和支线\n   - 设置合理的冲突和转折点\n   - 情节要符合逻辑，避免漏洞\n\n3. 环境描写：\n   - 环境要为情节和人物服务\n   - 细节描写要生动，让读者有代入感\n   - 注意场景转换的自然流畅`,
        '3': `📚 第三章：爆款技巧实战\n\n1. 黄金三章技巧：\n   - 第一章必须让主角陷入困境\n   - 第二章要展示主角的特殊能力或机遇\n   - 第三章要让主角开始逆袭\n\n2. 悬念设置：\n   - 每章结尾要留下钩子\n   - 适当设置伏笔，后期回收\n   - 利用读者好奇心推动情节发展\n\n3. 节奏控制：\n   - 张弛有度，避免拖沓\n   - 重要情节要详细描写\n   - 过渡情节要简洁明了`,
        '4': `📚 第四章：投稿和运营\n\n1. 投稿流程：\n   - 注册番茄小说作者账号\n   - 创建作品，填写标题、简介、标签\n   - 上传正文，等待审核\n\n2. 作品优化：\n   - 标题要吸引人，包含关键词\n   - 简介要突出亮点，留下悬念\n   - 标签要准确，提高曝光率\n\n3. 运营推广：\n   - 与读者互动，回复评论\n   - 参与平台活动，增加曝光\n   - 利用社交媒体推广作品`
    };
    
    return chapters[chapterNum] || `📚 第${chapterNum}章内容正在更新中，敬请期待...`;
}

function getTechnique(techniqueName) {
    const techniques = {
        '黄金三章': `🎯 黄金三章写作技巧\n\n1. 第一章：\n   - 开头500字必须出现冲突\n   - 主角要遭遇困境或危机\n   - 留下悬念，吸引读者继续阅读\n\n2. 第二章：\n   - 主角获得特殊能力或机遇\n   - 展示主角的变化和成长\n   - 为主角的逆袭做铺垫\n\n3. 第三章：\n   - 主角开始反击，打脸反派\n   - 展示主角的实力和潜力\n   - 让读者获得爽感`,
        '悬念设置': `🎯 悬念设置技巧\n\n1. 常见悬念类型：\n   - 身世悬念：主角的身世成谜\n   - 能力悬念：主角的能力来源不明\n   - 剧情悬念：未来的发展方向未知\n\n2. 设置方法：\n   - 先提出问题，再慢慢解答\n   - 适当隐藏关键信息\n   - 利用细节暗示真相\n\n3. 注意事项：\n   - 悬念要合理，不能为了悬念而悬念\n   - 要及时回收伏笔，避免烂尾\n   - 悬念的难度要适中，让读者有解谜的乐趣`,
        '节奏控制': `🎯 节奏控制技巧\n\n1. 快节奏场景：\n   - 战斗场面、逆袭打脸\n   - 用短句和动词，增强紧张感\n   - 减少不必要的描写\n\n2. 慢节奏场景：\n   - 情感交流、内心独白\n   - 用长句和形容词，营造氛围\n   - 注重细节描写，增强代入感\n\n3. 节奏转换：\n   - 快慢结合，避免单调\n   - 重要情节前可以适当放缓节奏\n   - 高潮过后需要给读者喘息的空间`
    };
    
    return techniques[techniqueName] || `🎯 "${techniqueName}"技巧正在更新中，敬请期待...`;
}

function getAdvice(question) {
    const advice = {
        '如何塑造反派角色': `💡 塑造反派角色的建议\n\n1. 反派要有明确的动机\n   - 不能单纯为了坏而坏\n   - 动机要合理，符合逻辑\n\n2. 反派要有实力\n   - 要能给主角造成威胁\n   - 实力要与主角相当或更强\n\n3. 反派要有魅力\n   - 可以有自己的原则和底线\n   - 适当展示反派的闪光点\n\n4. 反派的结局\n   - 要符合其行为逻辑\n   - 可以是被打败、洗白或自我救赎`,
        '如何写好爽文': `💡 写好爽文的建议\n\n1. 爽点要密集\n   - 每章至少有一个爽点\n   - 爽点要层层递进\n\n2. 主角要强大\n   - 主角要有特殊能力或机遇\n   - 主角的成长速度要快\n\n3. 打脸要彻底\n   - 反派要嚣张跋扈\n   - 打脸情节要解气\n\n4. 情感要到位\n   - 可以加入甜宠、友情等元素\n   - 满足读者的情感需求`,
        '如何提高写作速度': `💡 提高写作速度的建议\n\n1. 提前做好大纲\n   - 明确故事主线和支线\n   - 规划好各章节内容\n\n2. 固定写作时间\n   - 养成良好的写作习惯\n   - 提高写作效率\n\n3. 减少修改次数\n   - 先完成再完美\n   - 避免边写边改\n\n4. 学会利用工具\n   - 使用写作软件提高效率\n   - 可以适当使用语音输入`
    };
    
    // 匹配关键词
    for (const key in advice) {
        if (question.includes(key)) {
            return advice[key];
        }
    }
    
    return `💡 对于"${question}"这个问题，建议从以下几个方面入手：\n\n1. 明确核心需求\n2. 收集相关素材\n3. 制定写作计划\n4. 逐步完善内容\n\n如果需要更具体的建议，请提供更多细节！`;
}

function getSubmitGuide() {
    return `📝 番茄小说投稿指南\n\n1. 注册作者账号：\n   - 下载番茄小说APP\n   - 点击"我的" -> "成为作家"\n   - 按照提示完成注册\n\n2. 创建作品：\n   - 选择作品类型和题材\n   - 填写标题、简介、标签\n   - 上传作品封面\n\n3. 投稿要求：\n   - 原创作品，不得抄袭\n   - 内容健康，符合平台规定\n   - 章节字数不少于1000字\n\n4. 审核流程：\n   - 提交后一般在24小时内审核\n   - 审核通过后作品即可发布\n   - 审核不通过会给出具体原因\n\n5. 注意事项：\n   - 标题要吸引人，包含关键词\n   - 简介要突出亮点，留下悬念\n   - 标签要准确，提高曝光率`;
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.length === 0) {
        console.log('番茄小说大师课\n');
        console.log('用法：');
        console.log('  openclaw skill fanqie-masterclass chapter <章节号> - 查看课程章节内容');
        console.log('  openclaw skill fanqie-masterclass technique <技巧名称> - 学习爆款写作技巧');
        console.log('  openclaw skill fanqie-masterclass advice <问题> - 获取写作建议');
        console.log('  openclaw skill fanqie-masterclass submit - 查看投稿指南');
        process.exit(0);
    }
    
    const command = args[0];
    
    switch (command) {
        case 'chapter':
            console.log(getChapter(args[1]));
            break;
        case 'technique':
            console.log(getTechnique(args.slice(1).join(' ')));
            break;
        case 'advice':
            console.log(getAdvice(args.slice(1).join(' ')));
            break;
        case 'submit':
            console.log(getSubmitGuide());
            break;
        default:
            console.log('未知命令');
            process.exit(1);
    }
}

main();