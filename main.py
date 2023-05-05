#from fastapi import FastAPI
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import yfinance as yf
import json

app = Flask(__name__)
CORS(app)

@cross_origin()

@app.route("/", methods=['GET'])
def home():

    ibov = yf.Ticker("^BVSP")

    ibovData = ibov.history(period="1d").to_dict('records')

    return jsonify(ibovData);

if __name__ == "__main__":
    app.run(debug=True);