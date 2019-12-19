# https://docs.python.org/3/library/argparse.html

import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='\
				performing the operation on the given two numbers')
	parser.add_argument('number1', 
				type=int, help='First Number')
	parser.add_argument('number2', 
				type=int, help='Second Number')
	parser.add_argument('operation', 
				type=str, help='Operation to be performed \
				add = addition \
				mul = multiplication \
				sub = subtraction \
				div = division')
	
	# all the command line args are collected in args
	args = parser.parse_args()
	
	print('arg1 is ', args.number1)
	print('arg2 is ', args.number2)
	print('operation to be performed is ', args.operation) # its string but still using, not needed
	
	result = None
	
	if args.operation == 'add':
		result = args.number1 + args.number2
	elif args.operation == 'mul':
		result = args.number1 * args.number2
	elif args.operation == 'sub':
		result = args.number1 - args.number2
	elif args.operation == 'div':
		result = args.number1 / args.number2
	else:
		result = 'Invalid Operation'
	
	print('solution is ', result)
		
# how to run the program
# python filename -h  for help
# python filename 10 20 (add/sub/mul/div)