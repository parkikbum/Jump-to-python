import sys
from collections import deque
queue = deque()
N = int(input())
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        queue.append(int(a[1]))
    elif a[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])