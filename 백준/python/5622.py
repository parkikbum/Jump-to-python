apb = str(input())
list_n = list(apb)
num = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_n = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10,10]
sum = 0
for x in list_n:
    if x in num:
        sum = sum + num_n[num.index(x)]
print(sum)