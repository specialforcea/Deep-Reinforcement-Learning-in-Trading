import pandas as pd
import numpy as np

file_dir = 'C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading'

df = pd.read_csv(file_dir+'/Data/SPY_RL.csv')[['Date', 'score', 'VIX']]
df['2w_score'] = df['score'].rolling(10).mean()
df['3w_score'] = df['score'].rolling(15).mean()
df['4w_score'] = df['score'].rolling(20).mean()

df['3D_vix'] = df['VIX'].rolling(3).mean()
df['5D_vix'] = df['VIX'].rolling(5).mean()
df['8D_vix'] = df['VIX'].rolling(8).mean()
df['10D_vix'] = df['VIX'].rolling(10).mean()
df['15D_vix'] = df['VIX'].rolling(15).mean()
df['20D_vix'] = df['VIX'].rolling(20).mean()

df_spy = pd.read_csv(file_dir+'/Data/SPY.csv')
# df_spy['return'] = df_spy['Close'].pct_change()
# df_spy['5D_mom'] = df_spy['Close'].pct_change(periods=5)
# df_spy['3D_mom'] = df_spy['Close'].pct_change(periods=3)
# df_spy['8D_mom'] = df_spy['Close'].pct_change(periods=8)
# df_spy['10D_mom'] = df_spy['Close'].pct_change(periods=10)
# df_spy['15D_mom'] = df_spy['Close'].pct_change(periods=15)
# df_spy['20D_mom'] = df_spy['Close'].pct_change(periods=20)
# df_spy['25D_mom'] = df_spy['Close'].pct_change(periods=25)
# df_spy['30D_mom'] = df_spy['Close'].pct_change(periods=30)
# df_spy['40D_mom'] = df_spy['Close'].pct_change(periods=40)
# df_spy['60D_mom'] = df_spy['Close'].pct_change(periods=60)
# df_spy['90D_mom'] = df_spy['Close'].pct_change(periods=90)

df_spy['3_c_5'] = (df_spy['Close'].rolling(3).mean() > df_spy['Close'].rolling(5).mean()).astype(int)
# df_spy['3_c_10'] = (df_spy['Close'].rolling(3).mean() > df_spy['Close'].rolling(10).mean()).astype(int)
df_spy['5_c_10'] = (df_spy['Close'].rolling(5).mean() > df_spy['Close'].rolling(10).mean()).astype(int)
# df_spy['10_c_15'] = (df_spy['Close'].rolling(10).mean() > df_spy['Close'].rolling(15).mean()).astype(int)
df_spy['10_c_20'] = (df_spy['Close'].rolling(10).mean() > df_spy['Close'].rolling(20).mean()).astype(int)
df_spy['10_c_25'] = (df_spy['Close'].rolling(10).mean() > df_spy['Close'].rolling(25).mean()).astype(int)
# df_spy['10_c_30'] = (df_spy['Close'].rolling(10).mean() > df_spy['Close'].rolling(30).mean()).astype(int)
df_spy['20_c_30'] = (df_spy['Close'].rolling(20).mean() > df_spy['Close'].rolling(30).mean()).astype(int)
df_spy['20_c_40'] = (df_spy['Close'].rolling(20).mean() > df_spy['Close'].rolling(40).mean()).astype(int)
# df_spy['20_c_50'] = (df_spy['Close'].rolling(20).mean() > df_spy['Close'].rolling(50).mean()).astype(int)
df_spy['20_c_60'] = (df_spy['Close'].rolling(20).mean() > df_spy['Close'].rolling(60).mean()).astype(int)
# df_spy['30_c_50'] = (df_spy['Close'].rolling(30).mean() > df_spy['Close'].rolling(50).mean()).astype(int)
df_spy['30_c_60'] = (df_spy['Close'].rolling(30).mean() > df_spy['Close'].rolling(60).mean()).astype(int)
# df_spy['30_c_70'] = (df_spy['Close'].rolling(30).mean() > df_spy['Close'].rolling(70).mean()).astype(int)
df_spy['40_c_60'] = (df_spy['Close'].rolling(40).mean() > df_spy['Close'].rolling(60).mean()).astype(int)
# df_spy['40_c_70'] = (df_spy['Close'].rolling(40).mean() > df_spy['Close'].rolling(70).mean()).astype(int)
df_spy['40_c_80'] = (df_spy['Close'].rolling(40).mean() > df_spy['Close'].rolling(80).mean()).astype(int)
df_spy['50_c_70'] = (df_spy['Close'].rolling(50).mean() > df_spy['Close'].rolling(70).mean()).astype(int)
# df_spy['50_c_80'] = (df_spy['Close'].rolling(50).mean() > df_spy['Close'].rolling(80).mean()).astype(int)
# df_spy['60_c_80'] = (df_spy['Close'].rolling(60).mean() > df_spy['Close'].rolling(80).mean()).astype(int)
df_spy['60_c_90'] = (df_spy['Close'].rolling(60).mean() > df_spy['Close'].rolling(90).mean()).astype(int)


df_spy['volume_score'] = (df_spy['Volume'] - df_spy['Volume'].rolling(252).min()).div(df_spy['Volume'].rolling(252).max() -
                                                                                      df_spy['Volume'].rolling(252).min())
df_spy['3D_volume'] = df_spy['volume_score'].rolling(3).mean()
df_spy['5D_volume'] = df_spy['volume_score'].rolling(5).mean()
df_spy['8D_volume'] = df_spy['volume_score'].rolling(8).mean()
df_spy['10D_volume'] = df_spy['volume_score'].rolling(10).mean()
df_spy['15D_volume'] = df_spy['volume_score'].rolling(15).mean()
df_spy['20D_volume'] = df_spy['volume_score'].rolling(20).mean()

df_spy['Date'] = pd.to_datetime(df_spy['Date'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.merge(df_spy.loc[:, ~df_spy.columns.isin(['Open','High','Low','Adj Close','Volume'])], on='Date',how='left')

df = df.dropna()
df.to_csv(file_dir+'/Data/SPY_RL_.csv',index=False)

#print(df_spy.head(3000))