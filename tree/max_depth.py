


def find_max_depth_of_binary_tree(root):
  if root ==None :
    return 0
  else :
    left =find_max_depth_of_binary_tree(root.left)
    right=find_max_depth_of_binary_tree(root.right)
    if left > right:
      return left+1
    else:
      return right+1
