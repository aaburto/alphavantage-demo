import os
from alpha_vantage.timeseries import TimeSeries


def alphavantage(apikey,symbol,days):
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
    return print(data_displayed,"\nAverage close: {}".format(sum_close / days))

if __name__ == "__main__":
    alphavantage(os.environ.get('ALPHAVANTAGE_API_KEY'),os.environ.get('ALPHAVANTAGE_SYMBOL'),int(os.environ.get('NDAYS')))

