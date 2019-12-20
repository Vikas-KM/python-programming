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
		new_node = Node(data)
		curr = self.head
		if self.head is None:
			self.head = new_node
		while curr.next:
			curr = curr.next
		curr.next = new_node

	def insert_at_pos(self, pos, data):
		new_node = Node(data)
		curr = self.head
		if self.head is None:
			print('Empty list found')
			self.head = new_node
			return
		count = 1
		while curr:
			if count == pos:
				temp = curr.next
				curr.next = new_node
				new_node.next = temp
				return
			curr = curr.next
			count += 1
		print('position not found')
		return

	def reverse(self):
		pass

	def search(self):
		pass

	def print_list(self):
		curr = self.head
		while curr:
			print(curr.data, end=' ')
			curr = curr.next
		print('\n')


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

	try:
		choice = int(input())
	except ValueError:
		print('OOPS wrong input')
		continue

	if choice == 1:
		val = int(input('Enter the node value'))
		sll.insert_at_begin(val)
	elif choice == 2:
		val = int(input('Enter the node value'))
		sll.insert_at_end(val)
	elif choice == 3:
		val = int(input('Enter the node value'))
		pos = int(input('Enter position for node to insert, beginning at 1'))
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
