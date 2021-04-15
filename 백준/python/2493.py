import sys
from collections import deque

n = int(input())
tower = deque(map(int, input().split()))
stack = deque()
sol = [0]*n
for i in range(n-1, -1, -1):
    while stack and tower[stack[-1]] < tower[i]:
        sol[stack.pop()] = i+1
    stack.append(i)
print(*sol)