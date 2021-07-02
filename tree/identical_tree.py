# algorithm:
# create amethod with tow argumets that pass tow trees
# Return true if both trees are empty
# Return false if one is empty and other is not
# Create an empty queues/array for simultaneous traversals
# Enqueue/append Roots of trees in respective queues/arrays
# Get front nodes and compare them
# Remove front nodes from queues/array
# Enqueue/append left children of both nodes
# Enqueue/append left children of both nodes
# If one left child is empty and other is not
 # Right child code (Similar to left child code)



def identical(root1,root2):
    Q1 = []
    Q2 = []

    if not root1 and not root2:
        return False

    if root2 and not root1:
        return False

    if root1 and not root2:
        return False


    Q1.append(root1)
    Q2.append(root2)

    while len(Q1) > 0 and len(Q2):
        N1 = Q1.pop(0)
        N2 = Q2.pop(0)

        if N1 != N2:
            return False

        if N1.left and N2.left:
            Q1.append(N1.left)
            Q2.append(N2.left)

        elif N1.left or N2.right:
            return False

        if N1.right and N2.right:
            Q1.append(N1.right)
            Q2.appent(N2.right)

        elif N1.right or N2.right:
            return False
    return True
    