# function to flatten list of list

import itertools
import operator
from functools import reduce

list_2d = [[1, 2, 3], [4, [5, 6]], [7], [8, 9]]

merged = list(itertools.chain(*list_2d))
y = sum(list_2d, [])
x = reduce(operator.concat, list_2d)

print(merged)
print(y)
print(x)

out = []


def flatten(lst):
    for i in lst:
        if type(i) == list:
            flatten(i)
        else:
            out.append(i)


flatten(list_2d)
print(out)
