import sys
n,m = map(int, input().split())
tree = [int(x) for x in input().split()]
start = 1
end = max(tree)
while start <= end:
    mid = (start+end)//2
    sum = 0
    for i in tree:
        if i>= mid:
            sum = sum + i - mid
    if sum>=m:
        start = mid+1
    else:
        end = mid - 1
print(end)