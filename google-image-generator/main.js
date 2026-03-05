#!/usr/bin/env node

const process = require('process');
const fs = require('fs');
const axios = require('axios');

async function generateImage(prompt, aspectRatio = '16:9', outputPath = 'output.png') {
    try {
        // 获取Google API密钥
        const apiKey = process.env.GOOGLE_API_KEY;
        if (!apiKey) {
            throw new Error('GOOGLE_API_KEY环境变量未配置');
        }

        // 转换比例参数
        const ratioMap = {
            '16:9': '16:9',
            '4:3': '4:3',
            '1:1': '1:1',
        };

        // 调用Google Image Generation API
        console.log('正在生成图片，请稍候...');
        const response = await axios.post(
            `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-001:generateContent?key=${apiKey}`,
            {
                contents: [
                    {
                        parts: [
                            {
                                text: prompt
                            }
                        ]
                    }
                ],
                generationConfig: {
                    aspectRatio: ratioMap[aspectRatio],
                    responseMimeType: 'image/png'
                }
            }
        );

        // 解析图片数据
        const imageData = response.data.candidates[0].content.parts[0].inlineData.data;
        const imageBuffer = Buffer.from(imageData, 'base64');

        // 保存图片
        fs.writeFileSync(outputPath, imageBuffer);
        console.log(`图片已保存到文件：${outputPath}`);
    } catch (error) {
        console.error('图片生成失败：', error.response ? error.response.data : error.message);
        process.exit(1);
    }
}

function main() {
    const args = process.argv.slice(2);

    if (args.length === 0 || args[0] === 'help') {
        console.log('Google图片生成工具\n');
        console.log('用法：');
        console.log('  openclaw skill google-image-generator generate <prompt> [--ratio <ratio>] [--output <path>] - 生成图片');
        console.log('  openclaw skill google-image-generator help - 显示帮助信息');
        console.log('');
        console.log('示例：');
        console.log('  openclaw skill google-image-generator generate "AI自动化工作流程图，科技感蓝色调，简洁扁平设计，中文标注" --ratio "16:9" --output "cover.png"');
        process.exit(0);
    }

    const command = args[0];

    switch (command) {
        case 'generate':
            if (args.length < 2) {
                console.error('错误：请提供图片描述prompt');
                process.exit(1);
            }

            const prompt = args[1];
            const options = {
                ratio: '16:9',
                output: 'output.png',
            };

            // 解析命令行参数
            for (let i = 2; i < args.length; i++) {
                if (args[i] === '--ratio') {
                    options.ratio = args[++i];
                } else if (args[i] === '--output') {
                    options.output = args[++i];
                }
            }

            // 生成图片
            generateImage(prompt, options.ratio, options.output);
            break;

        default:
            console.error('未知命令：', command);
            process.exit(1);
    }
}

main();