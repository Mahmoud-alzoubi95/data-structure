"""
Given the root of a binary search tree, rearrange the tree in in-order so that the
 leftmost node in the tree is now the root of the tree, and every node has no left child
 and only one right child.
 """

def increasingBST(root):
    def inorder(node):
        if node:
            inorder(node.left)
            node.left = None
            cur.right = node
            cur = node
            inorder(node.right)

    ans = cur = Node(None)
    inorder(root)
    return ans.right
