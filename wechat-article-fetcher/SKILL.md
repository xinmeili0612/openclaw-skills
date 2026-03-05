---
name: wechat-article-fetcher
description: 微信公众号文章获取工具，支持获取微信公众号文章的完整内容。
---

# 微信公众号文章获取工具

## 功能特点
- 📄 获取微信公众号文章的完整内容
- 📝 提取文章标题、作者、发布时间、内容等信息
- 🎯 支持批量获取多个文章
- 📊 输出格式支持文本、Markdown、JSON等

## 使用方法

### 获取单篇文章内容
```bash
openclaw skill wechat-article-fetcher fetch "https://mp.weixin.qq.com/s/5exzrS24OSkVgzKb2Zs-dA"
```

### 获取单篇文章内容并保存为Markdown文件
```bash
openclaw skill wechat-article-fetcher fetch "https://mp.weixin.qq.com/s/5exzrS24OSkVgzKb2Zs-dA" --output markdown --file article.md
```

### 批量获取文章内容
```bash
openclaw skill wechat-article-fetcher batch --urls urls.txt --output json --file articles.json
```

## 配置说明
- 支持代理配置，解决反爬虫问题
- 支持自定义User-Agent
- 支持设置请求延迟，避免被封禁
- 支持设置最大重试次数

## 注意事项
- 微信公众号有反爬虫机制，建议使用代理或设置请求延迟
- 频繁请求可能会导致IP被封禁，请谨慎使用
- 仅用于学习和研究目的，请勿用于商业用途
- 请遵守微信公众号的使用条款和相关法律法规