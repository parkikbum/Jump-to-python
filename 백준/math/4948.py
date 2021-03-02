list_p = [True] * (2*123456+2)
list_p[0]=list_p[1]=False

for i in range(2, int((2*123456+1)**0.5)+1) :
    if list_p[i]:
        for k in range(2*i , 2*123456+1, i):
            list_p[k] = False
while 1:
    x=int(input())
    if x == 0:
        break
    print(sum(list_p[x+1:2*x+1]))