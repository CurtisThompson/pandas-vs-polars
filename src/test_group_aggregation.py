import pandas as pd
import polars as pl

from utils.time_wrappers import repeat
from utils.data_load import load_ufo


# Load test datasets
df_pd = load_ufo('pd')
df_pl = load_ufo('pl')


@repeat(num_times=10)
def group_mean_pd():
    mean = df_pd.groupby('country')['duration (seconds)'].agg('mean')
    return mean


@repeat(num_times=10)
def group_mean_pl():
    mean = df_pl.group_by('country').mean().select(['country', 'duration (seconds)'])
    return mean


@repeat(num_times=10)
def group_median_pd():
    med = df_pd.groupby('country')['duration (seconds)'].agg('median')
    return med


@repeat(num_times=10)
def group_median_pl():
    med = df_pl.group_by('country').median().select(['country', 'duration (seconds)'])
    return med


def run_tests():
    group_mean_pd()
    group_mean_pl()
    group_median_pd()
    group_median_pl()