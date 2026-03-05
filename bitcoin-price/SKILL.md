---
name: bitcoin-price
description: 实时获取比特币价格信息，支持多种货币单位和数据源。
---

# 比特币实时价格工具

## 功能特点
- 📈 实时获取比特币价格
- 💰 支持多种货币单位：USD、CNY、EUR、JPY等
- 📊 提供价格走势图数据
- 📉 显示24小时涨跌幅
- 🔄 支持多种数据源：CoinGecko、Binance、Coinbase等

## 使用方法

### 获取比特币实时价格（默认USD）
```bash
openclaw skill bitcoin-price get
```

### 获取人民币价格
```bash
openclaw skill bitcoin-price get --currency CNY
```

### 获取详细信息（包括涨跌幅、走势图）
```bash
openclaw skill bitcoin-price detail
```

### 使用Binance数据源
```bash
openclaw skill bitcoin-price get --source binance
```

## 配置说明
- 默认数据源：CoinGecko
- 默认货币单位：USD
- 支持自定义数据源和货币单位
- 可以配置API密钥用于私有数据源

## 注意事项
- 价格数据来自公开API，可能存在延迟
- 不同数据源价格可能略有差异
- 部分数据源需要API密钥
- 实时价格可能随时波动