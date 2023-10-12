# Pandas vs Polars

This repository is a basic comparison of the run times between two data manipulation Python packages: [Pandas](https://pandas.pydata.org/) and [Polars](https://www.pola.rs/).

## Set-Up

To create the environment for these tests, run the following command:

```
conda env create --name pandas-vs-polars-test --file ./env/environment.yaml
```

## Experiments

The individual experiments can be found within `./src/`. They can all be run directly from `./run_tests.py`.

Note that the individual run times will depend on the machine that code is run from and so identical results will be hard to reproduce. However, the important thing is which package is faster - which should be the same regardless of which machine is used.

| Experiment | Pandas Avg. (ns) | Polars Avg. (ns) | Faster Package |
|---|---|---|---|
|Load csv|63409|15185|Polars|
|Filter and Select (1)|2664|4200|Pandas|
|Filter and Select (2)|8631|15478|Pandas|
|Group and Aggregate (1)|11752|4599|Polars|
|Group and Aggregate (2)|13315|5283|Polars|
|Rolling Mean|69417|21116|Polars|

The table above shows one run of the experiments. Polars is faster than Pandas in all experiments except when filtering and selecting data. Overall, this indicates Polars is better when wanting to write fast-executing code.

## Data

The following datasets are used in the experiments.

**netflix_titles.csv**  
*Metadata for all TV shows and movies on Netflix. 12 columns. 8807 rows. 3 MB. [Source (Version 5)](https://www.kaggle.com/datasets/shivamb/netflix-shows).*

**StudentsPerformance.csv**  
*Sample exam scores for students of different demographics. 8 columns. 1000 rows. 70 KB. [Source (Version 1)](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)*

**ufo_sightings.csv**
*Data on UFO sightings across five countries. 11 columns. 69586 rows. 13 MB [Source (Scrubbed Version 2)](https://www.kaggle.com/datasets/NUFORC/ufo-sightings?select=scrubbed.csv)*