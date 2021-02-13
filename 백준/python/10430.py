list = [ int(x) for x in input().split() ]
print((list[0]+list[1])%list[2])
print(((list[0]%list[2])+(list[1]%list[2]))%list[2])
print((list[0]*list[1])%list[2])
print(((list[0]%list[2]) * (list[1]%list[2]))%list[2])

