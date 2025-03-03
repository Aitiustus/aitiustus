#https://github.com/kernc/backtesting.py/issues/15
#https://www.pyquantnews.com/free-python-resources/creating-and-backtesting-trading-strategies-with-backtrader
from backtesting import Backtest, Strategy
import pandas as pd
import pandas_ta as ta
from pandas import DataFrame, Series
import yfinance as yf
import talib
from backtesting.lib import crossover
import backtrader as bt
from datetime import datetime


stock = yf.Ticker("CRDO")

df = df = stock.history(period='1y', interval="1d")

df.round(2)

print(df)

class Signal_Strategy_v1(Strategy):
    # lets do a sweep of multiple technical indicators and try to do backtesting optimization using backtesting.py

    macd_fast = 12
    macd_slow = 26
    macd_sig = 9
    macd_upper = +2.5
    macd_lower = -2.5
    rsi_window = 14
    # Do as much initial computation as possible
    def init(self):
        self.rsi  = self.I(talib.RSI, self.data.Close, self.rsi_window)
        self.macd = self.I(talib.trend.macd_diff, self.data.Close.to_series(), \
                  self.macd_fast, self.macd_slow, self.macd_sig)


    def next(self):

        if self.macd.macd[0] > self.signal.signal[0] and self.position.size == 0:
            self.buy()

        elif self.macd.macd[0] < self.signal.signal[0] and self.position.size > 0:
            self.sell()

bt = Backtest(df, Signal_Strategy_v1, cash = 100)

stats = bt.run()

print(stats)

bt.plot()
