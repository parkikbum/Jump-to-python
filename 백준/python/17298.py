import sys
n = int(sys.stdin.readline())
a = []
a = list(map(int, sys.stdin.readline().split()))
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        a[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)
while stack:
    a[stack[-1]] = -1
    stack.pop()
for i in a:
    print(i, end=' ')