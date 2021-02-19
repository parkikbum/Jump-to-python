list_n = []
b = 0
while 1:
    c = int(input())
    list_n.append(c)
    b = b + 1
    if b == 10:
        break
list_mod=[]
i=0

while 1:
    if list_n[i]%42 not in list_mod :
        list_mod.append(list_n[i]%42)
    i=i+1
    if i==10:
        break

print(len(list_mod))