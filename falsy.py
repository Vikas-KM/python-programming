from decimal import Decimal
from fractions import Fraction

# https://docs.python.org/3/library/stdtypes.html#truth-value-testing

a = Decimal(0)
print('Decimal ', bool(a))

b = Fraction(0, 1)
print('Fractional ', bool(b))

c = range(0)
print('range ', bool(c))

d = []
print('[] ', bool(d))

e = {}
print('{} ', bool(e))

f = set()
print('set() ', bool(f))

g = dict()
print('dict() ', bool(g))

h = ''
print("'' ", bool(h))

a = 10
b = 20
# not has a lower priority than non-Boolean operators, \
# so not a == b is interpreted as not (a == b), and a == not b is a syntax error.
# print(a == not b))


# The resultant value is a whole integer, though the result’s type is not necessarily int.\
# The result is always rounded towards minus infinity
print(1//2)
print(-1//2)
print(-1//-2)
print(1//-2)
print(pow(0,0))             # prints 1
print(0**0)                 # prints 1

n = 37
print(n.bit_length())       # bits required to represent the integer
print((0.0).is_integer())   # True
print((3.2).is_integer())   # False

print('gg' in 'eggs')       # returns True

lst = [[]] *3
print(lst)                  # [[], [], []]
lst[0].append(3)
print(lst)                  # [[3], [3], [3]]

# Work around for the above problem
lst1 = [[] for i in range(3)]
print(lst1)
lst1[0].append(3)
print(lst1)

# set
s = set('foobar')
print(s)
s = set(['a','b','foo'])
print(s)

# String templates
from string import Template

s = Template('$who eats $what')
print(s.substitute(who='vikas', what='cake'))
