import sys
r = int(input())
i = 0
b = 0
a = 2
cm = 0
score = 0
score_list =[]
while 1:
    score_a = input()
    list_s = list(score_a)
    for c in list_s:
        if c == 'O':
            if cm == 'O':
                score = score + a
                a = a+1
            else:
                score = score + 1
                cm = c
                a = 2
        else:
            cm = 0
    score_list.append(score)
    list_s.clear()
    b = b + 1
    a = 2
    cm = 0
    score = 0
    i = 0
    if r == b:
        break
for z in score_list:
    print(z)