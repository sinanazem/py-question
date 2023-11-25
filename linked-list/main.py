list_ = [92, 97, 21, 79]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = None
        
first_node = Node(92)
second_node = Node(97)
third_node = Node(21)
fourth_node = Node(79)