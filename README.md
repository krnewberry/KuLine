# KuLine
A kline endpoint pagination system for Kucoin's API.

## Why KuLine?
Kucoin's kline endpoint is limited to a single call which is only 1500 rows of OHLCV data. This endpoint lacks native support for pagination and outputs far too little data to properly backtest algo trading strategies. With 1500 rows the OHLCV history of a 15min chart would show at most 15 days worth of data. KuLine aims to patch this lack of functionality by forcibly paginating the data through a looped series of endpoint requests. The json data gathered is then appended into a single .csv file. The response data captured are as follows: time, open, close, high, low, volume, turnover. 

## Install

### Using Github
```
git clone git@github.com:krnewberry/KuLine.git
```

## User Configured Variables
- ```pair```
- ```candle_type```
- ```time_begin```

### Pair Example: 
```
pair = "ETH-BTC"
```
This represents the chart pairing of ETH/BTC

### Candle Type Example:
```
candle_type = "1min"
```
This represents a 1 minute candle chart. See below for other supported ```candle_type``` values:

### Supported ```candle_type``` Values
- 1min
- 3min
- 5min
- 15min
- 30min
- 1hour
- 2hour
- 4hour
- 6hour
- 8hour
- 12hour
- 1day
- 1week

### Time Begin Example:
```
time_begin = 1566789720
```
```1566789720``` or Sun Aug 25 2019 23:22:00 GMT-0400 (Eastern Daylight Time) is the furthest back that kucoin's API will go. You can choose any date after ```1566789720``` but it needs to be converted into UTC seconds. A link to accomplish this conversion has been provided below.

### USEFUL LINKS:
- https://www.unixtimestamp.com
- https://docs.kucoin.com/#get-klines
