
def invert_tree(root):
    if not root:
        return
    current = root.right
    root.right = root.left
    root.left = current 
    invert_tree(root.left)    
    invert_tree(root.right)
    return root      
