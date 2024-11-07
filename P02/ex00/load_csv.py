import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except (FileNotFoundError, IsADirectoryError) as msg:
        print(msg)
