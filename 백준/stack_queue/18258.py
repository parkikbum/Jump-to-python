import sys
from collections import deque
n = int(sys.stdin.readline())
arr = deque()
cmd = []
for x in range(n):
    cmd = list(sys.stdin.readline().rsplit())
    if cmd[0] == 'push':
        arr.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif cmd[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])