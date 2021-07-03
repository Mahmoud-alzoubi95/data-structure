"""

input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

"""

def sumRootToLeaf(root):

    root_to_leaf = 0
    stack = [(root, 0) ]
    
    while stack:
        curr_number = stack.pop()
        
        if root is not None:
            curr_number = (curr_number << 1) | root.val
            # if it's a leaf, update root-to-leaf sum
            if root.left is None and root.right is None:
                root_to_leaf += curr_number
            else:
                stack.append((root.right, curr_number))
                stack.append((root.left, curr_number))
                    
    return root_to_leaf
