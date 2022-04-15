import fastquant as fq
import re   
from datetime import date, timedelta
import pandas as pd
import time
from gi.repository import Notify

startdate = str(date.today() - timedelta(days = 1))
enddate = str(date.today())

SELL_VALUE = 50000.0
BUY_VALUE = 35000.0

Notify.init("Test Notifier")

while True:
    btc = fq.get_crypto_data('BTC/USDT', startdate, enddate)
    btcvalue = btc.loc[enddate, "close"]
    print(btcvalue)
    if btcvalue >= SELL_VALUE:
        Notify.Notification.new("Bitcoin value is high! SELL!").show()
    if btcvalue <= BUY_VALUE:
        Notify.Notification.new("Bitcoin value is low! BUY!").show()
    time.sleep(5)