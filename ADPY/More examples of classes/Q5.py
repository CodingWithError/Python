class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
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
        
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_str}\n{rating_str}"


def minimum_grade(rating: float, series_list: list):
    for series in series_list:
        if series.ratings:  
            avg = sum(series.ratings) / len(series.ratings)
            if avg >= rating:
                yield series


def includes_genre(genre: str, series_list: list):
    for series in series_list:
        if genre in series.genres:
            yield series


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum rating of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
