class Series:
    def __init__(self, name: str, seasons: int, genres: list):
        self.name = name
        self.seasons = seasons
        self.genres = genres
        self.ratings = []  

    def rate(self, rating: int):
        """Adds a rating between 0 and 5 to the series."""
        if 0 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Please enter a value between 0 and 5.")

    def __str__(self) -> str:
        genre_str = ", ".join(self.genres)
        if self.ratings:
            avg_rating = sum(self.ratings) / len(self.ratings)
            rating_str = f"{len(self.ratings)} ratings, average {avg_rating:.1f} points"
        else:
            rating_str = "no ratings"
        
        return f"{self.name} ({self.seasons} seasons)\ngenres: {genre_str}\n{rating_str}"


dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)

print(dexter)
