'''Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2'''

"output:"

"""   2     
     / \   
    1   3

    """
def searchBST(self, root, val):
    
    while(root):
        if root.val == val:
            return root
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    return root