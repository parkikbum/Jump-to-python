sub = int(input())
list_score = [int(x) for x in input().split()]
max = max(list_score)
sum = 0
i = 0
for z in list_score:
    sum = sum + z/max*100

print(round(sum/sub, 2))
