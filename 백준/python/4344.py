r = int(input())
student = 0
i = 0
eve = 0
while 1:
    if i == r:
        break
    list_s = [int(x) for x in input().split()]
    for x in list_s:
        eve = eve + x
    eve = eve - list_s[0]
    eve = eve/list_s[0]
    for z in list_s:
        if z != list_s[0]:
            if z > eve:
                student = student + 1
    eve_1 =format(round(student/list_s[0]*100, 3) , '.3f')
    print(eve_1+'%')
    i = i+1
    list_s.clear()
    eve = 0
    student =0
