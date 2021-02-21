list_m = [str(x) for x in input().split()]
list_m1 = list(list_m[0])
list_m2 = list(list_m[1])
list_m1.reverse()
list_m2.reverse()
lm1 = ''.join(list_m1)
lm2 = ''.join(list_m2)
if int(lm1) > int(lm2):
    print(lm1)
else:
    print(lm2)