word = input().upper()
word_list = list(word)
word_unique = list(set(word))
cnt = []
i = 0
for x in word_unique:
    cnt.append(word_list.count(x))
    i = i + 1
if cnt.count(max(cnt)) == 1:
    print(word_unique[(cnt.index(max(cnt)))])
else:
    print("?")


