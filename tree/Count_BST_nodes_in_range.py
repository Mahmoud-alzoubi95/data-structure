


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