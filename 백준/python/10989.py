import sys
n = int(sys.stdin.readline())
num_ls = [0] * 10001
for i in range(n):
    num = int(sys.stdin.readline())
    num_ls[num] = num_ls[num]+1
for k in range(10001):
    if num_ls[k] != 0:
        for j in range(num_ls[k]):
            print(k)