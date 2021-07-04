
# If both trees are empty, then they are mirror images

# root1 and root 1 the same tree

def isMirror(root1, root2):
   
    if root1 is None and root2 is None:
        return True
        
    if (root1 is not None and root2 is not None):
        if root1.value == root2.value:

            isMirror(root1.left, root2.right)
            isMirror(root1.right, root2.left)

            return "symmitric"
                    
    # If none of the above conditions is true then root1
    # and root2 are not mirror images

    return False