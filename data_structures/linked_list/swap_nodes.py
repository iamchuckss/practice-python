class Linked_List:
    def __init__(self):
        self.head = None

    def push(self, data):
       self.head = Node(data, self.head) 

    def swap_nodes(self, n1, n2):
        prev_1 = None
        prev_2 = None
        
        if self.head == None:
            return
        
        if n1 == n2:
            return

        # search for n1
        node_1 = self.head
        while node_1 is not None and node_1.data != n1:
            prev_1 = node_1
            node_1 = node_1.next
        
        # search for n2
        node_2 = self.head
        while node_2 is not None and node_2.data != n2:
            prev_2 = node_2
            node_2 = node_2.next

        if node_1 == None and node_2 == None:
            return

        # if prev_1 is None, then n1 is head
        if prev_1 == None:
            self.head = node_2;
        else:
            prev_1.next = node_2;

        # if prev_2 is None, then n2 is head
        if prev_2 == None:
            self.head = node_1;
        else:
            prev_2.next = node_1;

        # swap next nodes of n1 and n2
        temp = node_1.next
        node_1.next = node_2.next
        node_2.next = temp

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
        print()

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

if __name__ == '__main__':
    list = Linked_List()
    list.push(5)
    list.push(4)
    list.push(3)
    list.push(2)
    list.push(1)

    list.print_list()

    list.swap_nodes(1, 4)
    print("After swapping")
    list.print_list()