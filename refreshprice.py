from first_sequence import*

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

ts = TimeSeries(key='E7W0A9REUL6LY9J9', output_format='pandas')

data, meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')  #replace symbol with the variable stock after importing first_sequence

# time

live_set = 0

setprice = input("What limit would you like for your stock?")


def livedata():
    live, meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')
    closingprice = live['4. close']
    global refresh
    refresh = closingprice[5]
    print(refresh)  # remove from statement when you will create email functionality


while True:
    livedata()
    time.sleep(60)

    if int(refresh) == int(setprice):
        print("The stock has reached your point!")
        break
    else:
        continue


