import logging
import pandas as pd
from adapters.kaggle_repository import KaggleRepository


def analyze_dataset_case():
    repo = KaggleRepository()
    file_path = repo.download_dataset()
    if file_path is None:
        return None
    df = pd.read_csv(file_path)
    logging.info("%d rows and %d columns.", df.shape[0], df. shape[1])
    logging.info("Top 5 records:\n%s", df.head().to_string())
    return df.describe()
