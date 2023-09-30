import pandas as pd
import polars as pl

from utils.time_wrappers import repeat
from utils.data_load import load_ufo


# Load test datasets
df_pd = load_ufo('pd')
df_pl = load_ufo('pl')


@repeat(num_times=10)
def rolling_mean_pd():
    df = df_pd.sort_values('datetime', ignore_index=True)
    roll = df['duration (seconds)'].rolling(5, min_periods=1).mean() 
    return roll


@repeat(num_times=10)
def rolling_mean_pl():
    df = df_pl.sort('datetime')
    roll = df['duration (seconds)'].rolling_mean(10, min_periods=1)
    return roll


def run_tests():
    rolling_mean_pd()
    rolling_mean_pl()