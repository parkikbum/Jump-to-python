#자료형 관련 연습문제
#1번문제
K = 80
E = 75
M = 55

ave = (K+E+M)/3

print("홍길동님의 평균점수는 %f 입니다." %ave )

#2번문제

a = 143215235246

def define_N (a):
    if(a%2)>0:
        return 0;
    else:
        return 1;
if(define_N(a) > 0):
    print("%d은(는) 짝수입니다." %a)
else:
    print("%d은(는) 홀수입니다." %a)

#3번문제
h = "881120-1068234"
print("%s" %h)
print("YYYYMMDD : 19%s" %h[:6] + " 뒷자리 %s" %h[7:])

#4번문제
pin = "881120-1068234"
print ("성별을 나타내는 숫자 %s" %pin[7])

#5번문제
a1 = "a:b:c:d"
print(a1)
print(a1.replace(":" , "#"))

#6번문제 그냥 sorting함
a2 =[1,3,5,4,2]
a2.sort()
a2.reverse()
print(a2)

#7번문제
a3 =['life', 'is', 'too', 'short']
a4 = ' '.join(a3)
print(a4)

#8번문제
t1 = (1,2,3)
t1 = (1,2,3) + (4,)
print(t1)

#9번문제
d = dict()
d
{}

#1. d['name'] = 'python'
#2. d[('a', )] = 'python'
#3. d[[1]] = 'python'  (안됨) key값으로는 변하지 않는 값을 사용해야함. 근데 list는 변할수 있기때문에 안됨
#4. a[250] = 'python'

#10번문제
a10 = {'A':90, 'B':80, 'C':70}
print(a10.pop('B')) #pop하면 값 사라짐
print(a10)

#11번문제
a11 = [1,1,1,2,2,3,3,3,4,4,5]
a11Set = set(a11)
b11 = list(a11Set)
print(b11)

#12번문제
a13 = b13 = [1, 2, 3]
a13[1] = 4
print(b13)

#a13과 a14의 변수는 모두 동일한 [1,2,3]이라는 리스트 객체를 가리키고있기 때문이다.

