import sys
import heapq
n = int(sys.stdin.readline())
study = []
sol = []
for x in range(n):
    p,d = map(int, sys.stdin.readline().split())
    study.append([p,d])
study.sort(key= lambda k : k[1])
for i in study:
    heapq.heappush(sol, i[0])
    if len(sol) > i[1]:
        heapq.heappop(sol)
print(sum(sol))
