a=int(input())
c=0
while(a>0):
  b=int(a%10)
  c=int((c*10)+b)
  a=int(a/10)
print(int(c))
