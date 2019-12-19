# decorator example
# finding the division of zero error in code itself

def div_smart(func):
	# inner will take args as many as the decorating func
    def inner(a,b):
        if b==0:
            return 'Division by zero found'
        return func(a,b)
    return inner
    
# decorating func	
@div_smart
def div(a,b):
    return a/b

print(div(4,0))
print(div(4,2))
