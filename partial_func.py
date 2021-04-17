from functools import partial


def multiply(x, y):
    return x * y


db1 = partial(multiply, 2)
print(db1(3))
