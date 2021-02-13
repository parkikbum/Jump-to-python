list = [ int(x) for x in input().split() ]

if list[1]>= 45:
    print(list[0], list[1]-45)

elif (list[0] == 0) & (list[1] >= 45) :
    print(list[0], list[1]-45)

elif (list[0] == 0) & (list[1] <45):
    print(23, (list[1]+60)-45)

else:
    h2 = list[0]-1
    m2 = (list[1]+60)-45
    print(h2, m2)

