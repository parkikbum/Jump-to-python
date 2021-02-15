l = int(input())
list_s = []
list_c = []
a = 0
b = 0
while 1:
    list = [ int(x) for x in input().split() ]
    l = l - 1
    list_s.insert( a, (list[0] + list[1]))
    list_c.insert(b, list[0])
    list_c.insert(b+1,list[1])
    a = a+1
    b = b+2
    if l ==0:
        break;

i = 1
j = 0
for x in list_s:
    print("Case #%d: %d + %d = %d"%(i,list_c[j],list_c[j+1],x))
    i = i+1
    j = j+2