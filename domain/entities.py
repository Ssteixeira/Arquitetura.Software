class NetflixTitle:
    def __init__(self, title, type_, country, date_added, release_year, rating, duration, genres):
        self.title = title            # Nome do filme ou série
        self.type = type_             # Movie ou TV Show
        self.country = country        # País de origem
        self.date_added = date_added  # Data que foi adicionado ao catálogo
        self.release_year = release_year  # Ano de lançamento
        self.rating = rating          # Classificação etária (PG, R, etc)
        self.duration = duration      # Duração do filme ou série
        self.genres = genres          # Lista de gêneros ou categoria
    def __repr__(self):
        return f"NetflixTitle(title={self.title}, type={self.type}, country={self.country}, date_added={self.date_added}, release_year={self.release_year}, rating={self.rating}, duration={self.duration}, genres={self.genres})"