n = int(input())
is_han = 0
if n<100:
    for x in range(1,n+1):
        is_han = is_han + 1

if n >= 100:
    is_han = 99
    for c in range(100,n+1):
        a = str(c)
        list_num = list(a)
        if (int(list_num[0]) - int(list_num[1])) == (int(list_num[1])-int(list_num[2])):
            is_han = is_han + 1

print(is_han)


