n =int(input())
card = [int(x) for x in range(1,n+1)]
top = 0
while n-1>0:
    n = n-1
    top = top + 2
    card.append(card[top-1])
print(card[top])