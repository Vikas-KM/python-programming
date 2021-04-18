class Employee:

    pay_raise = 1.05    # 5% pay rise

    def __init__(self, first_name, last_name, salary ):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    def apply_raise(self):
        self.salary = int(self.salary * self.pay_raise)
