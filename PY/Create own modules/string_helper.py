import re

def change_case(orig_string: str):
  String=""
  for i in orig_string:
    if i==i.lower():
      String+=i.upper()
    else:
      String+=i.lower()
  return String

def split_in_half(orig_string: str):
  str_len = len(orig_string)
  mid = str_len // 2  
  return (orig_string[:mid], orig_string[mid:])

def remove_special_characters(orig_string: str):
  return re.sub(r'[^a-zA-Z1-10\s]','',orig_string)

#print(change_case("Hi theRe, HOW Are you"))

