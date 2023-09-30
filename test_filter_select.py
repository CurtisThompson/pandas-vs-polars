import pandas as pd
import polars as pl

from utils.time_wrappers import repeat

df_pd = pd.read_csv('./data/netflix_titles.csv')
df_pl = pl.read_csv('./data/netflix_titles.csv')

df_ufo_pd = pd.read_csv('./data/ufo_sightings.csv')
df_ufo_pl = pl.read_csv('./data/ufo_sightings.csv', dtypes={'duration (seconds)':pl.Float64})

@repeat(num_times=10)
def filter_select_pd():
    count = df_pd.loc[df_pd['type'] == 'Movie', 'title'].nunique()
    return count

@repeat(num_times=10)
def filter_select_pl():
    count = df_pl.filter(pl.col('type') == 'Movie').select(pl.col('title')).n_unique()
    return count

@repeat(num_times=10)
def filter_select_ufo_pd():
    count = df_ufo_pd.loc[df_ufo_pd['country'] == 'us', 'state'].nunique()
    return count

@repeat(num_times=10)
def filter_select_ufo_pl():
    count = df_ufo_pl.filter(pl.col('country') == 'us').select(pl.col('state')).n_unique()
    return count

filter_select_pd()
filter_select_pl()
filter_select_ufo_pd()
filter_select_ufo_pl()