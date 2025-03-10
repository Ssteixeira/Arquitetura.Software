from infrastructure.logging_config import setup_logging
from application.authenticate_kaggle import authenticate_kaggle_case
from application.analyze_dataset import analyze_dataset_case


def main():
    setup_logging()
    if authenticate_kaggle_case():
        analyze_dataset_case()


if __name__ == "__main__":
    main()