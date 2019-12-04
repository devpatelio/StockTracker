
from first_sequence import*

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

ts = TimeSeries(key='E7W0A9REUL6LY9J9', output_format='pandas')

data, meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')
print(data)

fig = plt.figure(figsize=(12, 8))
style.use('fivethirtyeight')
ani = animation.FuncAnimation(fig, data, interval=60000)


data['4. close'].plot()
plt.title('Stock Tracker: ' + stock)
plt.show()


