k,n = map(int, input().split())
lan = []
for x in range(k):
    lan.append(int(input()))
start = 1
end = max(lan)
mid = 0
sol = 0
while start <= end:
    cnt = 0
    mid = (start+end)//2
    for x in lan:
        cnt = cnt + x//mid
    if cnt >=n:
        start = mid + 1
        sol = mid
    else:
        end = mid -1
print(sol)