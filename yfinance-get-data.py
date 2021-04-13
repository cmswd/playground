import os

import yfinance as yf

ticker = yf.Ticker(os.environ.get("TICKER", "MSFT"))

data = ticker.history(period=os.environ.get("PERIOD", "180d"),
                      interval=os.environ.get("INTERVAL", "60m"))
with open("data/%s.csv" % os.environ.get("TICKER", "MFST"), "w") as fp:
    data.to_csv(fp)
