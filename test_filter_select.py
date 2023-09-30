import pandas as pd
import polars as pl

from utils.time_wrappers import repeat

df_pd = pd.read_csv('./data/netflix_titles.csv')
df_pl = pl.read_csv('./data/netflix_titles.csv')

@repeat(num_times=10)
def filter_select_pd():
    count = df_pd.loc[df_pd['type'] == 'Movie', 'title'].nunique()
    return count

@repeat(num_times=10)
def filter_select_pl():
    count = df_pl.filter(pl.col('type') == 'Movie').select(pl.col('title')).n_unique()
    return count

filter_select_pd()
filter_select_pl()