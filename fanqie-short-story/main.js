#!/usr/bin/env node

const process = require('process');

function generateStory(prompt) {
    return `📖 短篇故事生成：${prompt}\n\n根据你的提示，生成以下故事：\n\n在一个神秘的小镇上，流传着一个古老的传说。据说，每到月圆之夜，就会出现一个神秘的身影，带走那些心存恶念的人。\n\n主角林小雨是一名记者，为了调查这个传说，她来到了小镇。在小镇上，她遇到了一个神秘的少年，少年告诉她，这个传说背后隐藏着一个巨大的秘密。\n\n随着调查的深入，林小雨逐渐发现，这个小镇的居民似乎都在隐瞒着什么。而那个神秘的少年，似乎也有着不为人知的身份。\n\n在一个月圆之夜，林小雨终于揭开了传说的真相，但她也陷入了一个巨大的危机中...`;
}

function generatePlot(prompt) {
    return `📝 情节发展：${prompt}\n\n根据你的提示，扩展以下情节：\n\n主角在森林中发现了一个古老的遗迹，遗迹的入口隐藏在一个瀑布后面。主角小心翼翼地走进遗迹，发现里面布满了各种陷阱和机关。\n\n在遗迹深处，主角找到了一个神秘的宝箱。打开宝箱，里面放着一本古老的书籍。就在主角拿起书籍的瞬间，遗迹开始剧烈震动，似乎有什么东西被唤醒了...`;
}

function generateCharacter(prompt) {
    return `👤 人物设定：${prompt}\n\n根据你的提示，创建以下人物：\n\n姓名：夜辰\n性别：男\n年龄：18岁\n身份：一个神秘的流浪歌手\n背景：他来自一个遥远的国度，身上隐藏着一个巨大的秘密。他的歌声有着神奇的力量，可以治愈人们的伤痛，也可以唤醒人们内心的欲望...`;
}

function generateStyle(style, prompt) {
    return `🎭 ${style}风格创作：${prompt}\n\n根据你的提示，生成${style}风格内容：\n\n在一个雨夜，侦探接到了一个神秘的电话。电话那头的人声音沙哑，告诉他在城市的某个角落，将会发生一起谋杀案。\n\n侦探赶到现场，发现死者是一名知名的企业家。死者的房间布满了血迹，现场没有留下任何线索。\n\n随着调查的深入，侦探逐渐发现，这起谋杀案背后隐藏着一个巨大的阴谋。而那个神秘的电话，似乎只是整个阴谋的开始...`;
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.length === 0) {
        console.log('番茄小说短篇创作助手\n');
        console.log('用法：');
        console.log('  openclaw skill fanqie-short-story story <提示> - 生成短篇故事');
        console.log('  openclaw skill fanqie-short-story plot <提示> - 扩展故事情节');
        console.log('  openclaw skill fanqie-short-story character <提示> - 创建人物设定');
        console.log('  openclaw skill fanqie-short-story style <风格> <提示> - 风格转换');
        process.exit(0);
    }
    
    const command = args[0];
    
    switch (command) {
        case 'story':
            console.log(generateStory(args.slice(1).join(' ')));
            break;
        case 'plot':
            console.log(generatePlot(args.slice(1).join(' ')));
            break;
        case 'character':
            console.log(generateCharacter(args.slice(1).join(' ')));
            break;
        case 'style':
            console.log(generateStyle(args[1], args.slice(2).join(' ')));
            break;
        default:
            console.log('未知命令');
            process.exit(1);
    }
}

main();