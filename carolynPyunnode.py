###
# CS 3C Advanced Data Structures and Algorithms in Python
# Application: Node Class
# Solution File: carolynPyunnode.py
# Date:  1/25/22
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata
        return True

    def setNext(self,newnext):
        self.next = newnext
        return True
