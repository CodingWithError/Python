class Book:
  def __init__(self,name: str,author: str,genre: str,year: int):
    self.name=name
    self.author=author
    self.year=year
    self.genre=genre

def books_of_genre(books: list,gen: str):
  gene=[]
  for i in books:
    if i.genre==gen:
      gene.append(i)
  return gene  

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

print("Books in the crime genre:")
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")