import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

start = dt.datetime(2020, 1, 1)
data = pdr.get_data_yahoo("NFLX", start)

""" The Average True Range (ATR) is a moving average of the True Range (TR).
    And the TR is given by the maximum of the current high (H) minus current low (L), 
    the absolute value of current high (H) minus previous close (Cp), 
    and the absolute value of current low (L) and previous close (Cp). """

# using .shift() to get the previous close
high_low = data['High'] - data['Low']
high_cp = np.abs(data['High'] - data['Close'].shift())
low_cp = np.abs(data['Low'] - data['Close'].shift())

# creating data frame with max values
df = pd.concat([high_low, high_cp, low_cp], axis=1)
true_range = np.max(df, axis=1)

# ATR as moving average
average_true_range = true_range.rolling(14).mean()

# visualisation of the data on the simple chart
fig, ax = plt.subplots()
average_true_range.plot(ax=ax)
ax2 = data['Close'].plot(ax=ax, secondary_y=True, alpha=.3)
ax.set_ylabel("ATR")
ax2.set_ylabel("Price")
plt.show()








