a=input()
b=list(a)
b[::2],b[1::2]=b[1::2],b[::2]
print(''.join(b))
