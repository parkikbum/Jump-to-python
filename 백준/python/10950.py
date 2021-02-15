l = int(input())
list_s = []
a = 0
while 1:
    list = [ int(x) for x in input().split() ]
    l = l - 1
    list_s.insert( a, (list[0] + list[1]))
    a = a+1
    if l ==0:
        break;


for x in list_s:
    print(x)