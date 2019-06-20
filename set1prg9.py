aa,bb = map(int,input().split())
cc = []
for i in range(aa,bb + 1):
  count = 0
  for j in range(2,i + 1):
    if(i % j == 0):
      count = count + 1
  cc.append(count)
print(cc.count(1))
