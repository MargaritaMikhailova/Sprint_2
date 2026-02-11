class Movies:
    def __init__(self):
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'

comedy_obj = Comedy()
result1 = comedy_obj.add_movie('Большой куш')
print(result1)  

drama_obj = Drama()
result2 = drama_obj.add_movie('Оружейный барон')
print(result2) 

print(comedy_obj.add_movie('Маска'))  
print(drama_obj.add_movie('Форрест Гамп')) 