word = list(map(str, input()))
list_w = list(word)
list_abc = list('abcdefghijklmnopqrstuvwxyz')
list_mn = [-1 for j in range(len(list_abc))]
for x in range(len(word)):
    if list_mn[list_abc.index(word[x])] == -1:
        list_mn[list_abc.index(word[x])] = x

for l in list_mn:
    print(l, end=" ")