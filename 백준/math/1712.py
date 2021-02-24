import sys
price = [int(x) for x in sys.stdin.readline().split()]
if price[2] <= price[1]:
    print("-1")
else:
    sum = price[0] // (price[2] - price[1])
    print(sum+1)