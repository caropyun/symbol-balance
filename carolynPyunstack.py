###
# CS 3C Advanced Data Structures and Algorithms in Python
# Application: Stack Class
# Solution File: carolynPyunstack.py
# Date:  1/25/22
#

from carolynPyunnode import Node


class Stack:

    # head default None
    def __init__(self):
        self.head = None

    # Add data to stack, add to start of stack
    def push(self, item):
        if self.head is None:    # if first one
            self.head = Node(item)
        else:   # add and update
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp

    # Remove current head
    def pop(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            self.head = self.head.getNext()
            symbol = current.getData()
            current.next = None
            return symbol

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.getDate()

    # Check if stack is empty
    def is_empty(self):
        return self.head is None

    @classmethod
    def create_stack(cls):
        """Creates stack"""
        return Stack()

    def delete_stack(self):
        temp = self.head
        while temp is not None:
            temp = self.pop()







