class Book:
  def __init__(self,name: str,author: str,genre: str,year: int):
    self.name=name
    self.author=author
    self.year=year
    self.genre=genre

def older_book(B1: object,B2: object):
  if B1.year>B2.year:
    print(f'{B2.name} is older, it was published in {B2.year}')
  elif B1.year==B2.year:
    print(f'{B1.name} and {B2.name} were published in {B1.year}')
  else:
    print(f'{B1.name} is older, it was published in {B2.year}')


python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)