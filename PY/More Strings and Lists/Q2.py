def common(string):
  char_count={}
  for i in string:
    if i in char_count:
      char_count[i]+=1
    else:
      char_count[i]=1
  return max(char_count,key=char_count.get)

first_string = "exemplaryelementary"
print(common(first_string))
