def find_movie(database: list,search_word: str):
  search_word=search_word.lower()
  result=[
    movie for movie in database
    if search_word in movie["name"].lower()
  ]
  return result


database = [
    {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
]

my_movies = find_movie(database, "python")
print(my_movies)