from adapters.kaggle_repository import KaggleRepository


def authenticate_kaggle_case():
    """Attempts to authenticate with Kaggle API."""
    repo = KaggleRepository()
    return repo.authenticate()
