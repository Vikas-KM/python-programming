# create two sorted lists

class Node:
    def __init__(self, data=None):
        self.data=data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end='->')
            curr = curr.next
        print('end')

# method 1 using while loop in O(n) 
def merger(list_a, list_b):
    new_list = LinkedList()
    curr = new_list

    while True:
        if list_a is None and list_b is None:
            break
        elif list_a is None:
            while list_b is not None:
                temp = Node(list_b.data)
                new_list.next = temp
                new_list = new_list.next
                list_b = list_b.next
        elif list_b is None:
            while list_a is not None:
                temp = Node(list_a.data)
                new_list.next = temp
                new_list = new_list.next
                list_a = list_a.next
        elif list_a.data <= list_b.data:
            temp = Node(list_a.data)
            new_list.next = temp
            new_list = new_list.next
            list_a = list_a.next 
        else:
            temp = Node(list_b.data)
            new_list.next = temp
            new_list = new_list.next
            list_b = list_b.next     
    return curr.next   


first_list = LinkedList()
first_list.append(2)
first_list.append(3)
first_list.append(5)
first_list.append(10)
first_list.append(20)
first_list.print_list()

second_list = LinkedList()
second_list.append(1)
second_list.append(4)
second_list.append(8)
second_list.append(15)
second_list.append(25)
second_list.print_list()

merge_list = LinkedList()
merge_list.head = merger(first_list.head, second_list.head)
merge_list.print_list()
