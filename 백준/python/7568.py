n = int(input())
dc = []
for k in range(n):
    x,y = map(int, input().split())
    dc.append((x,y))
grade = []
for l in range(n):
    grade.append(int(1))
for i in range(n):
    for j in range(i+1, n):
        if dc[i][0] < dc[j][0] and dc[i][1] < dc[j][1]:
            grade[i] = grade[i] + 1
        elif dc[i][0] > dc[j][0] and dc[i][1] > dc[j][1]:
            grade[j] = grade[j] + 1
for a in grade:
    print(a,end=" ")