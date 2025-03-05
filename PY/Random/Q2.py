from random import choices
from string import ascii_lowercase

def genPass(leg):
  return ''.join(choices(ascii_lowercase, k=leg))

for i in range(10):
    print(genPass(8))