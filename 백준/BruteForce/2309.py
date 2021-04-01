import sys
key = []
for x in range(9):
    key.append(int(input()))
ksum = sum(key)
key.sort()
for i in range(9):
    for j in range(1,9):
        if (ksum - (key[i]+key[j])) == 100:
            for k in key:
                if k != key[i]:
                    if k!= key[j]:
                        print(k)
            sys.exit()