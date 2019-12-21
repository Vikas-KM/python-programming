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
            print('Nothing to pop, empty list')
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


stk = Stack()
stk.push(1)
stk.push(2)
stk.pop()
stk.pop()
stk.pop()
