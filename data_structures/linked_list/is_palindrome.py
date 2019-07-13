def is_palindrome(head):
    if not head:
        return True
    
    # split the list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # set second to first node after mid
    second = slow.next

    # reverse second part
    prev = None
    while second:
        temp_next = second.next
        second.next = prev
        prev = second
        second = temp_next
    
    # compare reversed second part and first part
    # second part has the same or one less node
    second_head = prev
    while second_head:
        if second_head.data != head.data:
            return False 
        second_head = second_head.next
        head = head.next
    return True


