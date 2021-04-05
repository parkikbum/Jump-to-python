import sys
n,m = map(int, sys.stdin.readline().split())
pk_num = 1
pkmon_s = {}
pkmon_n = {}
for x in range(n):
    name = str(sys.stdin.readline().strip())
    pkmon_s[pk_num] = name
    pkmon_n[name] = pk_num
    pk_num = pk_num + 1
for k in range(m):
    pkmon = sys.stdin.readline().strip()
    if pkmon in pkmon_n:
        print(pkmon_n[pkmon])
        continue
    else:
        print(pkmon_s[int(pkmon)])
        continue
        