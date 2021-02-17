max = int(input())
list=[max]
for i in range(8):
    a=int(input())
    list.append(a)
    if a >= max:
        max=a
print(max)
print(int(list.index(max))+1)