n = int(input())
stack = []
cmd = []
sol = []
def push(self):
    stack.append(self)
    return
def pop():
    if len(stack) == 0:
        return sol.append(-1)
    else:
        return sol.append(stack.pop(len(stack)-1))
def size():
    return sol.append(len(stack))
def empty():
    if len(stack) == 0:
        return sol.append(1)
    else:
        return sol.append(0)
def top():
    if len(stack) == 0:
        return sol.append(-1)
    else:
        return sol.append(stack[len(stack)-1])
for x in range(n):
    cmd = [str(i) for i in input().split()]
    if cmd[0] == 'push':
        push(cmd[1])
        cmd.pop(0)
        cmd.pop(0)
    elif cmd[0] == 'pop':
        pop()
        cmd.pop(0)
    elif cmd[0] == 'size':
        size()
        cmd.pop(0)
    elif cmd[0] == 'empty':
        empty()
        cmd.pop(0)
    elif cmd[0] == 'top':
        top()
        cmd.pop(0)
for k in sol:
    print(k)

