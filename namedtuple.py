# why namedtuple ?
# readable, and dictionary is verbose

# WITHOUT namedtuple
# we have a color tuple with RGB

Color =(55,155,255)
print(Color[0]) # prints red color
print(Color[1]) # prints green color

# ABOVE code is not readable down the line after
# few months when we check back

#Alternative is dictionary

Color = {'red': 55, 'green': 155, 'blue': 255}
print(Color['red'])
print(Color['green'])
# print(Color.red) can't be used

# ABOVE replacement is clear but verbose and need to
# change when you need to add, also dot syntax is not usable in dictionary

# BELOW NamedTuples

from collections import namedtuple

Color = namedtuple('Color',['red','green','blue'])
color = Color(55,155,255)

print(color[0])
print(color.red)

# Above code is readble and easy

