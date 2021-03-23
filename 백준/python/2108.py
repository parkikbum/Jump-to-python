import sys
from collections import Counter
n = int(sys.stdin.readline())
data = []
my_sum = 0
for i in range(n) :
    temp = int(sys.stdin.readline())
    data.append(temp)
    my_sum += temp
print('%.0f' % (my_sum/n))
if n == 1:
    print(data[0])
    print(data[0])
    print(0)
    sys.exit()
data = sorted(data)
print(data[n//2])
cnt = Counter(data)
cnt = sorted(cnt.items(), key=lambda x: (-x[1],x[0]))
if cnt[0][1] == cnt[1][1] :
    print(cnt[1][0])
else :
    print(cnt[0][0])
print(data[-1]-data[0])