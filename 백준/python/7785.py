import sys
n = int(sys.stdin.readline())
name_io = []
for x in range(n):
    name_io.append(map(int, (sys.stdin.readline().split())))
for k in len(name_io):
    name_io.count(name_io[k][0]) 


