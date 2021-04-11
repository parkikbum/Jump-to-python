import sys
n = int(sys.stdin.readline())
nameIo = {}
for x in range(n):
    name,inout = map(str, sys.stdin.readline().split())
    nameIo[name] = inout
    if nameIo[name] == 'leave':
       del nameIo[name] 
nameIo = sorted(nameIo, reverse=True)
for k in nameIo:
    print(k)
