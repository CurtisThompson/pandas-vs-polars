import pandas as pd
import polars as pl

from utils.time_wrappers import repeat

df_pd = pd.read_csv('./data/ufo_sightings.csv')
df_pl = pl.read_csv('./data/ufo_sightings.csv', dtypes={'duration (seconds)':pl.Float64})

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


group_mean_pd()
group_mean_pl()
group_median_pd()
group_median_pl()