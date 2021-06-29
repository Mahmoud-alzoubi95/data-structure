def rightRotate(head, k):
 
    # If the linked list is empty
    if (not head):
        return head
 
    # len is used to store length of the linked list
    # tmp will point to the last node after this loop
    tmp = head
    len = 1
 
    while (tmp.next != None):
        tmp = tmp.next
        len += 1
 
    # If k is greater than the size
    # of the linked list
    if (k > len):
        k = k % len
 
    # Subtract from length to convert
    # it into left rotation
    k = len - k
 
    # If no rotation needed then
    # return the head node
    if (k == 0 or k == len):
        return head
 
    # current will either point to
    # kth or None after this loop
    current = head
    cnt = 1
 
    while (cnt < k and current != None):
        current = current.next
        cnt += 1
 
    # If current is None then k is equal to the
    # count of nodes in the list
    # Don't change the list in this case
    if (current == None):
        return head
 
    # current points to the kth node
    kthnode = current
 
    # Change next of last node to previous head
    tmp.next = head
 
    # Change head to (k+1)th node
    head = kthnode.next
 
    # Change next of kth node to None
    kthnode.next = None
 
    # Return the updated head pointer
    return head