#5장 연습문제
import sys
import time
import random

#1번문제
class UpgradeCalculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
cal.minus(7)
print(cal.value)

#2번문제
class MaxLimitCalculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value =100



cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)


#3번 문제
print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')

#4번문제

print(list(filter(lambda x: x>0, [1,-2,3,-5,8,-3])))


#5번문제
print(int('0xea', 16))

#6번문제
print(list(map(lambda x: x*3, [1,2,3,4])))

#7번문제
a = [-8,2,7,5,-3,5,0,1]
print(max(a) * min(a))

#8번문제
a = round(17/3, 4)
print(a)

#12번문제
print(time.strftime('%y/%m/%d %X', time.localtime(time.time())))

#13번 문제
#1~45사이의 숫자 6개
a = list(range(1,46))

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = list(range(1, 46))
    i = 0
    while data:
        print(random_pop(data))
        i=i+1
        if i ==6:
            break

