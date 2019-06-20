p,q=input().split()
o=0
for i in range(len(p)):
  if p[i]!=q[i]:
    o+= 1
if o==1:
  print("yes")
else:
  print("no")
