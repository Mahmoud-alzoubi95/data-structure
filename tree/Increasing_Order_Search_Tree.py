

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
