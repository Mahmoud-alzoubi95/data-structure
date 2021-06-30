class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binarytree:
    def __init__(self):
        self.root=None

    def preOrder(self):
        """
        root->left->right
        """
        output = []
        def walk(node):
            if node is None:
                return

            output.append(node.value)
            walk(node.left)
            walk(node.right)

        walk(self.root)
        return output
            
    def in_Order(self):
        """
        left->root->right
        """
        output = []
        def walk(node):
            if node is None:
                return
            walk(node.left)
            output.append(node.value)
            walk(node.right)

        walk(self.root)
        return output


    def postOrder(self):
        """
        left->right->root
        """
        output=[]
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            _walk(node.right)
            output.append(node.value)
        _walk(self.root)
        return output


    def maxvalue(self):
        self.max = self.root.value
        def walk(node):
            if not node:
                return "empty node"
            if node.value > self.max:
                self.max = node.value
            walk(self.root.right)
            walk(self.root.left)
        walk(self.root)    
        return self.max


    def Breadth_first(self,tree):
        temp = []
        result = []

        if self.root:
            temp.append(self.root)

            while temp:
                node = temp.pop(0)
                result.append(node.value)

                if node.left:
                    temp.append(node.left)

                if node.right:
                    temp.append(node.right)

            return result

        return "tree is empty"


class Binarysearchtree(Binarytree):

    def add(self,value):

        if self.root is None:
            self.root = Node(value)
        
        else:
            current = self.root
            while current:
                if current.value > value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left
                
                elif current.value < value:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right

    def contains(self,value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif current.value > value:
                if current.left == value:
                    return True
                current = current.left
            elif current.value < value:
                if current.right == value:
                    return True
                current = current.right
        return False

if __name__=="__main__":
    bt=Binarytree()
    bt.root = Node('1')
    bt.root.left = Node('2')
    bt.root.left.left = Node('3')
    bt.root.left.right = Node('4')
    bt.root.left.left.left = Node('5')
    bt.root.right = Node('7')
    bt.root.right.right = Node('8')
    bt.root.right.left = Node('9')
    print(bt.preOrder())
