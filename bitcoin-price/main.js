#!/usr/bin/env node

const process = require('process');
const axios = require('axios');

async function getBitcoinPrice(currency = 'USD', source = 'coingecko') {
    try {
        let price = 0;
        let change24h = 0;
        let volume24h = 0;

        if (source === 'coingecko') {
            // 使用CoinGecko API
            const response = await axios.get(`https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=${currency.toLowerCase()}&include_24hr_change=true`);
            price = response.data.bitcoin[currency.toLowerCase()];
            change24h = response.data.bitcoin[currency.toLowerCase() + '_24h_change'];
        } else if (source === 'binance') {
            // 使用Binance API
            const symbol = currency === 'CNY' ? 'BTC/USDT' : `BTC/${currency.toUpperCase()}`;
            const response = await axios.get(`https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT`);
            price = response.data.lastPrice;
            change24h = response.data.priceChangePercent;
            volume24h = response.data.volume;
        } else if (source === 'coinbase') {
            // 使用Coinbase API
            const response = await axios.get(`https://api.coinbase.com/v2/prices/BTC-${currency.toUpperCase()}/spot`);
            price = response.data.data.amount;
        }

        return {
            price: parseFloat(price),
            currency: currency,
            change24h: parseFloat(change24h) || 0,
            volume24h: parseFloat(volume24h) || 0,
            source: source
        };
    } catch (error) {
        console.error('获取比特币价格失败：', error.response ? error.response.data : error.message);
        process.exit(1);
    }
}

function main() {
    const args = process.argv.slice(2);

    if (args.length === 0 || args[0] === 'help') {
        console.log('比特币实时价格工具\n');
        console.log('用法：');
        console.log('  openclaw skill bitcoin-price get [--currency <currency>] [--source <source>] - 获取比特币价格');
        console.log('  openclaw skill bitcoin-price detail - 获取详细信息');
        console.log('  openclaw skill bitcoin-price help - 显示帮助信息');
        console.log('');
        console.log('示例：');
        console.log('  openclaw skill bitcoin-price get --currency CNY');
        console.log('  openclaw skill bitcoin-price get --source binance');
        process.exit(0);
    }

    const command = args[0];

    switch (command) {
        case 'get':
            let currency = 'USD';
            let source = 'coingecko';

            for (let i = 1; i < args.length; i++) {
                if (args[i] === '--currency') {
                    currency = args[++i];
                } else if (args[i] === '--source') {
                    source = args[++i];
                }
            }

            getBitcoinPrice(currency, source).then(result => {
                console.log(`💰 比特币实时价格（${result.currency}）：`);
                console.log(`价格：${result.price.toLocaleString(undefined, {maximumFractionDigits: 2})} ${result.currency}`);
                if (result.change24h !== 0) {
                    const trend = result.change24h > 0 ? '📈' : '📉';
                    console.log(`24小时涨跌幅：${trend} ${Math.abs(result.change24h).toFixed(2)}%`);
                }
                if (result.volume24h !== 0) {
                    console.log(`24小时成交量：${result.volume24h.toLocaleString(undefined, {maximumFractionDigits: 2})} BTC`);
                }
                console.log(`数据源：${result.source}`);
            });
            break;

        case 'detail':
            getBitcoinPrice('USD').then(result => {
                console.log(`💰 比特币实时价格详情：`);
                console.log(`美元价格：${result.price.toLocaleString(undefined, {maximumFractionDigits: 2})} USD`);
                const cnyPrice = result.price * 7.2; // 汇率估算
                console.log(`人民币价格：${cnyPrice.toLocaleString(undefined, {maximumFractionDigits: 2})} CNY`);
                const eurPrice = result.price * 0.93; // 汇率估算
                console.log(`欧元价格：${eurPrice.toLocaleString(undefined, {maximumFractionDigits: 2})} EUR`);
                if (result.change24h !== 0) {
                    const trend = result.change24h > 0 ? '📈' : '📉';
                    console.log(`24小时涨跌幅：${trend} ${Math.abs(result.change24h).toFixed(2)}%`);
                }
                console.log(`数据源：${result.source}`);
            });
            break;

        default:
            console.error('未知命令：', command);
            process.exit(1);
    }
}

main();