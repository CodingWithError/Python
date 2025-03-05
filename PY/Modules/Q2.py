import string
def separate(String: str):
  Letter=""
  punct=""
  chara=""
  for i in String:
    if i in string.ascii_letters: 
      Letter+=i
    elif i in string.punctuation:
      punct+=i
    else:
      chara+=i
  return (Letter,punct,chara)


String="Olé!!! Hey, are ümläüts wörking?"
parts=separate(String)
print(parts[0])
print(parts[1])
print(parts[2])
print()
print(dir(string))