a=input()
b=0
if(a[0]=='I'):
  for i in a:
    if(i=='I'):
      b=b+1
    elif(i=='V'):
      b=5-b
    elif(i=='X'):
      b=10-b
if(a[0]=='V'):
  for i in a:
    if(i=='V'):
      b=b+5
    elif(i=='I'):
      b=b+1
    elif(i=='X'):
      b=b+10
if(a[0]=='X'):
  for i in a:
    if(i=='X'):
      b=b+10
    elif(i=='I'):
      b=b+1
    elif(i=='V'):
      b=b+5
print(b)
