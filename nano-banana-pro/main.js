#!/usr/bin/env node

const process = require('process');
const fs = require('fs');
const replicate = require('replicate');

async function generateImage(prompt, aspectRatio = '16:9', outputPath = 'output.png') {
    try {
        // 初始化Replicate客户端
        const client = new replicate({ token: process.env.REPLICATE_API_TOKEN });

        // 转换比例参数
        const ratioMap = {
            '16:9': '16:9',
            '4:3': '4:3',
            '1:1': '1:1',
        };

        const modelInput = {
            prompt: prompt,
            aspect_ratio: ratioMap[aspectRatio],
            num_inference_steps: 50,
            guidance_scale: 7.5,
        };

        // 调用模型生成图片
        console.log('正在生成图片，请稍候...');
        const output = await client.run(
            'google/nano-banana-pro',
            {
                input: {
                    prompt: prompt
                }
            }
        );

        // 下载图片
        console.log('图片生成成功，正在下载...');
        console.log('输出结果：', output);
        if (output.images && output.images[0]) {
            const imageResponse = await fetch(output.images[0]);
            const imageBuffer = await imageResponse.arrayBuffer();
            fs.writeFileSync(outputPath, Buffer.from(imageBuffer));
        } else if (output.url) {
            const imageResponse = await fetch(output.url);
            const imageBuffer = await imageResponse.arrayBuffer();
            fs.writeFileSync(outputPath, Buffer.from(imageBuffer));
        } else {
            throw new Error('无法从输出结果中提取图片URL');
        }

        console.log(`图片已保存到文件：${outputPath}`);
    } catch (error) {
        console.error('图片生成失败：', error.message);
        process.exit(1);
    }
}

function main() {
    const args = process.argv.slice(2);

    if (args.length === 0 || args[0] === 'help') {
        console.log('Google Nano Banana Pro 图片生成工具\n');
        console.log('用法：');
        console.log('  openclaw skill nano-banana-pro generate <prompt> [--ratio <ratio>] [--output <path>] - 生成图片');
        console.log('  openclaw skill nano-banana-pro help - 显示帮助信息');
        console.log('');
        console.log('示例：');
        console.log('  openclaw skill nano-banana-pro generate "AI自动化工作流程图，科技感蓝色调，中文标注" --ratio "16:9" --output "cover.png"');
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