while 1:
    n = input()

    if n == '.':
        flage = False
        break
    stack = []
    flag = True

    for x in n:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag=False
                break
    if flag and not stack:
        print("yes")
    else:
        print("no")