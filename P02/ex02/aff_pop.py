import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from load_csv import load


def main(path: str):
    try:
        loaded = load(path)
        loaded.set_index('country', inplace=True)
        french_plot = loaded.loc['France'].apply(multiply)
        pakistan_plot = loaded.loc['Pakistan'].apply(multiply)
        pakistan_plot, french_plot = pakistan_plot[:-50], french_plot[:-50]
        plot = french_plot.plot(title="Population Projections", xlabel="Year",
                                ylabel="Population", label='France')
        pakistan_plot.plot(label='PAKISTAN100%CRAZY')
        plot.yaxis.set_major_formatter(EngFormatter())
        plt.legend()
        plt.show()
    except (KeyboardInterrupt, AssertionError) as msg:
        print(msg)


def multiply(row):
    if 'k' in row:
        print("stoopid")
        row = round(float(row[:-1]) * 1000)
    elif 'M' in row:
        row = round(float(row[:-1]) * 1000000)
    elif 'B' in row:
        row = round(float(row[:-1]) * 1000000000)
    return row


if __name__ == "__main__":
    main("population_total.csv")
