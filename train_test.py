import pandas as pd
import numpy as np
import os
import glob
import warnings
import time
import pickle
import plotly.offline as py
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *
warnings.filterwarnings('ignore')

from Main import World
from Analytics.Trade_Analytics import sharpe_calc
from Analytics.Training_Analytics import loss_vis, reward_vis
import gc
import re

train_test_split = 0.3
results_dict = {}
stock_file = 'C:/Users/yuchen.yue/Documents/veta_/veta/Deep-Reinforcement-Learning-in-Trading/Data/SPY_RL_.csv'

start = time.time()
results = World(filename=stock_file, train_test_split=train_test_split,
                episodes=60, display=True, history_length=1)
end = time.time()
print('Time Taken = ', end - start)
df = pd.read_csv(stock_file)
df = df.iloc[int(train_test_split * len(df)):, :]
returns = df['Close'].pct_change()
perf_metrics = sharpe_calc(results['trades_df'].copy())

results['buy_and_hold_sharpe'] = np.mean(returns) / np.std(returns)
results['strategy_sharpe'] = perf_metrics['strategy_sharpe']
results['num_trades'] = perf_metrics['num_trades']
results['position_df'] = perf_metrics['position_df']

results_dict['SPY'] = results
gc.collect()

pickle.dump(results_dict, open("results_revised.p", "wb"))

