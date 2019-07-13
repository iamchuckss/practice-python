def is_palindrome(head):
    if not head:
        return True
    
    # 1. split the list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # slow will stop at mid if odd, mid-1 if even
    # set second to first node after mid
    second = slow.next

    # 2. reverse second part
    prev = None
    while second:
        temp_next = second.next
        second.next = prev
        prev = second
        second = temp_next
    
    # 3. compare reversed second part and first part
    # second part has the same or one less node
    second_head = prev
    while second_head:
        if second_head.data != head.data:
            return False 
        second_head = second_head.next
        head = head.next
    return True

def is_palindrome_stack(head):
    # True if list has only less than 2 nodes
    if head == None or head.next == None:
        return True

    # 1. split the list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # set second to first node after mid
    second = slow.next
    # 2. push the second half into the stack
    stack = []
    while second:
        stack.append(second)
        second = second.next
    
    # 3. comparison
    while stack:
        if stack.pop().data != head.data:
            return False
        head = head.next

    return True



    
    

    


