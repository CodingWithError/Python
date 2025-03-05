def firstword(sen):
  return sen.split()[0]
def secondword(sen):
  return sen.split()[1]
def lastword(sen):
  return sen.split()[-1]

sen="it was a dark and stormy python"
print(firstword(sen))  
print(secondword(sen))  
print(lastword(sen))