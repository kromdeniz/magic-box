import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib.pyplot import figure

df = pd.read_csv('xxx.csv')

df_mpl = df.copy()

import matplotlib.dates as dates
df_mpl.Date = dates.datestr2num(df_mpl.Date)


df_subset = df_mpl[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
df_list = [list(x) for x in df_subset.values]


fig = plt.figure(figsize=(16,8))
ax1 = plt.subplot2grid((1,1), (0,0))

candlestick_ohlc(ax1, df_list, width=0.4, colorup='#77d879', colordown='#db3f3f')

for label in ax1.xaxis.get_ticklabels():
     label.set_rotation(45)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax1.grid(True)

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Selimin Gizemli illuminati hisseleri')
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()