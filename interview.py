d = {
    'age': 34
}
print(f"{d['age']} is old")
try:
    print(f'{d.age} is old')  # gives error
except AttributeError:
    print('Attribute Error')
print('{age} is old'.format(**d))

s = 'blah123'
print(s.islower())  # prints True
print(s.islower() and s.isalpha())  # prints False

lst = [1, 2, 3]
# lst.remove()

s = {1, 2, 3}
s.update((4, 5, 6, 7))
print(s)

print(globals())  # prints the globals
x = 10


def func():
    x = 20
    print(x)
    print(globals()['x'])


func()

even_numbers = list(map(lambda x: x % 2 == 0, lst))
print(even_numbers)

for i in even_numbers:
    print(i)

from functools import reduce

val = reduce(lambda x, y: x + y, lst)
print(val)


def multipliers_1():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers_1()])


def multipliers_2():
    for i in range(4): yield lambda x: i * x


print([m(2) for m in multipliers_2()])


def multipliers_3():
    return [lambda x, i=i: i * x for i in range(4)]


print([m(2) for m in multipliers_3()])


def multipliers_4():
    return (lambda x: i * x for i in range(4))


print([m(2) for m in multipliers_4()])


def foo(k):
    k = [1]


# CAP WORDS

import string

s = 'The quick brown fox jumped over the lazy dog.'

print(string.capwords(s))

values = {
    'name': 'vikas',
    'loves': 'python'
}

# STRING TEMPLATES
t = string.Template('my name is $name and loves $loves')

print(t.substitute(values))
try:
    x = string.Template('my name is $name1 and loves $loves1')
    print(x.substitute(values))
except KeyError as err:
    print('ERROR ', str(err))

x = string.Template('my name is $name and loves $loves1')
print(x.safe_substitute(values))