import sys
t = int(sys.stdin.readline())
rank = []
cnt = 1
for i in range(t):
    n = int(sys.stdin.readline())
    for k in range(n):
        document,interview = map(int, sys.stdin.readline().split())
        rank.append((document,interview))
    rank = sorted(rank, key = lambda x : x[0])
    max_value = rank[0][1]
    for j in range(1, n):
        if max_value > rank[j][1]:
            cnt = cnt + 1
            max_value = rank[j][1]
    print(cnt)
    rank = []
    cnt = 1