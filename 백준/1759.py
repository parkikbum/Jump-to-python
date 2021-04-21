import sys
l,c = map(int, sys.stdin.readline().split())
passWord = list(map(str, sys.stdin.readline().split()))
passWord.sort(key = lambda x : x[0])
while 1:
    for i in range(l):
        print(passWord[i], end="")
    passWord.append(passWord.pop(3))
        

