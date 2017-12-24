# implement a linked list with insert and delete methods


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.current = None

    def add_node(self, data):
        new = Node()
        new.data = data
        new.next = self.current
        self.current = new

    def delete_node(self, node):
        self.current.next = node.next

    def list_print(self):
        node = self.current
        while node:
            print node.data
            node = node.next
