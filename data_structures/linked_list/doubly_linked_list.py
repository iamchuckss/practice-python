from __future__ import print_function


class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, data):
        if self.isEmpty():
            self.head = Node(data, None, None)
            self.tail = self.head
        self.head.prev = Node(data, None, self.head)   # new <-> currenthead
        self.head = self.head.prev                     # new(head) <-> oldhead


    def insertTail(self, data):
        if self.isEmpty():
            self.tail = Node(data, None, None) 
            self.head = self.tail
        self.tail.next = Node(data, self.tail, None)   # currenttail <-> new
        self.tail = self.tail.next                     # oldtail <-> new(tail)
    
    def deleteHead(self):
        if self.isEmpty():
            return None
        temp = self.head.data
        self.head = self.head.next                     # currenthead <-> 2nd
        self.head.prev = None                          # oldhead -> 2nd(head)

        if self.head is None:
            self.tail = None  
        return temp
    
    def deleteTail(self):
        if self.isEmpty():
            return None
        temp = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        if self.tail is None:
            self.head = None
        return temp

    def isEmpty(self):
        return self.head is None

    def delete(self, target):
        curr = self.head

        while curr is not None and curr.data != target:
            curr = curr.next
        
        if curr == self.head:
            self.deleteHead()
        elif curr == self.tail:
            self.deleteTail()
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
        print()

class Node:
    def __init__(self, data, prev, next):
        self.prev = prev
        self.next = next
        self.data = data
