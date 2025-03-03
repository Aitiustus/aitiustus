#https://www.youtube.com/watch?v=e4ytbIm2Xg0&list=PLnSVMZC68_e48lA4aRYL1yHYZ9nEq9AiH
#https://www.marketcalls.in/python/introduction-to-pandas-dataframe-python-tutorial-for-traders-part-1.html
from backtesting import Backtest, Strategy
import pandas as pd
from pandas import DataFrame, Series
import yfinance as yf
import talib
from backtesting.lib import crossover


stock = yf.Ticker("UDOW")

df = df = stock.history(period='1y', interval="1d")

df.round(2)

print(df)

class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.rsi  = self.I(talib.RSI, self.data.Close, self.rsi_window)

    def next(self):

        if crossover(self.rsi, self.upper_bound):
            self.position.close()

        elif crossover(self.lower_bound, self.rsi):
            self.buy()

bt = Backtest(df, RsiOscillator, cash = 100)

stats = bt.run()

print(stats)

bt.plot()
