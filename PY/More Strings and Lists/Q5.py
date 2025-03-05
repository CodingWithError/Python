def longestSeq(no):
  if not no:
    return 0
  longest=1
  currentlong=1
  for i in range(1,len(no)):
    if abs(no[i]-no[i-1])==1:
      currentlong+=1
      longest=max(longest,currentlong)
    else:
      currentlong=1
  return longest

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longestSeq(my_list)) 