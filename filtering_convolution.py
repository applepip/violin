#!/usr/bin/python
#-*-coding:utf-8 -*-

from thinkdsp import *

# facebook每日股票收盘价格平滑

import pandas as pd

df = pd.read_csv('data/FB.csv', header=0, parse_dates=[0])
print df.head()
print df.tail()

close = df['Close']
dates = df['Date']
days = (dates - dates[0]) / np.timedelta64(1,'D')


M = 30
window = np.ones(M)
window /= sum(window)
smoothed = np.convolve(close, window, mode='valid')

smoothed_days = days[M//2: len(smoothed) + M//2]

print M//2

plt.plot(days, close, color='gray', alpha=0.6, label='daily close')
plt.plot(smoothed_days, smoothed, color='C1', alpha=0.6, label='30 day average')

decorate(xlabel='Time (days)', ylabel='Price ($)')

plt.show()