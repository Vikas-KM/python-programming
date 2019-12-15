# function to flatten list of list

import itertools
import operator
from functools import reduce

list2d = [[1,2,3], [4,[5,6]], [7], [8,9]]

merged = list(itertools.chain(*list2d))
y = sum(list2d,[])
x=reduce(operator.concat,list2d)

print(merged)
print(y)
print(x)

out=[]
def flatten(lst):
    for i in lst:
        if type(i) == list:
            flatten(i)
        else:
            out.append(i)

flatten(list2d)
print(out)