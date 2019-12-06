~~~~~ Refresh File has live data overwrite


from first_sequence import*

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

ts = TimeSeries(key='E7W0A9REUL6LY9J9', output_format='pandas')

data, meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')  #replace symbol with the variable stock after importing first_sequence

# time

live_set = []

def livedata():
    live, meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')
    # live_set.append(live['4. close'])
    closingprice = live['4. close']
    live_set.append(closingprice[5])
    print(live_set)  # remove from statement when you will create email functionality



while True:
    livedata()
    time.sleep(60)



fig = plt.figure(figsize=(12, 8))
style.use('fivethirtyeight')
ani = animation.FuncAnimation(fig, data, interval=60000)


data['4. close'].plot()
plt.title('Stock Tracker: ' + stock)
plt.show()


