import requests
import pandas as pd
import time
from datetime import datetime, timezone

# KUCOIN API
api_url = "https://api.kucoin.com"
api_max_json_rows = 1500
api_rate_limit = 1

# USER CONFIGURED VARIABLES
pair = "ETH-BTC"
candle_type = "1min"
candle_type_in_seconds = 60
time_begin = 1566789720

# TIME
time_end = round(datetime.now().replace(tzinfo=timezone.utc).timestamp())
time_delta = api_max_json_rows * candle_type_in_seconds
time_advance = time_begin

# CSV NAMING CONVENTION
csv_name = "Kucoin_" + pair + "_" + candle_type

# API CALL & PAGINATION LOOP
while time_advance < time_end:
    
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
    df.to_csv(csv_name+'.csv', mode='a')
    
    # OUTPUT MESSAGE
    time.sleep(api_rate_limit)
    print(f"Capturing: {candle_type} {pair} @ {time_advance} UTC")

print("Completed...")