import sys
arr = list(map(str, sys.stdin.readline().rstrip()))
arr2 = list()
m = int(sys.stdin.readline())
cs = len(arr)
for x in range(m):
    cmd = list(str(sys.stdin.readline().rstrip()))
    if cmd[0] == 'L' and arr != []:
        arr2.append(arr.pop())
    elif cmd[0] == 'D' and arr2 != []:
        arr.append(arr2.pop())
    elif cmd[0] == 'B' and arr != []:
        arr.pop()
    elif cmd[0] == 'P':
        arr.append(cmd[2])
for i in arr:
    print(i , end='')
for k in reversed(arr2):
    print(k, end='')