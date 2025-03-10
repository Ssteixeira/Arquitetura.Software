import os
import kaggle  # type: ignore
import logging


class KaggleRepository:

    def __init__(self):
    
        self.dataset = "sebastianwillmann/beverage-sales"
        self.file_name = "synthetic_beverage_sales_data.csv"
        os.makedirs("data", exist_ok=True)

    def authenticate(self):
        try:
            kaggle.api.authenticate()
            logging.info("Kaggle authentication successful.")
            return True
        except kaggle.rest.ApiException as e:
            logging.error("Kaggle authentication failed: %s", e)
            return False
        
    def download_dataset(self):
        try:
            kaggle.api.dataset_download_files(
                self.dataset, path="data", unzip=True)
            file_path = os.path.join("data", self.file_name)
            if os.path.exists(file_path):
                logging.info("Dataset downloaded successfully.")
                return file_path
            logging.error("Dataset file not found after download.")
            return None
        except kaggle.rest.ApiException as e:
            logging.error("Dataset download failed: %s", e)
            return None
