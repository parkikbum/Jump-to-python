n = int(input())
def fc(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n * fc(n-1)
print(fc(n))