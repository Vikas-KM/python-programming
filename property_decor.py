'''
    Programming explaining the property decorator

    https://www.youtube.com/watch?v=jCzT9XFZ5bw
'''


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')


e = Employee('John', 'Doe')
e.first = 'Jackson'
e.fullname = 'Marget Thacter'
print(e.first)
print(e.last)
print(e.email)
print(e.fullname)
