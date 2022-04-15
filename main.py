import fastquant as fq
import re   
from datetime import date, timedelta
import pandas as pd
import time

startdate = str(date.today() - timedelta(days = 1))
enddate = str(date.today())

while True:
    btc = fq.get_crypto_data('BTC/USDT', startdate, enddate)
    print(btc.loc[enddate, "close"])
    time.sleep(5)