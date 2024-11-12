import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def aff_live(path: str):
    loaded = load(path)
    loaded = loaded.__str__.replace("M", "000000")
    loaded = loaded.str.replace(".", "")
    loaded.set_index('country', inplace=True)
    print(loaded.loc['France'])
    french_plot = loaded.loc['France']
    china_plot = loaded.loc['China']
    french_plot.plot(title="Population Projections", xlabel="Year", ylabel="Population")
    china_plot.plot()
    plt.legend()
    plt.show()
    


aff_live("population_total.csv")
