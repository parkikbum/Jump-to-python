l = int(input())
mjy = input()
sol = 0
for x in range(l):
    sol = sol + (ord(mjy[x])-96) * (31 ** x)
print(sol % 1234567891)
