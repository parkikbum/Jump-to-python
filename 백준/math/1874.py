stack = []
num =[]
cnt = 0
last = 0
sol = []
temp = True
def push(self):
    return stack.append(self)
def pop():
    return stack.pop(len(stack)-1)
n = int(input())
for x in range(n):
    num.append(int(input()))
while num:
    if cnt > num[0] and stack[len(stack) - 1] != num[0]:
        temp = False
        break
    if len(stack) == 0:
        for l in range(cnt+1, num[0]+1):
            push(l)
            sol.append('+')
            cnt = cnt+1
    else:
        if stack[len(stack)-1] == num[0]:
            last = pop()
            num.pop(0)
            sol.append('-')
        else:
            for y in range(cnt+1, num[0]+1):
                push(y)
                sol.append('+')
                cnt = cnt+1
if temp == False:
    print('NO')
else:
    for m in sol:
        print(m)