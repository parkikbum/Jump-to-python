import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
arr = deque(range(1, n+1))
sol = []
k = k - 1
while 1:
    if len(arr) == 0:
        break
    arr.rotate(-k)
    sol.append(arr[0])
    arr.popleft()
print('<'+", ".join(map(str, sol))+'>')
