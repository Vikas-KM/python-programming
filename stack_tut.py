# implementation of stack programming using double linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        print('pushed node ', new_node.data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        curr = self.tail
        self.tail.next = new_node
        new_node.prev = curr
        self.tail = new_node

    def pop(self):
        if self.head is None:
            print('Nothing to pop, empty stack')
            return
        del_node = self.tail
        temp = self.tail.prev
        if temp is None:
            self.head = None
            self.tail = None
            print('deleted node ', del_node.data)
            return
        self.tail = temp
        self.tail.next = None
        print('deleted node ', del_node.data)

    def size(self):
        curr = self.head
        count = 0
        if self.head is None:
            print(' stack size is ', count)
            return
        while curr != self.tail.next:
            count += 1
            curr = curr.next
        print(' stack size is ', count)

    def is_empty(self):
        if self.head is None:
            print('Yes, stack is empty')
            return
        print(f'No, stack is not empty')


stk = Stack()
stk.is_empty()
stk.push(1)
stk.push(2)
stk.push(3)
stk.is_empty()
stk.size()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.is_empty()
stk.size()
