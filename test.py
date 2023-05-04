import yfinance as yf
import json

def home():

    ibov = yf.Ticker("^BVSP")

    ibovData = ibov.history(period="1d").to_dict('records')#.to_json()

    return ibovData

    ##return json.dumps(ibovData);

print(home());