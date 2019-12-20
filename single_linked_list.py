# Implementation of single linked list


class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		curr = self.head
		self.head = new_node
		self.head.next = curr

	def insert_at_end(self, data):
		pass

	def insert_at_pos(self, pos, val):
		pass

	def reverse(self):
		pass

	def print_list(self):
		curr = self.head
		while curr:
			print(curr.data, end=' ')
			curr = curr.next
		print('\n')

	def search(self):
		pass


sll = LinkedList()
while True:
	print('Enter the choices')
	print('1: to add node at the beginning')
	print('2: to append the node at the end')
	print('3: to add the node after certain position')
	print('4: to reverse the linked list')
	print('5: to search an element in the list')
	print('6: to print the linked list')
	print('7: to exit')

	choice = int(input())

	if choice == 1:
		val = int(input('Enter the node value'))
		sll.insert_at_begin(val)
	elif choice == 2:
		val = int(input('Enter the node value'))
		sll.insert_at_end(val)
	elif choice == 3:
		val = int(input('Enter the node value'))
		pos = int(input('Enter the position for the node to insert'))
		sll.insert_at_pos(pos, val)
	elif choice == 4:
		sll.reverse()
	elif choice == 5:
		val = int(input('Enter the node value to search'))
		sll.search(val)
	elif choice == 6:
		sll.print_list()
	elif choice == 7:
		print('Exiting...')
		break
	else:
		print('Invalid Input')
		print('please enter correct input')
		continue
