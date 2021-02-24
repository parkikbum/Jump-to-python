cnt = 0
n = int(input())

for i in range(n):
    word = input()
    cnt += list(word) == sorted(word, key=word.find)

print(cnt)