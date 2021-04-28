import sys
n = int(sys.stdin.readline())
route = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
dice = []
maxnum = 0
for x in range(n):
    dice.append(list(map(int,sys.stdin.readline().split())))
for i in range(6):
    sol = []
    temp = [1,2,3,4,5,6]
    temp.remove(dice[0][i])
    next = dice[0][route[i]]
    temp.remove(next)
    sol.append(max(temp))
    for j in range(1,n):
        temp = [1,2,3,4,5,6]
        temp.remove(next)
        next = dice[j][route[dice[j].index(next)]]
        temp.remove(next)
        sol.append(max(temp))
    sol = sum(sol)
    if maxnum < sol:
        maxnum = sol
print(maxnum)

    