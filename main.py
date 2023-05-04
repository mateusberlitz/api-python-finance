#from fastapi import FastAPI
from flask import Flask
import yfinance as yf
import json

app = Flask(__name__)

@app.get("/")
def home():

    ibov = yf.Ticker("^BVSP")

    ibovData = ibov.info

    return json.dumps(ibovData);

if __name__ == "__main__":
    app.run(debug=True);

