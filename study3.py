#입력출력연습문제
#1번문제
def is_odd(n):
    if int(n)%2 == 0:
        print("%d는 짝수입니다." %int(n))
    else:
        print("%d는 홀수입니다." %int(n))

print("자연수를 입력해주세요 : ")
n = input()
is_odd(n)

#2번문제
a = 1
b = 0
while(1):
    print("평균값을 구할 자연수를 입력해주세요 :   (종료하고 싶으시면 q을 입력해주세요.)")
    n = input()
    if n == 'q':
        break

    b = b + int(n)
    print("평균값 : %d" %int(b/a))
    a = a + 1

#3번문제
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" %int(total))


#4번문제

#print("you" "need" "python")
#print("you"+"need"+"python")
#print("you", "need", "python")
#print("".join(["you", "need", "python"]))

#5번문제
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
data = f2.read()
print(data)
f2.close()

#6번문제
f1 = open("test.txt", 'a')
input1 = input("저장할 내용을 입력해주세요.")
f1.write("\n" + input1)
f1.close()


#7번문제
import textwrap
f1 = open("test.txt", 'r')
origin = f1.read()
f1.close()
print(origin)
input1 = input("바꾸고싶은 단어를 입력하세요 : ")
input2 = input("바꿀 단어를 입력하세요 :")
origin = origin.replace(input1, input2)
print(origin)

f2 = open("test.txt" , 'w')
f2.write(origin)
f2.close()

