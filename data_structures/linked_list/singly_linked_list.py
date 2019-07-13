from __future__ import print_function


class Node:
    def __init__(self, data, next):
        self.next = next
        self.data = data

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        self.head = Node(data, self.head)
        
    def insert_tail(self, data):
        curr = self.head;
        while (curr.next is not None):
            curr = curr.next
        curr.next = Node(data, None)

    def delete_head(self):
        if self.head is None:
            return None
        curr = self.head.data
        self.head = self.head.next
        return curr

    def delete_tail(self):
        if (self.head is None) or (self.head.next is None):
            return self.head

        curr = self.head
        while (curr.next.next is not None):
            curr = curr.next
        temp = curr.next.data
        curr.next = None
        return temp

    def is_empty(self):
        return self.head is None
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next;
            curr.next = prev;
            prev = curr
            curr = next_node
        self.head = prev

    def reverse_recursive(self, item):
        if item.next is None:
            self.head = item
            return
        self.reverse_recursive(item.next)
        temp = item.next
        temp.next = item
        item.next = None

    def print_list(self):
        curr = self.head
        while (curr is not None):
            print(curr.data)
            curr = curr.next

def main():
    A = Singly_Linked_List()
    print("Inserting 1st at Head")
    a1=input()
    A.insert_head(a1)
    print("Inserting 2nd at Head")
    a2=input()
    A.insert_head(a2)
    print("\nPrint List : ")
    A.print_list()
    print("\nInserting 1st at Tail")
    a3=input()    
    A.insert_tail(a3)
    print("Inserting 2nd at Tail")
    a4=input()
    A.insert_tail(a4)
    print("\nPrint List : ")
    A.print_list()
    print("\nDelete Head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.print_list()
    print("\nReverse Linked List")
    A.reverse()
    print("\nPrint List : ")
    A.print_list()
    print("\nReverse Linked List")
    A.reverse_recursive(A.head)
    print("\nPrint List : ")
    A.print_list()

if __name__ == '__main__':
    main()