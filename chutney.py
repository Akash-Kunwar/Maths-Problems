def countPal(arr,d):
  s=''.join(arr)
  for i in s:
    if i in d.keys():
      d[i]+=1
    else:
      d[i]=1
  count=0
  print(d)
  for i in d.keys():
    if d[i]%2!=0:
      count+=1
  if count==0 or count==1:
    return True
  return False
print(countPal('tamarind ',{}))