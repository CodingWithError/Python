import random
import string

def gen_pass(LE: int,IN_NO: bool,IN_SPCHAR: bool):
  lowerCase=string.ascii_lowercase
  number=string.digits if IN_NO else ""
  spec_char="!?=+-()#" if IN_SPCHAR else ""

  all_char=lowerCase+number+spec_char
  passw = [random.choice(lowerCase)]

  if IN_NO:
    passw.append(random.choice(number))
  if IN_SPCHAR:
    passw.append(random.choice(spec_char))
  
  passw.extend(random.choices(all_char,k=LE-len(passw)))
  random.shuffle(passw)

  return ''.join(passw)

for i in range(10):
  print(gen_pass(8,True,True))