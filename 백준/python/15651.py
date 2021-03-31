n,m = map(int, input().split())
visited = [False] * n
out = []
out_a = []
def solve(depth,n,m):
    if depth == m:
        out_str = ' '.join(map(str, out))
        out_a.append(out_str)
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = False
            out.append(i+1)
            solve(depth+1, n,m)
            visited[i] = False
            out.pop()
solve(0,n,m)
for k in out_a:
    print(k)
    