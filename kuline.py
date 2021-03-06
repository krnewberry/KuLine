import requests
import pandas as pd
import time
from datetime import datetime, timezone

print("KuLine: A kline endpoint pagination system for Kucoin's API. \n")

# INPUTS
pair = input("Enter Pair: ").upper()
candle_type = input("Candle Type: ")
time_begin = int(input("Time Start: ") or 1566789720)

# KUCOIN API
api_url = "https://api.kucoin.com"
api_max_json_rows = 1500
api_rate_limit = 1

# TIME
candle_type_seconds_equiv = {"1min": 60, "3min": 180, "5min": 300, "15min": 900, "30min": 1800, "1hour": 3600, "2hour": 7200, "4hour": 14400, "6hour": 21600, "8hour": 28800, "12hour": 43200, "1day": 86400, "1week": 604800}
candle_type_in_seconds = candle_type_seconds_equiv[candle_type]
time_end = round(datetime.now(timezone.utc).timestamp())
time_delta = api_max_json_rows * candle_type_in_seconds
time_advance = time_begin

# CSV
csv_name = "Kucoin_" + pair + "_" + candle_type
csv_header = True

# API CALL & PAGINATION LOOP

while time_advance <= time_end + time_delta:
    
    # API PARAMETERS
    api_parameters = {
        "symbol":pair,
        "startAt":time_advance,
        "endAt":time_advance + time_delta,
        "type":candle_type,
        }

    # API CALL
    data = requests.get(f"{api_url}/api/v1/market/candles",
	    params = api_parameters,
	    headers = {"content-type":"application/json"})
    
    # ERROR CHECK, RETRY
    json_data = data.json()
    if "data" not in json_data:
        print("Retrying:", json_data)
        time.sleep(10)
        continue
    time_advance += time_delta

    # CSV CAPTURE
    df = pd.DataFrame(data.json()["data"],
	    columns = ["time","open","close","high","low","volume","turnover"])
    df["date"] = pd.to_datetime(df["time"], unit='s')
    df = df[["date","open","high","low","close"]]
    df.sort_values(by='date', inplace=True)
    # df.to_csv(csv_name+'.csv', mode='a', header=csv_header, chunksize=1000, index=False)
    df.to_csv(csv_name+'.csv', mode='a', header=csv_header, index=False)
    csv_header = False

    # REST & OUTPUT MESSAGE
    time.sleep(api_rate_limit)
    print(f"Capturing: {candle_type} {pair} @ {time_advance} UTC")

print("Completed...")

