class Book:
  def __init__(self,name: str,author: str,genre: str,year: int):
    self.name=name
    self.author=author
    self.year=year
    self.genre=genre

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")