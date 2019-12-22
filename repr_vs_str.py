# __str__ vs __repr__

class Car:
    def __init__(self, color, mileage):
        self.color=color
        self.mileage = mileage
    
    # print and it returns always string
    # for easy to read representation
    def __str__(self):
        return '__str__ : a {self.color} car with {self.mileage} mileage'.format(self=self)

    # typing mycar in console calls this
    # unambiguous
    # for internal use, for developers
    def __repr__(self):
        return '__repr__ :a {self.color} car with {self.mileage} mileage'.format(self=self)

my_car = Car('red', 123)

# see which methods they are calling
# comment __STR__ method see what is the ouput again
print(my_car)
print(str(my_car))
print('{}'.format(my_car))
print(repr(my_car))
