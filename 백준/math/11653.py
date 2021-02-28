n =int(input())
x = 2
while 1:
    if n%x ==0:
        n=n//x
        print(x)
    if n%x !=0:
        x = x+1
    if n == 1:
        break