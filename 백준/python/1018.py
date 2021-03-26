n,m = map(int, input().split())
result,lst,lst_8 = [],[],[]
ck = []
def minimum(lst8):
    ckw = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    ckb = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    sum_a,sum_b = 0,0
    for i in range(8):
        for j in range(8):
            if lst8[i][j] != ckw[i][j]:
                sum_a = sum_a + 1
            if lst8[i][j] != ckb[i][j]:
                sum_b = sum_b + 1
    return min(sum_a,sum_b)

for i in range(n):
    lst.append(input())
for j in range(n-8+1):
    for k in range(m-8+1):
        for l in range(8):
            lst_8.append(lst[j+l][k:k+8])
        result.append(minimum(lst_8))
        lst_8 = []
print(min(result))