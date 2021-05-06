import sys
n = int(sys.stdin.readline())
cnt = 0
k = 1
num = 1000 - n
while num >= 500:
    num= num - 500
    cnt = cnt + 1
while num >= 100:
    num= num - 100
    cnt = cnt + 1
while num >= 50:
    num = num - 50
    cnt = cnt + 1
while num >= 10:
    num = num - 10
    cnt = cnt + 1
while num >= 5:
    num = num - 5
    cnt = cnt + 1
while num >= 1:
    num = num - 1
    cnt = cnt + 1
print(cnt)
        
