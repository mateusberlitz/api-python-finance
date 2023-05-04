from fastapi import FastAPI
import yfinance as yf
import json

app = FastAPI()

@app.get("/")
def home():

    ibov = yf.Ticker("^BVSP")

    ibovData = ibov.info

    return json.dumps(ibovData);