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


def multipliers1():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers1()])


def multipliers2():
    for i in range(4): yield lambda x: i * x


print([m(2) for m in multipliers2()])


def multipliers3():
    return [lambda x, i=i: i * x for i in range(4)]


print([m(2) for m in multipliers3()])


def multipliers4():
    return (lambda x: i * x for i in range(4))


print([m(2) for m in multipliers4()])


def foo(k):
    k = [1]


q = [0]
foo(q)
print(q)


