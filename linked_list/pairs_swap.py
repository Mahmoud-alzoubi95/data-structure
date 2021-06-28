def pairWiseSwap(self):
 
        # If list is empty or with one node
        if (self.head is None or
            self.head.next is None):
            return
 
        # Initialize previous and current pointers
        prevNode = self.head
        currNode = self.head.next
 
        # Change head node
        self.head = currNode
 
        # Traverse the list
        while True:
            nextNode = currNode.next
             
            # Change next of current
            # node to previous node
            currNode.next = prevNode 
 
            # If next node is the last node
            if nextNode.next is None:
                prevNode.next = nextNode
                break
 
            # Change next of previous to
            # next of next
            prevNode.next = nextNode.next
 
            # Update previous and current nodes
            prevNode = nextNode
            currNode = prevNode.next






def pairWiseSwap(self, node):

    # If list is empty or with one node
    if node is None or node.next is None:
        return node

    # Store head of list after 2 nodes
    remaining = node.next.next

    # Change head
    newHead = node.next

    # Change next to second node
    node.next.next = node

    # Recur for remaining list and
    # change next of head
    node.next = self.pairWiseSwap(remaining)