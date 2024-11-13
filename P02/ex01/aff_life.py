import matplotlib.pyplot as plt
from load_csv import load


def main(path: str):
    try:
        loaded = load(path)
        loaded.set_index('country', inplace=True)
        print(loaded.loc['France'])
        plot = loaded.loc['France']
        plot.plot(title="France life expectancy Projections", xlabel="Years",
                  ylabel="Life expentanct")
        plt.show()
    except (AttributeError, AssertionError) as msg:
        print(msg)


if __name__ == "__main__":
    main("life_expectancy_years.csv")
