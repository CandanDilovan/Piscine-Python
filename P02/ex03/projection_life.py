import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import EngFormatter


def main(path_income: str, path_life: str):
    try:
        income_csv, life_csv = load(path_income), load(path_life)
        plot = plt.gca()
        plot.set_title("1900")
        plot.set_xlabel("Gross domestic product")
        plot.set_ylabel("Life Expectancy")
        plt.scatter(income_csv["1900"], life_csv["1900"])
        plt.xscale("log")
        plot.xaxis.set_major_formatter(EngFormatter())
        plt.xticks([300, 1000, 10000])
        plt.show()
    except (FileNotFoundError, IsADirectoryError, KeyboardInterrupt) as msg:
        print(msg)


if __name__ == "__main__":
    main("income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
         "life_expectancy_years.csv")
