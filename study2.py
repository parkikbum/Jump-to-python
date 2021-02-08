#제어문 연습문제

#1번문제
#shirt

#2번문제
n = 1
sum =0
while n<=100:
    if n%3 == 0:
        print(n)
        sum = sum+n
        n=n+1
    else:
        n=n+1

print(sum)

#3번문제
n = 1
while n:
    if n == 1:
        print("*")
        n = n+1
    elif n == 2:
        print("**")
        n = n + 1
    elif n == 3:
        print("***")
        n = n + 1
    elif n == 4:
        print("****")
        n = n + 1
    elif n == 5:
        print("*****")
        break

#4번문제
n = 1
a = []
b = 1
while n<=100:
    a.insert(n,n)
    n = n+1

for b in a:
    if b<=100:
        print(b)
    else:
        break

#5번문제
f_score =[70, 65, 55, 75, 95, 90, 80, 80, 85, 100]
n = 0
eve = 0
score2 = 0
for score in f_score:
    n = n + 1
    score2 = score2 + score

eve = score2/n
print(eve)

#6번문제
numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num%2 == 1]

print(result)