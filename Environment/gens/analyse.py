import pandas as pd
import numpy as np

import pickle
from matplotlib import pyplot as plt
import pyfolio as pf

train_test_split = 0.0
results_dict = pickle.load(open("C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading/results_revised.p", "rb"))
results = results_dict['SPY']

df=pd.read_csv('C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading/Data/SPY_RL_.csv')
df=df.iloc[int(train_test_split*len(df)):,:]
action = []
#print(type(results['action_policy_df']['action'].iloc[0]))
for act in results['action_policy_df']['action']:
    if all(act==np.array([1,0,0])):
        action.append(0)
    elif all(act==np.array([0,1,0])):
        action.append(1)
    else:
        action.append(-1)

print(len(action),len(df))
action = [np.nan]*(len(df)-len(action)) + action# + [1]
df['action'] = action
df['return'] = df['Close'].pct_change()

print(df.head(10))


state = 0
port = [100]
states = []
df = df.dropna()
for i in range(len(df)):
    states.append(state)
    port.append(port[-1] * (1 + df['return'].iloc[i] * state))
    if df['action'].iloc[i] == 1.:
        state += 1
        if state > 0:
            state = 1.
    elif df['action'].iloc[i] == 0.:
        pass
    elif df['action'].iloc[i] == -1.:
        state -= 1
        if state < 0:
            state = 0.

df['port'] = port[1:]
df['state'] = states
print(df.head())
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df['Close'] = df['Close']/df['Close'].iloc[0]*100
df[['port','Close']].plot()
df.to_csv('C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading/test.csv')
plt.show()
df['port_return'] = df['port'].pct_change().dropna()
df_analyis = df[['return', 'port_return']]
stat = pf.compute_stats(df_analyis, benchmark_rets=df_analyis['return'])
print(stat)
stat.to_csv('C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading/stats.csv')
