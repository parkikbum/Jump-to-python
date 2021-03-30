n,m = map(int, input().split())
visited = [False] * n
out = []
def solve(depth,a,m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(a, len(visited)):
        visited[i] = True
        out.append(i+1)
        solve(depth+1, i,m)
        visited[i] = False
        out.pop()
solve(0,0,m)