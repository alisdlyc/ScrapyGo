from collections import Iterable

for c in 'alisdlyc':
    print(c)

for i, value in enumerate(['A', 'B', 'C']):
    print('%d ---> %s' % (i, value))

print(isinstance([1, 2, 3], Iterable))  # list是否可迭代)
print(isinstance('qwq', Iterable))  # list是否可迭代)
