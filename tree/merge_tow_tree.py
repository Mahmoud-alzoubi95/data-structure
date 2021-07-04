
# Recursive Algorithm: 

# Check if both the tree nodes are NULL 
# If not, then update the value
# Recur for left subtrees
# Recur for right subtrees
# Return root of updated Tree

def mergetrees(t1,t2):
    if not t1 and t2:
        return t2

    if not t2 and t1:
        return t1

    if not t2 and not t1:
        return False

    t1.data+=t2.data
    t1.left = mergetrees(t1.left,t2.left)
    t1.right = mergetrees(t1.right,t2.right)
    return t1
    
    


# Create a stack
# Push the root nodes of both the trees onto the stack.
# While the stack is not empty 
# Pop a node pair from the top of the stack
# For every node pair removed, add the values corresponding to the two nodes and update the value of the corresponding node in the first tree
# If the left child of the first tree exists, push the left child(pair) of both the trees onto the stack.
# If the left child of the first tree doesn’t exist, append the left child of the second tree to the current node of the first tree
# Do same for right child pair as well.
# If both the current nodes are NULL, continue with popping the next nodes from the stack.
# Return root of updated Tree

def MergeTrees(t1, t2):
 
    if (not t1):
        return t2
    if (not t2):
        return t1
    s = []
     
    temp = snode(t1, t2)
     
    s.append(temp)
    n = None
     
    while (len(s) != 0):
     
        n = s[-1]
        s.pop()
         
        if (n.l == None or n.r == None):
            continue
             
        n.l.data += n.r.data
        if (n.l.left == None):
            n.l.left = n.r.left
            
        else:
            t=snode(n.l.left, n.r.left)
            s.append(t)
         
        if (n.l.right == None):
            n.l.right = n.r.right

        else:
            t=snode(n.l.right, n.r.right)
            s.append(t)
         
    return t1