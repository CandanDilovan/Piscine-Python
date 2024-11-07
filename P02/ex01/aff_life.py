import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def aff_live(path: str):
    loaded = load(path)
    loaded.set_index('country', inplace=True)
    print(loaded.loc['France'])
    plot = plt.plot(loaded.loc['France'])
    plot.show()
    


aff_live("life_expectancy_years.csv")