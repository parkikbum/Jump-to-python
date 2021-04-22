import sys
from itertools import combinations
mouem = ['a','e','i','o','u']
sol = []
l,c = map(int, sys.stdin.readline().split())
passWord = list(map(str, sys.stdin.readline().split()))
passWord.sort(key = lambda x : x[0])

for i in combinations(passWord, l):
    word = ''.join(i)
    vFlag = False
    cFalg = 0
    for i in word:
        if i in mouem:
            vFlag = True
        else:
            cFalg = cFalg + 1
    if vFlag == True and cFalg >=2:
        sol.append(word)
print('\n'.join(sol))