k = int(input())
num = []
n = 0
for x in range(k):
    n = int(input())
    if n == 0:
        num.pop(len(num)-1)
    if n != 0:
        num.append(n)
print(sum(num))
