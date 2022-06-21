import os
from alpha_vantage.timeseries import TimeSeries
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def alphavantage():

    apikey = os.environ.get('API_KEY')
    symbol = os.environ.get('SYMBOL')
    days = int(os.environ.get('NDAYS'))
    # ts will let us use apikey
    ts = TimeSeries(key=apikey)
    # data, meta_data will contain info from alphavantage
    data, meta_data = ts.get_daily(symbol)
    # meta_data and NDAYS numbers to display.

    sum_close = 0
    k = 0

    data_displayed = list(data.items())[:days]

    while k < len(data_displayed):
        sum_close += float(data_displayed[k][1]['4. close'])
        k += 1
    
    return jsonify(results = data_displayed, Average_close = sum_close / days)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

