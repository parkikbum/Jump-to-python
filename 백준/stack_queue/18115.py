import sys
from collections import deque
n = int(sys.stdin.readline())
stack = deque(list())
process = []
process = list(map(int, sys.stdin.readline().split()))
cnt = 1
before = 0
for i in reversed(process):
    if i == 1:
        stack.appendleft(cnt)
        cnt = cnt + 1
    elif i == 2:
        if len(stack) > 0:
            before = stack.popleft()
            stack.appendleft(cnt)
            stack.appendleft(before)
            cnt = cnt + 1
        else:
            stack.append(cnt)
            cnt = cnt + 1
    elif i == 3:
        stack.append(cnt)
        cnt = cnt + 1
for x in stack:
    print(x , end=" ")