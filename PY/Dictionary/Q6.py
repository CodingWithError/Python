def invert(s):
  dir={}
  for i in s:
    dir[s[i]]=i
  return dir

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
new_dir=invert(s)
print(new_dir)