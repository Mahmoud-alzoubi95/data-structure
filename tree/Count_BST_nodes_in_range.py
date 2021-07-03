


# If current node is in range, theninclude it in count and recur forleft and right children of it.
# If current node is smaller than low,then recur for right child
# Else recur for left child

def getCount(root, low, high):
     
    # Base case
    if root == None:
        return 0
         
    # Special Optional case for improving
    # efficiency
    if root.data == high and root.data == low:
        return 1

    if root.data <= high and root.data >= low:
        return (1 + getCount(root.left, low, high) +
                    getCount(root.right, low, high))
 
    elif root.data < low:
        return getCount(root.right, low, high)
 
    else:
        return getCount(root.left, low, high)



# Function to perform level order traversal on the Tree and calculate the required sum

# declare variable to store the sum inside it
# Stores the nodes while performing level order traversal
# Push the root node into the queue
# Iterate until queue is empty
# Stores the front node of the queue
# If the value of the node lies in the given range
# Add it to sum
# If the left child is not NULL and exceeds low Insert into queue
# Return the resultant sum

def rangeSumBST(root, low, high):
    sum = 0
     
    # Base Case
    if (root == None):
        return 0

    q = enqeue()
    q.append(root)
 
    while (len(q) > 0):
 

        curr = q.popleft()
        # q.pop()

        if (curr.val >= low
            and curr.val <= high):

            sum += curr.val
 
        if (curr.left != None
            and curr.val > low):
 

            q.append(curr.left)

        if (curr.right != None
            and curr.val < high):

            q.append(curr.right)
 
    return sum