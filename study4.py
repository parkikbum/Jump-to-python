#파이썬 날개달기
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
print(cal.value)

#2번문제
