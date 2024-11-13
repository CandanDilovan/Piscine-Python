import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        df = pd.DataFrame(df)
        return df
    except (FileNotFoundError, IsADirectoryError, Exception) as msg:
        print(msg)
