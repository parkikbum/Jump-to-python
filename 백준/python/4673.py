num = set(range(1,10001))
not_self = set()

for a in range(1,10001):
    for b in str(a):
        a = a + int(b)
    not_self.add(a)
self = num - not_self
self = sorted(self)
for c in self:
    print(c)