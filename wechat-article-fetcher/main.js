#!/usr/bin/env node

const process = require('process');
const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

async function fetchArticle(url, options = {}) {
    try {
        // 设置请求配置
        const config = {
            headers: {
                'User-Agent': options.userAgent || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'Referer': 'https://mp.weixin.qq.com/',
            },
            proxy: options.proxy || null,
            timeout: options.timeout || 10000,
        };

        // 发送请求
        const response = await axios.get(url, config);
        const html = response.data;

        // 使用cheerio解析HTML
        const $ = cheerio.load(html);

        // 提取文章信息
        const article = {
            title: $('h2.rich_media_title').text().trim(),
            author: $('a.rich_media_meta.nickname').text().trim(),
            publishTime: $('em.rich_media_meta[id="publish_time"]').text().trim(),
            content: $('div.rich_media_content').html(),
            textContent: $('div.rich_media_content').text().trim(),
        };

        return article;
    } catch (error) {
        console.error('获取文章失败：', error.message);
        return null;
    }
}

function saveToFile(content, filePath, format = 'text') {
    try {
        let data;
        if (format === 'json') {
            data = JSON.stringify(content, null, 2);
        } else if (format === 'markdown') {
            data = `# ${content.title}\n\n作者：${content.author}\n发布时间：${content.publishTime}\n\n${content.textContent}`;
        } else {
            data = content.textContent;
        }

        fs.writeFileSync(filePath, data, 'utf8');
        console.log(`文章内容已保存到文件：${filePath}`);
    } catch (error) {
        console.error('保存文件失败：', error.message);
    }
}

async function main() {
    const args = process.argv.slice(2);

    if (args.length === 0) {
        console.log('微信公众号文章获取工具\n');
        console.log('用法：');
        console.log('  openclaw skill wechat-article-fetcher fetch <URL> [--output <format>] [--file <path>] - 获取单篇文章内容');
        console.log('  openclaw skill wechat-article-fetcher batch --urls <file> [--output <format>] [--file <path>] - 批量获取文章内容');
        console.log('  openclaw skill wechat-article-fetcher help - 显示帮助信息');
        process.exit(0);
    }

    const command = args[0];

    switch (command) {
        case 'fetch':
            if (args.length < 2) {
                console.error('错误：请提供微信公众号文章的URL');
                process.exit(1);
            }

            const url = args[1];
            const options = {
                output: 'text',
                file: null,
            };

            // 解析命令行参数
            for (let i = 2; i < args.length; i++) {
                if (args[i] === '--output') {
                    options.output = args[++i];
                } else if (args[i] === '--file') {
                    options.file = args[++i];
                }
            }

            // 获取文章内容
            const article = await fetchArticle(url);
            if (article) {
                console.log(`标题：${article.title}`);
                console.log(`作者：${article.author}`);
                console.log(`发布时间：${article.publishTime}`);
                console.log('\n文章内容：');
                console.log(article.textContent.substring(0, 500) + '...'); // 只显示前500个字符

                // 如果指定了文件路径，保存文章内容
                if (options.file) {
                    saveToFile(article, options.file, options.output);
                }
            }
            break;

        case 'batch':
            // 批量获取文章内容
            console.log('批量获取文章内容功能正在开发中，敬请期待...');
            break;

        case 'help':
            console.log('微信公众号文章获取工具\n');
            console.log('用法：');
            console.log('  openclaw skill wechat-article-fetcher fetch <URL> [--output <format>] [--file <path>] - 获取单篇文章内容');
            console.log('  openclaw skill wechat-article-fetcher batch --urls <file> [--output <format>] [--file <path>] - 批量获取文章内容');
            console.log('  openclaw skill wechat-article-fetcher help - 显示帮助信息');
            break;

        default:
            console.error('未知命令：', command);
            process.exit(1);
    }
}

// 安装依赖
function installDependencies() {
    const exec = require('child_process').execSync;
    try {
        console.log('正在安装依赖...');
        exec('npm install axios cheerio', { stdio: 'inherit', cwd: __dirname });
        console.log('依赖安装完成！');
    } catch (error) {
        console.error('依赖安装失败：', error.message);
        process.exit(1);
    }
}

// 如果是首次运行，安装依赖
if (process.argv.includes('--install')) {
    installDependencies();
} else {
    main();
}
