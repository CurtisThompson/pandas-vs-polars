import pandas as pd
import polars as pl


def load_students(form):
    """Loads the Student Exam dataset."""
    if (form.lower() == 'pandas') or (form.lower() == 'pd'):
        return pd.read_csv('./data/StudentsPerformance.csv')
    elif (form.lower() == 'polars') or (form.lower() == 'pl'):
        return pl.read_csv('./data/StudentsPerformance.csv')
    return None


def load_netflix(form):
    """Loads the Netflix Titles dataset."""
    if (form.lower() == 'pandas') or (form.lower() == 'pd'):
        return pd.read_csv('./data/netflix_titles.csv')
    elif (form.lower() == 'polars') or (form.lower() == 'pl'):
        return pl.read_csv('./data/netflix_titles.csv')
    return None


def load_ufo(form):
    """Loads the UFO sighting dataset."""
    if (form.lower() == 'pandas') or (form.lower() == 'pd'):
        return pd.read_csv('./data/ufo_sightings.csv')
    elif (form.lower() == 'polars') or (form.lower() == 'pl'):
        return pl.read_csv('./data/ufo_sightings.csv', dtypes={'duration (seconds)':pl.Float64})
    return None