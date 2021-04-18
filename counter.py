import operator
from collections import Counter
from functools import cache
from itertools import accumulate

c = Counter('gallahad')                 # a new counter from an iterable
print(c)
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
print(c)
c = Counter(cats=4, dogs=8)         # a new counter from keyword args
print(c)
c = Counter()                           # a new, empty counter
print(c)
c = Counter(['eggs', 'ham'])
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))

print(Counter('abracadabra').most_common(3))


lst = [1,2,3,4,5,6,7,8,0,8,8,6,4,2]
l_add = list(accumulate(lst, operator.add))
l_mul = list(accumulate(lst, operator.mul))
print(l_add)
print(l_mul)


# Feature of python 3.9
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(10))
print(factorial(5))