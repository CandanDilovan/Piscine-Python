import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from load_csv import load
import pandas as pd


def aff_live(path: str):
    loaded = load(path)
    loaded.set_index('country', inplace=True)
    french_plot = loaded.loc['France'].apply(multiply)
    pakistan_plot = loaded.loc['Pakistan'].apply(multiply)
    plot = french_plot.plot(title="Population Projections", xlabel="Year",
                            ylabel="Population", label='France')
    pakistan_plot.plot(label='PAKISTAN100%CRAZY')
    plot.yaxis.set_major_formatter(EngFormatter())
    plt.legend()
    plt.show()


def multiply(row):
    if 'k' in row:
        print("stoopid")
        row = round(float(row[:-1]) * 1000)
    elif 'M' in row:
        row = round(float(row[:-1]) * 1000000)
    elif 'B' in row:
        row = round(float(row[:-1]) * 1000000000)
    return row


aff_live("population_total.csv")
