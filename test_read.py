import pandas as pd
import polars as pl

from utils.time_wrappers import repeat


@repeat(num_times=100)
def load_data_pd():
    df = pd.read_csv('./data/netflix_titles.csv')
    return df


@repeat(num_times=100)
def load_data_pl():
    df = pl.read_csv('./data/netflix_titles.csv')
    return df


load_data_pd()
load_data_pl()