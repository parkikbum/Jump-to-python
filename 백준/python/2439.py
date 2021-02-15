n = int(input())
list_n = [x for x in range(1,n)]
list_n.reverse()
f =0
for a in range(1 , n+1):
    for c in list_n:
        print(end = " ")
    for b in range(1,a+1):
        print("*" , end="")

    print("")
    if list_n.count(1) == 0 :
        print("")
    else:
        list_n.pop(f)