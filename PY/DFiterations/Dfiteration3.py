def anagrams(name,name1):
  name=sorted(name)
  name1=sorted(name1)
  return name==name1

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False