class Movie:
    def __init__(self, id: int, title: str, genre: str, duration: int, rating: float):
        self.id = id
        self.t = title
        self.g = genre
        self.d = duration
        self.r = rating
    
    def update_rating(self, new_rating: float):
        self.r = new_rating
        print(new_rating)

    def __str__(self):
        return f"Film: {self.t} | Janr: {self.g} | Davomiyligi: {self.d} daqiqa | Reyting: {self.r}"


film = Movie(id=1, title="Titanic", genre="Drama", duration=195, rating=9.0)

film.update_rating(9.5)

print(film) 