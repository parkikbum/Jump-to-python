x = int(input())
sum = 0
for i in range(1,10000000):
    sum = i + sum
    if x <= sum:
        if i%2 == 1:
           print((sum-x+1), '/',i-(sum-x),sep="")
           break
        else:
            print(i-(sum-x), '/', (sum-x+1),sep="")
            break

