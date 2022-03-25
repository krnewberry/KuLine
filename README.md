# KuLine
A kline endpoint pagination system for Kucoin's API.

## Why KuLine?
Kucoin's kline endpoint is limited to a single call which only produces 1500 rows of OHLCV data. This endpoint lacks native support for pagination and outputs far too little data to properly backtest algo trading theories. With 1500 rows the OHLCV history of a 15min chart would show at most 15 days worth of data. KuLine aims to patch this lack of functionality by forcibly paginating the data through a looped series of endpoint requests. The json data gathered is then appended into a single .csv file. The response data are as follows: time, open, close, high, low, volume, turnover. 

## User Configured Variables
- api_rate_limit
- pair
- candle_type
- candle_type_in_seconds
- time_begin

### API Rate Limit Format Example:
api_rate_limit = 1 (in seconds)

### Pair Format Example: 
pair = "ETH-BTC" (for ethereum/bitcoin)

### Candle Type Format Example:
candle_type = "1min" (1 minute candle charts. See additional options below)

### Candle Type in Seconds Format Example:
candle_type_in_seconds = 60 (this needs to match the amount of seconds in the candle chart you've chosen (1min = 60, 3min = 180, etc.)

### Supported Candle Charts and their equivalent in seconds.
- 1min (60 seconds) 
- 3min (180 sec.) 
- 5min (300 sec.) 
- 15min (900 sec.) 
- 30min (1800 sec.) 
- 1hour (3600 sec.) 
- 2hour (7200 sec.) 
- 4hour (14400 sec.) 
- 6hour (21600 sec.) 
- 8hour (28800 sec.) 
- 12hour (43200 sec.) 
- 1day (86400 sec.)
- 1week (604800 sec.)

### Time Begin Format Example:
time_begin = 1566789720 (this is default and the furthest back kucoin's api will go. You can choose any date after this but it needs to be in UTC (seconds) format.
