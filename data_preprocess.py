import pandas as pd
import numpy as np

file_dir = 'C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading'

df = pd.read_csv(file_dir+'/Data/SPY_RL.csv')[['Date','Close','score', 'VIX', 'Volume']]
df_spy = pd.read_csv(file_dir+'/Data/SPY.csv')
df_spy['return'] = df_spy['Close'].pct_change()
df_spy['5D_mom'] = df_spy['Close'].pct_change(periods=5)
df_spy['10D_mom'] = df_spy['Close'].pct_change(periods=10)
df_spy['20D_mom'] = df_spy['Close'].pct_change(periods=20)
df_spy['30D_mom'] = df_spy['Close'].pct_change(periods=30)
df_spy['60D_mom'] = df_spy['Close'].pct_change(periods=60)

df_spy['Date'] = pd.to_datetime(df_spy['Date'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.merge(df_spy[['Date','return','5D_mom','10D_mom','20D_mom','30D_mom','60D_mom']], on='Date',how='left')
df.to_csv(file_dir+'/Data/SPY_RL_.csv')

print(df_spy.head(3000))