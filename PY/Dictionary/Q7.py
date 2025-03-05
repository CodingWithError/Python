def add_movie(D,N,Director,Year,RunTime):
  g={}
  g["name"]=N
  g["Director"]=Director
  g["Year"]=Year
  g["runtime"]=RunTime
  D.append(g)

database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)